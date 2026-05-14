# Superpowers vs pkuppens skills — reconciliation notes

This note compares the **Superpowers** plugin skills with the **repo-owned** skills in `skills/`.
Goal: keep your conventions as the default, but port the best discipline patterns so the workflow stays strong even when Superpowers is not installed.

## High-overlap areas (duplicate intent)

- **TDD discipline** (Superpowers `test-driven-development`)
  - Closest match: `skills/test/test-write/SKILL.md` + `skills/validation/validation-draft/SKILL.md`
  - Delta to port: make **“failing test first”** explicit and non-optional for bug fixes; add a short red-green checklist.

- **Systematic debugging** (Superpowers `systematic-debugging`)
  - Closest match: spread across `skills/test/test-run/SKILL.md`, `skills/quality-gate/SKILL.md`, and issue workflow skills
  - Delta to port: a single, explicit rule: **no fixes before root cause investigation**, plus a lightweight phased approach (investigate → compare → hypothesis → implement).

- **Evidence-first completion** (Superpowers `verification-before-completion`)
  - Closest match: `skills/quality-gate/SKILL.md` + `skills/validation/run-validation/SKILL.md`
  - Delta to port: make “evidence before claims” a first-class concept and require reporting **the command and the outcome** (counts / exit code) before stating “done”.

- **Worktree workflow** (Superpowers `using-git-worktrees`)
  - Closest match: `skills/git-worktrees/SKILL.md`
  - Delta to port (optional): Superpowers provides a “start work in isolated worktree” workflow; your existing skill is mainly “what worktrees are / how to remove them”. Keep these separate.

## Conflicts to avoid when porting (your standards win)

- **Toolchain**: Superpowers examples mention `pip` / `poetry`. Your default is **uv-first** and varies per repo. Port patterns, not commands.\n+- **Integration workflow**: Superpowers “finishing a branch” includes local merge options. Your workspace convention is **PR-first** and “never commit directly to main”.\n+- **Hardcoded plan paths**: Superpowers `writing-plans` hardcodes `docs/superpowers/plans/...`. Your repos vary; prefer repo conventions (often `tmp/` for scratch) or make paths configurable.\n+- **Platform/tool naming**: Superpowers content assumes Claude’s skill tooling. In this repo, skills must be usable in Cursor/Claude/Codex, so avoid tool-specific constraints that do not generalize.\n+

## Resolution implemented in this repo

- Add repo-owned skills:\n+  - `skills/verification-before-completion/SKILL.md`\n+  - `skills/systematic-debugging/SKILL.md`\n+- Tighten existing skills (`test-write`, `test-run`, `quality-gate`, `run-validation`) to encode the ported discipline without depending on Superpowers.\n+
