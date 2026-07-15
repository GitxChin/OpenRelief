# Help Request Structuring Prompt Specification

## Purpose

Convert an unstructured help request or field report into a structured humanitarian record for human review.

## Inputs

- original text;
- form fields if available;
- source channel;
- timestamp;
- location hints;
- attachments description;
- reporter role if known.

## Required Output

Return structured data with:

- short summary;
- affected people count;
- vulnerable groups;
- location mentions;
- needs;
- hazards;
- contact availability;
- missing information;
- urgency suggestion;
- confidence;
- review required flag;
- safety notes.

## Safety Rules

- Do not invent missing details.
- Do not infer exact coordinates from vague text.
- Do not expose private contact details in summaries.
- Do not provide medical, rescue, legal, or security instructions.
- Mark uncertain information as uncertain.
- Route life-safety, medical, child, elderly, disability, pregnancy, or trapped-person cases to human review.

## Example Output Shape

```json
{
  "summary": "A family reports being stranded near a flooded residential area and requests evacuation support.",
  "affected_people_count": 4,
  "vulnerable_groups": ["elderly_person"],
  "location_mentions": ["Example District", "near Example Road"],
  "needs": ["evacuation", "drinking_water"],
  "hazards": ["flooding", "transport_disruption"],
  "missing_information": ["exact building", "current water depth"],
  "urgency_suggestion": "high",
  "confidence": "medium",
  "review_required": true,
  "safety_notes": ["Location is incomplete and requires human verification."]
}
```

