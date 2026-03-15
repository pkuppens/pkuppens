# Skills Audit — Inventory and Mapping

**Date:** 2025-03-15  
**Issue:** #27 — Audit and merge skills from all repos into pkuppens/skills/  
**Parent:** #26

*Note: Issue specified `tmp/skills/inventory/audit-results.md`; this file lives in `docs/skills/` for version control. Copy to `tmp/skills/inventory/` locally if needed.*

## Executive summary

Audit of 82+ skill files across workspace locations. Canonical set: `pkuppens/skills/` (37 SKILL.md files). Overlaps identified; mapping table below. `babblr` has no skills. `~/.claude/skills` not audited (likely symlinked to pkuppens or user-specific).

---

## 1. Inventory by location

### 1.1 pkuppens/skills/ (canonical) — 37 files

| Path | Canonical equivalent |
|------|----------------------|
| architecture/SKILL.md | architecture (orchestrator) |
| architecture/architecture-building-blocks/SKILL.md | 3.3 architecture-building-blocks |
| architecture/architecture-consult/SKILL.md | 3.1 architecture-consult |
| architecture/architecture-decisions/SKILL.md | 3.7 architecture-decisions |
| architecture/architecture-document-existing/SKILL.md | 3.2 (retrofitting) |
| architecture/architecture-risks-debt/SKILL.md | 3.9 architecture-risks-debt |
| architecture/architecture-solution-strategy/SKILL.md | 3.2 architecture-solution-strategy |
| deployment/SKILL.md | 12 deployment (orchestrator) |
| deployment/deployment-build/SKILL.md | 12.1 deployment-build |
| deployment/deployment-release/SKILL.md | 12.2 deployment-release |
| design/design-consult/SKILL.md | 4.1 design-consult |
| find-skills/SKILL.md | find-skills |
| implementation/implementation-construction/SKILL.md | 7.1 implementation-construction |
| integration/SKILL.md | 11 integration (orchestrator) |
| integration/integration-commit/SKILL.md | 11.1 integration-commit |
| integration/integration-merge/SKILL.md | 11.3 integration-merge |
| integration/integration-pr/SKILL.md | 11.2 integration-pr |
| issue-workflow/SKILL.md | 5 issue-workflow (orchestrator) |
| issue-workflow/issue-acceptance-criteria/SKILL.md | 5.4 issue-acceptance-criteria |
| issue-workflow/issue-check-duplicates/SKILL.md | 5.1 issue-check-duplicates |
| issue-workflow/issue-estimate/SKILL.md | 5.6 issue-estimate |
| issue-workflow/issue-metadata/SKILL.md | 5.7 issue-metadata |
| issue-workflow/issue-out-of-scope/SKILL.md | 5.5 issue-out-of-scope |
| issue-workflow/issue-purpose-alignment/SKILL.md | 5.2 issue-purpose-alignment |
| issue-workflow/issue-work-down/SKILL.md | 5.3 issue-work-down |
| mojo-gpu-fundamentals/SKILL.md | mojo-gpu-fundamentals |
| mojo-python-interop/SKILL.md | mojo-python-interop |
| mojo-syntax/SKILL.md | mojo-syntax |
| new-modular-project/SKILL.md | new-modular-project |
| openclaw-security/SKILL.md | 10.5 openclaw-security |
| operations/SKILL.md | 13 operations (orchestrator) |
| operations/operations-audit/SKILL.md | 13.3 operations-audit |
| operations/operations-incident/SKILL.md | 13.2 operations-incident |
| operations/operations-monitoring/SKILL.md | 13.1 operations-monitoring |
| quality-gate/SKILL.md | 10 quality-gate |
| validation/skill-benchmark/SKILL.md | 8.4 skill-benchmark |
| validation/validation-draft/SKILL.md | 8.1 validation-draft |
| _meta/skill-creation/SKILL.md | skill-creation (meta) |

### 1.2 on_prem_rag/.claude/skills/ — 12 files

| Skill dir | Canonical equivalent | Action |
|-----------|----------------------|--------|
| api-design | design/design-consult | Overlap — merge if api-design has unique content |
| branch-cleanup | maintenance/maintenance-cleanup (14.2) | Project-specific; keep in place |
| commit | integration/integration-commit | **Duplicate** — delegate to canonical |
| create-validation | validation/validation-draft | **Duplicate** — merge/dedup |
| get-started | — | Project-specific; keep in place |
| pr | integration/integration-pr | **Duplicate** — delegate to canonical |
| run-validation | validation (8.3 validation-run) | **Duplicate** — merge/dedup |
| skills | — | Meta; keep or symlink to skill-creation |
| test | test (9.x) | Overlap — pkuppens has no test-write yet |
| update-commits | — | Project-specific; keep in place |
| update-date-tags | — | Project-specific; keep in place |

### 1.3 on_prem_rag/.cursor/skills/ — 7 files

| Skill dir | Canonical equivalent | Action |
|-----------|----------------------|--------|
| api-design | design/design-consult | Same as .claude |
| branch-cleanup-after-pr | maintenance/maintenance-cleanup | Project-specific; keep |
| code-quality-design | design/quality-gate overlap | Project-specific; keep |
| code-quality-docs | quality-gate (docs) | Project-specific; keep |
| code-quality-testing | quality-gate + test | Project-specific; keep |
| create-validation | validation/validation-draft | Same as .claude |
| run-validation | validation | Same as .claude |

### 1.4 sir-read-a-lot/.claude/skills/ — 9 files (skill.md)

| Skill dir | Canonical equivalent | Action |
|-----------|----------------------|--------|
| arch-scan | architecture-document-existing | Merge (#28) |
| arch-adr | architecture-decisions | Merge (#28) |
| arch-component | architecture-building-blocks | Merge (#28) |
| arch-abstraction | architecture-building-blocks | Merge (#28) |
| arch-runtime-flow | architecture (3.4 runtime) | Merge (#28) |
| arch-user-flow | design-consult | Merge (#28) |
| arch-refactor | implementation-refactor | Cross-ref (#28) |
| arch-rules | architecture-crosscutting | Merge (#28) |
| arch-migrate | architecture-decisions | Merge (#28) |
| arch-definition | architecture-glossary | Merge (#28) |

### 1.5 babblr

No `.claude/skills/` or `.cursor/skills/` found. No SKILL.md files.

### 1.6 ~/.claude/skills

Not audited (user-level; may be symlinked to pkuppens or contain user-specific skills).

---

## 2. Overlaps and duplicates

| Canonical (pkuppens) | Other locations | Resolution |
|----------------------|-----------------|------------|
| integration-commit | on_prem_rag: commit | Symlink on_prem_rag → pkuppens or merge commit → integration-commit |
| integration-pr | on_prem_rag: pr | Same |
| validation-draft | on_prem_rag: create-validation | Merge create-validation content into validation-draft |
| validation-run (8.3) | on_prem_rag: run-validation | Merge or cross-ref |
| design-consult | on_prem_rag: api-design | Merge api-design unique content into design-consult |
| architecture-* | sir-read-a-lot: arch-* | Merge in #28 |

---

## 3. Skills unique to project repos (do not generalise)

| Location | Skill | Rationale |
|----------|-------|-----------|
| on_prem_rag | get-started | Project onboarding |
| on_prem_rag | update-commits | Project-specific commit workflow |
| on_prem_rag | update-date-tags | Project-specific |
| on_prem_rag | branch-cleanup, branch-cleanup-after-pr | Project-specific (references on_prem_rag workflow) |
| on_prem_rag | code-quality-design, code-quality-docs, code-quality-testing | Project-specific quality checks |

---

## 4. Recommendations

1. **on_prem_rag**: Replace `commit`, `pr`, `create-validation`, `run-validation` with symlinks to `pkuppens/skills/` (or merge content and delete). Track in separate on_prem_rag issue.
2. **sir-read-a-lot**: Merge arch skills into pkuppens per #28. Do not change sir-read-a-lot files (out of scope for #27).
3. **pkuppens SKILL_TREE**: Update implementation status to reflect audit (see below).
4. **Symlink setup**: Document in `skills/README.md` that project repos should symlink to canonical. Already present.

---

## 5. SKILL_TREE inventory update

Post-audit counts:

- **pkuppens/skills**: 37 SKILL.md files
- **Sub-skills implemented**: architecture (6), deployment (2), integration (3), issue-workflow (7), operations (3)
- **Missing from SKILL_TREE**: architecture-runtime (3.4), architecture-deployment (3.5), architecture-crosscutting (3.6), architecture-quality (3.8), architecture-glossary (3.10) — some exist only as sir-read-a-lot arch-* until #28 merge
