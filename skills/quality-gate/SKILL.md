---
name: quality-gate
description: Runs lint, format, type check, and security scan; enforces pre-commit hooks. Use before every commit and as the final step before opening a PR. Invokes sub-skills (lint, format, type, security) as needed.
---

# Quality Gate

Enforces code quality before commits and PRs. Runs the minimum required checks for the repo's toolchain.

## When to use

- Before every `git commit`
- Before opening a PR
- After implementation to catch style and correctness issues early

## Standard checks

Run these in order (fail fast):

```bash
# 1. Lint — catch style and logic issues
uv run ruff check .

# 2. Format — enforce consistent style
uv run ruff format --check .

# 3. Type check (if configured)
uv run pyright   # or: uv run mypy

# 4. Tests
uv run pytest

# 5. Pre-commit (runs all hooks)
pre-commit run --all-files
```

## Per-check sub-skills

| Sub-skill | Tool | When |
|-----------|------|------|
| [quality-gate-lint](quality-gate-lint/SKILL.md) | ruff check | Every commit |
| [quality-gate-format](quality-gate-format/SKILL.md) | ruff format | Every commit |
| [quality-gate-type](quality-gate-type/SKILL.md) | pyright / mypy | Before PR |
| [quality-gate-security](quality-gate-security/SKILL.md) | bandit / npm audit | Before PR / CI |

## Fix before commit — not after

- Fix lint and format errors immediately; do not `--no-verify`.
- If a pre-commit hook blocks a commit, investigate the root cause — do not bypass.
- If a check is not configured for this repo, skip it and note the gap.

## Repo-specific toolchain

Check the repo's `pyproject.toml` for:
- `[tool.ruff]` — line length, selected rules
- `[tool.pyright]` or `[tool.mypy]` — type checking configuration
- `.pre-commit-config.yaml` — active hooks

## Output

Report pass/fail per check:

```markdown
## Quality Gate Results

- [x] ruff check — clean
- [x] ruff format --check — clean
- [ ] pyright — 2 errors (see below)
- [x] pytest — 42 passed, 0 failed
```

List errors with file and line reference for any failures.

## Integration

- Run after [implementation-construction](../implementation/implementation-construction/SKILL.md).
- Must pass before [integration-commit](../integration/integration-commit/SKILL.md).
