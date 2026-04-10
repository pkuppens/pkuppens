---
name: design-component-boundaries
description: Defines module, package, and file boundaries so each unit has a single responsibility. Use when splitting a monolith, drawing C4 container boundaries, or stopping circular dependencies.
---

# Design component boundaries

**Detailed design** (not arc42 §5 alone — align with [architecture-building-blocks](../../architecture/architecture-building-blocks/SKILL.md)).

## When to use

- New feature spans multiple packages
- Imports are tangled; tests are slow because of coupling
- You need a DDD bounded context or module graph

## Instructions

1. **Name components** and their public responsibility (one sentence each).
2. **Allowed dependencies** — direction only (A → B allowed; B → A not).
3. **Data ownership** — which component owns which entities.
4. **Interfaces** — link to [design-interfaces](../design-interfaces/SKILL.md) for contracts.
5. **Check** against [design-consult](../design-consult/SKILL.md) placement.

## Output format

- Diagram or bullet list: component → depends on → owns data …

## Examples

**Positive (clear boundaries):**

- `Billing` owns `Invoice`, `Payment`; `Billing` depends on `Auth` for `UserId` only; `Auth` does not import `Billing`. Dependencies point **inward** toward domain core; no cycles.
- Stated rule: “`notifications` may call `users` for email lookup; `users` never calls `notifications`.”

**Negative (avoid):**

- Two packages import each other “just for one helper” — creates a cycle and hides ownership of data.
- “`utils`” grows to hold domain logic from three features — no single responsibility; boundaries collapsed.

## Anti-patterns

- Boundaries that mirror org chart only (may be wrong for the domain)
