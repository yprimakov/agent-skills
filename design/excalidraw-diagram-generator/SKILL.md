---
name: excalidraw-diagram-generator
description: Generates polished Excalidraw diagrams from data, markdown, or natural language descriptions. Supports flowcharts, architecture diagrams, data visualizations, infographics, and mind maps. Outputs .excalidraw files.
  Use ONLY when the user wants to create a visual diagram, flowchart, infographic, mind map, architecture diagram, or data visualization — and wants it as an Excalidraw file.
  Do NOT use for text-only outputs, Mermaid diagrams (use native Obsidian Mermaid), or when the user asks for a chart library (Chart.js, D3, etc.).
---

# Excalidraw Diagram Generator

You are an expert diagram designer. You generate beautiful, clear, well-laid-out Excalidraw diagrams by writing `.excalidraw` JSON files directly.

---

## Phase 0: Analyze Input

Read the user's input (markdown file, dataset, description) and determine:

1. **Diagram type** — which layout engine to use:
   - `flowchart` — process flows, decision trees, pipelines, org charts
   - `architecture` — system diagrams, microservices, infrastructure
   - `data-viz` — bar charts, comparisons, metrics dashboards
   - `infographic` — visual explainers, step-by-step guides, icon+text layouts
   - `mind-map` — radial/hierarchical concept maps
   - `timeline` — chronological sequences, roadmaps
   - `comparison` — side-by-side feature matrices, pros/cons

2. **Content extraction** — pull out:
   - Nodes/entities and their labels
   - Relationships/connections between them
   - Data values (if data-viz)
   - Hierarchy/grouping structure
   - Any color/style hints from the user

3. **Scale estimation** — how many elements? This determines spacing and font sizes.

---

## Phase 1: Layout Computation

Compute element positions BEFORE generating JSON. Use these layout algorithms:

### Flowchart / Architecture Layout
```
Direction: top-to-bottom (default) or left-to-right
Node size: 200x80 (standard), 160x60 (compact), 240x100 (large)
Horizontal gap: 60px between nodes in the same row
Vertical gap: 100px between rows
Center-align each row relative to the widest row
```

For decision diamonds, branch left (No) and right (Yes) with labels on arrows.

### Data Visualization Layout
```
Canvas: 800-1200px wide depending on data points
Bar width: canvas_width / (n * 2)
Bar gap: bar_width * 0.5
Max bar height: 400px
Scale bars proportionally: bar_height = (value / max_value) * max_bar_height
X-axis labels: centered below each bar
Y-axis: optional scale markers
Title: centered above, fontSize 28
Legend: below chart if multiple series
```

### Infographic Layout
```
Direction: vertical scroll (top to bottom)
Section width: 700px centered
Section height: varies by content
Section gap: 60px
Each section: icon/number left (80x80) + text block right (500px wide)
OR: full-width header + content blocks below
Color-code sections with distinct background fills
```

### Mind Map Layout
```
Center node: 250x100, positioned at canvas center (400, 300)
Level 1 branches: radial placement, 300px from center
Level 2 branches: 200px from their parent
Angular spacing: 360 / n_branches degrees apart
Avoid overlap: min 40px between node edges
Curved arrows from parent to child
```

### Timeline Layout
```
Direction: left-to-right or top-to-bottom
Spine: horizontal/vertical line through center
Event nodes: alternating above/below (or left/right) of spine
Node spacing: 250px apart along spine
Connector: short arrow from spine to event node
Date labels: on the spine at each event position
```

### Comparison Layout
```
Columns: one per item being compared
Header row: item names in colored rectangles
Feature rows: 60px tall, alternating subtle backgrounds
Check/cross indicators or value text in each cell
Column width: 200-250px
Row gap: 10px
```

---

## Phase 2: Generate Excalidraw JSON

### File Structure
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

Use `"viewBackgroundColor": "#ffffff"` for light mode (default) or `"#1e1e1e"` for dark mode.

### Element Generation Rules

1. **Every element needs a unique `id`** — use descriptive IDs like `"node_auth_service"`, `"arrow_auth_to_db"`, `"label_title"`.
2. **Every element needs a unique `seed`** — integer 0 to 2147483647. Increment by 1000 from a random start.
3. **Bindings are ALWAYS bidirectional:**
   - Arrow's `startBinding`/`endBinding` references shape IDs
   - Those shapes MUST list the arrow in their `boundElements`
   - Text's `containerId` references the parent shape
   - The parent shape MUST list the text in its `boundElements`
4. **Arrow `points` are relative** to the arrow's `x,y`. First point is always `[0, 0]`.
5. **`width`/`height` on arrows** must match the bounding box of the points array.
6. **Compute text element `x,y`** to center within containers:
   - `text_x = container_x + (container_width - text_width) / 2`
   - `text_y = container_y + (container_height - text_height) / 2`

### Required Properties for Every Element

```json
{
  "id": "unique_id",
  "type": "rectangle",
  "x": 100, "y": 100,
  "width": 200, "height": 80,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "angle": 0,
  "seed": 1234567,
  "version": 1,
  "versionNonce": 7654321,
  "index": null,
  "isDeleted": false,
  "groupIds": [],
  "frameId": null,
  "boundElements": null,
  "updated": 1700000000000,
  "link": null,
  "locked": false,
  "roundness": {"type": 2}
}
```

### Text Element Additional Properties
```json
{
  "text": "Display text",
  "originalText": "Display text",
  "fontSize": 20,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": null,
  "autoResize": true,
  "lineHeight": 1.25
}
```

### Arrow/Line Additional Properties
```json
{
  "points": [[0, 0], [200, 0]],
  "startBinding": {
    "elementId": "source_id",
    "fixedPoint": [1, 0.5],
    "mode": "inside"
  },
  "endBinding": {
    "elementId": "target_id",
    "fixedPoint": [0, 0.5],
    "mode": "inside"
  },
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "elbowed": false
}
```

**fixedPoint reference** (normalized 0-1 within shape bounding box):
- Left center: `[0, 0.5]`
- Right center: `[1, 0.5]`
- Top center: `[0.5, 0]`
- Bottom center: `[0.5, 1]`
- Top-right: `[1, 0]`

**Arrowhead types**: `"arrow"` | `"bar"` | `"circle"` | `"circle_outline"` | `"triangle"` | `"triangle_outline"` | `"diamond"` | `"diamond_outline"` | `null`

---

## Styling Guide

### Font Families
| Value | Name | Style | lineHeight | Best For |
|---|---|---|---|---|
| `1` | Virgil | Hand-drawn (legacy) | 1.25 | Avoid — use 5 instead |
| `2` | Helvetica | Clean sans-serif | 1.15 | Clean/professional diagrams |
| `3` | Cascadia | Monospace | 1.2 | Code snippets, technical labels |
| `5` | Excalifont | Hand-drawn (default) | 1.25 | Default hand-drawn style |
| `6` | Nunito | Rounded sans-serif | 1.25 | Friendly/approachable |
| `7` | Lilita One | Display/bold | 1.15 | Titles, headers |

### Color Palettes

**Use these curated palettes per diagram type.** Each palette has 4-6 colors that work together.

#### Professional (architecture, flowcharts)
| Role | Stroke | Background |
|---|---|---|
| Primary | `#1971c2` | `#a5d8ff` |
| Secondary | `#099268` | `#96f2d7` |
| Accent | `#6741d9` | `#d0bfff` |
| Warning | `#e8590c` | `#ffd8a8` |
| Neutral | `#343a40` | `#e9ecef` |

#### Warm (infographics, data-viz)
| Role | Stroke | Background |
|---|---|---|
| Primary | `#e03131` | `#ffc9c9` |
| Secondary | `#f08c00` | `#ffec99` |
| Accent | `#c2255c` | `#fcc2d7` |
| Success | `#2f9e44` | `#b2f2bb` |
| Neutral | `#343a40` | `#e9ecef` |

#### Cool (mind maps, timelines)
| Role | Stroke | Background |
|---|---|---|
| Primary | `#1971c2` | `#a5d8ff` |
| Secondary | `#0c8599` | `#99e9f2` |
| Accent | `#9c36b5` | `#eebefa` |
| Tertiary | `#099268` | `#96f2d7` |
| Neutral | `#343a40` | `#e9ecef` |

### Roughness Settings
| Value | Style | When to use |
|---|---|---|
| `0` | Architect (clean lines) | Technical diagrams, architecture, data-viz |
| `1` | Artist (default) | General purpose, flowcharts, mind maps |
| `2` | Cartoonist (very sketchy) | Informal brainstorms, fun infographics |

### Roundness
| Value | Effect | When to use |
|---|---|---|
| `null` | Sharp corners | Technical/precise diagrams |
| `{"type": 2}` | Proportional radius (shapes) | Default for rectangles/diamonds |
| `{"type": 3}` | Adaptive radius (lines) | Default for arrows/lines |

### Font Sizes by Role
| Role | Size | Weight context |
|---|---|---|
| Diagram title | 28-36px | Top of diagram |
| Section header | 24px | Group/frame labels |
| Node label | 16-20px | Inside shapes |
| Arrow label | 14-16px | On connectors |
| Caption/annotation | 12-14px | Small notes, footnotes |

---

## Phase 3: Write File

1. Generate the complete JSON with all elements
2. Write to `{diagram-name}.excalidraw` in the current working directory
3. Report the filename and element count to the user

**Filename convention**: kebab-case, descriptive. Examples:
- `ci-cd-pipeline.excalidraw`
- `q4-revenue-comparison.excalidraw`
- `how-https-works.excalidraw`
- `ml-concepts-mindmap.excalidraw`

---

## Phase 4: Visual Verification

After writing the file, render a preview SVG and screenshot it with Playwright to verify the layout before reporting to the user.

**Steps:**
1. Parse the `.excalidraw` JSON and render it to an SVG file using basic shape rendering (rectangles, diamonds, ellipses, arrows with arrowheads, text positioning)
2. Open the SVG in Playwright and screenshot it
3. Review the screenshot for:
   - **Arrow direction**: Do arrows point the correct way?
   - **Arrow crossing**: Are there unnecessary crossings that can be fixed by repositioning nodes?
   - **Text overflow**: Does text fit inside its container?
   - **Element overlap**: Are any shapes sitting on top of each other?
   - **Layout balance**: Is the diagram centered and well-spaced?
4. If issues are found, adjust element positions/arrow points and regenerate
5. Minimum 1 verification pass; iterate until the layout is clean

**Arrow crossing rules** (learned from iteration):
- In layered/tiered diagrams, vertically align components between tiers so cross-tier arrows go straight down
- Place related components in the same column across tiers
- If fan-out is needed (e.g., load balancer → web servers), stack targets vertically and keep them close to the source's horizontal position
- For circular/cycle diagrams, space nodes evenly around the circle and use consistent angular gaps

---

## Quality Checklist

Before writing the file, verify:

- [ ] All `boundElements` references are bidirectional (container↔text, shape↔arrow)
- [ ] All arrow `points` start with `[0, 0]`
- [ ] Arrow `width`/`height` match the points bounding box
- [ ] No duplicate points in arrow `points` arrays
- [ ] No overlapping elements (check x/y/width/height don't collide)
- [ ] Text fits within containers (text_width < container_width - 10)
- [ ] Consistent color palette throughout (don't mix palettes)
- [ ] All IDs are unique
- [ ] All seeds are unique
- [ ] Font sizes are appropriate for the diagram scale
- [ ] Sufficient spacing between elements (min 40px gaps)
- [ ] Cross-tier arrows flow vertically (no full-width diagonal crossings)
- [ ] Visual preview screenshot reviewed and approved

---

## Element Templates

### Labeled Rectangle
```json
[
  {
    "id": "box1", "type": "rectangle",
    "x": 100, "y": 100, "width": 200, "height": 80,
    "backgroundColor": "#a5d8ff", "strokeColor": "#1971c2",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "seed": 1001, "version": 1, "versionNonce": 2001,
    "index": null, "isDeleted": false, "groupIds": [], "frameId": null,
    "boundElements": [{"id": "box1_label", "type": "text"}],
    "updated": 1700000000000, "link": null, "locked": false,
    "roundness": {"type": 2}
  },
  {
    "id": "box1_label", "type": "text",
    "x": 120, "y": 122, "width": 160, "height": 25,
    "text": "My Label", "originalText": "My Label",
    "fontSize": 20, "fontFamily": 5,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "box1", "autoResize": true, "lineHeight": 1.25,
    "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
    "roughness": 1, "opacity": 100, "angle": 0,
    "seed": 1002, "version": 1, "versionNonce": 2002,
    "index": null, "isDeleted": false, "groupIds": [], "frameId": null,
    "boundElements": null,
    "updated": 1700000000000, "link": null, "locked": false,
    "roundness": null
  }
]
```

### Connecting Arrow (between two shapes)
```json
{
  "id": "arrow1", "type": "arrow",
  "x": 300, "y": 140, "width": 100, "height": 0,
  "points": [[0, 0], [100, 0]],
  "startBinding": {"elementId": "box1", "fixedPoint": [1, 0.5], "mode": "inside"},
  "endBinding": {"elementId": "box2", "fixedPoint": [0, 0.5], "mode": "inside"},
  "startArrowhead": null, "endArrowhead": "arrow", "elbowed": false,
  "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
  "roughness": 1, "opacity": 100, "angle": 0,
  "seed": 1005, "version": 1, "versionNonce": 2005,
  "index": null, "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": null,
  "updated": 1700000000000, "link": null, "locked": false,
  "roundness": {"type": 3}
}
```
**Remember**: Both `box1` and `box2` must include `{"id": "arrow1", "type": "arrow"}` in their `boundElements` arrays.

### Decision Diamond
```json
{
  "id": "decision1", "type": "diamond",
  "x": 150, "y": 300, "width": 160, "height": 120,
  "backgroundColor": "#ffec99", "strokeColor": "#f08c00",
  "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
  "roughness": 1, "opacity": 100, "angle": 0,
  "seed": 1010, "version": 1, "versionNonce": 2010,
  "index": null, "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": [{"id": "decision1_label", "type": "text"}],
  "updated": 1700000000000, "link": null, "locked": false,
  "roundness": {"type": 2}
}
```

### Standalone Text (title, annotation)
```json
{
  "id": "title1", "type": "text",
  "x": 200, "y": 20, "width": 400, "height": 40,
  "text": "System Architecture", "originalText": "System Architecture",
  "fontSize": 32, "fontFamily": 5,
  "textAlign": "center", "verticalAlign": "top",
  "containerId": null, "autoResize": true, "lineHeight": 1.25,
  "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
  "roughness": 1, "opacity": 100, "angle": 0,
  "seed": 1020, "version": 1, "versionNonce": 2020,
  "index": null, "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": null,
  "updated": 1700000000000, "link": null, "locked": false,
  "roundness": null
}
```

### Frame (container for grouping)
```json
{
  "id": "frame1", "type": "frame",
  "x": 50, "y": 50, "width": 500, "height": 400,
  "name": "Backend Services",
  "strokeColor": "#dadada", "backgroundColor": "transparent",
  "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
  "roughness": 0, "opacity": 100, "angle": 0,
  "seed": 1030, "version": 1, "versionNonce": 2030,
  "index": null, "isDeleted": false, "groupIds": [], "frameId": null,
  "boundElements": null,
  "updated": 1700000000000, "link": null, "locked": false,
  "roundness": null
}
```
Child elements set `"frameId": "frame1"` to belong to this frame.
