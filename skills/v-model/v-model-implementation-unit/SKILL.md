---
name: v-model-implementation-unit
description: Pairs implementation work with unit-level tests. Use when closing the bottom of the V for modules and pure logic. Third person.
---

# V-model: implementation ↔ unit tests

Links **left:** [implementation](../../implementation/SKILL.md) (**7.x**) — especially [implementation-construction](../../implementation/implementation-construction/SKILL.md) — with **right:** fast, isolated tests (**9.1**).

## When to use

- New or changed functions/classes with deterministic behaviour.
- Bug fixes where a unit test should lock the fix.

## Instructions

1. From the issue AC, derive cases (happy, edge, failure); use [validation-draft](../../validation/validation-draft/SKILL.md) if helpful.
2. Add or update tests with [test-write](../../test/test-write/SKILL.md); run [test-run](../../test/test-run/SKILL.md) or project test command.
3. Run [quality-gate](../../quality-gate/SKILL.md) before commit.

## TDD variant

If the team uses test-first ordering, write **9.1** before finishing **7.1** for that change set (see [COOPERATION.md](../../COOPERATION.md) TDD flow).

## Related

- [v-model-design-verification](../v-model-design-verification/SKILL.md) for boundary-heavy code
- [v-model-retrofit](../v-model-retrofit/SKILL.md) when legacy code lacks tests
