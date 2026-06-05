# Human-in-the-Loop Policy

Human review is mandatory for high-risk OpenRelief workflows.

## Mandatory Human Review

Human review is required when a record involves:

- possible immediate life threat;
- trapped, injured, missing, elderly, child, pregnant, disabled, or medically vulnerable people;
- medical, rescue, legal, or security-sensitive topics;
- precise private location;
- personally identifiable information;
- low-confidence AI classification;
- conflicting sources;
- public publication;
- partner handoff;
- volunteer task assignment.

## Review Outcomes

Reviewers may mark records as:

- `new`
- `needs_more_information`
- `verified`
- `partially_verified`
- `duplicate`
- `escalated`
- `matched`
- `in_progress`
- `resolved`
- `closed_unresolved`
- `not_relevant`

## Reviewer Responsibilities

Reviewers should:

- check the original source;
- preserve uncertainty;
- avoid over-claiming;
- redact sensitive details when needed;
- record actions in the audit trail;
- escalate cases beyond their role or expertise.

## AI Correction Loop

When reviewers correct AI output, the correction should be stored as future evaluation material only if privacy, consent, and anonymization requirements are satisfied.

