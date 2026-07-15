# Data Model

This document defines the conceptual data model for OpenRelief. It is not an implementation schema yet.

## Entity Overview

```text
HelpRequest
  ├── Need
  ├── Location
  ├── PersonGroup
  ├── Evidence
  ├── VerificationRecord
  ├── ConsentRecord
  └── AuditLog

ResourceOffer
  ├── Resource
  ├── Organization
  ├── Availability
  └── ReviewStatus

Task
  ├── HelpRequest
  ├── ResourceOffer
  ├── Volunteer
  ├── Organization
  ├── CommunicationLog
  └── AuditLog
```

## HelpRequest

Represents a request for help or a report of affected people.

Suggested fields:

- `id`
- `source_channel`
- `original_content`
- `submitted_at`
- `submitted_by_role`
- `contact_visibility`
- `affected_people_count`
- `vulnerable_groups`
- `location`
- `needs`
- `hazards`
- `urgency_level`
- `verification_status`
- `consent_status`
- `evidence`
- `audit_logs`

## Need

Represents a specific need extracted from a help request.

Suggested categories:

- rescue;
- medical support;
- medicine or medical equipment;
- food;
- drinking water;
- shelter;
- transport;
- evacuation;
- communication;
- psychological support;
- care for children, elderly people, pregnant people, people with disabilities, or patients;
- other.

## ResourceOffer

Represents available resources offered by individuals, communities, companies, NGOs, or partners.

Suggested fields:

- `id`
- `resource_type`
- `quantity`
- `availability_window`
- `service_area`
- `provider_type`
- `constraints`
- `contact_visibility`
- `review_status`

## Task

Represents a coordination action created from a reviewed request or match.

Suggested fields:

- `id`
- `task_type`
- `priority`
- `related_help_request_id`
- `assigned_organization_id`
- `assigned_volunteer_id`
- `required_capabilities`
- `status`
- `due_time`
- `handoff_notes`
- `communication_logs`
- `audit_logs`

## Evidence

Represents source material supporting an assessment.

Suggested fields:

- `id`
- `source_type`
- `source_url_or_reference`
- `captured_at`
- `description`
- `privacy_level`
- `verification_status`

## VerificationRecord

Tracks human verification.

Suggested fields:

- `id`
- `reviewer_role`
- `reviewed_at`
- `status`
- `method`
- `notes`
- `next_action`

## ConsentRecord

Tracks whether and how data may be used.

Suggested fields:

- `id`
- `scope`
- `granted_by`
- `granted_at`
- `expires_at`
- `withdrawn_at`
- `notes`

## AuditLog

Records who changed what and why.

Suggested fields:

- `id`
- `actor_role`
- `action`
- `target_type`
- `target_id`
- `timestamp`
- `reason`
- `metadata`

## Privacy Levels

- `public_safe`: safe to publish after review.
- `internal`: visible to project and partner reviewers.
- `restricted`: visible only to authorized coordinators.
- `sensitive`: requires special handling and minimal exposure.

