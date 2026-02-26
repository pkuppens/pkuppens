---
name: skill-creation
description: Guides creation of new AI coding skills for Cursor, Claude, and Codex. Use when creating, writing, or authoring a new skill, or when asking about skill structure, SKILL.md format, or best practices. Enforces single responsibility, one-liner, progressive disclosure, and Claude skill structure.
---

# Creating Skills

Guides creation of new skills per REFACTORED_SKILLS.md principles and [Claude skill structure](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices#skill-structure).

## Required structure

Every skill needs a directory with `SKILL.md`:

```
skill-name/
├── SKILL.md              # Required
├── reference.md          # Optional — loaded when needed
└── examples.md          # Optional
```

### YAML frontmatter

```yaml
---
name: skill-name
description: What the skill does. Use when [trigger scenarios]. Third person, WHAT + WHEN.
---
```

- **name:** Max 64 chars, lowercase letters, numbers, hyphens only
- **description:** Max 1024 chars. Third person. Include trigger terms for discovery.

## Principles

### Single responsibility
One skill = one capability. Compose for complex workflows.

### One-liner
Skill description + one-line summary per sub-skill. Optional 1–2 comment lines. No verbose explanations.

### Progressive disclosure
- Metadata (name, description) — always loaded
- SKILL.md body — loaded when triggered
- reference.md, examples.md — loaded as needed
- Keep SKILL.md under 500 lines

### Degrees of freedom

| Level | When | Example |
|-------|------|---------|
| High | Multiple valid approaches | Code review guidelines |
| Medium | Preferred pattern, acceptable variation | Templates |
| Low | Fragile, consistency critical | Exact scripts |

## SKILL.md body template

```markdown
---
name: example-skill
description: Does X. Use when [trigger].
---

# Example Skill

## When to use
- Trigger scenario 1
- Trigger scenario 2

## Instructions
1. Step one
2. Step two
3. Step three

## Output format
[Template if needed]

## Additional resources
- See [reference.md](reference.md) for details
```

## Anti-patterns

- Vague names: `helper`, `utils`, `tools`
- First/second person in description
- Explaining what the agent already knows
- SKILL.md over 500 lines without split
- Windows-style paths (`\`)

## Arc42 alignment

For architecture-related skills, align with arc42 sections (1–12): goals, constraints, context, solution strategy, building blocks, runtime, deployment, crosscutting, decisions, quality, risks, glossary.

## Self-improvement (optional)

After creating a skill, consider: Did execution or user feedback suggest changes to this meta-skill or the new skill? Capture refinements for iteration.
