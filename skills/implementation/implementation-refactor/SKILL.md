---
name: implementation-refactor
description: Restructures code without changing observable behaviour. Use when reducing duplication, improving names, or preparing for a feature while keeping tests green.
---

# Implementation refactor

**Behaviour preserved** — if outputs change, that is a **fix** or **feature**, not this skill.

## When to use

- Tests exist and pass; structure is hard to extend
- Duplication or long methods block safe changes
- You need a mechanical rename/move before new logic

## Instructions

1. **Baseline** — run tests; commit or stash so you can diff behaviour.
2. **Small steps** — one refactor per commit when possible.
3. **Mechanical first** — extract function, rename, move file; no mixed behaviour edits.
4. **Re-run tests** after each meaningful step.
5. **Stop** if tests fail — revert or fix without adding features.

## Output format

- Short log of steps; PR should be reviewable as “move-only” where possible

## Anti-patterns

- “Refactor” mixed with bug fix in the same commit (hard to review)
- No tests (add minimal coverage first or use characterization tests)
