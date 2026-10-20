# Angle Exploration Document template → `03-angle-exploration.md`

The Phase 3 deliverable for the client. Modelled on the Element Vital Angle Exploration (Oct 21, 2026). It sits next to the DRIVE Strategy (`04-drive-strategy.md`): the strategy holds the mechanism, the sophistication map, the ICP profiles and the offer, and this document is the working angle library built from them. Pick angles, brief them out, ship them.

Write it after Steps 1-8 of `phase3-angles.md`. Those steps produce the working files (`03-angles.md`, the validation flags, the dominate plans and `03-mechanism-check.md`); this template is how they are presented. Nothing in it is new research: every count, quote, ad and trend comes from the Phase 1-3 files, with its link.

## Inputs (all required unless noted)
- ICPs (3 obvious + 3 underserved) and the Big Idea: `02-drive.md` / `04-drive-strategy.md`
- Pain counts and verbatim quotes: `01-counts.md`, `02-consolidation.md`, `01-quotes.jsonl` (verified quotes only)
- Competitor ads and validation: `01-ads.jsonl`, `01-ad-matrix.md`, `01-ad-searches.md`, `03-angles.md` Steps 1-4
- The client's own ads: `00-account.md` (proven on account, tested and stopped)
- Trends: `01-trends.md` (UNRIDDEN / EARLY RIDERS / RIDDEN), `01-tiktok.md`
- Evidence ceiling and guardrails: `01-science.md`
- Site fixes: `00-offer-audit.md` (for objection angles on HOLD)

---

## Document layout

### Cover
Brand, product, "ANGLE EXPLORATION DOCUMENT", the subtitle *ICPs × Pain Points × [Problem] Research = New Ad Territory*, the one-line Big Idea, the prepared date and the sources it is built from.

### How to use this document
- One paragraph: this is a working library, not the strategy.
- **The three inputs where angles come from:** the ICPs (name all six); the pain points, counted from N verbatim excerpts across N platforms ("Not invented. Not assumed. Every card shows its BASIS"); and the science we can stand behind, with the product claim at its honest ceiling.
- **Where the three meet a buyer nobody else speaks to, the angle goes to the front of the queue.**
- **The document structure:** one line per section.
- **What this document does NOT do:** dictate format, soften the emotion (claims already sit inside the guardrails), repeat the DRIVE document, or write scripts.
- **Working assumption box:** the reframe that stays the same in every angle. "Different doorways into the same room."

### Contents
A table of sections, then the cluster table: Cluster | Pain | Lane and role (spine / entry / bridge / TEST ONLY / NOT PURSUED) | Angles.

---

### Section 1: The pain point universe and the ICP matrix

**1A. Pain point universe**

| Cluster | Specific pain points | Lane and role | Frequency | Count |
|---|---|---|---|---|

- Frequency uses the research bands: DOMINANT 30+, HIGH 15-29, MODERATE 6-14, LOW 3-5, RARE 1-2. Counts are excerpt rows from `01-counts.md`. Where two counts are joined, show both so nothing is double counted.
- Include clusters that are **mapped, not pursued** (e.g. a medication side-effect lane the formula can't safely sell into), with the reason.
- Close with a summary box: where the client's live creative sits today (e.g. "15 of its 18 active ads lead with cold feet, a lane 10 brands already fight over"), which clusters are empty across the category, which are contested by only 1-2 brands. Every number links back to `00-account.md` or `01-ad-matrix.md`.

**1B. ICP × pain point matrix**

Rows = clusters, columns = the six ICPs. Cells: **CORE** (main doorway), **YES** (second doorway or proof beat), **CAUTION** (the buyer has the pain but the formula makes it unsafe to sell into), **TEST** (test lane only).
Add the "read it two ways" box: rows that reach the most buyers are the best places to test new hooks; columns with the fewest competitors are the best places to build new concepts.

---

### Section 2: Competitor takeover (required)

**Every angle a competitor is running right now gets a takeover card. Adopt what is proven, then improve it.** A long-running competitor ad is proof the angle sells, so it is never dropped. The client's own proven ads come first (iterate before inventing).

Order: (1) the client's own PROVEN ON ACCOUNT ads, (2) CROWDED, (3) PROVEN, (4) EMERGING. Within each, longest-running first.

```
### Takeover T<nn>: <angle name>      Flag: <PROVEN / CROWDED / EMERGING / PROVEN ON ACCOUNT>

THIS ANGLE IS CURRENTLY RUNNING FROM <Competitor> (and <N> others: <names>)
- Their ad: <ad library or TrendTrack link>   Status: live   Days running: <d>   Format: <UGC / static / B-roll …>
- Their exact copy: hook "<verbatim>" · headline "<verbatim>" · key body line "<verbatim>"
- Their mechanism: "<verbatim phrasing>"
- Who they target: <ICP / avatar, age, gender, from the creative and copy>
- Their proof: <testimonial / doctor / study / demo / review count>
- Their offer: <price, bundle, guarantee as shown in the ad or on the landing page>
- Why it works (proof of demand): <days running, number of variants, scaling signal> + VOC count for the pain (<theme> = N rows, <band>)
- Where it is weak: <the VOC complaint about their approach, the belief their ad leaves unhandled, the ICP it ignores, a claim the science won't support> — with quote + URL

HERE'S HOW WE DOMINATE IT
- Adopt (keep what is proven): <the pain, desire or scene we keep>
- Improve (our lever): <unique mechanism / new ICP / new proof / new villain / new scene / specificity / format / sophistication step-up>
- Our ICP: <which of the six, and why they are under-served by the competitor's version>
- Our mechanism: <problem mechanism → solution mechanism, one line each>   Distinctness: <OK / REWORDED, from 03-mechanism-check.md>
- Our proof: <the proof beat we have or can get; asset needed>
- Our format: <format + one-line reason>
- Hooks (our words, never naming the competitor):
    1. <hook>
    2. <hook>
    3. <hook>
- Side by side:  Theirs: "<their hook>"  →  Ours: "<our best hook>"
- Why ours beats theirs: one sentence tied to data
- Compliance: safe / soften / needs citation (per 01-science.md guardrails)
- Feeds DRIVE: Angle <nn>
```

Rules for this section:
- Copy, links and days running come from `01-ads.jsonl`. No link → the card is not written (CLAUDE.md rule). Re-check "live" and days running on the day the document is written; note the check date.
- Every competitor named is internal intel for the client. Hooks, headlines and briefs never name or attack a competitor, so every handoff reads as our own idea.
- Run `mechanism_check.py` on every mechanism line and hook in this section. A REWORD line is rewritten before the document ships.
- If the competitor is the category leader attacking one of our ingredients, say so and don't make that ingredient the hero.
- End the section with a one-table summary: Angle | Competitor(s) | Days running | Their target | Our lever | Our ICP | First hook.

---

### Section 3: The angle library (open and under-served angles)

Grouped by pain cluster, 2-4 angles per cluster, numbered in order through the whole library. Angles already covered by a takeover card in Section 2 are referenced, not repeated.

**Cluster header:** `Cluster <X>: <Pain>` / `LANE: <…> | FREQUENCY: <band> (<counts>)` / one or two lines on the competitive situation (how many brands touch it, as what).

**Angle card:**
```
ANGLE <n>: <Name>
ICP: <one or two of the six> | STAGE: <sophistication 1-5> | FEEDS DRIVE: Angle <nn> | FLAG: <OPEN / EMERGING / … + searches in 03-angles.md>

PAIN POINT: two sentences in plain words.
BASIS: "<real quote, exact, 15 words or fewer>" (<platform, who, age if given>) <URL>

HOOKS:
   <hook 1>
   <hook 2>
   <hook 3>

MECHANISM TIE-IN: two or three sentences linking the pain to the problem mechanism, with any number cited in 01-science.md.
NOTE: casting, format, tone, the one trap to avoid (e.g. "Never position as a replacement", "Do not claim zero side effects").
```

Three rules for every card: hooks are our words, so they never sit in quotation marks; quotes in the BASIS line are real, exact and linked; no card names a competitor.

**Mapped, not pursued:** a cluster heading with no cards and the reason (safety, the formula, the account health).

**Objections at the buy button (Cluster S):** angles answering why he stops at the buy box (meds, price, subscription, refund, scam, dose, shame), each marked **HOLD until <fix n> in 00-offer-audit.md lands** when the site contradicts it. An objection angle the page contradicts is worse than no angle.

---

### Section 4: Trend angles (riding what competitors aren't)

From `01-trends.md` and `01-tiktok.md`. One card per UNRIDDEN or EARLY RIDERS trend that links to a VOC cluster.

```
TREND ANGLE <n>: <Name>       Trend flag: UNRIDDEN / EARLY RIDERS
The trend: <what it is> · Evidence: <Google Trends term + change, TikTok hashtag/sound + views, news link> · Act by: <date or window>
Who is riding it: <none found (searches logged) / competitors + ad links + days running>
Linked pain: Cluster <X> (<count>, <band>)
ICP: <…> | STAGE: <…> | FEEDS DRIVE: Angle <nn>
HOOKS: three, in our words
MECHANISM TIE-IN: one or two sentences
NOTE: format (TikTok-native first), the shelf life of the trend, compliance
```

RIDDEN trends are listed in one line each with who rides them; if worth entering, they get a Section 2 takeover card instead.

---

### Section 5: Angles by sophistication stage

The same angles sorted for planning a batch: Stage 2 (bigger, specific claims), Stage 3 (new mechanism reframes), Stage 4 (mechanism amplification, checkable specifics), Stage 5 (identity). One line per angle: Angle n (Name): Cluster, ICP. Include takeover and trend angles.
**Balance check box:** a first batch covers at least three stages; say where the client's longest runners sit and where the open ground is.

### Section 6: Headline library
60-80 headlines pulled from the cards, grouped by emotional doorway (e.g. Recognition, Partner / Love, Freedom, Vindication, Comfort, Proof / Skeptic, Identity, Objection). Each ends with its angle number. All are our words, no quotation marks.

### Appendix: raw buyer language
Verbatim quotes by theme, each with platform, who, and URL. Close with a **sentiment read** box: the loudest single line in the market and what must come before any claim.

### Last page: how to brief a new ad from this document
1. Pick a cluster or a takeover card. Look at what is missing from the current rotation.
2. Pick an angle that matches the ICP you are targeting; Section 5 shows its stage.
3. Pull the hooks. Test 4-6 openings on the same body.
4. Apply the persuasion stack from the DRIVE document and mark its non-negotiables on the brief.
5. Match the format (the DRIVE format matrix applies).
6. Hand it off clean: copy the BASIS quote into the brief's real-voice field, flag only the traps that could catch the copywriter (DRIVE claim guardrails), and stop before body copy.

Closing line: the clusters and ICPs are different doors into the same room, plus the count line (N pain clusters, N ICPs, 1 Big Idea, N angles: N takeover, N library, N trend).

---

## Quality checks before it ships
1. Every competitor-run angle in `03-angles.md` Step 3 (PROVEN / CROWDED / EMERGING) has a Section 2 takeover card with an ad link, exact copy, days running and target. None dropped.
2. The client's own proven ads are covered first.
3. Every BASIS quote is verified (`verify_quotes.py`) and 15 words or fewer, with a URL.
4. `mechanism_check.py` shows 0 REWORD lines for all mechanism tie-ins and hooks.
5. No hook names a competitor or sits in quotation marks.
6. Every claim sits under the evidence ceiling in `01-science.md`; objection angles the site contradicts are on HOLD.
7. Each trend angle carries its evidence and act-by window.
8. Counts in Section 1 match `01-counts.md`.
9. Dell's terms only: ICP, Mechanism (problem + solution), Angles, Hooks, plus the labels his own documents use (DRIVE angle numbers, Stage, Lane). No other internal framework labels.
