---
name: integration
description: Orchestrates commit, PR, and merge; enforces conventional commits and issue linkage. Use when completing work ready for main; runs after quality-gate passes.
---

# Integration

Creates PR, merges to main, and ensures proper Git workflow per repo CLAUDE.md.

## When to use

- After implementation and quality-gate pass
- When work is ready for review and merge

## Flow

1. **Commit** — [integration-commit](integration-commit/SKILL.md). Conventional message, issue reference.
2. **PR** — [integration-pr](integration-pr/SKILL.md). Open PR, link issue, fill description.
3. **Merge** — [integration-merge](integration-merge/SKILL.md). Merge, resolve conflicts, squash if needed.

## Instructions

1. Ensure quality-gate passes (lint, format, tests).
2. Run integration-commit; stage and commit with conventional message.
3. Push branch; run integration-pr to open PR.
4. After review/approval, run integration-merge.

## Prerequisites

- `gh` CLI authenticated
- Branch naming: `feature/NNN-short-description` per CLAUDE.md

## Integration

- Runs after [quality-gate](../quality-gate/SKILL.md).
- Uses `gh pr create`, `gh pr merge`. See [COOPERATION.md](../COOPERATION.md) for composition patterns.
