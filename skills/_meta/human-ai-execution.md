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

## External skills

Some workflow steps rely on skills **not in this repo** — install separately via [Skills CLI](https://github.com/vercel-labs/skills) or [skills.sh](https://www.skills.sh/). Install and listing conventions: [skills/README.md § External and vendor skills](../README.md#external-and-vendor-skills).

| Skill | Role in this workflow | Reference |
|-------|----------------------|-----------|
| **triage** | Classify issues; post Agent Brief; apply `execution:ai-ok` before AFK coding | <https://www.skills.sh/mattpocock/skills/triage> |
| **grill-with-docs** | Sharpen vague requirements; resolve terms against `CONTEXT.md`; produce detailed acceptance criteria before coding | <https://www.skills.sh/mattpocock/skills/grill-with-docs> |

## Relation to skills

- [v-model](../v-model/SKILL.md) and [v-model-retrofit](../v-model/v-model-retrofit/SKILL.md) often produce **human-review** artefacts (tests and docs that encode intent).
- [issue-workflow](../issue-workflow/SKILL.md) should still define clear acceptance criteria; humans remain accountable for what “done” means in regulated contexts.
- After external **triage** marks an issue ready for agents (`execution:ai-ok`, Agent Brief comment), [issue-coding](../issue-workflow/issue-coding/SKILL.md) runs the TDD inner loop; [integration](../integration/SKILL.md) follows human merge review.
