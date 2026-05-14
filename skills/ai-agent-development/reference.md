# AI Agent Development — Reference

Deep patterns, anti-patterns, and framework comparison for AI agent implementation. Companion to [SKILL.md](SKILL.md).

## Agent design patterns

### 1. Router pattern

A lightweight classifier routes user input to specialised handlers. Not a full agent — no reasoning loop.

```text
User input → Router (classifier / keyword) → Handler A | Handler B | Handler C
```

- Use when: fixed set of intents, no need for open-ended reasoning
- Implement with: intent classifier, regex, or small LLM call
- Avoids the overhead of a full ReAct loop for predictable tasks

### 2. Plan-and-execute pattern

The agent creates a plan first, then executes each step. Separates planning from execution.

```text
User input → Planner LLM → [Step 1, Step 2, Step 3]
                                    │
                              Executor (per step) → results
                                    │
                              Re-plan if needed
```

- Use when: complex multi-step tasks, long-running workflows
- Advantage: the plan is inspectable and modifiable before execution
- Framework support: LangGraph (plan-and-execute template), AutoGen

### 3. Reflection pattern

After generating output, a second LLM call critiques and refines it.

```text
User input → Generator LLM → draft output → Critic LLM → feedback
                  ▲                                          │
                  └──────────────────────────────────────────┘
                              (refine loop)
```

- Use when: output quality matters more than latency (writing, code review)
- Limit iterations (2-3 max) to prevent infinite refinement

### 4. Human-in-the-loop pattern

The agent pauses at decision points and requests human approval before continuing.

- Use when: high-stakes actions (financial transactions, data deletion, deployment)
- Implement with: LangGraph interrupt nodes, custom approval webhooks
- Log the human decision for audit trail

### 5. Supervisor pattern

A supervisor agent monitors other agents, intervenes on errors, and ensures quality.

```text
                    Supervisor
                   /     |     \
               Agent A  Agent B  Agent C
```

- Use when: multi-agent systems need quality control
- The supervisor can re-assign tasks, retry, or escalate to human

## Anti-patterns catalogue

| Anti-pattern | Description | Fix |
|-------------|-------------|-----|
| Prompt stuffing | Cramming everything into the system prompt (tools, examples, rules, history) | Split into tools, RAG, and structured prompts |
| God agent | One agent with 50+ tools | Decompose into specialised sub-agents |
| Infinite loop | No max iterations on the ReAct loop | Set `max_iterations` (5-15 typical) |
| Silent failure | Swallowing tool errors | Surface errors to the agent for recovery |
| Context amnesia | Not persisting conversation state | Add memory (sliding window, summarisation) |
| Provider coupling | Hard-coding `openai.ChatCompletion.create()` everywhere | Abstract behind provider interface |
| Eval-free deployment | Shipping agents without systematic evaluation | Build eval suites (accuracy, latency, cost) |
| Security bypass | Trusting LLM output for system commands | Validate and sandbox all agent actions |

## Framework comparison matrix (detailed)

| Criterion | LangChain | LangGraph | Semantic Kernel | AutoGen | CrewAI |
|-----------|-----------|-----------|-----------------|---------|--------|
| Primary language | Python, JS | Python, JS | C#, Python, Java | Python, C# | Python |
| Agent loop | Built-in AgentExecutor | Custom graph | ChatCompletionAgent | ConversableAgent | Crew/Task |
| Tool calling | Tool classes, @tool decorator | Same as LangChain | KernelFunction / Plugin | Function decorator | @tool decorator |
| Multi-agent | Limited (agent supervisor) | Full support (graph nodes) | AgentGroupChat | GroupChat, Swarm | Crew with roles |
| RAG support | Extensive (100+ loaders) | Same ecosystem | Plugins + connectors | Plugins | Built-in |
| State management | RunnablePassthrough | Checkpointer (SQLite, Postgres) | Kernel + DI container | Chat history | Task context |
| Streaming | Yes (astream) | Yes (astream_events) | Yes (streaming kernel) | Yes (streaming) | Limited |
| Human-in-the-loop | Manual | Interrupt nodes | Filters | Human proxy | Manual |
| On-premises | Yes (any provider) | Yes | Yes (local endpoints) | Yes | Yes |
| Production maturity | High (widely adopted) | Growing | High (Microsoft backing) | Growing | Moderate |
| Learning curve | Medium | Medium-High | Medium | Medium | Low |

## Evaluation approaches

### Offline evaluation

- **Accuracy on test set** — predefined questions with known answers; measure exact match, F1, ROUGE
- **Tool call accuracy** — does the agent call the right tool with correct arguments?
- **Retrieval quality** — precision@k, recall@k, nDCG for RAG pipelines
- **Hallucination rate** — percentage of claims not supported by retrieved context

### Online evaluation

- **User satisfaction** — thumbs up/down, explicit ratings
- **Task completion rate** — percentage of tasks completed without human escalation
- **Latency** — time to first token, total response time
- **Cost per interaction** — total LLM tokens consumed

### Evaluation tools

| Tool | Scope | Notes |
|------|-------|-------|
| RAGAS | RAG evaluation | Faithfulness, relevance, context recall |
| DeepEval | General agent eval | Hallucination, toxicity, tool use |
| LangSmith | LangChain tracing + eval | Traces, datasets, automated scoring |
| Promptfoo | Prompt testing | Assertions, comparisons, grading |
| Custom pytest | Targeted unit tests | Test tool calls, output format, edge cases |

## Security considerations

- **Tool sandboxing** — never let the agent execute arbitrary code without sandboxing (Docker, gVisor)
- **Output validation** — validate JSON output with Pydantic before acting on it
- **Credential isolation** — tools should receive scoped credentials, not the agent's full permissions
- **Network boundaries** — restrict agent HTTP access to allowlisted endpoints
- **Prompt injection defence** — separate user input from system instructions at the API level (system vs user messages)

## A2A protocol reference

Google's Agent2Agent protocol defines inter-agent communication:

- **Agent card** — JSON metadata at `/.well-known/agent.json` describing capabilities
- **Task lifecycle** — `POST /tasks` creates a task; status transitions: `submitted → working → completed | failed`
- **Streaming** — SSE (Server-Sent Events) for real-time progress updates
- **Authentication** — OAuth2 or API key between agents
- **Push notifications** — webhook callbacks for async task completion

Key design principle: agents are services with well-defined inputs and outputs, not chat partners.
