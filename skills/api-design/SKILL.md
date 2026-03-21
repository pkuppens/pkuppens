---
name: api-design
description: Enforce API design rules when adding or changing endpoints. Apply REST conventions, versioning, deduplication semantics, OpenAPI documentation.
---

# API Design

Use when designing new HTTP APIs, refactoring routes, or reviewing API changes.

## When to Invoke

- Adding a new route or router
- Changing request/response models
- Reviewing API documentation (OpenAPI, `/docs`, `/redoc`)
- Deciding between a new endpoint vs extending an existing one

## Core Rules

### 1. HTTP Verbs and Status Codes

| Verb | Use | Idempotent |
|------|-----|------------|
| GET | Retrieve, list, health | Yes |
| POST | Create, actions (domain operations) | No (unless designed idempotent) |
| PUT | Replace resource | Yes |
| DELETE | Remove | Yes |

**Upload / create semantics (common pattern)**:

- New resource: **201 Created** with a clear body
- Duplicate or idempotent hit (e.g. same hash): **200 OK** with a flag such as `created: false` — no duplicate side effects

### 2. Resource Naming

- Plural nouns: `/api/documents`, not `/api/document`
- Hierarchical: `/api/documents/{id}/chunks`
- No verbs in URLs; use HTTP method
- RPC-style actions are acceptable for domain operations when they fit the product: `/api/ask`, `/api/transcribe`

### 3. New vs Extend

**Create new** when: different resource, different contract, clear separation.
**Extend** when: same resource, minor variant, additive parameters.

### 4. Anti-Patterns

- **Duplicate endpoints** for the same operation (e.g. legacy `/api/v0/upload` next to `/api/v1/documents`) — consolidate behind one versioned surface.
- **Overlapping semantics** across routers — unify the contract.
- **Missing OpenAPI metadata** — add tags, summary, description, examples.

### 5. Checklist Before PR

- Correct HTTP verb
- Consistent naming
- OpenAPI tags, description, examples
- Pydantic models or equivalent for request/response
- Tests for the route or handler
- Project API index or changelog updated if your repo maintains it

## References

- Project-specific rules: often under `.cursor/rules/` (e.g. `api-design.mdc`)
- Technical docs: e.g. `docs/technical/API_DESIGN.md`, `API_ENDPOINTS.md` when present
