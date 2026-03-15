---
name: architecture-glossary
description: Maintains glossary of business and technical terms (arc42 §12). Use when defining domain vocabulary or resolving terminology ambiguity.
---

# Architecture Glossary

Maintains ubiquitous language — shared vocabulary across architecture, code, and UI. Aligns with arc42 §12 (glossary). DDD concept: same terms everywhere to avoid confusion.

## When to use

- Defining new domain concepts or clarifying existing ones
- Resolving ambiguity (e.g. "Transcription" vs "Speech-to-Text")
- Onboarding — new team members learning terminology
- Architecture reviews — ensuring consistent vocabulary
- Refactoring — when considering renames

## Output

`docs/architecture/07-ubiquitous-language.md`

## Definition entry format

```markdown
### Term Name
**Category:** Domain Concept / Technical Concept / UI Concept
**Definition:** Clear, concise definition.
**Synonyms:** Alternative terms (list all)
**Related Terms:** Related but distinct
**Usage Examples:** Code, documentation, UI
**Anti-patterns:** ❌ Don't call it X (confusing)
**References:** [Component](../components/...), [ADR](../adr/...)
```

## Synonym groups

When multiple terms refer to same concept:

```markdown
### Speech-to-Text / Transcription / STT
**Preferred Term:** Speech-to-Text
**Acceptable Synonyms:** Transcription (code), STT (deprecated)
**Definition:** Converting spoken audio into written text.
**Usage Guidelines:** Doc: "Speech-to-Text"; Code: `transcribe()` acceptable
```

## Operations

- **Look up**: Read glossary, search term, display definition
- **Define**: Check if exists; create entry; cross-reference ADRs, components
- **List**: Extract headings, display alphabetically
- **Validate**: Search codebase for inconsistent usage; report violations

## Update rules

- Evidence-based: include code examples
- Living document: update during refactoring
- Document synonyms when multiple terms exist

## Integration

- [architecture-decisions](../architecture-decisions/SKILL.md) for terminology ADRs
- [architecture-building-blocks](../architecture-building-blocks/SKILL.md) for component terms
