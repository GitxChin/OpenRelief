# OpenRelief

**AI-enabled disaster information for humanitarian action.**

OpenRelief is an open-source humanitarian technology project for NGOs, volunteer networks, community responders, and disaster information teams. It helps transform fragmented crisis information into structured, reviewable, privacy-aware records that support needs assessment, urgency triage, resource matching, and situation reporting.

OpenRelief builds on the practice of **[NCP Relief](https://weibo.com/u/6892480749)** and the disaster information service methodology inherited from **[Zhuoming Info Aid](https://news.un.org/zh/story/2023/08/1120742) (aka Zhuoming Disaster Information Center)**. The project also draws from research in disaster informatics, crisis computing, social media situation awareness, emergency message classification, and human-in-the-loop AI.

> OpenRelief does not replace emergency services, professional responders, medical judgment, or local command systems. It is designed as decision-support infrastructure: AI assists, humans decide.

This project was initiated by former core volunteers of NCP Relief and Zhuoming Info Aid.  
It has **no legal affiliation, employment, or leadership relationship** with those teams or their members.  
Any negative impact or legal responsibility arising from this project will be borne solely by the project initiators.

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
```