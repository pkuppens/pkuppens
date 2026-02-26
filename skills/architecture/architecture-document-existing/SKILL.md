---
name: architecture-document-existing
description: Infers and documents architecture from an existing codebase. Use when the codebase has no or minimal architecture docs; produces arc42-aligned documentation.
---

# Architecture Document Existing

Infers and documents architecture from an existing codebase. Use when structure exists in code but docs are missing (Retrofitting mode).

## When to use

- Undocumented codebase — need to understand and document structure
- Reverse-engineering for onboarding or maintenance
- Before major refactor — baseline documentation first

## Instructions

1. **Scan codebase** — use file tree, `rg`, module imports to identify top-level structure.
2. **Identify layers and modules** — backend/frontend, packages, entry points.
3. **Map dependencies** — which modules import which; data flow.
4. **Infer building blocks** — from package layout and naming.
5. **Produce arc42-aligned docs** — start with §4 (solution strategy), §5 (building blocks), §9 (decisions if ADRs can be inferred).
6. **Create `docs/architecture/`** — if missing, create directory and write inferred sections.

## Output format

Create or update:

- `docs/architecture/04-solution-strategy.md` — inferred from code patterns
- `docs/architecture/05-building-blocks.md` — from package/module structure
- `docs/architecture/adr/` — optional inferred decisions

```markdown
# Building Blocks (arc42 §5) — Inferred

## Inferred structure
[From package layout, imports, entry points]

| Path | Responsibility (inferred) |
|------|---------------------------|
| `src/backend/` | [inferred from structure] |
| `src/frontend/` | [inferred from structure] |
```

## Integration

- Retrofitting mode: primary sub-skill.
- Can be followed by [architecture-consult](../architecture-consult/SKILL.md) to refine.
- Parent: [architecture](../SKILL.md) orchestrator.
