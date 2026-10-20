# Phase 1 – Collectors

Each section is one source. Open-access sources can run as parallel subagents; give each subagent its section, the brief, the quote record format and the output paths. Browser-only sources run in the main session, one at a time.

## Quote record format (`01-quotes.jsonl`, one JSON object per line)

```json
{"id":"reddit-0001","source":"reddit","sub":"r/frozenshoulder","url":"https://...","date":"2025-03-14",
 "author":"u/…","role":"op|commenter|reviewer|answerer","engagement":142,
 "quote":"verbatim text, spelling untouched",
 "tags":["PAIN","SCENE"],"theme":"cant-sleep-on-side","segment":"self-buyer-45plus",
 "brand":null,"sentiment":null,"credential":null,"cost":null,"duration":null}
```

Fields:
- `tags` – from: PAIN, SCENE, EVENT/TRIGGER, SITUATION, FAILED SOLUTION, CURRENT BELIEF, VILLAIN, TRUST, BLOCKING BELIEF, IDENTITY, STATISTIC, CAUSE, SAFETY CONCERN, PRODUCT EXPERIENCE, PRE-PURCHASE QUESTION, QUESTION, CONFESSION, PARTNER/SOCIAL CONFLICT, COST, SKEPTICISM, DESIRE, UNEXPECTED
- `theme` – a short slug naming *what* the quote is about (`cortisone-wore-off`, `physio-too-expensive`, `feel-old`). Reuse slugs across quotes and across sources; this is what the counting script aggregates. Keep a running list in `01-themes.md` so collectors converge on the same slugs. Before inventing a slug, check the list.
- `segment` – one of the brief's segment slugs, or `unknown`.
- `brand` – product/brand named in the quote, if any. `sentiment` – positive/negative/mixed for PRODUCT EXPERIENCE.
- `cost`, `duration` – capture any "$400 later", "3 years", "6 weeks" mention as a number plus unit.

Rules that apply to every collector:
- Verbatim. No paraphrase, no spelling fixes, no truncation mid-thought.
- No URL → do not record.
- Recency: prefer the last 36 months; always record the date.
- Targets are targets. If a source blocks, rate-limits or is thin, stop and write the shortfall note in the per-source summary: what was searched, how many pages read, what blocked.
- Read reply chains, not just top posts. Page 2+ of forum threads, 2-3 levels of replies on Reddit/YouTube.

Per-source summary (`01-<source>.md`): record counts (quotes, threads/pages read), the frequency lists requested in that section, shortfall note, and "unexpected findings" with quotes.

---

## Reddit (open)
Use `https://old.reddit.com/r/<sub>/search?q=<query>&restrict_sr=on&sort=top&t=all` or append `.json` to thread URLs for comments. Run every query from the brief in every listed subreddit; also run the top 10 condition queries site-wide. Top 10 threads per query cluster per sub. Target 300 quotes.
Summary lists: top 10 pain phrases, top 10 failed solutions, top 10 scenes, top 5 triggers, beliefs, villains, blocking beliefs, trust authorities, identity statements, safety concerns, product experiences (pos/neg/mixed), unexpected.

## Forums (open)
Use the forum URLs in the brief; search with the forum queries. Top 10-20 threads by reply count per query. Read all pages. Note poster's post count and date. Target 150.
Summary: top 5 pain descriptions unique to forums, top 5 failed solutions with duration+cost, top 5 device experiences, top 5 entrenched beliefs, top 3 patterns absent from Reddit.

## Quora (partial – login usually needed for full answers; use browser if present)
Spaces first, then every query. Top 10 questions per query; all answers and comments; related questions with 5+ answers. Capture question titles (tag QUESTION) with follower/answer counts and any claimed credential. Target 100.
Summary: top 10 questions, failed solutions, beliefs, products mentioned, trusted authorities, credential types, anything new vs Reddit.

## Complaints (open)
Trustpilot, BBB, ComplaintsBoard, ConsumerAffairs, Sitejabber, ProductReview.com.au (market-dependent). Search the brand and every competitor. Read all 1-3 star entries; note total count, rating, date range. Complaint categories as `theme`: product-failure, safety, billing, delivery, customer-service, refund, quality, fit-comfort, cost, misleading, scam-accusation. No target: zero complaints is a data point.
Summary: top 5 categories, brands by volume, brands with zero, every scam/refund complaint against the user's brand, category-level (3+ brands) vs brand-specific complaints.

## Amazon (partial – often blocks scrapers; browser preferred)
Market domain + amazon.com. Each product search from the brief. Per listing: name, price, rating, review count; Top Critical first, then ~50-100 most-recent 1/2/4/5-star; the Q&A section (tag PRE-PURCHASE QUESTION). Filter negatives with the brief's phrases. For positives capture the "it works" moment, timeline, activity regained, sleep, medication reduction, gift purchase, repurchase. Target 200.
Summary: top 10 complaints, top 10 praises, return reasons, "this actually works" moments, gift patterns, pre-purchase questions, 3 best- and 3 worst-reviewed competitors, "switched to" mentions.

## YouTube (open, limited)
For each query, top 5-8 videos by views with 50+ comments. Note title, channel, views, sponsored or not. Read the top 50 comments and reply chains 2-3 deep. Capture every duration/cost mention. Target 150. If comments cannot be loaded without a browser, record what was reachable and note the shortfall.
Summary: pain timelines, failed solutions with duration+cost, videos with most pain-language comments (channel + style), device mentions pos/neg/mixed, unanswered questions, strongest single quote.

## Google (partial)
Autocomplete: for each seed and the modifiers (for / that / vs / without / best / why does / how to fix / is … worth) record every suggestion. People Also Ask: expand each box until no new questions; record question, snippet (2 sentences), source site. Related searches. Google often blocks automated access; try `https://www.google.com/complete/search?client=firefox&q=` for autocomplete, otherwise use browser, otherwise record shortfall. Record suggestions as quotes with tag QUESTION, theme by intent (problem-understanding, solution-seeking, product-evaluation, comparison, safety, cost, timeline).
Summary: full lists, 10 most revealing questions, 5 skepticism questions.

## Authority (open) → `01-authority.md`
Google Scholar, PubMed, Cochrane with the brief's queries; last 5 years; systematic reviews > RCTs > observational. Per study: title, first author, year, journal, n, one-line finding, SUPPORTS / CONTRADICTS / INCONCLUSIVE for the brand's claims, DOI. Regulators: registration status, what claims are allowed. Publications: what the trusted outlets say.
Output: evidence summary per claim; mechanism validation (verified / plausible / unsupported); regulatory status; compliance boundaries (say with citation / soften to "users report" / cannot say); mechanism opportunities; recognised experts and trusted channels.

## Social – Facebook Groups, TikTok, Instagram, X (browser only)
Only with Claude in Chrome. One source at a time, ~40 page loads max per source per run, pause between actions. Ask the user to allow each site when prompted.
- Facebook: group search terms from the brief; 10-20 largest active groups; inside each, search category term, condition, competitors, and the emotional / burden / social / money / professional / identity / drastic-action keywords. Top 10-15 posts per term, all comments. Extra tags: CONFESSION, PARTNER/SOCIAL CONFLICT. Target 100.
- TikTok + Instagram: queries, hashtags, competitor handles; 20+ videos/posts with 50+ comments; top 30 comments each. Target 100 combined. Separate any reactions to the user's brand's own ads.
- X: queries + brand names + "help / advice / worth it / scam" variants; top 20 by engagement; reply chains on 10+ replies. Target 75.
Summaries: Facebook – scenes, identity, peer recommendations and warnings, partner conflicts, definitions of progress, confessions. TikTok/IG – instant reactions, skepticism, validation phrases, price objections, gift intent, "this is me". X – real-time vents, cost complaints, skepticism, viral angles, language unique to X.

## Competitors – website teardown (open) → `01-competitors.md`
For each direct competitor in the brief (and the top 3 advertisers found by the Ads collector, if not already listed), fetch the product page and run the Phase 0.1 extraction in short form: price/offer/guarantee, hero feature, stated mechanism (and whether it's a real mechanism or a label), claims, proof and trust signals, objections handled, avatar the page speaks to, implied villain.
Output a comparison table (rows = brands incl. ours, columns = those fields), then: where we win, where we lose, where we're identical but worded differently, and every mechanism phrasing in use (Phase 3 uses this list to keep our mechanism distinct).

## Ads – ad intelligence → `01-ads.jsonl`, `01-ad-searches.md`, `01-ads.md`
Source priority (use the first available, add the next ones if coverage is thin):
1. **TrendTrack MCP** (`mcp__Trendtrack__*`) – see the playbook below.
2. **Meta Ad Library in Chrome** – https://www.facebook.com/ads/library – market country then US; Active then All (inactive ads reveal angles that were tried and dropped).
3. Neither available → write `01-ads.md` with "NOT COLLECTED – no ad data source", so Phase 3 flags every angle NOT VALIDATED.

### TrendTrack playbook

TrendTrack spends credits. Before collecting, call `check_credits`, tell the user the remaining balance, and propose a budget for this run (typical full competitor pass: 150-400 credits; TikTok and Google library cost 1 credit per returned item). Stay inside it and report credits used at the end.

Use only read tools. Never call write tools (`add_to_brandtracker`, `create_board`, `add_board_item`, share links, folder moves, deletes) unless the user asks: they change the user's workspace.

1. **Resolve competitors** – `lookup` (q = brand or domain) for each competitor in the brief; `search_advertisers` (query = category terms, `country` = market, `sort_by: activeAds`) to find advertisers the brief missed. Add real ones to the competitor list.
2. **Competitor briefs** – `brief_competitor` (competitor = domain) for the top 5-8 competitors: traffic, estimated revenue, best-selling products, email strategy, top scaling ads. Feed the snapshot into `01-competitors.md`.
3. **Each competitor's ads** – `search_ads` with `query` = brand or domain, `search_in: brand` or `domain`, `status: all`, `sort_by: longestRunning`. Then again with `sort_by: reachDelta7d` for what is scaling right now. Gives first-seen, days running, duplicates (variations), estimated spend, media link.
4. **Angle searches** – for every angle/theme from the brief and consolidation, `search_ads` with `query` + `keywords` (3-5 phrasings of the angle in customer and marketer words), `search_in: ad_copy`, `status: all`, `sort_by: longestRunning`, `ad_countries: {include:[<market>]}` and a second pass for US if the market isn't US. Important: always pass `sort_by` (or `trend_signal: longest_running` / `relevance`). Without it, the tool defaults to 7-day reach growth and silently drops ads with no recent reach, which hides abandoned angles.
5. **Avatar searches** – repeat the key angle searches with `sex: men` / `sex: women` and `min_age` / `max_age` bands matching the brief's segments. Zero hits for an angle in one avatar band = evidence for an open avatar.
6. **Hooks and structure** – `scan_ad` (pass `collation_id` from search results) on the 15-25 longest-running or fastest-scaling ads: opening hook (from transcripts), copy framing, creative structure, landing page, scaling verdict.
7. **Tracked brands** – if a competitor is already in the user's Brand Tracker (`list_tracked_brands`), use `get_brandtracker_scaling_ads` (rank movers 7d/30d) and `get_brandtracker_transcripts` (full video scripts) – the best source for the mechanism and avatar each competitor uses. If not tracked, suggest which competitors the user could add; don't add them yourself.
8. **Other channels (optional, credit cost per item)** – `search_tiktok_library` (`type: ad`, query = angle) and `search_google_ads_library` when the brief says the category runs there. Keep `limit` small.

Log every call in `01-ad-searches.md` (tool, query/keywords, filters, date, hit count, credits). Include each ad's media link (media URL, else thumbnail) in records and summaries.

Searches: the brief's keyword and advertiser lists, plus each competitor found in `01-competitors.md`. Log every search in `01-ad-searches.md`: source, query, country, active/all, date, hit count. Zero-hit searches matter: they are the evidence for OPEN angles.

Record every ad running 15+ days or with multiple variations, one JSON line each:
```json
{"source":"trendtrack|meta-ad-library|tiktok|google-ads","advertiser":"…","ad_id":"…","collation_id":"…","url":"…","media_url":"…","first_seen":"2026-07-02","last_seen":"2026-10-18","days_running":110,"active":true,"variations":4,"est_spend":12000,"reach":null,
 "hook":"exact first lines / first 3 s","hook_type":"…","angle":"kidney-filter-health","avatar":"men-50plus-borderline-labs",
 "mechanism":"their stated mechanism, verbatim-ish","desire":"LF8 #","villain":"…","awareness":"problem","proof":"…","format":"ugc","narrator":"…",
 "claimed_outcomes":"…","offer":"…","landing_url":"…"}
```
`angle` and `avatar` are slugs. Reuse the theme slugs from `01-themes.md` and the segment slugs from the brief where they fit, so ads and VOC line up; add new slugs to `01-themes.md` when needed. `avatar` is who the ad speaks to (age/gender/situation as shown in the creative and copy), not who the brand says it targets.

Then: `python scripts/ad_matrix.py research/<brand>/01-ads.jsonl --brand "<our advertiser name>" > research/<brand>/01-ad-matrix.md`

`01-ads.md` summary: hook-type map, format map, desire map, proof map, 5 longest-running ads (advertiser, hook, format, days), our own ads audit (what we run that they don't, what they run that we don't, any red flags from 0.1).

---

## After all collectors

1. `python scripts/count_quotes.py research/<brand>/01-quotes.jsonl > research/<brand>/01-counts.md`
2. Verification: sample 10% of records (min 10, spread across sources), reopen each URL, confirm the quote text appears. Remove failures from the jsonl, rerun the count, write `01-verification.md` (sampled, passed, removed, by source).
3. Proceed to `phase1-consolidation.md`.
