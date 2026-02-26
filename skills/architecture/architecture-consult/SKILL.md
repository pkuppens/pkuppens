---
name: architecture-consult
description: Consults current architecture docs, ADRs, and codebase to identify relevant components, modules, and files. Use before adding a feature, scoping a change, or placing new code; surfaces constraints and existing decisions.
---

# Architecture Consult

Reads project architecture documentation and codebase to answer: *where does this change belong, and what constraints apply?*

## When to use

- Before starting implementation of a new feature or fix
- When scope of a change is unclear (which modules, which layers)
- When an ADR or prior decision may constrain the approach

## Instructions

1. **Locate architecture docs** — check `docs/architecture/` for arc42 sections (01–12) and `docs/architecture/adr/` for ADRs.
2. **Read CLAUDE.md** — project-level CLAUDE.md contains module boundaries, key patterns, and critical rules.
3. **Identify relevant building blocks** — use codebase search (`rg`, `gh`, file tree) to find existing modules, classes, or services that touch the feature area.
4. **Check ADRs** — scan ADR index (`09-decisions.md` or `adr/`) for decisions that constrain the approach (e.g. "use async-first", "SQLAlchemy 2.0 style").
5. **Map placement** — state which module/package/file the change belongs in, and which layer (route → service → repository → provider).
6. **Surface constraints** — list any ADRs, patterns, or rules that apply (toolchain, naming, style, testing).

## Output format

```markdown
## Architecture Consult: [Feature/Change]

### Relevant components
- `module/path/` — [role]
- `module/path/file.py` — [what it does]

### Applicable ADRs / decisions
- ADR-NNN: [title] — [constraint it imposes]

### Placement recommendation
[One paragraph: where to add code, which layer, which files to create/modify]

### Constraints
- [Rule or pattern that applies]
```

## Integration

- Read `docs/architecture/` sections relevant to the domain (§5 building blocks, §8 crosscutting, §9 decisions).
- Use `rg <term> --type py` or `gh` to locate existing implementations.
- Compose with [design-consult](../../design/design-consult/SKILL.md) for detailed placement.
