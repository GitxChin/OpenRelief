# OpenRelief

OpenRelief is an open-source humanitarian relief coordination project for NGOs, volunteer networks, and community responders. It builds on the field experience of [NCP Relief](https://weibo.com/u/6892480749) and the disaster information service methodology inherited from [Zhuoming Info Aid](https://news.un.org/zh/story/2023/08/1120742) (aka Zhuoming Disaster Information Center), with the goal of using AI to improve disaster information processing, needs triage, resource matching, and collaborative response.

OpenRelief is not intended to replace emergency services, professional responders, medical judgment, or local command systems. It is designed as human-in-the-loop infrastructure: AI helps structure, classify, summarize, prioritize, and route information, while high-risk decisions remain under human review.

## Current Stage

This repository is in the foundation stage. The first version focuses on project governance, humanitarian principles, research foundations, safety policies, data models, prompt specifications, evaluation cases, and examples. Application code will be added only after the product scope and implementation plan are reviewed.

## Why OpenRelief

During disasters, people ask for help through many fragmented channels: mini programs, social media, messaging apps, phone calls, public posts, local volunteers, community organizations, and NGOs. Relief teams need to turn these noisy signals into verified, actionable information:

- Who needs help?
- Where are they?
- What happened?
- What is urgent?
- What resources are available?
- Who can verify or respond?
- What evidence supports this assessment?

OpenRelief aims to provide a transparent, auditable, privacy-aware workflow for this process.

## Core Capabilities

- **Information intake**: collect help requests, field reports, resource offers, and volunteer updates.
- **AI-assisted structuring**: convert unstructured text into structured relief records.
- **Needs classification**: identify medical, shelter, food, water, transport, rescue, psychological support, and other needs.
- **Urgency triage**: flag life-threatening and high-priority cases for human review.
- **Situation awareness**: organize reports by location, time, disaster type, affected groups, and evolving topics.
- **Resource matching**: match requests with available organizations, volunteers, supplies, and services.
- **Briefing support**: draft situation briefs with source attribution and verification status.
- **Safety and audit**: preserve provenance, consent, review status, and operational accountability.

## Repository Structure

```text
OpenRelief/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── GOVERNANCE.md
├── ROADMAP.md
├── CHANGELOG.md
├── docs/
│   ├── architecture.md
│   ├── research-foundations.md
│   ├── humanitarian-use-cases.md
│   ├── data-model.md
│   ├── ai-workflows.md
│   ├── safety-privacy-and-ethics.md
│   ├── threat-model.md
│   └── volunteer-operations.md
├── product/
│   ├── prd.md
│   ├── mvp-scope.md
│   ├── personas.md
│   ├── user-journeys.md
│   ├── workflows.md
│   └── acceptance-criteria.md
├── ai/
│   ├── prompts/
│   ├── policies/
│   └── evals/
├── examples/
└── .github/
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

## Documentation

- Product Definition
  - [Product Requirements](product/prd.md)
  - [MVP Scope](product/mvp-scope.md)
  - [Personas](product/personas.md)
  - [User Journeys](product/user-journeys.md)
  - [Product Workflows](product/workflows.md)
  - [Acceptance Criteria](product/acceptance-criteria.md)
- [Architecture](docs/architecture.md)
- [Project Background](docs/project-background.md)
- [Research Foundations and Acknowledgements](docs/research-foundations.md)
- [Humanitarian Use Cases](docs/humanitarian-use-cases.md)
- [Data Model](docs/data-model.md)
- [AI Workflows](docs/ai-workflows.md)
- [Safety, Privacy, and Ethics](docs/safety-privacy-and-ethics.md)
- [Threat Model](docs/threat-model.md)
- [Volunteer Operations](docs/volunteer-operations.md)

## Human-in-the-Loop Principle

AI outputs in OpenRelief must be treated as decision support, not final authority. The following actions require human review:

- life-safety urgency classification;
- medical, rescue, legal, or security-sensitive suggestions;
- public release of situation reports;
- volunteer or organization task assignment for high-risk cases;
- handling of personally identifiable or sensitive information;
- escalation to external partners or authorities.

## Research Foundations

OpenRelief is informed by prior work in disaster informatics, crisis computing, AI-assisted disaster response, social media situation awareness, emergency message classification, and automated reporting. See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) and [docs/research-foundations.md](docs/research-foundations.md) for acknowledgements and references.

## Contributing

OpenRelief welcomes contributions from NGO practitioners, emergency managers, digital volunteers, researchers, designers, engineers, translators, and safety reviewers. Please read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md) before contributing.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
