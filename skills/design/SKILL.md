---
name: design
description: Defines detailed design components, interfaces, and data flows. Use when working in lifecycle area 4.x per SKILL_TREE.
---

# Design (orchestrator)

Canonical index: [SKILL_TREE.md](../SKILL_TREE.md) §4.

| Sub-skill | One-line role |
|-----------|----------------|
| [design-consult](design-consult/SKILL.md) (4.1) | Place new code in the right files and layers; single responsibility and correct layering. |
| [design-component-boundaries](design-component-boundaries/SKILL.md) (4.2) | Split modules and define who may depend on whom; stop cycles and clarify data ownership. |
| [design-interfaces](design-interfaces/SKILL.md) (4.3) | Specify APIs, contracts, and schemas between components before coding. |
| [design-data-model](design-data-model/SKILL.md) (4.4) | Model entities, relationships, and invariants for persistence and exposed fields. |

Agents should pick the sub-skill by **intent** (placement vs boundaries vs contracts vs data). If unsure, start with **design-consult** (4.1).

For V pairing, see [v-model-design-verification](../v-model/v-model-design-verification/SKILL.md).
