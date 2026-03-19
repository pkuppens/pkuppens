---
name: git-worktrees
description: Explains git worktrees and Claude Code usage; guides removal and cleanup when a branch cannot be deleted because of an active worktree. Use when "cannot delete branch used by worktree", cleaning up .claude/worktrees/, or when the user asks about worktrees.
---

# Git Worktrees

Explains git worktrees, how Claude Code uses them, and how to remove or clean them.

## When to use

- `git branch -D <branch>` fails with "cannot delete branch used by worktree"
- User asks "what are worktrees?" or "how does Claude use worktrees?"
- Cleaning up `.claude/worktrees/` after sessions
- Deciding whether to keep or discard a Claude worktree

## What are worktrees?

A **worktree** lets you check out multiple branches from the same repo at once, each in its own directory. Shared: history, remotes, config. Independent per worktree: working files, index, checked-out branch.

**Rule:** A branch can be checked out in only one worktree at a time. That is why `git branch -D <branch>` fails while the worktree exists.

## How Claude Code uses worktrees

| Aspect | Behaviour |
|--------|-----------|
| **Creation** | Creates worktrees under `.claude/worktrees/` when you say "work in a worktree" or use `claude --worktree` |
| **Branch naming** | Branches like `claude/jolly-euler` (random suffix) or `claude --worktree feature-name` for a named worktree |
| **Isolation** | Each session can have its own worktree to avoid conflicts between parallel sessions or sub-agents |
| **Auto-cleanup** | If no changes were made, Claude removes the worktree and branch when the session ends |
| **With changes** | Claude prompts to keep or discard; if kept, the worktree remains until you remove it manually |

**Task tool:** `isolation: "worktree"` in agent frontmatter makes sub-agents run in their own worktree.

**Recommended:** Add `.claude/worktrees/` to `.gitignore`.

## Remove and clean

Before deleting a branch used by a worktree, remove the worktree first.

### Step 1 — Inspect (optional but recommended)

Check if the worktree has unique content worth keeping:

```bash
git log main..<branch> --oneline   # Commits in branch not in main
git log <branch>..main --oneline   # Commits in main not in branch
```

If the branch has no commits ahead of main and no uncommitted changes, it is safe to remove.

### Step 2 — Remove the worktree

```bash
git worktree remove .claude/worktrees/<name>
```

If uncommitted changes exist and you still want to remove: `git worktree remove --force .claude/worktrees/<name>`.

### Step 3 — Delete the branch

```bash
git branch -D <branch>
```

### Step 4 — Prune stale refs (optional)

```bash
git worktree prune
```

### If the directory is locked

If `git worktree remove` fails with "not a working tree", or the branch was already deleted, the directory may be orphaned and locked by another process (IDE, Explorer). Remove it manually once nothing is using it:

```powershell
Remove-Item -Recurse -Force .claude\worktrees\<name>
```

## Integration

- Referenced by [maintenance-cleanup](../maintenance/maintenance-cleanup/SKILL.md) for worktree removal during post-merge cleanup.
- See [README.md](README.md) for further reading and links to official docs.
