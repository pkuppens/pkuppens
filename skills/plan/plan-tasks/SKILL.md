---
name: plan-tasks
description: Breaks an issue into ordered tasks or subtasks with clear outcomes. Use when the issue is too large for one PR or when parallel work needs a split.
---

# Plan tasks

Produces **ordered** work units (not estimates only — see [issue-estimate](../../issue-workflow/issue-estimate/SKILL.md)).

## When to use

- Implementation plan or epic needs decomposition
- You must show progress in checkpoints
- Multiple agents or devs will work in sequence

## Instructions

1. **Goal** — from issue one-liner.
2. **Tasks** — each finishes with a verifiable artefact (code, test, doc).
3. **Order** — respect dependencies (schema before API before UI, etc.).
4. **Map** to files or modules when known.
5. **Out of scope** — defer to linked issues.

## Output format

- Numbered list; optional checkboxes for tracking

## Anti-patterns

- Tasks that are “continue” or “misc” (not verifiable)
