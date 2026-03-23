# Auth0 — Design Reference
**Extracted via Playwright computed styles · March 2026**

---

## Site Overview

Auth0 (by Okta) is an identity and authentication platform. The current homepage (2025/2026) is a premium dark-mode-only marketing site with a stark, confident aesthetic: pure black backgrounds, warm off-white type, and a sophisticated purple/blue gradient accent system. The design is decisive — no light mode, no user-controlled theme switching.

**Stack:** React / styled-components (hashed class names: `sc-xxx`), custom font ("Aeonik"), video background hero, Okta CDN for assets.
**Theme:** Dark only — no toggle, single mode.
**Font strategy:** Custom "Aeonik" (geometric sans-serif) as primary, `fakt-web` as CSS var fallback.
**Background system:** Video (`background.mp4`) playing looped/muted as hero layer, cursor-following radial glow overlay in purple.

---

## Color Palette

### Backgrounds (surface scale: pure dark)
| Name | Value | Use |
|------|-------|-----|
| `bg-void` | `rgb(0, 0, 0)` / `#000000` | Body, page base |
| `bg-surface-1` | `rgb(17, 17, 17)` / `#111111` | Nav, sections, primary cards |
| `bg-surface-2` | `rgb(25, 25, 25)` / `#191919` | Secondary cards, nested surfaces |
| `bg-surface-3` | `rgb(36, 36, 36)` / `#242424` | Elevated elements, highlights |
| `bg-glass` | `rgba(23, 23, 23, 0.96)` | Nav dropdowns (with blur) |
| `bg-glass-light` | `rgba(23, 23, 23, 0.30)` | Lighter glass components |

### Text
| Name | Value | Use |
|------|-------|-----|
| `text-primary` | `rgb(255, 254, 250)` / `#FFFEFA` | Body text — warm off-white, not pure white |
| `text-white` | `rgb(255, 255, 255)` / `#FFFFFF` | Nav links, some headings |
| `text-muted-1` | `rgb(189, 196, 207)` / `#BDC4CF` | Secondary text |
| `text-muted-2` | `rgb(140, 146, 156)` / `#8C929C` | Tertiary / caption |
| `text-muted-3` | `rgb(171, 171, 171)` / `#ABABAB` | Inactive tabs, fine print |
| `text-link` | `rgb(10, 132, 174)` / `#0A84AE` | Hyperlinks, announcement bar |
| `text-dark` | `rgb(30, 33, 42)` / `#1E212A` | Text on light surfaces (e.g., h4 on white cards) |

### Brand Accents (gradient system — no single "brand orange")
| Name | Value | Use |
|------|-------|-----|
| `accent-purple` | `rgb(140, 103, 246)` / `#8C67F6` | Gradient start (stat numbers) |
| `accent-lavender` | `rgb(180, 155, 252)` / `#B49BFC` | Gradient / hero cursor glow |
| `accent-lavender-light` | `rgb(199, 179, 255)` / `#C7B3FF` | Gradient end |
| `accent-blue-deep` | `rgb(63, 89, 228)` / `#3F59E4` | Blue gradient start |
| `accent-blue-mid` | `rgb(66, 89, 191)` / `#4259BF` | Blue gradient mid |
| `accent-blue-light` | `rgb(182, 202, 255)` / `#B6CAFF` | Blue gradient end |
| `accent-teal` | `rgb(76, 183, 163)` / `#4CB7A3` | Blue→Teal gradient (10B+ stat) |
| `accent-teal-light` | `rgb(177, 228, 222)` / `#B1E4DE` | Teal gradient end |

### Borders
| Name | Value | Use |
|------|-------|-----|
| `border-default` | `rgb(42, 42, 42)` / `#2A2A2A` | Card/section borders |
| `border-white-12` | `rgba(255, 255, 255, 0.12)` | Card inset highlight (rim light) |
| `border-tag` | `rgb(244, 244, 244)` / `#F4F4F4` | Active tab/pill border |

---

## Typography

**Primary Font:** `Aeonik` — a geometric sans-serif (rounded terminals, clean construction similar to Circular). Loaded as a custom font; falls back to `sans-serif`. Note: this is a commercial font and not available on Google Fonts.
**Secondary Font:** `fakt-web` (CSS variable `--font-main`) — older/fallback reference in CSS vars.

### Type Scale
| Element | Size | Weight | Color | Notes |
|---------|------|--------|-------|-------|
| `h1` | 64px | 400 (light) | `rgb(255, 254, 250)` | Very large, regular weight — Aeonik's rounded geometry at display size |
| `h2` | 48px | 400 | `rgb(255, 254, 250)` | Section headings |
| `h3` | 48px | 400 | `rgb(255, 254, 250)` | Same scale as h2 |
| `h4` | 14px | 700 | `rgb(30, 33, 42)` | Small label weight, used on light cards |
| `p` | 14px | 500 | `rgb(255, 255, 255)` | Body copy |
| `a` | 14px | 400 | `rgb(10, 132, 174)` | Links |
| `button` | 14px | 400 | varies | CTA text |
| `label` | 16px | 500 | `rgb(255, 254, 250)` | Form labels |

### Gradient Text (distinctive feature)
Key stats and accent labels use `background-clip: text` with gradient fills:
- **Stats purple:** `linear-gradient(87deg, rgb(140, 103, 246) 0.92%, rgb(199, 179, 255) 82.42%)` — "3 billion+"
- **Stats blue:** `linear-gradient(76deg, rgb(182, 202, 255) 4.21%, rgb(66, 89, 191) 92.93%)` — "99.99%"
- **Stats blue-teal:** `linear-gradient(91deg, rgb(63, 89, 228) -15.54%, rgb(76, 183, 163) 52.43%, rgb(177, 228, 222) 98.25%)` — "10 billion+"
- **Label lavender:** `linear-gradient(88deg, rgb(180, 155, 252) 0.71%, rgb(182, 202, 255) 85.75%, rgb(246, 241, 231) 168.38%)` — "AI AGENTS"

---

## Spacing & Layout

- **Content width:** `120rem` (CSS var `--content-width`) — very wide, ~1920px max
- **Spacing unit:** 8px base (standard Aeonik/geometric system)
- **Button padding (large):** `12px 32px`
- **Button padding (medium):** `8px 24px`
- **Tag padding:** `14px 28px`

---

## Component Inventory

### Navigation
- **Position:** Fixed, `z-index: 1000`, full-width
- **Background:** Fully transparent (`rgba(0,0,0,0)`) — floats over the video hero
- **Height:** 106px
- **Structure:** Logo left, horizontal nav links center/right, CTA buttons right
- **Dropdowns:** Glass panels `rgba(23,23,23,0.96)` + `backdrop-filter: blur(14px)` + `border-radius: 10px`

### Primary Button ("Sign up", "Start building for free")
```
background-color: transparent
background-image:
  linear-gradient(0deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.4) 100%),
  radial-gradient(123.72% 71.29% at 7.15% 100%, rgb(255,255,255) 0%, rgba(255,255,255,0) 100%),
  radial-gradient(234.4% 144.94% at 84.62% 0%, rgb(255,255,255) 0%, rgba(255,255,255,0) 100%),
  linear-gradient(26deg, rgba(255,255,255,0.17) -32.04%, rgba(255,255,255,0) 133.43%)
box-shadow: rgba(255,255,255,0.48) 0px -16px 24px 0px inset, rgba(0,0,0,0.25) 0px 4px 4px 0px
border-radius: 6px
padding: 12px 32px
color: rgb(0, 0, 0)
font-size: 14px
```
Effect: Multi-layer white radial gradients on transparent base → glowing white glass button. Inset white glow at top gives 3D lit edge. Drop shadow below.

### Ghost Button ("Login", secondary "Sign up")
```
background-image: linear-gradient(26deg, rgba(255,255,255,0.15) -32.04%, rgba(255,255,255,0) 133.43%)
background-color: transparent
color: rgb(255, 254, 250)
border-radius: 6px
padding: 12px 32px
```
Effect: Barely-there white shimmer, white text — reads as outlined/ghost on dark bg.

### Tab/Pill Component (horizontal filter tabs)
- **Active tab:** `background: rgb(255,254,250)`, `color: rgb(25,25,25)`, `border-radius: 30px`, `padding: 14px 28px`, `border: 1px solid rgb(244,244,244)`
- **Inactive tab:** `background: transparent`, `color: rgb(174,174,174)`, `border-radius: 30px`, `padding: 14px 28px`

### Cards / Case Studies
```
border-radius: 24px
background: rgb(211, 211, 211)  // light gray on dark bg — customer logo/case study cards
box-shadow:
  rgba(255,255,255,0.12) -1px 0px 0px 0px inset,   // left rim highlight
  rgb(255,255,255) -2px -2px 2px 0px inset          // top-left corner highlight
```
Note: The complex multi-layer inset shadow creates a subtle "lit corner" effect.

### Glass / Dropdown Panels
```
background: rgba(23, 23, 23, 0.96)
backdrop-filter: blur(14px)
border-radius: 10px
```

### Cursor Glow Effect (hero)
An absolutely-positioned div tracks the cursor with a radial gradient that follows mouse position:
```
background: radial-gradient(160px at [mouseX] [mouseY], rgb(180,155,252), rgba(158,76,183,0.13), transparent)
position: absolute
z-index: 3
```
The `at [x] [y]` values update dynamically via JS on mousemove.

### Marquee / Logo Strip
Animated via keyframe `jOVXA`: `translateX(0) → translateX(-256rem)` — the logos translate left to create a seamless scroll. Content is duplicated for looping.

---

## Motion & Animation

| Name | Effect | Notes |
|------|--------|-------|
| `jBcSpD` | Fade in (`opacity: 0 → 1`) | Enter animations for sections |
| `jOVXA` | `translateX(0) → translateX(-256rem)` | Logo marquee scroll strip |
| `kbRkAL` | `scale(1) → scale(0.93)` | Button press / click shrink |
| `kPIRny` | `width: 0 → 100%` | Progress/underline expand — tab indicator or loading |
| `slide-down-custom` | `bottom: 0px` (from offscreen) | Cookie/consent banner entrance |
| `onetrust-fade-in` | `opacity: 0 → 1` | OneTrust banner fade |

---

## Interactive States

### Primary Button
- **Default:** Multi-layer white radial gradient + inset top glow
- **Press:** `scale(0.93)` via `kbRkAL` animation — satisfying physical click feel
- **Hover:** Likely slight brightness increase (not captured via Playwright hover state without explicit trigger)

### Tab / Filter Pill
- **Active:** White bg pill `rgb(255,254,250)`, dark text
- **Inactive:** Transparent, muted gray text `rgb(174,174,174)`
- **Hover:** Subtle transition to active-like state (transition not captured)

### Nav Links
- **Default:** `rgb(255,255,255)` / `rgb(255,254,250)`
- **Hover:** Dropdown opens for expandable items; color shift inferred

---

## Design Personality

1. **No-compromise dark** — There is no light mode. The page is built entirely for black. This sends a signal: Auth0 is for developers, and developers trust dark UIs.

2. **Warmth in the whites** — Body text is `rgb(255,254,250)` not `rgb(255,255,255)`. This 1-unit-of-warm tint feels intentional — it softens the pure black/white contrast slightly.

3. **Gradient text as the only color** — The entire page is monochromatic until you hit the stat numbers and "AI Agents" label. That's where lavender, blue, and teal live — making them extremely high-impact.

4. **Buttons that feel physical** — The primary button's multi-layer radial gradient + inset top glow simulates a raised, lit surface. The `scale(0.93)` press animation makes it feel tactile.

5. **Video atmosphere** — The hero background is an MP4 video (looped/muted), not a static gradient or SVG. This is a deliberate choice to create cinematic motion without animations that could be laggy.

6. **Cursor awareness** — The hero section tracks mouse position and renders a 160px purple radial glow following the cursor. This is subtle but makes the hero feel alive.

7. **Aeonik at display weight** — Using `font-weight: 400` for 64px headings is bold for a geometric sans. Aeonik's geometry at this scale and weight reads as authoritative without being heavy.
