---
name: fact-check
description: Evaluates the accuracy and truthfulness of claims in any content — social media posts, articles, videos, or transcripts. Extracts individual claims, classifies them, researches each one, and produces a multi-dimensional truth assessment covering accuracy, context, source reliability, and bias. Uses a 5-dimension evaluation model inspired by PolitiFact, CRAAP test, and Ad Fontes Media.
  Use when the user says "is this true?", "fact check this", "verify these claims", "how accurate is this?", "check the facts in this post", or shares content and asks about its truthfulness. Also use after /ingest when the user wants to evaluate accuracy.
  Do NOT use for opinion pieces where the user wants agreement/disagreement rather than fact-checking, or for generating new content.
---

# Fact Check

You evaluate the accuracy and truthfulness of claims in any content. You extract individual claims, classify them, research each one against authoritative sources, and produce a multi-dimensional truth assessment.

The user provides a URL, text, or output from a previous /ingest run. You break the content into discrete claims, verify each one, and deliver a structured fact-check report.

---

## Phase 0: Extract Content

Determine the input type and obtain the content to fact-check:

1. **URL provided** — Run the /ingest skill internally to extract the content. Use the raw extraction output as the basis for claim extraction.
2. **Text or markdown provided directly** — Use the provided text as-is.
3. **Previous /ingest output** — If the user references a prior ingestion (e.g., "fact check what we just ingested"), read the relevant file from `ingest-output/` and use that as the source material.

Store the source content for reference. Note the original source URL, author, and publication date if available.

---

## Phase 1: Claim Extraction

Break the content into individual, discrete claims. For each claim, classify its type:

| Type | Description | Example | Proceed to Verification? |
|---|---|---|---|
| **VERIFIABLE_FACT** | Empirically testable | "The Pentagon budget is $1 trillion" | Yes |
| **STATISTICAL_CLAIM** | Data-dependent, methodology matters | "Crime is up 20%" | Yes |
| **EXPERT_CONSENSUS** | Scientific/expert agreement exists | "Vaccines don't cause autism" | Yes |
| **CONTESTED_CLAIM** | Genuine expert disagreement | "Optimal tax rate is X%" | Yes |
| **OPINION** | Value judgment, not empirically testable | "This policy is unfair" | No — note underlying facts |
| **PREDICTION** | Future-oriented | "Inflation will reach 5%" | No — note underlying facts |
| **SATIRE** | Intentionally non-literal | Obvious parody or satire | No — flag as satire |
| **HYPERBOLE** | Exaggerated for rhetorical effect | "Everyone knows this" | No — flag as hyperbole |

Only VERIFIABLE_FACT, STATISTICAL_CLAIM, EXPERT_CONSENSUS, and CONTESTED_CLAIM proceed to Phase 2 verification. For OPINION and PREDICTION claims, identify and note the underlying factual assumptions they rely on. For SATIRE and HYPERBOLE, flag them and move on.

Output a numbered list of all extracted claims with their classifications before proceeding.

---

## Phase 2: Research & Verify Each Claim

For each checkable claim (VERIFIABLE_FACT, STATISTICAL_CLAIM, EXPERT_CONSENSUS, CONTESTED_CLAIM):

### Step 1: Search for Evidence
Use WebSearch to find 3-5 authoritative sources for each claim. Prioritize:
- Government data and official statistics
- Peer-reviewed academic studies
- Reputable journalism (AP, Reuters, established outlets)
- Domain-specific authoritative bodies (WHO for health, IPCC for climate, etc.)

### Step 2: Apply the SIFT Method
For each claim, follow the SIFT evaluation process:
1. **Stop** — Don't react to the claim emotionally. Assess it neutrally.
2. **Investigate the source** — Who made this claim? What is their expertise, track record, and potential motivation?
3. **Find better coverage** — Look beyond the original source. What do other authoritative sources say?
4. **Trace to origin** — Where did the claim originate? Has it been distorted through re-sharing or paraphrasing?

### Step 3: Cross-Reference
Compare findings across multiple sources. Note:
- Where sources agree
- Where sources disagree
- The strongest evidence FOR the claim
- The strongest evidence AGAINST the claim

### Step 4: Handle Statistical Claims with Extra Scrutiny
For STATISTICAL_CLAIM types, additionally evaluate:
- What time period is being referenced?
- What baseline is being compared against?
- Is the methodology sound?
- Are the numbers absolute or relative (and does that matter)?
- Is the sample size adequate?

---

## Phase 3: Rate Each Claim (5-Dimension Assessment)

Apply all five dimensions to each verified claim.

### Dimension 1: Accuracy Rating

| Rating | Definition |
|---|---|
| **TRUE** | Accurate, nothing significant missing |
| **MOSTLY_TRUE** | Accurate but needs clarification or minor caveats |
| **MIXED** | Partially accurate, important context missing |
| **MOSTLY_FALSE** | Contains an element of truth but is overall misleading |
| **FALSE** | Not accurate |
| **FABRICATED** | Entirely made up with no basis in fact |
| **UNVERIFIABLE** | Cannot verify with available evidence |
| **OUTDATED** | Was true at one point but is no longer accurate |

### Dimension 2: Context & Completeness

| Rating | Definition |
|---|---|
| **FULL_CONTEXT** | Presents relevant context fairly and completely |
| **MISSING_CONTEXT** | True on its face but omits important qualifying information |
| **CHERRY_PICKED** | Selectively uses data points to support a narrative while ignoring contradictory data |
| **DECONTEXTUALIZED** | Removed from its original meaning or setting |
| **MISATTRIBUTED** | Attributed to the wrong source, time, or event |
| **MANIPULATED** | Altered from its original form (edited quotes, doctored data, etc.) |

### Dimension 3: Source Reliability

Score each sub-dimension from 1 (lowest) to 5 (highest):

| Sub-dimension | What to Evaluate |
|---|---|
| **Authority/Expertise** | Does the claimant have relevant credentials or domain expertise? |
| **Evidence Quality** | Is the evidence cited primary, peer-reviewed, or anecdotal? |
| **Transparency** | Is the methodology or reasoning behind the claim visible? |
| **Track Record** | Has this source been accurate or inaccurate in the past? |
| **Independence** | Is the source independent from the subject of the claim, or do they have a vested interest? |

Composite source reliability score = average of all five sub-scores.

### Dimension 4: Bias Indicators

**Direction:**
- LEFT | LEAN_LEFT | CENTER | LEAN_RIGHT | RIGHT | NON_POLITICAL

**Type:**
- NONE — No detectable bias
- FRAMING — Presents facts through a particular interpretive lens
- OMISSION — Leaves out relevant information that would change the picture
- SELECTION — Chooses which facts to highlight based on a narrative
- LANGUAGE — Uses loaded, emotional, or persuasive language

**Severity:**
- MINIMAL — Bias present but does not meaningfully affect accuracy
- MODERATE — Bias noticeably shapes the presentation
- SIGNIFICANT — Bias materially distorts the message
- EXTREME — Content is primarily advocacy disguised as reporting

### Dimension 5: Confidence Level

| Level | Definition |
|---|---|
| **HIGH** | Multiple reliable, independent sources agree; strong evidence base |
| **MEDIUM** | Some reliable sources available; reasonable but not conclusive evidence |
| **LOW** | Limited sources; weak, indirect, or contradictory evidence |
| **INSUFFICIENT** | Cannot make a meaningful determination with available evidence |

---

## Phase 4: Synthesize Overall Assessment

After rating all individual claims, produce an overall content assessment:

1. **Overall accuracy score** — Calculate the percentage of verifiable claims rated TRUE or MOSTLY_TRUE.
2. **Most significant inaccuracies** — Identify the claims that are most consequentially wrong or misleading.
3. **Strongest areas** — Note where the content is most accurate and well-supported.
4. **Weakest areas** — Note where the content falls short.
5. **"Misleading but technically true" patterns** — Call these out explicitly. Content that is technically accurate but framed to create a false impression is one of the most common and damaging forms of misinformation.
6. **Acknowledge uncertainty** — Use language like "the evidence suggests" rather than "this is definitively." Fact-checking is not omniscient.

---

## Phase 5: Write Output

Create a `fact-check-output/` subdirectory in the current working directory. Save the report as `fact-check-output/{source-slug}-fact-check.md` using this structure:

```markdown
# Fact Check: {Content Title}

**Source:** {URL or "Direct text input"}
**Author:** {name, if known}
**Date checked:** {today's date}
**Overall accuracy:** {X}% of verifiable claims rated True or Mostly True
**Confidence:** {HIGH/MEDIUM/LOW}

---

## Executive Summary

{2-3 sentences summarizing the overall accuracy of the content, the most important findings, and the confidence level of the assessment.}

## Claim-by-Claim Analysis

### Claim 1: "{exact quote or close paraphrase}"

- **Type:** VERIFIABLE_FACT
- **Accuracy:** MOSTLY_TRUE
- **Context:** MISSING_CONTEXT
- **Source Reliability:** {composite score}/5
- **Bias:** {direction} | {type} | {severity}
- **Confidence:** HIGH
- **Evidence:** {What authoritative sources say, with URLs where available}
- **Verdict:** {Plain English explanation of the finding — what's right, what's wrong, what's missing}

### Claim 2: "{exact quote or close paraphrase}"

- **Type:** STATISTICAL_CLAIM
- **Accuracy:** MIXED
- **Context:** CHERRY_PICKED
- **Source Reliability:** {composite score}/5
- **Bias:** {direction} | {type} | {severity}
- **Confidence:** MEDIUM
- **Evidence:** {What authoritative sources say, with URLs where available}
- **Verdict:** {Plain English explanation}

{Continue for all claims...}

### Non-Verified Claims

{List any OPINION, PREDICTION, SATIRE, or HYPERBOLE claims identified, with a brief note on the underlying factual assumptions where relevant.}

## Bias Assessment

{Overall bias analysis of the content as a whole. Direction, type, severity, and how it affects the presentation of facts.}

## What's True

- {Bullet list of claims rated TRUE or MOSTLY_TRUE, with brief supporting evidence}

## What's Misleading

- {Bullet list of claims rated MIXED or with MISSING_CONTEXT/CHERRY_PICKED/DECONTEXTUALIZED context ratings, with explanations of WHY they are misleading}

## What's False

- {Bullet list of claims rated MOSTLY_FALSE, FALSE, or FABRICATED, with corrections and sources}

## Sources Consulted

1. {Source name} — {URL}
2. {Source name} — {URL}
3. {Source name} — {URL}
{Continue for all sources used...}

---

*Evaluated by the /fact-check skill using the 5-dimension truth assessment framework*
```

---

## Phase 6: Respond to User

After writing the output file, present a concise summary to the user:

1. **Accuracy table** — A compact table showing each claim, its type, accuracy rating, and confidence level.
2. **Key findings** — Highlight the 2-3 most important findings (the biggest inaccuracies, the most misleading framing, or the strongest confirmations).
3. **Confidence statement** — Note the overall confidence level and any limitations encountered during verification.
4. **Output file location** — Point the user to the detailed report in `fact-check-output/`.

Keep the response focused. The detailed analysis lives in the markdown file. The response should be the executive summary that tells the user what they need to know at a glance.

Example response format:

```
## Fact Check Results: {Content Title}

**Overall accuracy: {X}% of verifiable claims rated True or Mostly True**

| # | Claim | Type | Accuracy | Confidence |
|---|---|---|---|---|
| 1 | "{short claim}" | VERIFIABLE_FACT | TRUE | HIGH |
| 2 | "{short claim}" | STATISTICAL_CLAIM | MIXED | MEDIUM |
| 3 | "{short claim}" | EXPERT_CONSENSUS | MOSTLY_TRUE | HIGH |

**Key findings:**
- {Most important finding}
- {Second most important finding}
- {Third most important finding}

**Confidence:** {LEVEL} — {brief explanation of limitations}

Full report saved to `fact-check-output/{slug}-fact-check.md`
```

---

## Error Handling

- **Insufficient sources found**: If WebSearch returns fewer than 2 sources for a claim, rate confidence as LOW or INSUFFICIENT and note the limitation explicitly.
- **Contradictory sources**: When authoritative sources disagree, present both sides and rate the claim as MIXED or CONTESTED_CLAIM. Do not pick a side without strong evidence.
- **Content too vague**: If the content makes claims too vague to verify ("things are bad"), note them as UNVERIFIABLE and explain why.
- **Satire misidentification**: If content appears to be satire but is being shared as fact, flag this pattern explicitly in the bias assessment.
- **Outdated information**: If a claim was once true but is no longer, rate as OUTDATED and provide the current accurate information.

Never present a fact-check as more certain than the evidence warrants. Overconfidence in fact-checking is itself a form of misinformation.
