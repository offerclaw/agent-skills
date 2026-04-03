# Recommendation Letter Quality Checklist

Check the draft against every item below and report a verdict with a brief note.

## Viewpoint Discipline (Error)

- [ ] Every statement could be directly observed by the recommender.
- [ ] The letter does not describe the student's inner thoughts or private conversations.
- [ ] The letter avoids unobservable implementation detail, confidential team discussion, or inside knowledge.

## Factual Consistency (Error)

- [ ] Names, course titles, grades, roles, and dates match the user input.
- [ ] No data, grades, rankings, or outcomes were fabricated.
- [ ] Technical detail has been translated into ability and impact language when needed.

## Content Completeness (Error)

- [ ] The letter has a complete opening, body, and closing.
- [ ] Each body paragraph focuses on no more than 2 strengths or qualities.
- [ ] The closing contains a warm, strong endorsement and willingness to be contacted.

## Language Quality (Warning)

- [ ] The letter avoids em-dash-based sentence sprawl.
- [ ] The letter does not quote the student's speech directly.
- [ ] Sentence length varies naturally and reads smoothly.
- [ ] The letter includes 1 to 2 natural observation-style teaching or mentoring lines.
- [ ] The letter avoids a score-report tone or jargon dumping.

## Structural Logic (Warning)

- [ ] Paragraph transitions feel natural and coherent.
- [ ] Body paragraphs focus on different strengths without repetition.

## Output Format

Group the review by severity:

- **Error**: must be fixed before returning the draft.
- **Warning**: should be improved if possible.
- **Pass**: no issue found.

If any Error-level issue appears, fix it and return the revised version.
