---
name: issue-out-of-scope
description: Defines out-of-scope for an issue to prevent gold-plating and scope creep. Use when drafting or refining an issue.
---

# Issue Out of Scope

Explicitly states what is excluded from the issue to keep scope bounded.

## When to use

- Creating a new issue with non-trivial scope
- Refining an issue that risks scope creep

## Principles

- Be explicit: list items that might be assumed in-scope but are not
- Reference follow-up: "Y (tracked in #NNN)" when another issue exists
- Short list: 1–5 items typically

## Instructions

1. Consider the goal and likely extensions (related features, edge cases, UI polish).
2. List items explicitly excluded. Prefer "X is out of scope" or "Y (tracked in #N)".
3. Keep list concise; avoid explaining why.

## Output format

```markdown
## Out of Scope
- [Item 1]
- [Item 2 — tracked in #NNN if applicable]
```

## Examples

- "Support for DOCX files (tracked in #42)"
- "UI redesign — this issue covers API only"
- "Authentication — assumed existing"
- "Performance optimization — separate follow-up"
