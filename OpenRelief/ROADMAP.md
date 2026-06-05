# Roadmap

This roadmap is intentionally staged. OpenRelief should grow from a clear, safe foundation into working software only after the humanitarian workflows, data model, AI policies, and evaluation criteria are explicit.

## Phase 0: Repository Foundation

- Establish README, license, contribution guide, governance, security, and code of conduct.
- Document humanitarian use cases and safety principles.
- Document product requirements, MVP scope, personas, user journeys, workflows, and acceptance criteria.
- Document the first system architecture and data model.
- Add AI prompt specifications, policies, and evaluation rubrics.
- Add fictional examples and GitHub issue templates.
- Acknowledge research foundations and prior disaster informatics work.

## Phase 1: MVP Product Definition

- Define the first user journeys for help seekers, NGO coordinators, volunteers, and resource providers.
- Convert the existing mini-program workflow into structured product requirements.
- Define required review states, escalation states, and closure states.
- Define minimum viable schemas for help requests, needs, resources, organizations, volunteers, tasks, evidence, and audit logs.
- Define non-goals for the first implementation.

## Phase 2: AI-Assisted Workflow Prototype

- Implement help request structuring.
- Implement needs classification.
- Implement urgency triage with conservative human-review defaults.
- Implement source attribution and verification status.
- Implement fictional evaluation cases.
- Compare prompt-based behavior against human labels.

## Phase 3: Operations Workspace

- Build a coordinator-facing dashboard for incoming reports, review queues, maps, and tasks.
- Support duplicate detection and case merging.
- Support volunteer review and organization handoff.
- Support brief drafting with citations and verification labels.
- Add role-based permissions and audit logs.

## Phase 4: Public Intake and Partner Integrations

- Connect public intake channels such as mini programs, forms, and trusted partner feeds.
- Add resource offer intake.
- Add notification and collaboration integrations.
- Add data export for vetted NGO partners.
- Add privacy-preserving public map and briefing views.

## Phase 5: Evaluation, Localization, and Field Readiness

- Build Chinese disaster information evaluation datasets using consented or fully anonymized data.
- Evaluate bias, recall, false negatives, and high-risk misclassification.
- Add localization support for Chinese dialects, mixed-language text, and multilingual coordination.
- Conduct tabletop exercises with NGO and volunteer teams.
- Publish deployment and incident response guidance.
