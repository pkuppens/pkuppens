---
name: requirements-capture
description: Records functional and non-functional requirements from stakeholders or issue text. Use when starting a feature, migrating notes into structured requirements, or clarifying vague asks.
---

# Requirements capture

Turns **raw input** into structured requirement statements.

## When to use

- New issue or doc lacks testable statements
- Stakeholder interview notes need normalization
- You inherit a ticket with only a title

## Instructions

1. **Sources** — list people, docs, tickets, screenshots (no PII in shared text).
2. **Functional** — “The system shall …” per capability (verbs + objects).
3. **Non-functional** — performance, security, accessibility, availability (measurable where possible).
4. **Assumptions and unknowns** — explicit list.
5. **IDs** — stable labels (REQ-001…) if the project uses them.

## Output format

- Table or list: ID, statement, source, priority (if known)

## Anti-patterns

- Mixing solution design into requirements (“use Redis”) unless it is a hard constraint
