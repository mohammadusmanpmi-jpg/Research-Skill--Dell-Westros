# David Briggs course playbook

Methods from David Briggs' ECOMM Architects copywriting course (v2, 30 modules), arranged by research phase. The rest of the skill already follows the course's structure (DRIVE, the desire matrix, the Default Desire Trap, Trust / Identity / Risk objections, angle scoring). This file adds the detailed methods behind those steps. Each phase file points to the section it needs.

Source: `David Brigs Course.docx` in the project Library (transcripts 1-30). Transcripts 2 and 22 (advertorials) have no file, and 17 (show, don't tell) is a duplicate of 16, so those modules are not covered.

**House rules win where the course differs.** See § 9.

---

## 1. Phase 0 additions – website brief

**Means-end chain (M5).** For every feature in `00-extraction.md`, write: Feature → functional benefit → emotional payoff → Life Force 8 driver.
Example: breathable bamboo fabric → keeps you cool → sleep through, wake energised → comfortable living + survival.

**Plain-outcome translation (M19).** Pair each spec with the plain outcome, in customer words where VOC exists. "Patented compression lock technology" → "Run all day, never get a blister."

**Funnel score (M9).** Score 1-5 each: price point · category familiarity · complexity · visual impact of results · technical differentiation.
- Low total (cheap, obvious, visible result) → ad straight to product page.
- Middle → advertorial or listicle bridge.
- High (complex, expensive, benefit not obvious) → VSL.
- Flag **premium in a commodity category** (e.g. $50 socks, $200 blue-light glasses): it needs a value-education step. "People don't have a price problem, they have a value problem."

**Offer and proof inventory (M7, M23, M25).**
- Guarantee length and terms. Flag under 30 days; 90 days "works really effectively".
- Usage timeline: when early wins show, when the full result shows. This becomes the realistic-timeline offer (e.g. "three months is the minimum", then a 3-month bundle).
- Proof on hand, by tier: UGC video > UGC images > text testimonials > named reviews, counts, third-party tests, media mentions.
- Does the current page continue the angle and avatar of the current ads? (ad-to-page continuity)

---

## 2. Phase 1 additions – collection

### 2.1 Extra sources (M6, M8, M9, M10, M12, M21, M30)
Add to the source menu when available:

| Source | What it reveals |
|---|---|
| Customer service logs (first-party) | Most common objections. "How does it work?" = low awareness; "Which bundle?" = high awareness |
| Pre-purchase questions | Beliefs and doubts before buying |
| Return reasons | Expectation gaps, overpromise |
| Post-purchase survey ("What almost stopped you buying?", "What else have you tried?") | Real objections, failed alternatives |
| Repeat-buyer reviews and "when I stopped using it" lines | Hidden desires such as regression avoidance ("I noticed when I stopped") |
| Competitor ad comment sections | Self-identification ("that's me"), category distrust ("none of these work") |
| Adjacent niches that share an ideology (swim goggles ← ski and cycling DR brands) | VOC and ads when the direct category is thin |
| Organic viral content (TikTok, influencers) | How attitudes in the category are shifting now |
| Indirect competitors in the same problem space (back brace ← cushions, wraps, supplements) | Missed opportunities to own |

First-party sources need the client's data. Ask for them in the menu; never invent them.

### 2.2 How to read reviews (M6)
- **Weight by star band.** 2-3 stars (and 4) are the goldmine: "no one flicks two, three, or four stars... without having a thought process behind it." 5-star teaches little. In 1-star, filter out shipping, logistics and service complaints first.
- **Start with 100-200 reviews** per product (own, competitor, Amazon), with ratings.
- **Look for four patterns:**
  1. **Frequency** – words and phrases repeated across dozens of reviews. Flag any word that appears 10+ times as a hook candidate.
  2. **Emotion** – exclamation marks, capitals, feeling words ("I actually cried looking at my skin").
  3. **Contradictions** – where reviewers disagree (in your own reviews this can mean the ads oversell).
  4. **Surprise** – benefits nobody expected. These are untapped angles.
- Also note what customers mention first.
- **Never paraphrase.** "Use the exact phrases, do not let AI paraphrase for you."

### 2.3 Extra fields to capture per quote (M15, M18, M23)
These are new tags added to the existing `tags` list in `01-quotes.jsonl`. Use them alongside SCENE, FAILED SOLUTION, COST etc.:
- `MOMENT` – one frozen scene where the problem became unbearable ("lying on the bathroom floor").
- `OBSERVER` – someone else noticing ("my husband noticed before I told him").
- `SELF-EXCLUSION` – "it doesn't work **for me**", which is not the same objection as "it doesn't work".
- `LAPSE` – what happened when they stopped using it.
- `REPEAT BUYER` – a repeat purchase, and why.
- `CONSEQUENCE` – what gets worse over time if left alone.
- `TIMELINE` – how long until it worked.

Record money wasted in `cost` and the number of failed products in the quote's FAILED SOLUTION tag (the count stays in the verbatim text). Add an optional `rating` field (1-5) for reviews, so the 2-3 star band can be filtered.

### 2.4 Competitor ads (M4, M21, M30)
- **Winning-ad signal:** active, running 15+ days (really 30+), with several variations. "People tend not to leave ads running if they are on profit." This matches the PROVEN threshold in Phase 3.
- Use the **Active** filter for "what works now"; keep inactive ads for the ABANDONED check.
- **Find long-form funnels:** sort by longest video (1:20+) and look for "Learn more" CTAs. These usually lead to VSLs and advertorials.
- **Teardown fields per ad** (add to `01-ads.jsonl` notes):
  - hook type
  - awareness level
  - sophistication stage
  - belief shift (from → to)
  - mechanism: real or just a label
  - open loop and where it pays off
  - proof types used
  - close and offer
  - why it stopped the scroll
- **Beat breakdown for the 3 best winners:** timestamp each beat, then note what each line does and why it works. Borrow the skeleton, never the words. "We are not copying other people's ads because their ads will be at different sophistication levels."
- An ad library is not research until each ad is annotated with why it works.

---

## 3. Consolidation additions (M6, M7, M28)

Add a **Review analysis** block to `02-consolidation.md`:
- Top 5 repeated emotions (with counts)
- The expectation gap: what 5-star reviewers say vs 2-3 star, and why
- 3 surprise benefits
- 10 customer phrases usable verbatim

Add a **Buyer-language bank** (hook bank):
- The 10 most-repeated problem phrases
- The 5 most-repeated relief phrases
- Exact words only, grouped by emotion (frustration, hope, gratitude)
- Counts come from `count_quotes.py`

**Finding → use rules:**

| Finding | Becomes |
|---|---|
| Repeated emotion | The emotional core of the ad |
| Expectation gap | Before-after-bridge angle ("here's how others let you down") |
| Surprise benefit | Untapped angle (OPEN candidate) |
| Striking phrase | Headline or hook |
| Contradiction | Objection-led angle |
| Common objection no competitor addresses | Lead with it (OPEN candidate) |

---

## 4. Phase 2 (DRIVE) additions

### 4.1 Market diagnostic – awareness and sophistication from evidence (M9)
Keep them separate: "sophistication is about the market and awareness is about the customer." Answer with evidence, not guesses:
1. How new is the product to the market?
2. Can customers name competitors? (yes = solution-aware) Can they name yours? (= product-aware)
3. What does customer service get asked? ("How does it work?" = low; "Which bundle?" = high)
4. How many similar claims do competitor ads make? (many = stage 4-5). Most markets are stage 3-4.
5. What do 2-3 star competitor reviews say? ("Didn't live up to the hype" = overpromise; everyone saying the same thing = stage 5)
6. If a plain benefits ad was run: did it work (low stage) or flop with a good product (they've heard it before)?

**Lead by stage:**

| Stage | Lead with |
|---|---|
| 1-2 | The claim, plainly or enlarged |
| 3 | A new mechanism or reason behind the problem |
| 4 | The mechanism, amplified with proof, specifics and experts |
| 5 | Identity: "those work for others, not you; this is built for you" |

In stage 5, piling on proof or benefits can backfire.

### 4.2 Desire selection (M5, M10)
Extends S1-S4:
- **Spot → test power → map to LF8 → competitive check → lock in.** Test power on:
  - **scope** – % of VOC mentions, from counts
  - **urgency** – how badly they want relief now
  - **staying power** – does it keep coming back, and are new people still finding the problem?
- The most-mentioned desire is often the wrong lead. White space beats volume. If the top 5 competitors all lead with one desire, cede it unless a unique mechanism gives real differentiation.
- **Elevation strategy:** write one line per LF8 driver for the same product, weakest to strongest, and tag each with the awareness level it fits. A product-aware buyer needs social proof, not the mechanism.
- **Conscious vs unconscious desire:** what they'll admit ("healthier skin") vs what they really want ("people stop asking if I'm tired").
- Lock the winner as a one-sentence **Desire Statement**: "the compass for every piece of copy."

### 4.3 Objections (M7, M20)
Extends S6:
- **Five-step diagnostic:**
  1. Write the stated objection exactly.
  2. Ask what would have to be true for it to disappear.
  3. Ask what past experience created it.
  4. Name the real belief as one specific sentence (not "they don't trust it").
  5. Tag it Trust, Identity or Risk.
- **Fix by category:**
  - **Trust** – proof stacking; "show the science, don't claim it".
  - **Identity** – self-recognition; "it's not you, it's the approach".
  - **Risk** – guarantee, trial, price per day, price anchoring, outcome anchoring.
- **Four strategies:**
  - **Preempt** – only when the objection is near-universal (many 2-3 star mentions).
  - **Reframe** – especially price.
  - **Outprove** – some objections "only fall to evidence".
  - **Ignore** – objections from people the product isn't for.

  Never preempt a minority objection: it plants the doubt in everyone else.
- Price objections are usually mechanism-education problems, not reasons to cut the price.
- Don't name skepticism in copy ("you might be skeptical"). Use the customer's own words for doubt.
- Keep at least 5 objections per product.

### 4.4 Unique mechanism (M11, M23)
Add to the Reframe stage:
- Split it into the **mechanism of the problem** (the root cause that explains why nothing worked) and the **mechanism of the solution**. A two-part solution often fits: "one soothes, the other rebuilds."
- **Build steps:**
  1. What the category assumes.
  2. Where it fails (from the review expectation gap).
  3. What the product does differently.
  4. Name it.
  5. Link it to the benefit: "the mechanism isn't the benefit, but it's the reason the benefit is believable."
- **Three types:**
  - **existing** – a known feature, made fresh or accessible to a new group
  - **unspoken** – competitors have the feature but never named it, so we name it and own it
  - **transubstantiated** – an ordinary feature given a new name or meaning, and it must still describe a real function
- **Six-point test:** specific and easy to explain · explains HOW · distinct from competitors · tied to a major pain · memorable name · backed by proof. Labels like "BioSync formula" or "patented" fail.

### 4.5 Beliefs and category reframe (M12, M14)
Extends S9-S12 and S17:
- **Blocking belief** and **new belief**, each one specific, falsifiable sentence.
- **Blocking-belief types:**
  - self-exclusion ("works for others, not me")
  - explanation fatigue ("every solution is another theory")
  - category distrust
- **Belief-shift sequence:** validate → introduce doubt (as questions) → new information or an analogy → reframe → new path. One belief per piece, and never attack the old belief head-on (backfire effect).
- **Category reframe paragraph:**
  1. List what every competitor assumes.
  2. Find the flaw.
  3. Check that the flaw explains disappointment in the reviews.
  4. Write one paragraph: what they assume / why it fails / how we differ.
- **Positioning mode:**
  - **Product** positioning: a measurable advantage, stage 1-2.
  - **Category** positioning: stage 3-5, self-blame markets, or when the mechanism is the differentiator.

### 4.6 Working avatar (M8, M27)
Extends S7:
- One sentence each: **identity** (how they see themselves) · **belief system** (what they think causes the problem, and what they've tried) · **self-narrative** (the story they tell themselves, e.g. "Maybe this is just what 42 looks like").
- Demographics are optional: "avatar theater". **Litmus test:** a paragraph written from the avatar must sound different from what you'd write anyway.
- Add one gut-punch line from VOC per avatar (the PIG method: "Empathy isn't a soft skill, it's a research skill").

### 4.7 Story arc fit (M18)
For each segment, pick the arc that fits its beliefs:
- **Against all odds** – burned before, tried everything.
- **Real-world desperation** – opens on one worst moment; suits pain relief.
- **Discovery** – an unexpected source leads to a non-obvious mechanism; suits burnout or natural remedies.

The `moment` quotes from Phase 1 supply the opening scene.

---

## 5. Phase 3 additions – angles, avatars, hooks

### 5.1 Angle rules (M13, M5, M19)
- **An angle is not a hook.** One angle carries many hooks of mixed types.
- **Every angle cites the research insight it came from**, not a swipe file. "If you struggle to create angles, your research isn't deep enough."
- **Angle types** (add to the existing list): fear/loss · aspiration/identity · education/mechanism · social proof/authority · contrarian · comparison · story/transformation · urgency/timing.
- **Aim for 8-15 genuinely different angles.** Two fear angles count as one angle with two variations.
- **Rule of One:** one desire, one emotion, one argument, one avatar, one CTA per angle.
- **Angle card adds:**
  - target awareness level
  - sophistication stage
  - blocking → new belief
  - positioning mode (product or category)
  - recommended funnel (from the funnel score)
  - destination page hero line (ad-to-page continuity)

### 5.2 Persona split (M27)
For each avatar, keep product, offer, mechanism, price, guarantee and core promise identical. Change five things, each filled from tagged VOC:
1. **Voice** – how they describe the pain, in their words.
2. **Scene** – where it happens, their moment.
3. **Proof** – whose proof they trust (mums trust mums). Mirror effect: the person on screen looks like them.
4. **Stakes** – what they fear (dad: missing work; grandma: being the liability).
5. **CTA meaning** – what "yes" means to them.

Single-function products diversify by who uses them and where, not by inventing benefits.

### 5.3 Creative diversity check (M1, M26)
Meta's Andromeda treats near-identical ads as one creative: "diversity is your targeting." Each test batch must vary on more than one of: **angle · format · persona · hook style**. "Four headlines on the same photo" is one concept.

When iterating a winner, make a "cousin, not a twin": a persona swap, hook swap, scene swap or voice swap (founder ↔ customer). Rewording is a variation, not an iteration.

### 5.4 Hook frameworks and awareness (M15, M26)
Add to the hook types:

| Framework | Best for |
|---|---|
| Curiosity gap | Unaware, problem-aware |
| Objection flip | Solution-aware, skeptical |
| Mechanism reveal | Solution-aware, stage 3+ |
| Results statement (sourced stat + "here's why") | Product-aware |
| Self-recognition / call-out ("If you're over 60 and…") | Problem-aware, burned before |
| Contrarian claim | Solution-aware, stage 4-5 |
| Story opening | Unaware, problem-aware |
| Direct challenge | Strong-assumption audiences |

**Awareness → hook:**
- unaware → story or identity moment
- problem-aware → validate the problem, then hint at a fix
- solution-aware → challenge the category belief
- product-aware → proof and difference
- most aware → urgency, offer, risk reversal

**Every hook must be defensible (M15).** Record, per hook:
1. framework
2. awareness level
3. the research it came from (quote URL)
4. the open loop and where it pays off

**Open loop types (M16):** unanswered question · incomplete reveal · unexpected claim · story interrupt · mechanism tease.

**Loop test:**
1. Is the curiosity genuine?
2. Does closing it lead to the product?
3. Does it fit the awareness level?
4. Does it close before the CTA?
5. Could a competitor use the exact same loop? (If yes, rewrite.)

**Saturated structures.** Validate hook and loop *structures* against competitor ads too, not just angles. A structure every competitor uses is CROWDED even if the angle is OPEN.

**Specificity (M15).** Build hooks from quotes tagged MOMENT, OBSERVER, FAILED SOLUTION and from the `cost` field. "Specificity creates credibility... You don't have to guess."

Ship 3-5 hooks per angle and never judge an angle on one hook.

### 5.5 Offer notes per angle (M7, M9, M23, M25)
- Realistic-timeline bundle (from the Phase 0 timeline).
- Price per day.
- Anchor against the DIY stack or the clinic alternative.
- Money already wasted on failed alternatives.
- "This vs that" framing (Coke next to Pepsi), not "buy or not".
- Visible guarantee, with best-case / worst-case framing.

---

## 6. Proof hierarchy (M25)
Hardest to fake first: UGC video → UGC images → text testimonials. Then named buyers, specific stats, review counts, third-party tests, media mentions, a visible guarantee.

- "Cold readers don't trust you. So stack proof until you close the trust deficit."
- Proof must match the avatar and the specific doubt: acne-scar proof from a 20-year-old doesn't help a 50-year-old with wrinkles.
- Stage 4 markets lead with proof.

---

## 7. Results loop additions (M15, M29, M30)
When results come back (Phase 3 Step 8), find where the ad breaks:

| Metric | Benchmark | If weak, fix |
|---|---|---|
| Thumbstop | 90%+ | First frame |
| Hook rate | <20% bad, 25-35% OK, 40%+ good | First frame and first line |
| Hold rate | <30% bad | Body: loop not paid off, hook-body mismatch, unclear mechanism, weak proof |
| CTR | <1% bad, ~1.5% healthy | Promise too weak, no direct-response push |
| CVR | ~2% reference | Page: trust, proof, mechanism clarity, relevance |

- **High CTR with low CVR:** overpromise, ad/page mismatch, hollow promise, wrong page type, or price shock. "Check availability" buttons inflate CTR.
- **A body that keeps failing means a research re-check.** "Is it the wrong person in the wrong awareness stage? Am I speaking like it's level 2 market sophistication when actually it's level 4?" Re-run the market diagnostic (§ 4.1).
- Keep a one-sentence **Big Idea** at the top of `03-angles.md` and review it every quarter against what the market responds to.
- "Data tells you what to fix, not whether to give up."

---

## 8. Course DRIVE vs this skill's phases
In the course, DRIVE is the whole campaign loop. This skill covers the same ground:

| Course stage | What it covers | In this skill |
|---|---|---|
| Discover | Desires, LF8, awareness, sophistication, avatars | Phase 0, Phase 1, DRIVE 2.1-2.2 |
| Reframe | Belief block, mechanism, proof, objections | DRIVE 2.3, § 4.3-4.5 |
| Ignite | Emotion, story, dimensionalized scenes | DRIVE 2.4, § 4.7 |
| Variate | Angles × formats × personas × awareness | DRIVE 2.5, Phase 3 |
| Evolve | Feedback loop, back to research | Phase 3 Step 8, § 7 |

---

## 9. Where house rules override the course
- **Competitor angles.** The course's angle prompt says to avoid any overlap with competitor angles. We keep them and write a take-over plan (Phase 3 Step 4). The course itself allows competing "if you can prove your product is superior."
- **Numbers.** The course's example stats ("73% of marathon runners", "12,000 women") are illustrative. Every number in our output needs a source.
- **True stories only.** The course praises a competitor story that is "not hugely true". We record that as a tactic to spot in competitor ads, never one to use.
- **Local market first.** The course's examples are mostly US/UK. Sources and idioms come from the client's target market (Client Research Workflow § 3). The course agrees: native wording matters (UK "A-lister" vs US "red carpet").
- **AI judgment.** The course warns that AI is "confirmation-biased" and can't judge sophistication or which angles the market has seen. That is why every sophistication call and angle flag needs logged evidence.
