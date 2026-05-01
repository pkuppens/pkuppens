---
name: issue-gh-bulk-scratch
description: Creates an EPIC and many GitHub issues with gh, keeps local gitignored tmp body files named 1-1 with issue numbers, and self-assigns. Use when batch-filing a portfolio/roadmap set from scratch files or renumbering after creation.
---

# GitHub bulk issues + local 1-1 scratch files

## When to use

- You are creating **one umbrella EPIC** and **several child issues** with `gh issue create` and want **local markdown copies** that stay in sync (filename = GitHub issue number).
- You need **self-assignment** so every issue (EPIC and children) appears on the assignee’s list.
- You are **renumbering** after creation when draft files were `ISSUE-1` … `ISSUE-n` (sequence) before you knew the real numbers.

## Prerequisites

- `gh auth login` (user who should own issues, so `@me` matches intended assignee)
- `tmp/` in repo `.gitignore` for scratch (see repo CLAUDE.md)
- [issue-metadata](../issue-metadata/SKILL.md): default assignee = trigger / operator via `--assignee @me`

## Way of working

1. **Draft bodies** in gitignored `tmp/` (repo root or `tmp/github/` if your repo standardizes that):
   - **Option A (unknown numbers):** `tmp/EPIC-DRAFT.md` and `tmp/ISSUE-DRAFT-1.md` … `tmp/ISSUE-DRAFT-N.md` — import order = creation order, not the final issue number.
   - **Option B (after creation):** one file per issue: `tmp/EPIC-<#>.md`, `tmp/ISSUE-<#>.md` (GitHub number in the name).

2. **Create on GitHub** (PowerShell: parse number from the URL line `https://github.com/OWNER/REPO/issues/N` if `gh issue create` has no `--json number` in your `gh` version):
   - EPIC first; optional `gh issue comment` on the EPIC listing children.
   - For each child: `gh issue create --title "..." --body-file tmp/... --assignee @me` (or run **Assign** in step 4 in one pass).

3. **Rename to 1-1 (required):** after you know the numbers, write final files as `tmp/EPIC-<N>.md` and `tmp/ISSUE-<N>.md` and delete the draft names. **The integer in the filename must equal the GitHub issue number.** Optional first line in each file:

   ```markdown
   > **Local scratch** for GitHub **#N** — [open issue](.../issues/N) · EPIC: [#PARENT](.../issues/PARENT)
   ```

4. **Self-assign (required for visibility on “my” list):** for EPIC and every child, either:
   - pass `--assignee @me` on each `gh issue create`, or
   - after creation: `gh issue edit <n> --add-assignee @me` for all `N` in one loop.

   **PowerShell:** `@me` must be quoted or the shell treats `@` as splatting — use `--add-assignee '@me'` (or assign the login from `gh api user -q .login`).

5. **Record mapping** in `tmp/GITHUB-REFS.md` (gitignored) or `tmp/GITHUB-REFS.md` + table: `Kind | # | URL | local file`.

6. **Link children to EPIC:** `gh issue comment` on the EPIC with a checklist `- #16` …, and optionally a short comment on each child: `Part of portfolio EPIC #15`.

## gh CLI (examples)

```bash
# Create with assignee
gh issue create -t "Title" -F tmp/EPIC-DRAFT.md --assignee @me

# Self-assign in batch (bash)
for n in 15 16 17 18; do gh issue edit "$n" --add-assignee @me; done
```

## Integration

- Composes with [issue-workflow](../SKILL.md) (duplicates, acceptance criteria) and [issue-metadata](../issue-metadata/SKILL.md) (assignee rules).
- After issues exist, work follows the repo branch strategy ([plan-branch-strategy](../../plan-branch-strategy/SKILL.md), [plan](../../plan/SKILL.md)).

## Anti-patterns

- Committing `tmp/*` to git unless the project explicitly version-controls drafts.
- Leaving assignees empty when the human requester is known — use `@me` or the requester’s login.
- Keeping only `ISSUE-1` … `ISSUE-10` as final names when GitHub actually issued #16…#25 (breaks 1-1 reference).
