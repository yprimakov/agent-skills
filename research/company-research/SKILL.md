---
name: company-research
description: Produces a comprehensive company due diligence and research report as a self-contained HTML file. Covers corporate structure, financials, leadership, litigation, patents, cybersecurity, employee sentiment, competitive positioning, and 20+ other categories across public and private companies.
  Use this skill whenever the user asks to research a company, investigate a business, run company due diligence, analyze a competitor, evaluate a potential employer, vet a vendor, assess an acquisition target, or understand a company's background. Also use when the user names a company and asks "what can you find out about them?", "tell me about [company]", "is [company] legit?", "dig into [company]", or "company research on [company]".
  Do NOT use for stock analysis or valuation (use goldman-sachs-stock-screener or morgan-stanley-dcf-valuation), real estate (use real-estate-due-diligence), or individual person background checks.
---

# Company Research & Due Diligence

You are a corporate intelligence analyst. You take a company name (and optionally a ticker, URL, or industry) and produce a comprehensive HTML due diligence report covering up to 26 research categories.

The report works for both public and private companies — SEC-dependent categories gracefully degrade for private firms, while web-based research categories always produce results.

---

## Phase 0: Identify the Company

From the user's input, determine:
- **Company legal name** (and any DBAs or former names)
- **Ticker symbol** (if public — search for it even if not provided)
- **Company website URL** (search if not given)
- **Industry / sector** (infer from context or search)
- **Public vs. private** (determines which data sources are available)
- **Headquarters location** (state/country affects regulatory sources)

If ambiguous (e.g., "research Apple" — the tech company or the record label?), ask before proceeding.

---

## Phase 1: Run Research (Tier 1 — Always Run)

These 14 categories use free, publicly available data. Run all of them for every company. Use WebSearch, WebFetch, and Playwright as the primary tools.

**Run searches in parallel groupings — not one at a time.** Batch related searches together.

### 1. Corporate Overview & Structure
**Why:** Establishes the basic facts and reveals related entities, subsidiaries, and ownership complexity.

**Searches:**
- `[company name] SEC EDGAR CIK` (if public)
- `[company name] site:opencorporates.com`
- `[company name] [state] secretary of state business entity`
- `[company name] subsidiaries corporate structure`
- For public: fetch SEC EDGAR Exhibit 21 (subsidiary list) via `https://efts.sec.gov/LATEST/search-index?q=[company]&dateRange=custom&startdt=2024-01-01&forms=10-K`

**Capture:** Legal name, CIK number, SIC code, state of incorporation, date founded, subsidiaries, parent company (if subsidiary), beneficial owners, corporate structure complexity.

### 2. Financial Health
**Why:** Revenue trajectory, profitability, debt load, and cash position reveal whether the company is growing, stable, or distressed.

**Searches:**
- For public: fetch latest 10-K/10-Q from SEC EDGAR full-text search
- `[company name] revenue employees valuation [year]`
- `[company name] financial performance [year]`
- `[ticker] financials site:finance.yahoo.com` or `site:macrotrends.net`

**Capture:** Revenue (trailing 12 months + 3-year trend), net income/loss, gross margin, operating margin, total debt, cash position, debt-to-equity ratio, current ratio, revenue per employee. For private companies: estimate from news, fundraising, and headcount signals.

### 3. Leadership Team
**Why:** Who runs the company, how long they've been there, and what they did before reveals stability, competence, and red flags.

**Searches:**
- `[company name] CEO founder leadership team`
- `[company name] board of directors`
- For public: `[company name] proxy statement DEF 14A` (executive compensation, board composition)
- `[CEO name] background career history`
- `[company name] executive departure OR executive change [year]`

**Capture:** CEO/founder name and tenure, C-suite team, board members, executive compensation (public), recent leadership changes, founder equity (if available), background flags.

### 4. Litigation & Enforcement
**Why:** Active lawsuits, regulatory actions, and settlement history reveal legal exposure and character.

**Searches:**
- `[company name] lawsuit court case`
- `[company name] site:courtlistener.com`
- `[company name] SEC enforcement action`
- `[company name] FTC complaint OR consent decree`
- `[company name] class action settlement`
- `[company name] regulatory fine penalty`

**Capture:** Active lawsuits (plaintiff and defendant), regulatory enforcement actions, class actions, settlements, consent decrees, SEC investigations, criminal charges. Note severity and financial exposure.

### 5. News & Media Coverage
**Why:** Recent news reveals the public narrative — growth stories, scandals, pivots, or crises.

**Searches:**
- `[company name] news [current year]`
- `[company name] controversy OR scandal OR investigation`
- `[company name] acquisition OR merger OR partnership [year]`
- `"[company name]" layoffs OR restructuring`

**Capture:** Top 5-10 recent news items with dates and sources. Categorize as: positive (growth, awards, partnerships), neutral (product updates, leadership changes), or negative (lawsuits, layoffs, scandals). Note the overall media narrative arc.

### 6. Patent & IP Portfolio
**Why:** Patent count and type reveal innovation intensity and defensibility.

**Searches:**
- `[company name] patent site:patents.google.com`
- WebFetch: `https://api.patentsview.org/patents/query?q={"_contains":{"assignee_organization":"[COMPANY]"}}&f=["patent_number","patent_title","patent_date","patent_num_claims"]&o={"page":1,"per_page":25}`
- `[company name] trademark USPTO`

**Capture:** Total patents filed/granted, recent patent activity (last 2 years), key technology areas, trademark registrations, any IP litigation (cross-reference with Category 4).

### 7. Government Contracts
**Why:** Federal contract revenue reveals government dependency and potential conflicts of interest.

**Searches:**
- WebFetch: `https://api.usaspending.gov/api/v2/search/spending_by_award/?filters={"recipient_search_text":["[COMPANY]"],"time_period":[{"start_date":"2023-01-01","end_date":"2026-12-31"}],"award_type_codes":["A","B","C","D"]}`
- `[company name] government contract federal`

**Capture:** Total federal contract value, number of contracts, awarding agencies, contract types, percentage of estimated revenue from government, recent awards.

### 8. Regulatory Compliance History
**Why:** Violations reveal operational quality and legal exposure.

**Searches:**
- `[company name] FDA warning letter` (healthcare/pharma/food)
- `[company name] OSHA violation` (any employer)
- `[company name] EPA enforcement` (manufacturing/energy)
- `[company name] CFPB enforcement` (financial services)
- `[company name] data breach notification`

**Capture:** Warning letters, citations, fines, consent orders, corrective actions by agency. Note recency and severity. Flag repeat offenders.

### 9. Domain & Brand Infrastructure
**Why:** Domain age, web history, and trademark status reveal brand maturity and legitimacy.

**Searches:**
- `[company domain] site:web.archive.org` (Wayback Machine history)
- `whois [company domain]` (domain registration date and registrar)
- `[company name] trademark site:tsdr.uspto.gov`
- `[company domain] domain age`

**Capture:** Domain registration date, registrar, historical snapshots (how has the site changed?), active trademarks, trademark disputes.

### 10. Cybersecurity Posture
**Why:** Security hygiene correlates with operational maturity and data protection practices.

**Searches:**
- WebFetch: `https://securityheaders.com/?q=[company-domain]&followRedirects=on`
- `[company domain] SSL certificate site:ssllabs.com`
- `[company name] data breach site:haveibeenpwned.com`
- `[company name] security incident OR data breach [year]`

**Capture:** Security headers grade (A-F), SSL/TLS configuration, known breaches, breach notification history, security certifications (SOC 2, ISO 27001) mentioned on website.

### 11. BBB & Consumer Complaints
**Why:** Complaint volume and resolution patterns reveal customer service quality and business practices.

**Searches:**
- `[company name] site:bbb.org`
- `[company name] consumer complaint CFPB`
- `[company name] complaint [state] attorney general`

**Capture:** BBB rating (A+ to F), accreditation status, complaint count (last 3 years), complaint resolution rate, CFPB complaint count, common complaint themes.

### 12. Social Media & Brand Sentiment
**Why:** Public perception and community health signal brand strength and potential reputational risks.

**Searches:**
- `[company name] site:reddit.com review OR complaint OR praise`
- `[company name] site:x.com controversy OR love OR hate`
- `[company name] customer review sentiment [year]`

**Capture:** Overall sentiment (positive/mixed/negative), common praise themes, common complaint themes, viral moments (positive or negative), community size/engagement.

### 13. Product & Service Reviews
**Why:** Third-party reviews reveal product quality and customer satisfaction independent of marketing.

**Searches:**
- `[company name] site:g2.com`
- `[company name] site:capterra.com`
- `[company name] reviews site:trustpilot.com`
- `[company name] app review` (if has mobile app)

**Capture:** G2/Capterra rating (out of 5), review count, common pros/cons, NPS if available, competitive comparison mentions, app store rating.

### 14. Tax & Accounting Red Flags
**Why:** Auditor changes, restatements, and going-concern opinions are early warning signals.

**Searches (public companies only):**
- `[company name] auditor change 8-K`
- `[company name] financial restatement`
- `[company name] going concern`
- `[company name] SEC comment letter`

**Capture:** Current auditor name, any auditor changes in last 3 years (red flag), restatement history, going-concern opinions, material weaknesses in internal controls, SEC comment letters.

---

## Phase 2: Run Research (Tier 2 — When Available)

These 7 categories may produce limited data depending on company size and public/private status. Run them but don't force results — "Data not available" is a valid finding.

### 15. Competitive Positioning
**Searches:** `[company name] competitors market share`, `[company name] vs [competitor]`, `[industry] market landscape [year]`
**Capture:** Top 3-5 competitors, estimated market position, competitive advantages/moats, market share if available.

### 16. Market & Industry Context
**Searches:** `[industry] market size growth rate [year]`, `[industry] trends [year]`, `[industry] regulatory outlook`
**Capture:** Industry size (TAM), growth rate, key trends, regulatory tailwinds/headwinds, macro risks.

### 17. Employee Sentiment
**Searches:** `[company name] site:glassdoor.com reviews`, `[company name] employer review`, `[company name] work culture`
**Capture:** Glassdoor rating (out of 5), CEO approval %, "recommend to a friend" %, top pros/cons themes, recent review trend (improving/declining).
**Note:** Glassdoor requires Playwright for JS rendering. If extraction fails, note "Glassdoor data requires manual review" and provide the direct URL.

### 18. Funding History
**Searches:** `[company name] funding round series`, `[company name] site:crunchbase.com`, `[company name] investors valuation`
**Capture:** Total funding raised, funding rounds with dates and amounts, lead investors, last known valuation, notable exits/acquisitions.

### 19. ESG Ratings
**Searches:** `[company name] ESG rating score`, `[company name] sustainability report`, `[company name] diversity equity inclusion`
**Capture:** ESG rating from any provider, environmental initiatives, diversity metrics (if disclosed), governance score, controversy score.

### 20. Technology Stack
**Searches:** `[company domain] site:builtwith.com`, `[company name] technology stack engineering blog`
**Capture:** Key technologies detected (hosting, frameworks, analytics, CMS), engineering team size signals, technical blog maturity.

### 21. Web Traffic
**Searches:** `[company domain] site:similarweb.com`, `[company name] website traffic monthly visits`
**Capture:** Estimated monthly visits, traffic trend (growing/declining), top traffic sources, geographic distribution.

---

## Phase 3: Note Tier 3 Enrichment Opportunities

Don't research these — just note them as "recommended for deeper analysis" in the report:

- 22. Employee & Hiring Signals (LinkedIn Talent Insights)
- 23. Supply Chain Risk (Resilinc, import records)
- 24. Company Culture Deep Dive (beyond Glassdoor)
- 25. Industry Analyst Reports (Gartner, Forrester, IDC)
- 26. Detailed Valuation — if public, reference the `/morgan-stanley-dcf-valuation` skill

---

## Phase 4: Synthesize & Assess Risk

For each researched category, assign a risk level:
- **CLEAR** (green) — No issues found, positive indicators
- **CAUTION** (amber) — Minor concerns, needs monitoring, or incomplete data
- **HIGH RISK** (red) — Significant issues found, requires investigation
- **NOT AVAILABLE** (gray) — Data not accessible (private company, blocked, etc.)

Write an executive summary (2-3 paragraphs) covering:
1. What the company does and its market position
2. Key strengths discovered in the research
3. Key risks or red flags that warrant further investigation
4. Overall risk posture (low / moderate / elevated / high)

---

## Phase 5: Generate HTML Report

Output a single self-contained HTML file: `{company-slug}-research.html`

The HTML must be fully self-contained — all CSS inline, no external dependencies. Use this design system:

### Design Specifications

**Header:**
- Dark navy background (`#0D1B2A`) spanning full width
- Company name in white, large font (28-32px)
- Ticker symbol (if public) in gold (`#C9A84C`) next to company name
- Industry tag and overall risk badge in the header
- Subtitle: "Company Due Diligence Report — Generated {date}"

**Company Snapshot Grid:**
- 6-8 metric cards in a responsive grid (2-3 columns)
- Each card: metric label (small, muted), value (large, bold)
- Cards for: Founded, HQ, Employees, Revenue, Funding, Industry, Website, Ticker

**Executive Summary:**
- Gold (`#C9A84C`) left border accent box
- White background with slight shadow
- 2-3 paragraph narrative

**Research Categories:**
- Each category is a collapsible card (use `<details>/<summary>` for no-JS collapsing)
- Card header: category name + risk badge (color-coded pill)
- Card body: data table with alternating row shading + narrative paragraphs
- Table styling: `border-collapse: collapse`, subtle borders, left-aligned text
- Risk badge colors: green (#2d9e5c) CLEAR, amber (#d4a017) CAUTION, red (#c0392b) HIGH RISK, gray (#6c757d) NOT AVAILABLE

**Risk Summary Matrix:**
- Full-width table after all categories
- Columns: #, Category, Status (color dot), Key Finding, Recommended Action
- Sorted by risk level (red first, then amber, then green)

**Enrichment Opportunities:**
- Light gray box listing Tier 3 categories as "Recommended for deeper analysis"
- Each with a brief description of what it would reveal and what tool/service provides it

**Sources:**
- Numbered list at the bottom
- Each source: clickable URL, source name, what was found there

**Footer:**
- Gray background, small text
- Disclaimer: "This report is based on publicly available information and should not be considered legal, financial, or investment advice. Verify all findings with authoritative sources before making decisions."
- Generation date and tool attribution

**Responsive Design:**
- Works at 1200px+ (desktop), 768px (tablet), and 375px (mobile)
- Cards stack single-column on mobile
- Tables scroll horizontally on small screens

**Typography:**
- Font stack: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- Load Inter from Google Fonts CDN (single `<link>` tag)
- Heading sizes: h1=28px, h2=22px, h3=18px
- Body: 15px, line-height 1.6

Save to: `{company-slug}-research.html` in the current working directory.

---

## Phase 6: Respond to User

After writing the HTML file:

1. Present a concise in-chat summary with the risk matrix table
2. List the top 3 findings (most important things the user should know)
3. Highlight any red flags
4. Note what couldn't be found and what Tier 3 enrichment would add
5. Tell the user the file path

---

## Quality Checklist

- [ ] All 14 Tier 1 categories researched (none skipped)
- [ ] All 7 Tier 2 categories attempted (with graceful "not available" where needed)
- [ ] Tier 3 categories listed as enrichment opportunities
- [ ] Risk level assigned to every category
- [ ] Executive summary written with specific findings (not generic boilerplate)
- [ ] At least 15 distinct sources cited with URLs
- [ ] HTML is self-contained (no broken external references)
- [ ] Collapsible sections work without JavaScript (using `<details>/<summary>`)
- [ ] Risk badges are color-coded correctly
- [ ] Responsive layout works at mobile widths
- [ ] Sources are clickable links
- [ ] Disclaimer present in footer
- [ ] Company name, ticker, and industry correct in header
- [ ] Private company categories degrade gracefully (not "error" — "not available for private companies")

---

## Important Notes

- All information is from public sources. This is not a substitute for professional due diligence.
- SEC EDGAR is authoritative for public company filings. For private companies, web search and news are the primary sources.
- Always note the date of the most recent data found — stale data should be flagged.
- When sources conflict, present both versions and note the discrepancy.
- For the HTML output: test that it renders correctly by reading back the file after writing. If it's too large for a single Write, use Python to generate it.
