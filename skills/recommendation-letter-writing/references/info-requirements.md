# Recommendation Letter Information Requirements

## Collection Checklist

**Required fields**

| Field | Required sub-fields |
|------|------|
| Student name | — |
| Student gender or pronouns | Needed for pronoun choice |
| Recommender name | — |
| Recommender title / role | Professor, associate professor, supervisor, manager, etc. |
| Recommender department / organization | — |
| Relationship between recommender and student | Context of contact (course / research supervision / work), duration, course or project name |
| Core story material | Scenes the recommender could directly observe; each story needs situation, task/challenge, concrete student actions, and observable results |

**Optional fields**

| Field | Notes |
|------|------|
| Target program / field | Helps shape emphasis |
| Sample letter | Style reference |
| Grades / rank | Only if the recommender would realistically know them |
| Extra requirements | Word count, special emphasis, submission constraints, etc. |

## Validation Rules

The Phase 1 gate checks **coverage**, not material quantity or quality.

- **Addressed** means either:
  - the user provided that category with all required sub-fields, or
  - the user explicitly said they cannot provide more for that category, such as having only one deep interaction with the recommender.
- **Not addressed** means either:
  - the category was never discussed, or
  - the category was mentioned but is missing required sub-fields, such as a story with praise but no concrete scene or action.

Story count and STAR completeness are judged in Phase 2 and do not block the Phase 1 gate.

## Material-Mining Strategy

1. Infer likely observation scenes from the recommender's role: professor -> classroom interaction, office hours, paper guidance, exam performance; lab mentor -> experiments, group meetings, project collaboration; internship supervisor -> work tasks, teamwork, problem solving.
2. Use careful inference to prompt memory in question form.
   - Example: "You mentioned strong performance in Professor Li's class. Was there a discussion, presentation, or office-hours conversation that left a strong impression?"
   - Example: "You mentioned participation in the XX project. What specific problem did the recommender see the student solve?"
3. Probe for story specificity: when and where it happened, what the student actually did, and what result the recommender could directly observe.
4. Check viewpoint discipline by asking: "How would the recommender know this?" Keep only content within the recommender's direct observational range.

## Sufficiency Criteria

Sufficiency is judged in Phase 2 and determines whether the workflow goes to Branch A (final version) or Branch B (reference draft).

| Judgment | Criteria |
|------|------|
| Sufficient | All required fields are covered, there are 2 to 3 concrete stories that fit the recommender's viewpoint, each story has a clear STAR structure, and the stories cover at least 2 different strengths. |
| Thin | Any of the following: only generic praise, only 1 story, stories missing action or result detail, or the relationship / observation context is unclear. |
