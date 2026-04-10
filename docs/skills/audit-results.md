# Skills Audit — Inventory and Mapping

**Date:** 2026-04-10  
**Issue:** #27 — Audit and merge skills from all repos into pkuppens/skills/  
**Last inventory refresh:** #57  
**Parent:** #26

*Note: Issue specified `tmp/skills/inventory/audit-results.md`; this file lives in `docs/skills/` for version control. Copy to `tmp/skills/inventory/` locally if needed.*

## Executive summary

Audit of 82+ skill files across workspace locations (historical). Canonical set: `pkuppens/skills/` — **94** `SKILL.md` files as of 2026-04-10 (#59–#65). Regenerate the list with the commands below; overlaps and mapping for *other repos* remain valid at a high level. `babblr` has no skills. `~/.claude/skills` not audited (likely symlinked to pkuppens or user-specific).

---

## 1. Inventory by location

### 1.1 pkuppens/skills/ (canonical) — **94** `SKILL.md` files

The static table below is **not** duplicated here (it went stale quickly). Use one of:

```bash
# Unix / Git Bash (repo root)
find skills -name 'SKILL.md' | sort | wc -l   # count
find skills -name 'SKILL.md' | sort            # paths
```

```powershell
# PowerShell (repo root)
(Get-ChildItem -Path skills -Recurse -Filter SKILL.md).Count
Get-ChildItem -Path skills -Recurse -Filter SKILL.md | Sort-Object FullName | ForEach-Object { $_.FullName.Substring((Get-Location).Path.Length + 1) }
```

**Expected count:** must match the figure in [SKILL_TREE.md](../../skills/SKILL_TREE.md) (*Inventory* line under Implementation Status). If they differ, refresh this doc (#57) or fix the tree.

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
| arch-scan | architecture-document-existing | ✅ Merged (#28) |
| arch-adr | architecture-decisions | ✅ Merged (#28) |
| arch-component | architecture-building-blocks | ✅ Merged (#28) |
| arch-abstraction | architecture-building-blocks | ✅ Merged (#28) |
| arch-runtime-flow | architecture-runtime (new) | ✅ Merged (#28) |
| arch-user-flow | design-consult | ✅ Merged (#28) |
| arch-refactor | architecture-decisions (AMI) | ✅ Cross-ref (#28) |
| arch-rules | architecture-crosscutting (new) | ✅ Merged (#28) |
| arch-migrate | architecture-decisions | ✅ Merged (#28) |
| arch-definition | architecture-glossary (new) | ✅ Merged (#28) |

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

Post–#28 / current canonical counts (2026-04-10):

- **pkuppens/skills**: **94** `SKILL.md` files (see §1.1 commands).
- **Sub-skills:** full tree status is maintained in [SKILL_TREE.md](../../skills/SKILL_TREE.md) → **Implementation Status** (not duplicated here).
