---
name: issue-coding
description: >-
  Orchestrates the TDD coding inner loop for a validated issue on a feature branch.
  Use when acceptance criteria exist, plan/branch are done, and implementation begins;
  runs validation-draft first, then construction, test-run, and quality-gate as exit.
---

# Issue coding

Thin orchestrator for the **coding inner loop** between [plan](../../plan/SKILL.md) (branch + tasks ready) and [integration](../../integration/SKILL.md) (commit, PR, merge). Does not redefine issues, create branches, or open PRs.

## When to use

- A GitHub issue has **acceptance criteria** (mandatory) and a **feature branch** exists
- [issue-workflow](../SKILL.md) (5.1–5.7) and [plan](../../plan/SKILL.md) are complete
- The agent or human is starting implementation (not planning or merging)

Acceptance criteria are the **target function** for AI-assisted coding: they define what “done” means for this session. Without them, stop and return to [issue-acceptance-criteria](../issue-acceptance-criteria/SKILL.md) or external [grill-with-docs](https://www.skills.sh/mattpocock/skills/grill-with-docs) until criteria are testable and documented on the issue (see [_meta/human-ai-execution.md](../../_meta/human-ai-execution.md#external-skills)).

## Acceptance criteria (required, stable during coding)

**Before coding:** Criteria must be specific enough to drive [validation-draft](../../validation/validation-draft/SKILL.md) and tests — copy-pastable checks, expected outcomes, not vague goals. If the issue body is thin, run **grill-with-docs** (or [issue-workflow](../SKILL.md) acceptance-criteria sub-skill) with the human until criteria are written on the issue.

**During the coding loop:** Treat acceptance criteria as **frozen** unless changed through an explicit human agreement:

- Human approves an update in chat (human-in-the-loop), **or**
- The change is recorded in a **GitHub issue comment** or **PR comment** that the agent (or reviewer) can cite.

Do not silently reinterpret, expand, or rewrite criteria mid-implementation. Scope creep belongs in a new issue or an agreed issue/PR comment first.

## Preconditions (guard)

Stop and resolve before coding if any check fails:

1. **Issue is implementation-ready** — body includes testable acceptance criteria (checkboxes); each maps to a verifiable outcome. If missing or vague, stop — use [issue-acceptance-criteria](../issue-acceptance-criteria/SKILL.md) or external [grill-with-docs](https://www.skills.sh/mattpocock/skills/grill-with-docs) before continuing. Prefer an **Agent Brief** comment from external [triage](https://www.skills.sh/mattpocock/skills/triage) when present; it is the contract for AFK agents (see [_meta/human-ai-execution.md](../../_meta/human-ai-execution.md#external-skills)).
2. **Triage / execution** — issue carries `execution:ai-ok` **or** the maintainer explicitly started coding in chat. If the issue has `execution:human-required` or `execution:human-review` without approval, pause for human sign-off (see [_meta/human-ai-execution.md](../../_meta/human-ai-execution.md)).
3. **Branch** — current branch is not `main`/`master`; matches repo convention (`feature/NNN-…`, etc.). If missing, run [plan-branch-strategy](../../plan-branch-strategy/SKILL.md) via `plan` first.
4. **Scope** — re-read **Out of Scope** on the issue; do not expand into integration or new issue drafting.

**Human-in-the-loop pause:** After issue-workflow and plan, a maintainer may review the issue before invoking this skill. Do not start coding until that review completes unless `execution:ai-ok` and the user (or agent brief) explicitly authorizes implementation.

## Flow (mandatory order)

Do not skip or reorder steps 1–5.

| Step | Skill | Purpose |
|------|--------|---------|
| 1 | [validation-draft](../../validation/validation-draft/SKILL.md) | **TDD:** draft tests/scenarios from acceptance criteria **before** production code |
| 2 | [test-write](../../test/test-write/SKILL.md) | Implement failing tests where automation applies |
| 3 | [implementation-construction](../../implementation/implementation-construction/SKILL.md) | Write or change code to satisfy tests and criteria |
| 4 | [test-run](../../test/test-run/SKILL.md) | Red/green loop until the suite passes |
| 5 | [quality-gate](../../quality-gate/SKILL.md) | Lint, format, type-check, tests — **exit condition** |

Optional within step 1–2: [create-validation](../../validation/create-validation/SKILL.md) for a full executable checklist when the issue warrants it.

### Inner loop

After step 3, repeat **test-run → fix (construction) → test-run** until green. Then run **quality-gate** once. If quality-gate fails, fix and re-run from the failing check (usually construction + test-run + quality-gate).

## Exit and handoff

**Done for this skill when:** [quality-gate](../../quality-gate/SKILL.md) passes on the feature branch.

**Next:** [integration](../../integration/SKILL.md) — commit, PR, review, merge. Do not open a PR inside `issue-coding`.

## Instructions

1. Run the **preconditions** guard; fetch issue with `gh issue view NNN` if needed.
2. Run **validation-draft** against every acceptance criterion; produce scenarios or test plan.
3. Run **test-write** for automated coverage; expect red tests before implementation.
4. Run **implementation-construction** for the planned tasks only; satisfy the **frozen** acceptance criteria (see above).
5. Run **test-run**; iterate until pass.
6. Run **quality-gate**; fix until pass.
7. Report: branch name, tests run, quality-gate result, and that work is ready for **integration**.

## Out of scope

- Issue definition, duplicates, estimates ([issue-workflow](../SKILL.md) 5.1–5.7)
- Rewriting acceptance criteria without human agreement or issue/PR comment
- Branch creation and task breakdown ([plan](../../plan/SKILL.md))
- Commit, PR, merge ([integration](../../integration/SKILL.md))
- Staleness detection if `main` diverged since issue creation (user must request explicit re-validation)
- CI pipeline specifics beyond what quality-gate already covers

## Integration

- Chained from [issue-workflow](../SKILL.md) optional step 11 after planning.
- Composes with [COOPERATION.md](../../COOPERATION.md) TDD and issue → coding → integration flows.
- External [triage](https://www.skills.sh/mattpocock/skills/triage) → `ready-for-agent` + Agent Brief + `execution:ai-ok` is the typical entry for AFK agents on this repo.
- V-model: optional pairing via [v-model-implementation-unit](../../v-model/v-model-implementation-unit/SKILL.md).
