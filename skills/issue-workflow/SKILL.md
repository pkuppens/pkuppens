---
name: issue-workflow
description: Orchestrates issue lifecycle from idea to closed. Use when creating, refining, or validating a GitHub issue; triggers sub-skills (5.1–5.7) as needed. New issues assign the trigger user for explicit ownership and review.
---

# Issue Workflow

Orchestrates the GitHub issue lifecycle per [GitHub Issue Lifecycle](https://docs.github.com/en/issues) conventions and repo CLAUDE.md.

## When to use

- User has an idea or bug report and wants a well-formed issue draft
- Refining an existing issue before implementation
- Validating an issue for completeness (acceptance criteria, out-of-scope, duplicates)

## Flow

1. **Check duplicates** — [issue-check-duplicates](issue-check-duplicates/SKILL.md). Search open and recently closed issues. If duplicate found, link and stop or merge scope.
2. **Architecture (optional)** — For issues that touch architecture (new system, undocumented code, ADR changes), invoke [architecture](../architecture/SKILL.md) orchestrator or [architecture-consult](../architecture/architecture-consult/SKILL.md) before or during purpose-alignment. Requirements and implementation plan should reflect ADRs, building blocks, and constraints.
3. **Purpose alignment** — [issue-purpose-alignment](issue-purpose-alignment/SKILL.md). Ensure goal aligns with project goals and quality attributes.
4. **Work down** — [issue-work-down](issue-work-down/SKILL.md). Identify files, tests, related issues; scope the work.
5. **Acceptance criteria** — [issue-acceptance-criteria](issue-acceptance-criteria/SKILL.md). Each checkbox with copy-pastable validation steps. Include architecture-related criteria when relevant (e.g. ADR updated, docs in `docs/architecture/`).
6. **Out-of-scope** — [issue-out-of-scope](issue-out-of-scope/SKILL.md). Define exclusions.
7. **Estimate** — [issue-estimate](issue-estimate/SKILL.md). T-shirt size (XS–XL).
8. **Metadata** — [issue-metadata](issue-metadata/SKILL.md). Tags, milestones, assignees (always assign the person who triggered the issue—directly or indirectly—so ownership and review are explicit).
9. **Bulk EPIC + children with `gh` (optional)** — [issue-gh-bulk-scratch](issue-gh-bulk-scratch/SKILL.md). When creating many related issues at once: gitignored `tmp/EPIC-#.md` and `tmp/ISSUE-#.md` named **1-1** with GitHub issue numbers, and `--assignee @me` (or batch `gh issue edit`) so each item shows on the assignee’s list.
10. **Draft issue** — Combine into issue body with Goal, Tasks, Acceptance Criteria, Out of Scope, Estimate, Metadata.

## Instructions

1. Gather context: repo, idea summary, existing issues if any.
2. Run check-duplicates → (architecture if architecture-related) → purpose-alignment → work-down; decide proceed.
3. When the issue touches architecture (new system, undocumented codebase, ADR or building-block changes), invoke architecture orchestrator or architecture-consult before or during purpose-alignment or acceptance-criteria. Ensure requirements and implementation plan reference ADRs, building blocks, or constraints.
4. Run acceptance-criteria; produce a checklist with copy-pastable steps per criterion. Add architecture-related criteria when relevant.
5. Run out-of-scope; list exclusions.
6. Run estimate; add T-shirt size.
7. Run metadata; add labels, milestone, and assignees (default: assign the trigger user per issue-metadata).
8. If bulk-filing an EPIC and many sub-issues with `gh`, use [issue-gh-bulk-scratch](issue-gh-bulk-scratch/SKILL.md) for local 1-1 `tmp` names and self-assign.
9. Assemble final issue draft for `gh issue create` or paste into GitHub UI.

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
Labels: size:M, type:task — Milestone: (none) — Assignee: @trigger — Parent: #N

## Related
- #N (if duplicate/related)
```

## Integration

Uses `gh` CLI: `gh issue list`, `gh issue view`, `gh issue create`. Ensure `gh auth login` if needed. For EPIC + multiple sub-issues with local scratch files, see [issue-gh-bulk-scratch](issue-gh-bulk-scratch/SKILL.md).

### Optional: V-model traceability

For issues in regulated, high-assurance, or “must prove verification” contexts, after acceptance criteria are drafted consider [v-model](../v-model/SKILL.md) so each AC can be tied to validation/tests. For **brownfield** work, see [v-model-retrofit](../v-model/v-model-retrofit/SKILL.md). Execution ownership: [_meta/human-ai-execution.md](../_meta/human-ai-execution.md).
