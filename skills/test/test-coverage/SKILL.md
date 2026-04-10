---
name: test-coverage
description: Analyses coverage gaps and adds tests where risk is high. Use when coverage drops on a PR or critical paths lack assertions.
---

# Test coverage

**Risk-based**, not 100% line count for its own sake.

## When to use

- CI reports coverage regression
- New module has no tests
- Refactor needs confidence on untouched branches

## Instructions

1. **Generate** report (`pytest --cov`, `coverage`, Istanbul — match repo).
2. **Identify** high-risk gaps: error paths, permissions, parsing.
3. **Prioritise** tests that would catch real failure modes.
4. **Avoid** testing getters/setters only to bump numbers.
5. **Document** exclusions if the tool supports them (dead code, generated).

## Output format

- Short summary: areas improved, remaining known gaps

## Anti-patterns

- Disabling coverage locally to “pass” CI
