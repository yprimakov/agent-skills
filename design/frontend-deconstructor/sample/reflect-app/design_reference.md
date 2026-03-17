# Reflect.app — Design Reference

**Source:** https://reflect.app/
**Extracted:** 2026-03-16
**Method:** Static HTML/CSS analysis via WebFetch

---

## Site Overview

Reflect is a networked note-taking app with AI integration. The design is a premium, dark-only experience with a deep purple-black base (`#030014`) and a pervasive use of translucent glass-morphism layers, glowing purple/violet accents, and motion-rich animations (rising stars, rotating radars, hue-rotating gradients). The overall aesthetic is "dark space / AI-forward luxury SaaS" — polished, opinionated, and high-contrast without being harsh.

No light mode is present. The palette is monochromatic dark purple with colored-light accent gradients.

---

## Color Palette

### Background Colors
| Role | Value | Notes |
|------|-------|-------|
| Page background | `#030014` | Deep purple-black, used on `body` |
| Header background | `rgba(3, 0, 20, 0.08)` | Frosted glass over page bg |
| Nav pill background | `rgba(255, 255, 255, 0.02)` | Barely-visible white tint |
| Card overlay (hover) | `rgba(255, 255, 255, 0.06)` | Subtle lift on hover |
| AI showcase hover | `rgba(255, 255, 255, 0.05)` | Card hover state |
| Connected card 1 | `radial-gradient(100% 146.88% at 100% 100%, rgba(255,255,255,.03) 0%, rgba(3,0,20,0) 100%)` | Radial corner glow |
| Hero radial overlay | `radial-gradient(37.74% 81.78% at 50% 26.56%, rgba(148,101,255,0.08) 0%, rgba(3,0,20,0) 100%)` | Purple radial behind hero |
| Button primary bg | `rgba(113, 47, 255, 0.12)` + gradient overlay | Glass violet |
| Button primary hover bg | `rgba(113, 47, 255, 0.24)` + gradient overlay | Brighter on hover |
| Button secondary bg | `rgba(147, 130, 255, 0.01)` + gradient overlay | Near-invisible glass |

### Text Colors
| Role | Value | Notes |
|------|-------|-------|
| Primary text | `#ffffff` / `#fff` | Body default |
| Nav links | `#ffffffe6` (~90% white) | Default nav link color |
| Nav links hover | `#ffffff99` (~60% white, `#fff9`) | Dimmed on hover |
| Body / description text | `#efedfdb3` (~70% warm white) | Section descriptions |
| Secondary description | `#efedfd99` (~60% warm white) | Dimmer body copy |
| Near-white | `#fffc` (~80% white) | Various UI labels |
| Faded white variants | `#ffffff70`, `#ffffff52` | Metadata, captions |

### Accent / Brand Colors
| Role | Value | Notes |
|------|-------|-------|
| Purple accent primary | `#ba9cff` | Badge/gradient mid |
| Purple accent light | `#e59cff` | Badge/gradient start |
| Blue-purple accent | `#9cb2ff` | Badge/gradient end |
| Deep violet (CTA) | `#5046e4` | Button fill (alt) |
| Starlight/shimmer | `#c9b1ff` | Animated starlight color |
| Swiper default | `#007aff` | Third-party swiper only |

### Gradient Accents
| Role | Gradient |
|------|---------|
| Badge text gradient | `linear-gradient(90.01deg, #e59cff 0.01%, #ba9cff 50.01%, #9cb2ff 100%)` blended with `rgba(255,255,255,0.4)` in screen mode |
| AI rainbow text gradient | `linear-gradient(to right, #FC72FF, #8F68FF, #487BFF, #2CD9FF, #2CFFCC)` |

### Border / Divider Colors
| Role | Value |
|------|-------|
| Nav pill border | `rgba(255, 255, 255, 0.08)` |
| AI showcase border (hover) | `rgba(255, 255, 255, 0.161)` (`#ffffff29`) |

### Shadow Colors
| Role | Value |
|------|-------|
| Button primary inset | `inset 0 0 12px #bf97ff3d` (default), `inset 0 0 12px #bf97ff70` (hover) |
| Button secondary inset | `inset 0 0 12px #ffffff14` |
| Hero badge inset | `inset 0 -7px 11px #a48fff1f` (default), `inset 0 -7px 11px #a48fff3d` (hover) |
| Section badge inset | `inset 0 -7px 11px #a48fff1f` |
| Deep shadow | `32px 36px 32px #03001480` |
| Glow outer | `0 0 6px 4px #ed78ff0a` |

---

## Typography System

### Font Families
| Family | Usage | Weights Available | Source |
|--------|-------|-------------------|--------|
| `AeonikPro` | Headings (H1 / hero titles) | 500 (medium) | Self-hosted `/home/fonts/AeonikPro/medium.woff2` |
| `Inter V` | Body, UI, all other text | 400 (regular), 500 (medium) | Self-hosted `/home/fonts/InterV/regular.woff2`, `medium.woff2` |

Both fonts use `font-display: swap` and fall back to: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif`.

### Font Feature Settings
Applied globally to UI text (buttons, nav, cards):
```
font-feature-settings: "ss01" on, "cv10" on, "calt" off, "liga" off
```
Headings (`.section-header-title-h1`) use `font-feature-settings: unset`.

### Type Scale
| Role | Font | Size | Line Height | Weight |
|------|------|------|-------------|--------|
| H1 / Hero title | AeonikPro | 72px | 80px | 500 |
| H2 / Section title | Inter V | 56px | 64px | 500 |
| H3 / Sub-section title | Inter V | 48px | 56px | 500 |
| H5 / Card title large | Inter V | 32px | 40px | 500 |
| Hero description | Inter V | 18px | 28px | 400 |
| Section description | Inter V | 16px | 24px | 400 |
| Card description | Inter V | 16px | 24px | 400 |
| Card title small | Inter V | 16px | 24px | 500 |
| AI showcase label | Inter V | 15px | 24px | 500 |
| Nav links / Buttons | Inter V | 14px | 20px | 500 |
| Meeting/meta details | Inter V | 13px | 20px | 500 |
| Logo | Inter V | 16px | 24px | 500 |

### Responsive Typography (max-width: 1248px)
| Element | Mobile Size | Mobile Line Height |
|---------|------------|-------------------|
| H1 | 44px | 52px |
| H2 | 40px | 48px |
| H3 | 36px | 40px |

### Letter Spacing
No explicit `letter-spacing` values found in extracted CSS. Likely relies on font's built-in metrics.

---

## Spacing & Layout System

### Container Widths
| Class | Max Width |
|-------|-----------|
| `.container-lg` | 1296px |
| `.container` | 1248px |
| `.container-md` | 1200px |
| `.container-sm` | 1128px |

### Section Padding
| Section | Padding |
|---------|---------|
| `.hero` | `padding-top: 173px` (desktop), `108px` (mobile) |
| `.connected` | `padding-top: 496px`, `padding-bottom: 145px` |
| `.ai` | `padding-top: 116px`, `padding-bottom: 110px` |
| `.research` | `padding-top: 64px`, `padding-bottom: 128px` |
| `.encryption` | `padding: 222px 0 236px` (desktop), `134px top / 46px bottom` (mobile) |
| `.meetings` | `padding: 294px 0 24px` |
| `.header` | `padding: 26px 0` (vertical), `padding: 0 20px` (horizontal) |

### Component Spacing
| Component | Spacing |
|-----------|---------|
| `.features-card` | `padding: 24px 32px 36px` |
| `.research-card` | `padding: 32px 32px 48px` |
| `.hero-badge` | `padding: 4px 13px 4px 8px` |
| `.section-header-badge` | `padding: 6px 14px 6px 15px` |
| `.button` | `padding: 8px 16px` |
| `.header-nav` | `padding: 10px 12px` |
| `.header-nav li` | `margin: 0 12px` |
| `.section-header-description` | `margin: 12px auto 0`, `max-width: 455px` |
| `.features` | `margin: -78px auto 0` (negative top margin pulls into hero) |
| `.research` | `width: 890px` (fixed) |

### Grid Systems
| Component | Layout |
|-----------|--------|
| Features cards | `grid-template-columns: repeat(4, 1fr)` |
| Connected cards | `grid-template-columns: repeat(2, 1fr)` |
| Research cards | `grid-template-columns: repeat(2, 1fr)` |
| AI cards | `display: flex; flex-wrap: wrap; justify-content: center` |

### Base Spacing Unit
Inferred 4px base unit: values are consistently multiples of 4 (4, 8, 12, 16, 20, 24, 32, 36, 40, 48, 64, 80, 110, 116, 128, 145, 173, 222, 236, 294, 496).

### Breakpoints
| Breakpoint | px Value |
|------------|----------|
| Mobile | max-width: 390px |
| Tablet/Desktop transition | max-width: 1248px |
| Desktop minimum | min-width: 1248px |

---

## Border Tokens

### Border Radius
| Usage | Value |
|-------|-------|
| Large components / sections | `24px` |
| Buttons, cards | `8px` |
| Badges (hero, section) | `32px` |
| Nav pill | `999px` (fully round) |
| Small UI elements | `6px`, `4px` |

### Border Widths
| Usage | Value |
|-------|-------|
| Nav pill border | `1px solid rgba(255, 255, 255, 0.08)` |
| AI showcase border | `1px` (color changes on hover to `#ffffff29`) |

---

## Component Inventory

### Navigation (Header)
- Fixed position, full viewport width, `z-index: 10`
- Frosted glass background: `backdrop-filter: blur(16px)`, `background: rgba(3,0,20,0.08)`
- Center-aligned pill nav with `border-radius: 999px`
- Nav links: 14px/500 weight, `#ffffffe6` default, `#fff9` on hover
- Right side: "Login" (secondary button) + "Start free trial" (primary button)

### Buttons
| Variant | Background | Box Shadow | Hover Change |
|---------|-----------|------------|--------------|
| Primary | `rgba(113,47,255,0.12)` + dark gradient | `inset 0 0 12px #bf97ff3d` | Shadow → `#bf97ff70`, bg opacity doubles |
| Secondary | `rgba(147,130,255,0.01)` + subtle gradient | `inset 0 0 12px #ffffff14` | Slight bg opacity increase |

Both buttons:
- `backdrop-filter: blur(8px)`
- `border-radius: 8px`
- `font-size: 14px / line-height: 20px / font-weight: 500`
- `color: #f4f0ff`
- Hover uses pseudo-element opacity crossfade (`:before` fades out, `:after` fades in) with `transition: 0.2s opacity cubic-bezier(0.6, 0.6, 0, 1)`

### Hero Section
- `padding-top: 173px`
- Radial gradient overlay behind hero content
- Badge pill above headline with purple gradient text
- H1: AeonikPro 72px/80px
- Description: Inter V 18px/28px, `#efedfdb3`
- Primary CTA: "Start free trial" → `/sign-up`

### Badges (Hero & Section)
- `border-radius: 32px`
- `backdrop-filter: blur(6px)`
- `box-shadow: inset 0 -7px 11px #a48fff1f` (glow underneath)
- Gradient text: `#e59cff → #ba9cff → #9cb2ff`

### Feature Cards (4-column grid)
- `padding: 24px 32px 36px`
- `overflow: hidden`
- Hover: gradient overlay (`rgba(255,255,255,0.06)`) fades in via pseudo-element
- Transition: `0.45s cubic-bezier(0.6, 0.6, 0, 1) opacity`

### Connected Cards (2-column grid)
- Card 1 has a radial corner glow background
- Showcases backlinks, networked notes concept

### Research Cards (2-column grid)
- `padding: 32px 32px 48px`
- Fixed-width container: 890px

### AI Showcase Items
- Hover: background → `rgba(255,255,255,0.05)`, border-color → `#ffffff29`
- Rainbow gradient text: `linear-gradient(to right, #FC72FF, #8F68FF, #487BFF, #2CD9FF, #2CFFCC)`

### Section Headers
- Centered layout with badge + title + description pattern
- Description max-width: 455px
- `margin: 12px auto 0` for description

---

## Motion & Animation

### Primary Easing
```
cubic-bezier(0.6, 0.6, 0, 1)
```
Used consistently across transitions. This is a deceleration curve — fast start, smooth stop (similar to `ease-out` but more pronounced).

### Transition Durations
| Duration | Usage |
|----------|-------|
| `0.2s` | Button pseudo-element opacity crossfade |
| `0.3s` | Nav link color change |
| `0.45s` | Card overlay, badge box-shadow |
| `1s` | Looping linear animations |
| `2s` | Hue rotation loop |

### Keyframe Animations
| Name | Effect | Timing |
|------|--------|--------|
| `heroBlackHoleStarsRotate` | Rotating star field behind hero | 70s linear infinite |
| `heroBlackHoleStarsTwinkle` | Star opacity pulse | linear infinite |
| `risingStarsAnimation` | Stars float upward: `translateY(0) → translateY(-2000px)` | linear infinite |
| `hue-rotate` | `filter: hue-rotate(0deg → 360deg)` on accent elements | 2s infinite linear |
| `researchRadarRotate` | Radar arm rotates: `-201deg → 159deg` | looping |
| `researchRadarItem` | Radar blips appear: `scale(0) → scale(1.2)` with opacity | staggered |
| `aiShowcaseText` | Text reveal animation | 4s 1 linear forwards |
| `aiShowcaseStarlight1` | Shimmer moves: `translate(-100%) → translate(100%)` | looping |
| `connected-card-backlink-circle` | Circle appears: `opacity 0→1, scale 0→1` | on scroll trigger |
| `swiper-preloader-spin` | Loading spinner rotation | standard |

### Backdrop Blur Layers
| Usage | Blur |
|-------|------|
| Header | `blur(16px)` |
| Badges | `blur(6px)` |
| Buttons | `blur(8px)` |
| Cards (some) | `blur(12px)` |

### Interactive State Summary
| Element | Default | Hover | Focus | Active |
|---------|---------|-------|-------|--------|
| Nav link | `#ffffffe6` | `#fff9` (dimmed) | Not specified | Not specified |
| Button primary | `rgba(113,47,255,0.12)` bg, shadow `#bf97ff3d` | Shadow doubles to `#bf97ff70`, bg doubles opacity | Not specified | Not specified |
| Button secondary | `rgba(147,130,255,0.01)` bg | Slight bg opacity increase | Not specified | Not specified |
| Hero badge | `shadow: inset 0 -7px 11px #a48fff1f` | `inset 0 -7px 11px #a48fff3d` | — | — |
| Feature card | No overlay | Overlay gradient fades in (0.06 opacity) | — | — |
| AI showcase item | Transparent bg, faint border | `rgba(255,255,255,0.05)` bg, `#ffffff29` border | — | — |

---

## Design Personality Notes

1. **Dark-only, no theme toggle.** The experience is entirely designed for dark mode. `#030014` is not black — it's a deep navy-purple that gives the entire interface a warm space-like quality.

2. **Glass-morphism as the primary layering mechanism.** Every interactive container (nav, buttons, badges, cards) uses `backdrop-filter: blur()` + semi-transparent background + inset box shadows to create depth without traditional drop shadows.

3. **Animation is a core feature, not decoration.** The hero has a live animated star field rotating over 70 seconds. Sections have radar sweeps, rising stars, and shimmer effects. Animation is used to communicate the AI/intelligence theme.

4. **The type system is binary.** AeonikPro for hero headlines only; Inter V for everything else. This creates a clear hierarchy without needing many size levels.

5. **Purple is the only brand hue.** The palette goes from violet (`#5046e4`, `#7132FF`) through lavender (`#ba9cff`, `#9cb2ff`) to near-white. The rainbow gradient on AI elements (`#FC72FF → #2CFFCC`) is the only multicolor departure.

6. **Spacing uses large, confident values.** Section padding in the hundreds of pixels (`496px`, `294px`, `222px`) creates generous breathing room and makes scrolling feel like moving through space.

7. **The easing function `cubic-bezier(0.6, 0.6, 0, 1)` is a design signature.** Used on nearly all transitions, it creates a snappy-but-smooth motion feel that feels custom rather than generic.
