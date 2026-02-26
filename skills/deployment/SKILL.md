---
name: deployment
description: Orchestrates deployment to target environment; runs build and release checks. Use when deploying artefacts to staging or production. Sub-skills (12.1, 12.2) tracked for implementation.
---

# Deployment

Builds artefacts and releases to target environments per SKILL_TREE §12.

## When to use

- After merge; when releasing to staging or production
- When running deployment pipeline or build checks

## Sub-skills (to be implemented)

- **deployment-build** (12.1) — Build artefacts (images, bundles); run build pipeline
- **deployment-release** (12.2) — Release to staging/production; rollback if needed

## Placeholder

Until sub-skills exist, run repo-specific build commands (e.g. `uv build`, `docker build`, CI workflow trigger).

## Integration

- Follows [integration-merge](../integration/integration-merge/SKILL.md).
- See [COOPERATION.md](../COOPERATION.md).
