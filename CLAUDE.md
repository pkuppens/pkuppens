# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

The `pkuppens/pkuppens` GitHub profile repository. It serves two purposes:

1. **GitHub profile README** (`README.md`) — displayed at `github.com/pkuppens`.
2. **Unified AI coding skills library** (`skills/`) — shared `SKILL.md` files for Cursor, Claude, and Codex.

There is no build system or test suite. All content is Markdown. Skills under `skills/` are checked in CI: [`validate-skills.yml`](.github/workflows/validate-skills.yml); see [ADR 001](docs/skills/decisions/001-skill-validation-and-tooling.md).

## Repository Layout

```
pkuppens/
├── README.md                    # GitHub profile page (public-facing)
├── skills/                      # AI coding skills library
│   ├── SKILL_TREE.md            # Canonical index of all 16 top-level skills + 60+ sub-skills
│   ├── CLAUDE.md                # Agent instructions scoped to skills/
│   ├── _meta/skill-creation/    # Meta-skill: how to author new skills
│   │   └── SKILL.md
│   └── <skill-name>/            # One directory per skill (mostly not yet created)
│       └── SKILL.md
├── docs/
│   ├── screenshots/             # Assets referenced from README.md
│   └── skills/
│       └── decisions/           # ADRs for the skills library (e.g. validation tooling)
└── tmp/                         # Gitignored scratch (drafts, planning)
```

## Skills Architecture

Skills are Markdown files (`SKILL.md`) with YAML frontmatter. They are loaded by IDEs (Cursor, Claude, Codex) from linked or copied locations.

### SKILL.md format

```yaml
---
name: skill-name           # max 64 chars, lowercase letters/numbers/hyphens
description: Does X. Use when [trigger scenarios]. Third person, WHAT + WHEN.
---
```

Body under 300 lines. Use `reference.md` and `examples.md` for overflow — create additional small skills rather than exceeding 500 lines.

### Skill tree

`SKILL_TREE.md` is the canonical index. Sixteen top-level skills cover the full software lifecycle:

| Range | Domain |
|-------|--------|
| 0 | Orchestrator |
| 1–4 | Ideation, Requirements, Architecture (arc42-aligned), Design |
| 5–6 | Issue workflow, Planning |
| 7–10 | Implementation, Validation, Test, Quality gate |
| 11–13 | Integration, Deployment, Operations |
| 14–15 | Maintenance, Governance |

Architecture skills (3.x) align with **arc42 sections 1–12**. ADRs live in `docs/architecture/adr/` within the _project_ repos — not here.

### Adding a new skill

1. Read `skills/_meta/skill-creation/SKILL.md` first.
2. Create `skills/<skill-name>/SKILL.md` following the template.
3. Add an entry to `SKILL_TREE.md` in the correct section.
4. Keep `skills/CLAUDE.md` up to date if structural conventions change.

### IDE linking

Skills in this repo are intended to be symlinked from project or user-level IDE directories:

| IDE | Project-level | User-level |
|-----|--------------|------------|
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Claude | `.claude/skills/` | `~/.claude/skills/` |
| Codex | — | `~/.codex/skills/` |

See `skills/README.md` for symlink commands. Do not duplicate skill files — always symlink back to this repo.

## Scratch Directory

`tmp/` is gitignored. Use it for drafts, planning notes, and research. Never `git add` from there.

## Git Workflow

Branch naming: `feature/NNN-short-description` (issue number prefix). Alternatives: `hotfix/NNN-…`, `chore/…`, `epic/NNN-…` per repo convention.
Commit messages: `#NNN: type: description` (types: `feat`, `fix`, `docs`, `refactor`, `chore`).
All changes via PRs — never commit directly to `main`.

## Plan Mode Checklist

Before writing a plan, work through these steps. Skill links are optional reading for detail.

| # | Step | Skill |
|---|------|-------|
| 1 | Check for duplicate or already-completed work (issues, PRs, git log) | [issue-check-duplicates](skills/issue-workflow/issue-check-duplicates/SKILL.md) |
| 2 | Verify purpose alignment with project goals | [issue-purpose-alignment](skills/issue-workflow/issue-purpose-alignment/SKILL.md) |
| 3 | Identify work already done in code/tests | [issue-work-down](skills/issue-workflow/issue-work-down/SKILL.md) |
| 4 | Define acceptance criteria before scoping | [issue-acceptance-criteria](skills/issue-workflow/issue-acceptance-criteria/SKILL.md) |
| 5 | Select and create feature branch (before any edits) | [plan-branch-strategy](skills/plan-branch-strategy/SKILL.md) |

**Extending:** Add a row. Link to an existing skill or create one under `skills/` first.
