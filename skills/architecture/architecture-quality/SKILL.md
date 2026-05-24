---
name: architecture-quality
description: "Documents quality tree and quality scenarios; maps to requirements (arc42 §10). Use when defining non-functional goals, scenarios, or acceptance of quality attributes."
---

# Architecture Quality

Documents quality goals as scenarios the architecture must satisfy. Aligns with arc42 §10 (quality requirements).

## When to use

- Defining or refining non-functional requirements (performance, security, availability)
- Before major design decisions — test options against quality scenarios
- Pairing with [requirements-goals](../../requirements/requirements-goals/SKILL.md) for top-level goals

## Outputs

- `docs/architecture/10-quality.md` — quality tree and scenarios
- Trace links to requirements and ADRs where decisions affect quality

## Instructions

1. **List quality attributes** — e.g. performance, security, maintainability, usability, compliance.
2. **Build a quality tree** — refine each attribute into measurable sub-topics.
3. **Write scenarios** — stimulus / environment / artefact / response / measure (ISO 25010 style).
4. **Map to requirements** — link scenario IDs to requirement or issue IDs.
5. **Record architecture tactics** — caching, redundancy, authZ — without duplicating full ADR text (link to §9).

## Quality scenario format

```markdown
# Quality (arc42 §10)

## Quality tree
- Performance
  - API latency under load
  - Batch throughput

## Scenarios
| ID | Attribute | Stimulus | Response | Measure |
|----|-----------|----------|----------|---------|
| QS-01 | Performance | 100 RPS sustained | p95 < 200ms | load test |
```

## Integration

- Informs [design](../../design/SKILL.md) and [quality-gate](../../quality-gate/SKILL.md) checks.
- [architecture-risks-debt](../architecture-risks-debt/SKILL.md) when scenarios reveal unacceptable risk.
- Parent: [architecture](../SKILL.md).
