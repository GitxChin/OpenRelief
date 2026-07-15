# Resource Matching Prompt Specification

## Purpose

Suggest candidate matches between reviewed needs and available resources, organizations, or volunteers.

## Inputs

- reviewed help request;
- needs list;
- urgency level;
- location and service area;
- available resources;
- organization capabilities;
- volunteer capabilities;
- constraints;
- verification status.

## Required Output

For each candidate match:

- matched need;
- candidate resource or organization;
- match rationale;
- constraints;
- missing information;
- confidence;
- required human confirmation;
- suggested next contact step.

## Safety Rules

- Do not assign tasks automatically.
- Do not expose restricted contact information unnecessarily.
- Do not recommend unqualified volunteers for professional work.
- Do not match medical needs to non-medical responders unless the task is logistics or verification.
- Do not ignore location uncertainty.

