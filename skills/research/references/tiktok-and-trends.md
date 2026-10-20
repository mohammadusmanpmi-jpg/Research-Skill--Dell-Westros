# TikTok and trend spotting

Two additions to Phase 1:
- **§ A – TikTok collector:** a full collector covering TikTok Shop reviews, video comments, creator content and TikTok ads.
- **§ B – Trend scan:** finds what is rising in the target market right now and checks which trends competitors are not riding yet.

Both are limited to the client's **target market**: its country, its language, local creators and local news. US content counts only as a labelled supplement, never as the base (Client Research Workflow § 3).

---

## A. TikTok collector → `01-tiktok.md` (quotes into `01-quotes.jsonl`, ads into `01-ads.jsonl`)

### A.1 Access

| Route | Gets | Needs |
|---|---|---|
| **TrendTrack** `search_tiktok_library` | TikTok ads and organic videos: caption, hashtags, music, views, likes, shares, days running, media link | TrendTrack connected. Costs 1 credit per item, so keep `limit` small |
| **Claude in Chrome** on tiktok.com and the TikTok Shop | Comments, Shop reviews, creator profiles | Browser, with the user logged in |
| **TikTok Creative Center** (ads.tiktok.com/business/creativecenter) | Trending hashtags, songs, creators and top ads by country | Partly open; some views need a login, so use the browser |
| None of the above | — | Write a shortfall note. Never invent TikTok quotes |

First check whether **TikTok Shop is live in the market**. If it isn't, skip A.2 and say so in the summary.

### A.2 TikTok Shop reviews (where the Shop is live)
- **Search the Shop** for the category, for each competitor product, and for "<category> + dupe / alternative".
- **For each listing record:** product, seller, price, units sold (if shown), rating and review count.
- **Reviews:** read 2-3 star reviews first, then 4, then 1-star after removing logistics complaints. This is the same weighting as course-playbook § 2.2.
- **Target:** 50-100 reviews across the top 5-8 listings (floor 150 verified quotes from 8 listings; see phase1-collectors.md § Minimum depth).
- **Tags and fields:** PRODUCT EXPERIENCE, plus `rating` (1-5) and `source: "tiktok-shop"`.
- **Why it matters:** these are impulse buyers, so watch for expectation gaps ("looked different in the video") and "TikTok made me buy it" regret or delight.

### A.3 Video comments
- **Which videos:**
  - organic videos about the problem (searches and hashtags from the brief)
  - competitor ads
  - creator reviews
- **Selection:** pick 20+ videos with 50+ comments, using the local-language queries from the brief, and read the top 30 comments of each. Open reply threads with 5 or more replies.
- **What to capture:**
  - instant reactions ("need this", "does it actually work?")
  - skepticism ("it's an ad", "paid review")
  - "this is me" and tag-a-friend comments, which show self-recognition (IDENTITY tag)
  - price objections
  - gift intent
  - questions that reveal the buyer's awareness level
- Set `source` to `"tiktok-comments"` and `role` to `commenter`. Keep comments on the client's own ads separate, so they don't skew the research.

### A.4 Creator content
- **Find local creators** in the category with `search_tiktok_library` (`type: organic`, `countries: [<market>]`, `language: <market language>`, `sort_by: views` or `engagement_rate`), or by searching the browser.
- **Record:**
  - review, dupe and comparison videos ("I tried 5 X so you don't have to")
  - "TikTok made me buy it" content
  - stitches and duets that argue with a claim
  - before-and-after demos
- **Per video:**
  - creator handle and follower count
  - views and engagement
  - the opening line (verbatim)
  - the angle used
  - the format (talking head, green screen, demo, POV, skit)
  - which product, and whether it is paid (#ad, "partner")
- **Why it matters:** this shows how real people in the market talk about the problem. The words and formats feed hooks directly, and organic videos with high views and no matching competitor ad point to OPEN angles.

### A.5 TikTok ads
- Run `search_tiktok_library` with `type: ad`, `countries: [<market>]`, the angle keywords and `sort_by: days_running`. Make a second pass with `sort_by: views` to see what is scaling.
- Record each ad in `01-ads.jsonl` with `source: "tiktok"`, using the same fields as Meta ads (hook, hook_type, angle, avatar, format, days_running, media_url).
- The same winning-ad rule applies: active, running 15+ days (really 30+), with variations.

### A.6 Summary `01-tiktok.md`
- Counts per sub-source, plus a shortfall note.
- The 10 most revealing comments.
- Top 5 creator formats.
- Top 10 local phrases and slang for the problem, which feed the buyer-language bank.
- Shop review expectation gaps.
- TikTok-native angles not seen in Meta ads.

---

## B. Trend scan → `01-trends.md`

Run it as part of Phase 1, or on its own (menu option "Pick phases → Trend scan", and the weekly scan in the Client Research Workflow).

### B.1 Sources (all filtered to the target market)

| Source | How | Look for |
|---|---|---|
| **Google Trends** (trends.google.com) | Set `geo` to the market country, in the market language. Compare past 12 months with past 5 years. Check the category, the problem terms and each competitor brand | Rising queries and "Breakout" terms, seasonal peaks, new related topics, brands gaining search share |
| **TikTok Creative Center** trends | Pick the market country and the last 7 / 30 days. Check hashtags, songs, creators and top products | Hashtags and sounds rising in the category or near it, with views and posts |
| **TikTok search and Shop** | Trending searches on the category; Shop best sellers | New formats, new products, "dupe" waves |
| **TrendTrack** | `search_tiktok_library` (`sort_by: newest`, then `views`, `published_after` = 30 days ago, market country); `find_winning_products` (niche + keywords) for products gaining traction; `daily_radar` if competitors are tracked | New creatives taking off, winning products, competitor launches |
| **Local news and media** | Google News in the market language and country edition; the main national outlets and trade press | Health scares, regulation, celebrity moments, studies, seasonal or cultural events that change demand |
| **Local marketplaces** | The local Amazon "Movers & Shakers" and best sellers, and the leading local marketplaces | Products and sub-categories climbing fast |
| **Local forums and Reddit** (optional) | New threads on the problem in the last 30-90 days | New complaints, new solutions people are trying |

Log every search in `01-ad-searches.md` (source, query, country, date window, result).

### B.2 Record each trend

```
### T<nn> – <trend name>
Type: search · hashtag · sound · format · product · news · cultural moment
Evidence: <numbers + link + date>, e.g. "Google Trends AU, 'magnesium for sleep' +180% past 90 days" / "#nervoussystemreset 42k posts, +65% in 30 days (Creative Center, AU)"
Stage: EARLY (just starting) · RISING · PEAKING · FADING
Relevance: how it connects to the product, desire or pain (cite VOC themes if they match)
Competitors riding it: searched <keywords / hashtag / sound> on <TrendTrack / Meta Ad Library / TikTok>, <date> → N ads from <advertisers>
Flag: 🟢 UNRIDDEN · 🟡 EARLY RIDERS · 🔴 RIDDEN
Use: angle or hook idea, best format, and the window to act in
Risk: compliance, brand fit, or likely to fade fast
```

### B.3 Flags
Check each trend against competitor ads in the market before flagging it:

| Flag | Meaning | Move |
|---|---|---|
| 🟢 **UNRIDDEN** | The trend is real and rising, and no competitor ads use it | Act first: highest priority if it's relevant and EARLY or RISING |
| 🟡 **EARLY RIDERS** | 1-2 competitors started, under 30 days running | Move fast and out-execute |
| 🔴 **RIDDEN** | 3+ competitors, or ads running 30+ days | Only with a new twist (persona, mechanism, format) |

A FADING trend is never top priority, whatever its flag. A trend with no link to the product's VOC is a guess, so say so.

### B.4 Output
- **Top trends to act on:** UNRIDDEN and EARLY RIDERS, EARLY or RISING, ranked by relevance × stage. For each, give one angle and one hook idea, built from quotes where possible.
- **Seasonal calendar:** the peaks found in Google Trends for the next 12 months.
- **Watch list:** trends to re-check next scan.
- **For the weekly scan:** show only what changed since the last `01-trends.md` or `Trend Scan - <date>.md`: new trends, stage changes, and flags that moved (an UNRIDDEN trend now has riders).

Phase 3 reads `01-trends.md`: UNRIDDEN and EARLY RIDERS trends that link to VOC go into the angle pool as candidates, keeping their trend evidence.
