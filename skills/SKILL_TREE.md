# Skill Tree — Complete Software Engineering Process

Personal skills for AI-assisted coding, aligned with arc42 and the full software lifecycle.

**Principles:** Single responsibility per skill; clear name + one-liner (+ optional 1–2 comment lines); recursive sub-skills up to 4–5 levels.

**Creating skills:** Use the [skill-creation](_meta/skill-creation/SKILL.md) meta-skill when adding or extending skills from this tree.

---

## Process Variations (Optional)

| Variation | When to use | Notable skill adaptations |
|-----------|-------------|---------------------------|
| **Waterfall** | Fixed scope, formal phases, sign-off gates | Sequential: requirements → architecture → design → implementation → validation. Fewer parallel branches. |
| **Agile** | Iterative, incremental, changing scope | Short cycles; issue-workflow per sprint; backlog grooming; retrospectives. |
| **TDD** | Test-first, red-green-refactor | validation-draft and test-write before implementation-construction; validation-detail after. |

---

## Meta-skills

### skill-creation
Guides creation and maintenance of skills in this tree. Use when authoring a new `SKILL.md`, extending an existing skill, or reviewing skill structure and conventions.
// Lives in `_meta/skill-creation/`; operates on the skill system itself, not on the software lifecycle.

---

## Level 0: Process Orchestrator

### 0. software-engineering-process
Orchestrates the full lifecycle from ideation to production monitoring, auditing, and maintenance; invokes phase skills as needed.
// Entry: bug report, feature idea, maintenance need, audit finding.
// Variations: waterfall (sequential), agile (iterative), TDD (test-first).

---

## Level 1: Ideation

### 1. ideation
Generates and evaluates ideas; checks similar work for re-use; identifies show-stoppers.

#### 1.1 brainstorm
Generates new ideas (feature, improvement, refactor) from problem statements or opportunities.

#### 1.2 ideation-swot
Evaluates idea via SWOT (strengths, weaknesses, opportunities, threats); surfaces risks and show-stoppers.

#### 1.3 ideation-reuse-check
Searches similar existing work, libraries, patterns for re-use before designing from scratch.

---

## Level 1: Requirements Engineering

### 2. requirements
Captures, refines, and validates requirements; aligns with goals and constraints.

#### 2.1 requirements-capture
Captures functional and non-functional requirements from stakeholders or issue context.

#### 2.2 requirements-goals
Extracts and documents top 3–5 quality goals and success criteria (arc42 §1).
// Aligns with introduction & goals.

#### 2.3 requirements-constraints
Documents regulations, external constraints, and technical limits (arc42 §2).
// Aligns with constraints.

#### 2.4 requirements-context-scope
Defines system boundary, external systems, interfaces (arc42 §3).
// Context diagram, scope in/out.

#### 2.5 requirements-prioritise
Prioritises requirements (MoSCoW, value vs effort); defines MVP.

#### 2.6 requirements-validate
Validates requirements for clarity, testability, consistency.

---

## Level 1: Architecture (arc42-aligned)

**arc42 conventions** (from [Beyond Autocomplete](https://www.beyondautocomplete.nl/how-i-use-claude-code-to-keep-my-architecture-decisions-on-track/)): One markdown file per section in `docs/architecture/` (01–12); `adr/` subdir for ADRs. Fill Section 1 (Introduction and Goals) first — it gives AI project context. Record ADRs as you go; use them to populate §4 (Solution Strategy) and other sections.

### 3. architecture
Documents and maintains system and software architecture per arc42; consults existing design.

#### 3.1 architecture-consult
Consults current architecture docs, ADRs, and codebase to identify components/modules/files.
// Use before adding features or scoping changes.

#### 3.2 architecture-solution-strategy
Documents core ideas, fundamental decisions, and solution approaches (arc42 §4).
// Strategy before structure. Can summarize from existing ADRs.

#### 3.3 architecture-building-blocks
Documents static decomposition: hierarchy, black-box/white-box of building blocks (arc42 §5).
// Modules, components, packages, files.

#### 3.4 architecture-runtime
Documents runtime behaviour: scenarios, sequences, error handling (arc42 §6).
// Runtime view; sequence/activity diagrams.

#### 3.5 architecture-deployment
Documents deployment: infrastructure, hardware, containers, mapping of software to infra (arc42 §7).
// Deployment view; topology.

#### 3.6 architecture-crosscutting
Documents crosscutting concepts: recurring patterns, domain model, shared rules (arc42 §8).
// Logging, security, error handling patterns.

#### 3.7 architecture-decisions
Authors or updates Architecture Decision Records (arc42 §9).
// Store in docs/architecture/adr/ as 001-title.md; update TOC in 09-decisions.md. Format: context, options considered, decision, consequences.

#### 3.8 architecture-quality
Documents quality tree and quality scenarios; maps to requirements (arc42 §10).
// Performance, security, maintainability scenarios.

#### 3.9 architecture-risks-debt
Documents risks, technical debt, mitigation (arc42 §11).
// Risk register; debt backlog.

#### 3.10 architecture-glossary
Maintains glossary of business and technical terms (arc42 §12).
// Shared vocabulary; avoid ambiguity.

---

## Level 1: Design (Detailed)

### 4. design
Defines detailed design: components, interfaces, data flows; single responsibility.

#### 4.1 design-consult
Consults current design and architecture to place new code correctly.

#### 4.2 design-component-boundaries
Defines component/module/file boundaries; single responsibility; C4/DDD.

#### 4.3 design-interfaces
Defines APIs, contracts, data schemas between components.

#### 4.4 design-data-model
Defines data structures, entities, relationships.
// May nest: design-data-entities, design-data-schema.

---

## Level 1: Issue Workflow (Orchestrator for Implementation)

### 5. issue-workflow
Orchestrates issue lifecycle from idea to closed; triggers sub-skills as needed.

#### 5.1 issue-check-duplicates
Checks related open and recently closed issues to prevent duplication.

#### 5.2 issue-purpose-alignment
Ensures focused purpose aligned with project goals and quality attributes.

#### 5.3 issue-work-down
Identifies work-down from other issues, code, and tests; scopes the issue.

#### 5.4 issue-acceptance-criteria
Defines acceptance criteria as minimum baseline of done.
// Optional: 5.4.1 issue-acceptance-testable, 5.4.2 issue-acceptance-verifiable.

#### 5.5 issue-out-of-scope
Defines out-of-scope to prevent gold-plating.

#### 5.6 issue-estimate
Adds T-shirt size (or equivalent) estimate.

#### 5.7 issue-metadata
Adds tags, milestones, assignees, planning references.

---

## Level 1: Planning

### 6. plan
Breaks work into tasks, estimates, dependencies, branch strategy.

#### 6.1 plan-tasks
Decomposes issue into ordered tasks or subtasks.

#### 6.2 plan-dependencies
Identifies task dependencies and critical path.

#### 6.3 plan-branch-strategy
Selects branch naming and base (feature/task/bug/hotfix); creates the branch before edits.
// Use at planning time or when the feature-branch hook fires (HOOK:FEATURE_BRANCH_REQUIRED).

---

## Level 1: Implementation

### 7. implementation
Code construction following Code Complete 2; naming, layout, style, single responsibility.

#### 7.1 implementation-construction
Writes new code with consistent naming, formatting, docstrings.

#### 7.2 implementation-refactor
Refactors existing code without changing behaviour.

#### 7.3 implementation-delete
Removes unused code; maintains consistency.
// Maintenance entry point.

---

## Level 1: Validation & Testing

### 8. validation
Drafts and executes validation steps; ensures acceptance criteria are met.

#### 8.1 validation-draft
Drafts validation steps, scenarios, or test cases from acceptance criteria (BDD/TDD).
// Can run before implementation in TDD.

#### 8.1b create-validation
Creates full implementation validation documents: markdown checklists with exact commands, URLs, and expected outcomes; issue-scratch or committed paths. Complements validation-draft.

#### 8.2 validation-detail
Refines validation with implementation-specific details when code shape is known.

#### 8.3 validation-run
Executes validation checklist; records evidence. Implemented: [run-validation](validation/run-validation/SKILL.md).

#### 8.4 skill-benchmark
Evaluates skill effectiveness by comparing agent output on a task with and without the skill; produces a scored comparison table.
// Use to validate new or revised skills; create benchmark evidence for PRs.

---

### 9. test
Writes and runs tests; increases coverage.

#### 9.1 test-write
Adds or updates unit/integration/e2e tests.

#### 9.2 test-run
Runs test suite; reports results and coverage.

#### 9.3 test-coverage
Analyses and increases test coverage; identifies gaps.
// Maintenance entry point.

---

## Level 1: Quality Gate

### 10. quality-gate
Runs lint, format, type check, security scan; enforces pre-commit.

#### 10.1 quality-gate-lint
Runs linter (e.g. ruff, eslint); reports and fixes issues.

#### 10.2 quality-gate-format
Applies formatter (e.g. ruff format, prettier).

#### 10.3 quality-gate-type
Runs type checker (e.g. pyright, tsc).

#### 10.4 quality-gate-security
Runs security scan (e.g. bandit, npm audit).

#### 10.5 openclaw-security
Enforces OpenClaw security constraints; mandates `openclaw security audit --deep` and `--fix` before every code-change PR. Use for OpenClaw projects only.

---

## Level 1: Integration & Deployment

### 11. integration
Creates PR, merge, deployment checks.

#### 11.1 integration-commit
Commits with conventional message; references issue.

#### 11.2 integration-pr
Opens PR; links to issue; fills description.

#### 11.3 integration-merge
Merges PR; resolves conflicts; squashes if needed.

---

### 12. deployment
Deploys to target environment; runs deployment checks.

#### 12.1 deployment-build
Builds artefacts (images, bundles); runs build pipeline.

#### 12.2 deployment-release
Releases to staging/production; rollback if needed.

---

## Level 1: Operations (Production)

### 13. operations
Monitors production; handles incidents; audits.

#### 13.1 operations-monitoring
Monitors logs, metrics, alerts; detects anomalies.
// Observability; health checks.

#### 13.2 operations-incident
Responds to incidents; triages, mitigates, communicates.

#### 13.3 operations-audit
Performs audit: compliance, security, performance, data.
// Regulatory, internal, or external audit.

---

## Level 1: Maintenance & Bug Reporting

### 14. maintenance
Bug reporting, refactoring, tech debt reduction; post-merge hygiene.

#### 14.1 maintenance-bug-report
Captures bug report: reproduction, expected vs actual, environment.
// Creates or enriches issue from incident/feedback.

#### 14.2 maintenance-cleanup
Branch cleanup, GitHub Actions runs, tmp/ hygiene after merge.

#### 14.3 maintenance-debt
Addresses technical debt; links to architecture-risks-debt.

---

## Level 1: Governance & Improvement

### 15. governance
Progress tracking, post-mortem, workflow improvement.

#### 15.1 governance-progress
Updates workflow state, milestone comments, handoff notes (e.g. tmp/github/).

#### 15.2 governance-post-mortem
Reflects on errors, lessons, self-improvement; refines skills and workflow.
// Retro; blameless post-mortem for incidents.

#### 15.3 governance-audit-trail
Maintains audit trail: decisions, changes, evidence.
// Links to operations-audit; compliance.

---

## Language & Framework Skills

### find-skills
Helps users discover and install agent skills when they ask "how do I do X", "find a skill for X", or express interest in extending capabilities.

### mojo-syntax
Mojo syntax and conventions. Use when writing Mojo code, translating to Mojo, or generating Mojo. Combines with mojo-gpu-fundamentals and mojo-python-interop as needed.

### mojo-gpu-fundamentals
GPU programming basics in Mojo. Use with mojo-syntax when targeting NVIDIA, AMD, or Apple silicon GPUs.

### mojo-python-interop
Mojo–Python interoperability: calling Python from Mojo, exposing Mojo to Python, type conversion. Use with mojo-syntax when integrating with Python libraries.

### new-modular-project
Creates new Mojo or MAX projects; initializes Pixi or UV for Mojo/MAX.

### git-worktrees
Explains git worktrees and Claude Code usage; guides removal and cleanup when a branch cannot be deleted because of an active worktree. Use when "cannot delete branch used by worktree", cleaning up .claude/worktrees/, or when asked about worktrees.

---

## Summary: Skill Tree Overview

| # | Skill | arc42 / Lifecycle | Sub-skills |
|---|-------|-------------------|------------|
| — | skill-creation *(meta)* | Skill authoring | — |
| 0 | software-engineering-process | Orchestrator | — |
| 1 | ideation | Ideation | 1.1–1.3 |
| 2 | requirements | Requirements (arc42 §1–3) | 2.1–2.6 |
| 3 | architecture | arc42 §4–12 | 3.1–3.10 |
| 4 | design | Detailed design | 4.1–4.4 |
| 5 | issue-workflow | Issue lifecycle | 5.1–5.7 |
| 6 | plan | Planning | 6.1–6.3 |
| 7 | implementation | Construction | 7.1–7.3 |
| 8 | validation | Validation | 8.1–8.4, 8.1b |
| 9 | test | Testing | 9.1–9.3 |
| 10 | quality-gate | Quality | 10.1–10.5 |
| 11 | integration | Integration | 11.1–11.3 |
| 12 | deployment | Deployment | 12.1, 12.2 |
| 13 | operations | Production, monitoring, audit | 13.1–13.3 |
| 14 | maintenance | Bug report, cleanup, debt | 14.1–14.3 |
| 15 | governance | Progress, post-mortem, audit trail | 15.1–15.3 |

**Total:** 1 meta-skill + 16 lifecycle skills, 60+ sub-skills. Nesting: up to 4–5 levels where needed (e.g. 5.4.1, 5.4.2).

## Implementation Status

*Post-audit #27: 37 SKILL.md files in pkuppens/skills. See [audit-results.md](../docs/skills/audit-results.md) for full inventory and mapping.*

| Skill | Status |
| skill-creation | ✅ implemented |
| issue-workflow (5.x) | ✅ implemented |
| architecture (3.x) | ✅ implemented (#28: sir-read-a-lot arch skills merged) |
| design (4.1) | ✅ implemented |
| implementation (7.1) | ✅ implemented |
| validation (8.1) | ✅ implemented |
| create-validation (8.1b), run-validation (8.3) | ✅ implemented |
| api-design, branch-cleanup-after-pr, code-quality-design/docs/testing | ✅ implemented |
| quality-gate (10.x) | ✅ implemented |
| openclaw-security (10.5) | ✅ implemented |
| integration (11.x) | ✅ implemented |
| deployment (12.1, 12.2) | ✅ implemented |
| operations (13.1–13.3) | ✅ implemented |
| skill-benchmark (8.4) | ✅ implemented |
| find-skills, mojo-syntax, mojo-gpu-fundamentals, mojo-python-interop, new-modular-project, git-worktrees | ✅ implemented |
| maintenance-cleanup (14.2) | ✅ implemented |
| plan (orchestrator: branch strategy, implementation-workflow through PR/CI) | ✅ implemented |
| plan-branch-strategy (6.3) | ✅ implemented |
| ideation, requirements, design (4.2–4.4), plan 6.1–6.2, test, validation (8.2–8.3), maintenance (14.1, 14.3), governance | 🔲 stubs / not yet implemented |
