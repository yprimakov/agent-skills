---
name: frontend-deconstructor
description: Reverse-engineer any web application to extract its complete design system: colors, typography, spacing, animations, interactive states, and component structure. Use this skill whenever the user wants to analyze, clone, or understand the design of an existing website or app. Trigger for requests like "analyze the design of X", "deconstruct this site", "extract the design system from Y", "what fonts/colors does Z use", "reverse engineer this UI", or "I want to recreate the look of this site." Also use when the user shares a URL and wants to understand how it's built visually.
---

You are an autonomous reverse-engineering agent. Your objective is to deconstruct a target web application using Playwright browser automation and web fetching. You will extract styling, semantic structure, interactive states, and animation logic through computed styles on the live rendered page — not static HTML analysis — then synthesize these into structured, portable design documents.

The user provides a URL (or enough context to identify the target site). Your output is a set of design reference files that fully document the site's visual design system.

## Core Principle: Playwright-First Extraction

**Always use Playwright (`playwright.sync_api`) as the primary extraction tool.** Static HTML/CSS fetching is unreliable for modern SPAs (Next.js, React, Vue) because:
- Class names are hashed or utility-based (Tailwind) — HTML source tells you little
- RSC streaming (`self.__next_f` payloads) means rendered class names aren't in the static source
- Background layers, animated elements, and interactive states only exist post-JS execution
- `getComputedStyle()` on live DOM gives you actual rendered values, not class-name guesses

Use WebFetch only as a fallback for sites where Playwright is unavailable or blocked.

---

## Execution Pipeline

### Phase 1: Playwright Extraction

Launch a headless Chromium browser. Navigate to the target URL and wait for `networkidle`. Then run a systematic extraction sequence:

**1.1 Force both theme modes**

Check if the site has a dark mode. If so:
- Force dark mode: `document.documentElement.classList.add('dark')` + `localStorage.setItem('theme', 'dark')`
- Take a full-viewport screenshot in dark mode
- Force light mode and take another screenshot
- Identify which is the default (check `localStorage`, `prefers-color-scheme`, or initial class state)

**1.2 Extract background system**

The background is often the most complex and misunderstood element. Query everything:
```python
# Find ALL elements with backgroundImage (orbs, gradients, patterns)
page.evaluate("""() => {
    return Array.from(document.querySelectorAll('*')).filter(el => {
        const s = window.getComputedStyle(el);
        return s.backgroundImage && s.backgroundImage !== 'none';
    }).map(el => {
        const s = window.getComputedStyle(el);
        return {
            tag: el.tagName, class: el.className.substring(0, 150),
            bgImage: s.backgroundImage, position: s.position,
            zIndex: s.zIndex, width: s.width, height: s.height,
            top: s.top, left: s.left, bottom: s.bottom, right: s.right,
            filter: s.filter, opacity: s.opacity, animation: s.animation
        };
    });
}""")
```
Look for: fixed-position orb layers, CSS grid overlays, gradient fills. Note animation names — these are often the key detail that makes the design feel alive (e.g., slow floating drift on background orbs).

**1.3 Extract glass/card system**

Find all elements with `backdropFilter` set:
```python
page.evaluate("""() => {
    return Array.from(document.querySelectorAll('*')).filter(d => {
        const s = window.getComputedStyle(d);
        return s.backdropFilter && s.backdropFilter !== 'none';
    }).slice(0, 8).map(el => {
        const s = window.getComputedStyle(el);
        const inner = el.querySelector(':scope > div') || el.firstElementChild;
        const si = inner ? window.getComputedStyle(inner) : null;
        return {
            outerClass: el.className.substring(0, 150),
            outerBg: s.backgroundColor, backdropFilter: s.backdropFilter,
            outerRadius: s.borderRadius, outerBoxShadow: s.boxShadow,
            outerPadding: s.padding,
            innerBg: si?.backgroundColor, innerRadius: si?.borderRadius,
            innerBoxShadow: si?.boxShadow, innerClass: inner?.className?.substring(0, 150)
        };
    });
}""")
```
This reveals the two-layer glass card pattern (transparent outer + rgba inner), exact shadow values, and the 1px padding rim-light trick.

**1.4 Extract nav structure**

```python
page.evaluate("""() => {
    const navs = document.querySelectorAll('nav, header, [class*="nav"], [class*="Nav"]');
    return Array.from(navs).map(n => ({
        tag: n.tagName, class: n.className.substring(0, 200),
        position: window.getComputedStyle(n).position,
        bg: window.getComputedStyle(n).backgroundColor,
        html: n.innerHTML.substring(0, 1500)
    }));
}""")
```
Look for: sticky positioning, frosted glass blur, sliding active indicator elements (absolute-positioned bg divs inside nav pills), CSS var usage for active state.

**1.5 Extract typography**

```python
page.evaluate("""() => {
    return ['h1','h2','h3','h4','p','span','a','button','label'].map(tag => {
        const el = document.querySelector(tag);
        if (!el) return null;
        const s = window.getComputedStyle(el);
        return { tag, text: el.innerText?.substring(0, 60),
            fontSize: s.fontSize, fontWeight: s.fontWeight,
            fontFamily: s.fontFamily, lineHeight: s.lineHeight,
            color: s.color, letterSpacing: s.letterSpacing };
    }).filter(Boolean);
}""")
```

**1.6 Extract interactive elements**

For buttons, links, and form inputs:
```python
page.evaluate("""() => {
    return Array.from(document.querySelectorAll('button, a[href], input')).slice(0, 12).map(el => {
        const s = window.getComputedStyle(el);
        return { text: el.innerText?.substring(0, 40), tag: el.tagName,
            bg: s.backgroundColor, bgImage: s.backgroundImage.substring(0, 120),
            color: s.color, borderRadius: s.borderRadius, padding: s.padding,
            fontSize: s.fontSize, fontWeight: s.fontWeight, border: s.border };
    });
}""")
```

**1.7 Take targeted screenshots**

Capture at minimum:
- Hero / above-fold (default theme)
- Hero / above-fold (dark theme forced)
- Scrolled down to card grid
- Further scroll to see marquees, lists, portfolio sections

Use these screenshots as ground truth when building the component library.

**1.8 Extract CSS keyframe animations**

```python
page.evaluate("""() => {
    return Array.from(document.styleSheets)
        .flatMap(sheet => { try { return Array.from(sheet.cssRules); } catch(e) { return []; } })
        .filter(r => r.type === CSSRule.KEYFRAMES_RULE)
        .map(r => ({ name: r.name, cssText: r.cssText.substring(0, 400) }));
}""")
```
This reveals animation names like `float-1`, `animate-scroll`, `spotlight`, and their keyframe definitions.

---

### Phase 2: Synthesis

Organize everything into **three output files**:

**`design_reference.md`** — Human-readable design reference:
- Site overview: aesthetic impression, CSS framework, component library, rendering strategy (SSR/RSC/SPA)
- Background system: describe the ambient layer (orbs, gradients, patterns) with exact gradient values
- Color palette: organized by role (background, surface/glass, text, accent/brand, border, shadow, gradient stops)
- Typography system: verified font families, complete size scale with computed px values
- Spacing & layout system
- Component inventory: for each major component, document the full CSS property set (bg, backdrop-filter, border-radius, box-shadow, padding, transition)
- Motion & animation: list every named animation, its duration, easing, what it animates
- Interactive states: hover/focus/active per component type
- Design personality: what makes this design distinctive — be specific, not generic

**`theme_architecture.jsonc`** — Structured design token file:
```jsonc
{
  "meta": {
    "site": "",
    "framework": "",           // Next.js App Router, Vite, etc.
    "cssFramework": "",        // Tailwind version, CSS Modules, etc.
    "componentLibrary": "",    // shadcn/ui, Radix, Headless UI, etc.
    "themeMode": "",           // light-only / dark-only / light+dark
    "fontStrategy": "",        // system-ui / Google Fonts / custom
    "backgroundSystem": "",    // describe ambient layer implementation
    "verificationMethod": ""   // Playwright computed styles / static analysis
  },
  "colors": {
    // Include ALL of these where applicable:
    "background": {},          // page bg, light + dark
    "foreground": {},          // primary text
    "primary": {},             // primary interactive color
    "secondary": {},           // secondary surfaces
    "muted": {},               // disabled/subdued areas
    "mutedForeground": {},     // secondary text
    "accent": {},              // hover/focus accent
    "accentBrand": {},         // SINGLE brand accent color (if present)
    "border": {},
    "ring": {},                // focus ring
    "destructive": {},
    "ambientOrbs": {},         // background orb gradients, positions, sizes, animations
    "badgeGradients": {},      // gradient palettes used on tags/badges
    "overlays": {}
  },
  "typography": {
    "fontFamilies": {},
    "fontSizes": {},           // include computed px values
    "fontWeights": {},
    "lineHeights": {},
    "letterSpacing": {}
  },
  "spacing": {},
  "borders": { "radius": {}, "widths": {} },
  "shadows": {},
  "effects": {
    "backdropBlur": {},
    "glassmorphism": {
      // Document outer wrapper AND inner card separately:
      "outerWrapper": {},      // bg, backdropFilter, borderRadius, padding, shadow
      "innerCard": {}          // bg, borderRadius, boxShadow (inset highlight)
    }
  },
  "motion": {
    "durations": {},
    "easings": {},
    "animations": {}           // each named animation: type, keyframes, duration, easing, what it does
  },
  "breakpoints": {},
  "components": {}             // nav, hero, glassCard, cardBorder, button, marquee, etc.
}
```

**`component_library.html`** — A self-contained, single-file HTML component showcase that:

**Must defaults:**
- **Default to the site's primary theme mode.** If the site defaults to dark, set `class="dark"` on `<html>`.
- Dark mode toggle must be functional (JS class swap on `<html>`, persisted to `localStorage`)

**Background layer (critical):**
- Implement the exact ambient background system: if the site uses floating orbs, replicate all of them with correct gradient values for both light and dark modes
- Include any CSS keyframe animations that make the background feel alive (floating drift, pulsing, etc.)
- Background layer must be `position:fixed; z-index:-10; overflow:hidden`

**Glass card system:**
- Use a two-layer approach matching the site: `.glass-wrap` (outer) + `.glass-card` (inner)
- Outer: `position:relative; border-radius:Xpx; padding:1px; backdrop-filter:blur(Xpx); overflow:hidden; box-shadow:[shadow]`
- Inner: `position:relative; border-radius:inherit; z-index:20; background:rgba(...); box-shadow:inset 0 1px 0 rgba(255,255,255,0.X)`
- The 1px padding creates the rim-light gap — this is the detail that makes glass cards look physically lit

**Spotlight / mouse-follow effects:**
- If the site has a mouse-follow glow effect, implement it with vanilla JS:
  - `mousemove` listener → `requestAnimationFrame` flag (not `setTimeout`) → `getBoundingClientRect` per element → `style.setProperty('--mx', x+'px')` and `style.setProperty('--my', y+'px')`
  - CSS `::before`/`::after` pseudo-elements translate via `transform: translate(var(--mx), var(--my))`
  - Mark all spotlight-reactive elements with `data-spot` attribute
  - Apply the effect to the nav pill, all cards, and any other interactive surfaces

**Nav:**
- Replicate the actual nav structure: sticky/fixed, centered vs. left-aligned, pill vs. full-width
- If the site uses a sliding active indicator (absolute-positioned bg element that moves to active link), implement it with JS that reads `getBoundingClientRect` of the active link and positions the indicator

**Marquee/scroll animations:**
- Wrap in a glass card
- Include gradient fade masks on both edges (`::before`/`::after` on the overflow container)
- Duplicate the content array for seamless looping

**Content fidelity:**
- Use the site's actual content (names, job titles, project names) not placeholder lorem ipsum
- Preserve visual hierarchies: if past experience items have `text-decoration:line-through`, replicate that — don't just dim the opacity
- All interactive states (hover transform, border fade-in, color shift) must work

**Layout:**
- Wrap every section in a glass card — the component library itself should feel like the site
- All sections are scrollable and each has a `cl-section-title` label and optional `cl-label` annotations showing the CSS property values used

**Quality standards:**
- Zero console errors
- No external dependencies (except Google Fonts if the site uses them)
- Fully functional in any modern browser with no build step

---

### Phase 3: Visual Verification Loop

After generating the component_library.html, **take Playwright screenshots of both the component library and the reference site** and compare them visually before finalizing:

```python
# Screenshot component library
lib.goto('file:///path/to/component_library.html')
lib.screenshot(path='lib_v1.png')

# Screenshot reference site (with forced theme match)
ref.goto('https://target-site.com')
ref.screenshot(path='ref.png')
```

Compare:
1. Does the background atmosphere match? (orb colors, positions, glow intensity)
2. Do the glass cards look the same? (opacity, blur, shadow color)
3. Does the nav match in structure and style?
4. Does typography weight and size feel right?
5. Do interactive effects (hover, spotlight) behave the same?

**Iterate** — if there are visible discrepancies, re-extract the specific values that differ and update the file. Repeat until the screenshots are visually aligned. Minimum 2 comparison rounds.

---

### Phase 4: Quality Check

Before presenting results:
- Flag any design tokens you could not extract with certainty — label them `// UNVERIFIED` in the JSONC
- Ensure ALL named CSS animations are documented (especially background drift animations that make the design feel alive)
- Verify the JSONC has no syntax errors (no trailing commas before `}` or `]`)
- Confirm the component_library.html opens with zero console errors
- Confirm both themes render correctly and the toggle works

---

## Failure Conditions

- **Never guess computed values** — if you can't verify a value with `getComputedStyle`, mark it `// UNVERIFIED`
- **Never treat background gradients as decoration** — the ambient background layer is often the defining character of a design; always extract it fully
- **Never use placeholder content** — use the site's actual text, names, and content
- **Never skip the visual comparison loop** — static analysis alone is insufficient for modern SPAs

---

## How to Extract (Tool Priority Order)

1. **Playwright Python** (`from playwright.sync_api import sync_playwright`) — primary tool, always use first
2. **WebFetch** — fallback for CSS bundle files, fetching specific `chunk-*.js` or `*.css` files that contain design tokens or animation keyframes
3. **Grep** — searching fetched CSS/JS content for specific patterns (`--variable-name`, `keyframes`, `font-family`)

When Playwright is available, prefer `getComputedStyle()` over parsing source CSS — computed styles are what actually renders.

---

## Output

Save all output files to the directory specified by the user, or create a sensibly named folder (`sample/<site-name>/`) if none is specified. Present a brief summary of key findings after saving the files, noting:
- The site's CSS framework and rendering strategy
- The default theme mode
- Any particularly distinctive design elements discovered (e.g., spotlight effect, floating orbs, animated borders)
- Any values that remain `UNVERIFIED`
