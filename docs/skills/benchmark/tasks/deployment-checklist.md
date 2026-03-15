# Benchmark task: Deployment checklist

**Skill under test:** deployment-release  
**Use when:** Running skill-benchmark on deployment-release.

## Task prompt

Produce a deployment checklist for releasing version 0.9.0 of a Python FastAPI application to staging and production. The app runs in Docker, uses Docker Compose for local orchestration, and is deployed to fly.io for production. Include: pre-deploy verification steps, staging deployment, smoke tests, production promotion criteria, rollback procedure, and post-deploy verification.

## Expected coverage

- Pre-conditions (build artefact, tests, merge status)
- Staging deploy steps (commands)
- Smoke test format (health endpoint, key API)
- Production promotion criteria
- Rollback commands (Docker Compose, fly.io)
- Post-deploy monitoring checklist

## Scoring dimensions

| Dimension | Without skill | With skill |
|-----------|---------------|------------|
| Coverage | — | — |
| Specificity | — | — |
| Correctness | — | — |
| Completeness | — | — |
