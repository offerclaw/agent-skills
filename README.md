# OfferClaw Agent Skills

AI-powered writing tools for graduate school applications — CV, recommendation letters, and more.

A collection of agent skills for graduate admissions writing by [OfferClaw](https://offerclaw.pro).

[简体中文说明](./README.zh-CN.md)

## Available Skills

### admissions-cv-writing

Writes graduate admissions CVs or resumes tailored for specific programs and exports the final Markdown document to PDF.

**Use when:**

- "Write my admissions CV"
- "Create a graduate school resume"
- "Export my CV to PDF"
- "Tailor my CV for this program"

**Features:**

- Program-specific CV tailoring
- Academic and research experience formatting
- Markdown-to-PDF export
- Publication and project listing

### recommendation-letter-writing

Writes graduate admissions recommendation letters from student and recommender context, matching tone and emphasis to the target program.

**Use when:**

- "Write a recommendation letter"
- "Draft a letter of recommendation for a student"
- "Help me recommend a student for grad school"

**Features:**

- Recommender voice and tone matching
- Program-specific emphasis
- Student achievement highlighting
- Academic and professional context integration

## Why OfferClaw

- Open, inspectable, and customizable skills for graduate admissions writing, validated through real application-season use and real offers
- Ready to install out of the box, or to fork and integrate into your own agent or workflow
- Keeps prompts, review logic, and writing standards as assets you can own instead of hiding them inside an external platform

## For Consultants and Teams

If you are an admissions consultant, studio, or agency and want more than a standalone skill, OfferClaw also provides deployment support for practitioners, including end-to-end AI agent setup and automation workflow integration. The goal is to unlock broader AI capabilities and differentiated configurations, then embed them directly into the tools and service processes you already use.

## Installation

```bash
npx skills add offerclaw/agent-skills
```

Install specific skills:

```bash
npx skills add offerclaw/agent-skills --skill admissions-cv-writing
npx skills add offerclaw/agent-skills --skill recommendation-letter-writing
```

List all available skills:

```bash
npx skills add offerclaw/agent-skills --list
```

## Skill Structure

Each skill lives in its own directory under `skills/`:

```text
skills/<skill-name>/
├── SKILL.md          # Skill definition (required)
├── references/       # Reference documents and examples
├── scripts/          # Helper scripts
└── assets/           # Static assets
```

`SKILL.md` is the only required file. Optional support files (`references/`, `scripts/`, `assets/`) are scoped to the skill that uses them.

## Learn More

- Website: [offerclaw.pro](https://offerclaw.pro)

## License

MIT
