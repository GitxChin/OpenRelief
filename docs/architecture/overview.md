# Architecture

OpenRelief is designed as a humanitarian information-to-action system. Its purpose is to help NGOs and volunteer teams receive fragmented disaster information, structure it, verify it, prioritize it, match it with resources, and produce accountable operational outputs.

## Design Goals

- Support existing public intake channels, including the current emergency help mini-program workflow.
- Preserve the disaster information service logic inherited from NCP Relief and Zhuoming Info Aid.
- Use AI for structuring, classification, summarization, matching, and drafting.
- Keep human review mandatory for high-risk decisions.
- Track provenance, verification status, consent, and audit history.
- Avoid building a heavy application before workflows and safety policies are clear.

## System Layers

```text
Public and Partner Inputs
        ↓
Data Intake Layer
        ↓
Structuring and Normalization
        ↓
AI-Assisted Analysis
        ↓
Human Review Queue
        ↓
Coordination Workspace
        ↓
Maps, Briefs, Tasks, Partner Handoffs
```

## Core Components

### Data Intake Layer

Receives information from:

- mini-program help requests;
- resource offer forms;
- field volunteer reports;
- public social media posts;
- partner NGO updates;
- official notices, weather, hydrology, and traffic sources.

The intake layer should preserve the original text, timestamp, source, channel, attachments, and consent state.

### Structuring and Normalization

Converts raw inputs into structured records:

- requester and contact visibility;
- affected location;
- people count;
- vulnerable groups;
- needs;
- hazards;
- photos or evidence;
- verification status;
- duplicate candidates.

### AI-Assisted Analysis

AI modules provide decision support:

- help request structuring;
- relevance filtering;
- needs classification;
- urgency triage;
- HEINA-style situation structuring;
- location mention extraction;
- duplicate and cluster suggestions;
- resource matching;
- situation brief drafting.

AI outputs must include confidence, reasoning signals, uncertainty, and review requirements.

### Human Review Queue

Human reviewers confirm or correct:

- whether a record is real and relevant;
- whether it is urgent;
- whether the location is usable;
- whether contact is possible;
- whether the case should be escalated;
- whether public publication is safe.

### Coordination Workspace

Future application surfaces should support:

- incoming case list;
- triage queue;
- map view;
- resource inventory;
- organization and volunteer directory;
- task assignment;
- communication logs;
- evidence and audit trail;
- briefing editor.

### Output Layer

Outputs may include:

- internal task boards;
- priority lists;
- situation maps;
- verified resource gaps;
- partner handoff packages;
- disaster assessment briefs;
- public-safe dashboards.

## HEINA Alignment

OpenRelief can use HEINA as a high-level disaster information structure:

- **H - Hazard**: disaster type and triggering hazard.
- **E - Exposure and environment**: affected population, infrastructure, geography, weather, and surrounding conditions.
- **I - Impact**: damage, casualties, disruption, displacement, and service interruption.
- **N - Needs**: rescue, medical, shelter, water, food, transport, psychological support, and other needs.
- **A - Actions**: government, NGO, volunteer, community, and resource-provider actions.

## Safety Boundary

OpenRelief must not automatically:

- dispatch rescue teams;
- issue medical instructions;
- publish personally identifiable help requests;
- release unverified situation reports;
- override local command or partner protocols;
- expose sensitive locations or contact details.

## First Repository Scope

This first repository stage contains documentation, policies, prompts, evaluation cases, examples, and GitHub collaboration templates. Application code is intentionally deferred.

