#!/usr/bin/env python3
"""Check Phase 1 collection depth against the minimum floors.

Usage: python depth_check.py research/<brand>/01-quotes.jsonl [research/<brand>/01-ads.jsonl] > research/<brand>/01-depth.md

Counts, per source: quotes, distinct threads/pages (distinct URLs without the
comment anchor), distinct communities (`sub` field), the largest share of quotes
coming from one thread, and the 2-3 star share for review sources. Compares
each with the floors in phase1-collectors.md § Minimum depth and prints PASS /
BELOW FLOOR. Also reports how many quotes are verified (`verified: true`, set by
verify_quotes.py). Phase 1 is not done while any line says BELOW FLOOR without a
logged shortfall, or while verification is under 100%.
"""
import json
import re
import sys
from collections import Counter, defaultdict

# source: (min quotes, min threads/pages/videos/listings, min communities or 0)
FLOORS = {
    "reddit": (600, 120, 10),
    "forums": (250, 60, 6),
    "quora": (150, 30, 0),
    "amazon": (250, 8, 0),            # threads = listings
    "complaints": (100, 0, 0),
    "youtube": (250, 25, 0),
    "tiktok-comments": (300, 40, 0),  # threads = videos
    "tiktok-shop": (150, 8, 0),       # threads = listings
    "facebook": (200, 0, 10),         # communities = groups
    "instagram": (100, 20, 0),
    "x": (100, 0, 0),
}
TOTAL_QUOTES = 2000
MIN_SOURCES = 6
MAX_THREAD_SHARE = 0.15
MIN_LOW_STAR_SHARE = 0.40  # 2-3 star share for review sources
REVIEW_SOURCES = {"amazon", "tiktok-shop"}
ADS_FLOORS = {"ads": 100, "advertisers": 8, "ads_30d": 30}


def thread_key(url):
    url = url.split("#")[0].rstrip("/")
    m = re.match(r"(https?://[^/]*reddit\.com/r/[^/]+/comments/[^/]+)", url)
    return m.group(1) if m else url


def load(path):
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def status(ok):
    return "PASS" if ok else "**BELOW FLOOR**"


def main(quotes_path, ads_path=None):
    rows = [r for r in load(quotes_path) if r.get("url") and r.get("quote")]
    by_src = defaultdict(list)
    for r in rows:
        by_src[r.get("source", "unknown")].append(r)

    p = print
    p("# Phase 1 depth check\n")
    p(f"Input: `{quotes_path}`\n")
    p("| Source | Quotes | Floor | Threads/pages | Floor | Communities | Floor | Top thread share | 2-3 star share | Status |")
    p("|---|---|---|---|---|---|---|---|---|---|")
    below = []
    for src in sorted(set(by_src) | set(FLOORS)):
        recs = by_src.get(src, [])
        fq, ft, fc = FLOORS.get(src, (0, 0, 0))
        threads = Counter(thread_key(r["url"]) for r in recs)
        comms = {r.get("sub") for r in recs if r.get("sub")}
        top_share = (threads.most_common(1)[0][1] / len(recs)) if recs else 0
        rated = [r for r in recs if isinstance(r.get("rating"), (int, float))]
        low = (sum(1 for r in rated if 2 <= r["rating"] <= 3) / len(rated)) if rated else None
        ok = len(recs) >= fq and len(threads) >= ft and len(comms) >= fc
        if recs and top_share > MAX_THREAD_SHARE:
            ok = False
        if src in REVIEW_SOURCES and rated and low < MIN_LOW_STAR_SHARE:
            ok = False
        if not recs and src in FLOORS:
            st = "not collected"
        else:
            st = status(ok)
            if not ok:
                below.append(src)
        p(f"| {src} | {len(recs)} | {fq or '-'} | {len(threads)} | {ft or '-'} | {len(comms)} | {fc or '-'} "
          f"| {top_share:.0%} | {'-' if low is None else f'{low:.0%}'} | {st} |")

    collected = [s for s in by_src if by_src[s]]
    p("")
    p(f"- Total quotes: {len(rows)} (floor {TOTAL_QUOTES}) – {status(len(rows) >= TOTAL_QUOTES)}")
    p(f"- Sources collected: {len(collected)} (floor {MIN_SOURCES}) – {status(len(collected) >= MIN_SOURCES)}")
    p(f"- No single thread may supply more than {MAX_THREAD_SHARE:.0%} of a source's quotes.")
    p(f"- Review sources need at least {MIN_LOW_STAR_SHARE:.0%} of rated quotes from 2-3 star reviews.")

    verified = sum(1 for r in rows if r.get("verified") is True)
    failed = sum(1 for r in rows if r.get("verified") is False)
    unchecked = len(rows) - verified - failed
    p(f"- Verified against live link: {verified}/{len(rows)} "
      f"({(verified / len(rows) if rows else 0):.0%}); failed {failed}; not yet checked {unchecked} "
      f"– {status(unchecked == 0 and failed == 0)}")

    if ads_path:
        ads = load(ads_path)
        advertisers = {a.get("advertiser") for a in ads if a.get("advertiser")}
        long_run = sum(1 for a in ads if (a.get("days_running") or 0) >= 30)
        p("")
        p(f"- Competitor ads recorded: {len(ads)} (floor {ADS_FLOORS['ads']}) – {status(len(ads) >= ADS_FLOORS['ads'])}")
        p(f"- Advertisers: {len(advertisers)} (floor {ADS_FLOORS['advertisers']}) – {status(len(advertisers) >= ADS_FLOORS['advertisers'])}")
        p(f"- Ads running 30+ days: {long_run} (floor {ADS_FLOORS['ads_30d']}) – {status(long_run >= ADS_FLOORS['ads_30d'])}")

    p("")
    if below:
        p("**Below floor:** " + ", ".join(below) + ". Keep collecting, or log a shortfall with every query and page tried "
          "and ask the user before moving on.")
    else:
        p("All collected sources meet their floors.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
