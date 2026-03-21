# Human vs AI execution (issues and skills)

Use this note when scoping GitHub issues and when agents follow skills that affect **judgment**, **sign-off**, or **compliance**.

## GitHub labels (pkuppens repo)

| Label | When to use |
|-------|-------------|
| `execution:ai-ok` | Safe for an agent to execute end-to-end (e.g. drafting Markdown, scaffolding, link checks). Human merge review is still normal. |
| `execution:human-review` | Agent may draft; a human must approve content, merge, or external sign-off. |
| `execution:human-required` | Human must perform the step (stakeholder decision, regulatory interpretation, production change approval). |
| `retrofit:explicit` | Dedicated backfill / close-the-V scope for a module or system slice. |
| `retrofit:incremental` | Only extend traceability for code **touched** by this issue unless scope is widened. |

## Issue body template (optional)

Add an **Execution** block so ownership stays with the issue, not only on the board:

```markdown
## Execution
- [ ] (ai-ok) …
- [ ] (human-review) …
- [ ] (human-required) …
```

## Relation to skills

- [v-model](../v-model/SKILL.md) and [v-model-retrofit](../v-model/v-model-retrofit/SKILL.md) often produce **human-review** artefacts (tests and docs that encode intent).
- [issue-workflow](../issue-workflow/SKILL.md) should still define clear acceptance criteria; humans remain accountable for what “done” means in regulated contexts.
