---
name: issue-check-duplicates
description: Checks open and recently closed GitHub issues to prevent duplication. Use when drafting a new issue or validating that an idea is not already tracked.
---

# Issue Check Duplicates

Searches related issues before creating a new one to avoid duplicates and surface related work.

## When to use

- Before creating a new issue
- When refining an idea that might overlap existing work

## Instructions

1. Extract key terms from the idea (feature name, bug area, component).
2. Run `gh issue list --repo OWNER/REPO --state open --limit 50` or with `--search "term1 term2"`.
3. Run `gh issue list --repo OWNER/REPO --state closed --limit 20` for recently closed.
4. Compare titles and bodies; note overlaps, supersedes, or related issues.
5. Report: list related issue numbers and recommendation (proceed / merge / close as duplicate).

## Example

```bash
gh issue list --repo pkuppens/on_prem_rag --search "BM25 retrieval" --state all --limit 10
```

## Output

- **No overlap:** Proceed with new issue.
- **Partial overlap:** Link related issues in new issue body; narrow scope.
- **Duplicate:** Do not create; comment on existing issue or close duplicate.
