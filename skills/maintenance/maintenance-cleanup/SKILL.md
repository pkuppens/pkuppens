---
name: maintenance-cleanup
description: Branch cleanup, GitHub Actions runs, tmp/ hygiene after merge. Use when cleaning up after PR merge, deleting local branches, removing worktrees, or pruning stale workflow runs.
---

# Maintenance Cleanup

Post-merge hygiene: branch cleanup, worktree removal, GitHub Actions runs, tmp/ hygiene.

## When to use

- After PR merge when local branch should be deleted
- When `git branch -D` fails because branch is used by a worktree
- When cleaning up old GitHub Actions workflow runs
- When tidying `tmp/` or other scratch directories

## Branch cleanup

For a full PR-merge checklist (merge, squash, rebase, `gone` remotes), see [branch-cleanup-after-pr](../../branch-cleanup-after-pr/SKILL.md).

1. `git checkout main`, `git pull`
2. `git branch -d <branch>` (or `-D` if squash-merged)
3. `git fetch --prune` to remove stale remote-tracking refs

### If branch is used by a worktree

If `git branch -D <branch>` fails with "cannot delete branch used by worktree", follow the remove/clean procedure in [git-worktrees](../../git-worktrees/SKILL.md#remove-and-clean).

## GitHub Actions runs

Delete old or failed workflow runs to reduce clutter:

```bash
# Delete completed runs older than 30 days for a workflow
gh run list --workflow ci.yml --status completed --limit 100 --json databaseId,createdAt \
  | jq '[.[] | select(.createdAt < (now - 2592000 | todate))] | .[].databaseId' \
  | xargs -I {} gh run delete {}
```

## tmp/ hygiene

Ensure `tmp/` is gitignored. Remove obsolete drafts, planning notes, and debug artifacts. Per-repo `tmp/` layout: see workspace CLAUDE.md scratch directory section.

## Integration

- Runs after [integration-merge](../../integration/integration-merge/SKILL.md).
- Worktree removal: [git-worktrees](../../git-worktrees/SKILL.md).
