---
name: client-research-workflow
description: How research projects are run for Dell's clients (one project per client, local-market sources only, reuse existing research, prioritise angles competitors haven't tested, optional weekly trend scan). Use at the start of any research ask in a client project, before running /research, and whenever setting up a new client project.
---

# Client research workflow

This is the house workflow that wraps the `research` skill. Read it before any research in a client project.

## 1. One project per client

- Each client gets its own project (and its own folder / repo). Never mix two clients' research.
- Every client project has a **target market** on record: country, language and product. It lives in project memory or project instructions.
- If any of the three is missing, **ask before researching**. Do not guess the market from the website's domain or currency.

## 2. Research runs only when asked

- Research is the main job of the project but it is not automatic. Run it when the user asks ("research this", "find angles", "/research"), not on every message.
- When asked, run it through the `research` skill and its phases, in order:
  1. collect customer voice and competitor ads,
  2. consolidate them,
  3. map the emotional drivers (DRIVE),
  4. generate angles and avatars.
- A full run also starts with **the client's own ad account** (what already works is iterated before anything new is invented), the business context and an audit of the label, dose and offer (Phase 0B), adds a **science and authority** check for health products (the evidence ceiling and the claims we don't make), and ends with the client-facing **DRIVE Strategy Document** (Phase 4) and **Angle Exploration Document**.
- Use Dell's terms in everything client-facing: **ICP** (each buyer type; 3 obvious + 3 underserved, plus parked segments), **Mechanism** (problem mechanism + solution mechanism), then **Angles** and **Hooks**.
- The user may ask for one phase only. Run only that phase.

## 3. Everything comes from the target market

- Sources must be local to the market: local-language forums, review sites, marketplaces, media, search trends and competitor ads **in that country**. Reddit and US sources are allowed only as a supplement, never as the base.
- Search in the market's language. Quote verbatim in the original language, with a short English gloss if the user needs it.
- Competitor ads: use TrendTrack when it is connected, filtered to the market's country; otherwise the Meta Ad Library for that country.
- **TikTok is a standard source**, not an extra: TikTok Shop reviews (where the Shop is live in the market), comments on videos and competitor ads, local creator content, and TikTok ads, all in the market's country and language (`research` skill, tiktok-and-trends.md § A).
- **Every research run includes a trend scan** of the market: Google Trends for that country, TikTok trending hashtags and sounds, local news and local marketplaces. Each trend is checked against competitor ads and flagged UNRIDDEN / EARLY RIDERS / RIDDEN; lead with trends competitors aren't riding yet (tiktok-and-trends.md § B).
- Every quote and every ad keeps its source link. No link, no record.
- **Research is only done when it is deep enough and fully checked:** every source meets its minimum floor (e.g. Reddit 600 quotes from 120+ threads across 10+ subreddits; 2,000+ quotes across 6+ sources and 15+ platforms in total, aiming for 25-30 platforms including health forums for health products; see the `research` skill, phase1-collectors.md § Minimum depth), and **every** quote has been re-checked against its live link, not a sample. A source that can't reach its floor gets a logged shortfall, and the user is told before moving on.

## 4. Check existing research first

- Before collecting anything, look in `/mnt/project-files/research/` (or `research/<brand-slug>/` in the project folder) for earlier outputs.
- If existing research already covers the ask, say so, point to the files, and list only what is missing. Do not repeat work that is already on disk.
- Save every new output in the client's research folder (`/mnt/project-files/research/<brand-slug>/`, or `research/<brand-slug>/` when there is no shared folder). If that folder doesn't exist yet, ask before creating it (section 5).

## 5. Folders and file names

- **Ask before creating any new folder.** When starting a new client, new research or anything else with no folder for it yet, ask first: "There's no folder for this yet. Shall I create one called `<name>`?" Wait for a yes. Do not create folders silently, even when the user forgot to set one up.
- Keep each topic in **one flat folder**, with no nested sub-folders inside it.
- Give every file a clear, labelled name that says what it is, e.g. `Phase 2 - DRIVE Strategy.md` or `Install - Research Skill.skill`. Never leave a visible file named just `SKILL.md`, `README.md` or `notes.md`.

## 6. Prioritise what competitors have not used

- Assume competitors already test the obvious angles. Validate every angle against their ads (OPEN / EMERGING / PROVEN / CROWDED / ABANDONED / NOT VALIDATED) and lead with OPEN and EMERGING angles and with avatars competitors do not address.
- Every angle and avatar is backed by verbatim quotes and source links from the market.
- Angles competitors already run are not dropped: give a take-over plan (new mechanism, new avatar, new proof, sharper words).
- The Angle Exploration Document **leads with open angles no competitor has tested**, most of the document, each proved by logged searches with 0 ads and built with the David Briggs methods (white-space desire, open ICP, unspoken mechanism, category reframe, objection flips, story arcs, hook frameworks).
- After that, every competitor-run angle gets a dominate, differentiate or compete card with a full strategy (ICP, mechanism, proof, format, offer, timing): **"This angle is currently running from [competitor]"** with their exact copy, ad link, days running and who they target, then **"Here's how we dominate it"**: what we adopt, what we improve, and our ICP, mechanism, proof, format and hooks. Our mechanism and hook wording is checked against competitor phrasing (`mechanism_check.py`) so we never echo them.

## 7. Optional weekly trend scan

- If the client wants it, set up a weekly routine that only spots **new trends in the target market**: new competitor ads, new products, rising search terms, new complaints in local forums.
- Run it with the trend scan procedure (tiktok-and-trends.md § B): Google Trends for the country, TikTok Creative Center trends and new TikTok creatives, local news, local marketplace movers, TrendTrack `daily_radar` for tracked competitors. Report only what changed since the last scan, with each trend's UNRIDDEN / EARLY RIDERS / RIDDEN flag.
- The scan reports what is new since last week with links. It does not re-run the full research and does not generate angles unless asked.
- Save each scan as `Trend Scan - <YYYY-MM-DD>.md` in the client's research folder (ask before creating it, per section 5).

## 8. Setting up a new client project

When asked to set up a client, collect and record:
- client name, product and website,
- target market: country, language,
- competitors already known,
- whether the weekly trend scan is wanted.

Then write the project instructions from this file and the `research` skill, and add this repository to the project so every thread has both skills.
