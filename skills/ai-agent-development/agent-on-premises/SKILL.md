---
name: agent-on-premises
description: >-
  Guides on-premises deployment of AI agents: local model serving, data
  sovereignty, air-gapped environments, GPU provisioning, and infrastructure
  patterns. Use when agents must run locally without sending data to cloud APIs.
---

# Agent On-Premises

Patterns for deploying AI agents entirely on-premises — no data leaves the local network. Covers model serving, GPU provisioning, infrastructure, and the trade-offs versus cloud deployment.

## When to use

- Data sovereignty or regulatory requirements prohibit cloud API usage (GDPR, HIPAA, government)
- Air-gapped or restricted network environments
- Sensitive data (medical records, financial data, classified information) must not leave the premises
- Cost optimisation for high-volume inference (own hardware vs pay-per-token)
- Low-latency requirements where cloud round-trips are unacceptable

## Architecture

```
On-Premises Network
┌──────────────────────────────────────────────────┐
│                                                  │
│  ┌──────────┐    ┌─────────────┐   ┌──────────┐ │
│  │  Agent    │───▶│  Model      │   │  Vector  │ │
│  │  App      │    │  Server     │   │  Store   │ │
│  │ (FastAPI) │    │ (Ollama /   │   │ (Chroma /│ │
│  └──────────┘    │  vLLM)      │   │  Qdrant) │ │
│       │          └─────────────┘   └──────────┘ │
│       │                │                  │      │
│       └────────────────┼──────────────────┘      │
│                        │                         │
│                  ┌─────┴─────┐                   │
│                  │   GPU(s)  │                   │
│                  └───────────┘                   │
└──────────────────────────────────────────────────┘
```

## Model serving options

| Server | Setup complexity | Production-ready | GPU support | Quantisation |
|--------|-----------------|-----------------|-------------|-------------|
| Ollama | Low (single binary) | Development / small teams | CUDA, ROCm, Metal | GGUF (Q4, Q5, Q8) |
| vLLM | Medium (Python) | Yes (high throughput) | CUDA | AWQ, GPTQ, FP8 |
| TGI | Medium (Docker) | Yes (HuggingFace) | CUDA | GPTQ, AWQ, EETQ |
| llama.cpp | Low (C++ binary) | Development | CUDA, Metal, Vulkan, CPU | GGUF (extensive) |
| LocalAI | Medium (Docker) | Community | CUDA, CPU | GGUF, GPTQ |

## GPU provisioning

### Minimum GPU memory by model size

| Model parameters | Min GPU VRAM (FP16) | Min GPU VRAM (Q4) | Example GPU |
|-----------------|--------------------|--------------------|-------------|
| 1-3B | 4 GB | 2 GB | RTX 3060 (12 GB) |
| 7-8B | 16 GB | 4-6 GB | RTX 4070 (12 GB) |
| 13B | 28 GB | 8-10 GB | RTX 4090 (24 GB) |
| 30-34B | 68 GB | 20-24 GB | A100 (40 GB) or 2x RTX 4090 |
| 70B | 140 GB | 40-48 GB | A100 (80 GB) or 2x A100 (40 GB) |

### Quantisation trade-offs

- **Q4_K_M** — good balance of quality and memory (most common for on-prem)
- **Q5_K_M** — slightly better quality, 25% more memory
- **Q8_0** — near-FP16 quality, double the Q4 memory
- **FP16** — full precision, requires most memory, best quality

## Docker Compose pattern

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:11434/api/tags"]
      interval: 30s
      retries: 3

  chromadb:
    image: chromadb/chroma:latest
    ports:
      - "8000:8000"
    volumes:
      - chroma_data:/chroma/chroma

  agent:
    build: .
    ports:
      - "8080:8080"
    environment:
      LLM_BACKEND: ollama
      LLM_BASE_URL: http://ollama:11434
      LLM_MODEL: llama3.2
      CHROMA_URL: http://chromadb:8000
    depends_on:
      ollama:
        condition: service_healthy
```

## Air-gapped deployment

For environments with no internet access:

1. **Pre-download models** on a connected machine (`ollama pull`, download GGUF files)
2. **Transfer via secure media** (USB, approved file transfer)
3. **Load from local volume** — mount the model directory into the container
4. **Pre-build Docker images** — save with `docker save`, load with `docker load`
5. **Embedding models** — download sentence-transformers models and serve locally

## Data sovereignty checklist

- [ ] No API calls leave the local network (verify with network monitoring)
- [ ] All models are served locally (no cloud model fallback)
- [ ] Embedding generation is local (not using cloud embedding APIs)
- [ ] Vector store runs on local infrastructure
- [ ] Audit logs are stored locally
- [ ] Model updates follow an approved change process (no auto-download)

## Integration with other skills

- [agent-llm-providers](../agent-llm-providers/SKILL.md) — on-prem provider configuration
- [agent-context](../agent-context/SKILL.md) — local vector stores and embedding models
- [agent-guardrails](../agent-guardrails/SKILL.md) — on-prem PII filtering
- [deployment-build](../../deployment/deployment-build/SKILL.md) — container image builds
- [deployment-release](../../deployment/deployment-release/SKILL.md) — on-prem release process
