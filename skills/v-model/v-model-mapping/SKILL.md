---
name: v-model-mapping
description: Maps classic V-model stages to pkuppens SKILL_TREE skills 2–10. Use when explaining or applying V traceability alongside arc42 and Agile slices. Third person.
---

# V-model mapping

Relates **classic V-model** ideas to this repository’s skills. arc42 (**3.x**) is richer than a single classic V box; treat mapping as **many-to-many**, not a rigid 1:1.

## Classic left arm (decomposition) ↔ skills

| Classic stage (left) | Primary skills | Notes |
|---------------------|----------------|-------|
| Requirements / analysis | [requirements](../../requirements/SKILL.md) (**2.x**), [issue-acceptance-criteria](../../issue-workflow/issue-acceptance-criteria/SKILL.md) | AC often acts as the testable requirement for a slice. |
| High-level / system design | [architecture-solution-strategy](../../architecture/architecture-solution-strategy/SKILL.md), [architecture-building-blocks](../../architecture/architecture-building-blocks/SKILL.md), **3.x** | Spans several arc42 sections. |
| Detailed design | [design](../../design/SKILL.md) (**4.x**), [design-consult](../../design/design-consult/SKILL.md) | APIs, components, data shapes. |
| Implementation | [implementation](../../implementation/SKILL.md) (**7.x**) | Code construction and refactors. |

## Classic right arm (integration & verification) ↔ skills

| Classic stage (right) | Primary skills | Notes |
|----------------------|----------------|-------|
| Unit / component test | [test-write](../../test/test-write/SKILL.md) (**9.1**), [validation-detail](../../validation/validation-detail/SKILL.md) | Closest to module-level V leg. |
| Integration test | **9.x**, **8.x**, [architecture-runtime](../../architecture/architecture-runtime/SKILL.md) (behaviour to assert) | Scenarios drive what to integrate-test. |
| System test | **8.3** [validation-run](../../validation/validation-run/SKILL.md), **9.2** | Full stack or system slice. |
| Acceptance | **8.x**, issue AC | Stakeholder-facing evidence; may be manual or automated. |

## Quality automation

[quality-gate](../../quality-gate/SKILL.md) (**10.x**) supports the right arm continuously (lint, type, security) but does not replace domain tests.

## Next steps

- For pairing guidance at each level, use the other **v-model-*** sub-skills under [v-model](../SKILL.md).
- For existing codebases, use [v-model-retrofit](../v-model-retrofit/SKILL.md).
