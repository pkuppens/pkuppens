# Unified AI Coding Skills

Shared skills for Cursor, Claude, and Codex. Committed to this repo; referenced from each IDE's expected location.

## Usage

Skills are markdown files (`SKILL.md`) in skill-specific directories. Each skill has a `name` and `description` in YAML frontmatter; IDEs discover skills automatically when the directory is linked.

Full skill tree: [SKILL_TREE.md](SKILL_TREE.md). How skills compose: [COOPERATION.md](COOPERATION.md). Optional **V-model** traceability overlay: [v-model/SKILL.md](v-model/SKILL.md).

**Format and CI:** Metadata must follow the [Agent Skills specification](https://agentskills.io/specification). Pull requests that touch `skills/` run automated validation (`skills-ref`, pinned in GitHub Actions). Tooling choices and Skilz vs spec are documented in [ADR 001 — Skill validation and tooling](../docs/skills/decisions/001-skill-validation-and-tooling.md).

## IDE Setup

Reference this `skills/` folder from your IDE. Do not duplicate skills. Symlinks below work for **Cursor**, **Claude**, and **Codex**.

### Option A: Symlinks (recommended)

**From a project that uses pkuppens as parent:**
```bash
# Project-level (e.g. on_prem_rag, babblr) — create parent dir if missing
mkdir -p .cursor
ln -s ../../pkuppens/skills .cursor/skills
# or
mkdir -p .claude
ln -s ../../pkuppens/skills .claude/skills
```

**User-level (all projects):**
```bash
# Clone pkuppens somewhere; create parent dirs if missing
mkdir -p ~/.cursor ~/.claude ~/.codex
ln -s /path/to/pkuppens/skills ~/.cursor/skills
ln -s /path/to/pkuppens/skills ~/.claude/skills
ln -s /path/to/pkuppens/skills ~/.codex/skills
```

**Windows:** Symlinks may require Administrator. Use Developer Mode or run terminal as Admin. Alternative: `mklink /D .cursor\skills skills` (cmd as Admin).

### Option B: Sync script

Create `scripts/sync-skills-to-ide.sh` to copy or symlink `skills/` into `~/.cursor/skills/pkuppens`, `~/.claude/skills/pkuppens`, etc. Run after clone.

### IDE expected locations

| IDE | Project | User |
|-----|---------|------|
| Cursor | `.cursor/skills/`, `.agents/skills/` | `~/.cursor/skills/` |
| Claude | `.claude/skills/` | `~/.claude/skills/` |
| Codex | — | `~/.codex/skills/` |

Cursor also loads from `.claude/skills/` and `~/.claude/skills/`.

## Directory structure

```
skills/
├── README.md           # This file
├── CLAUDE.md           # Agent instructions
├── SKILL_TREE.md
├── _meta/              # Meta-skills
│   ├── skill-creation/
│   │   └── SKILL.md
│   └── human-ai-execution.md
├── api-design/
├── branch-cleanup-after-pr/
├── code-quality-design/
├── code-quality-docs/
├── code-quality-testing/
├── code-review/        # PR review checklist (imports, headers, compliance wording)
├── ideation/
├── requirements/
├── architecture/
├── design/
├── issue-workflow/
├── plan/
├── implementation/
├── validation/         # validation-draft, create-validation, run-validation, skill-benchmark
├── test/
├── quality-gate/
├── integration/
├── deployment/
├── operations/
├── maintenance/
├── governance/
└── v-model/            # V-model overlay (orchestrator + 6 sub-skills)
```
