# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

## Repository Overview

A collection of agent skills for graduate admissions writing tasks by [OfferClaw](https://offerclaw.pro). Skills provide packaged instructions, references, and scripts that extend an AI agent's capabilities for producing CVs, recommendation letters, and other application documents for graduate school (master's, PhD, study abroad).

## Creating a New Skill

### Directory Structure

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    references/           # Optional: supplementary materials (examples, templates, rubrics)
    scripts/              # Optional: executable helper scripts
    assets/               # Optional: static assets (images, PDFs)
```

### Naming Conventions

- **Skill directory**: `kebab-case` (e.g., `cv-writer`, `recommendation-letter`)
- **SKILL.md**: Always uppercase, always this exact filename
- **Scripts**: `kebab-case.sh` (e.g., `format-cv.sh`, `merge-sections.sh`)

### SKILL.md Format

```markdown
---
name: {skill-name}
description: {One sentence describing when to use this skill. Include trigger phrases.}
---

# {Skill Title}

{Brief description of what the skill does.}

## How It Works

{Numbered list explaining the skill's workflow}

## Usage

{Instructions, arguments, and 2-3 example invocations}

## Output

{Example output the user will see}
```

Frontmatter must contain **only** `name` and `description` — no extra metadata fields.

### Best Practices for Context Efficiency

Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant.

To minimize context usage:

- **Keep SKILL.md under 500 lines** — put detailed reference material in `references/`
- **Write specific descriptions** — helps the agent know exactly when to activate the skill
- **Use progressive disclosure** — reference supporting files that get read only when needed
- **Prefer scripts over inline code** — script execution doesn't consume context (only output does)
- **File references work one level deep** — link directly from SKILL.md to supporting files

### Script Requirements

If a skill includes helper scripts:

- Use `#!/bin/bash` shebang
- Use `set -e` for fail-fast behavior
- Write status messages to stderr: `echo "Message" >&2`
- Write machine-readable output (JSON) to stdout
- Include a cleanup trap for temp files

## Installation

**Via CLI (recommended):**
```bash
npx skills add offerclaw/agent-skills --skill {skill-name}
```

**Manual:** Copy the skill directory into your agent's skills folder (e.g., `~/.claude/skills/`, `~/.agents/skills/`).
