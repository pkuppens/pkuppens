---
name: create-validation
description: Create an implementation validation document for a feature or issue. Produces a step-by-step checklist with exact commands, URLs, and expected outcomes. Use after implementation planning or before PR creation to define how the feature can be verified end-to-end.
---

# Create Implementation Validation

A validation document proves an implementation is complete. It is executable: each step is a concrete action (command, URL, UI check) with an explicit expected outcome.

Works with [validation-draft](../validation-draft/SKILL.md) (criteria → steps) and [run-validation](../run-validation/SKILL.md) (execute the checklist).

## When to Use

- After planning is complete — create validation so it guides implementation
- Before creating a PR — validate against the spec
- When acceptance criteria must be verified, not only asserted

## Format

If your project defines a schema (e.g. `docs/technical/VALIDATION_FORMAT.md`), follow it. Otherwise use the step structure below.

## Storage

| Scope | Typical location |
|-------|------------------|
| Issue-scoped (ephemeral) | `tmp/github/issue-NNN/validation.md` or project scratch layout |
| Feature-scoped (committed) | `docs/validations/<feature>-validation.md` |

Default to ephemeral scratch unless the user asks for a committed validation.

## How to Create a Validation

### 1. Gather Context

Read: issue acceptance criteria, implementation plan, API docs, ports, and run commands from the repo README or `CLAUDE.md`.

### 2. Identify Validation Steps

Map each acceptance criterion to verifiable steps:

- **Does it run?** → test command
- **Does the API respond correctly?** → HTTP request with expected status + body
- **Is the UI visible/functional?** → URL + what to click or observe
- **Does it integrate?** → end-to-end scenario

### 3. Write Steps

Each step must have:

- **Action**: exact command or exact UI instruction
- **Expected**: explicit outcome (exit code, output substring, HTTP code — not "it works")
- **Checkbox**: `- [ ] Step passed`

**Step ordering**: simple → complex; unit → integration → end-to-end.

### 4. Prerequisites

List what must be running before step one, with commands to start services if needed.

### 5. Goal

One sentence: what this validation proves.

## Quality Bar

- Executable by someone who did not write the code
- No ambiguous expectations ("visible", "works" without specifics)
- Covers the critical path, not every edge case

## Example Step (Good vs Bad)

**Bad:** "Upload a file. Expected: works."

**Good:** Exact `curl` or UI path, expected HTTP code and JSON fields (or UI state).

## References

- [run-validation](../run-validation/SKILL.md) — executes this checklist
