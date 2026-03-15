# DCF MD Report

**Type:** Companion
**Author:** Yury Primakov
**Parent Skill:** [morgan-stanley-dcf-valuation](../../)
**Invoked By:** `morgan-stanley-dcf-valuation` (Step 3a)

## Overview

Formats the completed Morgan Stanley-style DCF analysis into a structured Markdown valuation memo following investment banking conventions.

## What It Produces

A single `.md` file containing:

| Section | Description |
|---------|-------------|
| Executive Summary | Verdict, intrinsic value, market price, implied upside/downside |
| Revenue Projections | 5-year table with growth % and assumptions |
| Margin Estimates | EBIT and margin trajectory by year |
| FCF Model | Full line-item free cash flow table |
| WACC Calculation | All CAPM inputs and blended WACC |
| Terminal Value | Both exit multiple and perpetuity growth results |
| Sensitivity Analysis | 5×5 WACC vs. terminal growth grid |
| Valuation Summary | EV bridge to per-share intrinsic value |
| Investment Verdict | Final call with thesis paragraph |
| Key Model Risks | Top 5 assumptions ranked by impact |

## File Naming
`dcf-valuation-[TICKER]-YYYY-MM-DD.md`
