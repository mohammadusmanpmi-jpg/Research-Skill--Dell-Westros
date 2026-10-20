# Phase 1.13 – Consolidation → `02-consolidation.md`

Inputs: `01-counts.md` (computed), `01-quotes.jsonl`, every `01-<source>.md`, `01-authority.md`, `01-ads.md`, `01-verification.md`.

Frequency bands come from `01-counts.md`. Do not re-estimate them. Band definitions (mentions = records sharing a theme; sources = distinct `source` values):

- DOMINANT = 30+ mentions across 4+ sources
- HIGH = 15-29 across 3+
- MODERATE = 6-14 across 2+
- LOW = 3-5 across 1-2
- RARE = 1-2

If fewer sources were collected than the band thresholds assume (e.g. only Reddit and Amazon), say so at the top and treat bands as relative, not absolute.

No invented quotes, no paraphrase, no brand-blog content as a source. Every representative quote is copied from the jsonl with its URL.

## Executive summary (top of document)
1. Dominant pain (theme, count, band)
2. Most common scene (count)
3. Most common trigger (count)
4. Most tried-and-failed solution (count)
5. Dominant belief (count)
6. Dominant villain (count)
7. Most trusted authority (count)
8. #1 blocking belief (count)
9. Dominant psychographic
10. Most useful statistic for ad copy
11. Strongest mechanism opportunity
12. Total data: X verified quotes from Y sources across Z platforms (from verification file)

The single most important finding: one sentence.

Unexpected findings: quote, source, why flagged.

Competitor landscape (from `01-ad-matrix.md`, `01-ads.md` and `01-competitors.md`, or "not collected"): OPEN / EMERGING / PROVEN / CROWDED / ABANDONED angles and avatars: saturated / contested / white-space angles, dominant and underserved desire, dominant and underused format.

Source quality ranking: rank the sources actually collected, with what each uniquely contributed.

## Sections

**1. Pain point inventory** – table: pain | band | count | representative quote | source type | URL. All pain themes, ≥15 where data allows, DOMINANT first. Closing line: the gap between #1 and #2 and what it means for where to lead.

**2. Scene map** – scene/location | time | activity | who is present | band | quote | URL. Scenes are specific moments, not categories. ≥10. Closing line: the most frequent scene is the opening frame of the lead ad.

**3. Trigger event timeline** – trigger | when in the journey | band | verbatim | URL. Sorted chronologically through the customer journey. Closing line: most common trigger vs highest-emotional-charge trigger.

**4. Failed solution trail** – solution | typical order | cost mentioned | why it failed (verbatim) | band | URL. Sorted first-tried → last resort. Closing: most-failed solution; average number tried (computed from quotes mentioning multiple); money range from `cost` fields; the solution tried most recently before this category.

**5. Current beliefs map** – belief | type (problem / solutions / self) | TRUE / FALSE / PARTIALLY (per `01-authority.md`) | band | copy implication | URL. Closing: dominant belief and whether copy should validate, question or reframe it.

**6. Villain map** – villain | verbatim | band | usable in copy (Yes / With care / No) | risk | URL. Closing: dominant villain vs most usable villain.

**7. Trust map** – authority | why trusted | Primary / Secondary / Conditional | band | can narrate ads? | URL.

**8. Blocking beliefs** – belief | segment blocked | Trust / Identity / Risk / Cost | band | handle by Preempt / Reframe / Prove / Demonstrate / Ignore | URL. Closing: the #1 blocker; the easiest fix; the one with no easy fix and the alternative strategy for that segment. (Do not invent an "audience lost %" – no data supports it.)

**9. Demographics and psychographics** – 9A stated demographics (verbatim only). 9B psychographic patterns: pattern | what it reveals | how it changes copy | evidence (quotes + count). Closing: dominant psychographic in one sentence.

**10. Statistics** – 10A market/prevalence from authority sources (verified? Y/N). 10B customer-stated numbers labelled VOC. Closing: the statistic to use and the one to avoid.

**11. Root cause science** – 11A problem mechanism (plain language, cited). 11B product mechanism: verified / plausible / unsupported. 11C mechanism opportunities. 11D compliance boundaries (with citation / soften / cannot say).

**12. Full source list** – source | URL | type | quotes collected | key finding. Plus sources considered and rejected, with reason. Total count.

Write `state.json` entry `consolidation` when done.
