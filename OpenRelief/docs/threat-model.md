# Threat Model

This document lists early risks for OpenRelief. It should be expanded before handling real sensitive data.

## Assets

- help request records;
- contact details;
- precise locations;
- medical or vulnerability information;
- volunteer profiles;
- resource inventories;
- partner organization data;
- AI prompts and evaluation data;
- audit logs;
- public briefs and maps.

## Threats

### Data Leakage

Sensitive information may be exposed through public issues, logs, prompts, examples, exports, maps, or briefs.

Mitigations:

- public examples must be fictional;
- restrict sensitive fields;
- redact public outputs;
- review prompts and reports before publication.

### False or Malicious Reports

Bad actors may submit fake help requests, resource offers, or rumors.

Mitigations:

- verification status;
- source provenance;
- duplicate detection;
- human review;
- escalation rules.

### AI Misclassification

AI may miss urgent cases or incorrectly classify non-urgent cases.

Mitigations:

- prioritize recall for urgent triage;
- route uncertain cases to humans;
- maintain evaluation cases;
- record confidence and reason codes.

### Unsafe AI Advice

AI may generate unsafe medical, rescue, legal, or security instructions.

Mitigations:

- strict AI output policy;
- human review;
- safety cases;
- prompt constraints;
- public disclaimers.

### Unauthorized Access

Unauthorized users may access restricted records.

Mitigations for future implementation:

- role-based access control;
- audit logs;
- least privilege;
- sensitive-field masking;
- secure partner handoff.

### Operational Exposure

Public outputs may reveal rescue routes, vulnerable households, or partner capacity.

Mitigations:

- aggregate public data;
- delay or withhold sensitive operational details;
- review public briefs and maps.

## Open Questions

- What data retention policy should apply to help requests?
- Which partners may access restricted data?
- How should consent be recorded in emergency contexts?
- What incident response process should be used during active disasters?

