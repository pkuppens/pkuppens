---
name: architecture-decisions
description: Authors or updates Architecture Decision Records. Use when making or changing architecture decisions; produces arc42 §9 content and ADR files.
---

# Architecture Decisions

Authors or updates Architecture Decision Records (ADRs). Aligns with arc42 §9: decisions, context, options, consequences.

## When to use

- Evolving architecture — new decision or change to existing one
- Before major implementation — capture rationale
- When answering "which ADRs are in place?" or "why did we choose X?"

## Instructions

1. **Locate ADR directory** — `docs/architecture/adr/` (or `adr/` at project root).
2. **Check existing ADRs** — read index (`09-decisions.md` or `adr/README.md`) to avoid duplicates.
3. **Use ADR format** — context, decision, options considered, consequences.
4. **Number and title** — e.g. `001-use-async-first.md`, `002-sqlalchemy-20-style.md`.
5. **Update index** — add to `09-decisions.md` or ADR TOC.

## Output format

Create `docs/architecture/adr/NNN-title.md`:

```markdown
# ADR-NNN: [Decision Title]

**Status**: Proposed | Accepted | Deprecated | Superseded
**Date**: YYYY-MM-DD
**Deciders**: [Who made this decision]
**Related**: [Links to components, abstractions, other ADRs]

## Context and Problem Statement

What is the issue we're addressing? What factors do we need to consider?

## Decision Drivers

- Driver 1 (business/technical requirement)
- Driver 2 (constraint or quality attribute)

## Considered Options

1. Option A — [Brief description]
2. Option B — [Brief description]

## Decision Outcome

**Chosen option**: "Option A"

**Rationale**: Why we chose this over alternatives.

### Positive Consequences

- Pro 1

### Negative Consequences

- Con 1 (and mitigation)

## Pros and Cons of the Options

### Option A
- ✅ Pro 1
- ❌ Con 1

### Option B
- ✅ Pro 1
- ❌ Con 1
```

Update `docs/architecture/09-decisions.md`:

```markdown
- [ADR-NNN: Title](adr/NNN-title.md)
```

**Rules:**
- ADRs are immutable once accepted — supersede with a new ADR, don't edit
- Numbering: sequential `001-title.md`; check existing ADRs for next number
- After creating: update affected component/abstraction docs to reference this ADR; add to `00-system-architecture.md` ADR index

## Integration

- Evolving mode: run for new or changed decisions.
- [architecture-consult](../architecture-consult/SKILL.md) reads ADRs to surface constraints.
- Parent: [architecture](../SKILL.md) orchestrator.
