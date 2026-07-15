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

## Operational Workflow

```text
Intake
  ↓
AI structuring
  ↓
Relevance and safety screening
  ↓
Human review
  ↓
Needs and urgency confirmation
  ↓
Resource matching or escalation
  ↓
Task follow-up
  ↓
Briefing and closure
```

### Help Request Workflow

#### Intake

Capture:

- original content;
- source channel;
- timestamp;
- reporter role if known;
- contact visibility;
- attachments description;
- initial location hints.

#### Structuring

AI suggests:

- affected people count;
- vulnerable groups;
- needs;
- hazards;
- location mentions;
- missing fields;
- urgency level;
- review requirements.

#### Human Review

Reviewer confirms:

- relevance;
- urgency;
- needs;
- location usability;
- duplicate status;
- escalation path.

#### Follow-Up

Coordinator may:

- request more information;
- escalate to professional supporter;
- match with resource;
- create task;
- hand off to partner;
- close with reason.

### Field Report Workflow

#### Intake

Capture field observations such as:

- water depth;
- road access;
- building condition;
- public service interruption;
- shelter condition;
- local resource gaps.

#### Classification

AI classifies:

- hazard;
- impact;
- need;
- action;
- location;
- verification confidence.

#### Review and Cluster

Reviewer checks whether the report:

- confirms an existing case;
- adds new information;
- conflicts with other sources;
- should be added to situation board;
- is safe to include in a brief.

### Resource Offer Workflow

#### Intake

Capture:

- provider type;
- resource type;
- quantity;
- availability;
- service area;
- constraints;
- contact visibility.

#### Review

Coordinator checks:

- provider credibility;
- resource usability;
- restrictions;
- safety concerns;
- matching readiness.

#### Matching

AI or rules suggest candidate matches. Human confirmation is required before task creation or partner handoff.

### Brief Drafting Workflow

#### Select Evidence

Coordinator selects reviewed or partially reviewed records for a time window and location scope.

#### Draft

AI drafts:

- summary;
- affected areas;
- key needs;
- vulnerable groups if safe;
- action updates;
- uncertainty;
- source references.

#### Editorial Review

Human editor checks:

- factual accuracy;
- source grounding;
- verification labels;
- privacy;
- operational sensitivity;
- public suitability.

#### Publish or Withhold

The brief is approved, revised, kept internal, or withheld.

### Review Statuses

- `new`
- `ai_structured`
- `needs_review`
- `needs_more_information`
- `verified`
- `partially_verified`
- `duplicate`
- `escalated`
- `matched`
- `task_created`
- `in_progress`
- `resolved`
- `closed_unresolved`
- `not_relevant`

### Closure Requirements

Every closed case should include:

- closure status;
- closure reason;
- reviewer role;
- last known evidence;
- unresolved risks;
- handoff if any.
