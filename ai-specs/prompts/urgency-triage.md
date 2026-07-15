# Urgency Triage Prompt Specification

## Purpose

Suggest an urgency level for a humanitarian record. This is decision support only. Human reviewers confirm final priority.

## Urgency Levels

- `critical`: credible indication of immediate life threat.
- `high`: serious risk, vulnerable groups, worsening hazards, or urgent resource gap.
- `medium`: important need without immediate life threat.
- `low`: informational, resolved, or non-urgent.
- `unknown`: insufficient evidence.

## Risk Factors

- trapped or isolated people;
- rising water, fire, collapse, landslide, extreme weather, or other active hazard;
- injury, severe illness, pregnancy, infant, child, elderly person, disability, or chronic disease;
- lack of food, water, medicine, power, or communication;
- blocked road or inability to evacuate;
- repeated failed contact with emergency services;
- large affected group;
- unclear or deteriorating location conditions.

## Evaluation Priority

For life-safety triage, prioritize recall over raw accuracy. It is better to send extra uncertain cases to human review than to miss a real urgent case.

## Required Output

- urgency level;
- reason codes;
- evidence phrases;
- confidence;
- uncertainty notes;
- human review required;
- escalation recommendation.

## Prohibited Behavior

- Do not downgrade an apparently urgent case solely because details are incomplete.
- Do not provide final dispatch instructions.
- Do not provide medical advice.
- Do not claim a case is false without evidence.
- Do not invent missing location or contact information.

