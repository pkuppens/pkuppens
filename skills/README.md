# Unified AI Coding Skills

Shared skills for Cursor, Claude, and Codex. Committed to this repo; referenced from each IDE's expected location.

## Usage

Skills are markdown files (`SKILL.md`) in skill-specific directories. Each skill has a `name` and `description` in YAML frontmatter; IDEs discover skills automatically when the directory is linked.

Full skill tree: [REFACTORED_SKILLS.md](REFACTORED_SKILLS.md)

## IDE Setup

Reference this `skills/` folder from your IDE. Do not duplicate skills.

### Option A: Symlinks (recommended)

**From a project that uses pkuppens as parent:**
```bash
# Project-level (e.g. on_prem_rag, babblr)
ln -s ../../pkuppens/skills .cursor/skills
# or
ln -s ../../pkuppens/skills .claude/skills
```

**User-level (all projects):**
```bash
# Clone pkuppens somewhere, then:
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
├── REFACTORED_SKILLS.md
├── _meta/              # Meta-skills
│   └── skill-creation/
│       └── SKILL.md
├── ideation/
├── requirements/
├── architecture/
├── design/
├── issue-workflow/
├── plan/
├── implementation/
├── validation/
├── test/
├── quality-gate/
├── integration/
├── deployment/
├── operations/
├── maintenance/
└── governance/
```
