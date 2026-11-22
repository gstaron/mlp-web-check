#!/usr/bin/env python3
"""Turn crawler output (data/pages.jsonl, data/checks.jsonl) into findings.json."""
import json
import re
import sys
from collections import defaultdict, Counter
from urllib.parse import urlsplit, unquote

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from crawler import normalize, INTERNAL_HOSTS  # noqa: E402

D = sys.argv[1] if len(sys.argv) > 1 else "data"
pages = [json.loads(l) for l in open(f"{D}/pages.jsonl")]
checks = {}
try:
    for l in open(f"{D}/checks.jsonl"):
        r = json.loads(l)
        checks[r["url"]] = r["chain"]
except FileNotFoundError:
    pass


def malformed_reason(raw):
    """Static problems visible in the href itself."""
    s = raw.strip()
    if raw != s:
        return "mezera na začátku/konci odkazu"
    if not s:
        return "prázdný odkaz (href=\"\")"
    low = s.lower()
    if re.match(r"^(https?:)?//?(https?:)", low) or re.match(r"^https?://https?", low) or "http//" in low or "https//" in low:
        return "zdvojený nebo poškozený protokol (http://http…)"
    if re.match(r"^https?:/[^/]", low) or re.match(r"^https?:[^/]", low):
        return "chybí lomítko za protokolem"
    if re.match(r"^www\.", low):
        return "chybí https:// – prohlížeč to bere jako relativní adresu na mlp.cz"
    if re.match(r"^[a-z0-9.-]+\.(cz|com|org|eu|sk|net)(/|$)", low):
        return "chybí https:// – prohlížeč to bere jako relativní adresu na mlp.cz"
    if low.startswith(("file:", "c:\\", "\\\\")):
        return "odkaz na lokální soubor (file:/C:\\)"
    if re.search(r"localhost|127\.0\.0\.1|/admin/|/node/\d+/edit", low):
        return "odkaz do administrace / localhost"
    if low.startswith("mailto:"):
        addr = unquote(s[7:].split("?")[0])
        if not re.fullmatch(r"[^@\s,;]+@[^@\s,;]+\.[a-z]{2,}", addr, re.I):
            return "chybná e-mailová adresa v mailto:"
        return None
    if low.startswith("tel:"):
        if not re.fullmatch(r"tel:\+?[\d\s()./-]+", low):
            return "chybné telefonní číslo v tel:"
        return None
    if low.startswith(("javascript:", "#", "data:")):
        return None
    if s.startswith("//") and "." not in s[2:].split("/")[0]:
        return "odkaz na interní síťový disk / soubor v počítači redakce (//SERVER/...)"
    parts = urlsplit(s)
    if parts.scheme in ("http", "https") and parts.hostname and "." not in parts.hostname:
        return "neplatná doména – chybí www.mlp.cz (např. https://katalog/...)"
    if parts.scheme and parts.scheme not in ("http", "https", "mailto", "tel", "javascript", "data"):
        return f"neznámý protokol „{parts.scheme}:“ v adrese"
    internal = not parts.hostname or parts.hostname in INTERNAL_HOSTS
    dpath = unquote(parts.path)
    if re.search(r"/[,;.:)(]", dpath) or re.search(r"[,;:(]$", dpath) or (internal and re.search(r"[,;(]", dpath)):
        return "v adrese je přilepená interpunkce/text (např. „,které“)"
    if " " in dpath.strip() or "%20" in parts.netloc:
        return "mezera uvnitř adresy"
    if re.search(r'["<>]', parts.path + parts.query):
        return "uvozovky nebo HTML znaky v adrese"
    return None


def final_status(chain):
    last = chain[-1]
    st = last.get("status")
    if st == "external":
        return "redirect-external", last["url"]
    if isinstance(st, int) and st >= 500 and last.get("retry_status") and last["retry_status"] < 500:
        return f"{st} (dočasně, při opakování {last['retry_status']})", last["url"]
    return st, last["url"]


findings = []  # one per (page, link)
external_hosts = Counter()
external_links = defaultdict(set)
for p in pages:
    base = p.get("final") or p["url"]
    for l in p["links"]:
        raw = l["raw"]
        reason = malformed_reason(raw)
        n = normalize(base, raw) if raw is not None else None
        host = urlsplit(n).hostname if n else None
        status = None
        final = None
        redirects = 0
        if n and host in INTERNAL_HOSTS and n in checks:
            chain = checks[n]
            status, final = final_status(chain)
            redirects = sum(1 for c in chain if isinstance(c.get("status"), int) and 300 <= c["status"] < 400)
        elif n and host and host not in INTERNAL_HOSTS:
            external_hosts[host] += 1
            external_links[n].add(p["url"])
        broken = (isinstance(status, int) and status >= 400) or status is None and n in checks
        if reason or broken or (isinstance(status, str) and status[:1] == "5"):
            findings.append({
                "page": p["url"],
                "page_title": p.get("title", ""),
                "region": l["region"],
                "tag": l["tag"],
                "text": l["text"],
                "href": raw,
                "resolved": n,
                "status": status,
                "final": final,
                "redirects": redirects,
                "malformed": reason,
            })

json.dump({
    "pages_crawled": len(pages),
    "pages_status": Counter(str(p["status"]) for p in pages),
    "internal_checked": len(checks),
    "findings": findings,
    "external_hosts": external_hosts.most_common(),
    "external_links": {k: sorted(v) for k, v in external_links.items()},
}, open(f"{D}/findings.json", "w"), ensure_ascii=False, indent=1)

print("pages:", len(pages), "checked:", len(checks), "findings:", len(findings))
c = Counter((f["malformed"] or str(f["status"])) for f in findings)
for k, v in c.most_common():
    print(f"  {v:4}  {k}")
print("external hosts:", len(external_hosts), "external urls:", len(external_links))
