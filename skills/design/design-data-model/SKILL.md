---
name: design-data-model
description: Describes entities, relationships, and lifecycle rules for persistence and APIs. Use when adding tables, migrations, or shared DTOs that must stay consistent.
---

# Design data model

Complements **interfaces** with **state** shape.

## When to use

- New tables or collections
- Entity relationships (1:N, M:N) affect API and queries
- Soft delete, audit columns, or multi-tenancy keys

## Instructions

1. **Entities** — name, purpose, primary key.
2. **Relationships** — cardinality; foreign keys or references.
3. **Invariants** — uniqueness, cascades, not-null rules.
4. **Migration stance** — expand/contract; backward compatibility window.
5. **Link** to [design-interfaces](../design-interfaces/SKILL.md) for exposed fields.

## Output format

- ER description or bullet model; optional Mermaid `erDiagram` if the repo uses it

## Anti-patterns

- Data model without ownership (who writes which entity?)
