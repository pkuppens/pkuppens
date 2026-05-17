---
name: architecture-deployment
description: "Documents deployment topology: infrastructure, containers, and mapping of software to infra (arc42 §7). Use when describing how the system is deployed or updating deployment docs."
---

# Architecture Deployment

Documents how software is mapped to infrastructure. Aligns with arc42 §7 (deployment view).

## When to use

- Greenfield: first deployment topology for a new system
- New environments (staging, DR) or hosting changes
- Before release work — align with [deployment-release](../../deployment/deployment-release/SKILL.md)

## Outputs

- `docs/architecture/07-deployment.md` — deployment view narrative
- `docs/architecture/diagrams/deployment.mmd` — optional topology diagram (Mermaid)

## Instructions

1. **Inventory runtime units** — services, workers, databases, queues, object storage, CDN.
2. **Map to infrastructure** — hosts, regions, clusters, serverless, managed services.
3. **Document environments** — dev, staging, production; what differs (scale, secrets, URLs).
4. **Show communication** — ingress, egress, VPC/subnet boundaries, TLS termination.
5. **Link building blocks** — each deployable maps to a component from §5.
6. **Note operational hooks** — health checks, config sources, secrets management (no secret values in docs).

## Deployment doc format

```markdown
# Deployment (arc42 §7)

## Environments
| Environment | Purpose | Hosting |
|-------------|---------|---------|

## Topology
[Diagram or bullet list: nodes and connections]

## Mapping: software → infrastructure
| Component | Artifact | Runtime | Notes |

## Cross-cutting deployment concerns
- Scaling, backups, DR, observability endpoints
```

## Integration

- Complements [architecture-building-blocks](../architecture-building-blocks/SKILL.md) (what) with where/how it runs.
- [deployment-build](../../deployment/deployment-build/SKILL.md) and [deployment-release](../../deployment/deployment-release/SKILL.md) execute releases; this skill documents the target topology.
- Parent: [architecture](../SKILL.md).
