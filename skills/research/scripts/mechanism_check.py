#!/usr/bin/env python3
"""Flag our mechanism lines and hooks that nearly copy a competitor's.

Usage: python mechanism_check.py research/<brand>/01-ads.jsonl ours.txt > research/<brand>/03-mechanism-check.md

`ours.txt` holds one line per mechanism anchor or hook (from 03-angles.md).
Competitor text comes from the `mechanism`, `hook` and `claimed_outcomes` fields
of every ad in 01-ads.jsonl whose `owner` is not "client". For each of our lines
it reports the closest competitor line, the shared 3-word phrases, and a
similarity score. Lines that share a 3-word phrase (not counting phrases made
only of filler words), or score 0.55 or more, are flagged REWORD. Structural echoes (e.g. "outside ... inside") still need a human
read; the script lists the top match so it can be checked.
"""
import difflib
import json
import re
import sys

THRESHOLD = 0.55
STOP = set("the a an and or of to in on for is it your you this that with are be".split())


def words(text):
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)


def grams(text, n=3):
    w = words(text)
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)
            if not all(x in STOP for x in w[i:i + n])}


def main(ads_path, ours_path):
    comp = []
    with open(ads_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                a = json.loads(line)
            except json.JSONDecodeError:
                continue
            if a.get("owner") == "client":
                continue
            for field in ("mechanism", "hook", "claimed_outcomes"):
                if a.get(field):
                    comp.append((a[field], a.get("advertiser", "?"), a.get("days_running"), a.get("url", "")))
    with open(ours_path, encoding="utf-8") as f:
        ours = [l.strip() for l in f if l.strip()]

    print("# Mechanism and hook distinctness check\n")
    print(f"{len(ours)} of our lines against {len(comp)} competitor lines.\n")
    print("| Our line | Closest competitor line | Advertiser (days) | Shared 3-word phrases | Score | Verdict |")
    print("|---|---|---|---|---|---|")
    flagged = 0
    for line in ours:
        g = grams(line)
        best, best_score, best_shared = None, 0.0, set()
        for text, adv, days, url in comp:
            shared = g & grams(text)
            score = difflib.SequenceMatcher(None, " ".join(words(line)), " ".join(words(text))).ratio()
            if (len(shared), score) > (len(best_shared), best_score):
                best, best_score, best_shared = (text, adv, days, url), score, shared
        if not best:
            print(f"| {line} | – | – | – | 0 | OK |")
            continue
        bad = bool(best_shared) or best_score >= THRESHOLD
        flagged += bad
        text, adv, days, url = best
        link = f"[{adv}]({url})" if url else adv
        print(f"| {line} | {text[:160]} | {link} ({days or '?'}) | {'; '.join(sorted(best_shared)) or '–'} "
              f"| {best_score:.2f} | {'**REWORD**' if bad else 'OK'} |")
    print(f"\n{flagged} line(s) flagged. Reword each flagged line, and read the OK lines next to their closest "
          "match for structural echoes before calling them distinct.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
