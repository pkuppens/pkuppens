# Software Development Discipline (Platform-Agnostic)

This document is the single, platform-independent source of truth for how this repository is developed and reviewed. Procedures here avoid binding to one vendor’s commands or config layout.

Platform-specific guides (command names, exact CI file locations) live beside this doc:

- [GitHub mapping](github.md)
- [Azure DevOps mapping](azure-devops.md) (when available)

## Scope (non-exhaustive examples)

This doc applies regardless of tooling. Common mappings:

| Concern | Examples (not limited to these) |
|---------|----------------------------------|
| Git hosting | GitHub, Azure DevOps Repos, GitLab |
| CI/CD products | GitHub Actions, Azure Pipelines, GitLab CI |
| Work tracking | GitHub Issues, Azure Boards, Jira |

Details for a chosen stack belong in the platform guide, not here.

---

## 1) Issue discipline

Every unit of work starts as an issue that is specific enough for an implementer (human or agent) to execute without extra back-and-forth.

When requirements are still vague, run a structured refinement session before coding. The external [grill-with-docs](https://www.skills.sh/mattpocock/skills/grill-with-docs) skill (or equivalent workshop) helps sharpen acceptance criteria and terminology against project docs. That step is human-in-the-loop and happens **before** implementation.

Refined issue text is also a good **skill-benchmark** candidate: compare baseline output vs output with issue-workflow (or grill-with-docs) skills loaded.

### Title format

Use: `[TYPE]: verb + object`

Common types in this repository: `FEAT`, `TASK`, `BUG`, `STORY`, `EPIC` (and optionally `CHORE`).

### Required sections (minimum)

- **Goal**: one sentence describing the outcome and why it matters
- **Tasks**: a short, numbered list of concrete steps
- **Acceptance Criteria**: copy-pastable checks, as measurable outcomes
- **Context**: dependencies, links, constraints, and any “why” that would otherwise be guessed
- **Out of Scope**: what will not be addressed in this work item
- **Estimate**: T-shirt size (S/M/L) or a short time range
- **Metadata**: ownership/assignee and any repo conventions (labels, milestones, etc.)

### Acceptance Criteria guidance

Acceptance criteria must be testable. Prefer:

- Measurable outcomes (what changes, where to observe it)
- Explicit validation steps (commands, URLs, file paths, or UI checks)
- A clear definition of “done” that does not include “it looks OK”

### Ownership

An issue should have an explicit owner (assignee). If multiple stakeholders are involved, link them in **Context** rather than leaving the implementer guessing.

---

## 2) Branching

### Branch per unit of work (with flexibility)

Default: one branch per issue so review scope stays tight.

Allowed variations:

- **Epic branch** (`epic/NNN-description`) for coordinated work across several child issues; merge only when the epic’s acceptance criteria are met.
- **Feature branch for a parent issue** when child issues land in the same PR sequence; still link every commit to the relevant `#NNN`.
- **Sub-issues** keep their own issue numbers; branch name should reflect the issue you are implementing now, not only the parent epic.

Pick the smallest branch scope that still matches how reviewers will validate the change.

### Branch prefixes

Use consistent prefixes:

- `feature/NNN-description`
- `hotfix/NNN-description`
- `chore/NNN-description`
- `epic/NNN-description`

Where `NNN` is the issue number for the branch’s primary tracking item (feature, task, or epic).

### No direct commits to default branch

Do not push changes directly to `main`/`master` (or any protected default branch). All changes must go through the pull/merge request workflow.

---

## 3) Commit conventions

Commits complement the issue by preserving an auditable history.

### Conventional commits + issue linking

Use `type: description` (e.g. `feat: add workflow doc`) and include a reference to the issue in every commit message (e.g. `#NNN`).

### Explain the intent (what + why)

Write commit messages that make the reason for the change easy to understand later:

- **What** changed
- **Why** it needed to exist

Avoid committing without context; if you need a long explanation, put it in the issue description or PR notes instead.

---

## 4) Pull/merge request workflow

All code and doc changes must be proposed via a pull/merge request and reviewed before merging.

### PR description structure

Use a structured PR description that mirrors the issue discipline:

- Summary (what and why)
- Changes (what files/areas were touched)
- Issue link(s) (which issues this PR closes or relates to)
- Validation evidence (what checks were run and what the result was)

### Review before merge

Do not merge until:

- The PR review is complete
- Quality gates have passed (lint/format/test/security as applicable)
- Any open “Changes requested” items are resolved

---

## 5) Code review checklist

Reviews should focus on correctness, maintainability, and safety.

Use a checklist like this:

- Imports and structure: no unnecessary coupling, no circular dependencies
- Naming and intent: clear and consistent with surrounding code
- Tests: changes are covered where risk is introduced
- Security and privacy: no sensitive data leakage, safe handling of secrets
- Documentation: new behavior is documented, and links are correct

### Severity model

Treat findings as one of:

- Ready to merge (no blockers)
- Changes requested (must fix before merge)
- Blocked (requires discussion, design decision, or external access)

---

## 6) Quality gates

Quality gates prevent avoidable regressions and enforce a consistent baseline.

Run these before every commit and again before merging:

- Linting
- Formatting
- Type checking (if configured)
- Unit/integration tests
- Security/static checks (as applicable)

Never bypass quality gates with a “skip checks” workflow. If a check needs an exception, document the exemption explicitly in the PR notes and track the reason in the issue.

---

## 7) CI/CD principles

The CI/CD pipeline should provide confidence in both correctness and deployability.

### Required pipeline behavior

- **Validation checks run on (or immediately after) PR creation** so reviewers see lint/test results alongside the diff. Examples: lint, format, unit tests, type check, security scan, markdown lint.
- **Not every pipeline step is a validation check.** Building container images, publishing packages, or deploying to staging/production may run later (often after merge). Do not block PR review on deploy-only jobs unless the change requires them.
- Merge triggers a staged deployment path (staging before production)
- Rollback is possible if a deploy fails or a regression is detected
- Smoke tests run after deployment to confirm basic health

### Evidence over assumptions

Do not claim “release is safe” without evidence from checks and smoke tests.

---

## 8) Post-merge cleanup

After merging, keep the repo healthy and reduce operational noise.

### Cleanup tasks

- Prune or delete local branches that are no longer needed
- Clean CI run history as appropriate for the repository’s conventions
- Keep scratch directories tidy (`tmp/`), and ensure no accidental artifacts were committed

---

## 9) Verification

Verification is the discipline of proving that “done” is actually true.

Before stating that work is complete:

- Run the relevant validation checks
- Report what you ran and what the result was
- Prefer exact commands and observable outcomes over vague statements

If something fails, update the issue/PR with the failure evidence and the fix plan.
