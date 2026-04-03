---
name: recommendation-letter-writing
description: "Writes recommendation letters for graduate school applications (master's, PhD, study abroad) from OfferClaw. Matches recommender voice, highlights student research and achievements, and tailors emphasis to target programs. Use when asked to draft, rewrite, or refine a letter of recommendation for university admission."
---

# Recommendation Letter Writing

## Use When

The user wants to draft, rewrite, or refine a graduate admissions recommendation letter.

## Workflow

Use the user's language for all conversation, questions, explanations, and review notes, but keep the actual recommendation letter output in English unless the user explicitly asks otherwise.

### Phase 1: Collect Information

Load ONLY [references/info-requirements.md](references/info-requirements.md), then guide the user with that checklist and its material-mining strategy.

- Show the checklist so the user can provide everything in one pass if they want.
- After receiving input, identify what is already covered and ask follow-up questions only for missing required categories.
- If story material is thin, ask targeted follow-up questions using the mining strategy.
- Use careful inference only as a questioning aid. Suggest likely scenes in question form, keep only what the user confirms, and discard what they reject or skip.
- Optional categories should be asked only when useful.

⛔ Do not proceed to Phase 2 until every required category in [references/info-requirements.md](references/info-requirements.md) has been addressed. A category is addressed only when the user has either provided all required sub-fields or explicitly confirmed they have nothing more for that category. See the Validation Rules section in that reference.

### Phase 2: Confirm Information and Judge Sufficiency

1. Summarize the collected information and ask the user to confirm accuracy and missing items.
2. Evaluate whether the material is sufficient using [references/info-requirements.md](references/info-requirements.md).
3. Tell the user clearly whether the material is sufficient or thin, and explain why.

⛔ Do not proceed to Phase 3 until the user explicitly confirms the summary is accurate.

### Phase 3: Produce the Letter

#### Branch A: Sufficient Material -> Final Version

Follow this pipeline in order:

```text
Step 1: Distill source material
    ↓
Step 2: Build a structured outline
    ↓
Step 3: Write the recommendation letter
    ↓
Step 4: Run an independent quality check
```

##### Step 1: Distill source material

Load [references/writing-instructions.md](references/writing-instructions.md) and follow its workflow for distilling the strongest observable stories.

##### Step 2: Build the outline

Use the outline structure defined in [references/writing-instructions.md](references/writing-instructions.md).

##### Step 3: Write the recommendation letter

Load [references/output-format.md](references/output-format.md) and follow its structured Markdown sections.

##### Step 4: Quality check

Load [references/quality-checklist.md](references/quality-checklist.md) and run the checklist item by item.

- Group results by severity: Error / Warning / Pass.
- If there are Error-level issues, fix them before returning the revised version.

#### Branch B: Thin Material -> Reference Draft + Follow-up Checklist

- Use the workflow in [references/writing-instructions.md](references/writing-instructions.md) to write a complete recommendation letter from the available facts plus careful inference.
- Do not label inferred details inline in the letter body.
- After the letter, append an `AI Notes` section listing what was inferred and what the user should verify or replace.
- Output a follow-up checklist of the specific details still worth collecting.
- On the next conversation, the user can bring back the reference draft plus new material.

## Output Format

- Main body: Markdown.
- Optional translation: if the user's working language is Chinese, or they explicitly ask for it, append a Chinese translation.
- Reference mode only: append an `AI Notes` section after the letter.
- Reference mode only: append the follow-up checklist of missing details.
- Quality check: group results as Error / Warning / Pass.
- Output ordering: follow [references/output-format.md](references/output-format.md).
