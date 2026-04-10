---
name: maintenance-debt
description: Plans and tracks technical debt work linked to architecture risks. Use when shortcuts accumulate, upgrades are deferred, or debt must be scheduled without blocking delivery forever.
---

# Maintenance debt

Connects **codebase pain** to **tracked work**.

## When to use

- Team agrees something is “debt” but it has no owner
- Upgrade (framework, runtime) is overdue
- Duplication blocks velocity

## Instructions

1. **Describe** the debt in user or developer impact terms.
2. **Link** to [architecture-risks-debt](../../architecture/architecture-risks-debt/SKILL.md) or ADR if exists.
3. **Cost of delay** — incidents, slower features, security.
4. **Proposal** — incremental steps with issues.
5. **Guardrails** — tests or metrics so debt does not return silently.

## Output format

- Issue or epic with acceptance criteria for “debt reduced” (measurable)

## Anti-patterns

- “Refactor everything” without slices that fit milestones
