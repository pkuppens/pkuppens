---
name: deployment
description: Orchestrates deployment to target environment; runs build and release checks. Use when deploying artefacts to staging or production.
---

# Deployment

Builds artefacts and releases to target environments per SKILL_TREE §12.

## When to use

- After merge; when releasing to staging or production
- When running deployment pipeline or build checks

## Sub-skills

| Sub-skill | Use when |
|-----------|----------|
| [deployment-build](deployment-build/SKILL.md) (12.1) | Preparing a release; running docker build, uv build, or CI build |
| [deployment-release](deployment-release/SKILL.md) (12.2) | Deploying validated artefacts; running smoke tests; rollback on failure |

## Flow

1. Run [deployment-build](deployment-build/SKILL.md) — build artefact, validate, tag
2. Run [deployment-release](deployment-release/SKILL.md) — deploy to staging → smoke test → promote to production; rollback if needed
3. Post-deploy: [operations-monitoring](../operations/operations-monitoring/SKILL.md)

## Integration

- Follows [integration-merge](../integration/integration-merge/SKILL.md).
- See [COOPERATION.md](../COOPERATION.md) for deployment flow.
