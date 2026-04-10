---
name: plan-dependencies
description: Identifies which tasks block others and surfaces the critical path. Use when parallelisation is possible but ordering mistakes would waste time.
---

# Plan dependencies

Adds **graph** thinking to [plan-tasks](../plan-tasks/SKILL.md).

## When to use

- More than three tasks
- External blockers (API, design, infra)
- You need to explain why task A must precede B

## Instructions

1. **List tasks** (IDs from plan-tasks).
2. **Edges** — A blocks B (finish-to-start).
3. **External** — vendor, reviewer, other team (mark clearly).
4. **Critical path** — longest chain of dependent work.
5. **Float** — tasks that can slip without delaying delivery (if helpful).

## Output format

- List of dependencies (A → B) + critical path summary

## Anti-patterns

- Hidden dependency on a secret manual step (document or automate)
