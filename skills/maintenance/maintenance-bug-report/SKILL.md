---
name: maintenance-bug-report
description: Captures reproduction steps, expected versus actual behaviour, and environment for a defect. Use when filing or enriching an issue from user feedback or an incident.
---

# Maintenance bug report

Makes bugs **actionable** for [issue-workflow](../../issue-workflow/SKILL.md).

## When to use

- User reports “it broke”
- CI flaky failure needs a ticket
- Incident post-mortem spawns a fix issue

## Instructions

1. **Summary** — one sentence, outcome-focused.
2. **Reproduce** — numbered steps or minimal script.
3. **Expected vs actual** — observable.
4. **Environment** — OS, version, commit SHA, feature flags.
5. **Severity / scope** — who is affected.
6. **Attachments** — logs (redact secrets), screenshots if UI.

## Output format

- Issue body ready to paste; link to related PRs if regression

## Anti-patterns

- “Doesn’t work” without version or steps
