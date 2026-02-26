---
name: issue-workflow
description: Orchestrates issue lifecycle from idea to closed. Use when creating, refining, or validating a GitHub issue; triggers sub-skills (check-duplicates, acceptance-criteria, out-of-scope) as needed.
---

# Issue Workflow

Orchestrates the GitHub issue lifecycle per [GitHub Issue Lifecycle](https://docs.github.com/en/issues) conventions and repo CLAUDE.md.

## When to use

- User has an idea or bug report and wants a well-formed issue draft
- Refining an existing issue before implementation
- Validating an issue for completeness (acceptance criteria, out-of-scope, duplicates)

## Flow

1. **Check duplicates** — Invoke [issue-check-duplicates](issue-check-duplicates/SKILL.md). Search open and recently closed issues for overlap. If duplicate found, link and stop or merge scope.
2. **Acceptance criteria** — Invoke [issue-acceptance-criteria](issue-acceptance-criteria/SKILL.md). Ensure checkboxes define "done".
3. **Out-of-scope** — Invoke [issue-out-of-scope](issue-out-of-scope/SKILL.md). Define what is explicitly excluded to prevent creep.
4. **Draft issue** — Combine into a markdown issue body with Goal, Tasks, Acceptance Criteria, Out of Scope.

## Instructions

1. Gather context: repo, idea summary, existing issues if any.
2. Run check-duplicates; report findings and decide proceed/merge/close.
3. Run acceptance-criteria; produce a checklist.
4. Run out-of-scope; list exclusions.
5. Assemble final issue draft for `gh issue create` or paste into GitHub UI.

## Output format

```markdown
## Goal
[One sentence: what and why]

## Tasks
- [ ] ...

## Acceptance Criteria
- [ ] ...

## Out of Scope
- ...

## Related
- #N (if duplicate/related)
```

## Integration

Uses `gh` CLI: `gh issue list`, `gh issue view`, `gh issue create`. Ensure `gh auth login` if needed.
