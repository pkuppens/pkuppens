---
name: requirements-validate
description: Reviews requirements for clarity, testability, and consistency before design commits. Use when requirements look ambiguous, contradictory, or untestable.
---

# Requirements validate

Quality gate **before** heavy design or coding.

## When to use

- Acceptance criteria use vague words (“fast”, “secure”)
- Two requirements conflict
- Test team cannot derive cases from text

## Instructions

1. **Clarity** — each requirement has one interpretation; mark ambiguities.
2. **Testability** — each can fail/pass in principle (observable).
3. **Consistency** — no contradictions with goals and constraints.
4. **Traceability** — IDs link forward to design/tests when the project requires it.
5. **Outcome** — approve / revise / split issues.

## Output format

- Findings table: ID, problem, suggested fix
- **Verdict:** ready for design | needs revision

## Anti-patterns

- Validating alone without a tester or implementer mindset
