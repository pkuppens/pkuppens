---
name: plan
description: Breaks work into tasks, estimates, dependencies, branch strategy. Ensures implementation plans include feature-branch workflow and completion through PR with CI validation. Use when creating implementation plans, decomposing issues, or in plan mode.
---

# Plan

Decomposes work into tasks, dependencies, and branch strategy per SKILL_TREE §6. **Plans must include validation before implementation, then the full workflow through PR and CI.**

## When to use

- Creating an implementation plan from an issue or task
- Plan mode (agent produces a plan before implementation)
- Decomposing work into ordered subtasks

## Phase 1 — Validate (before any implementation)

Before creating branches or editing code:

1. **Check duplicates** — Was this already implemented (fully or partially)? See [issue-check-duplicates](../issue-workflow/issue-check-duplicates/SKILL.md); search codebase, `git log`, merged PRs.
2. **Purpose alignment** — Does the issue align with project goals? See [issue-purpose-alignment](../issue-workflow/issue-purpose-alignment/SKILL.md).
3. **Work-down** — What code, tests, or related issues exist? Which components, modules, or ADRs apply? See [issue-work-down](../issue-workflow/issue-work-down/SKILL.md).
4. **Acceptance criteria** — Are they clear and testable? See [issue-acceptance-criteria](../issue-workflow/issue-acceptance-criteria/SKILL.md).
5. **Architecture** — Which components/sub-components exist? Must anything be added or inspected? Consult architecture docs and [architecture-consult](../architecture/architecture-consult/SKILL.md) if placement is unclear.

Stop if the issue is obsolete, duplicate, or not ready. Do not proceed to implementation until validation is complete.

## Phase 2 — Implementation workflow (mandatory in plans)

Every implementation plan **must** include these steps:

1. **Create feature branch and implement** — Branch from `main` before any edits. Use a branch prefix per repo convention: `feature/NNN-…`, `hotfix/NNN-…`, `chore/…`, `epic/…`. See [plan-branch-strategy](../plan-branch-strategy/SKILL.md). Execute all plan tasks on this branch; never implement on `main`.
2. **Quality gate** — Run repo quality checks before commit: lint, format, tests. See [quality-gate](../quality-gate/SKILL.md).
3. **Commit and push** — Conventional commit with issue reference. See [integration-commit](../integration/integration-commit/SKILL.md).
4. **Open PR** — Create PR linking to issue. See [integration-pr](../integration/integration-pr/SKILL.md).
5. **CI validation** — Plan must include waiting for or verifying CI before considering work complete. Strategies vary by project: e.g. unit tests on PR, integration suite at merge to `main`; or single pipeline on PR. Check `.github/workflows/` or equivalent for the repo’s setup. Confirm N/A for markdown-only repos.

**Summary:** Validate first; work from a feature branch; complete through PR; do not stop until PR is open and CI has validated (or N/A).

### Optional: V-model and brownfield

When the project or issue calls for **traceability** (pairing specs/design with tests), follow [v-model](../v-model/SKILL.md). On an **existing codebase**, default to **touch-driven** [v-model-retrofit](../v-model/v-model-retrofit/SKILL.md): strengthen tests and minimal docs only for the **surfaces changed** in this issue unless the user or issue explicitly requests a wider retrofit (`retrofit:explicit`).

## Sub-skills

| Sub-skill | Use when |
|-----------|----------|
| plan-tasks (6.1) | Decomposing into ordered subtasks |
| plan-dependencies (6.2) | Identifying task dependencies and critical path |
| [plan-branch-strategy](../plan-branch-strategy/SKILL.md) (6.3) | Selecting branch prefix and creating feature branch |

## Integration

- Feeds into [architecture](../architecture/SKILL.md) or [design-consult](../design/design-consult/SKILL.md) when placement needed.
- Implementation follows [implementation-construction](../implementation/implementation-construction/SKILL.md).
- Completion flow: [quality-gate](../quality-gate/SKILL.md) → [integration](../integration/SKILL.md).
- See [COOPERATION.md](../COOPERATION.md) for issue → implementation → integration flow.
