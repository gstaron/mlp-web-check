#!/usr/bin/env python3
"""Check external links collected by analyze.py (data/findings.json -> data/external.jsonl)."""
import json
import os
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit

import requests

D = sys.argv[1] if len(sys.argv) > 1 else "data"
CA = "/root/.ccr/ca-bundle.crt"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"

links = json.load(open(f"{D}/findings.json"))["external_links"]
out = f"{D}/external.jsonl"
done = set()
if os.path.exists(out):
    done = {json.loads(l)["url"] for l in open(out)}

by_host = defaultdict(list)
for u in links:
    if u not in done:
        by_host[urlsplit(u).hostname].append(u)


def check_host(urls):
    s = requests.Session()
    s.headers["User-Agent"] = UA
    s.headers["Accept-Language"] = "cs,en;q=0.8"
    if os.path.exists(CA):
        s.verify = CA
    res = []
    for u in urls:
        rec = {"url": u}
        try:
            r = s.get(u, timeout=30, allow_redirects=True, stream=True)
            rec.update(status=r.status_code, final=r.url, hops=len(r.history))
            r.close()
        except requests.RequestException as e:
            rec.update(status=None, error=type(e).__name__ + ": " + str(e)[:300])
        res.append(rec)
        time.sleep(1)
    return res


with open(out, "a") as f, ThreadPoolExecutor(8) as ex:
    for res in ex.map(check_host, by_host.values()):
        for rec in res:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        f.flush()
print("DONE")
