# Stock Screener MD Report

**Type:** Companion
**Parent Skill:** [goldman-sachs-stock-screener](../../)
**Invoked By:** `goldman-sachs-stock-screener` (Step 3a)

## Overview

Formats the completed Goldman Sachs stock screening analysis into a clean, structured Markdown file following GS equity research report conventions.

## How to Use

This skill is invoked automatically by `goldman-sachs-stock-screener` after the 10-stock analysis is complete. You do not need to call it directly.

If you want to regenerate the Markdown report from existing screening data, you can invoke it manually and paste in the analysis output.

## What It Does

Takes the structured screening output and formats it as a `.md` file containing:

- Client investment profile table
- Executive summary paragraph
- Summary table (all 10 stocks, all key metrics)
- Individual stock sections with all 9 analysis steps
- Portfolio construction table (Core / Growth / Speculative)
- Disclaimer and generation timestamp

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Client profile | `goldman-sachs-stock-screener` output | Yes |
| 10-stock analysis | `goldman-sachs-stock-screener` output | Yes |
| Portfolio allocation | `goldman-sachs-stock-screener` output | Yes |

## Output

| File | Format | Naming Convention |
|------|--------|------------------|
| Markdown report | `.md` | `gs-stock-screener-report-YYYY-MM-DD.md` |

## Formatting Conventions

- Metric labels in `**bold**`
- Executive summaries as `>` blockquotes
- Stock sections separated by `---` dividers
- Prices formatted with `$` and commas
- Percentages include `+` prefix for positive values
- Risk scores displayed as `X/10`
- Moat and payout scores capitalized (`Strong`, `Moderate`, `Weak`)
