---
name: validation-detail
description: Refines validation steps with implementation-specific commands, URLs, and fixtures once code shape exists. Use when moving from high-level checks to an executable checklist before merge.
---

# Validation detail

Bridges [validation-draft](validation-draft/SKILL.md) and [run-validation](run-validation/SKILL.md).

## When to use

- API paths, ports, or feature flags are now known
- You need exact `curl`, CLI, or UI clicks
- Same AC as draft, but concrete

## Instructions

1. **Start from** draft or acceptance criteria bullets.
2. **Replace placeholders** — host, path, test file name, env vars.
3. **Order** — fastest signal first (unit → API → e2e).
4. **Expected** — status codes, JSON keys, log lines.
5. **Hand off** to [create-validation](create-validation/SKILL.md) if the repo commits checklists.

## Output format

- Numbered steps with command blocks and expected output

## Anti-patterns

- Steps that only work on one developer machine (document ports/paths)
