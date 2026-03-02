# Value Proposition: Complete Software Development Department

*Created as part of [#23](https://github.com/pkuppens/pkuppens/issues/23).*

## Messaging

### Headline / Tagline

**One professional, end-to-end capability—architecture, development, testing, deployment, process, and AI automation.**

### Supporting Bullets

1. **Architecture & delivery**: arc42-aligned design, ADRs, lifecycle from ideation to production. Proven at ASML, Philips, CART-Tech, Nemo.
2. **AI-assisted workflow**: Curated skills library for Cursor, Claude, and Codex—rules, skills, and agents that orchestrate the full software process. Not just "uses ChatGPT"; structured, repeatable workflows.
3. **Domain experience**: Healthcare (medical device, DICOM, IEC 62304), finance (anomaly detection, transaction monitoring), high-tech (EUV, GIS).

## Demo Plan

### What to Show in the Profile

| Element | Location | Purpose |
|---------|----------|---------|
| Value proposition headline | README top | Immediate differentiation |
| Skills library + SKILL_TREE | README, skills/ | Demonstrate agentic workflow design |
| on_prem_rag | Pinned repo | Full-stack AI, RAG, FastAPI |
| babblr | Pinned repo | Product, Electron, LLM integration |
| healthcare-aigent | Pinned repo | Healthcare AI, agent patterns |

### What to Highlight in Conversations / Proposals

- "I bring a complete workflow: from requirements and architecture to implementation, testing, and deployment. One person replaces multiple roles."
- "My skills library shows how I structure AI coding assistants—rules, skills, agents—for consistent, auditable output."
- "Healthcare and finance experience: regulated environments, data sovereignty, compliance."

### Optional: One-Pager Outline

1. Intro: value proposition
2. Capabilities: architecture, development, AI automation, domain
3. Evidence: projects, skills library, certifications
4. Availability: freelance, near Den Bosch, remote
5. Contact: LinkedIn, website, GitHub

## Integration with Profile

- Headline: integrated into README intro or new section
- Bullets: 2–3 under a "What I offer" or similar section
- Skills showcase: extend AI Coding Skills Library section with rules/skills/agents mention
- Consistency: align tagline with pieterkuppens.net and LinkedIn (follow-up task)

## Claude Agents / Rules / Skills Showcase

The `skills/` directory demonstrates:

- **Rules**: CLAUDE.md, skills/CLAUDE.md—how AI assistants are instructed
- **Skills**: SKILL.md files per capability—single-responsibility, composable
- **Agents**: SKILL_TREE.md—orchestration (software-engineering-process) invokes phase skills

Example flow: `issue-workflow` → `architecture-consult` → `implementation-construction` → `quality-gate`. This is not generic prompt engineering; it’s a documented, versioned workflow aligned with arc42 and the full lifecycle.

**Profile copy**: "Includes agent rules, skills, and workflow definitions for Cursor, Claude, and Codex—ideation through deployment."
