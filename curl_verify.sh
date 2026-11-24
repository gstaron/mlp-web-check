#!/bin/bash
# Third pass: verify ambiguous external results with curl (browser UA). Output: url<TAB>http_code<TAB>curl_exit<TAB>effective_url
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
while IFS= read -r u; do
  t="$u"; [[ "$t" == http://* ]] && t="https://${t#http://}"
  out=$(curl -sS -A "$UA" -H "Accept-Language: cs" -L --max-time 30 -o /dev/null -w "%{http_code}\t%{url_effective}" "$t" 2>/tmp/curl_err); ec=$?
  printf '%s\t%s\t%s\t%s\n' "$u" "$(cut -f1 <<<"$out")" "$ec" "$(head -c 150 /tmp/curl_err | tr '\n\t' '  ')"
  sleep 1
done
