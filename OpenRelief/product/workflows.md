# Workflows

## Workflow Overview

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

## Help Request Workflow

### 1. Intake

Capture:

- original content;
- source channel;
- timestamp;
- reporter role if known;
- contact visibility;
- attachments description;
- initial location hints.

### 2. Structuring

AI suggests:

- affected people count;
- vulnerable groups;
- needs;
- hazards;
- location mentions;
- missing fields;
- urgency level;
- review requirements.

### 3. Human Review

Reviewer confirms:

- relevance;
- urgency;
- needs;
- location usability;
- duplicate status;
- escalation path.

### 4. Follow-Up

Coordinator may:

- request more information;
- escalate to professional supporter;
- match with resource;
- create task;
- hand off to partner;
- close with reason.

## Field Report Workflow

### 1. Intake

Capture field observations such as:

- water depth;
- road access;
- building condition;
- public service interruption;
- shelter condition;
- local resource gaps.

### 2. Classification

AI classifies:

- hazard;
- impact;
- need;
- action;
- location;
- verification confidence.

### 3. Review and Cluster

Reviewer checks whether the report:

- confirms an existing case;
- adds new information;
- conflicts with other sources;
- should be added to situation board;
- is safe to include in a brief.

## Resource Offer Workflow

### 1. Intake

Capture:

- provider type;
- resource type;
- quantity;
- availability;
- service area;
- constraints;
- contact visibility.

### 2. Review

Coordinator checks:

- provider credibility;
- resource usability;
- restrictions;
- safety concerns;
- matching readiness.

### 3. Matching

AI or rules suggest candidate matches. Human confirmation is required before task creation or partner handoff.

## Brief Drafting Workflow

### 1. Select Evidence

Coordinator selects reviewed or partially reviewed records for a time window and location scope.

### 2. Draft

AI drafts:

- summary;
- affected areas;
- key needs;
- vulnerable groups if safe;
- action updates;
- uncertainty;
- source references.

### 3. Editorial Review

Human editor checks:

- factual accuracy;
- source grounding;
- verification labels;
- privacy;
- operational sensitivity;
- public suitability.

### 4. Publish or Withhold

The brief is approved, revised, kept internal, or withheld.

## Review Statuses

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

## Closure Requirements

Every closed case should include:

- closure status;
- closure reason;
- reviewer role;
- last known evidence;
- unresolved risks;
- handoff if any.

