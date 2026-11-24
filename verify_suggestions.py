#!/usr/bin/env python3
"""Check internal suggested replacement URLs that the crawl did not cover (-> data/suggestions.json)."""
import json, sys
from urllib.parse import urlsplit
from crawler import check, normalize, INTERNAL_HOSTS
D, REP = sys.argv[1], sys.argv[2]
rows = json.load(open(f"{REP}/report.json"))["rows"]
out = {}
for r in rows:
    s = r.get("suggestion")
    if s and r.get("suggestion_ok") is None and s.startswith("http") and urlsplit(s).hostname in INTERNAL_HOSTS and s not in out:
        chain = check(normalize(s, s) or s)
        last = chain[-1].get("status")
        out[s] = isinstance(last, int) and last < 400
        print(last, s, flush=True)
json.dump(out, open(f"{D}/suggestions.json", "w"), ensure_ascii=False, indent=1)
