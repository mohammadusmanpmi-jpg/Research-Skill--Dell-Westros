# Phase 0B – Client account, business context and offer audit → `00-account.md`, `00-business.md`, `00-offer-audit.md`

Runs right after the Phase 0 brief and before Phase 1. It answers three questions before any new research is spent:
1. **What already works for this client?** We iterate proven ads before inventing new ones.
2. **What business situation are we in?** Traffic, clones, the price floor, competitor size and account health.
3. **What on the client's side will kill any ad?** These become the "client-side fixes before any ad runs" in the DRIVE Strategy.

Every finding carries a link, a screenshot reference or the tool call that produced it. Anything the client must supply is asked for in the menu, never guessed.

---

## 1. The client's own ad account → `00-account.md`

**Pull everything the client has run.** Get live ads, stopped ads and removed ads, across every page the brand uses, including sister pages.

| Route | How |
|---|---|
| TrendTrack | `lookup` (brand / domain), then `search_ads` with `query` = the brand or domain, `search_in: brand` and then `domain`, `status: all`, `sort_by: longestRunning`. Run it again with `sort_by: reachDelta7d`. Then `scan_ad` on the 10-20 longest-running ads |
| Meta Ad Library (browser) | Search the brand name and every page name, country = the market and then All. Use Active, then All. Note any "removed" / "ran without a disclaimer" notices and disabled pages |
| TikTok | `search_tiktok_library` with `handle` or `domain` = the client, `type: ad` |
| Client export (ask) | An Ads Manager export (ad name, spend, hook rate, hold rate, CTR, CVR, ROAS, days live) and any rejection or restriction emails. This is the best source when the client can share it |

**Record each ad in `01-ads.jsonl`** with `"owner": "client"`, using the same fields as competitor ads, plus:
- `page` – the page it runs on
- `landing_url` – where it sends people
- `status` – live / stopped / removed

**Then write `00-account.md`:**
- **Proven on account:** every client ad running 30+ days, or with the best metrics in the export. List days, format, hook (verbatim), angle, ICP, landing page and media link. **These are iterated first** (Phase 3 Step 3).
- **Tested and stopped:** what was tried and for how long, so we don't sell an old test as a new angle (e.g. "'My wife used to flinch when I touched her' ran 24 days").
- **Removed or rejected ads and disabled pages:** count them and give the likely reason (claim words, borrowed creative, persona). This feeds the claim guardrails.
- **Borrowed creative:** client ads that name another brand, a reseller or "TikTok Shop", or that copy a competitor's ad.
- **Landing-page map:** which ad goes to which page, and any mismatches (one ad sending traffic to four different pages, or the men's ad landing on the women's page).
- **Live claims check:** review counts, customer counts, survey numbers and percentages on the site and in the ads. Check each one against its live source (Judge.me, Trustpilot, Amazon). Record what the site says next to what the source returns today.

## 2. Business context → `00-business.md`

| Item | How | Output |
|---|---|---|
| **Traffic trend** | TrendTrack `brief_competitor` on the client domain (and the top competitors), or Similarweb in the browser | Monthly visits for the last 6-12 months, and the change since the peak |
| **White-label clones and price floor** | Search the exact ingredient list and the formula wording on Amazon, Walmart, Google Shopping, TikTok Shop and the local marketplaces. Also `search_shops` / `find_similar_shops` | Every brand selling the same formula, with its price and link. **The price floor** is the lowest price for the same formula |
| **Competitor revenue and scale** | `brief_competitor` (estimated revenue, best sellers, top scaling ads) for the top 5-8 competitors | Revenue estimate, ad count, guarantee length and main angle per competitor. Label these as estimates |
| **Account health** | From § 1 plus the client: removed-ad count, disabled pages, active pages left, any restriction | One line: how much risk the account can take. It sets the claim posture and the launch-batch size |
| **Market sophistication signal** | How many competitors run the same core claim ("blood flow", "nitric oxide"), from `01-ad-matrix.md` once Phase 1 has run | Feeds the sophistication map |

Write a **strategic situation paragraph** (5-8 sentences): what the brand sells, at what sophistication, against which clones and leaders, on what account health, and the one thing it can win on. It opens the DRIVE Strategy executive summary.

## 3. Label, dose and offer audit → `00-offer-audit.md`

Check each item on the live site, the label (photo or PDF), the checkout and the ads:

| Check | What to record | Typical fix |
|---|---|---|
| **Ingredient amounts** | Is the amount per serving shown for every ingredient? | "Publish the amount of every ingredient" |
| **Dose wording** | Every way the dose is written on the label, site, FAQ and ads ("2 droppers (2 mL)" vs "2 drops") | "One dose everywhere" |
| **Guarantee vs refund policy** | Guarantee length on every page, compared with the refund policy's actual terms (opened bottles? time window? who pays return shipping?) | "One guarantee everywhere, matching the policy" |
| **Auto-refill / subscription default** | Is subscribe ticked by default at checkout? How do you cancel? | "Untick auto-refill by default" |
| **Real buy box** | Every bundle exactly as shown: units, price, price per day, free-shipping threshold, which bundle is marked best seller | The offer architecture in IGNITE is built on these real prices |
| **Numbers on the site** | Every review, customer and survey count, and whether they agree with each other and with the live source (§ 1) | "One set of honest numbers" |
| **Unsupported claims** | Claims on the site and in the ads that Phase 1's science check can't support (disease claims, absorption percentages, day-by-day timelines) | "Pull claims the research could not support" |
| **Borrowed creative** | From § 1 | "Retire borrowed creative" |
| **Address, contact, policies** | Is there a real address and contact route, and can the policies be found? | Trust fix |

**Output:** a numbered list, **"Before any of this runs: N fixes on the client's side"**. Each fix gets one line on what to change and one line on why, with the evidence (a link or a complaint count). It goes straight into the DRIVE Strategy after the executive summary.
