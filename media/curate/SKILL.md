---
name: curate
description: Organizes ingested content into a searchable Obsidian content library with rich metadata tags. Use when the user says "save this to my library", "curate this", "add to my swipe file", "organize my content", "tag this post", or after running /ingest and wanting to store the results. Also use when the user asks to browse, search, or filter their content library.
  Do NOT use for initial content extraction (use /ingest for that) or for generating new content ideas (use /ideate for that).
---

# Content Curation & Library Organization

You organize ingested social media content into a searchable Obsidian content library. You classify content by archetype, hook type, format, and topic — then store it with rich YAML frontmatter so the user can browse, search, and draw inspiration from their collected swipe file.

This skill builds on `/ingest`. After content has been extracted and analyzed, `/curate` tags it, classifies it, and files it into a structured content library.

---

## Phase 0: Detect Input

Determine what the user is providing and what mode to operate in.

### Input Option A: Ingested Content (primary path)
Look for output from `/ingest` in the current working directory:
- Check for `ingest-output/` directory containing markdown analysis files
- Each file follows the pattern `{platform}-{descriptive-slug}.md` with structured sections: Summary, Key Findings, Notable Quotes, Context & Background, Raw Data
- Parse the file header for: **Source** (URL), **Platform**, **Author**, **Date**, **Extracted** timestamp

If `ingest-output/` exists and contains `.md` files, proceed to Phase 1 with these files.

### Input Option B: Raw URLs
If the user provides URLs directly (no `ingest-output/` present):
1. Inform the user: "I'll run /ingest first to extract the content, then curate it into your library."
2. Execute the `/ingest` skill on the provided URLs
3. Once ingest completes, proceed to Phase 1 with the generated files in `ingest-output/`

### Input Option C: Browse/Search Mode
If the user asks to browse, search, or filter their existing library:
- Look for `content-library/` in the current working directory
- If found, skip directly to Phase 5 (Search/Browse Mode)
- If not found, inform the user: "No content library found in the current directory. Curate some content first, or point me to your library path."

---

## Phase 1: Classify Content

For each piece of ingested content, read the full analysis file and determine the following classifications.

### Archetype (pick 1-2)

Assign based on the content's primary purpose and structure:

| Archetype | Description | Signals |
|---|---|---|
| **Educational** | Teaches something specific | How-to, tutorial, explainer, tips, lessons learned |
| **Entertaining** | Primarily for enjoyment | Humor, skits, memes, trending audio, comedy |
| **Inspirational** | Motivates or uplifts | Transformation story, milestone, motivational message |
| **Controversial/Hot Take** | Challenges conventional wisdom | "Unpopular opinion", contrarian take, debate-starter |
| **Authority/Proof** | Establishes credibility | Results, case studies, testimonials, credentials |
| **Behind-the-Scenes** | Shows the process | Day-in-the-life, workspace tour, making-of |
| **Community/Engagement** | Drives interaction | Polls, questions, challenges, duets, collabs |
| **Promotional** | Sells a product or service | Launch, offer, CTA-heavy, product demo |
| **Curated/Commentary** | Reacts to or curates others' content | Stitch, quote tweet, reaction, roundup |
| **Storytelling/Narrative** | Tells a story with arc | Personal story, case narrative, journey post |

### Hook Type (pick 1)

Identify the opening hook mechanism from the first line, first 3 seconds, or first slide:

| Hook Type | Pattern | Example |
|---|---|---|
| **Curiosity Gap** | Teases info without revealing it | "The one thing nobody tells you about..." |
| **Bold Claim** | Makes a strong, definitive statement | "Email marketing is dead." |
| **Pattern Interrupt** | Breaks expected behavior | Starting mid-action, unexpected visual |
| **Direct Question** | Asks the viewer something | "Have you ever wondered why...?" |
| **Shocking Statistic** | Leads with a surprising number | "87% of startups fail because of this one mistake" |
| **Before/After** | Shows transformation contrast | "6 months ago vs. now" |
| **Social Proof** | Leads with credibility/results | "How I got 100K followers in 90 days" |
| **Controversy** | Opens with a polarizing stance | "Stop doing [popular thing]" |
| **FOMO** | Creates urgency or scarcity | "This strategy won't work for long" |
| **Relatability** | Connects through shared experience | "POV: you just got your first client" |
| **Story Open** | Begins with a narrative hook | "Last Tuesday, I got an email that changed everything" |
| **Listicle Tease** | Promises a numbered set of items | "5 tools I use every day that nobody talks about" |

### Hook Rating (1-5)

Rate the hook's strength based on these criteria:
- **5** — Impossible to scroll past. Creates immediate tension, curiosity, or emotion. You must know what happens next.
- **4** — Very strong. Stops most people. Clear value proposition or emotional pull.
- **3** — Solid hook. Works for the target audience but wouldn't stop a casual scroller.
- **2** — Weak hook. Generic opening, buries the lead, or starts with throat-clearing.
- **1** — No real hook. Starts with "Hey guys" or dives in without any attention mechanism.

### Format

Identify the content format:
`short-form-video` | `carousel` | `static-image` | `long-form-video` | `text-post` | `thread` | `reel` | `story` | `live`

### Content Pillar

Infer the primary topic/pillar from the content. Common pillars include: marketing, sales, product, design, engineering, finance, health, fitness, mindset, leadership, creator-economy, AI, productivity, relationships — but infer from the actual content rather than forcing into a predefined list.

If the user has previously defined their own content pillars (check for a `content-library/_pillars.md` file), map to those pillars instead.

---

## Phase 2: Generate YAML Frontmatter

For each piece of content, construct comprehensive YAML frontmatter by combining:
- Classification from Phase 1
- Metadata extracted from the `/ingest` output (source URL, platform, creator, date, engagement metrics)
- Generated fields (slug, ingestion date, status)

### Frontmatter Schema

```yaml
---
title: "Descriptive title of the content"
source_url: "https://original-url.com/..."
platform: "tiktok | instagram | youtube | x | linkedin | threads"
creator: "@handle"
creator_followers: "approximate count if available"
date_published: YYYY-MM-DD
date_curated: YYYY-MM-DD
archetype:
  - educational
  - authority
content_pillar: "marketing"
format: "short-form-video"
hook_type: "curiosity-gap"
hook_text: "The exact first line / opening text / first 3 seconds"
hook_rating: 4
views: 0
likes: 0
comments: 0
shares: 0
saves: 0
engagement_rate: 0.00
tags:
  - topic1
  - topic2
  - topic3
status: "unreviewed"
starred: false
inspiration_notes: ""
---
```

Field notes:
- `date_curated`: Today's date (when the content is being curated, not when it was ingested)
- `engagement_rate`: Calculate as `(likes + comments + shares) / views` if views > 0, otherwise leave as 0.00
- `tags`: Generate 3-7 specific, lowercase tags based on the content topics — these are more granular than the content pillar
- `status`: Always starts as `"unreviewed"` — the user can later mark items as `"reviewed"`, `"starred"`, `"used"`, or `"archived"`
- `starred`: Default `false` — the user can star favorites for quick access
- `inspiration_notes`: Empty string — the user fills this in with their own notes on how to use this content for inspiration

---

## Phase 3: Store in Library

### Directory Structure

Create the content library directory structure if it does not already exist. Default location is `content-library/` in the current working directory.

```
content-library/
  _index.md          Dashboard with Dataview queries for browsing
  _pillars.md        User's content pillars (created on first run with defaults)
  swipes/            Individual curated content files
  hooks/             Extracted hooks reference file
```

Create directories with `mkdir -p`.

### Swipe Files

For each piece of curated content, write a markdown file to `content-library/swipes/`:

**Filename pattern:** `{platform}-{creator-handle}-{short-slug}.md`
- Strip `@` from creator handle
- Use lowercase, replace spaces with hyphens
- Keep the slug to 5-6 words max
- Example: `tiktok-alexhormozi-how-to-price-your-offer.md`

**File contents:**
1. The YAML frontmatter block from Phase 2
2. A horizontal rule `---`
3. The full analysis content from the `/ingest` output file (Summary, Key Findings, Notable Quotes, etc.)

### Hooks Reference

Append each hook to `content-library/hooks/hooks-reference.md` in this format:

```markdown
## {hook_type} — Rating: {hook_rating}/5

> "{hook_text}"

- **Creator:** {creator} ({platform})
- **Archetype:** {archetype}
- **Source:** [{title}]({source_url})
- **Curated:** {date_curated}

---
```

If the file already exists, append new hooks. If it does not exist, create it with a header:

```markdown
# Hooks Reference Library

A collection of hooks extracted from curated content, organized for quick reference and inspiration.

---

```

### Pillars File

On first run (when `_pillars.md` does not exist), create it with a default set:

```markdown
# Content Pillars

Define your core content pillars below. The /curate skill will map ingested content to these pillars.

Edit this file to customize your pillars.

## Active Pillars

- marketing
- sales
- product
- leadership
- personal-brand
- industry-trends

## Retired Pillars

(Move pillars here that you no longer focus on)
```

---

## Phase 4: Update Index

Create or update `content-library/_index.md` as a dashboard for browsing the library using Obsidian Dataview queries.

If the file does not exist, create it. If it does exist, overwrite it (the queries are regenerated each time to stay current).

### Index Content

```markdown
# Content Library Dashboard

> Your curated swipe file. Browse by archetype, platform, hook quality, or topic.
>
> **Total items:** Check the swipes/ folder for count.
> **Last updated:** {date_curated}

---

## Top Hooks (Rating >= 4)

```dataview
TABLE hook_text AS "Hook", hook_type AS "Type", hook_rating AS "Rating", creator AS "Creator", platform AS "Platform"
FROM "content-library/swipes"
WHERE hook_rating >= 4
SORT hook_rating DESC
LIMIT 20
```

## Recently Added

```dataview
TABLE title AS "Title", platform AS "Platform", creator AS "Creator", archetype AS "Archetype"
FROM "content-library/swipes"
SORT date_curated DESC
LIMIT 15
```

## By Archetype

### Educational
```dataview
TABLE title AS "Title", creator AS "Creator", hook_rating AS "Hook", platform AS "Platform"
FROM "content-library/swipes"
WHERE contains(archetype, "educational")
SORT hook_rating DESC
```

### Storytelling/Narrative
```dataview
TABLE title AS "Title", creator AS "Creator", hook_rating AS "Hook", platform AS "Platform"
FROM "content-library/swipes"
WHERE contains(archetype, "storytelling")
SORT hook_rating DESC
```

### Authority/Proof
```dataview
TABLE title AS "Title", creator AS "Creator", hook_rating AS "Hook", platform AS "Platform"
FROM "content-library/swipes"
WHERE contains(archetype, "authority")
SORT hook_rating DESC
```

### Controversial/Hot Take
```dataview
TABLE title AS "Title", creator AS "Creator", hook_rating AS "Hook", platform AS "Platform"
FROM "content-library/swipes"
WHERE contains(archetype, "controversial")
SORT hook_rating DESC
```

### Entertaining
```dataview
TABLE title AS "Title", creator AS "Creator", hook_rating AS "Hook", platform AS "Platform"
FROM "content-library/swipes"
WHERE contains(archetype, "entertaining")
SORT hook_rating DESC
```

### Inspirational
```dataview
TABLE title AS "Title", creator AS "Creator", hook_rating AS "Hook", platform AS "Platform"
FROM "content-library/swipes"
WHERE contains(archetype, "inspirational")
SORT hook_rating DESC
```

## By Platform

### TikTok
```dataview
TABLE title AS "Title", creator AS "Creator", archetype AS "Type", hook_rating AS "Hook"
FROM "content-library/swipes"
WHERE platform = "tiktok"
SORT date_curated DESC
```

### Instagram
```dataview
TABLE title AS "Title", creator AS "Creator", archetype AS "Type", hook_rating AS "Hook"
FROM "content-library/swipes"
WHERE platform = "instagram"
SORT date_curated DESC
```

### YouTube
```dataview
TABLE title AS "Title", creator AS "Creator", archetype AS "Type", hook_rating AS "Hook"
FROM "content-library/swipes"
WHERE platform = "youtube"
SORT date_curated DESC
```

### X / Twitter
```dataview
TABLE title AS "Title", creator AS "Creator", archetype AS "Type", hook_rating AS "Hook"
FROM "content-library/swipes"
WHERE platform = "x"
SORT date_curated DESC
```

### LinkedIn
```dataview
TABLE title AS "Title", creator AS "Creator", archetype AS "Type", hook_rating AS "Hook"
FROM "content-library/swipes"
WHERE platform = "linkedin"
SORT date_curated DESC
```

## Starred Items

```dataview
TABLE title AS "Title", creator AS "Creator", platform AS "Platform", archetype AS "Archetype", inspiration_notes AS "Notes"
FROM "content-library/swipes"
WHERE starred = true
SORT date_curated DESC
```

## By Content Pillar

```dataview
TABLE title AS "Title", creator AS "Creator", platform AS "Platform", hook_rating AS "Hook"
FROM "content-library/swipes"
SORT content_pillar ASC, hook_rating DESC
```
```

---

## Phase 5: Search/Browse Mode

When the user asks to search, browse, or filter their content library, operate in read-only search mode.

### Supported Queries

Parse the user's natural language request and translate it into filters:

| User says | Filter logic |
|---|---|
| "show me all educational content" | `archetype` contains "educational" |
| "best hooks" or "top hooks" | `hook_rating` >= 4, sorted by rating DESC |
| "TikTok content" | `platform` = "tiktok" |
| "content from @hormozi" | `creator` contains "hormozi" |
| "marketing posts" | `content_pillar` = "marketing" |
| "hooks with rating 5" | `hook_rating` = 5 |
| "carousel content" | `format` = "carousel" |
| "starred items" | `starred` = true |
| "show me everything" | No filter, list all |
| "content tagged with AI" | `tags` contains "ai" |

### Search Execution

1. Read all `.md` files in `content-library/swipes/`
2. Parse the YAML frontmatter from each file
3. Apply the user's filters to the parsed frontmatter fields
4. Sort results (default: by `date_curated` DESC, or by `hook_rating` DESC if searching for hooks)

### Search Output

Present results as a summary table:

```
| # | Title | Creator | Platform | Archetype | Hook Rating | Pillar |
|---|-------|---------|----------|-----------|-------------|--------|
| 1 | ...   | ...     | ...      | ...       | .../5       | ...    |
```

After the table, offer:
- "Want me to show the full analysis for any of these?"
- "Want to star any of these items?"
- "Want to filter further?"

If no results match the query, suggest alternative filters or broader searches.

---

## Phase 6: Respond to the User

After curating content, respond with:

1. **Summary of what was curated** — how many pieces, from which platforms
2. **Classification overview** — a quick table showing each piece with its archetype, hook type, hook rating, and content pillar
3. **Standout hooks** — highlight any hooks rated 4 or 5 with the actual hook text
4. **Files created** — list all files written to `content-library/`
5. **Next steps** — suggest the user:
   - Review items and update `status` from "unreviewed" to "reviewed"
   - Star favorites by setting `starred: true`
   - Add personal `inspiration_notes` for items they want to riff on
   - Run `/ideate` to generate new content ideas based on their library

---

## Error Handling

- **No ingest output found and no URLs provided**: Ask the user to either provide URLs or run `/ingest` first
- **Ingest output file is malformed or missing expected sections**: Extract what you can, note missing fields in the frontmatter as empty strings, and flag it in the response
- **Content library already has a file with the same name**: Append a numeric suffix (e.g., `-2`, `-3`) to avoid overwriting
- **Engagement metrics unavailable**: Set to 0 and note "metrics unavailable" in a comment within the frontmatter
- **Cannot determine hook or archetype**: Default to the closest match and set `hook_rating` to 3 with a note that manual review is recommended

Never fail silently. Always tell the user what was curated successfully and what needs attention.
