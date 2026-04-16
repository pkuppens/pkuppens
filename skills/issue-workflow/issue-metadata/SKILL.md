---
name: issue-metadata
description: Adds tags, milestones, assignees (always the user who triggered the issue), and planning references. Use when finalising an issue for GitHub or project tracking.
---

# Issue Metadata

Completes issue metadata for GitHub labels, milestones, assignees, and planning links.

## When to use

- When finalising an issue before creation or before implementation

## Instructions

1. **Tags / labels** — add `size:S`, `type:feature`, `area:backend`, `priority:high`, etc. per repo conventions.
2. **Milestone** — if repo uses milestones, suggest one; otherwise omit.
3. **Assignees (required)** — assign the GitHub user who **triggered** creation of this issue (directly or indirectly). This makes ownership explicit and turns the issue into a visible review task for that person. Do not leave assignees empty unless the repo forbids self-assignment or you cannot resolve the trigger (then note why in the issue body).
   - **Direct trigger:** the person who asked for the issue, reported the bug, or approved filing it. If you create the issue with `gh` as that person, use `--assignee @me`. If you draft for paste into the web UI, set Assignees to that user’s GitHub handle.
   - **Indirect trigger:** the originating actor for automation or hand-offs (e.g. author of the PR or commit that caused a bot to open an issue, user who ran the workflow, requester named in the parent ticket). Resolve their GitHub login and pass `--assignee <login>` or set them in the UI.
   - **Agent / assistant:** infer the human requester from conversation; if their GitHub login is unknown, ask once or use `@me` when the operator running `gh` is the requester.
4. **Planning references** — link to sprint doc, roadmap, or parent issue (e.g. Parent: #4).

## Output format

```markdown
## Metadata
- **Labels:** `size:M`, `type:task`, `area:skills`
- **Milestone:** (none | v1.2)
- **Assignees:** @username (trigger: direct | indirect — [who])
- **Parent:** #N
```

## gh CLI

```bash
gh issue create --title "..." --body "..." --label "size:M" --label "type:task" --assignee @me
```

Use `--assignee <login>` when the trigger is another GitHub user. `gh api user -q .login` shows the authenticated account when you need to confirm `@me`.

## Integration

- Runs last in issue-workflow sequence.
- Uses output from [issue-estimate](../issue-estimate/SKILL.md) for size label.
