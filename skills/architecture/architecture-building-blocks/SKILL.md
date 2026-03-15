---
name: architecture-building-blocks
description: Documents static decomposition: hierarchy and black-box/white-box view of building blocks. Use when defining structure for a new system; produces arc42 §5 content.
---

# Architecture Building Blocks

Documents static structure: hierarchy, black-box and white-box views. Aligns with arc42 §5: building blocks, modules, components, packages.

## When to use

- Greenfield project — after solution strategy (Initial mode)
- Defining module/package hierarchy for a new system
- Refining structure after strategy is clear

## Instructions

1. **Use solution strategy** — read `docs/architecture/04-solution-strategy.md` if present.
2. **Define top-level building blocks** — black-box: name, responsibility, interface.
3. **Decompose as needed** — white-box view for each block: inner structure.
4. **Map to code structure** — align with package/module layout (e.g. `src/`, `backend/`, `frontend/`).
5. **Write to arc42 §5 format** — hierarchy, interfaces, responsibilities.

## Output format

Write or append to `docs/architecture/05-building-blocks.md`:

```markdown
# Building Blocks (arc42 §5)

## Level 1: System
[Black-box: system responsibility, interfaces to external actors]

## Level 2: Top-level building blocks
| Block | Responsibility | Interface |
|-------|----------------|-----------|
| [Block A] | [role] | [API / events] |
| [Block B] | [role] | [API / events] |

## White-box: [Block A]
[Inner structure: sub-blocks or modules]
```

## Component documentation (retrofitting)

When documenting *existing* components (from architecture-document-existing scan), create `docs/architecture/components/<name>.md` with: Purpose & responsibilities; Public interfaces (API, events, signatures); Dependencies; Data (schemas, tables); Runtime interactions; Errors/retries; Tests; Observability; Links to abstractions and ADRs. Component = concrete implementation (e.g. `WhisperService`); abstraction = conceptual boundary (e.g. "Transcription Provider").

## Abstraction documentation (retrofitting)

When documenting *existing* abstractions, create `docs/architecture/abstractions/<name>.md` with: Intent and scope; Contract (interfaces, invariants); Allowed implementations; Maturity state (Concrete/Abstract/Mixed/Missing/Proposed); Anti-corruption rules; Links to components. Prefer "protocol + vendor adapter" pattern.

## Integration

- Run after [architecture-solution-strategy](../architecture-solution-strategy/SKILL.md) in Initial mode.
- Component/abstraction docs: used when [architecture-document-existing](../architecture-document-existing/SKILL.md) delegates.
- Informs [architecture-consult](../architecture-consult/SKILL.md) for placement.
- Parent: [architecture](../SKILL.md) orchestrator.
