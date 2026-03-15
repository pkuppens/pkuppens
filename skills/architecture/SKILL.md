---
name: architecture
description: Orchestrates architecture work across three modes. Use when starting a greenfield project, documenting existing code, or evolving architecture; routes to sub-skills (3.2–3.9) by mode.
---

# Architecture

Orchestrates architecture documentation and evolution per arc42. Routes to sub-skills based on **mode**: Initial (greenfield), Retrofitting (document existing), or Evolving (change/extend).

## When to use

- Starting a new (greenfield) project — architecture needed from scratch
- Codebase exists but lacks architecture docs — need to infer and document
- Adding a feature or changing architecture — ADRs, building blocks, or risks need updates

## Modes and routing

| Mode | Trigger | Sub-skills invoked |
|------|---------|---------------------|
| **Initial** | Greenfield project, no architecture yet | [architecture-solution-strategy](architecture-solution-strategy/SKILL.md) → [architecture-building-blocks](architecture-building-blocks/SKILL.md) |
| **Retrofitting** | Undocumented codebase | [architecture-document-existing](architecture-document-existing/SKILL.md) (or [architecture-consult](architecture-consult/SKILL.md) variant) |
| **Evolving** | Change or extend existing architecture | [architecture-decisions](architecture-decisions/SKILL.md) → [architecture-risks-debt](architecture-risks-debt/SKILL.md) as needed |

## Flow

1. **Determine mode** — from user intent or context:
   - "Plan a new app" / "Start from scratch" → Initial
   - "Document our architecture" / "Reverse-engineer structure" → Retrofitting
   - "Add feature X" / "Change decision Y" / "Address tech debt" → Evolving

2. **Initial mode**
   - Run architecture-solution-strategy (arc42 §4: goals, approach)
   - Run architecture-building-blocks (arc42 §5: structure, hierarchy)

3. **Retrofitting mode**
   - Run architecture-document-existing to infer and document from code
   - Optionally run architecture-consult to refine placement and constraints

4. **Evolving mode**
   - Run architecture-decisions for new or updated ADRs (arc42 §9)
   - Run architecture-risks-debt when addressing risks or tech debt (arc42 §11)
   - Use architecture-consult when placing new code within existing structure

## Instructions

1. Identify mode from user request (new project vs undocumented vs change).
2. Invoke sub-skills in sequence per mode table above.
3. When unsure, prefer architecture-consult for placement questions; use orchestrator sub-skills for creation or evolution.
4. Reference arc42 sections in `docs/architecture/` and `docs/architecture/adr/` for consistency.

## Output format

Output follows the sub-skill(s) invoked. Orchestrator output summarizes mode and which sub-skills ran:

```markdown
## Architecture: [Mode]

**Mode:** Initial | Retrofitting | Evolving
**Sub-skills run:** [list]
**Artifacts:** [paths to created/updated docs]
```

## Integration

- **Issue-workflow:** Can be triggered during issue creation or revision (see [issue-workflow](../issue-workflow/SKILL.md)). Requirements and implementation plans take architecture concerns into account.
- **Plan / Ask:** Invoked when planning a new system, asking about ADRs, or scoping architectural changes.
- **COOPERATION.md:** See architecture flows for when to trigger and how sub-skills compose.

## Additional sub-skills

| Sub-skill | When |
|-----------|------|
| [architecture-runtime](architecture-runtime/SKILL.md) | Document technical execution paths, sequences |
| [architecture-crosscutting](architecture-crosscutting/SKILL.md) | Define dependency rules, layer boundaries, architecture tests |
| [architecture-glossary](architecture-glossary/SKILL.md) | Maintain ubiquitous language, resolve terminology |

These can be invoked from architecture-document-existing during retrofitting, or directly when needed.
