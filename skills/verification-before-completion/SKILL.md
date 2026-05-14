---
name: verification-before-completion
description: Requires evidence before claiming work is done or fixed. Use before commit/PR, before telling a user “it works”, or when closing a task.
---

# Verification before completion

## When to use

- Before saying: “done”, “fixed”, “works”, “passes”, “ready to merge”, “ready for PR”
- Before `integration-commit` or `integration-pr`
- After delegating work to another agent (verify independently)

## Core rule

**Do not claim success without fresh evidence.**

Evidence means:

- The exact verification command was executed
- The outcome was observed (exit code, pass/fail counts, or expected UI state)

## Gate checklist

Before any completion claim:

1. **Identify** the command (or manual check) that proves the claim.
   - Examples: `uv run pytest`, `uv run ruff check .`, open a URL and confirm a UI state
2. **Run** the full check (fresh).
3. **Read** the output carefully.
4. **Report** the evidence (short and concrete).
5. **Only then** state the conclusion.

## Output format (recommended)

Use this shape in chat, issues, or PR descriptions:

```markdown
## Verification evidence

- [ ] <check name> — `<command>` → <result summary>
```

Examples:

```markdown
## Verification evidence

- [x] Tests — `uv run pytest` → 42 passed, 0 failed (exit 0)
- [x] Lint — `uv run ruff check .` → clean (exit 0)
```

## Common failure modes

- “It should work now” (confidence is not evidence)
- “It passed earlier” (stale evidence)
- Only running a subset of checks without stating the scope
- Claiming a bug is fixed without reproducing the original symptom

## Integration

- Strengthens: [quality-gate](../quality-gate/SKILL.md), [run-validation](../validation/run-validation/SKILL.md)
- Use before: [integration-commit](../integration/integration-commit/SKILL.md), [integration-pr](../integration/integration-pr/SKILL.md)
