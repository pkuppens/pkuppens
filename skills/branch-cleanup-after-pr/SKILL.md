---
name: branch-cleanup-after-pr
description: Sync local branches after a PR is merged. Checkout main, pull, fetch --prune, delete local branches that are merged or track gone remotes. Use when a PR was just merged (merge, squash, or rebase) or when local branch list is stale.
---

# Branch Cleanup After PR Merge

When a PR is merged (merge commit, squash-merge, or rebase-merge), run this to sync local state and remove obsolete branches.

Complements [maintenance-cleanup](../maintenance/maintenance-cleanup/SKILL.md) (broader hygiene) and [git-worktrees](../git-worktrees/SKILL.md) — use worktrees when branch deletion fails.

## Workflow

1. **Checkout main, pull**
   ```bash
   git checkout main
   git pull
   ```

2. **Fetch with prune** (removes refs for deleted remote branches)
   ```bash
   git fetch --prune
   ```

3. **Identify branches to delete**
   - **Merge commits**: `git branch --merged main` — branch tip is in main's history
   - **Gone upstream**: `git branch -vv | grep ': gone]'` — remote ref was deleted on GitHub
   - **Functional merge (patch-equivalent after squash/rebase/cherry-pick)**:
     - `git cherry -v main <branch>`
     - If all branch commits show `-`, the branch changes are already in `main` even when ancestry differs

4. **Delete local branches**
   - From `--merged` list (exclude protected branches), run `git branch -d <name>`
   - From `: gone]` list:
     - Try `git branch -d <name>`
     - If blocked as "not fully merged", verify with `git cherry -v main <name>`
     - If commits are all `-`, delete with `git branch -D <name>` (safe because patches already exist in `main`)

## Merge Type Coverage

| Type | Detection | Notes |
|------|-----------|-------|
| Merge commit | `--merged main` | Branch tip is ancestor of main |
| Squash merge | `git cherry -v main <branch>` | Commits often appear as `-` even if `--merged` misses them |
| Rebase merge | `git cherry -v main <branch>` | Same pattern as squash merge |
| Cherry-pick merge | `git cherry -v main <branch>` | Patch-equivalent commits appear as `-` |

## Protected Branches

Never delete: `main`, `master`, `develop`, `release/*`, `hotfix/*`

## Cross-Platform

- **PowerShell**: Use `Select-String` instead of `grep`; chain with `;` not `&&` where needed
- **Bash**: Standard grep/awk/sed

## Reference

Some repos keep copy-paste commands under `.cursor/commands/branch-cleanup.md` — optional.
