---
name: agent-types
description: >-
  Classifies AI agent patterns: chat completion, tool-using, ReAct, A2A protocol,
  subagents, and multi-agent orchestration. Use when choosing the right agent
  architecture for a task or comparing agent interaction patterns.
---

# Agent Types

Taxonomy of AI agent patterns, from simple to complex. Each pattern adds capabilities but also adds complexity — pick the simplest pattern that meets your requirements.

## When to use

- Starting a new agent project and choosing the architecture
- Deciding whether to add tool use, sub-agents, or multi-agent orchestration
- Implementing Agent2Agent (A2A) protocol for inter-agent communication
- Reviewing an agent system for over-engineering or missing capabilities

## Agent taxonomy

### 1. Chat completion agent

Stateless request-response wrapper around an LLM. No tools, no memory, no orchestration.

**Use when:** Simple Q&A, text generation, summarisation, translation.

```text
User prompt → LLM → Response
```

- Single turn or multi-turn with conversation history in the prompt
- System prompt defines persona and constraints
- No external data access beyond the model's training data

### 2. Tool-using agent (ReAct pattern)

Agent with access to external tools (functions, APIs, databases). Follows the Reason-Act-Observe loop: the LLM decides which tool to call, observes the result, and continues reasoning.

**Use when:** The agent needs to query databases, call APIs, perform calculations, or interact with external systems.

```text
User prompt → LLM → Tool call → Tool result → LLM → Response
                 └──────────────────────────────┘
                        (loop until done)
```

- Tool definitions as JSON schema (OpenAI function calling, Anthropic tool use)
- The LLM selects tools based on the user's intent — not hard-coded routing
- Guard against infinite loops with a maximum iteration count

### 3. Retrieval-augmented agent (RAG agent)

Tool-using agent where the primary tool is a retrieval system (vector store, search engine, knowledge graph). Combines retrieval with generation.

**Use when:** The agent must answer questions from a document corpus, knowledge base, or structured data that exceeds the context window.

See [agent-context](../agent-context/SKILL.md) for RAG pipeline design.

### 4. Subagent / delegation pattern

A parent agent delegates subtasks to specialised child agents. Each child has its own system prompt, tools, and constraints. The parent orchestrates results.

**Use when:** Tasks are decomposable into independent subtasks with different expertise requirements (e.g. research + code + review).

```text
User prompt → Orchestrator agent
                 ├─► Research agent → findings
                 ├─► Code agent → implementation
                 └─► Review agent → feedback
              Orchestrator → combined response
```

- Parent decides task decomposition and aggregation strategy
- Children can run in parallel when tasks are independent
- Each child has a focused system prompt and limited tool set

### 5. Multi-agent conversation

Multiple agents collaborate through a shared conversation or message bus. Agents take turns or respond to events. No single orchestrator.

**Use when:** Debate, peer review, simulation, or collaborative problem-solving where multiple perspectives add value.

- Round-robin, random, or LLM-routed turn selection
- Shared conversation history or message passing
- Termination conditions (consensus, max turns, human approval)

### 6. Agent2Agent (A2A) protocol agents

Agents communicate across process or network boundaries using a standardised protocol (Google A2A, custom gRPC/REST). Each agent is a service with a defined interface.

**Use when:** Agents are developed by different teams, run in different environments, or need to be composed dynamically.

- Agent card: metadata describing capabilities, input/output schemas
- Task lifecycle: submit → working → completed/failed
- Streaming support for long-running tasks
- Authentication and authorisation between agents

## Decision matrix

| Pattern | Complexity | Tool use | Memory | Multi-model | Use case |
|---------|-----------|----------|--------|-------------|----------|
| Chat completion | Low | No | Prompt only | No | Q&A, generation |
| Tool-using (ReAct) | Medium | Yes | Prompt + tool results | No | Data access, actions |
| RAG agent | Medium | Yes (retrieval) | Prompt + retrieved docs | No | Knowledge-base Q&A |
| Subagent | High | Per child | Per child | Yes | Complex decomposable tasks |
| Multi-agent | High | Per agent | Shared or per agent | Yes | Debate, collaboration |
| A2A protocol | High | Per service | Per service | Yes | Cross-team, cross-env |

## Anti-patterns

- **Over-orchestration** — using multi-agent when a single tool-using agent suffices
- **God agent** — one agent with 50+ tools instead of delegating to sub-agents
- **Missing termination** — no max iterations, leading to infinite tool-calling loops
- **Tight coupling** — agents that depend on internal implementation details of other agents
