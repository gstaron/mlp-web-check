#!/usr/bin/env python3
"""Second, sequential pass over external links that did not return 200 (data/external.jsonl -> data/external2.jsonl)."""
import json, os, sys, time
from urllib.parse import urlsplit
import requests

D = sys.argv[1] if len(sys.argv) > 1 else "data"
SKIP = {"www.facebook.com", "m.facebook.com", "www.youtube.com", "youtu.be", "www.instagram.com", "instagram.com"}
CA = "/root/.ccr/ca-bundle.crt"
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
s.headers["Accept"] = "text/html,application/xhtml+xml,*/*;q=0.8"
s.headers["Accept-Language"] = "cs,en;q=0.8"
if os.path.exists(CA):
    s.verify = CA
todo = []
for l in open(f"{D}/external.jsonl"):
    r = json.loads(l)
    h = urlsplit(r["url"]).hostname or ""
    if r.get("status") != 200 and h not in SKIP and "." in h:
        todo.append(r["url"])
with open(f"{D}/external2.jsonl", "w") as f:
    for u in todo:
        t = "https://" + u[7:] if u.startswith("http://") else u
        rec = {"url": u}
        for attempt in range(2):
            try:
                r = s.get(t, timeout=40, allow_redirects=True)
                rec.update(status=r.status_code, final=r.url, error=None)
                if r.status_code < 500 and r.status_code not in (401, 429):
                    break
            except requests.RequestException as e:
                rec.update(status=None, error=type(e).__name__ + ": " + str(e)[:300])
            time.sleep(3)
        f.write(json.dumps(rec, ensure_ascii=False) + "\n"); f.flush()
        time.sleep(1)
print("DONE", len(todo))
