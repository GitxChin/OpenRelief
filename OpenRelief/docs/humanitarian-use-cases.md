# Humanitarian Use Cases

OpenRelief focuses on practical NGO and volunteer workflows during disasters and public emergencies.

## User Roles

- **Help seeker**: a person affected by a disaster, or someone reporting on behalf of affected people.
- **Resource provider**: an individual, company, community group, or organization offering supplies, services, shelter, logistics, funds, or expertise.
- **Field volunteer**: a person providing local observations, verification, translation, mapping, or community support.
- **NGO coordinator**: a person reviewing incoming cases, assigning tasks, coordinating organizations, and preparing briefs.
- **Professional supporter**: medical, psychological, legal, logistics, or technical professionals who provide bounded support.
- **Maintainer**: a project steward responsible for system safety, privacy, and open-source collaboration.

## Use Case 1: Help Request Intake

A person submits a help request through a mini program or trusted form. OpenRelief structures the request, identifies location and needs, flags risk factors, and sends the case to human review.

Expected outputs:

- structured help request;
- urgency suggestion;
- needs categories;
- missing information checklist;
- review status;
- evidence and source record.

## Use Case 2: Field Information Reporting

A volunteer reports blocked roads, flooding, damaged buildings, supply shortages, or isolated communities. OpenRelief classifies the report, resolves location, detects duplicate reports, and adds it to the situation board.

Expected outputs:

- field report record;
- location confidence;
- HEINA tags;
- related cases;
- verification status.

## Use Case 3: Resource Offer Intake

A resource provider submits available supplies, shelter, transport, professional support, or technical capacity. OpenRelief structures the offer and makes it available for matching after review.

Expected outputs:

- resource record;
- quantity and availability;
- service area;
- constraints;
- contact visibility;
- review status.

## Use Case 4: Urgency Triage

Incoming records are screened for life-safety risk, vulnerable groups, hazards, and response constraints. AI can suggest urgency, but coordinators confirm final priority.

Expected outputs:

- urgency level;
- reason codes;
- confidence;
- required reviewer type;
- escalation recommendation.

## Use Case 5: Needs and Resource Matching

OpenRelief proposes potential matches between needs and available resources, volunteers, or organizations.

Expected outputs:

- candidate matches;
- match rationale;
- distance or service-area notes;
- constraints and missing information;
- human confirmation state.

## Use Case 6: Situation Brief Drafting

Coordinators draft disaster briefs using verified and partially verified records. AI can summarize patterns, but public release requires editorial approval.

Expected outputs:

- source-grounded brief draft;
- affected area summary;
- key needs;
- action updates;
- uncertainty notes;
- citations or source references.

## Non-Goals for the First Stage

OpenRelief should not initially attempt to:

- replace emergency dispatch;
- provide autonomous rescue routing;
- provide medical diagnosis;
- publish live personal help requests;
- process real sensitive data without a reviewed data protection plan;
- train models on private records without consent and anonymization.

