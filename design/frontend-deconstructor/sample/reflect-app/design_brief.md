# Reflect.app — Design Brief

**Source:** https://reflect.app/
**Extracted:** 2026-03-16
**Brief Type:** Reverse-engineered design brief

---

## Product Overview

Reflect is a networked note-taking and personal knowledge management app with deep AI integration. The product positions itself at the intersection of intelligence, privacy, and craft — appealing to knowledge workers, writers, and researchers who find consumer note apps too shallow and enterprise tools too clinical.

---

## Design Vision

> "Dark space. Living intelligence. Premium stillness."

The design communicates that using Reflect is not just productive — it's an experience. The interface feels like a command center built inside a nebula: deep, glowing, animated with restraint. The AI capabilities are not an afterthought — they're woven into the visual language via a distinct rainbow gradient that appears only when AI is the subject.

This is not a neutral tool. It has a point of view.

---

## Target Audience

- Knowledge workers and researchers who consume and synthesize large volumes of information
- Writers and thinkers who care about the quality of their tools
- Tech-forward users comfortable with AI-assisted workflows
- Users who have outgrown linear note-taking (Notion, Evernote, Apple Notes)

**Design implication:** The interface can be sophisticated and dense with information. Users are not intimidated by complex systems — they're attracted to tools that feel intelligent.

---

## Aesthetic Direction

### Mood
Dark, premium, alive. Not sterile-dark (like dev tools or terminals) — warm-dark. The base color `#030014` is a deep navy-purple, not black. Everything floats above it in translucent layers.

### Metaphors Driving the Design
1. **Space / Observatory** — Deep dark background, glowing stars, rotating fields, radar sweeps. The product helps you navigate a universe of knowledge.
2. **Glass & Light** — Every interactive element is translucent. Depth is created through layers of frosted glass, not opaque boxes.
3. **Intelligence as Glow** — AI features glow with a rainbow aurora. Regular features glow violet. The color encodes meaning.

### Personality Words
Precise · Alive · Deep · Sophisticated · Unapologetic · Premium · Spacious

---

## Color Strategy

### The Palette Is Intentionally Narrow
Reflect uses a single base hue (deep purple-black) with a single accent family (violet → lavender). This restraint makes the UI feel cohesive and intentional, not colorful. The rainbow gradient reserved for AI is more impactful *because* everything else is monochromatic.

### Color Roles
| Role | Color | Rationale |
|------|-------|-----------|
| Ground | `#030014` | Warm darkness — purple-black, not pure black |
| Interactive accent | `#7132FF` → `#ba9cff` | Violet-to-lavender range signals interactivity |
| AI / Intelligence | `#FC72FF → #2CFFCC` rainbow | Exclusively marks AI features — reserved, never overused |
| Text hierarchy | White at varying opacity | 4 levels: 90%, 70%, 60%, 52% opacity white |
| Depth layers | White at 2–12% opacity | Glassmorphism layers stacked on `#030014` |

### What to Avoid
- Pure black (`#000000`) — too harsh, kills the warmth
- Any saturated colors outside the violet family — breaks brand coherence
- Light mode — this design is architected for dark only

---

## Typography Strategy

### The Binary Type System
Reflect uses exactly two fonts in exactly one weight each for primary UI:

| Font | Weight | Role | Why |
|------|--------|------|-----|
| **AeonikPro** | 500 (Medium) | Hero headline only | Geometric, editorial — signals premium software |
| **Inter V** | 400 / 500 | Everything else | Neutral, legible, modern — disappears into content |

This binary system creates clear hierarchy without complexity. AeonikPro is used *sparingly* — only at 72px in the hero. Its restraint makes it powerful.

### Type Scale Principles
- The scale runs from 13px (metadata) to 72px (hero)
- Only two weights: regular (400) for body/description, medium (500) for headings/UI
- No letter-spacing tweaks — fonts are used with natural metrics
- Font features: `"ss01" on, "cv10" on, "calt" off, "liga" off` applied to all UI elements (enables stylistic alternates and character variants, disables contextual alternates and ligatures for cleaner UI rendering)

### Type Hierarchy in Practice
1. Hero title (AeonikPro 72px) — one per page
2. Section titles (Inter V 56px) — once per section
3. Sub-section (Inter V 48px) — secondary section headers
4. Card titles large (Inter V 32px) — key callouts
5. Body / Description (Inter V 16–18px) — all explanatory copy
6. UI labels (Inter V 14px) — buttons, nav, captions

---

## Spacing & Layout Strategy

### Generous Is the Point
Sections use padding in the hundreds of pixels (`496px`, `294px`, `222px`). This is deliberate — the spaciousness communicates premium quality and makes scrolling feel like moving through space, not scrolling through content.

### 4px Grid
All spacing values are multiples of 4px. Component-level padding follows tighter multiples (8, 16, 24, 32px). Section-level padding uses larger multiples that maintain the 4px base.

### Layout Principles
- Fixed containers (max-width 1128–1296px) prevent ultra-wide distortion
- Negative top margins (`margin-top: -78px` on features grid) create section overlap — content bleeds upward into the hero, reinforcing depth
- Grid systems: 4-column for features, 2-column for connected/research cards
- No sidebar layouts — everything is centered, editorial

---

## Motion Strategy

### The Signature Easing
```
cubic-bezier(0.6, 0.6, 0, 1)
```
Every interactive transition in Reflect uses this curve. It's a deceleration ease — fast start, long smooth tail. It feels snappy but not abrupt. This easing is a design signature: even without seeing the brand, a user would recognize it after extended use.

### Two Tiers of Animation

**Ambient / World-building (always running):**
- 70-second rotating star field behind the hero
- Hue-rotating accent elements (2s infinite)
- Rising stars floating upward in the background
- Radar sweeps in the Research section

These create the sensation of a living interface — the page breathes even when nothing is being interacted with.

**Reactive / Interactive (triggered by user):**
- Card hover: gradient overlay fades in (0.45s)
- Button hover: pseudo-element crossfade of two pre-rendered states (0.2s)
- Badge hover: inner glow intensifies (0.45s)
- AI showcase hover: background and border appear (0.45s)

### Why Pseudo-Element Crossfades for Buttons
The button hover uses `:before` (default state rendered) and `:after` (hover state rendered), with opacity transitioning between them. This is more performance-efficient than transitioning `background` directly — the browser doesn't have to recalculate composite styles, just composite two pre-rendered layers.

---

## Glass-morphism System

Glass-morphism is the dominant depth mechanism. Instead of opaque boxes and drop shadows, Reflect uses:

1. **Frosted glass backgrounds**: `background: rgba(white, low-opacity)` over the dark base
2. **Backdrop blur**: `backdrop-filter: blur(6–16px)` creates the frosted effect
3. **Inset box shadows**: Glow emanates from inside the element, not outside
4. **Thin border**: `1px solid rgba(white, 0.08)` — barely visible, adds separation

This stack creates interactive elements that feel like illuminated glass hovering above a dark surface.

### Blur Levels by Component
| Component | Blur | Rationale |
|-----------|------|-----------|
| Header | 16px | Heaviest blur — must separate from all content below |
| Buttons | 8px | Interactive, needs depth but not to overpower |
| Badges | 6px | Small elements, lighter blur |
| Cards | 12px | Content containers, moderate separation |

---

## Component Design Principles

### Navigation
The nav is a floating pill centered above the page content — not a full-width bar. This creates visual separation between navigation and hero content and reinforces the "object floating in space" metaphor. The pill has a barely-visible background (2% white) and a subtle border (8% white). Nav links dim on hover rather than brightening — the opposite of most hover conventions. This feels more sophisticated and reduces visual noise.

### Buttons
Two variants — primary (violet glass) and secondary (near-invisible glass). Both use the same size, padding, and font. The difference is entirely in background color and shadow intensity. Primary uses a purple-tinted background; secondary is essentially invisible until hovered. Both buttons use pseudo-element crossfades for hover — pre-rendering both states and crossfading between them rather than transitioning individual properties.

### Badges
Used as label/announcement elements above section headlines. Always pill-shaped (32px radius), always with a purple gradient text treatment, always with a bottom-weighted inner glow (`inset 0 -7px 11px`). The glow direction (bottom) simulates light pooling at the base of the pill.

### Cards
Feature cards are borderless — they rely on their content and hover overlay to define themselves. On hover, a gradient overlay fades in from the bottom. This is subtle: `rgba(255,255,255,0.06)` — barely there, but enough to signal interactivity.

### AI Rainbow Gradient
Used exclusively on text related to AI features. Applied as `background: linear-gradient(to right, #FC72FF, #8F68FF, #487BFF, #2CD9FF, #2CFFCC)` with `background-clip: text; -webkit-background-clip: text; color: transparent`. This treatment is reserved and meaningful — it's never used for decorative purposes.

---

## Design Constraints & Decisions

| Decision | Rationale |
|----------|-----------|
| Dark-only, no light mode | The glassmorphism system depends on a dark background — it would need to be redesigned for light mode, not just color-swapped |
| Self-hosted fonts | AeonikPro is not on Google Fonts — licensing requires hosting. Inter V (variable) is self-hosted for performance (single file, variable axes) |
| No letter-spacing adjustments | Fonts are used with their designed metrics — a sign of confidence in the typeface choices |
| Two weights max | Restraint in weight reinforces the refined, non-cluttered aesthetic |
| Easing standardization | Using one easing curve site-wide creates subconscious coherence — the product "moves like itself" |
| Animation as product communication | The radar sweep and star field aren't decorative — they visualize the AI/intelligence/network metaphors the product is built on |

---

## Figma Implementation Notes

When building this system in Figma:
1. **Color styles**: Define every `colors.*` token as a Figma color style with the same naming hierarchy
2. **Text styles**: Create one text style per row in the type scale table, using Inter as a Figma substitute for Inter V
3. **Effects**: Backdrop blur requires `Layer blur` on a fill layer in Figma; inset shadows use `Inner shadow` effect
4. **Components**: Build buttons with two variant states (Default, Hover) and use component properties for the pseudo-element crossfade simulation
5. **Auto layout**: All containers use Auto Layout — padding values map directly from the component spacing table
6. **Prototyping**: Set all interaction transitions to "Dissolve" at 200–450ms with a custom cubic bezier matching `0.6, 0.6, 0, 1`
