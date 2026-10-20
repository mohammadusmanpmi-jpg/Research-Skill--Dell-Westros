#!/usr/bin/env python3
"""Re-check every quote in 01-quotes.jsonl against its live link.

Usage: python verify_quotes.py research/<brand>/01-quotes.jsonl [--only-unchecked] [--delay 1.0]

For each record, fetches `url` (Reddit threads via their .json endpoint), strips
markup, and looks for the quote text. Matching ignores case, spacing,
punctuation and quote marks, and accepts the quote when any 80-character stretch
of it (or the whole quote, if shorter) is found on the page. Works for any
language.

Writes back to the same file, adding to each record:
  verified: true | false        (false = page loaded, text not found)
  verify_status: found | not-found | unreachable (<reason>)
  verified_at: ISO date
Records marked unreachable keep `verified` unset: re-check them in the browser
(Claude in Chrome) and set the fields by hand, or drop them. A summary goes to
stdout; save it as `01-verification.md`.
"""
import datetime
import html
import json
import re
import sys
import time
import unicodedata
import urllib.request

UA = "Mozilla/5.0 (research-skill verify_quotes)"
WINDOW = 80


def norm(text):
    text = unicodedata.normalize("NFKC", html.unescape(text)).lower()
    text = re.sub(r"[\W_]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)


def fetch(url):
    target = url
    is_reddit = re.search(r"reddit\.com/r/[^/]+/comments/", url)
    if is_reddit:
        base = url.split("?")[0].split("#")[0].rstrip("/")
        target = base + ".json?limit=500"
    req = urllib.request.Request(target, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode(resp.headers.get_content_charset() or "utf-8", "replace")
    if is_reddit:
        try:
            return " ".join(strings(json.loads(raw)))
        except json.JSONDecodeError:
            pass
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    return re.sub(r"<[^>]+>", " ", raw)


def found(quote, page):
    q = norm(quote)
    if not q:
        return False
    if len(q) <= WINDOW:
        return q in page
    step = WINDOW // 2
    return any(q[i:i + WINDOW] in page for i in range(0, len(q) - WINDOW + 1, step))


def main(path, only_unchecked=False, delay=1.0):
    with open(path, encoding="utf-8") as f:
        lines = [l for l in f if l.strip()]
    records = [json.loads(l) for l in lines]
    cache, today = {}, datetime.date.today().isoformat()
    for r in records:
        if only_unchecked and r.get("verified") is True:
            continue
        url = r.get("url")
        if not url or not r.get("quote"):
            r["verified"], r["verify_status"] = False, "not-found (no url or quote)"
            continue
        key = url.split("#")[0]
        if key not in cache:
            try:
                cache[key] = norm(fetch(url))
            except Exception as e:  # network errors, 403s, timeouts
                cache[key] = None
                cache[key + "#err"] = f"{type(e).__name__}: {e}"[:120]
            time.sleep(delay)
        page = cache[key]
        if page is None:
            r.pop("verified", None)
            r["verify_status"] = "unreachable (" + cache.get(key + "#err", "") + ")"
        elif found(r["quote"], page):
            r["verified"], r["verify_status"] = True, "found"
        else:
            r["verified"], r["verify_status"] = False, "not-found"
        r["verified_at"] = today
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    total = len(records)
    ok = sum(1 for r in records if r.get("verified") is True)
    bad = [r for r in records if r.get("verified") is False]
    unreach = [r for r in records if str(r.get("verify_status", "")).startswith("unreachable")]
    print("# Quote verification\n")
    print(f"Checked {total} quotes on {today}: {ok} found, {len(bad)} not found, {len(unreach)} unreachable.\n")
    by_src = {}
    for r in records:
        s = by_src.setdefault(r.get("source", "unknown"), [0, 0, 0])
        s[0 if r.get("verified") is True else 1 if r.get("verified") is False else 2] += 1
    print("| Source | Found | Not found | Unreachable |\n|---|---|---|---|")
    for s, (a, b, c) in sorted(by_src.items()):
        print(f"| {s} | {a} | {b} | {c} |")
    if bad:
        print("\nNot found (remove from the jsonl, or fix the URL if the quote is real):")
        for r in bad[:200]:
            print(f"- {r.get('id', '?')} – {r.get('url')}")
    if unreach:
        print("\nUnreachable (re-check in the browser before Phase 1 is done):")
        for r in unreach[:200]:
            print(f"- {r.get('id', '?')} – {r.get('url')} – {r['verify_status']}")
    print("\nPhase 1 is done only when every quote is found. Rerun count_quotes.py and depth_check.py after removals.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    delay = 1.0
    if "--delay" in sys.argv:
        delay = float(sys.argv[sys.argv.index("--delay") + 1])
        args = [a for a in args if a != str(sys.argv[sys.argv.index("--delay") + 1])]
    main(args[0], "--only-unchecked" in sys.argv, delay)
