# iMadeFire UI — Design System

**Author:** Yury Primakov
**Version:** 1.0
**Used by:** All iMadeFire skill HTML report outputs

---

## Overview

The iMadeFire UI is a dark FinTech dashboard design system inspired by modern SaaS financial platforms. It is data-dense, highly readable, and visually distinctive without relying on heavy decoration.

The design language prioritizes:
- **Clarity** — data is the hero, not the chrome
- **Hierarchy** — indigo/violet accents guide the eye to what matters
- **Density** — maximum information in minimum space, without feeling crowded
- **Consistency** — identical component patterns across every report

---

## Branding

| Element | Value |
|---------|-------|
| Brand name | iMadeFire |
| Logo | 🔥 |
| Tagline | *(none — let the data speak)* |
| Brand color | `#6366f1` (indigo) |

The brand icon in the topbar is a 30×30px rounded square with a `linear-gradient(135deg, #6366f1, #8b5cf6)` background displaying the 🔥 emoji.

---

## Color Palette

Copy this CSS `:root` block verbatim into every HTML report `<style>` section.

```css
:root {
  /* Backgrounds */
  --bg:          #0b0d1a;   /* page background */
  --bg-surface:  #111327;   /* table headers, input backgrounds */
  --bg-card:     #161930;   /* card backgrounds */
  --bg-card-h:   #1c2040;   /* card hover state */
  --bg-input:    #0e1022;   /* search/input fields */

  /* Primary accent — indigo/violet */
  --indigo:      #6366f1;
  --indigo-dim:  rgba(99,102,241,0.12);
  --indigo-glow: rgba(99,102,241,0.25);
  --violet:      #8b5cf6;
  --violet-dim:  rgba(139,92,246,0.12);

  /* Semantic colors */
  --green:       #22c55e;   /* positive, bull, profit */
  --green-dim:   rgba(34,197,94,0.12);
  --red:         #f43f5e;   /* negative, bear, loss */
  --red-dim:     rgba(244,63,94,0.12);
  --amber:       #f59e0b;   /* warning, moderate risk */
  --amber-dim:   rgba(245,158,11,0.12);
  --sky:         #38bdf8;   /* data highlights, entry zones */
  --sky-dim:     rgba(56,189,248,0.12);

  /* Borders */
  --border:      rgba(255,255,255,0.07);   /* default border */
  --border-v:    rgba(99,102,241,0.18);    /* accent border (hover, focus) */

  /* Typography */
  --t1: #f1f5f9;   /* primary text */
  --t2: #94a3b8;   /* secondary text */
  --t3: #475569;   /* muted text, labels */

  /* Radii */
  --r:    12px;   /* cards, containers */
  --r-sm:  8px;   /* inner elements, chips */
  --r-xs:  6px;   /* badges, small pills */

  /* Fonts */
  --font: 'Plus Jakarta Sans', sans-serif;
  --mono: 'IBM Plex Mono', monospace;

  /* Shadows */
  --shadow:   0 4px 24px rgba(0,0,0,0.4);
  --shadow-v: 0 4px 24px rgba(99,102,241,0.15);
}
```

---

## Typography

### Fonts
Load from Google Fonts CDN — include this in every report `<head>`:

```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@300;400;500;600&display=swap" rel="stylesheet" />
```

| Role | Font | Weights Used |
|------|------|-------------|
| All headings, body, UI labels | Plus Jakarta Sans | 400, 500, 600, 700, 800 |
| Numbers, data, tickers, dates, code | IBM Plex Mono | 400, 500, 600 |

### Scale

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Page title / hero | 28px | 800 | `letter-spacing: -0.03em` |
| Section title | 16px | 700 | `letter-spacing: -0.02em` |
| Card ticker | 22px | 700 | Mono, `color: #a5b4fc` |
| Metric value | 24px | 600 | Mono |
| Body text | 14px | 400 | — |
| Labels / eyebrows | 11px | 700 | Uppercase, `letter-spacing: 0.08em` |
| Table headers | 11px | 700 | Uppercase, `letter-spacing: 0.08em` |
| Fine print / muted | 11–12px | 400 | `color: var(--t3)` |

---

## Page Layout

```
┌─────────────────────────────────────────┐
│  TOPBAR (sticky, 60px, blur backdrop)   │
├─────────────────────────────────────────┤
│  PAGE (max-width: 1280px, padding: 32px)│
│  ┌─────────────────────────────────────┐│
│  │ HERO (title, badges, date)          ││
│  ├─────────────────────────────────────┤│
│  │ METRICS STRIP (5-col grid)          ││
│  ├─────────────────────────────────────┤│
│  │ SECTION (charts / table / cards...) ││
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
```

- **Topbar:** `position: sticky; top: 0; backdrop-filter: blur(12px); background: rgba(11,13,26,0.85)`
- **Page container:** `max-width: 1280px; margin: 0 auto; padding: 32px 32px 64px`
- **Section spacing:** `margin-bottom: 24px`
- **Grid gaps:** `16px` between cards, `20px` between major sections

### Body background
```css
body {
  background: var(--bg);
  background-image: radial-gradient(ellipse 80% 50% at 50% -10%, rgba(99,102,241,0.12) 0%, transparent 60%);
}
```

---

## Components

### Topbar

```html
<div class="topbar">
  <div class="topbar-brand">
    <div class="brand-icon">🔥</div>
    <div class="brand-name">iMadeFire</div>
  </div>
  <div class="topbar-right">
    <div class="topbar-pill">YYYY-MM-DD</div>
    <div class="topbar-pill">For Client Use Only</div>
    <div class="topbar-avatar">U</div>
  </div>
</div>
```

```css
.topbar { height: 60px; padding: 0 32px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border); }
.brand-icon { width: 30px; height: 30px; border-radius: 8px; background: linear-gradient(135deg, var(--indigo), var(--violet)); font-size: 16px; display: flex; align-items: center; justify-content: center; }
.brand-name { font-size: 15px; font-weight: 700; letter-spacing: -0.02em; }
.topbar-pill { font-family: var(--mono); font-size: 11px; color: var(--t2); padding: 4px 10px; background: var(--bg-card); border: 1px solid var(--border); border-radius: 6px; }
.topbar-avatar { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(135deg, #6366f1, #8b5cf6); border: 2px solid var(--border-v); }
```

---

### Cards

All cards share these base styles:

```css
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--r);
  padding: 20px;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.card:hover {
  border-color: var(--border-v);
  box-shadow: var(--shadow-v);
}
```

---

### Badges

```css
.badge { display: inline-flex; align-items: center; gap: 5px; padding: 4px 12px; border-radius: var(--r-xs); font-size: 12px; font-weight: 600; }
.badge-v   { background: var(--indigo-dim); border: 1px solid var(--border-v);              color: #a5b4fc; }
.badge-g   { background: var(--green-dim);  border: 1px solid rgba(34,197,94,0.2);          color: var(--green); }
.badge-sky { background: var(--sky-dim);    border: 1px solid rgba(56,189,248,0.2);         color: var(--sky); }
.badge-red { background: var(--red-dim);    border: 1px solid rgba(244,63,94,0.2);          color: var(--red); }
.badge-amb { background: var(--amber-dim);  border: 1px solid rgba(245,158,11,0.2);         color: var(--amber); }
```

---

### Section Headers

```css
.section-title {
  font-size: 16px; font-weight: 700; letter-spacing: -0.02em;
  display: flex; align-items: center; gap: 8px;
}
.section-title::before {
  content: ''; display: block; width: 3px; height: 18px;
  background: linear-gradient(to bottom, var(--indigo), var(--violet));
  border-radius: 2px;
}
```

---

### Tables

```css
thead th { padding: 12px 16px; font-size: 11px; font-weight: 700; color: var(--t3); text-transform: uppercase; letter-spacing: 0.08em; background: var(--bg-surface); border-bottom: 1px solid var(--border); }
thead th:hover { color: var(--indigo); }
tbody tr { border-bottom: 1px solid var(--border); transition: background 0.12s; }
tbody tr:hover { background: var(--bg-card-h); }
tbody td { padding: 13px 16px; }
```

Wrap tables in a container with `border-radius: var(--r); overflow: hidden` so corners clip correctly.

---

### Risk / Status Indicators

**Risk chips** (used in tables):
```css
.risk-lo { background: var(--green-dim); color: var(--green); }  /* score ≤ 4 */
.risk-md { background: var(--amber-dim); color: var(--amber); }  /* score 5–7 */
.risk-hi { background: var(--red-dim);   color: var(--red);   }  /* score ≥ 8 */
```

**Moat pills:**
```css
.moat-strong   { background: var(--green-dim); color: var(--green); border: 1px solid rgba(34,197,94,0.2); }
.moat-moderate { background: var(--amber-dim); color: var(--amber); border: 1px solid rgba(245,158,11,0.2); }
.moat-weak     { background: var(--red-dim);   color: var(--red);   border: 1px solid rgba(244,63,94,0.2); }
```

**Progress/score bars:**
```css
.bar-track { height: 5px; background: var(--bg-surface); border-radius: 3px; overflow: hidden; border: 1px solid var(--border); }
.bar-fill  { height: 100%; border-radius: 3px; } /* set background color dynamically based on value */
```

---

### Chart.js Defaults

Apply before initializing any chart:

```js
Chart.defaults.color = '#475569';
Chart.defaults.borderColor = 'rgba(255,255,255,0.06)';
Chart.defaults.font.family = "'IBM Plex Mono', monospace";
Chart.defaults.font.size = 11;
```

**Standard color assignments:**
| Purpose | Color |
|---------|-------|
| Primary / Core | `#6366f1` |
| Positive / Bull / Growth | `rgba(34,197,94,0.65)` |
| Negative / Bear / Loss | `rgba(244,63,94,0.65)` |
| Secondary data | `#38bdf8` |
| Warning / Moderate | `#f59e0b` |
| Speculative | `#f43f5e` |

Bar chart `borderRadius: 4`. Donut `cutout: '68%'`. Legend `position: 'bottom'` with `usePointStyle: true`.

---

### Animations

All major sections fade in on page load with staggered delays:

```css
@keyframes up {
  from { opacity: 0; transform: translateY(14px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

Apply with `animation: up 0.5s ease both` and increment `animation-delay` by `0.05s` per section or card.

---

## Collapsible Panels

For expandable content sections (e.g., analyst notes):

```css
.toggle { cursor: pointer; user-select: none; font-size: 11px; font-weight: 700; color: var(--t3); text-transform: uppercase; letter-spacing: 0.08em; }
.toggle:hover { color: var(--indigo); }
.toggle-body { display: none; margin-top: 12px; }
.toggle-body.open { display: block; }
```

Toggle open/close via: `element.classList.toggle('open')`

---

## Responsive Breakpoints

```css
@media (max-width: 960px) {
  .metrics-strip { grid-template-columns: repeat(3, 1fr); }
  .charts-row    { grid-template-columns: 1fr; }
  .cards-grid    { grid-template-columns: 1fr; }
}
```

---

## Checklist for New HTML Report Skills

Before shipping any new skill HTML output, verify:

- [ ] CSS `:root` variables copied verbatim from this guide
- [ ] Google Fonts CDN link included (`Plus Jakarta Sans` + `IBM Plex Mono`)
- [ ] Chart.js CDN included
- [ ] Topbar shows 🔥 iMadeFire brand
- [ ] `radial-gradient` body background applied
- [ ] All cards use `var(--r)` border-radius and hover `border-color: var(--border-v)`
- [ ] Section titles use the `::before` gradient bar pattern
- [ ] Tables wrapped in `overflow: hidden` container
- [ ] Staggered `animation: up` on page load
- [ ] `author: Yury Primakov` in SKILL.md frontmatter
