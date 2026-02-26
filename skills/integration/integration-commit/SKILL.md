---
name: integration-commit
description: Commits staged changes with conventional commit message; references issue. Use after quality-gate passes, before opening PR.
---

# Integration Commit

Produces conventional commits that reference the issue and follow repo conventions.

## When to use

- After quality-gate passes
- Before pushing and opening PR

## Conventional format

```
#NNN: type: short description

Optional body. Explain what and why, not how.
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `chore`, `test`

## Instructions

1. Run `git status`; stage only files for this change (`git add` paths).
2. Compose message: `#NNN: type: description` (issue number, type, one line).
3. Run `git commit -m "message"`.
4. Never `--no-verify`; fix quality-gate failures instead.

## Example

```bash
git add skills/issue-workflow/
git commit -m "#8: feat: Phase 3 — remaining issue-workflow sub-skills"
```

## Output

Commit hash and short log line.

## Integration

- Runs after [quality-gate](../../quality-gate/SKILL.md).
- Feeds into [integration-pr](../integration-pr/SKILL.md) (push then PR).
