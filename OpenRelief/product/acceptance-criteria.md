# Acceptance Criteria

These criteria define when the product documentation package is ready to support implementation planning.

## Repository-Level Acceptance

- README explains the project mission, current stage, and documentation map.
- Product documents exist under `product/`.
- Architecture and product documents are consistent.
- Research foundations and acknowledgements are visible.
- Safety, privacy, and human-in-the-loop rules are explicit.
- Public examples are fictional.

## Product Scope Acceptance

- MVP scope is narrow enough for a first implementation.
- In-scope and out-of-scope items are explicit.
- The first MVP does not imply autonomous emergency dispatch.
- Existing mini-program workflows can be mapped to the MVP.
- NGO coordinators and digital volunteers are first-class users.

## Workflow Acceptance

- Help request workflow is documented from intake to closure.
- Field report workflow is documented from observation to situation awareness.
- Resource offer workflow is documented from intake to candidate match.
- Brief drafting workflow includes source grounding and human editorial review.
- Closure requirements include reason, evidence, and unresolved risks.

## AI Acceptance

- AI is described as decision support only.
- Prompt specifications include safety rules.
- Urgency triage prioritizes review and recall for high-risk cases.
- AI outputs require confidence, evidence, uncertainty, and review flags.
- Medical, rescue, legal, and public reporting outputs require human review.

## Data Acceptance

- Help request, resource offer, task, evidence, consent, and audit concepts are defined.
- Contact visibility and privacy levels are documented.
- Sensitive data handling is addressed.
- Public examples contain no real personal information.

## GitHub Collaboration Acceptance

- Issue templates cover bugs, features, documentation, use cases, and safety/privacy concerns.
- Pull request template asks about safety and privacy.
- Contribution guide warns against uploading sensitive real-world data.
- Security policy explains private reporting expectations.

## Future Implementation Readiness

Implementation planning can begin when a maintainer can derive:

- initial record schemas;
- review state transitions;
- first prompt evaluation tasks;
- first coordinator workflow prototype;
- safety review requirements;
- non-goals for the first code milestone.

