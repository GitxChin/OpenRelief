# Product Requirements Document

## Product Name

OpenRelief: AI-enabled disaster information for humanitarian action

## Product Positioning

OpenRelief is an open-source workflow and knowledge infrastructure for NGO-led humanitarian response. The first product version focuses on helping coordinators and volunteers process disaster-related information from mini-program reports, public information, resource offers, and field updates.

It should help teams answer:

- What information has been received?
- Which reports are relevant and urgent?
- What needs are emerging?
- Where are affected areas and uncertain locations?
- What evidence supports each assessment?
- What resources or organizations may be suitable?
- What can be safely summarized into an internal or public brief?

## Problem Statement

During disasters, affected people and communities communicate through fragmented channels. Existing NGO teams often rely on spreadsheets, messaging groups, public posts, manual notes, and volunteer coordination. This creates several problems:

- important help requests can be missed;
- urgent and non-urgent information is mixed together;
- location, needs, and vulnerability details are incomplete;
- duplicate reports are hard to merge;
- resource offers are not easy to match with needs;
- brief generation is labor-intensive;
- privacy and evidence tracking are inconsistent;
- volunteer review is hard to coordinate at scale.

OpenRelief should make this workflow more structured, auditable, and AI-assisted while keeping humans responsible for high-risk decisions.

## Users

- Help seeker or proxy reporter.
- Field volunteer.
- Resource provider.
- NGO coordinator.
- Professional supporter.
- Safety reviewer.
- Project maintainer.

Detailed role definitions are in [personas.md](personas.md).

## MVP Product Goal

The MVP should provide a documented and testable workflow for:

1. receiving disaster-related help, field, and resource information;
2. structuring information into standard records;
3. classifying needs and urgency;
4. routing high-risk or uncertain cases to human review;
5. supporting resource matching suggestions;
6. drafting source-grounded situation briefs for human editing;
7. preserving privacy, evidence, provenance, and audit expectations.

The current repository stage implements the product definition and collaboration framework only. Business code is out of scope until the MVP scope and implementation plan are approved.

## Functional Requirements

### FR1: Help Request Intake Model

The product must define the minimum data needed to receive and review a help request:

- original content;
- source channel;
- submission time;
- affected people count;
- vulnerable groups;
- location;
- needs;
- hazards;
- contact visibility;
- verification status;
- consent status;
- evidence.

### FR2: Field Report Intake Model

The product must support field information such as:

- road status;
- flooding;
- building damage;
- shelter status;
- supply shortage;
- public service interruption;
- organization activity;
- local volunteer observation.

### FR3: Resource Offer Model

The product must support resource offers:

- resource type;
- quantity;
- availability window;
- service area;
- provider type;
- constraints;
- review status;
- restricted contact.

### FR4: AI-Assisted Structuring

The product must define how AI turns unstructured text into structured records. AI output must include:

- extracted fields;
- evidence phrases;
- confidence;
- uncertainty;
- missing information;
- review requirement.

### FR5: Needs Classification

The product must support multi-label needs classification, including rescue, evacuation, medical support, food, water, shelter, transport, communication, psychological support, care support, and field verification.

### FR6: Urgency Triage

The product must support urgency levels:

- critical;
- high;
- medium;
- low;
- unknown.

Critical and high-risk cases must require human review.

### FR7: Human Review Queue

The product must define review statuses and review actions:

- mark relevant or not relevant;
- confirm or correct urgency;
- confirm or correct needs;
- request more information;
- merge duplicate;
- escalate;
- match resource;
- close case.

### FR8: Resource Matching Support

The product must support AI or rule-based match suggestions, but final task assignment must be human-confirmed.

### FR9: Situation Brief Drafting

The product must support source-grounded brief drafting. Briefs must preserve:

- time window;
- location scope;
- verification status;
- key needs;
- affected groups;
- uncertainty;
- source references.

### FR10: Safety, Privacy, and Audit

The product must define:

- privacy levels;
- contact visibility;
- source provenance;
- consent records;
- audit logs;
- safety review triggers.

## Non-Functional Requirements

- **Safety first**: high-risk AI outputs require human review.
- **Privacy by design**: collect and expose the minimum data needed.
- **Auditability**: key actions must be traceable.
- **Explainability**: AI suggestions must include evidence and uncertainty.
- **Localization-ready**: Chinese disaster response workflows are first-class.
- **Open collaboration**: documentation and issue templates should allow NGO and research contributors to participate.
- **Modularity**: future code should separate intake, triage, matching, review, reporting, and audit concerns.

## MVP Success Criteria

The MVP product definition is successful when:

- contributors can understand the first product scope without reading the whole repository;
- the mini-program workflow can be mapped to the data model;
- AI workflow boundaries are explicit;
- safety review and escalation rules are documented;
- fictional examples cover help request and resource offer flows;
- GitHub issue templates can capture product, documentation, use case, and safety input;
- future implementation can begin from a clear backlog.

## Risks

- Overbuilding a large platform before validating workflows.
- Treating AI output as final judgment.
- Exposing sensitive personal or location data.
- Missing urgent cases because of over-reliance on accuracy.
- Importing English Twitter research without adapting to Chinese mini-program and NGO workflows.
- Creating documentation that looks complete but is not usable in operations.

## Dependencies

- Existing OpenRelief/NCP Relief operational knowledge.
- Existing mini-program workflow and field forms.
- Zhuoming Info Aid disaster information methodology and HEINA-style analysis.
- Research foundations documented in [../docs/research-foundations.md](../docs/research-foundations.md).
- Safety policies documented in [../ai/policies](../ai/policies).

