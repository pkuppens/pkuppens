---
name: v-model
description: Maps V-model traceability to the skill tree (requirements through tests). Use when pairing left-arm artefacts with right-arm verification, Agile mini-V per issue, brownfield retrofit, or compliance-style evidence. Third person.
---

# V-model (process overlay)

Optional overlay on skills **2–15**: pair **what we specify and build** with **how we verify** it. Does **not** replace the numbered lifecycle; it routes you to the right sub-skills.

## When to use

- Need traceability from acceptance criteria or requirements down to tests (or the reverse).
- Regulated, audited, or high-assurance context where **traceability** between artefacts and verification matters.
- Teaching or refining workflow in **Agile**: each backlog item can run a **mini-V** (vertical slice).
- **Brownfield:** code exists without a closed V; see [v-model-retrofit](v-model-retrofit/SKILL.md).

## When not to default to greenfield

If the codebase already exists, **do not** assume the user wants full upfront requirements for the whole system. Prefer **Retrofitting** architecture mode plus **touch-driven** retrofit unless an issue says otherwise.

## Sub-skills (use in order as needed)

| Sub-skill | Role |
|-----------|------|
| [v-model-mapping](v-model-mapping/SKILL.md) | Classic V ↔ SKILL_TREE; many-to-many with arc42 |
| [v-model-requirements-acceptance](v-model-requirements-acceptance/SKILL.md) | 2.x + AC ↔ acceptance validation |
| [v-model-architecture-integration](v-model-architecture-integration/SKILL.md) | 3.x ↔ integration / structural verification |
| [v-model-design-verification](v-model-design-verification/SKILL.md) | 4.x ↔ component / contract verification |
| [v-model-implementation-unit](v-model-implementation-unit/SKILL.md) | 7.x ↔ unit tests |
| [v-model-retrofit](v-model-retrofit/SKILL.md) | Explicit backfill vs incremental on touched code |

## Agile and shift-left

- **Incremental V:** one issue = one slice; complete the mapping for that slice.
- **Shift-left:** [validation-draft](../validation/validation-draft/SKILL.md) and tests may precede stable specs for that slice (same idea as TDD in [COOPERATION.md](../COOPERATION.md)).
- **CI:** [quality-gate](../quality-gate/SKILL.md) automates parts of the lower right arm continuously.

## Human vs AI

See [_meta/human-ai-execution.md](../_meta/human-ai-execution.md). Interpreting “intent” of legacy code as requirements is usually **human-review** or **human-required**.

## Integration

- Issues: [issue-workflow](../issue-workflow/SKILL.md), [issue-acceptance-criteria](../issue-workflow/issue-acceptance-criteria/SKILL.md).
- Planning: [plan](../plan/SKILL.md).
- Composition: [COOPERATION.md](../COOPERATION.md) V-model section.
