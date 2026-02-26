# Skill Cooperation Patterns

How skills compose: sequential vs parallel flows, triggers, and dependencies.

## Sequential flows

### Issue → Implementation → Integration

```
issue-workflow → plan → architecture-consult → design-consult
  → implementation-construction → quality-gate → integration-commit → integration-pr → integration-merge
```

Each step produces output for the next. No parallelism within this chain.

### TDD flow

```
issue-acceptance-criteria → validation-draft → test-write → implementation-construction → validation-run
```

Validation and tests are drafted before implementation.

## Parallel (independent) skills

These can run in any order or in parallel when context is ready:

- **ideation** (1.1–1.3) — brainstorm, SWOT, reuse-check
- **issue-workflow** sub-skills (5.1–5.7) — some can run in parallel (e.g. estimate + metadata after acceptance criteria)
- **quality-gate** sub-checks — lint, format, type, security (run in order but conceptually independent)

## Trigger conditions

| When | Trigger |
|------|---------|
| New feature idea | issue-workflow |
| Before adding code | architecture-consult, design-consult |
| After design | implementation-construction |
| Before commit | quality-gate |
| After quality-gate | integration-commit |
| After merge | maintenance-cleanup (optional) |

## Skill references

Skills link to each other via `[skill-name](path/SKILL.md)`. Forward references to not-yet-implemented skills are acceptable (e.g. validation-run, test-write).
