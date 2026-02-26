---
name: issue-acceptance-criteria
description: Defines acceptance criteria as a minimum baseline of done. Use when drafting or refining an issue; ensures criteria are testable and include copy-pastable validation steps.
---

# Issue Acceptance Criteria

Defines checkboxes that describe "done" for an issue. Per [GitHub Issue Lifecycle](https://docs.github.com/en/issues) and repo CLAUDE.md.

## When to use

- Creating a new issue
- Refining an issue that lacks clear completion criteria

## Principles

- Each criterion is a checkbox: `- [ ] ...`
- **Copy-pastable**: include concrete steps someone can run or click without interpretation
- Testable: verifiable in seconds to minutes
- Minimal: enough to close the issue, not gold-plating

## Copy-pastable validation steps

Every acceptance criterion must include specific steps that can be executed to validate it:

| Criterion type | Copy-pastable form |
|----------------|--------------------|
| CLI / backend | Exact commands, URLs, expected output |
| API docs | Start command, URL, endpoint path, Try-it flow |
| UI / frontend | Open URL, click path, expected result |
| Tests / lint | Exact command(s) and pass condition |

**Bad** (vague): "API docs updated at `/docs`"  
**Good**: "Run `uv run uvicorn backend.main:app`, open http://localhost:8000/docs, `/api/upload` is visible; with Try it, upload a sample PDF and succeed in <5s"

**Bad** (vague): "User can upload PDF and get cited answer"  
**Good**: "From app root, run `uv run uvicorn backend.main:app` and `uv run streamlit run frontend/app.py`. At http://localhost:8501, upload `tmp/sample.pdf`, submit query, cited answer appears within 5s"

**Bad** (vague): "Tests pass with >80% coverage"  
**Good**: "`cd backend && uv run pytest -v --cov=. --cov-fail-under=80` exits 0; new modules covered"

## Instructions

1. From the goal and tasks, list 2–5 criteria that must be true to close the issue.
2. For each criterion, add **copy-pastable validation steps**: commands, URLs, clicks, expected result.
3. Use imperative, verifiable language. Avoid "works", "correct" — specify what to run and what to observe.
4. Include quality gates if relevant: exact lint/test commands.
5. Format as markdown checkboxes.

## Output format

```markdown
## Acceptance Criteria
- [ ] [Criterion: copy-pastable command/URL → expected result]
- [ ] [Criterion: copy-pastable command/URL → expected result]
```

## Examples

- "`cd backend && uv run pytest -v --cov=. --cov-fail-under=80` exits 0; new modules covered"
- "`uv run ruff check . && uv run ruff format --check .` clean"
- "Run `uv run uvicorn backend.main:app`, open http://localhost:8000/docs, `/api/upload` visible; Try it upload of sample PDF succeeds in <5s"
- "Run backend + frontend, open chat UI, upload PDF, ask question; cited answer with source chunks appears within 5s"
