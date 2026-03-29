---
name: ingest
description: Ingests and analyzes content from any URL — YouTube videos, X/Twitter posts, Instagram, TikTok, LinkedIn, or any public website. Extracts transcripts, transcribes audio, scrapes content, conducts analysis, and produces structured markdown findings with key takeaways.
  Use this skill whenever the user shares a URL and wants to understand, summarize, or analyze the content. Also use when the user says "ingest this", "analyze this link", "what's this about", "summarize this video/post/article", "break down this content", "pull the key points from this", or shares any social media or website link with a request for analysis.
  Do NOT use for: generating new content from scratch (no URL provided), live data dashboards, or real-time monitoring.
---

# Media Ingestion & Analysis

You ingest content from URLs — videos, social media posts, articles, podcasts — and produce structured analysis with key findings and takeaways.

The user provides one or more URLs (and optionally specific instructions about what to focus on). You extract everything useful, analyze it, and deliver clear findings.

---

## Phase 0: Parse URLs & Detect Media Type

For each URL provided, identify the platform and content type:

| Platform | Detection | Content Type |
|---|---|---|
| **YouTube** | `youtube.com/watch`, `youtu.be/` | Video (transcript + audio) |
| **X / Twitter** | `x.com/`, `twitter.com/` | Post (text + media + replies) |
| **Instagram** | `instagram.com/p/`, `/reel/` | Post or Reel (text + media) |
| **TikTok** | `tiktok.com/` | Video (text + audio) |
| **LinkedIn** | `linkedin.com/posts/`, `/pulse/` | Post or Article (text) |
| **Generic website** | Any other URL | Article/page (text + metadata) |

Create an `ingest-output/` subdirectory in the current working directory. All output files go here.

---

## Phase 1: Extract Content

Run extraction for each URL. The approach depends on the platform:

### YouTube
WebFetch does NOT work for YouTube (returns only JS config). Use Playwright or yt-dlp.
1. **Try yt-dlp first** (if installed and not sandboxed): `yt-dlp --write-auto-sub --sub-lang en --skip-download --write-sub -o "ingest-output/%(title)s" <URL>` to pull subtitles
2. **If yt-dlp unavailable**, use Playwright:
   - Navigate to the watch URL and wait 3-5 seconds for the page to fully render
   - Take an accessibility snapshot (`browser_snapshot`) — this captures the full DOM tree including title, channel, view count, likes, description, and duration in a structured format
   - The page title follows the pattern: "Video Title - YouTube"
   - Key data locations in the snapshot: `heading [level=1]` has the title, `"X million subscribers"` for channel size, `"like this video along with N other people"` for likes, view count and age appear as text like `"1.7B views 16 years ago"`, description appears in a text block after the metadata
   - Captions button may say "Subtitles/closed captions unavailable" — note this in output
3. **If audio transcription is needed** and yt-dlp is available: download audio with `yt-dlp -x --audio-format mp3 -o "ingest-output/audio.%(ext)s" <URL>`, then transcribe (if Whisper or similar is installed)
4. Always extract: title, channel, subscriber count, date, description, duration, view count, likes

### X / Twitter
WebFetch does NOT work for X (returns 402). You MUST use Playwright.
1. Navigate to the URL
2. **Wait 5 seconds** after navigation — X loads content asynchronously and the initial snapshot shows only "Loading timeline". The post content appears after the wait.
3. Take an accessibility snapshot after waiting
4. The page title contains the full post text: `"Author on X: "full post text" / X"`
5. Extract from snapshot: post text (in a `generic` element), author name/handle, timestamp (as a `time` element), engagement group (`"N replies, N reposts, N likes, N bookmarks, N views"`), and any quoted tweet content
6. If the page shows "this page doesn't exist" — the post was deleted or the URL is invalid. Note this and move on.
7. X does NOT show replies to non-logged-in users beyond the main post — note this limitation

### Instagram
Use Playwright (WebFetch returns only CSS config, no post data).
1. Navigate to the post URL — Instagram will show a login modal overlay, but the post content IS visible underneath it
2. Take an accessibility snapshot immediately — no need to dismiss the modal, the post data is in the DOM
3. Key data locations: caption text appears as multiple `text` nodes inside a `generic` container, author as a link with handle, engagement as buttons (`"Like"` button followed by count, `"Comment"` button), date as a `time` element, and comments are listed as `generic` blocks with author links and text content
4. The snapshot captures: full caption, author handle (verified badge if present), location, post date, likes count, comments count, and visible comment text with commenter handles
5. For carousel posts, note the number of slides from `listitem` elements in the image area

### TikTok
Use Playwright (WebFetch returns only JS initialization config).
1. Navigate to the TikTok video URL
2. **Wait 3 seconds** — TikTok shows a keyboard shortcuts overlay on first load that obscures the content. After waiting, the full page renders with video metadata visible.
3. Take an accessibility snapshot
4. Key data locations: video title in an `img` alt text and in a text element near the author link, author handle as a `link` with `/url: /@handle`, engagement in `button` elements: `"Like video N likes"`, `"Read or add comments N comments"`, `"Add to Favorites. N added"`, `"Share video N shares"`, sound/music as a link: `"Watch more videos with music [sound name]"`, date appears near the author name
5. The page title updates to include the video description after loading: `"Video Description | TikTok"`
6. TikTok also shows related videos from the same creator — these can provide context about the creator's content style

### LinkedIn
WebFetch works well for LinkedIn posts — try it first (faster than Playwright).
1. **Try WebFetch first**: LinkedIn posts often return readable content via WebFetch, including post text, author, title, engagement metrics, and top comments
2. **If WebFetch returns insufficient data**, fall back to Playwright with a 3-second wait
3. For articles (`/pulse/` URLs): WebFetch usually captures the full article text
4. LinkedIn may require login for full comment threads — extract what's publicly visible and note any limitations

### Generic Website / Article
WebFetch is the primary tool — it works well for most articles and blog posts.
1. **Use WebFetch first** with a prompt asking for title, author, date, and full article text
2. WebFetch converts HTML to markdown and extracts main content effectively for most sites
3. **Fall back to Playwright** only if WebFetch returns JavaScript config instead of article content (indicates a JS-rendered SPA)
4. For long articles: WebFetch may summarize — if the user needs the full text, note this and consider Playwright as supplement
5. Extract: page title, meta description, main body text, author, publication date

### Extraction Output
For each URL, save a raw extraction file: `ingest-output/{platform}-{slug}-raw.md` containing all extracted data in a structured format. This is the working file — the final analysis will be separate.

---

## Phase 2: Analyze Content

With all extracted content in hand, analyze each piece:

1. **Content summary** — What is this about? What's the core message?
2. **Key claims & facts** — What specific claims, statistics, or facts are presented?
3. **Sentiment & tone** — What's the overall tone? Informative, persuasive, emotional, technical?
4. **Audience & context** — Who is this for? What's the broader context?
5. **Notable quotes** — Pull 2-5 direct quotes that capture the essence
6. **If the user provided specific instructions** — focus the analysis on what they asked for

If the user provided multiple URLs, also analyze:
- **Cross-references** — Do the sources agree, contradict, or complement each other?
- **Common themes** — What threads connect across the sources?

---

## Phase 3: Context Research (if needed)

After initial analysis, determine if additional context would strengthen the findings. Research is warranted when:
- The content references events, people, or concepts that need background
- Claims are made that should be fact-checked or contextualized
- The user asked for deeper analysis or "what does this mean?"
- The content is part of a larger ongoing story or debate

If research is needed:
1. Use WebSearch to look up 3-5 targeted queries based on the key claims and topics
2. Cross-reference findings with the original content
3. Add context, corrections, or additional perspective to the analysis
4. Loop back to Phase 2 and enrich the analysis with research findings

If the content is self-contained and the user's request is straightforward, skip this phase.

---

## Phase 4: Synthesize & Write Output

### Per-URL Files
For each URL, write: `ingest-output/{platform}-{descriptive-slug}.md`

```markdown
# {Title or Post Summary}

**Source:** {URL}
**Platform:** {Platform name}
**Author:** {Author/Channel name}
**Date:** {Publication date}
**Extracted:** {Current date/time}

---

## Summary

{2-3 paragraph summary of the content}

## Key Findings

- {Finding 1}
- {Finding 2}
- {Finding 3}
- ...

## Notable Quotes

> "{Direct quote 1}" — {Attribution}

> "{Direct quote 2}" — {Attribution}

## Context & Background

{Any additional context from research, or relevant background}

## Raw Data

{Engagement metrics, view counts, or other quantitative data}

---

*Ingested by the /ingest skill*
```

### Combined Summary File
If multiple URLs were provided, also write: `ingest-output/summary.md`

```markdown
# Ingestion Summary

**Date:** {Current date/time}
**Sources analyzed:** {count}
**User prompt:** {Original user instructions, if any}

---

## Overview

{1-2 paragraph high-level synthesis across all sources}

## Key Takeaways

1. {Takeaway 1 — the most important finding across all sources}
2. {Takeaway 2}
3. {Takeaway 3}
4. ...

## Source-by-Source

### 1. {Source 1 title} ({platform})
{Brief summary + link to detailed file}

### 2. {Source 2 title} ({platform})
{Brief summary + link to detailed file}

## Cross-Source Analysis

{How the sources relate, agree, or contradict each other}

## Recommendations

{If applicable: what should the user do with this information? What are the next steps?}

---

*Ingested by the /ingest skill — {count} sources analyzed*
```

---

## Phase 5: Respond to the User

After writing all files, respond with:

1. A concise summary of what was ingested and the key takeaways (don't make them re-read the whole file)
2. List the output files created in `ingest-output/`
3. Highlight anything surprising, contradictory, or particularly noteworthy
4. If the user had specific questions, answer them directly based on the analysis

Keep the response focused — the detailed analysis is in the markdown files. The response should be the "executive summary" version.

---

## Error Handling

Not every URL will cooperate. When extraction fails or is limited:

- **Login wall**: Note "partial extraction — login required for full content" and analyze what was captured
- **Rate limited / blocked**: Note the limitation, skip to the next URL, mention it in the output
- **Video with no captions**: Note "no transcript available — analysis based on title, description, and metadata only"
- **Dead link / 404**: Note it and move on

Never fail silently. Always tell the user what worked and what didn't so they know the completeness of the analysis.

---

## Tips for Better Results

- The more specific the user's instructions, the more focused the analysis. "What are the key investment takeaways from this video?" produces better output than "analyze this."
- For long YouTube videos, the transcript is the richest source. Prioritize it.
- For social media posts, engagement metrics (likes, views, reply ratio) are data points — include them in the analysis.
- When multiple URLs are provided, the cross-source analysis is where the real value is. Don't just analyze each one in isolation.
