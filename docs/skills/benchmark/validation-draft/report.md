# Skill Benchmark — validation-draft

**Date:** 2026-04-10  
**Issue:** #58  
**Task:** Draft validation steps from acceptance criteria for a feature issue (REST endpoint + tests).

*Committed benchmark per [validation/skill-benchmark](../../../skills/validation/skill-benchmark/SKILL.md). Raw session outputs may live in `tmp/skills/benchmark/validation-draft/` locally.*

## Task prompt

From the following acceptance criteria, produce a numbered validation checklist an engineer can run before merge: (1) POST `/api/v1/items` returns 201 with JSON body matching schema; (2) invalid payload returns 422 with field errors; (3) `uv run pytest` passes; (4) OpenAPI `/docs` lists the new route.

## Scoring (1–5 per dimension)

| Dimension | Without Skill | With Skill | Delta |
|-----------|---------------|------------|-------|
| Coverage | 3/5 | 5/5 | +2 |
| Specificity | 2/5 | 5/5 | +3 |
| Correctness | 4/5 | 5/5 | +1 |
| Completeness | 3/5 | 5/5 | +2 |
| **Total** | **12/20** | **20/20** | **+8** |

## Verdict

**Significant improvement** — with validation-draft, the output maps each acceptance bullet to concrete commands (`curl` examples, pytest invocation, URL for `/docs`) and expected HTTP codes; baseline output stays high-level.

## Key observation

With skill: checklist order follows risk (schema → errors → suite → docs) and names exact verification artefacts. Without skill: bullets repeat the AC text without executable steps.
