---
name: code-quality-design
description: Apply complexity management, naming, and function design principles from Code Complete 2 and A Philosophy of Software Design. Use when designing modules, refactoring, or reviewing code for structural quality.
---

# Code Quality: Design and Structure

Principles from McConnell and Ousterhout. Apply by default on every generation, refactor, and review.

## Complexity Management

- **Primary goal**: Reduce complexity — anything that makes code harder to understand or modify.
- **Never add complexity for anticipated future needs.** Build what is required now.
- **Isolate complexity.** If logic is inherently complex, contain it in one module with a simple interface. Do not leak into callers.
- **Avoid tactical programming.** Do not take shortcuts that create confusion tomorrow. If a design feels wrong, propose an alternative before implementing.

## Naming

Names are the primary documentation. A good name lets the reader skip the implementation.

- **Precise and unambiguous.** Avoid: `data`, `result`, `info`, `manager`, `handler`, `helper`, `utils`. Prefer domain-specific names such as `chunked_document`, `embedding_response`, `pii_scan_result`.
- **Function names describe what they return or do**, not how: `get_relevant_chunks()` not `run_vector_search_and_filter()`.
- **Booleans** read as true/false: `is_authenticated`, `has_audit_trail`, `requires_network`.
- **Do not abbreviate** unless domain-standard (e.g. `jwt`, `api`, `llm`).
- **Consistency.** If one module uses `document`, do not use `doc`, `file`, or `artifact` elsewhere for the same concept.

## Function and Module Design

- **Functions do one thing.** If you need "and" to describe it, split. Can you write a one-line docstring without "and"?
- **Deep modules, shallow interfaces.** Hide complexity behind minimal, stable interfaces. Prefer fewer, richer public functions.
- **Function length = cohesion.** Many lines serving one purpose can be fine. A few lines doing two unrelated things is too long.
- **Limit parameters to four or fewer.** Use structured models (Pydantic, dataclasses, typed structs) for more.
- **Avoid flag parameters** (`process(doc, is_streaming=True)`). They signal two behaviours — split instead.
- **Files under ~500 lines** (project convention). If larger, split by responsibility.
