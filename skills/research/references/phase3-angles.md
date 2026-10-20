# Phase 3 – Angle and avatar exploration → `03-angles.md`

Goal: angles and avatars we can win, every one validated against what competitors actually run.

Assume competitors do research too. Any angle that is obvious from customer data is probably already in their ad accounts. So:
- Never present an angle without its validation flag and the evidence behind it.
- A competitor using an angle is **not** a reason to drop it. A long-running competitor ad is proof the angle sells. The job is to find how we take it over: different mechanism, different avatar, sharper words, stronger proof.
- An angle nobody runs is not automatically good. Check whether it was tried and stopped (ABANDONED), and whether customers actually talk about it (VOC count). White space with no VOC demand is a guess.

Inputs: `02-consolidation.md` (required), `01-ad-matrix.md` + `01-ads.jsonl` + `01-ad-searches.md` (required for validation; if missing, every angle is flagged `NOT VALIDATED – no ad data` and the user is told to run the Ads collector), `01-competitors.md`, `02-drive.md`, `definitions.md`, `03-results.md` if present.

Client-facing output: after Steps 1-8, write `03-angle-exploration.md` from `angle-exploration-template.md`. It must open the angle library with a **competitor takeover** section: for every angle a competitor runs now, "This angle is currently running from [competitor]" (exact copy, ad link, days running, who they target), then "Here's how we dominate it" (adopt what is proven, improve it: our ICP, mechanism, proof, format, hooks). Then the open angles, then the trend angles.

Course additions: read course-playbook.md § 5 before this phase. Every angle cites its research insight and fills the extra angle-card fields (§ 5.1); avatars use the persona split (§ 5.2); test batches pass the creative diversity check (§ 5.3); every hook records framework, awareness level, source quote and open loop, and passes the loop test (§ 5.4); hook and loop structures are validated against competitor ads like angles; offer notes per angle (§ 5.5); results use the metric chain (§ 7).

## Step 1 – Competitor map

From `01-ad-matrix.md` and `01-competitors.md`, write:
- **What each top competitor owns**: per competitor, their 2-3 main angles, avatar, mechanism story, proof type, longest-running hook (verbatim).
- **The category's default story**: the angle + mechanism + avatar most competitors share. This is what the market is tired of.
- **Mechanism claims in use**: every mechanism phrasing competitors use, so ours can be distinct.

## Step 2 – Avatar gap map

Compare who competitors talk to (avatar column of `01-ad-matrix.md`) with who talks in the research (segment and identity counts in `01-counts.md` / consolidation S9).

| Avatar | VOC quotes | VOC band | Competitor ads | Ad status | Gap verdict |
|---|---|---|---|---|---|

Gap verdict:
- **OPEN AVATAR** – high VOC (MODERATE+), 0-2 competitor ads. Strongest opportunity.
- **UNDER-SERVED** – high VOC, competitors present but with generic messaging (no avatar-specific scene, words or proof).
- **CONTESTED** – high VOC, PROVEN/CROWDED. Win with specificity (see Step 4).
- **THIN** – low VOC. Only test if cheap.

For each OPEN / UNDER-SERVED avatar, write a short avatar card: who, situation, their exact words (3 quotes with URLs), what they've tried, what they fear, and why competitor ads miss them (cite the ads).

Also scan the angle × avatar grid: an angle that is CROWDED for one avatar but empty for another is a ready-made opening (same proven angle, new person).

## Step 3 – Angle pool with validation flags

**Start with the client's own account.** If `00-account.md` exists, every client ad marked PROVEN ON ACCOUNT becomes the first candidate angle, flagged `PROVEN ON ACCOUNT`, and is iterated first (new hooks, new ICP, new format on the same proven angle) before new angles are invented. Ads under "tested and stopped" are not resold as new angles.

Build 12-20 candidate angles from: DOMINANT/HIGH pains, scenes, triggers; failed solutions with cost/duration; DRIVE reframe chains; verified or plausible mechanisms; identity statements; "this actually works" moments; gift patterns; open avatars from Step 2; UNRIDDEN and EARLY RIDERS trends from `01-trends.md` that link to VOC (keep their trend evidence and act-by window); TikTok-native angles from `01-tiktok.md`.

For each angle, validate:
1. Map it to an angle slug in `01-ad-matrix.md`. If no slug fits, run new searches (TrendTrack, then Meta Ad Library) with 3-5 keyword variants of the angle, active **and** inactive ads, market country and US. Append the searches and hit counts to `01-ad-searches.md` and add any ads found to `01-ads.jsonl`, then rerun `ad_matrix.py`.
2. Assign the flag:

| Flag | Meaning | Default move |
|---|---|---|
| 🟢 OPEN | No competitor ads found (searches logged) | Test, but confirm VOC demand is MODERATE+ |
| 🟡 EMERGING | Competitor ads exist, none 30+ days | Move fast; out-execute before it's proven |
| 🟠 PROVEN | 1-2 competitors running 30+ days | Proof of demand. Take it over with a different lever |
| 🔴 CROWDED | 3+ competitors running 30+ days | Only enter with a clearly new mechanism, avatar or proof |
| ⚫ ABANDONED | Tried and stopped within ~3 weeks | Find out why (bad execution vs bad angle) before retesting |
| ⚪ NOT VALIDATED | No ad data available | Do not rank above validated angles; tell the user |

Each angle's evidence line: `Searched: "<kw1>", "<kw2>" … on <source>, <date> → N ads from <advertisers>, longest <d> days`.

## Step 4 – Dominate plans (for PROVEN, CROWDED, EMERGING)

Do not drop these. For each, pick the levers (definitions.md § Differentiation levers) that the data supports and write:

```
### Dominate: <angle>
Who owns it now: <advertisers>, longest run <d> days
Their version: hook "<verbatim>" · mechanism "<theirs>" · avatar <theirs> · proof <theirs>
Our lever(s): <unique mechanism / new avatar / new villain / new proof / new scene / specificity / format / sophistication step-up>
Why it beats theirs: one sentence tied to data (a VOC complaint about their approach, a belief their ads leave unhandled, an avatar they ignore)
Rewrite:
  Theirs: "<their hook>"
  Ours A (<lever>): "<hook>"
  Ours B (<lever>): "<hook>"
  Ours C (<lever>): "<hook>"
Mechanism line (one sentence a customer can repeat): "<…>"
Compliance: safe / soften / needs citation
```

Example of the pattern (illustrative only; real output must cite the research):
> Competitors run "supports kidney health" with a generic herbal blend. Lever: unique mechanism + new villain.
> Theirs: "Support your kidneys naturally."
> Ours A (mechanism): "Your kidneys filter 180 litres a day. Here's what clogs the filter."
> Ours B (avatar): "For the dad who was told his numbers are 'borderline' and to come back in six months."
> Ours C (proof): "We showed the before/after lab panel. They showed a leaf."

Unique mechanism rules: it must be true (verified or plausible in consolidation 11B, compliance-checked), it must explain *why* the problem happens or *why* past solutions failed, and its name or phrasing must not match any mechanism in Step 1's list.

## Step 4b – Mechanism distinctness check

Put every mechanism line from Step 4 and every candidate hook in `ours.txt` (one per line) and run:

```
python scripts/mechanism_check.py research/<brand>/01-ads.jsonl ours.txt > research/<brand>/03-mechanism-check.md
```

Reword every REWORD line, then read the OK lines next to their closest competitor match for structural echoes (e.g. "warms from the outside" vs "warming the outside"). Rerun until 0 lines are flagged. A mechanism that sounds like a competitor's hands them the credit.

## Step 5 – Angle briefs (top 10 after validation)

```
### A<nn> – <angle name>      Flag: <emoji + status>
Type · Segment/avatar · Awareness · Desire (LF8) · Villain · Mechanism
Core statement: one sentence
Evidence (VOC): 3 verbatim quotes with URLs; theme count + band
Evidence (ads): searches + result (from Step 3)
Competitive position: open / take-over plan (link to Step 4 block)
Blocking belief → new belief → bridge
Proof required + asset needed
Compliance: safe / soften / needs citation
Scores (1-5): VOC demand · emotional charge · provability · differentiation vs competitors · format fit
Total
```

Angle card fields for the client-facing documents (DRIVE Strategy and Angle Exploration): ICP · sophistication stage · driver (LF8) · formats · basis (a verbatim quote of 15 words or fewer + URL) · 3 hooks · mechanism anchor · proof beats · CTA frame · production notes.

Rank by total. VOC demand and differentiation weigh most; a validated OPEN angle with weak demand should not outrank a PROVEN angle with a strong take-over lever.

## Step 6 – Hooks and openings (top 8)

Per angle: 5 hooks (different hook types, <15 words, built from verbatim customer words where possible, source quote marked), 1 opening scene (first 3 s from the scene map), 2 formats with a reason. Check every hook against competitor hooks in `01-ads.jsonl`; reword any that is a near-copy.

## Step 7 – Test plan

| Rank | Angle | Flag | Avatar | First hook | Format | What must be true to win | Kill criteria |

Budget split for the test plan: about **60%** iterating proven angles (the client's PROVEN ON ACCOUNT ads and takeovers of competitor PROVEN angles), **30%** OPEN / EMERGING angles and new ICPs, **10%** wild cards (TEST-lane angles, UNRIDDEN trends).

Batches of 3-4; each batch mixes at least one OPEN/EMERGING angle with one take-over of a PROVEN angle, and at least two avatars, so every batch teaches something. Ask the user for their account benchmarks (hook rate, CTR, CPA) for kill criteria if unknown.

## Step 8 – Results loop (`03-results.md`)

When the user reports results, append: angle id, flag at launch, hook, format, metrics, verdict, one-line why. Next run: read it first, retire losing themes, create variations of winners, re-check flags (an OPEN angle may have become EMERGING since), and fill the Creative DNA template in `02-drive.md` S20.

End with: top 3 angles to shoot first, the open avatar to test first, and the single asset needed to unlock them.
