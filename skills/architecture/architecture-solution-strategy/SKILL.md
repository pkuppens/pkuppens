---
name: architecture-solution-strategy
description: Documents core ideas, fundamental decisions, and solution approaches for a new system. Use when starting a greenfield project; produces arc42 §4 content.
---

# Architecture Solution Strategy

Documents the solution strategy before structure. Aligns with arc42 §4: core ideas, fundamental decisions, and solution approaches.

## When to use

- Greenfield project — architecture from scratch (Initial mode)
- Before defining building blocks — strategy before structure
- When summarizing existing ADRs into a coherent strategy

## Instructions

1. **Gather context** — goals (arc42 §1), constraints (§2), context and scope (§3). Read `docs/architecture/01-introduction-and-goals.md` if present.
2. **Identify core ideas** — main architectural concepts (e.g. layered, event-driven, microservices).
3. **Document solution approach** — how the system will achieve its goals; key technology choices.
4. **Capture fundamental decisions** — decisions that affect the whole system; reference ADRs if they exist.
5. **Write to arc42 §4 format** — clear, concise; suitable for AI and human readers.

## Output format

Write or append to `docs/architecture/04-solution-strategy.md`:

```markdown
# Solution Strategy (arc42 §4)

## Core ideas
- [Main architectural concept 1]
- [Main architectural concept 2]

## Solution approach
[Paragraph: how the system achieves its goals]

## Fundamental decisions
- [Decision 1]: [rationale]
- [Decision 2]: [rationale]
```

## Integration

- Run before [architecture-building-blocks](../architecture-building-blocks/SKILL.md) in Initial mode.
- Can pull from existing [architecture-decisions](../architecture-decisions/SKILL.md) (ADRs) if present.
- Parent: [architecture](../SKILL.md) orchestrator.
