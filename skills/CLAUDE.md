# skills/ — Agent Instructions

When working in this directory, follow these rules.

## Scope

This directory contains unified AI coding skills for Cursor, Claude, and Codex. Skills are committed to the repo and referenced via symlinks from IDE expected locations.

## Structure

- Each skill lives in its own directory with `SKILL.md`
- Skill tree overview: [SKILL_TREE.md](SKILL_TREE.md)
- Cooperation patterns: [COOPERATION.md](COOPERATION.md)
- Meta-skills (e.g. skill-creation, human-ai-execution) in `_meta/`
- Optional V-model overlay: [v-model/SKILL.md](v-model/SKILL.md)

## Creating or editing skills

1. Use [skill-creation](_meta/skill-creation/SKILL.md) for new skills
2. Follow SKILL_TREE.md principles: single responsibility, one-liner, progressive disclosure
3. Conform to [Claude skill structure](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices#skill-structure) and the [Agent Skills specification](https://agentskills.io/specification): YAML frontmatter (`name`, `description`), concise body, progressive disclosure. Quote `description` when it contains colons.
4. Keep SKILL.md under ~300 lines; use reference.md, examples.md for details; add additional small skills when exceeding 300 lines.

Validation policy: [ADR 001 — Skill validation and tooling](../docs/skills/decisions/001-skill-validation-and-tooling.md).

## Scratch

Scratch files (research, drafts, skill reflection, and skill improvement suggestions) live in `tmp/skills/` at repo root, gitignored.
