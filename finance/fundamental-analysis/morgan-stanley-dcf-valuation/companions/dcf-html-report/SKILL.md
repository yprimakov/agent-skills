---
name: dcf-html-report
author: Yury Primakov
description: Generates a self-contained interactive HTML DCF valuation dashboard using the iMadeFire UI design system. Use after the morgan-stanley-dcf-valuation skill completes its model. Produces a single .html file with Chart.js visualizations, a WACC breakdown, sensitivity table, and verdict card.
---

# DCF Valuation HTML Report Generator

## Persona
You are a senior FinTech frontend engineer. Take the completed DCF model output and render it as a polished, self-contained iMadeFire UI HTML dashboard.

## Design System
Follow the iMadeFire UI design system exactly as documented in `/design/iMadeFire-ui/README.md`. Copy the CSS `:root` variable block verbatim. Use Plus Jakarta Sans + IBM Plex Mono fonts.

## Sections (in order)

1. **Topbar** — 🔥 iMadeFire brand, ticker pill, date pill, "Valuation Memo" label
2. **Hero** — Company name + ticker, verdict badge (color-coded), intrinsic value vs. market price, implied upside/downside
3. **Verdict Card** — Large prominent card: UNDERVALUED / FAIRLY VALUED / OVERVALUED with color (green/amber/red), intrinsic value, market price, upside %, one-line thesis
4. **Metrics Strip** — 5 cards: WACC, Terminal Growth Rate, 5Y Revenue CAGR, FCF Year 5, EV/EBITDA Exit Multiple
5. **Charts Row** — Three charts side by side:
   - Revenue & FCF line chart (dual axis, 5 years)
   - WACC waterfall/bar chart showing components (Re, Rd, blended)
   - Sensitivity heatmap table (styled as colored HTML table, not a chart — color cells from red→amber→green based on value relative to current price)
6. **Projection Table** — Full 5-year model: Revenue, Growth %, EBIT, EBIT Margin, D&A, CapEx, ΔNWC, FCF
7. **WACC Breakdown Card** — All inputs in a clean two-column layout
8. **Terminal Value Card** — Side-by-side: Exit Multiple method vs. Perpetuity Growth method, base case average
9. **Sensitivity Table** — Full colored grid (WACC rows × TGR columns), cells colored:
   - Green: implied price > current price × 1.15
   - Amber: within ±15% of current price
   - Red: implied price < current price × 0.85
   - Bold cell for base case
10. **Risk Assessment** — Ranked list of top 5 model risks as cards with impact badge
11. **Footer** — Disclaimer, 🔥 iMadeFire brand, generation date

## Data Object

Define at top of `<script>`:

```js
const DCF_DATA = {
  generatedDate: "YYYY-MM-DD",
  ticker: "",
  company: "",
  currentPrice: null,
  intrinsicValue: null,
  verdict: "",           // "UNDERVALUED" | "FAIRLY VALUED" | "OVERVALUED"
  updownPct: null,       // e.g. 34.2 (positive = upside, negative = downside)
  thesis: "",
  wacc: {
    rf: null,            // risk-free rate %
    erp: null,           // equity risk premium %
    beta: null,
    re: null,            // cost of equity %
    rdPretax: null,      // pre-tax cost of debt %
    taxRate: null,
    rdAftertax: null,
    equityWeight: null,
    debtWeight: null,
    wacc: null           // final WACC %
  },
  projections: [
    // 5 objects, one per year:
    { year: "", revenue: null, growthPct: null, ebit: null, ebitMarginPct: null,
      da: null, capex: null, deltaWC: null, fcf: null }
  ],
  terminalValue: {
    exitMultiple: null,
    exitMultipleTV: null,
    tgr: null,           // terminal growth rate %
    perpetuityTV: null,
    baseCaseTV: null
  },
  valuation: {
    ev: null,
    netDebt: null,
    equityValue: null,
    sharesOut: null,
    intrinsicPerShare: null
  },
  sensitivity: {
    waccValues: [],      // array of WACC % values (rows)
    tgrValues: [],       // array of TGR % values (columns)
    grid: []             // 2D array of implied share prices
  },
  risks: [
    { rank: 1, assumption: "", baseCase: "", bearCase: "", impact: "High" }
  ]
};
```

## Chart Specifications

**Revenue & FCF Line Chart (Chart.js):**
- X axis: years
- Line 1: Revenue — `var(--indigo)`, fill with `var(--indigo-dim)`
- Line 2: FCF — `var(--green)`, dashed, no fill
- Dual Y axis if scale difference is large

**WACC Components Bar Chart:**
- Horizontal bars: Cost of Equity, After-tax Cost of Debt, Blended WACC
- Colors: `#a5b4fc`, `var(--sky)`, `var(--indigo)`
- Show percentage labels on bars

**Sensitivity Table (HTML, not canvas):**
- Render as `<table>` with colored `<td>` backgrounds
- Base case cell: bold border `2px solid var(--indigo)`

## Auto-Launch
After saving, open in the default browser:
- Windows: `powershell -Command "Start-Process '<absolute-path>'"`
- macOS: `open <path>`
- Linux: `xdg-open <path>`

## File Naming
Save as: `dcf-valuation-[TICKER]-[DATE].html`
