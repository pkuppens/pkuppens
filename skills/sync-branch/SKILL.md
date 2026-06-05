---
name: sync-branch
description: Syncs remote default branch locally (checkout, fetch --prune, pull) and returns to the previous branch when it still exists. Reports stashes and worktrees not yet handled. Use when the user asks to sync main, update default branch, fetch/pull origin, or run /sync-branch.
---

# Sync Branch

Update default branch (`main`) without leaving the user stranded. Read-only on default branch — no commits.

**Not for:** branch deletion ([branch-cleanup-after-pr](../branch-cleanup-after-pr/SKILL.md)), PRs, rebase.

## Checklist

```text
- [ ] Pre-flight: working tree, stashes, worktrees
- [ ] Save current branch
- [ ] Checkout default → fetch --prune → pull
- [ ] Return to saved branch (if local + origin exist)
- [ ] Post: report leftover stashes/worktrees
```

## Pre-flight

**Dirty tree** — `git status --porcelain` non-empty → stop; ask stash / commit / abort. Do not auto-stash.

**Stashes** — `git stash list`. If any exist:

- Report each (`stash@{n}` + branch message).
- Do **not** drop, pop, or apply unless the user asked.
- If a stash targets the saved branch, note: `git stash pop` after return (only when user wants it).

**Worktrees** — `git worktree list`. If more than one entry:

- Report path + branch per worktree.
- Do **not** remove unless the user asked.
- Checkout/delete failures → [git-worktrees](../git-worktrees/SKILL.md).

## Sync steps

```bash
OLD_BRANCH=$(git branch --show-current)

DEFAULT=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's|^origin/||')
[ -z "$DEFAULT" ] && DEFAULT=main

git checkout "$DEFAULT"
git fetch origin --prune
git pull --ff-only origin "$DEFAULT" 2>/dev/null || git pull origin "$DEFAULT"

if [ -n "$OLD_BRANCH" ] && [ "$OLD_BRANCH" != "$DEFAULT" ]; then
  if git show-ref --verify --quiet "refs/heads/$OLD_BRANCH" \
     && git show-ref --verify --quiet "refs/remotes/origin/$OLD_BRANCH"; then
    git checkout "$OLD_BRANCH"
  elif git show-ref --verify --quiet "refs/heads/$OLD_BRANCH"; then
    echo "Staying on $DEFAULT: $OLD_BRANCH has no origin ref."
  elif git show-ref --verify --quiet "refs/remotes/origin/$OLD_BRANCH"; then
    echo "Staying on $DEFAULT: recreate with git checkout -b $OLD_BRANCH origin/$OLD_BRANCH"
  fi
fi
```

Detached HEAD: skip return; report HEAD short SHA.

**PowerShell:** same flow; chain with `;` not `&&`. Default branch: `gh repo view --json defaultBranchRef -q .defaultBranchRef.name` if symbolic-ref fails.

## Post-sync

Re-list `git stash list` and `git worktree list` if anything was reported in pre-flight and not yet addressed. Summarize:

- current branch
- stashes still present (count + branches)
- extra worktrees (count + paths)

## Safety

- No force-push, hard reset, branch delete, or `git config` changes
- On checkout/pull failure: report error; stay on last successful branch

## Related

- [branch-cleanup-after-pr](../branch-cleanup-after-pr/SKILL.md) — delete merged/gone branches
- [git-worktrees](../git-worktrees/SKILL.md) — worktree removal when branch locked
