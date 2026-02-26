---
name: architecture-risks-debt
description: Documents risks, technical debt, and mitigation. Use when evolving architecture or addressing tech debt; produces arc42 §11 content.
---

# Architecture Risks and Technical Debt

Documents risks and technical debt. Aligns with arc42 §11: risk register, debt backlog, mitigation.

## When to use

- Evolving architecture — addressing risks or debt
- After major change — capture new risks
- Maintenance — debt reduction planning

## Instructions

1. **Scan existing docs** — `docs/architecture/11-risks-and-debt.md` if present.
2. **Identify risks** — technical, operational, security; likelihood and impact.
3. **List technical debt** — known shortcuts, refactor needs, legacy code.
4. **Add mitigations** — for risks; plan for debt reduction.
5. **Write to arc42 §11 format** — risk register, debt items, mitigation.

## Output format

Write or append to `docs/architecture/11-risks-and-debt.md`:

```markdown
# Risks and Technical Debt (arc42 §11)

## Risk register
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | L/M/H | L/M/H | [Action] |

## Technical debt
- [Debt item]: [where, why, effort]
```

## Integration

- Evolving mode: run with [architecture-decisions](../architecture-decisions/SKILL.md) when needed.
- Links to [maintenance](../../operations/SKILL.md) for debt reduction.
- Parent: [architecture](../SKILL.md) orchestrator.
