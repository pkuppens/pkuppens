---
name: governance-progress
description: Updates workflow state, milestone notes, and handoff context so the next person or agent can continue without rediscovery. Use when a slice finishes, a sprint ends, or ownership changes.
---

# Governance progress

Keeps **visible state** aligned with reality.

## When to use

- Issue or PR moves between people
- Milestone or epic status changes
- You maintain `tmp/github/` or similar planning notes

## Instructions

1. **State the artifact** — issue #, milestone name, branch, or doc path.
2. **Done / in progress / blocked** — one line each with owner.
3. **Next actions** — ordered, with links (issue, PR, ADR).
4. **Handoff** — what the reader must know (secrets, flags, env).

## Output format

- **Current state:** …
- **Next:** numbered list with links
- **Risks:** …

## Anti-patterns

- Progress only in chat (lost when threads scroll)
- Duplicate status in three places without a single “source of truth” link
