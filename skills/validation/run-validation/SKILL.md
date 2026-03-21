---
name: run-validation
description: Execute an implementation validation file step by step. For each step, run the command or check the UI, compare to the expected outcome, check off passing steps, and document failures. When a step fails, attempt to diagnose and fix the issue, then update the validation with corrected steps or expectations. Use after implementation to verify a feature is complete.
---

# Run Implementation Validation

Reads a validation file, executes each step, tracks pass/fail, and iterates on failures.

Pairs with [create-validation](create-validation/SKILL.md).

## When to Use

- After completing implementation
- Before opening a PR — gate on all steps passing
- During development — partial runs for work-in-progress

## Inputs

The user provides one of:

- An issue number → look for `tmp/github/issue-NNN/validation.md` (or project convention)
- A file path → read that file
- Nothing → list available validation files and ask the user to select

## Execution Protocol

### Phase 1: Load Validation

1. Read the validation file
2. If frontmatter `status` is `passed`, confirm whether to re-run
3. List steps and checkbox state
4. Report title and step counts

### Phase 2: Execute Steps Sequentially

For each unchecked step (in order):

#### 2a. Execute the Action

- **CLI**: Run; capture stdout, stderr, exit code
- **HTTP**: Capture body + status code
- **UI**: Navigate and observe (browser tools if available)
- **File / log**: Read or tail as specified

#### 2b. Compare to Expected

Determine **PASS** or **FAIL**. On PASS, set checkbox to `[x]`. On FAIL, report actual vs expected.

#### 2c. On Failure — Diagnose and Fix

1. **Diagnose:** implementation bug, environment (service down), wrong expectation in file, or outdated command
2. **Fix:** code, start services, or correct the validation file — document why
3. **Re-run** the step after fixes
4. If still blocked, mark blocked and document; stop if a prerequisite step cannot pass

#### 2d. Blocking Failures

If a prerequisite step fails (e.g. app will not start), stop and set overall status `failed`.

### Phase 3: Final Report

Count passed / failed / blocked. Set frontmatter `status` to `passed` or `failed`. Summarize for the user.

### Phase 4: Post-Validation

- If passed: optional `gh issue comment` or checklist updates on the issue
- If failed: list next actions

## Rules

- **Do not skip steps** unless the user explicitly scopes a partial run
- **Do not mark passed** without executing and verifying
- **Document** why an expectation or command was corrected
- **Fix implementation first** — change the validation only when the spec was wrong

## References

- [create-validation](create-validation/SKILL.md)
- [validation-draft](validation-draft/SKILL.md)
