---
name: issue-workflow
description: Orchestrates issue lifecycle from idea to closed. Use when creating, refining, or validating a GitHub issue; triggers sub-skills (5.1–5.7) as needed.
---

# Issue Workflow

Orchestrates the GitHub issue lifecycle per [GitHub Issue Lifecycle](https://docs.github.com/en/issues) conventions and repo CLAUDE.md.

## When to use

- User has an idea or bug report and wants a well-formed issue draft
- Refining an existing issue before implementation
- Validating an issue for completeness (acceptance criteria, out-of-scope, duplicates)

## Flow

1. **Check duplicates** — [issue-check-duplicates](issue-check-duplicates/SKILL.md). Search open and recently closed issues. If duplicate found, link and stop or merge scope.
2. **Purpose alignment** — [issue-purpose-alignment](issue-purpose-alignment/SKILL.md). Ensure goal aligns with project goals and quality attributes.
3. **Work down** — [issue-work-down](issue-work-down/SKILL.md). Identify files, tests, related issues; scope the work.
4. **Acceptance criteria** — [issue-acceptance-criteria](issue-acceptance-criteria/SKILL.md). Each checkbox with copy-pastable validation steps.
5. **Out-of-scope** — [issue-out-of-scope](issue-out-of-scope/SKILL.md). Define exclusions.
6. **Estimate** — [issue-estimate](issue-estimate/SKILL.md). T-shirt size (XS–XL).
7. **Metadata** — [issue-metadata](issue-metadata/SKILL.md). Tags, milestones, assignees.
8. **Draft issue** — Combine into issue body with Goal, Tasks, Acceptance Criteria, Out of Scope, Estimate, Metadata.

## Instructions

1. Gather context: repo, idea summary, existing issues if any.
2. Run check-duplicates → purpose-alignment → work-down; decide proceed.
3. Run acceptance-criteria; produce a checklist with copy-pastable steps per criterion.
4. Run out-of-scope; list exclusions.
5. Run estimate; add T-shirt size.
6. Run metadata; add labels, milestone, assignees.
7. Assemble final issue draft for `gh issue create` or paste into GitHub UI.

## Output format

```markdown
## Goal
[One sentence: what and why]

## Tasks
- [ ] ...

## Acceptance Criteria
- [ ] ... (copy-pastable steps: command/URL → expected result)

## Out of Scope
- ...

## Estimate
Size: S | M | L — [rationale]

## Metadata
Labels: size:M, type:task — Milestone: (none) — Parent: #N

## Related
- #N (if duplicate/related)
```

## Integration

Uses `gh` CLI: `gh issue list`, `gh issue view`, `gh issue create`. Ensure `gh auth login` if needed.
