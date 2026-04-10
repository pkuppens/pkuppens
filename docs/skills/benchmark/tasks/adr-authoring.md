# Benchmark task: ADR authoring

**Skill under test:** architecture-decisions  
**Use when:** Running skill-benchmark on ADR structure and rigor.

**Scope note:** The PostgreSQL vs SQLite scenario below is a **fixed, concrete benchmark prompt** so baseline and skill runs are comparable (same constraints, same scoring). It is **not** a rule for the [architecture-decisions](../../../../skills/architecture/architecture-decisions/SKILL.md) skill itself, which stays **topic-agnostic** for any ADR (framework choice, auth, messaging, etc.). For other benchmark runs, swap the task prompt but keep the same ADR structure expectations.

## Task prompt

Write an Architecture Decision Record for choosing PostgreSQL over SQLite for a new service that must support concurrent writes and row-level security. Include: context, options considered (at least two), decision, consequences (positive and negative), and status.

## Expected coverage

- Context with constraints
- Comparable options with trade-offs
- Clear decision statement
- Consequences for operations and development

## Scoring dimensions

| Dimension | Without skill | With skill |
|-----------|---------------|------------|
| Coverage | — | — |
| Specificity | — | — |
| Correctness | — | — |
| Completeness | — | — |
