---
name: ideation-reuse-check
description: Searches for existing libraries, patterns, and internal code to reuse before designing from scratch. Use when a new feature might duplicate OSS, platform APIs, or another team module.
---

# Ideation reuse check

Reduces waste by finding **existing** solutions early.

## When to use

- New capability might already exist in the org or ecosystem
- “Build vs buy” is open
- Duplication risk is high (auth, logging, RAG, etc.)

## Instructions

1. **Define the capability** in domain terms (not a tech stack yet).
2. **Search internally** — repos, packages, shared services, ADRs, Slack/docs indexes.
3. **Search externally** — mature OSS, cloud managed services (check license and ops cost).
4. **Record findings:** name, link, fit (good/partial/poor), adoption cost.
5. **Recommend:** reuse, wrap, fork, or build; cite trade-offs.

## Output format

- **Capability:** …
- **Candidates:** table (source, fit, effort, risk)
- **Recommendation:** …

## Anti-patterns

- Starting design docs before a 30-minute search
- Rejecting reuse due to Not Invented Here without cost analysis
