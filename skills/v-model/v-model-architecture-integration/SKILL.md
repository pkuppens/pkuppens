---
name: v-model-architecture-integration
description: Pairs architecture artefacts with integration and structural verification. Use when boundaries, deployment, or runtime scenarios must be proven in tests. Third person.
---

# V-model: architecture ↔ integration

Links **left:** [architecture](../../architecture/SKILL.md) (**3.x**) — building blocks, runtime, deployment, decisions — with **right:** integration-style verification (**8.x**, **9.x**).

## When to use

- New services, APIs between components, or deployment topology changes.
- Refactors that move boundaries between modules or processes.

## Instructions

1. Consult [architecture-consult](../../architecture/architecture-consult/SKILL.md) or document the target state (**3.x**).
2. Identify **integration surfaces** (HTTP/gRPC/queue/DB contracts, process boundaries).
3. Define tests that fail if those boundaries regress: contract tests, narrow integration tests, or smoke paths; align with [validation-detail](../../validation/validation-detail/SKILL.md) where scenarios are known.
4. Record risky decisions in [architecture-decisions](../../architecture/architecture-decisions/SKILL.md) when verification encodes a specific option.

## Relation to arc42

Runtime (**3.4**) and deployment (**3.5**) views often drive **which** integration tests matter most.

## Related

- [v-model-mapping](../v-model-mapping/SKILL.md)
- [v-model-retrofit](../v-model-retrofit/SKILL.md) for undocumented systems
