---
name: issue-purpose-alignment
description: Ensures issue purpose is focused and aligned with project goals and quality attributes. Use when drafting or refining an issue; surfaces misalignment with arc42 goals or quality tree.
---

# Issue Purpose Alignment

Validates that an issue's purpose matches project goals and quality attributes (arc42 §1, §10).

## When to use

- After clarifying the idea, before drafting full issue
- When refining an issue that may drift from project scope

## Instructions

1. **Locate project goals** — read `docs/architecture/01-introduction-and-goals.md`, `CLAUDE.md`, or README for top 3–5 goals.
2. **Check quality attributes** — scan arc42 §10 or requirements for quality goals (performance, security, maintainability).
3. **Compare** — does this issue advance at least one goal or quality attribute? Does it conflict with any?
4. **Surface misalignment** — if the issue contradicts goals or adds scope outside quality tree, flag it.
5. **Recommend** — narrow scope, add rationale linking to goal, or split into follow-up issues.

## Output format

```markdown
## Purpose Alignment
- **Aligned with:** [Goal or quality attribute from project]
- **Rationale:** [One sentence: how this issue supports it]
- **Misalignments:** (none | [list any conflicts])
```

## Integration

- Runs after [issue-check-duplicates](../issue-check-duplicates/SKILL.md).
- Informs [issue-acceptance-criteria](../issue-acceptance-criteria/SKILL.md) and [issue-out-of-scope](../issue-out-of-scope/SKILL.md).
