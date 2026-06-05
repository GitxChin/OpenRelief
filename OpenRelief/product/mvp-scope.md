# MVP Scope

## MVP Theme

The first MVP is an **AI-assisted disaster information review and coordination workflow** for NGO coordinators and digital volunteers.

It is not a full emergency dispatch system. It is not a replacement for the existing mini-program. It is the structured backend logic and review workflow that can sit behind public intake channels.

## MVP Objective

Turn incoming help requests, field reports, and resource offers into reviewed, structured, evidence-aware records that can support:

- urgency triage;
- needs assessment;
- resource matching;
- volunteer review;
- situation brief drafting.

## In Scope

### 1. Product Documentation

- PRD.
- MVP scope.
- user journeys.
- personas.
- workflows.
- acceptance criteria.

### 2. Standard Records

Define conceptual records for:

- help request;
- field report;
- resource offer;
- need;
- location;
- evidence;
- verification record;
- review status;
- task;
- audit log;
- consent record.

### 3. AI Workflow Specifications

Define prompts and policies for:

- help request structuring;
- needs classification;
- urgency triage;
- resource matching;
- situation report drafting;
- safety review.

### 4. Human Review Workflow

Define:

- review statuses;
- reviewer roles;
- escalation triggers;
- high-risk case handling;
- closure expectations.

### 5. Fictional Examples

Provide example help requests, resource offers, and workflow narratives using fictional data only.

### 6. GitHub Collaboration

Provide templates for:

- bugs;
- feature requests;
- documentation improvements;
- humanitarian use cases;
- safety and privacy concerns;
- pull requests.

## Out of Scope

The MVP documentation stage does not include:

- production application code;
- web dashboard implementation;
- API implementation;
- database schema or migrations;
- real AI model calls;
- real personal data;
- real partner integrations;
- automatic rescue dispatch;
- public map publication;
- medical diagnosis or treatment;
- legal advice;
- automated final triage decisions.

## First Implementation Candidates

When code work begins later, the first implementation should likely focus on:

1. schema definitions for fictional records;
2. local prompt evaluation with fictional cases;
3. review status transitions;
4. source-grounded brief drafting;
5. simple coordinator-facing prototype.

These are candidates only. They are listed to help future planning, not to start coding now.

## MVP Inputs

- mini-program help request fields;
- field report text;
- resource offer text or form fields;
- official or partner source excerpts;
- volunteer review notes;
- fictional evaluation cases.

## MVP Outputs

- structured help request;
- structured resource offer;
- needs list;
- urgency suggestion;
- review status;
- escalation recommendation;
- match suggestion;
- brief draft;
- audit expectation.

## Acceptance Criteria

The MVP documentation package is acceptable when:

- a new contributor can explain the product in five minutes;
- a domain volunteer can map the mini-program form to the data model;
- a safety reviewer can identify where high-risk cases are handled;
- an engineer can see future module boundaries without code;
- a researcher can see how prior papers are acknowledged and translated into workflows;
- all public examples are fictional;
- there is no implication that AI makes final life-safety decisions.

