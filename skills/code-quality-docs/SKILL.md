---
name: code-quality-docs
description: Apply comment and documentation standards for Python code. Use when writing docstrings, adding comments, or marking technical debt (TODOs). Ensures explain-why-not-what and traceable debt.
---

# Code Quality: Documentation and Comments

Comments explain **why**, not **what**. Code should be self-documenting.

## Docstrings

- **Write the docstring before implementation.** If you cannot summarize in one sentence, the design is not clear yet.
- **Complete docstrings for public and core functions:** Args, Returns, Raises, and examples for complex functions. Follow your project's function-definition rules (often under `.cursor/rules/`).
- **Explain non-obvious decisions.** If a threshold, chunk size, or algorithm was chosen for a specific reason (benchmark, compliance, environment limit), document it.

### Module and package docstrings (scripts and tooling)

For **CLI modules, data pipelines, and agent-facing packages**, a one-line file header is usually not enough. Prefer a short block at the top of `*.py` that covers:

- **Purpose** — what problem the module solves and who it is for (human vs automation).
- **Processing** — the main steps, inputs, and outputs in order (not a wall of prose).
- **Boundaries** — what is explicitly out of scope, or where personal/sensitive data is expected to live (e.g. gitignored paths).

Function and method docstrings can then stay focused on contracts (Args / Returns / Raises). Dutch (or other) UI strings are fine in user-facing text; keep **identifiers and public API names in English**.

## Comments

- **Do not comment what the code already says.** Remove noise.
- **Explain why** when the reason is not obvious from code alone.

## Technical Debt (TODOs)

- **Prefer task reference:** `# TODO(TASK-NNN): …` or `# TODO(#123): …` when your repo issues map that way
- **Alternative:** One SMART sentence when no task exists yet: unambiguous, actionable, discoverable

Never use a bare `# TODO` without either a task ID or a complete, self-contained description.
