---
name: test-run
description: Executes the test suite locally or in CI and interprets failures. Use when validating a branch, debugging CI red builds, or checking coverage gates.
---

# Test run

**Signal** from the suite, not ad-hoc manual checks only.

## When to use

- Before push or after pulling `main`
- CI failed; need local reproduction
- Flaky test investigation

## Instructions

1. **Same command as CI** when possible (read workflow file).
2. **Reproduce** failure with minimal filter (`-k`, file path).
3. **Capture** traceback and last green commit if regression.
4. **Coverage** — if project enforces threshold, check report output.
5. **Escalate** — open issue if environmental (containers, secrets).

## Output format

- Pass/fail summary; if fail: root cause hypothesis + next step

## Anti-patterns

- “Works on my machine” without matching CI Python/Node version
