# Skill Cooperation Patterns

How skills compose: sequential vs parallel flows, triggers, and dependencies.

## Sequential flows

### Issue → Implementation → Integration

```
issue-workflow → plan → architecture (or architecture-consult) → design-consult
  → implementation-construction → quality-gate → integration-commit → integration-pr → integration-merge
```

During issue creation or revision, **architecture** (orchestrator or sub-skills) can be triggered before or during purpose-alignment, work-down, or acceptance-criteria so requirements and implementation plans reflect architecture concerns.

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

## Architecture flows

### Mode-based routing

The [architecture](architecture/SKILL.md) orchestrator routes by mode:

| Mode | When | Sub-skills (sequence) |
|------|------|------------------------|
| **Initial** | Greenfield project | architecture-solution-strategy → architecture-building-blocks |
| **Retrofitting** | Undocumented codebase | architecture-document-existing |
| **Evolving** | Change or extend | architecture-decisions → architecture-risks-debt (as needed) |

### When to trigger architecture

- **Issue creation or revision** — architecture can be triggered before or during purpose-alignment, work-down, or acceptance-criteria. Requirements and implementation plan reflect architecture concerns (ADRs, building blocks, constraints).
- **Plan a new system** — Initial mode.
- **Document existing code** — Retrofitting mode.
- **Place new code or change decision** — architecture-consult (placement) or architecture orchestrator (evolving).

### Sequential vs parallel for architecture

- Sub-skills within a mode run sequentially (e.g. solution-strategy before building-blocks).
- architecture-consult can run in parallel with design-consult when both placement and design are needed.

## Trigger conditions

| When | Trigger |
|------|---------|
| New feature idea | issue-workflow |
| New feature idea (architectural) | architecture orchestrator (Initial/Retrofitting/Evolving) |
| Issue creation or revision | issue-workflow; may invoke architecture before/during purpose-alignment, work-down, acceptance-criteria |
| Before adding code | architecture-consult, design-consult |
| After design | implementation-construction |
| Before commit | quality-gate |
| After quality-gate | integration-commit |
| After merge | maintenance-cleanup (optional) |

## Skill references

Skills link to each other via `[skill-name](path/SKILL.md)`. Forward references to not-yet-implemented skills are acceptable (e.g. validation-run, test-write).
