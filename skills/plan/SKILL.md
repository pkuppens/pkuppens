---
name: plan
description: Breaks work into tasks, estimates, dependencies, branch strategy. Ensures implementation plans include feature-branch workflow and completion through PR with CI validation. Use when creating implementation plans, decomposing issues, or in plan mode.
---

# Plan

Decomposes work into tasks, dependencies, and branch strategy per SKILL_TREE §6. **Plans must include the full implementation workflow through PR and CI validation.**

## When to use

- Creating an implementation plan from an issue or task
- Plan mode (agent produces a plan before implementation)
- Decomposing work into ordered subtasks

## Implementation workflow (mandatory in plans)

Every implementation plan **must** include these steps:

1. **Create feature branch** — Branch from `main`; use `feature/NNN-short-description` (issue number prefix).
2. **Implement** — Execute plan tasks on the feature branch. Never implement directly on `main`.
3. **Quality gate** — Run repo quality checks before commit: lint, format, tests. See [quality-gate](../quality-gate/SKILL.md).
4. **Commit and push** — Conventional commit with issue reference. See [integration-commit](../integration/integration-commit/SKILL.md).
5. **Open PR** — Create PR linking to issue. See [integration-pr](../integration/integration-pr/SKILL.md).
6. **CI validation** — Plan must include waiting for or verifying GitHub Actions (or equivalent CI) pass before considering the work complete. If the repo has `.github/workflows/`, CI runs on the PR branch.

**Summary:** Work from a feature branch; complete build through PR; do not stop until PR is open and CI has validated (or confirmed N/A for markdown-only repos).

## Sub-skills (future)

| Sub-skill | Use when |
|-----------|----------|
| plan-tasks (6.1) | Decomposing into ordered subtasks |
| plan-dependencies (6.2) | Identifying task dependencies and critical path |
| plan-branch-strategy (6.3) | Selecting branch naming (feature/task/bug/hotfix) |

## Integration

- Feeds into [architecture](../architecture/SKILL.md) or [design-consult](../design/design-consult/SKILL.md) when placement needed.
- Implementation follows [implementation-construction](../implementation/implementation-construction/SKILL.md).
- Completion flow: [quality-gate](../quality-gate/SKILL.md) → [integration](../integration/SKILL.md).
- See [COOPERATION.md](../COOPERATION.md) for issue → implementation → integration flow.
