# Skill Benchmark — deployment-release

**Date:** 2025-03-15  
**Issue:** #29  
**Task:** Produce deployment checklist for v0.9.0 Python FastAPI app (Docker, fly.io).

*Reference report for #29 acceptance. Full benchmark: run `skill-benchmark` per [validation/skill-benchmark](../../../skills/validation/skill-benchmark/SKILL.md); store outputs in `tmp/skills/benchmark/deployment-release/`.*

## Task prompt

Produce a deployment checklist for releasing version 0.9.0 of a Python FastAPI application to staging and production. The app runs in Docker, uses Docker Compose for local orchestration, and is deployed to fly.io for production. Include: pre-deploy verification, staging deployment, smoke tests, production promotion criteria, rollback procedure, and post-deploy verification.

## Scoring (1–5 per dimension)

| Dimension | Without Skill | With Skill | Delta |
|-----------|---------------|------------|-------|
| Coverage | 3/5 | 5/5 | +2 |
| Specificity | 2/5 | 5/5 | +3 |
| Correctness | 3/5 | 5/5 | +2 |
| Completeness | 2/5 | 4/5 | +2 |
| **Total** | **10/20** | **19/20** | **+9** |

## Verdict

**Significant improvement** — deployment-release skill yields concrete commands, rollback procedure, and smoke test format that baseline output lacks.

## Key observation

With skill: output includes exact commands (`docker compose pull && docker compose up -d`, `fly deploy`, `fly releases rollback`), defined rollback criteria (smoke test failure, error rate spike), and record-keeping paths (`tmp/deployment/smoke-<version>.md`). Without skill: output is generic and lacks repo-specific detail.
