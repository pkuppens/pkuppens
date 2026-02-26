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
# ADR-NNN: [Title]

## Context
[What situation or problem motivates this decision?]

## Decision
[The decision in one sentence.]

## Options considered
- **Option A**: [pros/cons]
- **Option B**: [pros/cons]

## Consequences
- [Positive consequence]
- [Negative consequence or trade-off]
```

Update `docs/architecture/09-decisions.md`:

```markdown
- [ADR-NNN: Title](adr/NNN-title.md)
```

## Integration

- Evolving mode: run for new or changed decisions.
- [architecture-consult](../architecture-consult/SKILL.md) reads ADRs to surface constraints.
- Parent: [architecture](../SKILL.md) orchestrator.
