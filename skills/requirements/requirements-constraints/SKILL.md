---
name: requirements-constraints
description: Documents regulations, organisational rules, and technical limits that bound the solution. Use when compliance, legacy systems, or fixed budgets block certain designs.
---

# Requirements constraints

Maps to **arc42 §2** — constraints.

## When to use

- Healthcare, finance, or data residency rules apply
- Must integrate with a locked vendor or mainframe
- Team size, language, or hosting is non-negotiable

## Instructions

1. **Regulatory / policy** — cite standard or internal policy ID when possible.
2. **Technical** — versions, protocols, max latency, browser support.
3. **Organisational** — approval gates, release windows.
4. **Consequences** — what designs are **out** because of each constraint.

## Output format

- Table: constraint, source, hard/soft, impact on architecture

## Anti-patterns

- Hiding “political” constraints until implementation (expensive rework)
