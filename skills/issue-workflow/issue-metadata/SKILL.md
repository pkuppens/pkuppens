---
name: issue-metadata
description: Adds tags, milestones, assignees, and planning references to an issue. Use when finalising an issue for GitHub or project tracking.
---

# Issue Metadata

Completes issue metadata for GitHub labels, milestones, assignees, and planning links.

## When to use

- When finalising an issue before creation or before implementation

## Instructions

1. **Tags / labels** — add `size:S`, `type:feature`, `area:backend`, `priority:high`, etc. per repo conventions.
2. **Milestone** — if repo uses milestones, suggest one; otherwise omit.
3. **Assignees** — add if known; leave empty for triage.
4. **Planning references** — link to sprint doc, roadmap, or parent issue (e.g. Parent: #4).

## Output format

```markdown
## Metadata
- **Labels:** `size:M`, `type:task`, `area:skills`
- **Milestone:** (none | v1.2)
- **Assignees:** (none | @username)
- **Parent:** #N
```

## gh CLI

```bash
gh issue create --title "..." --body "..." --label "size:M" --label "type:task"
```

## Integration

- Runs last in issue-workflow sequence.
- Uses output from [issue-estimate](../issue-estimate/SKILL.md) for size label.
