---
name: software-engineering-process
description: Orchestrates the full software lifecycle from ideation through operations and governance. Use when starting ambiguous work and you must pick the right phase skills in order, or when explaining how skills chain from issue to production.
---

# Software engineering process (Level 0)

Entry orchestrator for the lifecycle in [SKILL_TREE.md](../SKILL_TREE.md). It does not replace domain skills; it **routes** to them.

## When to use

- A request spans multiple phases (idea → issue → plan → code → ship → run)
- You need a default order of invocation before diving into one skill
- Onboarding: show how 0–15 map to arc42 and delivery

## Default flow (happy path)

1. **Shape the problem** — [ideation](../ideation/SKILL.md) (optional), then [issue-workflow](../issue-workflow/SKILL.md) so work is tracked with acceptance criteria.
2. **Plan** — [plan](../plan/SKILL.md) (branch strategy, tasks, dependencies).
3. **Design** — [architecture](../architecture/SKILL.md) and [design](../design/SKILL.md) as needed for the change size.
4. **Build** — [implementation](../implementation/SKILL.md); [quality-gate](../quality-gate/SKILL.md) before commit.
5. **Integrate** — [integration](../integration/SKILL.md) (commit → PR → review → merge).
6. **Ship & run** — [deployment](../deployment/SKILL.md) then [operations](../operations/SKILL.md).
7. **Sustain** — [maintenance](../maintenance/SKILL.md), [governance](../governance/SKILL.md) as needed.

## Validation and quality

- Before merge: [validation](../validation/SKILL.md), [test](../test/SKILL.md), quality gate.
- Optional traceability: [v-model](../v-model/SKILL.md).

## Anti-patterns

- Invoking this skill instead of a phase skill when only one phase applies
- Skipping issue-workflow for non-trivial work (no acceptance criteria, no traceability)

## Additional resources

- Full index: [SKILL_TREE.md](../SKILL_TREE.md)
- How skills compose: [COOPERATION.md](../COOPERATION.md)
