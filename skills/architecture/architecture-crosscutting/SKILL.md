---
name: architecture-crosscutting
description: Documents crosscutting concepts: dependency rules, layering, and architecture tests. Use when enforcing constraints or detecting architecture drift; produces arc42 §8 content.
---

# Architecture Crosscutting

Documents and enforces architectural constraints: dependency rules, layer boundaries, and architecture test proposals. Aligns with arc42 §8 (crosscutting concepts).

## When to use

- After identifying layering or dependency patterns in code
- When architecture drift is detected
- When onboarding new team members
- To enforce architectural decisions before production

## Evidence sources

Scan for: import/dependency patterns, layer violations (e.g. API calling DB directly), abstraction violations, circular dependencies, forbidden dependencies.

## Outputs

Adds section to:

- `docs/architecture/02-quality-attributes.md` — "Architecture Rules"
- Or `docs/architecture/00-system-architecture.md`
- Optionally: architecture test scaffolding

## Dependency rules format

```markdown
## Architecture Rules

### Allowed Dependencies
- ✅ API → Service → Repository → Database
- ✅ Service → Abstraction (interface)
- ✅ Frontend → API (via client abstraction)

### Forbidden Dependencies
- ❌ API → Repository (must go through Service)
- ❌ Service → Concrete (must use abstraction)
- ❌ Domain → Infrastructure
```

## Layer boundaries

Define layers and rules:

- **Presentation** — MAY depend on Application; MUST NOT depend on Data
- **Application** — MAY depend on Domain, Data (through abstractions only); MUST NOT depend on Presentation
- **Data** — MAY depend on Domain; MUST NOT depend on Application or Presentation

## Architecture test approach

Propose verification (Python: `import-linter`, AST, pytest; TypeScript: `madge`, `dependency-cruiser`). Example:

```python
def test_api_does_not_import_repositories():
    """API routes must not directly import repositories."""
    violations = check_imports(api_modules, repo_modules)
    assert len(violations) == 0
```

## Enforcement levels

1. Documentation only — manual review
2. Linter/static analysis — IDE and CI
3. Architecture tests — blocks merges on violations

## Update rules

- Document actual violations found; cite evidence
- Mark rules as "Enforced" vs "Aspirational"

## Integration

- Parent: [architecture](../SKILL.md) orchestrator.
- Complements [architecture-decisions](../architecture-decisions/SKILL.md) for constraint documentation.
