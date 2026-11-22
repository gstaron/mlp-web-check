#!/usr/bin/env python3
"""Link checker for www.mlp.cz.

Phase 1: download every content page listed in the "default" sitemap,
         extract links (<a href>, <img src>, <iframe src>) and remember
         where they sit on the page (content vs. header/footer).
Phase 2: check every unique internal URL (status code, redirect chain).

Results are written as JSON lines so the run can be resumed.
Respects robots.txt Crawl-delay (1 s between requests).
"""
import json
import os
import re
import sys
import time
from urllib.parse import urljoin, urlsplit, urlunsplit, quote, unquote

import requests
from bs4 import BeautifulSoup

BASE = "https://www.mlp.cz"
INTERNAL_HOSTS = {"www.mlp.cz", "mlp.cz"}
DELAY = float(os.environ.get("DELAY", "1.0"))
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
os.makedirs(OUT, exist_ok=True)

S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0 (compatible; mlp-link-check/1.0)"
CA = "/root/.ccr/ca-bundle.crt"
if os.path.exists(CA):
    S.verify = CA

_last = [0.0]


def polite_get(url, **kw):
    wait = DELAY - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    try:
        return S.get(url, timeout=40, **kw)
    finally:
        _last[0] = time.time()


def load_done(path, key):
    done = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    done[r[key]] = r
                except Exception:
                    pass
    return done


def sitemap_urls():
    r = polite_get(BASE + "/default/sitemap.xml?page=1")
    return re.findall(r"<loc>([^<]+)</loc>", r.text)


def region_of(tag):
    for p in tag.parents:
        if p.name in ("header", "footer", "nav"):
            return "layout"
        cls = " ".join(p.get("class", []))
        if p.name == "main" or "region-content" in cls:
            return "content"
    return "layout"


def extract(page_url, html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag, attr in (("a", "href"), ("img", "src"), ("iframe", "src")):
        for el in soup.find_all(tag):
            raw = el.get(attr)
            if raw is None:
                continue
            text = el.get_text(" ", strip=True) if tag == "a" else (el.get("alt") or "")
            links.append({
                "raw": raw,
                "tag": tag,
                "text": " ".join(text.split())[:120],
                "region": region_of(el),
            })
    title = soup.title.get_text(strip=True) if soup.title else ""
    return title, links


def normalize(page_url, raw):
    raw = raw.strip()
    if not raw or raw.startswith(("#", "javascript:", "mailto:", "tel:", "data:")):
        return None
    u = urljoin(page_url, raw)
    parts = urlsplit(u)
    if parts.scheme not in ("http", "https"):
        return None
    # percent-encode non-ASCII the way a browser does
    path = quote(unquote(parts.path), safe="/%:@!$&'()*+,;=-._~")
    query = quote(parts.query, safe="=&%/:+,;@!$'()*-._~[]?")
    return urlunsplit((parts.scheme, parts.netloc.lower(), path, query, ""))


def check(url):
    chain = []
    cur = url
    if cur.startswith("http://"):
        # the sandbox only has an HTTPS proxy; check the https:// variant instead
        chain.append({"url": cur, "status": "http-checked-as-https"})
        cur = "https://" + cur[7:]
    for _ in range(8):
        try:
            r = polite_get(cur, allow_redirects=False, stream=True)
            code = r.status_code
            loc = r.headers.get("Location")
            ctype = r.headers.get("Content-Type", "")
            r.close()
        except requests.RequestException as e:
            chain.append({"url": cur, "status": None, "error": type(e).__name__ + ": " + str(e)[:200]})
            return chain
        chain.append({"url": cur, "status": code, "ctype": ctype})
        if code in (301, 302, 303, 307, 308) and loc:
            cur = urljoin(cur, loc)
            if cur.startswith("http://"):
                cur = "https://" + cur[7:]
            if urlsplit(cur).hostname not in INTERNAL_HOSTS:
                chain.append({"url": cur, "status": "external"})
                return chain
            continue
        if code >= 500:
            # one retry for transient server errors
            time.sleep(5)
            try:
                r2 = polite_get(cur, allow_redirects=False, stream=True)
                chain[-1]["retry_status"] = r2.status_code
                r2.close()
            except requests.RequestException:
                pass
        return chain
    chain.append({"url": cur, "status": "too-many-redirects"})
    return chain


def main():
    pages_path = os.path.join(OUT, "pages.jsonl")
    checks_path = os.path.join(OUT, "checks.jsonl")

    urls = sitemap_urls()
    if BASE + "/" not in urls:
        urls.insert(0, BASE + "/")
    print(f"sitemap pages: {len(urls)}", flush=True)

    done = load_done(pages_path, "url")
    with open(pages_path, "a") as f:
        for i, u in enumerate(urls):
            if u in done:
                continue
            try:
                r = polite_get(u)
                title, links = extract(u, r.text) if "html" in r.headers.get("Content-Type", "") else ("", [])
                rec = {"url": u, "status": r.status_code, "final": r.url, "title": title, "links": links}
            except requests.RequestException as e:
                rec = {"url": u, "status": None, "error": str(e)[:200], "links": []}
            done[u] = rec
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            if i % 50 == 0:
                print(f"[pages] {i}/{len(urls)}", flush=True)

    targets = {}
    for rec in done.values():
        for l in rec.get("links", []):
            n = normalize(rec.get("final") or rec["url"], l["raw"])
            if n and urlsplit(n).hostname in INTERNAL_HOSTS:
                targets.setdefault(n, 0)
                targets[n] += 1
    # pages already fetched successfully as sitemap pages need no re-check
    fetched_ok = {rec["url"]: rec["status"] for rec in done.values()}
    print(f"unique internal targets: {len(targets)}", flush=True)

    cdone = load_done(checks_path, "url")
    with open(checks_path, "a") as f:
        for i, t in enumerate(sorted(targets)):
            if t in cdone:
                continue
            if fetched_ok.get(t) == 200:
                rec = {"url": t, "chain": [{"url": t, "status": 200, "from_sitemap": True}]}
            else:
                rec = {"url": t, "chain": check(t)}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            if i % 100 == 0:
                print(f"[checks] {i}/{len(targets)}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
