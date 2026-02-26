---
name: design-consult
description: Consults current design and architecture to place new code correctly within existing components, interfaces, and data flows. Use after architecture-consult, before implementation-construction; ensures single responsibility and correct layering.
---

# Design Consult

Maps where new code fits within existing components, interfaces, and data flows. Focuses on *detailed* placement — files, classes, method signatures — rather than high-level modules.

## When to use

- After [architecture-consult](../../architecture/architecture-consult/SKILL.md) has identified the relevant module
- Before writing new classes or functions
- When you need to decide between extending an existing class vs. creating a new one

## Instructions

1. **Read existing component** — open the relevant file(s) identified by architecture-consult; scan class/function signatures and docstrings.
2. **Check interfaces and abstractions** — look for base classes, Protocols, or ABCs the new code must implement or follow.
3. **Identify extension points** — factory functions, registries, or plugin patterns where the new code should register.
4. **Check naming conventions** — match existing patterns (module names, class names, method names, file layout).
5. **Decide: extend vs. create** — prefer extending existing abstractions; create a new file only when single responsibility demands it.
6. **Define method signatures** — draft public API (function names, parameter types, return types) before writing the body.

## Output format

```markdown
## Design Consult: [Feature/Component]

### Existing components consulted
- `path/to/file.py` — `ClassName` — [what it does]

### Interfaces / abstractions to implement
- `BaseX` in `path/to/base.py` — methods: `method_a(...)`, `method_b(...)`

### Extension point
- Register in `factory.py::create_x()` by adding a branch for `"new-type"`

### New file / class design
**File:** `module/path/new_thing.py`
**Class:** `NewThing(BaseX)`
**Public methods:**
- `method_a(param: Type) -> ReturnType`

### Naming conventions applied
- [Convention from existing code]
```

## Integration

- Follows [architecture-consult](../../architecture/architecture-consult/SKILL.md).
- Feeds into [implementation-construction](../../implementation/implementation-construction/SKILL.md).
