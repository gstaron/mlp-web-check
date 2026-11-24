# Kontrola odkazů na www.mlp.cz

Seznam nefunkčních odkazů na webu Městské knihovny v Praze s návrhy oprav (kontrola z 22. 11. 2026).

**➜ [Přehled chyb – PREHLED.md](PREHLED.md)**
**➜ [Tabulka pro Excel – report/opravy.xlsx](report/opravy.xlsx)** (s filtry a sloupcem „Opraveno“ pro rozdělení práce)

Kontrola byla připravena s pomocí AI asistenta Claude (Anthropic). Skripty i surová data jsou v tomto repozitáři, takže ji lze kdykoli zopakovat.

## Obsah repozitáře

- `PREHLED.md` – přehled chyb seřazený podle priority
- `report/opravy.xlsx`, `report/opravy.csv` – totéž jako tabulka (jeden řádek = jedna stránka a jeden chybný odkaz)
- `report/report.json` – data přehledu
- `data/` – surová data z procházení webu
- `*.py`, `curl_verify.sh` – skripty kontroly

## Jak kontrolu zopakovat

Potřeba: Python 3 s balíčky `requests`, `beautifulsoup4`, `openpyxl`.

```
python3 crawler.py data              # stránky ze sitemapy + kontrola odkazů na mlp.cz (1 požadavek/s)
python3 analyze.py data              # roztřídění nálezů
python3 check_external.py data       # odkazy na cizí weby
python3 recheck_external.py data     # 2. pokus pro nefunkční cizí odkazy
./curl_verify.sh < data/ambiguous.txt > data/external3.tsv   # 3. pokus
python3 check_listings.py data       # prázdné výpisy akcí
python3 build_report.py data report
python3 verify_suggestions.py data report && python3 build_report.py data report
python3 make_docs.py report          # PREHLED.md + opravy.xlsx
```

`check_listings.py` čte seznam odkazů na výpisy akcí z `data/akce_links.json`, který vznikl během analýzy.
