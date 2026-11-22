#!/usr/bin/env python3
"""Combine crawl results into a prioritised fix list (report/report.json, report/opravy.csv).

Inputs (data/): pages.jsonl, checks.jsonl, findings.json, external.jsonl,
external2.jsonl, external3.tsv, listings.json (optional), suggestions.json (optional).
"""
import csv
import difflib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import urlsplit, unquote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawler import normalize, INTERNAL_HOSTS  # noqa: E402

D = sys.argv[1] if len(sys.argv) > 1 else "data"
OUT = sys.argv[2] if len(sys.argv) > 2 else "report"
os.makedirs(OUT, exist_ok=True)

pages = [json.loads(l) for l in open(f"{D}/pages.jsonl")]
page_title = {p["url"]: p.get("title", "").replace(" | Městská knihovna v Praze", "") for p in pages}
checks = {}
for l in open(f"{D}/checks.jsonl"):
    r = json.loads(l)
    checks[r["url"]] = r["chain"]
findings = json.load(open(f"{D}/findings.json"))

sitemap = [p["url"] for p in pages if p.get("status") == 200]
sm_paths = {}
for u in sitemap:
    path = urlsplit(u).path.rstrip("/")
    sm_paths[path] = u
by_slug = defaultdict(list)
for path, u in sm_paths.items():
    by_slug[path.rsplit("/", 1)[-1]].append(u)
core_paths = {}
for path, u in sm_paths.items():
    core = re.sub(r"^/(cz|en)(?=/|$)", "", path)
    if path.startswith("/cz") or core not in core_paths:
        core_paths[core] = u

# ---------------------------------------------------------------- external
ext = {}
for l in open(f"{D}/external.jsonl"):
    r = json.loads(l)
    ext[r["url"]] = r
if os.path.exists(f"{D}/external2.jsonl"):
    for l in open(f"{D}/external2.jsonl"):
        r = json.loads(l)
        ext[r["url"]].update(status2=r["status"], error2=r.get("error"), final2=r.get("final"))
curl3 = {}
if os.path.exists(f"{D}/external3.tsv"):
    for line in open(f"{D}/external3.tsv"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 3:
            curl3[parts[0]] = (parts[1], parts[2], parts[3] if len(parts) > 3 else "")

OLD_MLP = {"old.mlp.cz", "demo.mlp.cz", "wwwbeta.mlp.cz", "l.mlp.cz", "web2.mlp.cz", "web3.mlp.cz"}
BOT_BLOCK = {400, 401, 403, 418, 429, 999}


def external_verdict(u):
    """Return (category, note) for an external URL or None when it is fine / unverifiable."""
    r = ext.get(u)
    if not r:
        return None
    host = urlsplit(u).hostname or ""
    st = r.get("status2", r.get("status"))
    if r.get("status") == 200 or st == 200:
        return None
    c = curl3.get(u)
    if c and c[0] in ("200", "301", "302") and c[1] == "0":
        return None
    if st in (404, 410):
        return ("external_404", f"Stránka na cizím webu vrací chybu {st} (neexistuje).")
    if st in BOT_BLOCK or (c and c[0] in ("401", "403", "418", "429")):
        return None  # web blocks automated checks, cannot judge
    err = (r.get("error2") or r.get("error") or "") + " " + (c[2] if c else "")
    if host in OLD_MLP:
        return ("old_domain", f"Starý/testovací web knihovny {host} už nefunguje.")
    if c and c[1] == "6" or "esolve" in err:
        return ("external_dead", "Doména neexistuje (nelze ji najít v DNS) – web zřejmě zanikl.")
    if u.startswith("http://") and "SSL" in err:
        return ("external_http", "Web nefunguje přes zabezpečené https a přes http jsme ho ověřit nemohli – zkontrolujte ručně.")
    if st is not None and st >= 500:
        return ("external_dead", f"Cizí web vrací chybu serveru {st}.")
    if "502" in err or "reset" in err or "SSL" in err or "imeout" in err:
        return ("external_dead", "Web se opakovaně nepodařilo načíst (nedostupný server / chybný certifikát) – ověřte ručně, pravděpodobně zanikl.")
    return None


# ---------------------------------------------------------------- suggestions
def verify(u):
    """True/False when the crawl knows the URL, None otherwise."""
    if u in checks:
        last = checks[u][-1]
        return isinstance(last.get("status"), int) and last["status"] < 400
    if u.rstrip("/") in {s.rstrip("/") for s in sitemap}:
        return True
    return None


def suggest_internal(path):
    p = unquote(path).rstrip("/")
    core = re.sub(r"^/(cz|en)(?=/|$)", "", p)
    if core in core_paths:
        return core_paths[core]
    slug = p.rsplit("/", 1)[-1]
    if slug and slug in by_slug and len(by_slug[slug]) == 1:
        return by_slug[slug][0]
    m = difflib.get_close_matches(core, list(core_paths), n=1, cutoff=0.82)
    if m:
        return core_paths[m[0]]
    return None


def fix_malformed(raw, reason):
    s = raw.strip()
    if "síťový disk" in reason:
        rest = re.sub(r"^//[^/]+", "", s)
        mail = re.search(r"[\w.+-]+@[\w-]+\.[\w.]+$", unquote(rest))
        if mail:
            return f"mailto:{mail.group(0)}", "Do odkazu se omylem vložila cesta k souboru na počítači redakce. Správně má být e-mailový odkaz."
        return "https://www.mlp.cz" + rest, "Do odkazu se omylem dostala adresa interního serveru „OREL“ (odkaz zkopírovaný z interního prostředí). Smažte začátek „//OREL“."
    if "neplatná doména" in reason:
        m = re.match(r"https?://([^/]+)(/.*)?$", s)
        host, rest = m.group(1), (m.group(2) or "/")
        if re.fullmatch(r"[a-z0-9-]+", host) and host not in ("z",):
            return "https://www.mlp.cz/" + host + rest, "V odkazu chybí doména – místo „https://pobocky/…“ má být „https://www.mlp.cz/pobocky/…“ (nebo jen „/pobocky/…“)."
        if host == "z":
            return "https://www.mlp.cz" + rest, "Odkaz začíná „https://z/“ – zbytek po zkrácení adresy. Smažte „https://z“."
        return None, "Místo adresy je v odkazu vložen text (název videa). Doplňte skutečnou adresu, nebo odkaz odstraňte."
    if "mezera na začátku" in reason:
        return s, "Odkaz začíná nebo končí mezerou. Ve většině prohlížečů funguje, ale je to chyba – mezeru smažte (u adres bez https:// a s mezerou na začátku odkaz nefunguje vůbec)." if not s.startswith("www.") else "Odkaz začíná mezerou a chybí mu „https://“, takže vede na neexistující stránku na mlp.cz."
    if "interpunkce" in reason:
        fixed = re.sub(r"/[,;.(][^/]*$", "/", s)
        fixed = re.sub(r"[,;:(]+$", "", fixed)
        return fixed, "Na konec adresy se přilepil kus textu nebo interpunkce. Odstraňte ho."
    if "mezera uvnitř" in reason:
        m = re.search(r"https?:/+(.*)$", unquote(s))
        if m:
            return "https://" + m.group(1).lstrip("/"), "Na začátku odkazu je přilepené „: “ a chybí jedno lomítko. Opravte na čistou adresu."
        return None, "V adrese je mezera."
    if "telefon" in reason:
        return None, "Odkaz „tel:+“ neobsahuje číslo. Doplňte telefonní číslo nebo odkaz odstraňte."
    if "mailto" in reason:
        return None, "Odkaz „mailto:“ neobsahuje e-mailovou adresu. Doplňte ji nebo odkaz odstraňte."
    if "chybí https" in reason:
        return "https://" + s, "Odkaz nemá „https://“, takže ho prohlížeč bere jako stránku na mlp.cz a skončí chybou 404."
    return None, reason


def internal_problem(u, status, final):
    path = urlsplit(final or u).path
    q = urlsplit(final or u).query
    sug = None
    if "/noRW_photodisplay/" in path:
        return "image", "Obrázek ze starého webu knihovny už neexistuje (adresy /noRW_photodisplay/ po přechodu na nový web nefungují). Nahrajte obrázek znovu do Médií a vložte ho, nebo obrázek z textu odstraňte.", None
    if "/dokumenty/" in path and "act=get" in q:
        return "document", "Odkaz na dokument ze starého webu (/cz/dokumenty/?act=get…) už nefunguje. Nahrajte dokument do Médií a odkaz nahraďte, případně odkaz odstraňte.", None
    if path.startswith("/sites/") and "/files/" in path:
        return "document", "Soubor (PDF/obrázek) na serveru neexistuje – byl smazán nebo přejmenován. Nahrajte ho znovu a odkaz aktualizujte.", None
    if status == 403:
        if "/novinky/" in path or "/akce/" in path:
            return "unpublished", "Odkaz vede na nepublikovaný (skrytý) článek – návštěvník uvidí „Přístup odepřen“. Článek publikujte, nebo odkaz odstraňte.", None
        return "unpublished", "Stránka vrací „Přístup odepřen“ (403) – zřejmě není publikovaná.", None
    if isinstance(status, int) and status >= 500:
        return "server", f"Server vrací chybu {status}. Nutno předat správci webu (technická chyba).", None
    if re.match(r"^/(cz/)?akce/[^/]+/\d+", path):
        sug = None
        return "event", "Akce byla smazána (nebo změnila adresu). Odkaz odstraňte nebo nahraďte odkazem na aktuální akci.", sug
    if re.match(r"^/(cz/|en/)?katalog/", path) or path.startswith("/davka/"):
        if path.startswith("/davka/"):
            return "catalog", "Chybí „/katalog“ na začátku adresy (správně /katalog/davka/…).", "https://www.mlp.cz/katalog" + path + ("?" + q if q else "")
        return "catalog", "Záznam v katalogu neexistuje (titul vyřazen nebo se změnilo ID). Vyhledejte titul v katalogu a odkaz aktualizujte, nebo ho odstraňte.", None
    sug = suggest_internal(path)
    if re.fullmatch(r"/[a-z0-9-]+/?", path) and not sug:
        return "old_url", "Krátká adresa ze starého webu (např. www.mlp.cz/ukrajina) přestala fungovat. Buď ji správce obnoví jako přesměrování (modul Redirect), nebo odkaz nahraďte plnou adresou.", None
    return "old_url", "Stránka s touto adresou neexistuje – nejčastěji jde o adresu ze starého webu, která se po redesignu změnila. Nahraďte ji novou adresou." + (" Navrhujeme níže uvedenou (ověřte, že jde o správnou stránku)." if sug else ""), sug


CAT_META = {
    "lang_switch": ("Přepínač jazyka EN vede na 404", 1),
    "malformed": ("Chybně zapsaný odkaz", 1),
    "server": ("Chyba serveru (5xx)", 1),
    "old_url": ("Stará / neexistující adresa na mlp.cz", 1),
    "unpublished": ("Odkaz na nepublikovaný článek", 1),
    "document": ("Chybějící dokument / soubor", 1),
    "catalog": ("Neexistující záznam v katalogu", 2),
    "event": ("Smazaná akce", 2),
    "image": ("Nefunkční obrázek ze starého webu", 2),
    "old_domain": ("Odkaz na starý / testovací web knihovny", 1),
    "external_404": ("Cizí web: stránka neexistuje (404)", 2),
    "external_dead": ("Cizí web nedostupný / zaniklý", 3),
    "external_http": ("Cizí web bez https – ověřit ručně", 3),
    "listing_empty": ("Odkaz na prázdný výpis akcí", 3),
}

items = {}
seen_layout = set()
for f in findings["findings"]:
    raw = f["href"]
    if f["region"] == "layout":
        key = ("layout", raw)
        if key in seen_layout:
            continue
        seen_layout.add(key)
    if f["malformed"]:
        sug, fix = fix_malformed(raw, f["malformed"])
        cat = "malformed"
        problem = f["malformed"]
    elif f["region"] == "layout" and f["text"] in ("EN", "CZ", "CS") and f["status"] == 404:
        cat, sug, problem = "lang_switch", None, "Přepínač jazyka vede na neexistující stránku (404)"
        fix = ("Stránka nemá jazykovou verzi, ale přepínač jazyka v hlavičce přesto odkazuje na /en/… se stejnou cestou. "
               "Správce webu: u stránek bez překladu přepínač skrýt, nebo ho nasměrovat na anglickou úvodní stránku https://www.mlp.cz/en "
               "(v Drupalu blok Language switcher / šablona hlavičky). Alternativně doplnit anglické překlady.")
        raw = "(přepínač jazyka EN)"
    elif "@" in raw and not raw.strip().lower().startswith(("mailto:", "http")):
        cat, sug, problem = "malformed", "mailto:" + raw.strip(), "E-mailová adresa bez „mailto:“"
        fix = "Odkaz obsahuje jen e-mailovou adresu bez „mailto:“, takže ho prohlížeč otevře jako neexistující stránku na mlp.cz. Doplňte „mailto:“ před adresu."
    else:
        cat, fix, sug = internal_problem(f["resolved"], f["status"] if isinstance(f["status"], int) else 500, f["final"])
        problem = f"Chyba {f['status']}"
    key = (f["page"], raw)
    it = items.get(key)
    if it:
        it["count"] += 1
        continue
    items[key] = {
        "cat": cat, "page": f["page"], "title": page_title.get(f["page"], ""), "region": f["region"],
        "tag": f["tag"], "text": f["text"], "href": raw, "problem": problem, "fix": fix,
        "suggestion": sug, "count": 1,
    }

# external
for p in pages:
    base = p.get("final") or p["url"]
    for l in p["links"]:
        n = normalize(base, l["raw"]) if l["raw"] is not None else None
        if not n:
            continue
        host = urlsplit(n).hostname or ""
        if host in INTERNAL_HOSTS or "." not in host:
            continue
        v = external_verdict(n)
        if not v:
            continue
        key = (p["url"], l["raw"])
        if key in items:
            items[key]["count"] += 1
            continue
        if l["region"] == "layout":
            if ("layout", l["raw"]) in seen_layout:
                continue
            seen_layout.add(("layout", l["raw"]))
        items[key] = {
            "cat": v[0], "page": p["url"], "title": page_title.get(p["url"], ""), "region": l["region"],
            "tag": l["tag"], "text": l["text"], "href": l["raw"], "problem": v[1],
            "fix": {"external_404": "Najděte na daném webu novou adresu stránky, nebo odkaz odstraňte.",
                    "external_dead": "Ověřte ručně v prohlížeči. Pokud web nefunguje, odkaz odstraňte nebo nahraďte.",
                    "external_http": "Otevřete odkaz v prohlížeči; pokud nefunguje, odkaz odstraňte.",
                    "old_domain": "Nahraďte odkazem na odpovídající stránku nového webu (www.mlp.cz), nebo odkaz odstraňte. Obrázky nahrajte znovu do Médií."}[v[0]],
            "suggestion": None, "count": 1,
        }

# listings
if os.path.exists(f"{D}/listings.json"):
    for u, r in json.load(open(f"{D}/listings.json")).items():
        if r.get("status") and r["status"] >= 500:
            cat, prob = "server", f"Výpis akcí vrací chybu serveru {r['status']}."
        elif r.get("items") == 0:
            cat, prob = "listing_empty", "Odkaz vede na výpis akcí, který je momentálně prázdný – návštěvník uvidí jen nadpis „Akce“ bez jakéhokoli vysvětlení."
        else:
            continue
        for page, text in r["refs"]:
            key = (page, u)
            if key in items:
                continue
            items[key] = {
                "cat": cat, "page": page, "title": page_title.get(page, ""), "region": "content", "tag": "a",
                "text": text, "href": u, "problem": prob,
                "fix": "Redakčně: odkaz zobrazovat jen když nějaká akce existuje, nebo text změnit (např. „Výstavy v Artotéce“). Technicky (správce webu): doplnit do pohledu (View) „Akce“ text pro prázdný výsledek, např. „Momentálně zde neprobíhá žádná akce/výstava. Podívejte se na všechny akce.“",
                "suggestion": None, "count": 1,
            }

# verify suggestions with crawl data / suggestions.json
sv = {}
if os.path.exists(f"{D}/suggestions.json"):
    sv = json.load(open(f"{D}/suggestions.json"))
for it in items.values():
    s = it["suggestion"]
    if s and not s.startswith(("http", "mailto:", "tel:")) and s.strip().startswith("/"):
        s = it["suggestion"] = "https://www.mlp.cz" + s.strip()
    if s and s.startswith("http") and urlsplit(s).hostname in INTERNAL_HOSTS:
        ok = verify(normalize(s, s) or s)
        if ok is None:
            ok = sv.get(s)
        it["suggestion_ok"] = ok
    else:
        it["suggestion_ok"] = None

# group identical broken links (same href + category) across pages
grouped = {}
for it in items.values():
    k = (it["cat"], it["href"].strip())
    g = grouped.get(k)
    if g is None:
        g = dict(it)
        g["pages"] = []
        g["texts"] = []
        grouped[k] = g
    g["pages"].append({"url": it["page"], "title": it["title"], "region": it["region"]})
    if it["text"] and it["text"] not in g["texts"]:
        g["texts"].append(it["text"])
rows = []
for g in grouped.values():
    g["n_pages"] = len(g["pages"])
    g["text"] = " / ".join(g["texts"][:3])
    g["page"] = g["pages"][0]["url"]
    g["title"] = g["pages"][0]["title"]
    del g["texts"], g["count"]
    g["cat_label"], g["priority"] = CAT_META[g["cat"]]
    rows.append(g)
rows.sort(key=lambda r: (r["priority"], r["cat"], -r["n_pages"], r["page"]))

summary = {
    "pages": len(pages),
    "internal_checked": len(checks),
    "external_checked": len(ext),
    "by_cat": Counter(r["cat"] for r in rows),
    "pages_affected": len({p["url"] for r in rows for p in r["pages"]}),
    "occurrences": sum(r["n_pages"] for r in rows),
    "total": len(rows),
    "http_internal": sum(1 for f in findings["findings"] if (f["href"] or "").startswith("http://www.mlp.cz")),
}
json.dump({"summary": summary, "cats": {k: v[0] for k, v in CAT_META.items()}, "rows": rows},
          open(f"{OUT}/report.json", "w"), ensure_ascii=False)
with open(f"{OUT}/opravy.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh, delimiter=";")
    w.writerow(["Priorita", "Typ chyby", "Stránka", "Název stránky", "Umístění", "Text odkazu", "Chybný odkaz", "Problém", "Jak opravit", "Navržená oprava", "Návrh ověřen", "Stejný odkaz na dalších stránkách"])
    for r in rows:
        for p in r["pages"]:
            w.writerow([r["priority"], r["cat_label"], p["url"], p["title"], "obsah" if p["region"] == "content" else "hlavička/patička",
                        r["text"], r["href"], r["problem"], r["fix"], r["suggestion"] or "",
                        {True: "ano", False: "NE", None: ""}[r["suggestion_ok"]], r["n_pages"] - 1])
print(json.dumps(summary, ensure_ascii=False, indent=1))
