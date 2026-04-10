---
name: governance-post-mortem
description: Runs a blameless review after incidents or major misses to capture causes and follow-up work. Use when production broke, a release failed, or a project lesson should be institutionalized.
---

# Governance post-mortem

Structured learning after **failure or near-miss** (not only outages).

## When to use

- Incident resolved ([operations-incident](../../operations/operations-incident/SKILL.md) handoff)
- Missed deadline with systemic cause
- Retro at sprint end when something repeatedly hurt velocity

## Instructions

1. **Timeline** — facts only (UTC), what changed when.
2. **Impact** — users, data, SLAs.
3. **Root causes** — 5-whys or equivalent; avoid naming individuals.
4. **What went well** — detection, recovery, comms.
5. **Action items** — owner, issue link, due date; track in [issue-workflow](../../issue-workflow/SKILL.md).

## Output format

- Summary (5–10 lines)
- Timeline
- Root causes / contributing factors
- Actions (table)

## Anti-patterns

- Blame-focused language (blocks honest analysis)
- “We’ll be more careful” without tracked actions
