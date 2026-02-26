---
name: issue-acceptance-criteria
description: Defines acceptance criteria as a minimum baseline of done. Use when drafting or refining an issue; ensures criteria are testable and verifiable.
---

# Issue Acceptance Criteria

Defines checkboxes that describe "done" for an issue. Per [GitHub Issue Lifecycle](https://docs.github.com/en/issues) and repo CLAUDE.md.

## When to use

- Creating a new issue
- Refining an issue that lacks clear completion criteria

## Principles

- Each criterion is a checkbox: `- [ ] ...`
- Testable: someone can verify without interpretation
- Minimal: enough to close the issue, not gold-plating

## Instructions

1. From the goal and tasks, list 2–5 criteria that must be true to close the issue.
2. Use imperative, verifiable language: "Tests pass for X", "API returns Y when Z".
3. Include quality gates if relevant: lint clean, coverage threshold, docs updated.
4. Format as markdown checkboxes.

## Output format

```markdown
## Acceptance Criteria
- [ ] [Criterion 1 — testable]
- [ ] [Criterion 2 — verifiable]
- [ ] [Criterion 3 — optional quality gate]
```

## Examples

- "Tests pass with >80% coverage on new code"
- "`uv run ruff check .` is clean"
- "API docs updated at `/docs`"
- "User can upload PDF and receive a cited answer within 5s"
