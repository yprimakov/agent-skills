# Stock Screener HTML Report

**Type:** Companion
**Parent Skill:** [goldman-sachs-stock-screener](../../)
**Invoked By:** `goldman-sachs-stock-screener` (Step 3b)

## Overview

Generates a self-contained, interactive HTML dashboard from the completed Goldman Sachs stock screening data. Produces a production-grade FinTech report with Chart.js visualizations, a sortable data table, and individual stock cards — all in a single `.html` file with no build step required.

## How to Use

This skill is invoked automatically by `goldman-sachs-stock-screener` after the Markdown report is generated. You do not need to call it directly.

To regenerate or customize the HTML report from existing data, invoke it manually and provide the `REPORT_DATA` object populated with your screening results.

## What It Does

Produces a single `.html` file containing:

| Section | Description |
|---------|-------------|
| Top Bar | GS branding, report classification, generation date |
| Hero Header | Report title, client profile badges, sector tags |
| Metrics Strip | 5 key summary stats (avg risk, top pick, avg P/E, etc.) |
| Charts Row | Portfolio allocation donut, risk score bar chart, bull/bear target bar chart |
| Summary Table | Sortable table with all 10 stocks and key metrics |
| Stock Cards Grid | Individual cards per stock with all 9 analysis metrics |
| Portfolio Table | Core / Growth / Speculative allocation with weights |
| Footer | Disclaimer and timestamp |

## Design System

| Property | Value |
|----------|-------|
| Theme | Dark (deep navy / charcoal) |
| Accent colors | Gold (`#c9a84c`), Blue (`#4a9eff`), Green (`#00c896`) |
| Display font | Playfair Display (serif) |
| Data font | IBM Plex Mono (monospace) |
| Body font | IBM Plex Sans |
| Charts | Chart.js via CDN |
| Dependencies | Google Fonts CDN, Chart.js CDN — no build step |

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Client profile | `goldman-sachs-stock-screener` output | Yes |
| 10-stock analysis | `goldman-sachs-stock-screener` output | Yes |
| Portfolio allocation | `goldman-sachs-stock-screener` output | Yes |

## Output

| File | Format | Naming Convention |
|------|--------|------------------|
| Interactive HTML dashboard | `.html` | `gs-stock-screener-report-YYYY-MM-DD.html` |

After saving, the skill automatically opens the file in the user's default browser using the appropriate OS command (`start` on Windows, `open` on macOS, `xdg-open` on Linux).

## Data Structure

All report data is defined in a single `REPORT_DATA` JavaScript object at the top of the script block, making it straightforward to swap in updated or real-time data without touching the layout or chart logic.
