---
name: brand-voice
description: Analyzes your existing content (social media posts, articles, videos) to extract your unique writing style into a reusable Brand Voice Profile. The profile captures your tone, vocabulary, sentence patterns, rhetorical devices, and platform-specific adaptations. Other content creation skills reference this profile to generate content that sounds authentically like you.
  Use when the user says "analyze my voice", "extract my writing style", "create a brand voice profile", "how do I write?", "make content sound like me", or provides their social media handles/content for style analysis.
  Do NOT use for analyzing someone else's content style (use /teardown for that) or for generating new content (use /ideate or /script with the voice profile).
---

# Brand Voice Profile Extraction

You analyze the user's existing content to extract their unique writing style, tone, and voice patterns into a reusable Brand Voice Profile. Other skills (/ideate, /script, /thread-writer) reference this profile to generate content that sounds like the user.

The user provides their own content samples — URLs, text files, or previously ingested content. You analyze everything across multiple dimensions and produce a structured, portable Voice DNA Profile document.

---

## Phase 0: Gather Samples

Collect the user's content for analysis. Accept any of these input methods:

1. **URLs to the user's own content** — social media profiles, blog posts, YouTube videos, newsletters, etc.
2. **Text files or markdown** — pasted directly or provided as file paths
3. **A folder of previously ingested content** — output from the /ingest skill

### If URLs are provided:
Use the /ingest skill internally to extract the content. For each URL, run ingest and collect the extracted text into working files.

### Sample requirements:
- **Minimum:** 3 samples totaling 300+ words. Fewer samples means a less reliable profile — warn the user.
- **Recommended:** 5-10 samples for reliable extraction across all dimensions.
- **Best practice:** Ask the user to provide their BEST-PERFORMING content. Top-performing posts represent their most effective voice — the voice that resonates with their audience.

### If the user provides fewer than 3 samples:
Proceed but add a disclaimer to the profile: "Based on limited samples — accuracy improves with more content."

### If the user provides a social media handle without specific posts:
Ask them to share 5-10 specific posts they're most proud of, or that performed best. A handle alone is not enough — you need the actual content text.

Save all collected samples to `brand-voice/samples/` as individual markdown files for reference.

---

## Phase 1: Multi-Dimensional Voice Analysis

Analyze all samples across these dimensions. This framework is based on NN/G's 4 core tone dimensions extended with additional taxonomies for comprehensive voice extraction.

### Core 4 Dimensions (rate on 1-10 spectrum)

| Dimension | Scale | What it measures |
|---|---|---|
| **Formality** | 1 (very casual) to 10 (very formal) | Slang vs. proper language, contractions vs. full forms, sentence completeness |
| **Humor** | 1 (completely serious) to 10 (constant humor) | Jokes, wit, irony, playfulness, self-deprecation |
| **Respect** | 1 (very irreverent) to 10 (very respectful/diplomatic) | How they treat opposing views, authority, conventions |
| **Energy** | 1 (reserved/matter-of-fact) to 10 (highly enthusiastic) | Exclamation marks, intensity words, emotional expressiveness |

For each dimension, provide both the numeric score AND a brief description of how it manifests in their writing.

### Extended Dimensions

5. **Vocabulary Level:** Simple/accessible vs. technical/jargon-heavy. Note the specific domain jargon they use and how they introduce technical concepts.

6. **Sentence Structure:** Short/punchy vs. long/flowing. Measure the active vs. passive voice ratio. Note any distinctive structural patterns (fragments, run-ons, compound sentences).

7. **Rhetorical Devices:** Identify which devices they rely on most — metaphors, analogies, numbered lists, rhetorical questions, repetition, callbacks, rule-of-three, contrast/juxtaposition, anaphora.

8. **Perspective:** Which grammatical person dominates — first person ("I"), second person ("you"), first plural ("we"), or third person. Note any patterns in when they shift perspective.

9. **Pacing:** Paragraph length patterns, use of line breaks for emphasis, one-liner frequency, use of whitespace as a rhetorical tool.

10. **Emotional Register:** The dominant emotional mode — empathetic, authoritative, vulnerable, aspirational, confrontational, nurturing, provocative. Most writers have a primary and secondary register.

11. **Cultural References:** Pop culture, academic citations, industry-specific references, memes, historical references, or none. This shapes how relatable vs. intellectual the content feels.

12. **Signature Patterns:** Recurring phrases, distinctive opening patterns, closing patterns, emoji usage, capitalization habits, unique expressions that are unmistakably theirs.

---

## Phase 2: Pattern Extraction

From the samples, extract specific, concrete, measurable patterns. Do not generalize — cite actual examples from the content.

### Quantitative Patterns
- **Sentence length distribution:** Calculate average, minimum, maximum, and approximate standard deviation across all samples.
- **Paragraph length:** Average sentences per paragraph, frequency of single-line paragraphs.
- **Punctuation frequency:** Exclamation marks per 100 words, question marks per 100 words, em dash frequency, ellipsis frequency.

### Structural Patterns
- **Opening patterns:** How do they start posts? Categorize: question, bold statement, story/anecdote, statistic, provocation, "I" statement. Provide 3+ examples from samples.
- **Closing patterns:** How do they end? CTA style, question to audience, summary statement, sign-off phrase, cliffhanger. Provide 3+ examples.
- **Paragraph structure:** Short single-line punches? Flowing multi-sentence paragraphs? Mixed with a rhythm? Describe the pattern with examples.

### Vocabulary Patterns
- **Most-used words/phrases:** Beyond common words (the, is, and), what words appear disproportionately? List the top 10-15.
- **Power words:** Words they use for emphasis or impact.
- **Words they avoid:** Equally important — note any conspicuous absences. Formal writers avoid slang; casual writers avoid jargon.
- **Jargon and terminology:** Industry-specific language, abbreviations, acronyms they assume the audience knows.

### Style Markers
- **Emoji usage:** None, occasional, frequent, or specific favorites. List any signature emojis.
- **Hashtag style:** None, minimal (1-2), strategy-heavy (5+), or specific recurring hashtags.
- **Formatting habits:** Bold text, italics, ALL CAPS for emphasis, bullet points, numbered lists.
- **Punctuation style:** Oxford comma? Serial exclamation marks? Ellipses for trailing thoughts? Em dashes for asides?

---

## Phase 3: Generate Voice DNA Profile

Create a structured, portable Voice DNA Profile document using the template below. Every field must be filled with specific observations from the samples — no generic placeholders.

```markdown
# Brand Voice Profile — {Name}

**Generated:** {date}
**Based on:** {N} content samples from {platforms}
**Last updated:** {date}

---

## Voice Identity (3-5 word summary)
{e.g., "Bold, Direct, Data-Driven Educator"}

## Brand Personality
- {Adjective 1}: {how it manifests in writing}
- {Adjective 2}: {how it manifests}
- {Adjective 3}: {how it manifests}

## Tone Dimensions
| Dimension | Score (1-10) | Description |
|---|---|---|
| Formality | X | {description} |
| Humor | X | {description} |
| Respect | X | {description} |
| Energy | X | {description} |

## Writing Patterns
- **Sentence style:** {description with examples}
- **Paragraph structure:** {description}
- **Opening moves:** {typical patterns with examples from samples}
- **Closing moves:** {typical patterns}
- **Signature phrases:** {list of recurring expressions}

## Vocabulary Guide
- **Power words:** {frequently used impactful words}
- **Avoid:** {words this person never uses}
- **Jargon level:** {description}
- **Reading level:** {approximate grade level}

## "This, Not That" Examples
| This (on-brand) | Not That (off-brand) |
|---|---|
| "{example from their content}" | "{same idea, wrong voice}" |
| "{example}" | "{wrong voice version}" |
| "{example}" | "{wrong voice version}" |

## Platform Adaptations
- **{Platform 1}:** {how voice shifts on this platform}
- **{Platform 2}:** {how voice shifts}

## How to Use This Profile
When generating content for {Name}, reference this profile to:
1. Match the tone dimensions (especially formality and energy levels)
2. Use their sentence structure patterns (short/punchy vs. flowing)
3. Open and close content using their established patterns
4. Include their signature phrases naturally
5. Match their vocabulary level and avoid words they don't use
```

The "This, Not That" table is critical. It gives concrete, side-by-side examples of on-brand vs. off-brand writing. Pull the "This" column directly from their content. Write the "Not That" column as the same idea expressed in a voice that is clearly NOT theirs — too formal, too casual, too generic, or wrong tone. Aim for at least 3 rows, ideally 5.

---

## Phase 4: Write Output

Save the completed Voice DNA Profile to `brand-voice/{name}-voice-profile.md` in the current working directory, where `{name}` is the user's name or handle in lowercase kebab-case.

### If a profile already exists:
- Inform the user that a previous profile was found.
- Offer two options: (a) update the existing profile by merging new sample analysis with existing patterns, or (b) replace it entirely with a fresh analysis.
- If updating, note the new sample count and update the "Last updated" date. Preserve patterns from the old profile that are still supported by the new samples, and flag any patterns that have shifted.

### File structure:
```
brand-voice/
  {name}-voice-profile.md    <- The main profile document
  samples/                    <- Folder with the raw content samples used
    sample-01.md
    sample-02.md
    ...
```

---

## Phase 5: Validation

After generating the profile, validate it by putting it to use:

1. **Generate 2-3 short sample paragraphs** (50-100 words each) written in the user's extracted voice. Each paragraph should be on a different topic — one could be an opinion, one a how-to tip, one a story opener.

2. **Present the samples to the user** and ask:
   - "Does this sound like you? Rate each sample 1-5 for voice accuracy."
   - "What feels off? What would you change?"
   - "Is there anything about your voice that's missing from the profile?"

3. **Refine based on feedback.** If the user identifies issues:
   - Adjust the relevant dimensions or patterns in the profile
   - Regenerate the sample paragraphs to confirm the fix
   - Update the saved profile document

4. **Mark the profile as validated** once the user confirms it sounds right. Add a line to the profile:
   ```
   **Status:** Validated by {Name} on {date}
   ```

The validation step is essential — voice extraction is inherently subjective, and the user is the only authority on whether the profile captures their voice accurately.

---

## Error Handling

- **Too few samples:** Proceed with a disclaimer but recommend the user add more content later. A 1-2 sample profile is a rough sketch, not a reliable guide.
- **Samples are too short:** If total word count is under 300, warn that the profile will be shallow. Recommend longer-form content if available.
- **Mixed voices:** If the samples seem to come from different authors or ghostwriters, flag this. Ask the user which samples best represent THEIR voice.
- **Platform-only content:** If all samples are from one platform (e.g., only tweets), note that the profile may not generalize well to long-form content. Recommend adding samples from other formats.
- **Ingestion failures:** If /ingest fails on a URL, report the failure, skip that sample, and continue with the remaining content. Note the reduced sample size in the profile.

---

## Tips for Better Profiles

- The best profiles come from diverse content: mix of platforms, topics, and formats. A profile built from 10 tweets and 0 articles will miss how the user writes long-form.
- Top-performing content matters more than average content. The user's viral posts reveal their most resonant voice.
- Voice is not static. If the user's style has evolved, use recent content (last 6-12 months) for the most accurate profile.
- The "This, Not That" table is the single most useful artifact for other skills. Make it specific and contrasting.
- When in doubt, ask the user. Voice is personal — they know their voice better than any analysis can capture.
