# OpenRelief

**Turning disaster information into response insights with AI.**

OpenRelief is an open-source humanitarian technology project for NGOs, volunteer networks, community responders, and disaster information teams. It turns fragmented crisis information into structured, reviewable, privacy-aware records for needs assessment, urgency triage, resource matching, and situation reporting.

OpenRelief builds on the practice of **[NCP Relief](https://weibo.com/u/6892480749)** and the disaster information service methodology inherited from **[Zhuoming Info Aid](https://news.un.org/zh/story/2023/08/1120742)**. It also draws from research in disaster informatics, crisis computing, situation awareness, emergency message classification, and human-in-the-loop AI.

> OpenRelief does not replace emergency services, professional responders, medical judgment, or local command systems. AI assists; humans decide.
>
> This project was initiated by former core volunteers of NCP Relief and Zhuoming Info Aid. It has no legal affiliation, employment, or leadership relationship with those teams or their members. Any negative impact or legal responsibility arising from this project will be borne solely by the project initiators.

## What OpenRelief Does

```text
Intake
  → AI-assisted structuring
  → Needs classification and urgency triage
  → Human review
  → Resource matching or escalation
  → Task follow-up
  → Situation briefs
  → Audit and learning
```

Core capabilities include:

- structuring help requests, field reports, and resource offers;
- identifying needs, hazards, locations, evidence, and missing information;
- surfacing possible life-safety cases for human review;
- suggesting matches between reviewed needs and available resources;
- drafting source-grounded situation briefs for human editors;
- preserving consent, provenance, review status, and audit history.

## Current Stage

OpenRelief is currently in the **product definition and repository foundation stage**. The repository contains product requirements, system architecture, AI specifications, safety policies, fictional examples, and evaluation cases.

Application code will be added in the next implementation stage after the current product and safety specifications are reviewed.

## Repository Structure

```text
OpenRelief/
├── docs/                 # Project, product, architecture, safety, and volunteer documentation
├── ai-specs/             # AI prompts, policies, and evaluation specifications
├── examples/             # Fictional workflow and structured-data examples
├── .github/              # GitHub contribution templates
└── standard project and community files
```

Future deployable code will live under `applications/`. Code shared by multiple applications will live under `shared/`. These directories will be created with the first implementation rather than filled with placeholders.

## Documentation

Start with the [documentation index](docs/README.md), or go directly to:

- [Project Overview and Humanitarian Use Cases](docs/project-overview.md)
- [Product Requirements](docs/product/requirements.md)
- [MVP Scope and Acceptance Criteria](docs/product/mvp.md)
- [Personas](docs/product/personas.md)
- [User Journeys and Workflows](docs/product/user-workflows.md)
- [Architecture](docs/architecture/overview.md)
- [Data Model](docs/architecture/data-model.md)
- [AI Workflows](docs/architecture/ai-workflows.md)
- [Safety, Privacy, and Ethics](docs/safety/principles.md)
- [Threat Model](docs/safety/threat-model.md)
- [Research Foundations](docs/research-foundations.md)
- [Volunteering](docs/volunteering.md)

## AI Specifications

- [AI Output Policy](ai-specs/policies/ai-output-policy.md)
- [Human-in-the-Loop Policy](ai-specs/policies/human-in-the-loop.md)
- [Escalation Rules](ai-specs/policies/escalation-rules.md)
- [Evaluation Guide](ai-specs/evaluations/README.md)
- [Evaluation Scoring Rubric](ai-specs/evaluations/scoring-rubric.md)

High-risk AI outputs remain suggestions until reviewed by an authorized human. Medical, rescue, legal, protection, public reporting, and security-sensitive decisions require appropriate human review.

## Examples

All public examples are fictional:

- [Sample Help Request](examples/sample-help-request.json)
- [Sample Resource Offer](examples/sample-resource-offer.json)
- [Demo Relief Workflow](examples/demo-relief-workflow.md)

Do not upload real names, phone numbers, addresses, medical records, private chat logs, credentials, or sensitive operational information.

## Contributing

OpenRelief welcomes NGO practitioners, disaster information workers, emergency managers, digital volunteers, researchers, designers, engineers, translators, and safety reviewers.

Before contributing, read:

- [Volunteering Guide](docs/volunteering.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)

## Roadmap and License

See [ROADMAP.md](ROADMAP.md) for planned phases. OpenRelief is licensed under the [Apache License 2.0](LICENSE).
