---
name: agent-visual-dev
description: >-
  Guides visual and GUI-based AI agent development with n8n, Flowise, and
  LangFlow. Covers low-code orchestration, when to use visual tools vs code,
  and on-premises self-hosting. Use when evaluating or building agents with
  visual workflow tools.
---

# Agent Visual Development

Patterns for building AI agents with visual/GUI tools instead of (or alongside) code. Covers n8n, Flowise, LangFlow, and when visual development is the right choice.

## When to use

- Evaluating visual agent builders for rapid prototyping
- Non-developers need to create or modify agent workflows
- Building agent pipelines where visual flow representation aids understanding
- Comparing visual tools vs code-first frameworks
- Self-hosting visual tools on-premises

## Tool comparison

| Tool | Focus | Self-hosted | LLM integrations | Agent capabilities |
|------|-------|-------------|-------------------|--------------------|
| **n8n** | General workflow automation + AI | Yes (Docker, npm) | OpenAI, Ollama, Anthropic, Azure | AI agent node, tool use, memory, sub-workflows |
| **Flowise** | LangChain visual builder | Yes (Docker, npm) | All LangChain providers | Chains, agents, RAG, tools, chatflows |
| **LangFlow** | LangChain/LangGraph visual builder | Yes (pip, Docker) | All LangChain providers | Flows, agents, RAG, custom components |
| **Dify** | LLM app platform | Yes (Docker) | OpenAI, Ollama, Azure, HuggingFace | Agents, RAG, workflow orchestration |
| **Rivet** | Visual AI pipeline editor | Desktop app | OpenAI, Anthropic | Graph-based prompt chains, evaluation |

## When visual vs code

| Factor | Visual tools | Code-first |
|--------|-------------|------------|
| Prototyping speed | Fast — drag and drop | Slower for initial setup |
| Complex logic | Limited — hard to express conditional branching | Full control |
| Version control | Limited — JSON export, harder to diff | Native git workflow |
| Testing | Manual via UI | Automated test suites |
| Debugging | Visual trace, step-by-step | Standard debugging tools |
| Team scaling | Good for small teams, non-devs | Better for engineering teams |
| Production deployment | Possible but less mature | Standard CI/CD pipelines |
| On-premises | All tools above support self-hosting | Full control |

### Recommended approach

- **Prototype** with visual tools to validate the agent design
- **Implement** in code for production systems that need testing, CI/CD, and version control
- **Hybrid** — use n8n for workflow orchestration, call code-based agents as HTTP services

## n8n for AI agents

n8n stands out as the most general-purpose option with strong AI capabilities:

- **AI Agent node** — built-in ReAct agent with tool use
- **Memory nodes** — conversation history (buffer, window, vector store-backed)
- **Tool nodes** — HTTP request, code execution, database queries, calculator
- **RAG workflow** — document loaders, text splitters, embeddings, vector stores
- **Sub-workflows** — compose complex agent pipelines from reusable pieces
- **Self-hosted** — Docker or npm install; runs entirely on-premises
- **Credentials** — manage API keys securely with built-in credential store

### n8n Docker setup (on-premises)

```yaml
services:
  n8n:
    image: n8nio/n8n:latest
    ports:
      - "5678:5678"
    environment:
      N8N_BASIC_AUTH_ACTIVE: "true"
      N8N_BASIC_AUTH_USER: admin
      N8N_BASIC_AUTH_PASSWORD: changeme
    volumes:
      - n8n_data:/home/node/.n8n
```

## Flowise and LangFlow

Both are visual frontends for LangChain:

- **Flowise** — Node.js based, simpler UI, focuses on chatflows and RAG
- **LangFlow** — Python based, closer to LangChain/LangGraph API, supports custom Python components

Choose Flowise for quick RAG chatbots. Choose LangFlow when you need LangGraph integration or custom Python components.

## Self-hosting checklist

- [ ] Deploy with Docker Compose (all tools above support it)
- [ ] Configure persistent storage for workflows and credentials
- [ ] Set up authentication (basic auth, OAuth, or reverse proxy)
- [ ] Connect to local LLM server (Ollama) — no cloud API needed
- [ ] Back up workflow definitions (export JSON, or mount config volume)
- [ ] Monitor resource usage (CPU, memory, GPU if applicable)

## Integration with other skills

- [agent-frameworks](../agent-frameworks/SKILL.md) — visual tools complement code-first frameworks
- [agent-on-premises](../agent-on-premises/SKILL.md) — self-hosting visual tools locally
- [agent-llm-providers](../agent-llm-providers/SKILL.md) — configuring LLM providers in visual tools
- [deployment-build](../../deployment/deployment-build/SKILL.md) — Docker-based deployment of visual tools
