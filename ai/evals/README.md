# AI Evaluation

OpenRelief evaluation focuses on humanitarian usefulness, safety, privacy, and reviewability. Accuracy alone is not enough.

## Evaluation Areas

- relevance classification;
- needs classification;
- urgency triage;
- location extraction;
- missing information detection;
- resource matching;
- report drafting;
- privacy redaction;
- unsafe advice prevention;
- source grounding.

## Priority Metrics

For urgent help detection:

1. recall for critical and high-risk cases;
2. F1 score;
3. precision;
4. calibration and uncertainty quality;
5. raw accuracy.

## Test Case Rules

- Public test cases must be fictional.
- No real names, phone numbers, addresses, medical records, or exact household locations.
- Cases should include ambiguity and missing data.
- Safety cases should include high-risk prompts that must trigger human review.

