---
name: requirements-context-scope
description: Defines the system boundary, external actors, and interfaces in scope versus out of scope. Use when integrations are unclear or scope creep threatens the milestone.
---

# Requirements context and scope

Maps to **arc42 §3** — context and scope.

## When to use

- Multiple systems exchange data with your service
- “In scope / out of scope” fights in backlog grooming
- You need a context diagram for ADRs

## Instructions

1. **System under design** — one boundary (name it).
2. **External actors** — users, systems, schedulers; direction of data flow.
3. **Interfaces** — protocol, auth model, rough frequency/volume.
4. **In scope** — this release.
5. **Out of scope** — explicit deferrals (link issues).

## Output format

- Short narrative + bullet lists; optional mermaid `C4Context`-style description in prose

## Anti-patterns

- Boundary that includes “the whole enterprise” (unbounded work)
