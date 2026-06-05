# OpenRelief

**Human-centered AI infrastructure for disaster relief coordination.**

OpenRelief is an open-source humanitarian technology project for NGOs, volunteer networks, community responders, and disaster information teams. It helps transform fragmented crisis information into structured, reviewable, privacy-aware records that support needs assessment, urgency triage, resource matching, and situation reporting.

OpenRelief builds on the practice of **[NCP Relief](https://weibo.com/u/6892480749)** and the disaster information service methodology inherited from **[Zhuoming Info Aid](https://news.un.org/zh/story/2023/08/1120742) (aka Zhuoming Disaster Information Center)**. The project also draws from research in disaster informatics, crisis computing, social media situation awareness, emergency message classification, and human-in-the-loop AI.

> OpenRelief does not replace emergency services, professional responders, medical judgment, or local command systems. It is designed as decision-support infrastructure: AI assists, humans decide.

## Why OpenRelief

During disasters, affected people and local communities often ask for help through fragmented channels: mini programs, social media, messaging groups, phone calls, public posts, volunteers, community organizations, and NGOs.

Relief teams need to quickly answer:

- Who needs help?
- Where are they?
- What happened?
- What is urgent?
- What resources are available?
- Who can verify or respond?
- What evidence supports the assessment?

OpenRelief aims to make this process more structured, accountable, and safe.

## What OpenRelief Does

OpenRelief is designed around an information-to-action workflow:

```text
Intake
  -> AI-assisted structuring
  -> Needs classification
  -> Urgency triage
  -> Human review
  -> Resource matching
  -> Task follow-up
  -> Situation briefs
  -> Audit and learning
```

Core capabilities include:

- **Help request structuring**: convert unstructured reports into standard humanitarian records.
- **Needs classification**: identify rescue, evacuation, medical, shelter, food, water, transport, communication, psychological support, and care needs.
- **Urgency triage**: surface possible life-safety cases for human review.
- **Situation awareness**: organize reports by location, time, hazard, impact, needs, and actions.
- **Resource matching**: suggest possible matches between needs, resources, volunteers, and organizations.
- **Brief drafting**: generate source-grounded situation report drafts for human editors.
- **Privacy and audit**: preserve consent, provenance, review status, and operational accountability.

## Current Stage

OpenRelief is currently in the **repository foundation and product definition stage**.

This repository now focuses on:

- project mission and governance;
- product requirements and MVP scope;
- humanitarian workflows;
- AI prompt and policy specifications;
- safety, privacy, and threat modeling;
- fictional examples and evaluation cases;
- GitHub collaboration templates.

Application code is intentionally deferred until the product scope and implementation plan are reviewed.

## Repository Map

```text
OpenRelief/
├── README.md
├── ACKNOWLEDGEMENTS.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── GOVERNANCE.md
├── ROADMAP.md
├── CHANGELOG.md
├── product/
│   ├── prd.md
│   ├── mvp-scope.md
│   ├── personas.md
│   ├── user-journeys.md
│   ├── workflows.md
│   └── acceptance-criteria.md
├── docs/
│   ├── project-background.md
│   ├── architecture.md
│   ├── research-foundations.md
│   ├── humanitarian-use-cases.md
│   ├── data-model.md
│   ├── ai-workflows.md
│   ├── safety-privacy-and-ethics.md
│   ├── threat-model.md
│   └── volunteer-operations.md
├── ai/
│   ├── prompts/
│   ├── policies/
│   └── evals/
├── examples/
└── .github/
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

## Product Documents

- [Product Requirements](product/prd.md)
- [MVP Scope](product/mvp-scope.md)
- [Personas](product/personas.md)
- [User Journeys](product/user-journeys.md)
- [Workflows](product/workflows.md)
- [Acceptance Criteria](product/acceptance-criteria.md)

## Technical and Operational Documents

- [Project Background](docs/project-background.md)
- [Architecture](docs/architecture.md)
- [Humanitarian Use Cases](docs/humanitarian-use-cases.md)
- [Data Model](docs/data-model.md)
- [AI Workflows](docs/ai-workflows.md)
- [Safety, Privacy, and Ethics](docs/safety-privacy-and-ethics.md)
- [Threat Model](docs/threat-model.md)
- [Volunteer Operations](docs/volunteer-operations.md)

## AI Safety Principles

OpenRelief follows a human-in-the-loop approach:

- AI suggestions are not final decisions.
- Critical and high-risk cases require human review.
- Medical, rescue, legal, and security-sensitive outputs require expert or coordinator review.
- Public reports must be source-grounded and edited by humans.
- Personal data and precise sensitive locations must be protected.
- Urgency triage should prioritize recall for life-safety cases.

See:

- [AI Output Policy](ai/policies/ai-output-policy.md)
- [Human-in-the-Loop Policy](ai/policies/human-in-the-loop.md)
- [Escalation Rules](ai/policies/escalation-rules.md)

## Research Foundations

OpenRelief acknowledges prior work in AI for disaster response, social media crisis analysis, situation awareness, emergency message classification, rescue scheduling, and automated disaster reporting.

See:

- [Acknowledgements](ACKNOWLEDGEMENTS.md)
- [Research Foundations](docs/research-foundations.md)

## Example Data

All public examples in this repository are fictional.

- [Sample Help Request](examples/sample-help-request.json)
- [Sample Resource Offer](examples/sample-resource-offer.json)
- [Demo Relief Workflow](examples/demo-relief-workflow.md)

Do not upload real names, phone numbers, addresses, medical records, private chat logs, or sensitive operational information.

## Contributing

OpenRelief welcomes contributions from NGO practitioners, disaster information workers, emergency managers, digital volunteers, researchers, designers, engineers, translators, and safety reviewers.

Before contributing, please read:

- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)

## Roadmap

See [ROADMAP.md](ROADMAP.md).

The current focus is repository foundation and product definition. Future work will move toward implementation only after the MVP scope, safety boundaries, and implementation plan are reviewed.

## License

OpenRelief is licensed under the [Apache License 2.0](LICENSE).

