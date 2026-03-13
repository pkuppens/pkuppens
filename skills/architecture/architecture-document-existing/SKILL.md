---
name: architecture-document-existing
description: Infers and documents architecture from an existing codebase. Use when the codebase has no or minimal architecture docs; produces arc42-aligned documentation.
---

# Architecture Document Existing

Infers and documents architecture from an existing codebase. Use when structure exists in code but docs are missing (Retrofitting mode).

## When to use

- Undocumented codebase — need to understand and document structure
- Reverse-engineering for onboarding or maintenance
- Before major refactor — baseline documentation first

## Operating rules (evidence-first)

- **Never ask "what is the project about?"** at the start — infer from code signals first
- **Separate clearly**: Observed Facts vs Assumptions vs Unknowns
- **When evidence conflicts** (README says X, code does Y): document both; prefer code evidence; mark as "Architecture Drift"
- **No fantasy**: if evidence is missing, record as an Open Issue in `99-open-issues.md` rather than inventing
- **Confidence levels**: High (direct code evidence) / Medium (reasonable inference) / Low (assumption)
- **Minimal-diff updates**: prefer small additive changes; keep diffs reviewable

## Evidence sources to scan

- `README.md`, `/docs/*` — project purpose, setup
- `package.json`, `pyproject.toml`, `requirements.txt` — dependencies
- `Dockerfile`, `docker-compose.yml` — deployment topology
- `.github/workflows/` — CI/CD pipeline
- Entry points: `main.py`, `app.py`, `index.ts`
- Module structure: directory layout, imports
- Config files: `.env.example`, `config/`

## Instructions

1. **Infer project purpose** from docs and structure (observe facts, note assumptions)
2. **Build component inventory** — identify backend AND frontend components from package layout
3. **Build abstraction inventory** — find interfaces, protocols, adapter patterns, factory functions
4. **Identify top 2–5 runtime flows** — MVP smoke test path, most frequently executed, business-critical
5. **Detect architecture drift** — new components without docs, dependencies changed without ADR, pattern violations
6. **Produce arc42-aligned docs** — start with §4 (solution strategy), §5 (building blocks), §9 (decisions if ADRs can be inferred)
7. **Create `docs/architecture/`** — if missing, create directory and write inferred sections
8. **Capture unknowns** — write `99-open-issues.md` for anything that can't be inferred

## Output format

Create or update:

- `docs/architecture/00-system-architecture.md` — executive overview (inferred)
- `docs/architecture/04-solution-strategy.md` — inferred from code patterns
- `docs/architecture/05-building-blocks.md` — from package/module structure
- `docs/architecture/adr/` — optional inferred decisions
- `docs/architecture/99-open-issues.md` — unknowns and options

```markdown
# Building Blocks (arc42 §5) — Inferred

## Inferred structure
[From package layout, imports, entry points]

| Path | Responsibility (inferred) | Confidence |
|------|---------------------------|------------|
| `src/backend/` | [inferred from structure] | High/Medium/Low |
| `src/frontend/` | [inferred from structure] | High/Medium/Low |
```

Open issues format:
```markdown
## [Issue Title]
**Context**: What we know
**Question**: What we need to decide
**Options**: 1. A (pros/cons)  2. B (pros/cons)
**Decision**: [when resolved, link to ADR]
```

**Initial baseline guidance:** Produce a "good enough" baseline — 1–2 paragraphs per component initially. Focus on getting structure right; details can evolve. An incomplete baseline today is more useful than a perfect baseline never written.

## Integration

- Retrofitting mode: primary sub-skill.
- Can be followed by [architecture-consult](../architecture-consult/SKILL.md) to refine.
- Parent: [architecture](../SKILL.md) orchestrator.
