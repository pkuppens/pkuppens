---
name: ai-agent-development
description: >-
  Guides implementation of AI agents: agent types, context/RAG, guardrails,
  swappable LLM providers, on-premises deployment, framework selection, and
  visual development. Use when designing, building, or reviewing AI agent
  systems in Python or C#.
---

# AI Agent Development

Covers the full design space for implementing AI agents — from simple chat completion wrappers to multi-agent orchestration with tool use, guardrails, and on-premises deployment. Provides framework-neutral patterns first, then maps them to concrete frameworks (LangChain/LangGraph, Semantic Kernel, AutoGen) and visual tools (n8n, Flowise).

## When to use

- Designing a new AI agent or multi-agent system
- Adding tool use, RAG, or knowledge graph integration to an existing agent
- Selecting between LangChain, Semantic Kernel, AutoGen, CrewAI, or rolling your own
- Implementing swappable LLM backends (Ollama, LlamaCPP, OpenAI, Gemini)
- Deploying agents on-premises with data sovereignty requirements
- Adding guardrails, auditing, or cost control to agent pipelines
- Evaluating visual/low-code agent builders (n8n, Flowise, LangFlow)
- Reviewing agent code for architecture and security concerns

## Sub-skills

| Sub-skill | Concern | When to use |
|-----------|---------|-------------|
| [agent-types](agent-types/SKILL.md) | Agent taxonomy | Choosing the right agent pattern for the task |
| [agent-context](agent-context/SKILL.md) | Context, RAG, knowledge graphs | Adding external knowledge to agents |
| [agent-guardrails](agent-guardrails/SKILL.md) | Auditing, safety, guardrails | Securing agent input/output and tracking usage |
| [agent-llm-providers](agent-llm-providers/SKILL.md) | Swappable LLM backends | Configuring open-source and closed-source models |
| [agent-on-premises](agent-on-premises/SKILL.md) | On-premises deployment | Running agents locally with data sovereignty |
| [agent-frameworks](agent-frameworks/SKILL.md) | Framework selection | Comparing and using agent frameworks |
| [agent-visual-dev](agent-visual-dev/SKILL.md) | Visual/GUI development | Building agents with low-code tools |

## Core design decisions

Before building an agent, resolve these:

1. **Agent pattern** — Is this a single-turn completion, a tool-using loop, a multi-agent system, or an A2A service? See [agent-types](agent-types/SKILL.md).
2. **Context strategy** — Does the agent need RAG, a knowledge graph, long-term memory, or just the prompt? See [agent-context](agent-context/SKILL.md).
3. **LLM backend** — Must it run on-premises? Which models? How do you swap providers? See [agent-llm-providers](agent-llm-providers/SKILL.md) and [agent-on-premises](agent-on-premises/SKILL.md).
4. **Safety** — What guardrails, auditing, and cost controls are needed? See [agent-guardrails](agent-guardrails/SKILL.md).
5. **Framework** — Build from scratch, use a framework, or use a visual tool? See [agent-frameworks](agent-frameworks/SKILL.md) and [agent-visual-dev](agent-visual-dev/SKILL.md).

## Architecture pattern

```
User Input
  │
  ▼
┌─────────────┐     ┌──────────────┐
│  Guardrails │────▶│  Agent Core  │
│  (input)    │     │  (reasoning) │
└─────────────┘     └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │  Tools   │ │  RAG /   │ │  Sub-    │
        │          │ │  Context │ │  agents  │
        └──────────┘ └──────────┘ └──────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  LLM        │◀── Provider interface
                    │  Provider   │    (Ollama / OpenAI / …)
                    └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  Guardrails │
                    │  (output)   │
                    └─────────────┘
                           │
                           ▼
                      Agent Output
```

## Code examples

See [examples.md](examples.md) for complete Python and C# implementations covering:

- Minimal chat completion agent
- Tool-using agent with provider abstraction
- RAG-augmented agent
- Multi-agent orchestration

## Integration with other skills

- [architecture-building-blocks](../architecture/architecture-building-blocks/SKILL.md) — agent as a building block in a larger system
- [architecture-crosscutting](../architecture/architecture-crosscutting/SKILL.md) — guardrails and auditing as crosscutting concerns
- [design-interfaces](../design/design-interfaces/SKILL.md) — LLM provider and tool interfaces
- [api-design](../api-design/SKILL.md) — exposing agents as API endpoints
- [fair-data-principles](../fair-data-principles/SKILL.md) — FAIR-aligned context and knowledge management

## Additional resources

- [reference.md](reference.md) — deep patterns, anti-patterns, framework comparison matrix
- [examples.md](examples.md) — Python and C# code examples
