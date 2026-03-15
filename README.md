# Agent Skills

A curated collection of reusable agent skills organized by domain. Each skill is a self-contained prompt or workflow that can be invoked as a Claude Code slash command.

## Structure

Skills are grouped into top-level categories. Each category contains specialized skills as subdirectories.

```
<category>/
  README.md           # Category overview and skill index
  <skill-name>/
    README.md         # Usage, inputs, outputs, examples
    skill.md          # The skill prompt/definition
```

## Categories

| Category | Description |
|----------|-------------|
| [finance/](finance/) | Financial analysis — markets, portfolios, risk, fundamentals, technicals |

## Usage

Skills are designed to be used as Claude Code slash commands. Copy a `skill.md` file into your project's `.claude/commands/` directory, or reference it directly.

## Contributing

Each skill should include:
- A clear description of what it does
- Required inputs and expected outputs
- At least one usage example
- Any dependencies or prerequisites
