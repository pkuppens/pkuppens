---
name: design-interfaces
description: Specifies APIs, contracts, and schemas between components. Use when defining REST or RPC shapes, event payloads, or shared DTOs between modules.
---

# Design interfaces

Keeps **contracts** explicit before implementation.

## When to use

- Two services or layers must agree on a message shape
- Breaking API changes need versioning notes
- You generate OpenAPI / protobuf from design

## Instructions

1. **Identify callers and callees** (from [design-component-boundaries](../design-component-boundaries/SKILL.md)).
2. **Operations** — methods, paths, or topics; idempotency, errors.
3. **Schemas** — types, required fields, validation rules.
4. **Versioning** — URL, header, or topic version strategy.
5. **Compatibility** — what old clients may still send.

## Output format

- Tables or OpenAPI-style sections per endpoint/event

## Anti-patterns

- “Same as before” without diffing old contract (silent drift)
