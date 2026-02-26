---
name: issue-work-down
description: Identifies work-down from other issues, existing code, and tests; scopes the issue. Use when drafting or refining an issue to avoid duplicate work and clarify boundaries.
---

# Issue Work Down

Decomposes the issue into actionable work items by linking to existing code, tests, and related issues.

## When to use

- After purpose alignment and before acceptance criteria
- When an issue spans multiple files or has dependencies on other work

## Instructions

1. **Search related issues** — `gh issue list --search "term" --state open`; note blocking or overlapping issues.
2. **Search codebase** — use `rg`, file tree, or IDE search for modules, classes, or files the change touches.
3. **Identify work-down** — list concrete items: files to create/modify, tests to add, issues to unblock.
4. **Scope boundary** — state what is in-scope vs deferred (hand off to issue-out-of-scope).

## Output format

```markdown
## Work Down
- **Related issues:** #N (blocks), #M (overlaps — narrow)
- **Files to modify:** `path/to/file.py`, `path/to/test_*.py`
- **New files:** `path/to/new_module.py`
- **Tests:** add/update in `tests/test_*.py`
- **Deferred:** [items for follow-up issues]
```

## Example

For "Add BM25 retrieval to RAG pipeline":
- Related: #12 (refactor retrievers)
- Modify: `backend/retrievers/base.py`, `backend/retrievers/bm25.py`
- Tests: `tests/test_bm25_retriever.py`

## Integration

- Runs after [issue-purpose-alignment](../issue-purpose-alignment/SKILL.md).
- Feeds [issue-acceptance-criteria](../issue-acceptance-criteria/SKILL.md) and [issue-estimate](../issue-estimate/SKILL.md).
