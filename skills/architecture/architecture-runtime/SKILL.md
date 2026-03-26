---
name: architecture-runtime
description: "Documents runtime behaviour: technical execution paths, component interactions, sequences (arc42 §6). Use when documenting flows or tracing execution."
---

# Architecture Runtime

Documents technical execution paths through components and services. Aligns with arc42 §6 (runtime view). Contrast with **user flows** (UX journey) — see [design-consult](../../design/design-consult/SKILL.md) for user flow documentation.

## When to use

- Documenting critical execution paths
- When new features add significant flows
- Debugging complex interactions

## Outputs

- `docs/architecture/03-runtime-flows.md` — append/update scenario
- `docs/architecture/diagrams/sequences.mmd` — sequence diagram

## Flow scenario format

For each scenario in `03-runtime-flows.md`:

1. **Trigger** — what initiates; entry point; preconditions
2. **Step-by-step** — technical sequence (HTTP → Controller → Service → DB)
3. **Components involved** — links to component docs
4. **Data touched** — tables, cache, external APIs
5. **Error handling** — what can fail; retries; fallbacks
6. **Observability** — logs, metrics, traces

## Selection criteria

Prioritise: MVP smoke test path; most frequently executed; business-critical; complex (multi-component); error-prone.

## Sequence diagram

Use Mermaid `sequenceDiagram` with participants, messages, returns, error paths.

## Update rules

- Document actual code paths; cite evidence
- Link to component docs
- Show success and error paths

## Integration

- Parent: [architecture](../SKILL.md).
- Complements [architecture-building-blocks](../architecture-building-blocks/SKILL.md) for component details.
