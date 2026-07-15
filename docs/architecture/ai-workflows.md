# AI Workflows

OpenRelief uses AI to support humanitarian information processing. AI should reduce cognitive load, increase consistency, and help surface urgent cases, but it must not replace accountable human judgment.

## Workflow 1: Help Request Structuring

Input:

- free-text help request;
- form fields;
- uploaded photos or descriptions;
- location hints;
- channel metadata.

AI output:

- structured summary;
- affected people count;
- vulnerable groups;
- needs;
- hazards;
- missing fields;
- suggested review priority;
- confidence and uncertainty notes.

Required review:

- any life-safety case;
- any medical or rescue implication;
- unclear location;
- exposed personal data.

## Workflow 2: Needs Classification

AI classifies needs into operational categories such as rescue, medicine, food, shelter, transport, communication, psychological support, or field verification.

The model should support multi-label output because one case can contain several simultaneous needs.

## Workflow 3: Urgency Triage

AI may suggest urgency levels:

- `critical`: possible immediate life threat;
- `high`: serious risk or vulnerable groups;
- `medium`: important but not immediately life-threatening;
- `low`: informational or non-urgent;
- `unknown`: insufficient evidence.

The system should prioritize recall for critical and high-risk cases. Missing a real urgent case is more harmful than sending extra cases to human review.

## Workflow 4: Location Resolution

AI extracts location mentions and flags uncertainty. It should not invent coordinates. Location confidence must be visible to reviewers.

## Workflow 5: Resource Matching

AI suggests candidate matches between needs and resources, but final assignment requires human confirmation.

Match rationale should include:

- matching need type;
- resource availability;
- location or service area;
- constraints;
- missing information;
- confidence.

## Workflow 6: Brief Drafting

AI drafts situation briefs from reviewed records and source material. Drafts must include source references, verification status, uncertainty, and editorial review requirements.

Public release requires human approval.

## Workflow 7: Safety Review

AI or rule-based checks flag outputs that may contain:

- personal information;
- precise sensitive locations;
- unsafe medical advice;
- unsupported claims;
- unverified public accusations;
- discriminatory language;
- operationally sensitive information.

