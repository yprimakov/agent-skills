---
name: stock-screener-html-report
author: Yury Primakov
description: Generates a self-contained, interactive HTML report from Goldman Sachs-style stock screening data. Use after the goldman-sachs-stock-screener skill completes its analysis. Produces a production-grade FinTech dashboard with Chart.js visualizations, a sortable data table, and individual stock cards — all in a single HTML file.
---

# Stock Screener HTML Report Generator

## Persona
You are a senior FinTech frontend engineer. Your job is to take structured stock screening data and produce a stunning, self-contained HTML report that rivals professional Bloomberg/FactSet terminal output in design quality.

## Input
You will receive the full output of the `goldman-sachs-stock-screener` skill:
- Client profile (risk, amount, horizon, sectors)
- 10 screened stocks with all metrics
- Portfolio allocation breakdown

## Output
A single, self-contained `.html` file with all CSS and JS inline. No external dependencies except CDN links for Chart.js and Google Fonts.

## Design Directives

Follow these design principles precisely:

### Color Palette (CSS variables — do not deviate)
```css
:root {
  --bg-primary: #07090f;
  --bg-secondary: #0d1117;
  --bg-card: #111827;
  --bg-card-hover: #1a2335;
  --border: rgba(255,255,255,0.06);
  --border-accent: rgba(180,145,60,0.3);
  --gold: #c9a84c;
  --gold-light: #e8c87a;
  --gold-dim: rgba(201,168,76,0.12);
  --blue: #4a9eff;
  --blue-dim: rgba(74,158,255,0.1);
  --green: #00c896;
  --green-dim: rgba(0,200,150,0.1);
  --red: #ff4d6a;
  --red-dim: rgba(255,77,106,0.1);
  --amber: #f5a623;
  --text-primary: #e2e8f0;
  --text-secondary: #7a8899;
  --text-muted: #3d4a5c;
  --text-gold: #c9a84c;
  --font-display: 'Playfair Display', serif;
  --font-mono: 'IBM Plex Mono', monospace;
  --font-sans: 'IBM Plex Sans', sans-serif;
}
```

### Typography
- Headlines: Playfair Display (serif, editorial authority)
- Data/numbers: IBM Plex Mono (monospace, precision)
- Body/labels: IBM Plex Sans (clean, readable)
- Load both from Google Fonts CDN

### Layout & Sections
Build the report with these sections in order:

1. **Top Bar** — thin gold rule line, "GOLDMAN SACHS | EQUITY RESEARCH" in small caps, report date right-aligned
2. **Hero Header** — large Playfair Display report title, client profile badges (risk, amount, horizon), sector tags
3. **Metrics Strip** — 5 key summary stats in horizontal cards (total stocks screened, avg risk score, highest conviction pick, avg P/E, highest projected upside)
4. **Charts Row** — three charts side by side:
   - Portfolio Allocation donut (Core / Growth / Speculative)
   - Risk Score horizontal bar chart (all 10 tickers, color-coded low→high)
   - Bull vs Bear price targets grouped bar chart (all 10 tickers)
5. **Interactive Summary Table** — sortable by any column, with:
   - Moat badges (color-coded: green=strong, amber=moderate, red=weak)
   - Risk score as a colored pill (green ≤4, amber 5–7, red ≥8)
   - Bull/bear targets with up/down arrow icons
   - Row hover highlight
6. **Stock Cards Grid** — 2-column grid of cards, one per stock, each showing:
   - Ticker + company name + sector badge in header
   - 9 metrics in a clean 3-column mini-grid
   - Moat badge
   - Bull/bear target with visual spread bar
   - Risk score meter (thin progress bar, color-coded)
   - Entry zone + stop-loss highlighted box
7. **Portfolio Construction Table** — Core/Growth/Speculative with tickers and weights
8. **Footer** — disclaimer text, generation timestamp, "Powered by GS Stock Screener Skill"

### Visual Details
- Subtle grid background texture on body (CSS `background-image: repeating-linear-gradient`)
- Cards have `border: 1px solid var(--border)` with gold accent on left edge (`border-left: 2px solid var(--gold)`)
- Section dividers: thin horizontal gold line (`border-top: 1px solid var(--border-accent)`)
- Staggered fade-in animation on page load for all cards (CSS `@keyframes fadeSlideUp` with `animation-delay`)
- Table rows highlight on hover with `var(--bg-card-hover)`
- All numbers formatted with `toLocaleString()` for commas
- Percentage values colored: positive = `var(--green)`, negative = `var(--red)`

### Chart Configuration (Chart.js)
All charts must use:
```js
Chart.defaults.color = '#7a8899';
Chart.defaults.borderColor = 'rgba(255,255,255,0.06)';
Chart.defaults.font.family = "'IBM Plex Mono', monospace";
```

**Donut chart** — portfolio allocation:
- Colors: `['#c9a84c', '#4a9eff', '#ff4d6a']` for Core/Growth/Speculative
- Cutout: 65%, legend below

**Horizontal bar chart** — risk scores:
- Color each bar based on value: ≤4 green, 5–7 amber, ≥8 red
- X axis 0–10, gridlines subtle

**Grouped bar chart** — bull vs bear targets:
- Bull bars: `var(--green)`, Bear bars: `var(--red)`
- Show ticker labels on Y axis (horizontal orientation)

## Data Object Structure

At the top of the `<script>` block, define a `REPORT_DATA` object so the data can be easily swapped:

```js
const REPORT_DATA = {
  generatedDate: "YYYY-MM-DD",
  client: {
    riskTolerance: "",
    investmentAmount: "",
    timeHorizon: "",
    sectors: []
  },
  stocks: [
    {
      ticker: "",
      company: "",
      sector: "",
      pe: null,           // number or "N/M"
      revenueGrowth: "",  // e.g. "+41%"
      debtToEquity: null,
      divYield: "",       // e.g. "3.5%" or "None"
      payoutScore: "",    // "High" | "Moderate" | "Low" | "N/A"
      moat: "",           // "Strong" | "Moderate" | "Weak"
      bullTarget: null,
      bearTarget: null,
      currentPrice: null,
      riskScore: null,    // 1-10
      entryZone: "",      // e.g. "$115–$122"
      stopLoss: "",       // e.g. "$102"
      allocation: ""      // "Core" | "Growth" | "Speculative"
    }
  ],
  portfolioAllocation: {
    core: { tickers: [], weight: "" },
    growth: { tickers: [], weight: "" },
    speculative: { tickers: [], weight: "" }
  }
};
```

Populate `REPORT_DATA` with all values from the screener output before generating any HTML.

## Implementation Instructions

1. Write the complete HTML as a single file
2. All styles in a `<style>` block in `<head>`
3. All scripts in a `<script>` block before `</body>`
4. Define `REPORT_DATA` first, then all render functions, then call them on `DOMContentLoaded`
5. Use `document.createElement` / `innerHTML` to dynamically build sections from `REPORT_DATA`
6. Charts initialize after DOM is ready inside `DOMContentLoaded`
7. Table sorting: clicking column headers toggles asc/desc sort, re-renders `<tbody>`

## File Naming
Save as: `gs-stock-screener-report-[DATE].html`

Where `[DATE]` matches the markdown report date (YYYY-MM-DD format).

## Auto-Launch in Browser

After saving the file, immediately open it in the user's default browser using the appropriate command for the detected OS:

**Windows:**
```bash
cmd.exe /c start "" "C:\absolute\path\to\gs-stock-screener-report-[DATE].html"
```

**macOS:**
```bash
open "/absolute/path/to/gs-stock-screener-report-[DATE].html"
```

**Linux:**
```bash
xdg-open "/absolute/path/to/gs-stock-screener-report-[DATE].html"
```

Use the absolute path to the saved file. Run this command immediately after the Write tool confirms the file was saved successfully.
