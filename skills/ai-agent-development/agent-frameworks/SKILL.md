---
name: agent-frameworks
description: >-
  Compares AI agent frameworks: LangChain/LangGraph, Semantic Kernel, AutoGen,
  CrewAI. Guides framework selection based on language, agent pattern, and
  deployment constraints. Use when choosing or evaluating an agent framework.
---

# Agent Frameworks

Comparison and guidance for AI agent frameworks. Covers Python-first frameworks (LangChain, LangGraph, CrewAI, AutoGen) and C#-first frameworks (Semantic Kernel, AutoGen for .NET). Helps select the right framework based on requirements.

## When to use

- Evaluating frameworks for a new agent project
- Migrating between frameworks
- Comparing LangChain vs Semantic Kernel vs rolling your own
- Deciding between code-first and visual agent builders

## Framework comparison

| Framework | Language | Agent pattern | Strengths | Weaknesses |
|-----------|----------|---------------|-----------|------------|
| **LangChain** | Python, JS | Chains, agents, tools | Largest ecosystem, most integrations | Frequent breaking changes, abstraction overhead |
| **LangGraph** | Python, JS | Graph-based agent orchestration | Explicit state machines, checkpointing, human-in-the-loop | Steeper learning curve than plain LangChain |
| **Semantic Kernel** | C#, Python, Java | Plugins, planners, agents | Microsoft ecosystem, Azure integration, enterprise-ready | Smaller community than LangChain |
| **AutoGen** | Python, C# | Multi-agent conversations | Strong multi-agent patterns, Microsoft backing | API still evolving (v0.4+) |
| **CrewAI** | Python | Role-based agent teams | Simple multi-agent setup, task delegation | Less flexible than LangGraph for complex flows |
| **Haystack** | Python | Pipeline-based RAG and agents | Clean pipeline abstraction, production-focused | Smaller agent feature set than LangChain |
| **Custom** | Any | Any | Full control, no dependency overhead | Must build everything from scratch |

## When to use which

### LangChain / LangGraph (Python)

Choose when:

- Python is the primary language
- You need extensive integrations (100+ vector stores, LLM providers, tools)
- Building graph-based agent workflows with state management
- Human-in-the-loop approval patterns are needed

```python
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI

def agent_node(state: MessagesState):
    llm = ChatOpenAI(model="gpt-4o")
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

graph = StateGraph(MessagesState)
graph.add_node("agent", agent_node)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)
app = graph.compile()
```

### Semantic Kernel (C#)

Choose when:

- C# / .NET is the primary language
- Azure OpenAI is the LLM backend
- Enterprise requirements (compliance, audit, RBAC)
- Integrating with existing .NET microservices

```csharp
var kernel = Kernel.CreateBuilder()
    .AddAzureOpenAIChatCompletion("gpt-4o", endpoint, apiKey)
    .Build();

kernel.Plugins.AddFromType<TimePlugin>();
kernel.Plugins.AddFromType<SearchPlugin>();

var agent = new ChatCompletionAgent
{
    Kernel = kernel,
    Name = "Assistant",
    Instructions = "You are a helpful assistant."
};
```

### AutoGen (Python / C#)

Choose when:

- Multi-agent conversation is the primary pattern
- Agents need to debate, review, or collaborate
- You want built-in conversation management

### CrewAI (Python)

Choose when:

- Role-based agent teams (researcher, writer, reviewer)
- Task delegation with simple sequential or parallel workflows
- Rapid prototyping of multi-agent systems

### Custom / no framework

Choose when:

- Simple single-agent with a few tools
- Maximum control over the agent loop
- Minimal dependencies are a requirement
- The framework abstraction adds more complexity than it removes

## Framework selection checklist

- [ ] **Language** — Does the framework support your primary language?
- [ ] **Agent pattern** — Does it match the agent type you need (single, multi-agent, graph)?
- [ ] **LLM providers** — Does it support your required providers (cloud + on-prem)?
- [ ] **Tool ecosystem** — Are the integrations you need available (vector stores, APIs)?
- [ ] **Production readiness** — Is it stable enough for production (versioning, support)?
- [ ] **On-premises** — Can it run without cloud dependencies?
- [ ] **Learning curve** — Can your team adopt it within the project timeline?

## Anti-patterns

- **Framework lock-in** — coupling business logic tightly to framework abstractions; keep core agent logic framework-independent where possible
- **Abstraction tax** — using a framework for a 20-line agent loop; the framework overhead outweighs the benefit
- **Version chasing** — upgrading LangChain every week; pin versions and upgrade deliberately
- **One framework for everything** — using LangChain for a simple completion wrapper that needs 3 lines of `openai` SDK

## Integration with other skills

- [agent-types](../agent-types/SKILL.md) — framework capabilities per agent pattern
- [agent-llm-providers](../agent-llm-providers/SKILL.md) — provider support per framework
- [agent-visual-dev](../agent-visual-dev/SKILL.md) — visual alternatives to code-first frameworks
- [ideation-reuse-check](../../ideation/ideation-reuse-check/SKILL.md) — checking if a framework already solves the problem
