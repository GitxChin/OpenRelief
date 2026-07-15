# Needs Classification Prompt Specification

## Purpose

Identify one or more humanitarian needs from a help request, resource request, or field report.

## Need Categories

- `rescue`
- `evacuation`
- `medical_support`
- `medicine_or_equipment`
- `food`
- `drinking_water`
- `shelter`
- `transport`
- `communication`
- `psychological_support`
- `field_verification`
- `care_support`
- `resource_coordination`
- `other`
- `unknown`

## Required Output

For each need:

- category;
- evidence phrase;
- severity;
- confidence;
- missing information;
- human review reason.

## Classification Principles

- Multi-label classification is expected.
- Prefer `unknown` when evidence is insufficient.
- Preserve evidence phrases from the source text when possible.
- Separate needs from hazards.
- Separate requests from resource offers.

## Human Review Triggers

- medical support;
- rescue or evacuation;
- vulnerable groups;
- unclear location;
- conflicting information;
- low confidence;
- public release requested.

