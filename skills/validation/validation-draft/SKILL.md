---
name: validation-draft
description: Drafts validation steps, BDD scenarios, or test cases from issue acceptance criteria. Use before or during implementation to produce an executable checklist; supports TDD (run before coding) and post-implementation verification.
---

# Validation Draft

Transforms acceptance criteria into an executable validation checklist. Produces concrete steps that any engineer can run without interpretation.

## When to use

- Before implementation (TDD): draft tests and verification steps from acceptance criteria
- During implementation: know exactly what "done" looks like before writing code
- After implementation: verify all criteria are met before opening a PR

## Instructions

1. **Read acceptance criteria** — each `- [ ]` checkbox in the issue is a criterion to validate.
2. **For each criterion**, produce:
   - The **command or action** to execute (exact CLI command, URL + click path, or test invocation)
   - The **expected result** (exit code, output text, UI state, response body)
3. **Identify test type** — unit test, integration test, manual UI flow, or CLI smoke test.
4. **Order by dependency** — infrastructure first (app starts), then feature tests, then edge cases.
5. **Flag untestable criteria** — if a criterion cannot be validated automatically, flag it for manual review.

## Validation step format

```markdown
### [Criterion summary]
**Type:** unit | integration | manual | smoke
**Command / action:**
```bash
<exact command>
```
**Expected result:** [What to observe — exit code, output, UI state]
```

## BDD scenario format (optional)

For feature-level criteria, use Gherkin when it aids clarity:

```gherkin
Given [precondition]
When  [action]
Then  [expected outcome]
```

## Example

**Criterion:** "`uv run pytest -v --cov=. --cov-fail-under=80` exits 0; new modules covered"

```markdown
### Tests pass with ≥80% coverage
**Type:** integration
**Command:**
```bash
cd backend && uv run pytest -v --cov=. --cov-fail-under=80
```
**Expected result:** Exit 0; coverage report shows ≥80% for new modules.
```

## Output format

Produce a `## Validation Checklist` section suitable for pasting into the issue or a `tmp/validation.md` scratch file:

```markdown
## Validation Checklist

- [ ] [Criterion 1] — `<command>` → [expected result]
- [ ] [Criterion 2] — Open [URL], click [path] → [expected state]
- [ ] [Criterion 3] — `<test command>` exits 0
```

## Integration

- Input: acceptance criteria from [issue-acceptance-criteria](../../issue-workflow/issue-acceptance-criteria/SKILL.md).
- Output feeds: [test-write](../../test/test-write/SKILL.md) and [validation-run](../validation-run/SKILL.md).
- In TDD flow: run *before* [implementation-construction](../../implementation/implementation-construction/SKILL.md).
