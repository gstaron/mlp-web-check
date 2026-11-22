# mlp-web-check

Kontrola nefunkčních odkazů na www.mlp.cz (22. 11. 2026).

- `report/index.html` + `report/report.json` – přehled chyb s návodem na opravu
- `report/opravy.csv` – stejný seznam jako tabulka (oddělovač `;`, UTF-8), jeden řádek = jedna stránka a jeden chybný odkaz
- `data/` – surová data z procházení

Postup: `crawler.py data` → `analyze.py data` → `check_external.py data` → `recheck_external.py data`
→ `curl_verify.sh < data/ambiguous.txt > data/external3.tsv` → `check_listings.py data`
→ `build_report.py data report` (→ `verify_suggestions.py data report` → `build_report.py data report`).
