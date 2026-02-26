---
name: issue-estimate
description: Adds T-shirt size (or equivalent) estimate to an issue. Use when drafting or refining an issue for planning and prioritisation.
---

# Issue Estimate

Assigns a size estimate so work can be prioritised and planned.

## When to use

- After work-down and acceptance criteria are clear
- When triaging or planning a sprint

## Size scale

| Size | Effort | Example |
|------|--------|---------|
| XS | &lt; 1 hour | Doc fix, typo |
| S | 1–4 hours | Single file change, one test |
| M | 0.5–2 days | New module, several files |
| L | 2–5 days | Feature with tests, docs |
| XL | 1+ weeks | Cross-cutting, many components |

## Instructions

1. **Consider work-down** — files, tests, docs.
2. **Pick size** — use table above; lean conservative if uncertain.
3. **Add to issue** — include estimate in metadata or a dedicated section.

## Output format

```markdown
## Estimate
**Size:** S | M | L (T-shirt)
**Rationale:** [One line — e.g. "2 files, 1 test, ~4h"]
```

## Integration

- Runs after [issue-work-down](../issue-work-down/SKILL.md).
- Feeds [issue-metadata](../issue-metadata/SKILL.md) for labels (e.g. `size:S`).
