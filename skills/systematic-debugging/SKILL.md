---
name: systematic-debugging
description: Investigates root cause before proposing fixes. Use when facing bugs, test failures, CI failures, unexpected behavior, or performance regressions.
---

# Systematic debugging

## When to use

- A test failed and the cause is not obvious
- CI is red and local reproduction is needed
- The system behaves unexpectedly (including performance regressions)
- A “quick fix” seems tempting but the root cause is unclear

## Core rule

**No fixes without a root cause investigation first.**

## Protocol (four phases)

### Phase 1 — Root cause investigation (collect evidence)

1. **Read the error carefully** (message, stack trace, file/line, environment).
2. **Reproduce consistently**.
   - If it is flaky: capture frequency, timing, and conditions.
3. **Check recent changes** (diff, recent commits, config/dependency changes).
4. **Trace the data flow** from symptom backward to the source value or decision.
   - Prefer fixing at the source, not at the crash site.

### Phase 2 — Pattern analysis (compare)

1. Find a **working example** in the same codebase (similar feature, similar test).
2. List **differences** between working and broken (even small ones).
3. Identify **assumptions** (env vars, file paths, versions, ordering).

### Phase 3 — Hypothesis and test (one variable)

1. Write a **single hypothesis**: “I think X is happening because Y”.
2. Make the **smallest change** to test it (one variable at a time).
3. Re-run the reproduction step.
   - If it fails the same way: revert and form a new hypothesis.
   - Do not stack multiple speculative fixes.

### Phase 4 — Implement fix (lock in)

1. Add or update a **test** that reproduces the bug (where practical).
2. Implement the fix addressing the root cause.
3. Verify:
   - the reproduction now passes
   - the broader suite still passes
4. Summarize what was wrong and why the fix addresses it (short).
## Output format (recommended)

```markdown
## Debugging notes

- Symptom: <what failed / what was observed>
- Repro: <exact command/steps>
- Root cause: <what and where>
- Fix: <what changed>
- Verification: <command> → <pass/fail summary>
```

## Anti-patterns

- “Quick fix now, investigate later”
- Multiple changes at once “to see what works”
- Fixing a symptom without understanding why it happened
- Claiming “fixed” without verification evidence (see [verification-before-completion](../verification-before-completion/SKILL.md))

## Integration

- Use with: [test-run](../test/test-run/SKILL.md), [quality-gate](../quality-gate/SKILL.md)
- Bug reporting: [maintenance-bug-report](../maintenance/maintenance-bug-report/SKILL.md)
