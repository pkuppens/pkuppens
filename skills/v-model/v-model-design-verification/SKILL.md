---
name: v-model-design-verification
description: Pairs detailed design with component and contract-level verification. Use when APIs, schemas, or module contracts need proving tests. Third person.
---

# V-model: design ↔ verification

Links **left:** [design](../../design/SKILL.md) (**4.x**) and [design-consult](../../design/design-consult/SKILL.md) with **right:** component-level and contract-level checks (**8.2**, **9.x**).

## When to use

- APIs, data schemas, or internal interfaces are stable enough to test against.
- You need tests that pin behaviour at module boundaries without full system cost.

## Instructions

1. Name the **contract**: inputs, outputs, errors, invariants (from **4.3**, **4.4** when present).
2. Draft checks via [validation-draft](../../validation/validation-draft/SKILL.md); tighten with [validation-detail](../../validation/validation-detail/SKILL.md) after implementation exists.
3. Prefer [test-write](../../test/test-write/SKILL.md) for automated contracts; document any manual-only checks in the issue or runbook.

## Pitfalls

- **Over-mocking:** integration value disappears if everything is mocked — pick the right layer (see [v-model-architecture-integration](../v-model-architecture-integration/SKILL.md)).

## Related

- [v-model-mapping](../v-model-mapping/SKILL.md)
- [implementation-construction](../../implementation/implementation-construction/SKILL.md)
