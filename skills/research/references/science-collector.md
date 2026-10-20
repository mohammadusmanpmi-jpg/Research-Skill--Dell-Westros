# Science and authority collector → `01-science.md`

This extends the Authority collector in `phase1-collectors.md`. It builds the evidence ceiling every claim must stay under, and supplies Appendix C (claim guardrails) and Appendix D (scientific footing) of the DRIVE Strategy.

**Floor:** about 50 sources (minimum 40). Count only peer-reviewed studies, systematic reviews, clinical guidelines, regulator pages and drug-interaction references, each with a DOI or a stable URL. Fewer than 40 → log a shortfall (every query and database tried) and tell the user.

## 1. The problem science
For the problem the product addresses:
- **What causes it.** The physiological mechanism in plain words, with citations. This is the raw material for the **problem mechanism**.
- **When it starts and who gets it.** Prevalence by age and sex, onset age, and measured decline curves (e.g. "artery widening holds until ~40, then drops ~0.21%/year in men; Celermajer, JACC 1994").
- **Why common explanations are wrong or incomplete.** Studies that rule out the usual suspects (age, hormones, stress), e.g. "true age-related low T in ~2% of men 40-79; Wu, NEJM 2010".
- **Warning-sign and guideline facts.** Specialist-society guidelines (AUA, NICE, ESC and so on) and large cohort or consensus findings that can be shown on screen with a source.

Prefer, in order: clinical guidelines and consensus statements > systematic reviews and meta-analyses > RCTs > large cohorts > small or observational studies > lab and animal studies. **Label lab and animal evidence clearly.** It never supports a human-outcome claim.

## 2. Ingredient evidence ceiling (per ingredient, at the product's actual dose)
For every ingredient on the label (amounts come from `00-offer-audit.md`; if they are missing, say so and treat the dose as unknown):

| Ingredient | Amount per serving | Studied dose in the best human evidence | Ratio (ours ÷ studied) | Best evidence (type, n, finding, citation) | What we can say | What we can't say |
|---|---|---|---|---|---|---|

Rules:
- The ceiling is set by the **best human evidence at a comparable dose**. If our dose is far below the studied dose (e.g. 1/20 to 1/90 of it), the line becomes "part of the blend", never the hero.
- **"Studied for" is not "proven to".** Never quote a study result as a product result.
- If a meta-analysis or Cochrane review finds no effect, say so, and drop any matching claim ("a meta-analysis found nitrate did not change brain blood flow" → no brain-blood-flow mechanism).
- Note when the category leader is attacking one of our ingredients (from the competitor ads). It's a reason not to make that ingredient the hero.

## 3. Drug interactions and safety
For every ingredient, check:
- NIH Office of Dietary Supplements fact sheets (ods.od.nih.gov)
- MedlinePlus herbs and supplements (medlineplus.gov/druginfo/herb_All.html)
- the Drugs.com interaction checker (drugs.com/drug_interactions.html)
- LiverTox (ncbi.nlm.nih.gov/books/NBK547852)
- NCCIH (nccih.nih.gov)
- the market's own regulator (TGA, MHRA, FDA and so on)

Record each interaction (ingredient × drug class, severity as rated by the source, mechanism, citation). Typical classes to check: ED drugs and nitrates, blood pressure and heart drugs, blood thinners (warfarin), diabetes drugs, statins, SSRIs, and pregnancy.

**Output:**
- An interactions table.
- **Which ICPs this touches.** For example, men on ED pills or blood pressure meds: never position the product as a replacement, and put "talk to your doctor before you combine them" inside the story.
- **The doctor line** to use wherever medication is part of the story.

## 4. Claim guardrails (three columns)
Built from §§ 1-3, the regulator's rules for the market, and the client's removed-ad reasons (`00-account.md`):

| USE FREELY (brand voice) | ONLY INSIDE A REAL CUSTOMER'S STORY | NEVER |
|---|---|---|

Then add **copy traps**: the specific phrasings that pull in the wrong buyer, read as disease claims or repeat removed-ad wording. Examples: a "spikes" hook, day-by-day timelines in brand voice, doctor personas, borrowed creative, inconsistent dose wording, an under-dosed ingredient made the hero.

## 5. What we don't claim, and why
A list of the claims currently on the site or in the ads (or common in the category) that the evidence does not support, each with a one-line reason and a citation. For example: "Plaque reduction: mouse studies only." / "98% absorption: no data; the best comparison found sublingual equal to capsules."

## Record format
Each source is one line in `01-authority.md` (title, first author, year, journal, n, design, one-line finding, SUPPORTS / CONTRADICTS / INCONCLUSIVE, DOI or URL). `01-science.md` holds §§ 1-5. `depth_check.py` does not count these; record the source count at the top of `01-science.md`.
