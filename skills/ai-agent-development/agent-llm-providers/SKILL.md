---
name: agent-llm-providers
description: >-
  Guides implementation of swappable LLM provider interfaces for AI agents.
  Covers open-source (Ollama, LlamaCPP) and closed-source (OpenAI, Gemini)
  backends via abstract base classes and factory patterns. Use when designing
  configurable or multi-provider agent systems.
---

# Agent LLM Providers

Patterns for abstracting LLM backends behind a common interface so agents can swap between providers without changing application code. Covers provider abstraction, factory pattern, configuration, and the trade-offs of each backend.

## When to use

- Designing a new agent system that must support multiple LLM providers
- Adding a new provider to an existing multi-provider system
- Switching from cloud APIs to on-premises models (or vice versa)
- Comparing providers for cost, quality, or latency

## Provider abstraction

Define an abstract interface that all providers implement:

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class LLMResponse:
    content: str
    model: str
    input_tokens: int
    output_tokens: int

class BaseLLMProvider(ABC):
    @abstractmethod
    async def complete(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> LLMResponse:
        ...

    @abstractmethod
    async def complete_with_tools(
        self,
        messages: list[dict[str, str]],
        tools: list[dict],
        temperature: float = 0.7,
    ) -> LLMResponse:
        ...
```

### Factory pattern

```python
def create_llm_provider(backend: str, **kwargs) -> BaseLLMProvider:
    providers = {
        "ollama": OllamaProvider,
        "openai": OpenAIProvider,
        "gemini": GeminiProvider,
        "llamacpp": LlamaCPPProvider,
    }
    if backend not in providers:
        raise ValueError(f"Unknown backend: {backend}. Available: {list(providers)}")
    return providers[backend](**kwargs)
```

### Configuration via environment

```bash
LLM_BACKEND=ollama
LLM_MODEL=llama3.2
LLM_BASE_URL=http://localhost:11434
LLM_API_KEY=          # empty for local providers
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2048
```

## Provider comparison

### Open-source (on-premises capable)

| Provider | Interface | Models | GPU required | Strengths |
|----------|-----------|--------|-------------|-----------|
| Ollama | REST API (OpenAI-compatible) | Llama, Mistral, Gemma, Phi, Qwen | Recommended | Easy setup, model management, OpenAI-compatible API |
| llama.cpp | C++ library, Python bindings | GGUF format models | Optional (CPU possible) | Lightweight, quantisation support, runs on CPU |
| vLLM | REST API (OpenAI-compatible) | HuggingFace models | Yes | High throughput, production-grade serving |
| TGI (HuggingFace) | REST API | HuggingFace models | Yes | HuggingFace ecosystem integration |

### Closed-source (cloud APIs)

| Provider | SDK | Key models | Strengths |
|----------|-----|------------|-----------|
| OpenAI | `openai` Python, C# SDK | GPT-4o, GPT-4o-mini, o3 | Widest tool-calling support, mature SDK |
| Google Gemini | `google-genai` Python SDK | Gemini 2.5 Pro/Flash | Multimodal, large context window (1M tokens) |
| Anthropic | `anthropic` Python SDK | Claude Sonnet/Opus | Strong reasoning, extended thinking |
| Azure OpenAI | `openai` with Azure config | Same as OpenAI | Enterprise compliance, VNet integration |

## Design guidelines

- **OpenAI-compatible API as baseline** — Ollama, vLLM, and LiteLLM all expose OpenAI-compatible endpoints; design your provider interface around this
- **Model-specific capabilities** — not all models support tool calling, vision, or structured output; query capabilities at init or config time
- **Streaming** — implement both streaming and non-streaming completion; use streaming for interactive UIs
- **Retry with backoff** — cloud APIs rate-limit; implement exponential backoff with jitter
- **Fallback chain** — configure a primary and fallback provider for reliability (e.g. GPT-4o → Ollama local)
- **Token counting** — each provider tokenises differently; use provider-specific tokenisers for accurate counting

## C# provider abstraction (Semantic Kernel)

Semantic Kernel provides built-in provider abstraction:

```csharp
// Swap providers by changing the service registration
var builder = Kernel.CreateBuilder();

// OpenAI
builder.AddOpenAIChatCompletion("gpt-4o", apiKey);

// Azure OpenAI
builder.AddAzureOpenAIChatCompletion("gpt-4o", endpoint, apiKey);

// Ollama (OpenAI-compatible endpoint)
builder.AddOpenAIChatCompletion("llama3.2", apiKey: null,
    httpClient: new HttpClient { BaseAddress = new Uri("http://localhost:11434/v1") });
```

## Integration with other skills

- [agent-types](../agent-types/SKILL.md) — providers power all agent types
- [agent-on-premises](../agent-on-premises/SKILL.md) — on-prem model selection and serving
- [agent-guardrails](../agent-guardrails/SKILL.md) — cost control per provider
- [design-interfaces](../../design/design-interfaces/SKILL.md) — provider interface design patterns
