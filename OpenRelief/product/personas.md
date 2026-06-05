# Personas

## Help Seeker

The help seeker is an affected person or a proxy reporter submitting information on behalf of affected people.

### Goals

- Make a request visible.
- Provide location, needs, and contact information.
- Receive appropriate follow-up when possible.

### Constraints

- May be under stress or in danger.
- May have poor network access.
- May not know precise address or official terminology.
- May not be able to provide complete details.

### Product Implications

- Intake must tolerate incomplete information.
- AI should identify missing fields.
- High-risk cases must be routed to human review.
- Public outputs must protect identity and exact location.

## Field Volunteer

The field volunteer provides local observations, verification, mapping, translation, or community support.

### Goals

- Report changing conditions.
- Verify information safely.
- Help coordinators understand local needs.
- Avoid duplicating work.

### Constraints

- May not have professional rescue training.
- May have limited availability.
- May face safety risks.
- Needs clear task boundaries.

### Product Implications

- Volunteer roles and permissions must be bounded.
- Tasks must include safety notes and escalation rules.
- Volunteers should not receive unnecessary sensitive data.

## NGO Coordinator

The NGO coordinator reviews information, prioritizes cases, coordinates volunteers, communicates with partners, and prepares situation updates.

### Goals

- See the most urgent and actionable information.
- Understand evidence and uncertainty.
- Assign review or follow-up tasks.
- Match needs with resources.
- Produce reliable situation briefs.

### Constraints

- Works under time pressure.
- Must manage uncertainty and incomplete information.
- Needs accountability and audit trails.
- May coordinate across many organizations.

### Product Implications

- Review queues must be clear.
- AI suggestions must be explainable.
- Evidence and verification state must stay visible.
- Briefs must be source-grounded.

## Resource Provider

The resource provider offers supplies, shelter, transport, funds, professional services, or technical support.

### Goals

- Make available resources known.
- Define where and when resources can be used.
- Coordinate with trusted organizations.

### Constraints

- May have limited logistics capacity.
- May need verification before handoff.
- May not want public contact exposure.

### Product Implications

- Resource offers need structured availability and constraints.
- Contact visibility should be restricted by default.
- Matching suggestions require coordinator confirmation.

## Professional Supporter

The professional supporter may include medical, psychological, legal, logistics, mapping, or technical experts.

### Goals

- Review cases within professional boundaries.
- Provide bounded guidance to coordinators.
- Avoid unsafe advice or role confusion.

### Constraints

- Needs context and evidence.
- Cannot provide final diagnosis or treatment through generic AI workflows.
- May have licensing, liability, or scope limits.

### Product Implications

- Professional review should be explicitly marked.
- AI must not impersonate professional judgment.
- Escalation rules must preserve role boundaries.

## Safety Reviewer

The safety reviewer checks privacy, AI misuse, data exposure, public reporting, and high-risk workflow risks.

### Goals

- Prevent harm from data exposure or unsafe automation.
- Review prompts, examples, reports, and public outputs.
- Maintain safety policies.

### Constraints

- Needs clear risk signals.
- Needs access to audit and source information.
- Must be able to block unsafe release.

### Product Implications

- Safety concerns need a first-class workflow.
- Public outputs require review states.
- Sensitive data must be easy to identify and restrict.

## Project Maintainer

The maintainer stewards the open-source repository, reviews contributions, protects project direction, and ensures the project remains maintainable.

### Goals

- Keep the project useful and safe.
- Review contributions efficiently.
- Maintain documentation and governance.
- Prepare for future implementation.

### Constraints

- Must avoid accepting unsafe examples or workflows.
- Must balance openness with humanitarian risk.

### Product Implications

- Contribution templates must ask about safety and privacy.
- Governance must define review expectations.
- Examples must remain fictional.

