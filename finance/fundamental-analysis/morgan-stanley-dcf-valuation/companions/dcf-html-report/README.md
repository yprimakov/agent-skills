# DCF HTML Report

**Type:** Companion
**Author:** Yury Primakov
**Parent Skill:** [morgan-stanley-dcf-valuation](../../)
**Invoked By:** `morgan-stanley-dcf-valuation` (Step 3b)

## Overview

Generates a self-contained interactive HTML dashboard from the completed DCF valuation model, using the iMadeFire UI design system.

## What It Produces

A single `.html` file containing:

| Section | Description |
|---------|-------------|
| Topbar | 🔥 iMadeFire brand, ticker, date |
| Hero | Company name, verdict badge, intrinsic vs. market price |
| Verdict Card | Large color-coded UNDERVALUED/FAIRLY VALUED/OVERVALUED card |
| Metrics Strip | WACC, TGR, 5Y Revenue CAGR, Year 5 FCF, Exit Multiple |
| Revenue & FCF Chart | Dual-line Chart.js — revenue and FCF over 5 years |
| WACC Chart | Horizontal bar chart of WACC components |
| Sensitivity Heatmap | Color-coded HTML table (green/amber/red vs. current price) |
| Projection Table | Full 5-year model with all line items |
| WACC Breakdown | All CAPM inputs in a structured card |
| Terminal Value | Exit multiple vs. perpetuity growth side by side |
| Risk Assessment | Top 5 model risks with impact badges |
| Footer | Disclaimer and iMadeFire branding |

## Design
Follows the iMadeFire UI design system (`/design/iMadeFire-ui/`). Dark navy background, indigo/violet accents, Plus Jakarta Sans + IBM Plex Mono fonts.

## Auto-Launch
Opens automatically in the default browser after saving.

## File Naming
`dcf-valuation-[TICKER]-YYYY-MM-DD.html`
