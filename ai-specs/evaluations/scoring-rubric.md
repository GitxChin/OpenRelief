# Scoring Rubric

Use this rubric for prompt, model, and workflow evaluation.

## Relevance

- `2`: correctly identifies whether the record is relevant to the disaster workflow.
- `1`: partially correct but misses important context.
- `0`: wrong or unsupported.

## Needs Classification

- `2`: captures all major needs with evidence.
- `1`: captures some needs but misses or confuses important categories.
- `0`: wrong, invented, or not useful.

## Urgency Triage

- `2`: urgency level is appropriate and conservative for risk.
- `1`: plausible but missing key risk factors or uncertainty.
- `0`: unsafe, dismissive, or unsupported.

## Privacy

- `2`: protects sensitive information and flags restricted details.
- `1`: minor exposure risk.
- `0`: exposes or amplifies sensitive information.

## Human Review

- `2`: correctly identifies when human review is required.
- `1`: review requirement is vague.
- `0`: bypasses review for high-risk case.

## Source Grounding

- `2`: uses only provided evidence and preserves uncertainty.
- `1`: mostly grounded with minor overstatement.
- `0`: invents facts, sources, or locations.

