#!/usr/bin/env python3
"""Fetch filtered event listings linked from content and detect empty results / errors."""
import json, sys, time
from urllib.parse import urlsplit, parse_qsl
from bs4 import BeautifulSoup
from crawler import polite_get

D = sys.argv[1] if len(sys.argv) > 1 else "data"
links = json.load(open(f"{D}/akce_links.json"))
out = {}
for u, refs in links.items():
    p = urlsplit(u)
    if p.hostname not in ("www.mlp.cz", "mlp.cz"):
        continue
    keys = {k for k, _ in parse_qsl(p.query, keep_blank_values=True)}
    if not keys & {"nid_entityreference_filter", "field_event_type_target_id"}:
        continue
    try:
        r = polite_get(u)
        soup = BeautifulSoup(r.text, "html.parser")
        view = soup.select_one("main .views-element-container")
        items = len(view.select(".views-row, article, li")) if view else None
        txt = " ".join(view.get_text(" ", strip=True).split())[:200] if view else ""
        out[u] = {"status": r.status_code, "items": items, "text": txt, "refs": refs}
    except Exception as e:
        out[u] = {"status": None, "error": str(e)[:200], "refs": refs}
    print(out[u].get("status"), out[u].get("items"), u, flush=True)
json.dump(out, open(f"{D}/listings.json", "w"), ensure_ascii=False, indent=1)
