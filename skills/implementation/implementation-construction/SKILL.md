---
name: implementation-construction
description: "Writes new code following Code Complete 2 construction principles: consistent naming, single responsibility, type hints, docstrings, and minimal surface area. Use when implementing a designed component or function; follows design-consult output."
---

# Implementation Construction

Constructs code from a design specification following Code Complete 2 principles. Focuses on correctness, clarity, and consistency — not cleverness.

## When to use

- After [design-consult](../../design/design-consult/SKILL.md) has defined files, classes, and method signatures
- When writing new classes, functions, or modules
- When refactoring existing code to meet construction standards

## Principles (Code Complete 2)

| Principle | Application |
|-----------|-------------|
| **One purpose** | Each function/class does one thing; name reflects it |
| **Minimal surface** | Private by default; expose only what callers need |
| **Intention-revealing names** | Names describe *what*, not *how* |
| **Type hints on all public signatures** | Enables tooling and documents intent |
| **Defensive at boundaries** | Validate at system entry points (API, user input); trust internal code |
| **Short functions** | Target ≤ 20 lines; extract helpers when logic nests 3+ levels |
| **No premature abstraction** | Abstract when you have 3+ concrete cases; not before |

## Instructions

1. **Start from design-consult output** — use the file, class, and method signatures as the skeleton.
2. **Write the signature first** — include type hints and a one-line docstring before the body.
3. **Implement body** — keep it short; extract logic into private helpers if needed.
4. **Match project style** — follow the repo's `pyproject.toml` line length, import style (absolute), and naming conventions.
5. **No TODO stubs without tracking** — if something is deferred, open an issue; do not leave `TODO: implement this`.
6. **Check project toolchain** — run `uv run ruff check .` and `uv run ruff format --check .` before committing.

## Checklist

- [ ] Type hints on all public function signatures
- [ ] Docstring on every public class and function (one line minimum)
- [ ] No `import *`; absolute imports only
- [ ] No mutable default arguments (`def f(x=[])`)
- [ ] Constants at module level, not buried in functions
- [ ] New code follows existing naming conventions in the file

## Output format

Produce the implementation as a code block with the target file path:

```python
# path/to/module/new_thing.py

from module.base import BaseX


class NewThing(BaseX):
    """One-line description of what this does."""

    def method_a(self, param: str) -> int:
        """Returns the length of param after processing."""
        ...
```

## Integration

- Follows [design-consult](../../design/design-consult/SKILL.md).
- Before committing, run [quality-gate](../../quality-gate/SKILL.md).
- After implementation, trigger [validation-draft](../../validation/validation-draft/SKILL.md) if not already done.
