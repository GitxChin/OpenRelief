# Project Background

OpenRelief is the next-stage open-source effort of a humanitarian relief initiative formerly known as NCP Relief.

## From NCP Relief to OpenRelief

NCP Relief developed experience in online support, help intake, volunteer coordination, medical and community assistance, and public-facing response workflows. OpenRelief aims to preserve this practical experience while building a more open, reusable, AI-assisted infrastructure for humanitarian response.

## Relationship to Zhuoming Info Aid

Much of the team's experience and methodology comes from Zhuoming Info Aid. Zhuoming's disaster information service practice emphasizes:

- collecting fragmented disaster information;
- verifying and structuring reports;
- producing situation assessments and briefs;
- mapping affected areas and needs;
- coordinating volunteers and social resources;
- supporting better decisions by NGOs and responders.

OpenRelief should treat this as a methodological foundation rather than only historical background.

## Existing Mini-Program Practice

The existing emergency help mini-program provides an important product foundation. Current screenshots show workflows including:

- emergency help platform homepage;
- information mutual-aid map;
- "I need help" intake;
- "I can help" resource and field information intake;
- rescue organization information;
- disaster briefs;
- key affected areas;
- social force statistics dashboard;
- about and contact flows.

The help request form already captures many fields that map directly into OpenRelief's AI workflow:

- requester name and contact;
- affected people count;
- affected person contact;
- affected person situation;
- request details;
- location;
- building condition;
- local landmarks and site features;
- water depth, traffic disruption, and building damage;
- surrounding affected people;
- site photos;
- request channel;
- other feedback.

## Product Direction

OpenRelief should not start from a blank product idea. It should evolve from existing field-tested workflows into:

- a public intake layer;
- an AI-assisted structuring and triage layer;
- a human review and verification layer;
- a coordinator workspace;
- a resource matching layer;
- a situation awareness and briefing layer;
- an audit, privacy, and safety layer.

## First Version Constraint

The current repository stage is framework-only. It documents mission, architecture, safety, research foundations, AI workflow specifications, evaluation cases, examples, and collaboration templates. Application code is intentionally deferred.

## Humanitarian Use Cases

OpenRelief focuses on practical NGO and volunteer workflows during disasters and public emergencies.

### User Roles

- **Help seeker**: a person affected by a disaster, or someone reporting on behalf of affected people.
- **Resource provider**: an individual, company, community group, or organization offering supplies, services, shelter, logistics, funds, or expertise.
- **Field volunteer**: a person providing local observations, verification, translation, mapping, or community support.
- **NGO coordinator**: a person reviewing incoming cases, assigning tasks, coordinating organizations, and preparing briefs.
- **Professional supporter**: medical, psychological, legal, logistics, or technical professionals who provide bounded support.
- **Maintainer**: a project steward responsible for system safety, privacy, and open-source collaboration.

### Help Request Intake

A person submits a help request through a mini program or trusted form. OpenRelief structures the request, identifies location and needs, flags risk factors, and sends the case to human review.

Expected outputs:

- structured help request;
- urgency suggestion;
- needs categories;
- missing information checklist;
- review status;
- evidence and source record.

### Field Information Reporting

A volunteer reports blocked roads, flooding, damaged buildings, supply shortages, or isolated communities. OpenRelief classifies the report, resolves location, detects duplicate reports, and adds it to the situation board.

Expected outputs:

- field report record;
- location confidence;
- HEINA tags;
- related cases;
- verification status.

### Resource Offer Intake

A resource provider submits available supplies, shelter, transport, professional support, or technical capacity. OpenRelief structures the offer and makes it available for matching after review.

Expected outputs:

- resource record;
- quantity and availability;
- service area;
- constraints;
- contact visibility;
- review status.

### Urgency Triage

Incoming records are screened for life-safety risk, vulnerable groups, hazards, and response constraints. AI can suggest urgency, but coordinators confirm final priority.

Expected outputs:

- urgency level;
- reason codes;
- confidence;
- required reviewer type;
- escalation recommendation.

### Needs and Resource Matching

OpenRelief proposes potential matches between needs and available resources, volunteers, or organizations.

Expected outputs:

- candidate matches;
- match rationale;
- distance or service-area notes;
- constraints and missing information;
- human confirmation state.

### Situation Brief Drafting

Coordinators draft disaster briefs using verified and partially verified records. AI can summarize patterns, but public release requires editorial approval.

Expected outputs:

- source-grounded brief draft;
- affected area summary;
- key needs;
- action updates;
- uncertainty notes;
- citations or source references.

### First-Stage Non-Goals

OpenRelief should not initially attempt to:

- replace emergency dispatch;
- provide autonomous rescue routing;
- provide medical diagnosis;
- publish live personal help requests;
- process real sensitive data without a reviewed data protection plan;
- train models on private records without consent and anonymization.
