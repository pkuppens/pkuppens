---
name: v-model-requirements-acceptance
description: Pairs requirements and issue acceptance criteria with acceptance-level validation. Use when closing the top of the V for a feature or release slice. Third person.
---

# V-model: requirements ↔ acceptance

Links **left:** [requirements](../../requirements/SKILL.md) (**2.x**) and well-formed [issue-acceptance-criteria](../../issue-workflow/issue-acceptance-criteria/SKILL.md) with **right:** acceptance-oriented validation (**8.x**).

## When to use

- Defining or refining an issue so each AC maps to observable evidence.
- Preparing stakeholder demo, UAT, or audit evidence for “what we said we would deliver.”

## Instructions

1. Ensure acceptance criteria are **testable** (copy-pastable steps where possible).
2. For each AC, name the **validation** method: automated check, scripted test, manual checklist, or monitored metric.
3. Use [validation-draft](../../validation/validation-draft/SKILL.md) to derive scenarios; refine with [validation-detail](../../validation/validation-detail/SKILL.md) once behaviour is known.
4. If requirements docs exist (goals, constraints, scope from **2.x**), add explicit **forward references** from AC to those clauses where helpful.

## Pitfalls

- **Duplicate prose:** keep one canonical statement of intent; link instead of copying long specs into both issue and docs.
- **Mushy AC:** “works well” → replace with measurable or binary checks.

## Related

- [v-model-mapping](../v-model-mapping/SKILL.md)
- [issue-workflow](../../issue-workflow/SKILL.md)
