#!/usr/bin/env python3
"""Render report/report.json as PREHLED.md (readable on GitHub) and report/opravy.xlsx."""
import json
import sys
from collections import Counter, OrderedDict

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

REP = sys.argv[1] if len(sys.argv) > 1 else "report"
d = json.load(open(f"{REP}/report.json"))
rows, cats, s = d["rows"], d["cats"], d["summary"]

PRI = {1: "1 – opravit hned", 2: "2 – opravit", 3: "3 – ověřit ručně"}
CAT_INTRO = {
    "lang_switch": "Na českých stránkách bez anglického překladu vede přepínač „EN“ v hlavičce na `/en/…` se stejnou cestou, což končí chybou 404. **Oprava pro správce webu:** u stránek bez překladu přepínač skrýt, nebo ho nasměrovat na https://www.mlp.cz/en.",
    "malformed": "Adresa je zapsaná chybně (přilepený text, chybějící doména, adresa interního serveru „//OREL/“, mezery). Stačí odkaz opravit v editoru – návrh správné adresy je v tabulce.",
    "old_url": "Adresa na novém webu neexistuje (většinou adresa ze starého webu). Nahraďte ji navrženou adresou, nebo přes modul Redirect nastavte přesměrování.",
    "old_domain": "Odkazy na starý / testovací web knihovny (old.mlp.cz, demo.mlp.cz, wwwbeta.mlp.cz, l.mlp.cz), který už nefunguje. Nahraďte odkazem na stránku na www.mlp.cz, nebo odkaz odstraňte.",
    "document": "Odkazovaný dokument (PDF) neexistuje – hlavně staré odkazy `/cz/dokumenty/?act=get…`. Nahrajte dokument do Médií a odkaz nahraďte, nebo ho odstraňte.",
    "unpublished": "Odkaz vede na nepublikovaný článek, návštěvník uvidí „Přístup odepřen“. Článek publikujte, nebo odkaz odstraňte.",
    "external_404": "Stránka na cizím webu byla zrušena nebo přesunuta. Najděte novou adresu, nebo odkaz odstraňte.",
    "image": "Obrázky vložené ze starého webu (`/noRW_photodisplay/…`) se nezobrazují. Nahrajte je znovu do Médií, nebo je z článku odstraňte.",
    "catalog": "Záznam v katalogu neexistuje. Vyhledejte titul znovu a odkaz aktualizujte.",
    "event": "Akce byla smazána. Odkaz odstraňte nebo nahraďte.",
    "external_dead": "Cizí web se opakovaně (třikrát) nepodařilo načíst – pravděpodobně zanikl. Ověřte v prohlížeči a případně odkaz odstraňte.",
    "external_http": "Cizí web nemá zabezpečené https a přes http ho nešlo ověřit. Ověřte v prohlížeči.",
    "listing_empty": "Odkaz vede na výpis akcí, který je teď prázdný a návštěvník vidí jen nadpis „Akce“. **Oprava pro správce webu:** doplnit do pohledu „Akce“ text pro prázdný výsledek (např. „Momentálně neprobíhá žádná výstava“).",
}


def md(t, n=None):
    t = (t or "").replace("|", "\\|").replace("\n", " ").strip()
    if n and len(t) > n:
        t = t[: n - 1] + "…"
    return t


def short(u):
    return u.replace("https://www.mlp.cz", "")


def page_links(r, n=3):
    out = [f"[{md(p['title'] or short(p['url']), 60)}]({p['url']})" for p in r["pages"][:n]]
    if r["n_pages"] > n:
        out.append(f"a dalších {r['n_pages'] - n}")
    return "<br>".join(out)


order = OrderedDict()
for r in rows:
    order.setdefault(r["cat"], []).append(r)
cat_order = sorted(order, key=lambda c: (order[c][0]["priority"], -len(order[c])))

L = []
L.append("# Nefunkční odkazy na www.mlp.cz\n")
L.append(f"Kontrola proběhla 22. 11. 2026. Prošli jsme **{s['pages']:,} stránek** ze sitemapy a ověřili "
         f"**{s['internal_checked'] + s['external_checked']:,} adres** (odkazy i obrázky). "
         f"Nalezeno **{s['total']} chybných odkazů na {s['pages_affected']} stránkách**.\n".replace(",", " "))
L.append("- Celý seznam jako tabulka pro Excel: [`report/opravy.xlsx`](report/opravy.xlsx) "
         "(jeden řádek = jedna stránka a jeden chybný odkaz, s filtry podle typu a priority).")
L.append("- Jak kontrola proběhla: viz [konec stránky](#jak-kontrola-proběhla).\n")

L.append("## Souhrn\n")
L.append("| Typ chyby | Priorita | Počet |")
L.append("|---|---|---:|")
for c in cat_order:
    L.append(f"| [{cats[c]}](#{c.replace('_', '-')}) | {order[c][0]['priority']} | {len(order[c])} |")
L.append("\nPriorita 1 = odkaz vede na chybovou stránku nebo jde o chybu celého webu. Priorita 3 = ověřit ručně.\n")

for c in cat_order:
    items = order[c]
    L.append(f'<a id="{c.replace("_", "-")}"></a>\n')
    L.append(f"## {cats[c]} ({len(items)})\n")
    L.append(f"Priorita {items[0]['priority']}. {CAT_INTRO.get(c, '')}\n")
    if c == "lang_switch":
        r = items[0]
        L.append(f"Týká se {r['n_pages']} stránek, např. " + ", ".join(f"[{short(p['url'])}]({p['url']})" for p in r["pages"][:5]) + ". Úplný seznam je v tabulce `opravy.xlsx`.\n")
        continue
    with_sug = any(r.get("suggestion") for r in items)
    hdr = "| Kde | Text odkazu | Chybný odkaz |" + (" Navržená oprava |" if with_sug else "")
    L.append(hdr)
    L.append("|---|---|---|" + ("---|" if with_sug else ""))
    for r in items:
        href = md(r["href"], 110)
        cells = [page_links(r), md(r["text"], 60), f"`{href}`" if href else ""]
        if with_sug:
            sug = r.get("suggestion") or ""
            if sug:
                sug = f"`{md(sug, 110)}`" + (" ✓ ověřeno" if r.get("suggestion_ok") else "")
            elif c == "malformed":
                sug = md(r["fix"], 120)
            cells.append(sug)
        L.append("| " + " | ".join(cells) + " |")
    L.append("")

L.append("## Jak kontrola proběhla\n")
L.append(
    "- Kontrolu jsem připravil a spustil s pomocí AI asistenta Claude (Anthropic): napsal skripty, které jsou v tomto repozitáři, "
    "a výsledky roztřídil. Vybrané nálezy byly ověřeny i v běžném prohlížeči.\n"
    "- Prošli jsme všechny stránky ze sitemapy (`/default/sitemap.xml`) a ověřili každý odkaz a obrázek na nich. Stránky katalogu jsme samostatně neprocházeli.\n"
    "- Server mlp.cz jsme zatěžovali nejvýše jedním požadavkem za sekundu podle `robots.txt`.\n"
    "- Odkazy v hlavičce a patičce (stejné na všech stránkách) uvádíme jen jednou.\n"
    "- Facebook, Instagram, YouTube a další weby automatické kontroly blokují; ty mezi chyby nepočítáme.\n"
    "- Cizí weby, které se nenačetly, jsme zkoušeli třikrát; i tak mohou být jen dočasně nedostupné (proto priorita 3).\n"
    "- Navržené opravy s označením „ověřeno“ fungují. U ostatních ověřte, že vedou na správnou stránku.\n"
    "- Kontrolu lze zopakovat skripty v repozitáři (postup je v souboru [`README.md`](README.md)).\n"
)
open("PREHLED.md", "w").write("\n".join(L))

# ---------------------------------------------------------------- Excel
wb = Workbook()
ws = wb.active
ws.title = "Opravy"
head = ["Priorita", "Typ chyby", "Stránka", "Název stránky", "Umístění", "Text odkazu", "Chybný odkaz",
        "Problém", "Jak opravit", "Navržená oprava", "Návrh ověřen", "Stejný odkaz na dalších stránkách", "Opraveno"]
ws.append(head)
for r in sorted(rows, key=lambda r: (r["priority"], cat_order.index(r["cat"]))):
    for p in r["pages"]:
        ws.append([PRI[r["priority"]], r["cat_label"], p["url"], p["title"],
                   "obsah" if p["region"] == "content" else "hlavička/patička",
                   r["text"], r["href"], r["problem"], r["fix"], r.get("suggestion") or "",
                   {True: "ano", False: "NE", None: ""}[r.get("suggestion_ok")], r["n_pages"] - 1, ""])
widths = [16, 30, 48, 34, 14, 30, 50, 30, 60, 50, 10, 12, 10]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w
fill = PatternFill("solid", fgColor="1F5F57")
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = fill
    cell.alignment = Alignment(wrap_text=True, vertical="top")
for row in ws.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "C2"
ws.auto_filter.ref = ws.dimensions

ws2 = wb.create_sheet("Souhrn")
ws2.append(["Typ chyby", "Priorita", "Počet chybných odkazů", "Počet výskytů"])
for c in cat_order:
    ws2.append([cats[c], order[c][0]["priority"], len(order[c]), sum(r["n_pages"] for r in order[c])])
for cell in ws2[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = fill
ws2.column_dimensions["A"].width = 40
for col in "BCD":
    ws2.column_dimensions[col].width = 20
wb.save(f"{REP}/opravy.xlsx")
print("rows:", ws.max_row - 1, "cats:", Counter(r["cat"] for r in rows).most_common(3))
