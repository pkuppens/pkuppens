---
name: code-review
description: Structured pull-request review checklist (imports, module headers, domain-neutral compliance language, naming). Use after opening a PR or when reviewing merged changes for lessons learned.
---

# Code review (PR)

Use this skill for **human or AI-assisted** review of a pull request before merge, or for a **post-merge** retrospective to capture recurring gaps.

## When to use

- After [integration-pr](../integration/integration-pr/SKILL.md) opens a PR and before [integration-merge](../integration/integration-merge/SKILL.md).
- When validating reviewer feedback against the branch (or `main` after merge).
- When consolidating **lessons learned** into team habits (document in the repo or a retrospective note if the review surfaces process issues).

## Position in the workflow

1. Implementation and tests are in place.
2. [quality-gate](../quality-gate/SKILL.md) passes locally (or CI is green).
3. PR is opened ([integration-pr](../integration/integration-pr/SKILL.md)).
4. **Run this checklist** on the diff (or on files touched).
5. Address findings; re-run quality-gate if needed.
6. Merge when approved ([integration-merge](../integration/integration-merge/SKILL.md)).

Reason: CI catches many issues, but conventions below are easy to miss in large security or compliance PRs.

## Checklist

### 1. Module headers (Python)

- [ ] **New or heavily changed** modules have a short **module docstring** at the top: purpose, main responsibilities, and where the module sits in the architecture (one short paragraph).
- [ ] Avoid files that jump straight into `import` with no context when the module is non-trivial (services, middleware, API entrypoints).

See [code-quality-docs](../code-quality-docs/SKILL.md) for docstring and comment standards.

### 2. Imports: one source root

- [ ] Prefer **absolute** imports from the project’s single package root (e.g. `from backend.some_package.module import ...`).
- [ ] Do not mix **`from backend...`**, **`from src.backend...`**, and deep **relative** imports (`from ..x import y`) in the same file unless the repo explicitly allows an exception.
- [ ] Align with the target repo’s `.cursor/rules` or `CLAUDE.md` (example: on-prem RAG uses `backend.*` from `src/` layout).

Reason: mixed roots confuse reviewers and break refactors.

### 3. Domain language in shared code

- [ ] Shared middleware, security notes, and compliance-oriented comments use **neutral** terms where possible: **auditability**, **traceability**, **compliance**, **regulated environments** — not a single sector (e.g. “banking-only”) unless the artifact is explicitly scoped to that domain.

Reason: the same controls often apply to healthcare, finance, and public sector; sector-specific wording belongs in sector-specific docs or ADRs.

### 4. Naming conventions

- [ ] **`logger` vs `_logger`**: Prefer `logger = logging.getLogger(__name__)` at module level for readability unless the repo mandates a private prefix.
- [ ] **Leading underscore** on module-level names usually means “internal by convention,” not “name collision avoidance.” If the only goal is to avoid clashing with a standard library name, prefer a clearer name (e.g. `logger` does not clash with the `logging` module).
- [ ] **`import foo as _foo`**: Often used to avoid re-export or to mark optional/heavy imports; do not mix unrelated underscore styles in one file without reason.

Document team choice in the repo if reviewers repeatedly disagree.

### 5. Security and compliance (spot check)

- [ ] Cryptographic choices (password hashing, JWT validation, secrets) match the PR’s claims and tests.
- [ ] **No secrets** in source; secret-scanning hooks or CI are respected when present.
- [ ] Logging does not print **full tokens** or PII without policy alignment (truncate or hash where required).

### 6. Tests

- [ ] New behavior has tests; security-sensitive paths have **negative** tests (invalid token, wrong algorithm, etc.) where applicable.

## Lessons learned (example: on_prem_rag PR #151)

The following came from a real security/compliance hardening PR; they are now part of this checklist:

- Add **module headers** where reviewers asked for parity with well-documented neighbors (e.g. middleware next to other middleware).
- Replace **sector-specific** phrasing with **auditability / compliance** language in shared components.
- Enforce **one import style** per file for `app.py`-style entrypoints.
- Align **`_logger`** / **`logger`** with project readability goals, not only PEP 8 “internal” habits.

## Integration

- **Documentation depth**: [code-quality-docs](../code-quality-docs/SKILL.md).
- **Construction habits**: [implementation-construction](../implementation/implementation-construction/SKILL.md).
- **PR workflow**: [integration](../integration/SKILL.md), [integration-pr](../integration/integration-pr/SKILL.md).
- **Before merge**: [quality-gate](../quality-gate/SKILL.md).

## References

- Agent Skills specification (frontmatter for `SKILL.md`): https://agentskills.io/specification
