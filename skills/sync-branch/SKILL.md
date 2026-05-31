---
name: sync-branch
description: Syncs the remote default branch locally (checkout, fetch --prune, pull) and returns to the previous branch when it still exists locally and on origin. Use when the user asks to sync branch, sync main, update default branch, fetch and pull origin, or run /sync-branch.
---

# Sync Branch

Refresh the repository default branch without leaving the user on it when their feature branch still exists.

## When to use

- User wants latest `main` / default branch without staying on it
- Before starting work, to update base branch while on a feature branch
- After remote branch cleanup (`fetch --prune` removes stale refs)

Not for: deleting merged branches (use `branch-cleanup-after-pr`), opening PRs, or rebasing a feature branch onto main.

## Preconditions

- Working tree should be clean. If `git status --porcelain` is non-empty, stop and ask whether to stash, commit, or abort.
- Do not run on `main` if the user forbids direct work there; this skill only **reads** default branch — it does not commit.

## Workflow

Copy and track progress:

```text
Sync branch:
- [ ] Save current branch name
- [ ] Resolve default branch name
- [ ] Checkout default branch
- [ ] Fetch origin --prune
- [ ] Pull latest default branch
- [ ] Return to saved branch (if both local and origin exist)
```

### Step 1: Save current branch

```bash
OLD_BRANCH=$(git branch --show-current)
```

If not on any branch (detached HEAD), set `OLD_BRANCH` from `git rev-parse --short HEAD` and skip the return step at the end.

### Step 2: Resolve default branch

Prefer remote HEAD, then common fallbacks:

```bash
DEFAULT=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's|^origin/||')
if [ -z "$DEFAULT" ]; then
  if git show-ref --verify --quiet refs/heads/main; then DEFAULT=main
  elif git show-ref --verify --quiet refs/heads/master; then DEFAULT=master
  else
    DEFAULT=$(git remote show origin | sed -n 's/.*HEAD branch: //p')
  fi
fi
```

On Windows PowerShell, use `git symbolic-ref refs/remotes/origin/HEAD` and strip `refs/remotes/origin/` from the result, or `gh repo view --json defaultBranchRef -q .defaultBranchRef.name` when `gh` is available.

### Step 3: Checkout default branch

```bash
git checkout "$DEFAULT"
```

### Step 4: Fetch with prune

```bash
git fetch origin --prune
```

### Step 5: Pull latest

```bash
git pull origin "$DEFAULT"
```

Use `git pull --ff-only` when the repo policy requires fast-forward only.

### Step 6: Return to previous branch

Only if **both** exist after fetch:

- Local: `refs/heads/$OLD_BRANCH`
- Remote: `refs/remotes/origin/$OLD_BRANCH`

```bash
if [ -n "$OLD_BRANCH" ] && [ "$OLD_BRANCH" != "$DEFAULT" ]; then
  if git show-ref --verify --quiet "refs/heads/$OLD_BRANCH" \
     && git show-ref --verify --quiet "refs/remotes/origin/$OLD_BRANCH"; then
    git checkout "$OLD_BRANCH"
  fi
fi
```

If local exists but remote was deleted, stay on `$DEFAULT` and tell the user their branch no longer exists on origin.

If local was deleted but remote exists, stay on `$DEFAULT` and suggest `git checkout -b "$OLD_BRANCH" "origin/$OLD_BRANCH"`.

## PowerShell (one-shot)

```powershell
$old = git branch --show-current
$default = (git symbolic-ref refs/remotes/origin/HEAD 2>$null) -replace '^refs/remotes/origin/', ''
if (-not $default) { $default = 'main' }
git checkout $default
git fetch origin --prune
git pull origin $default
if ($old -and $old -ne $default) {
  git show-ref --verify --quiet "refs/heads/$old" 2>$null; $local = $LASTEXITCODE -eq 0
  git show-ref --verify --quiet "refs/remotes/origin/$old" 2>$null; $remote = $LASTEXITCODE -eq 0
  if ($local -and $remote) { git checkout $old }
}
```

Chain with `;` not `&&` on older PowerShell.

## Safety

- Never force-push, reset hard, or delete branches in this workflow
- Never change `git config`
- If checkout or pull fails, report the error and do not guess; leave the user on whichever branch checkout last succeeded

## Related skills

- [branch-cleanup-after-pr](../branch-cleanup-after-pr/SKILL.md) — delete merged or gone branches after PR merge
- [git-worktrees](../git-worktrees/SKILL.md) — when branch is locked by a worktree
