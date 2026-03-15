# Fundamental Analysis Skills

Skills focused on evaluating companies through financial statements, valuation models, earnings quality, and competitive positioning.

## Skills

| Skill | Type | Description |
|-------|------|-------------|
| [goldman-sachs-stock-screener](goldman-sachs-stock-screener/) | Entry Point | Guides user through an investment profile questionnaire, then screens 10 stocks and generates MD + HTML reports |
| [morgan-stanley-dcf-valuation](morgan-stanley-dcf-valuation/) | Entry Point | Builds a 9-step Morgan Stanley-style DCF model for any ticker and generates MD + HTML valuation reports |

## Structure

Each entry point skill lives at this level. Companion skills (helpers invoked by an entry point) are nested inside their parent skill folder under `companions/`.

```
fundamental-analysis/
  <skill-name>/
    README.md
    SKILL.md
    companions/
      <companion-name>/
        README.md
        SKILL.md
```
