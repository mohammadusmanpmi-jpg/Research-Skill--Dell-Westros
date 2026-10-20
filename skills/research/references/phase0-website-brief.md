# Phase 0 – Website extraction and Research Brief

Two steps. Step 0.1 reads the site and records only what is on the page. Step 0.2 turns that into the brief that fills every placeholder in Phase 1.

Fetch each URL fully (product page, landing page, about, FAQ, reviews page). If a page is JavaScript-rendered and WebFetch returns little, use the browser if available; otherwise note "page did not render" and work with what loaded.

---

## 0.1 Website extraction → `00-extraction.md`

Record only what is on the page. For a missing item write `NOT FOUND ON PAGE`. Items marked *(inference)* are the one exception: label them clearly as your inference, not page content.

### PRODUCT
1. Product name (exact)
2. Product type / category (what it physically is)
3. Price and offer structure (full, discounted, bundles, subscription, shipping, guarantee)
4. What is in the box (quantity, size, contents)
5. How to use it (instructions, duration, frequency)

### PROBLEM
6. Problem the product claims to solve (exact language)
7. Who it is for (stated targeting)
8. How severe/urgent the page makes the problem sound

### MECHANISM
9. How it claims to work (ingredient, technology, process)
10. Real explanation or label? ("BioSync Formula" = label; "blocks DHT at the follicle" = mechanism)
11. Studies, research or authority cited (exact citations)
12. Specific numbers, statistics, data points

### FEATURES
13. Every feature, exact wording
14. For each: FEATURE (what it has/does) or BENEFIT (what the customer gets)
15. Hero feature (most space, first, visually highlighted)
16. Supporting features
17. Anything claimed unique / exclusive / patented / proprietary / "only"
18. Features with numbers attached (wavelength, dosage, runtime, weight…)
19. Category-standard features presented as special (positioning tell)
20. *(inference)* Features competitors in this category usually list that this page omits

### CLAIMS
21. Every specific claim: exact wording, substantiated or not, type (health / performance / comparison / experience)
22. Testimonials or reviews on page: how many, real or templated
23. Before/after shown: what it shows

### COMPETITIVE POSITIONING
24. Competitors named
25. Comparisons to alternatives
26. Category it positions against ("unlike regular kibble")
27. Implied villain (what is wrong with current solutions)

### TRUST AND PROOF
28. Trust signals (guarantee, review count, stars, badges, media logos, certifications)
29. Objections handled, and how
30. Questions left unanswered

### RED FLAGS
31. Inconsistencies or contradictions
32. Claims needing verification before ad copy
33. Compliance risks (health claims without citations, before/after implying medical outcome, testimonials promising results)

### BRAND
34. Brand name
35. Founding story
36. About / mission
37. Country, market, currency (from domain, pricing, shipping)
38. Social accounts linked

---

## 0.2 Research Brief → `00-brief.md`

Rules:
- Every subreddit, forum, Quora Space and competitor must be real. If you cannot confirm one exists (search for it), leave it out. Eight real entries beat fifteen padded ones.
- Every forum gets its exact search-page or board URL.
- Queries are written the way a person types them: lowercase, conversational, no marketing language.
- Separate DIRECT competitors (same product type) from SOLUTION competitors (different approach to the same problem, incl. professional services with typical cost).
- Group queries by intent, not platform.
- Use the current year in any "best X <year>" query.

### Category adaptation (do this first)

The query groups below were written for pain/health products. Decide which apply to this category and mark the rest `N/A – <reason>`. Replace inapplicable groups with ones that fit, for example:
- Pet products → owner guilt, vet cost, behaviour scenes, multi-pet households
- Skincare/hair → visibility/photos, social embarrassment, routine fatigue, ingredient skepticism
- Food/supplements → taste, compliance ("forgot to take it"), label distrust, subscription fatigue
- Devices/gadgets → setup friction, battery, durability, "gimmick" skepticism

### Brief format

```
### BRAND AND PRODUCT SUMMARY
BRAND / PRODUCT / MECHANISM / MARKET (country, currency, language) / PRICE POINT / GUARANTEE / SHIPPING
PROBLEM (customer language): 3-4 versions of how different customers describe it to a friend
PRODUCT CATEGORY: 4-5 search terms for this product type
CONDITIONS/PROBLEMS TARGETED: every one named on the page

### CATEGORY ADAPTATION
Which query groups apply, which are replaced, with what.

### COMPETITORS
Direct (6-8): brand + exact product name
Solution (up to 6): remedies, OTC, professional services with cost/session, competing technologies, DIY

### TARGET AUDIENCE
One paragraph: gender skew, age range, occupations, what they already tried and why it fell short, the purchase trigger moment, emotional state at purchase, gift-buyer segment if any.
Then list 2-4 SEGMENT SLUGS (e.g. `self-buyer-45plus`, `gift-adult-child`, `athlete`) – collectors tag every quote with one of these.

### REDDIT
Subreddits (as many real ones as exist, up to 15)
Queries by intent (adapt groups per category):
  Condition/symptom language (12-15)
  Daily life impact (10-14)
  Failed solutions (12-15)
  Emotional and identity (10-12)
  Product and device discussion (10-13)
  Sleep/routine disruption or category replacement (7-10)

### QUORA
Questions (15-20, full question form: What/How/Does/Why/Is), grouped: condition, treatment, skepticism, cost/access
Spaces (real ones, up to 8)

### NICHE FORUMS (exact URLs)
Health/condition or category forums (5-6) – name, URL, board, search terms
Country-specific (2-3)
Condition-specific (2-3)
Demographic-specific (1-2)
Forum queries (12-16)

### YOUTUBE
Queries (18): condition/treatment at home, honest device reviews, named channels (2-3), competitor reviews, "exercises not working", "best <type> <current year>", A vs B

### AMAZON / REVIEW PLATFORMS
Product searches (12; at least half "<brand> <product>" for named competitors; market domain + amazon.com)
Negative review filter phrases (8-14)
Review platforms with URLs

### COMPLAINT PLATFORMS (6-7 with URLs and search terms)

### FACEBOOK GROUPS – search terms (10)          [browser only]
### TIKTOK – queries (12, 2-4 words) + hashtags (10)   [browser only]
### INSTAGRAM – competitor handles (6) + hashtags (8)  [browser only]
### TWITTER/X – queries (10-14)                        [browser only]

### GOOGLE RESEARCH
Autocomplete seeds (8-12, "term ...")
People Also Ask seeds (8-10)

### ACADEMIC / AUTHORITY
Google Scholar queries (8)
Regulatory bodies (3-4, URL, what to verify)
Industry/authority publications (6-7, URL, what to look for)

### META AD LIBRARY                                    [browser only]
Keyword searches (12)
Advertiser names (10: the brand + 9 competitors)

### CLAIMS TO VERIFY
For each: CLAIM "<exact text>" / VERIFY: what evidence is missing

### RED FLAGS
For each: what it is, why it is a risk, which regulation or standard it may breach (TGA/ACCC, FDA/FTC, MHRA/ASA, etc. by market)
```

After writing the brief, show the user the summary block, segment slugs and the category adaptation, and ask for a go-ahead before Phase 1.
