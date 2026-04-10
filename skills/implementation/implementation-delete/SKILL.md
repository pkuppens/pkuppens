---
name: implementation-delete
description: Removes dead code, unused modules, and obsolete flags safely. Use when shrinking the codebase, deleting a feature, or clearing experiment paths.
---

# Implementation delete

**Shrink** the system without breaking callers.

## When to use

- Feature is retired or behind a flag that is always off
- Copy-paste duplication was replaced by a shared module
- Security or licence requires removal of a dependency

## Instructions

1. **Prove unused** — search references, routes, CI configs; check telemetry if available.
2. **Remove in layers** — API → service → storage; update docs and OpenAPI.
3. **Migration** — data or config cleanup if required by the repo.
4. **Verify** — tests, lint, manual smoke for touched surfaces.
5. **Changelog / release note** if user-visible.

## Output format

- List of removed symbols/paths; risk note for reviewers

## Anti-patterns

- Deleting “just in case” without reference search (breaks imports at distance)
