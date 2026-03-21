---
name: code-quality-testing
description: Apply testing efficiency and effectiveness principles. Use when writing tests, reviewing test suites, or improving test coverage. Emphasizes behavioral coverage and mutation-aware assertions.
---

# Code Quality: Testing

Tests are production code. Apply the same quality standards.

## Structure

- **Every test tests one behavior.** A failing test should tell you exactly what broke without reading the test body.
- **Test names are sentences:** `test_chunker_splits_on_sentence_boundary_not_word_boundary` is better than `test_chunker_2`.
- **Test docstrings:** Prefer user-facing phrasing (objective, benefit) for product-facing tests; for utilities, a concise one-liner or full docstring per project standards (often under `.cursor/rules/`).

## Efficiency

- **Prefer narrow, fast unit tests.** Mock external dependencies at boundaries — not deep inside pure logic.
- **Mark slow or external tests** with your project's markers (`slow`, `integration`, `docker`, etc.).
- **Avoid duplication.** Use `parametrize` or shared fixtures when the same shape repeats with small variations.

## Effectiveness

- **Mutation-aware assertions:** Assert specific outcomes. An assertion that passes when the condition is inverted does not test anything.
- **Coverage is a floor, not a goal.** Prefer behavioural coverage over line coverage.
