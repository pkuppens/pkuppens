---
name: agent-guardrails
description: >-
  Guides implementation of AI agent guardrails: input/output validation,
  PII filtering, cost control, safety policies, and audit logging. Use when
  securing agent pipelines or adding compliance and observability.
---

# Agent Guardrails

Patterns for securing AI agent input and output, controlling costs, protecting privacy, and maintaining audit trails. Guardrails wrap the agent core — they do not replace good prompt engineering.

## When to use

- Adding input validation or output filtering to an agent
- Implementing PII detection and redaction
- Setting up cost controls (token budgets, rate limits)
- Adding audit logging for compliance or debugging
- Reviewing agent security posture

## Guardrail architecture

Guardrails apply at two points in the agent pipeline:

```text
User Input → [Input Guardrails] → Agent Core → [Output Guardrails] → User Output
                                       │
                                  [Audit Log]
```

### Input guardrails

| Guardrail | Purpose | Implementation |
|-----------|---------|----------------|
| Prompt injection detection | Block attempts to override system instructions | Pattern matching, classifier model, or dedicated guardrail LLM |
| Input sanitisation | Strip dangerous content (scripts, SQL) | Regex/allowlist filtering |
| Topic restriction | Reject off-topic or prohibited queries | Classifier or keyword filter |
| Rate limiting | Prevent abuse and control costs | Token bucket, sliding window |
| Authentication | Verify caller identity | OAuth2, API key, JWT validation |

### Output guardrails

| Guardrail | Purpose | Implementation |
|-----------|---------|----------------|
| PII filtering | Redact personal data from responses | Named entity recognition (spaCy, Presidio) |
| Content policy | Block harmful, biased, or inappropriate output | Content classifier, keyword blocklist |
| Hallucination detection | Flag unsupported claims | Cross-reference with retrieved sources |
| Format validation | Ensure structured output matches expected schema | JSON schema validation, Pydantic parsing |
| Citation enforcement | Require source references in responses | Post-processing check against retrieved docs |

## PII filtering

Use Microsoft Presidio or spaCy NER for on-premises PII detection:

- **Detection** — identify PII entities (names, emails, phone numbers, SSNs, medical IDs)
- **Redaction** — replace with placeholders (`[PERSON]`, `[EMAIL]`)
- **Pseudonymisation** — replace with consistent fake values for testing
- **Audit** — log what was redacted (type, position) without logging the actual PII

Healthcare-specific: filter patient identifiers, medical record numbers, and clinical data per HIPAA/GDPR.

## Cost control

- **Token budgets** — set max input + output tokens per request and per session
- **Model routing** — use cheaper models for simple tasks, expensive models for complex ones
- **Caching** — cache identical or semantically similar queries to avoid redundant LLM calls
- **Circuit breaker** — disable the agent if spend exceeds a threshold

```python
class CostGuard:
    def __init__(self, max_tokens_per_request: int, max_cost_per_day: float):
        self.max_tokens_per_request = max_tokens_per_request
        self.max_cost_per_day = max_cost_per_day
        self.daily_cost = 0.0

    def check(self, estimated_tokens: int, cost_per_token: float) -> bool:
        estimated_cost = estimated_tokens * cost_per_token
        if estimated_tokens > self.max_tokens_per_request:
            return False
        if self.daily_cost + estimated_cost > self.max_cost_per_day:
            return False
        return True
```

## Audit logging

Every agent interaction should produce an audit record:

| Field | Description |
|-------|-------------|
| `request_id` | Unique identifier for the interaction |
| `timestamp` | ISO 8601 timestamp |
| `user_id` | Authenticated caller identity |
| `model` | LLM model used |
| `input_tokens` | Token count for the input |
| `output_tokens` | Token count for the output |
| `tools_called` | List of tools invoked with arguments (redacted) |
| `guardrails_triggered` | Which guardrails fired and their action (block, redact, warn) |
| `latency_ms` | End-to-end response time |
| `cost` | Estimated cost of the interaction |

- Store audit logs separately from application logs
- Never log raw user input or LLM output in production (PII risk) — log hashes or redacted versions
- Retention policy aligned with compliance requirements (GDPR: purpose-limited, HIPAA: 6 years)

## Frameworks and libraries

| Tool | Language | Scope |
|------|----------|-------|
| Guardrails AI | Python | Input/output validation with RAIL specs |
| NeMo Guardrails (NVIDIA) | Python | Programmable guardrails for LLM apps |
| Microsoft Presidio | Python | PII detection and anonymisation |
| LangChain output parsers | Python | Structured output validation |
| Semantic Kernel filters | C# | Pre/post-processing in the SK pipeline |

## Integration with other skills

- [agent-types](../agent-types/SKILL.md) — guardrails apply to all agent types
- [agent-on-premises](../agent-on-premises/SKILL.md) — on-prem PII filtering avoids sending data to cloud
- [operations-audit](../../operations/operations-audit/SKILL.md) — audit trail integration
- [architecture-crosscutting](../../architecture/architecture-crosscutting/SKILL.md) — guardrails as crosscutting concern
