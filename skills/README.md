# Unified AI Coding Skills

Shared skills for Cursor, Claude, and Codex. Committed to this repo; referenced from each IDE's expected location.

## Usage

Skills are markdown files (`SKILL.md`) in skill-specific directories. Each skill has a `name` and `description` in YAML frontmatter; IDEs discover skills automatically when the directory is linked.

Full skill tree: [SKILL_TREE.md](SKILL_TREE.md). How skills compose: [COOPERATION.md](COOPERATION.md). Optional **V-model** traceability overlay: [v-model/SKILL.md](v-model/SKILL.md).

**Format and CI:** Metadata must follow the [Agent Skills specification](https://agentskills.io/specification). Pull requests that touch `skills/` run `skills-ref` (pinned) and a non-interactive [Skills CLI](https://github.com/vercel-labs/skills) discovery smoke (`npx skills add … --list`). Tooling choices are documented in [ADR 001 — Skill validation and tooling](../docs/skills/decisions/001-skill-validation-and-tooling.md).

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

## Install this library with the Skills CLI (`npx skills`)

**Goal:** Install skills from **this** repository the same way as packages from [skills.sh](https://www.skills.sh/) and the [Skills CLI](https://github.com/vercel-labs/skills)—no extra file server; the CLI clones from Git and discovers `SKILL.md` under [`skills/`](https://github.com/vercel-labs/skills#readme) (this repo matches that layout).

**Who it is for:** Anyone who prefers the ecosystem installer over manual symlinks ([Option A](#option-a-symlinks-recommended)), or who wants a **subset** of skills (`--skill`) without linking the whole tree.

**Layout contract:** Each skill is `skills/<directory>/SKILL.md`; YAML `name` must match `<directory>` (same rule as [Agent Skills](https://agentskills.io/specification) and `skills-ref` in CI).

**Commands** (pin `skills@…` to match CI in [.github/workflows/validate-skills.yml](.github/workflows/validate-skills.yml); examples use `1.5.6`):

```bash
# List skills the CLI would install from this repo (non-interactive)
npx --yes skills@1.5.6 add https://github.com/pkuppens/pkuppens --list -y

# Install one skill by YAML name (project scope; add -g for user-wide)
npx --yes skills@1.5.6 add pkuppens/pkuppens --skill plan -y

# Target specific agents (non-interactive; repeat -a as needed)
npx --yes skills@1.5.6 add pkuppens/pkuppens --skill plan -y -a cursor -a claude-code

# Install many by name
npx --yes skills@1.5.6 add pkuppens/pkuppens --skill plan --skill test -y
```

Use `npx skills add --help` for the latest flags. Installs are **symlinks** by default; use `--copy` when symlinks are not supported.

**Verify an install:**

1. `npx skills list` (or `npx skills ls`) shows the new skill for the scope you chose (`-g` vs project).
2. Confirm files under the path your agent uses (see [IDE expected locations](#ide-expected-locations); e.g. Cursor loads `.cursor/skills/` and `~/.cursor/skills/`).
3. Run `skills-ref validate <path-to-skill-dir>` if you want the same check as CI (install [`skills-ref`](https://www.npmjs.com/package/skills-ref) globally or via `npx`).

## External and vendor skills

Symlinks above point at **this** `skills/` tree (the shared lifecycle library). Many teams also install **additional** skills from GitHub or registries with the Skills CLI (`npx skills add …`). Those installs land under the IDE’s skill paths but are **not** committed here.

**Why document them:** onboarding, reproducibility, and agent behaviour all improve when the project states which extra skills are expected (and any follow-up setup, for example extra CLIs or logins).

**Where to record (pick one or combine):**

- `CLAUDE.md` or `AGENTS.md` at the repo root — short bullet list with package URL and skill name
- `CONTRIBUTING.md` — “Agent / IDE setup” subsection
- `docs/skills-used.md` (or similar) — table of skill source, install command, owner, and last reviewed date

**Example install** (Azure DevOps–oriented; confirm against current CLI output):

```bash
npx skills add https://github.com/github/awesome-copilot --skill azure-devops-cli
```

Authoring guidance for “install first, write in `skills/` only when needed” lives in [`_meta/skill-creation/reference.md`](_meta/skill-creation/reference.md#example-platform-tooling-azure-devops).

## Canonical plus public skills (side by side)

This is the **merge** model: one skill surface for the agent, built from **(A)** this repo’s `skills/` tree (your canonical lifecycle library) and **(B)** extra packages from the open ecosystem (`npx skills add …`). They are not merged in git; they **coexist** under the IDE’s skill discovery paths.

### How it fits together

- The agent loads **all** skill directories the IDE exposes (for example `.cursor/skills/` and `~/.cursor/skills/` for Cursor). Your symlink (or junction) and any CLI-installed folders are **combined** automatically—there is no separate “merge” command.
- **Order of operations** does not matter for discovery: install public skills before or after creating the symlink; refresh the IDE if it caches paths.
- Exact subfolder names depend on the Skills CLI version and flags; after setup, list the skill root once so you know which directories are yours vs vendor.

### Project scale (one repository)

- Symlink **this** `skills/` tree into the **project** path (see [Option A](#option-a-symlinks-recommended) under `.cursor/` or `.claude/`).
- Add **project-scoped** public skills when your CLI supports installing into that project (check `npx skills add --help`). If installs are only practical with `-g`, use global adds and still **document** that this repo expects them ([External and vendor skills](#external-and-vendor-skills)).

### Global scale (your user profile)

- Symlink `pkuppens/skills` under `~/.cursor/skills`, `~/.claude/skills`, and/or `~/.codex/skills` so every clone gets the same baseline without repeating per-repo symlinks.
- Install cross-repo utilities with `npx skills add <package> -g` (see [find-skills](find-skills/SKILL.md)).

### Project and global at the same time

Both are usually **active together**: global baseline plus a project symlink (if the project adds one). The agent sees the **union** of all folders.

- **Avoid duplicate ownership** of the same workflow: if a public skill already covers a topic, do not maintain a near-copy under `skills/` unless you have a documented delta ([skill-creation reference](_meta/skill-creation/reference.md#public-agent-skills-ecosystem-before-authoring)).
- **Name collisions:** two skills with the same YAML `name` can confuse discovery. Prefer one copy, or rename a fork and document why.

### Layout tip: one subfolder for this repo, siblings for vendors

If you cannot symlink the **entire** `.cursor/skills` directory (because the CLI must create sibling packages), point **only a child** at this tree—for example `.cursor/skills/pkuppens` → `…/pkuppens/skills`—and let `npx skills add` place **other** directories beside `pkuppens/`. The same pattern matches [Option B](#option-b-sync-script), which treats `pkuppens` as one child among many.

## Directory structure

```text
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
