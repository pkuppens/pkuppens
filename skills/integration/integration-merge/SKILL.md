---
name: integration-merge
description: Merges PR; resolves conflicts; squashes if needed. Use after PR approval, before branch cleanup.
---

# Integration Merge

Merges the PR into main and performs post-merge cleanup.

## When to use

- After PR review and approval
- When ready to complete the integration

## Instructions

1. Merge: `gh pr merge <number> --merge` (or `--squash` if repo prefers).
2. Delete remote branch: `gh pr merge <number> --delete-branch` (or automatic if configured).
3. Local cleanup: `git checkout main`, `git pull`, `git branch -d <branch>` (or `-D` if squash-merged).

## Conflict resolution

If merge fails due to conflicts:
1. `git checkout <branch>`, `git pull origin main`
2. Resolve conflicts in editor
3. `git add`, `git commit`, `git push`
4. Retry `gh pr merge`

## Squash vs merge commit

- **Merge commit:** Preserves branch history; use when each commit is meaningful.
- **Squash:** Single commit on main; use for small PRs or when branch has WIP commits.

## Integration

- Runs after [integration-pr](../integration-pr/SKILL.md).
- Optional: [maintenance-cleanup](../../maintenance/maintenance-cleanup/SKILL.md) for branch pruning.
