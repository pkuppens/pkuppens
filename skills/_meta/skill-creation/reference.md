# Skill authoring — reference

Companion to [SKILL.md](SKILL.md). Load when patterns, examples, or checklists are needed.

**Size:** Prefer keeping this file under ~500 lines; split into extra files (e.g. `reference-patterns.md`) if it grows.

## Token discipline

The context window is shared. Default assumption: the agent already knows general programming; add only non-obvious procedures, project facts, and fragile steps.

Ask per paragraph: *Does the agent need this? Does it justify its token cost?*

**Good (concise):**

```markdown
## Extract PDF text

Use pdfplumber:

\`\`\`python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
\`\`\`
```

**Bad (verbose):** Long genre explanation of what PDFs are before naming a library.

## Description snippets and failures

```yaml
# Strong
description: Extract text and tables from PDFs, fill forms, merge documents. Use when working with PDFs, forms, or document extraction.

# Strong
description: Analyze Excel workbooks, pivot tables, and charts. Use when analyzing .xlsx files or tabular exports.

# Weak
description: Helps with documents
```

## Common patterns

### Template pattern

Give the agent a fixed output skeleton:

```markdown
## Report structure

\`\`\`markdown
# [Title]

## Executive summary
[One paragraph]

## Findings
- …

## Recommendations
1. …
\`\`\`
```

### Examples pattern

Show input → output pairs when format quality matters:

```markdown
## Commit message format

**Example 1**  
Input: Added user authentication with JWT  
Output:
\`\`\`
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
\`\`\`
```

### Workflow pattern

```markdown
## Task checklist

Task progress:
- [ ] Step 1: …
- [ ] Step 2: …

**Step 1**  
Run: \`python scripts/analyze_form.py input.pdf\`
```

### Conditional workflow pattern

Branch on intent:

```markdown
1. **Creating new content?** → Creation workflow below.
2. **Editing existing content?** → Editing workflow below.
```

### Feedback loop pattern

For quality-critical work:

```markdown
1. Make edits.
2. Run \`python scripts/validate.py output/\`.
3. On failure: fix and repeat until clean.
```

## Utility scripts

Prefer checked-in scripts when steps are brittle or must stay reproducible:

- More reliable than ad-hoc generated code
- Saves tokens if the skill points to execution instead of pasting logic
- States clearly whether the agent should **execute** or **only read** the script as spec

Example block for `SKILL.md` or here:

```markdown
**extract_fields.py** — list PDF form fields
\`\`\`bash
python scripts/extract_fields.py input.pdf > fields.json
\`\`\`
```

## Anti-patterns

| Issue | Prefer |
|-------|--------|
| Windows-only doc paths (`foo\\bar`) | POSIX-style \`scripts/helper.py\` in prose |
| Tool salad ("use pypdf or pdfplumber or …") | One default tool + short escape hatch |
| Deadlines baked into prose ("before August 2025 …") | "Current approach" vs collapsible deprecated |
| Mixed vocabulary ("endpoint" / "route" / "URL" for same thing) | Pick one term |
| Names like \`helpers\`, \`utils\`, \`tools\` | Specific verb-noun slug: \`deployment-release\`, \`code-review\` |

## Phased workflow (implementation aid)

When helping a human author a skill:

1. **Discovery** — purpose, location (personal vs project), triggers, constraints, precedent skills.
2. **Design** — folder name (\`skill-name\`), description draft, outline, whether \`reference.md\` /\`scripts/\` are needed.
3. **Implement** — create tree, frontmatter, body, sibling files.
4. **Verification** — run [Pre-merge checklist](#pre-merge-checklist); spot-check triggers with a teammate or second session.

AskQuestion prompts (examples):

- "Store under personal synced \`skills/\` or repo \`.cursor/skills/\` only?"
- "Include executable scripts?"

## Complete example layout

```
code-review/
├── SKILL.md
├── STANDARDS.md
└── examples.md
```

**Sample `SKILL.md` excerpt:**

```markdown
---
name: code-review
description: Reviews changes for correctness, security, and maintainability per team standards. Use when reviewing pull requests, diffs, or when the user requests a code review.
---

# Code review

## Quick start
1. Correctness and edge cases
2. Security (injection, authz, secrets)
3. Readability and test coverage

## Checklist
- [ ] Logic and edge cases
- [ ] Security issues
- [ ] Style and structure
- [ ] Tests adequately cover changes

## Feedback levels
- **Critical** — must fix before merge
- **Suggestion** — should improve
- **Nice to have** — optional

## Additional resources
- [STANDARDS.md](STANDARDS.md)
- [examples.md](examples.md)
```

## Pre-merge checklist

**Core**

- [ ] \`description\` is third person with WHAT + WHEN and concrete trigger terms
- [ ] \`name\` matches folder and naming rules
- [ ] Primary \`SKILL.md\` stays within agreed budget (~≤300 lines); oversized parts moved here or to \`examples.md\`
- [ ] Terminology is consistent throughout

**Structure**

- [ ] Links from \`SKILL.md\` to deeper files are **one level deep**
- [ ] Workflows read as ordered, checkable steps
- [ ] Time-sensitive lore avoided or isolated under deprecated/legacy headings

**Scripts**

- [ ] Scripts are documented (deps, inputs, outputs)
- [ ] Explicit whether agents run or read them

## Optional: trimmed project-facing copy

For a **repository that only needs a subset** (e.g. public OSS without personal paths):

1. Copy **When to use**, **Instructions**, and **Output format** sections into that repo’s \`.cursor/skills/<skill-name>/SKILL.md\`.
2. Remove references to machine-specific junctions (\`~\`) and internal mono-repo paths unless the repo is private.
3. Keep one link back to upstream docs or this \`skills/\` repo if governance requires a single authority.

Compose with the main skill repo as source of truth; avoid long-lived divergence without versioning notes.
