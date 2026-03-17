# Design Reference — yuryprimakov.com

**Extracted:** 2026-03-17
**Target:** Personal portfolio of Yury Primakov (Principal Full Stack Engineer)

---

## Site Overview

A Next.js 13+ App Router portfolio with a clean, professional aesthetic built on Tailwind CSS v3.4.13 and the shadcn/ui component system. The design is intentionally neutral — no custom brand color, leaning on a slate-family monochrome palette with colorful gradients reserved for accent elements (skill badges, section highlights). Supports light and dark mode via localStorage with system preference fallback.

**Overall aesthetic:** Modern, technical, minimal. System fonts reinforce a developer-native feel. Colorful gradient accents (blue → cyan → purple → pink ranges) add visual energy without committing to a single brand color.

---

## Color Palette

### Design Token System (shadcn/ui default → Tailwind Slate)

All colors are CSS custom properties at `:root` and `.dark`, expressed in HSL channel values (used as `hsl(var(--token))`).

#### Light Mode

| Token | HSL | Hex | Tailwind Equivalent | Role |
|---|---|---|---|---|
| `--background` | 0 0% 100% | `#ffffff` | white | Page background |
| `--foreground` | 222.2 84% 4.9% | `#020817` | slate-950 | Primary text |
| `--primary` | 222.2 47.4% 11.2% | `#0f172a` | slate-900 | Primary interactive |
| `--primary-foreground` | 210 40% 98% | `#f8fafc` | slate-50 | Text on primary |
| `--secondary` | 210 40% 96.1% | `#f1f5f9` | slate-100 | Secondary backgrounds |
| `--secondary-foreground` | 222.2 47.4% 11.2% | `#0f172a` | slate-900 | Text on secondary |
| `--muted` | 210 40% 96.1% | `#f1f5f9` | slate-100 | Muted backgrounds |
| `--muted-foreground` | 215.4 16.3% 46.9% | `#64748b` | slate-500 | Muted/secondary text |
| `--accent` | 210 40% 96.1% | `#f1f5f9` | slate-100 | Accent backgrounds |
| `--accent-foreground` | 222.2 47.4% 11.2% | `#0f172a` | slate-900 | Text on accent |
| `--border` | 214.3 31.8% 91.4% | `#e2e8f0` | slate-200 | Borders, dividers |
| `--input` | 214.3 31.8% 91.4% | `#e2e8f0` | slate-200 | Input borders |
| `--ring` | 222.2 84% 4.9% | `#020817` | slate-950 | Focus rings |
| `--destructive` | 0 84.2% 60.2% | `#ef4444` | red-500 | Error/destructive |

#### Dark Mode

| Token | HSL | Hex | Tailwind Equivalent | Role |
|---|---|---|---|---|
| `--background` | 222.2 84% 4.9% | `#020817` | slate-950 | Page background |
| `--foreground` | 210 40% 98% | `#f8fafc` | slate-50 | Primary text |
| `--primary` | 210 40% 98% | `#f8fafc` | slate-50 | Primary interactive |
| `--primary-foreground` | 222.2 47.4% 11.2% | `#0f172a` | slate-900 | Text on primary |
| `--secondary` | 217.2 32.6% 17.5% | `#1e293b` | slate-800 | Secondary backgrounds |
| `--secondary-foreground` | 210 40% 98% | `#f8fafc` | slate-50 | Text on secondary |
| `--muted` | 217.2 32.6% 17.5% | `#1e293b` | slate-800 | Muted backgrounds |
| `--muted-foreground` | 215 20.2% 65.1% | `#94a3b8` | slate-400 | Muted/secondary text |
| `--accent` | 217.2 32.6% 17.5% | `#1e293b` | slate-800 | Accent backgrounds |
| `--accent-foreground` | 210 40% 98% | `#f8fafc` | slate-50 | Text on accent |
| `--border` | 217.2 32.6% 17.5% | `#1e293b` | slate-800 | Borders, dividers |
| `--input` | 217.2 32.6% 17.5% | `#1e293b` | slate-800 | Input borders |
| `--ring` | 212.7 26.8% 83.9% | `#cbd5e1` | slate-300 | Focus rings |
| `--destructive` | 0 62.8% 30.6% | `#7f1d1d` | red-900 | Error/destructive dark |

### Gradient Accent Colors

The stylesheet includes a rich set of gradient utilities suggesting colorful accent elements (skill badges, tags, section decorations):

**Cool/Tech gradients:** `from-blue-500 (#3b82f6)` → `via-cyan-500 (#06b6d4)` → `to-teal-500 (#14b8a6)`
**Creative gradients:** `from-purple-500 (#a855f7)` → `via-pink-500 (#ec4899)` → `to-red-500 (#ef4444)`
**Warm gradients:** `from-orange-400 (#fb923c)` → `via-yellow-400 (#facc15)` → `to-lime-400 (#a3e635)`
**Sky gradients:** `from-sky-400 (#38bdf8)` → `via-blue-500 (#3b82f6)` → `to-indigo-500/600`

---

## Typography System

### Font Stack

No custom web fonts (no Google Fonts detected). The site uses the native system font stack:

```
system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji'
```

This renders as:
- **Windows:** Segoe UI
- **macOS:** San Francisco (SF Pro)
- **Android:** Roboto
- **Linux:** Ubuntu / Noto Sans

### Type Scale (Tailwind defaults)

| Class | Size | Line Height | Use |
|---|---|---|---|
| `text-xs` | 0.75rem (12px) | 1rem | Labels, captions |
| `text-sm` | 0.875rem (14px) | 1.25rem | Secondary text, metadata |
| `text-base` | 1rem (16px) | 1.5rem | Body text |
| `text-lg` | 1.125rem (18px) | 1.75rem | Subheadings, lead text |
| `text-xl` | 1.25rem (20px) | 1.75rem | Section subheadings |
| `text-2xl` | 1.5rem (24px) | 2rem | Section headings |
| `text-3xl` | 1.875rem (30px) | 2.25rem | Page section titles |
| `text-4xl` | 2.25rem (36px) | 2.5rem | Hero heading |
| `text-6xl` | 3.75rem (60px) | 1 | Display / large hero |

### Font Weights

| Class | Weight | Use |
|---|---|---|
| `font-light` | 300 | Light decorative text |
| `font-normal` | 400 | Body text |
| `font-medium` | 500 | Labels, nav items |
| `font-semibold` | 600 | Card titles, section headings |
| `font-bold` | 700 | Primary headings, CTAs |
| `font-black` | 900 | Display headings (if used) |

---

## Spacing & Layout System

### Base Unit

Tailwind default 4px base (1 unit = 0.25rem).

### Common Spacing Values

| Class | Value | Pixels |
|---|---|---|
| `p-1` / `m-1` | 0.25rem | 4px |
| `p-2` / `m-2` | 0.5rem | 8px |
| `p-3` / `m-3` | 0.75rem | 12px |
| `p-4` / `m-4` | 1rem | 16px |
| `p-6` / `m-6` | 1.5rem | 24px |
| `p-8` / `m-8` | 2rem | 32px |
| `p-12` / `m-12` | 3rem | 48px |
| `p-20` / `m-20` | 5rem | 80px |
| `p-24` / `m-24` | 6rem | 96px |

### Responsive Breakpoints

| Prefix | Breakpoint | Notes |
|---|---|---|
| (none) | 0px | Mobile-first base |
| `xs:` | 475px | Small phones |
| `sm:` | 640px | Large phones |
| `md:` | 768px | Tablets |
| `lg:` | 1024px | Desktops |
| `xl:` | 1280px | Large desktops |
| `2xl:` | 1536px | Wide screens |

---

## Border & Shape System

### Border Radius

| Token | Value | Notes |
|---|---|---|
| `--radius` | 0.5rem (8px) | Base radius |
| `rounded-sm` | `calc(var(--radius) - 4px)` = 4px | Small elements |
| `rounded-md` | `calc(var(--radius) - 2px)` = 6px | Medium elements |
| `rounded-lg` | `var(--radius)` = 8px | Cards, panels |
| `rounded-xl` | 0.75rem (12px) | Larger cards |
| `rounded-2xl` | 1rem (16px) | Feature cards |
| `rounded-full` | 9999px | Pills, avatars |

### Shadow Scale

| Class | Value |
|---|---|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` |
| `shadow` | `0 1px 3px rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)` |
| `shadow-md` | `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)` |
| `shadow-lg` | `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)` |
| `shadow-xl` | `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)` |
| `shadow-2xl` | `0 25px 50px -12px rgba(0,0,0,0.25)` |

---

## Motion & Animation

### Custom Animations

| Name | Effect | Timing |
|---|---|---|
| `animate-scroll` | `translateX(0) → translateX(-100%)` | 20s linear infinite |

**Used for:** Horizontal skills/tech marquee — a continuous scrolling strip of skill badges.

### Spotlight / Mouse-Follow Glow Effect

> Full implementation brief: see [`SPOTLIGHT_EFFECT.md`](./SPOTLIGHT_EFFECT.md)

The signature interactive effect: every card has a glowing orb that follows the mouse cursor. It is **JavaScript-driven**, not CSS-only. Three layers work together:

1. **`useMousePosition` hook** — global `window.mousemove` listener stores `clientX`/`clientY` in state
2. **`<Spotlight>` container** — throttled `useEffect` (~100ms) calls `getBoundingClientRect()` per card, writes `--mouse-x` / `--mouse-y` as CSS custom properties onto each card element
3. **`<SpotlightCard>`** — two large blurred circles (`::before` / `::after`) that `translate()` to the cursor position and blur into a soft diffused glow

#### Component hierarchy
```
<Spotlight>                          ← sets --mouse-x/--mouse-y per card
  <SpotlightCard>                    ← ::before (white orb) + ::after (violet orb)
    <div z-20>                       ← actual card content, semi-transparent + backdrop-blur
      {children}
    </div>
  </SpotlightCard>
</Spotlight>
```

#### Key numbers

| Property | Value |
|---|---|
| `::before` orb size | 320×320px |
| `::after` orb size | 384×384px |
| `::before` offset | `left: -160px; top: -160px` |
| `::after` offset | `left: -192px; top: -192px` |
| Blur radius | `100px` on both |
| `::before` color | `rgba(248, 250, 252, 1)` — white/slate |
| `::after` color (dark) | `rgb(139, 92, 246)` — violet-500 |
| `::after` color (light) | `rgb(237, 233, 254)` — violet-100 |
| `::before` opacity | 20% always-on |
| `::after` opacity | 20% light / 10% dark |
| Opacity transition | 500ms |
| Mouse update throttle | 100ms |
| Outer wrapper padding | `1px` — glow bleeds through as a rim light on the card edge |

#### The detail that makes it feel special

The `1px` padding on the outer `<Spotlight>` wrapper creates a hairline gap between wrapper and card. The glow orbs sit in that gap, making a faint colored rim light appear on the card edge nearest the cursor — the detail most viewers feel but can't identify.

#### Source files (in this project)
- `src/components/Spotlight.tsx` — `Spotlight` wrapper + `SpotlightCard`
- `src/components/common/Card.tsx` — wraps `SpotlightCard` with hover/scale/active state
- `src/lib/utils/useMousePosition.ts` — global mouse position hook

### Standard Tailwind Animations

| Name | Effect |
|---|---|
| `animate-bounce` | Vertical bounce (translateY -25%) |
| `animate-pulse` | Opacity fade to 0.5 |
| `animate-spin` | Full rotation (360°) |

### Transition System

**Default easing functions:**
- `ease-in`: `cubic-bezier(0.4, 0, 1, 1)` — accelerating
- `ease-out`: `cubic-bezier(0, 0, 0.2, 1)` — decelerating (most natural for UI)
- `ease-in-out`: `cubic-bezier(0.4, 0, 0.2, 1)` — standard interactive

**Common durations:** 100ms, 150ms, 200ms, 300ms, 500ms

### Backdrop Blur

Available for frosted-glass effects (likely nav bar on scroll):
- `backdrop-blur-sm`: blur(4px)
- `backdrop-blur-md`: blur(12px)
- `backdrop-blur-xl`: blur(24px)

---

## Component Inventory

### Navigation
- Fixed/sticky header (implied by portfolio conventions)
- Nav items: About, Skills, Portfolio, Login
- Likely uses `backdrop-blur` + semi-transparent background on scroll
- Light/dark theme toggle
- System font, `font-medium` weight for nav links

### Hero Section
- Profile image (256×256px, circular via `rounded-full`)
- Title: "Principal Full Stack Engineer"
- Subtitle/focus: "AI Automations using Personalized Autonomous Agent Swarms"
- Location text: Holmdel, NJ
- Resume link (Google Drive) — primary CTA button
- Social links: GitHub, CodePen, LinkedIn, Contact form

### Skills Marquee
- Horizontal scrolling strip using `animate-scroll` (20s linear infinite)
- Likely contains colorful gradient skill badges
- Overflow hidden container with duplicated content for seamless loop

### Experience Timeline
- 5 positions from 2003–2025
- Card-based or timeline layout
- Likely uses `shadow-md` or `shadow-lg` for card elevation
- `rounded-lg` (8px) borders

### Interests Section
- Grid of interest categories (9 items)
- Icons + labels pattern
- Skiing, Tennis, Volleyball, Cars, AI, Investing, Music, Gaming, Photography

### Theme System
- Toggle: light / dark / system
- Persisted in localStorage key `'theme'`
- System preference: `window.matchMedia('(prefers-color-scheme: dark)')`
- Applied via `.dark` class on `<html>` element

---

## Interactive States

### Links & Nav Items
- **Default:** `text-foreground` or `text-muted-foreground`
- **Hover:** color shift toward `text-primary`, likely `transition-colors duration-200`
- **Focus:** `ring` outline using `--ring` token

### Buttons (Primary)
- **Default:** `bg-primary text-primary-foreground`
- **Hover:** lighter shade or opacity change, `transition-colors`
- **Active:** slight scale-down transform
- **Focus:** ring outline

### Buttons (Secondary/Ghost)
- **Default:** `bg-secondary` or transparent
- **Hover:** `bg-muted` or `bg-accent`

---

## Design Personality

**Technical minimalism:** The choice of system fonts and a slate monochrome palette signals "built by a developer for developers" — no decorative typefaces, no brand mascot, no heavy imagery.

**Restrained with purposeful pops:** The base palette is nearly grayscale (slate family), but the gradient utilities confirm colorful accent moments — likely gradient skill badge pills that make the skills section visually dynamic while keeping the overall layout quiet.

**Smooth and modern:** shadcn/ui components bring consistent radius (8px), clean shadows, and reliable interactive states without custom styling overhead.

**Dual-mode first:** The theme system is deeply integrated (localStorage + system pref), suggesting dark mode isn't an afterthought — the dark palette (#020817 background with slate-50 text) is a first-class design state.

**Subtle motion:** The skills marquee is the only structural animation; other motion is limited to hover transitions (150–200ms). This keeps the portfolio feeling polished rather than distracting.
