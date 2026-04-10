---
name: test-write
description: Adds or updates automated tests at unit, integration, or end-to-end level. Use when implementing behaviour, fixing bugs, or locking a contract with tests.
---

# Test write

Aligns tests with **risk** and **contracts**.

## When to use

- New code paths need regression protection
- Bug fix requires a failing-then-passing test
- API or schema is stabilising

## Instructions

1. **Pick level** — unit for pure logic; integration for DB/HTTP; e2e for critical journeys.
2. **Name** tests for behaviour, not implementation detail.
3. **Arrange / act / assert** (or project equivalent).
4. **Data** — factories or fixtures; no secrets in repo.
5. **Run** via repo standard (`uv run pytest`, `npm test`, …).

## Output format

- Test files + how to run the focused subset

## Anti-patterns

- Tests that assert only “no exception” for complex flows
