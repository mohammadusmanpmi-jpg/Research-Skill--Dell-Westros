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
- The user may ask for one phase only. Run only that phase.

## 3. Everything comes from the target market

- Sources must be local to the market: local-language forums, review sites, marketplaces, media, search trends and competitor ads **in that country**. Reddit and US sources are allowed only as a supplement, never as the base.
- Search in the market's language. Quote verbatim in the original language, with a short English gloss if the user needs it.
- Competitor ads: use TrendTrack when it is connected, filtered to the market's country; otherwise the Meta Ad Library for that country.
- Every quote and every ad keeps its source link. No link, no record.

## 4. Check existing research first

- Before collecting anything, look in `/mnt/project-files/research/` (or `research/<brand-slug>/` in the project folder) for earlier outputs.
- If existing research already covers the ask, say so, point to the files, and list only what is missing. Do not repeat work that is already on disk.
- Save every new output under `/mnt/project-files/research/<brand-slug>/` (or `research/<brand-slug>/` when there is no shared folder), using the file names the `research` skill defines.

## 5. Prioritise what competitors have not used

- Assume competitors already test the obvious angles. Validate every angle against their ads (OPEN / EMERGING / PROVEN / CROWDED / ABANDONED / NOT VALIDATED) and lead with OPEN and EMERGING angles and with avatars competitors do not address.
- Every angle and avatar is backed by verbatim quotes and source links from the market.
- Angles competitors already run are not dropped: give a take-over plan (new mechanism, new avatar, new proof, sharper words).

## 6. Optional weekly trend scan

- If the client wants it, set up a weekly routine that only spots **new trends in the target market**: new competitor ads, new products, rising search terms, new complaints in local forums.
- The scan reports what is new since last week with links. It does not re-run the full research and does not generate angles unless asked.
- Save each scan as `/mnt/project-files/research/trends/<YYYY-MM-DD>.md`.

## 7. Setting up a new client project

When asked to set up a client, collect and record:
- client name, product and website,
- target market: country, language,
- competitors already known,
- whether the weekly trend scan is wanted.

Then write the project instructions from this file and the `research` skill, and add this repository to the project so every thread has both skills.
