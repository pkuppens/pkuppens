---
name: integration-pr
description: Opens PR; links to issue; fills description template. Use after commit and push, before merge.
---

# Integration PR

Creates a pull request with proper linkage to the issue and a structured description.

## When to use

- After integration-commit and push
- When work is ready for review

## Prerequisites

For OpenClaw projects: [openclaw-security](../../openclaw-security/SKILL.md) must have passed (quality-gate includes it). Do not open PR until `openclaw security audit --deep` and `openclaw security audit --fix` succeed.

## Instructions

1. Push branch: `git push -u origin <branch>`.
2. Create PR: `gh pr create --base main --title "#NNN: type: description" --body "..."`.
3. In body: Summary, Changes, link to issue (Closes #NNN).
4. Add labels if repo uses them (`gh pr edit --add-label "..."`).

## PR body template

```markdown
## Summary
[One paragraph: what and why]

## Changes
- ...
- ...

Closes #NNN
```

## Example

```bash
gh pr create --base main --title "#8: feat: Phase 3 — remaining issue-workflow sub-skills" --body "## Summary
Implements Phase 3...

Closes #8"
```

## Integration

- Runs after [integration-commit](../integration-commit/SKILL.md).
- Feeds into [integration-merge](../integration-merge/SKILL.md).
