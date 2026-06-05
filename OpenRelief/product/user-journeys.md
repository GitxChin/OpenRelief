# User Journeys

## Journey 1: Help Request Review

1. A help seeker or proxy reporter submits a request through a mini-program-like intake channel.
2. The record enters OpenRelief with original content, source, timestamp, and contact visibility.
3. AI structures the request into affected people, needs, location, hazards, missing information, and urgency suggestion.
4. The case enters the human review queue.
5. A reviewer checks relevance, location, urgency, and missing fields.
6. The reviewer either requests more information, escalates the case, marks it duplicate, or prepares it for resource matching.
7. Any high-risk case remains visible until it is escalated, assigned, resolved, or closed with reason.

### Success Outcome

The request is not lost, urgent signals are surfaced, uncertainty is visible, and no public personal data is exposed.

## Journey 2: Field Report to Situation Awareness

1. A field volunteer submits a report about road blockage, flooding, damaged buildings, shelter status, or local needs.
2. AI classifies the report as field information and extracts location, hazards, and HEINA-style tags.
3. The report is compared with existing records for duplicates or related clusters.
4. A reviewer marks it verified, partially verified, or needing more information.
5. The report contributes to internal situation awareness and may later support a brief.

### Success Outcome

Local observations become structured evidence without forcing volunteers into unsafe decision-making roles.

## Journey 3: Resource Offer to Candidate Match

1. A resource provider submits a fictional or real-world offer through a future intake channel.
2. The offer is structured into resource type, quantity, availability, service area, constraints, and contact visibility.
3. A coordinator reviews the offer before it is used for matching.
4. OpenRelief suggests candidate matches with reviewed needs.
5. The coordinator confirms, rejects, or requests more information.

### Success Outcome

Resources become discoverable and matchable while preserving provider privacy and coordinator control.

## Journey 4: Urgent Case Escalation

1. A record contains signs of immediate danger, vulnerable people, injury, or blocked evacuation.
2. AI suggests `critical` or `high`, or marks uncertainty with review required.
3. The case is routed to the NGO coordinator or professional supporter according to escalation rules.
4. The reviewer records action taken, handoff status, and unresolved risks.
5. The case remains auditable.

### Success Outcome

The system errs toward review and escalation rather than quietly missing a high-risk case.

## Journey 5: Situation Brief Drafting

1. Reviewed records accumulate over a defined time window and location scope.
2. A coordinator selects sources suitable for internal or public summary.
3. AI drafts a brief with key affected areas, needs, actions, uncertainty, and source references.
4. A human editor reviews the draft for accuracy, privacy, and safety.
5. The brief is approved, revised, or withheld.

### Success Outcome

The team saves time on drafting while preserving source grounding and editorial responsibility.

