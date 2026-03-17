---
name: plan-branch-strategy
description: Creates the feature branch for planned work. Use at planning time before any code edits, or when the feature-branch hook blocks an edit on main.
---

# Plan Branch Strategy

## When to use

- At the start of planning, before any file edits
- When the feature-branch hook returns `HOOK:FEATURE_BRANCH_REQUIRED`

## Branch naming

See [CLAUDE.md § Git Workflow](../../CLAUDE.md#git-workflow) for the canonical convention. Common prefixes (gitflow-style):

| Prefix | Use when |
|--------|----------|
| `feature/NNN-…` | New feature (most common) |
| `hotfix/NNN-…` | Urgent production fix |
| `chore/…` | Tooling, config, docs |
| `epic/NNN-…` | Large effort spanning multiple issues |

Repo conventions may vary; check the project’s CLAUDE.md or contribution docs.

## Instructions

1. Confirm the issue number (from `gh issue list` or conversation context).
2. Choose the prefix per repo convention.
3. Create and switch: `git checkout -b <prefix>/<NNN>-<slug>`.
4. Verify: `git branch --show-current`.

## Example

```bash
git checkout -b feature/42-plan-mode-checklist
git branch --show-current   # → feature/42-plan-mode-checklist
```

## Integration

- Runs before [implementation-construction](../implementation/implementation-construction/SKILL.md).
- Branch is later used by [integration-commit](../integration/integration-commit/SKILL.md) → [integration-pr](../integration/integration-pr/SKILL.md).
- Invoked by [plan](../plan/SKILL.md) in Phase 2.
