---
name: v-model-retrofit
description: Applies V-model traceability to brownfield codebases via explicit retrofit issues or touch-driven updates during normal work. Use when the system was built without a closed V. Third person.
---

# V-model retrofit (brownfield)

Most code never had a perfect left/right V. This skill defines **two modes** so agents do not imply a big-bang rewrite.

## Mode A — Explicit retrofit

**Trigger:** User request or a dedicated issue (label `retrofit:explicit`).

**Goal:** Backfill traceability for a named scope (module, bounded context, feature area).

**Steps:**

1. Understand **as-built** state: [architecture-document-existing](../../architecture/architecture-document-existing/SKILL.md), [architecture-consult](../../architecture/architecture-consult/SKILL.md) as needed.
2. Scope with [issue-work-down](../../issue-workflow/issue-work-down/SKILL.md); define **acceptance criteria for the retrofit** (e.g. “ADRs for boundaries X/Y”, “integration tests for API Z”).
3. Apply pairing sub-skills ([v-model](../SKILL.md)) **inside that scope only**; prefer **small PRs**.
4. When inferring *intent* from legacy behaviour, treat conclusions as **human-review** or **human-required** — do not silently elevate guesses to requirements. See [_meta/human-ai-execution.md](../../_meta/human-ai-execution.md).

## Mode B — Touch-driven (incremental)

**Trigger:** Ordinary bugfix or feature work; label `retrofit:incremental` optional.

**Goal:** Strengthen the V only for **surfaces touched** by this change unless the user widens scope.

**Steps:**

1. Map the change to the issue **acceptance criteria** ([issue-acceptance-criteria](../../issue-workflow/issue-acceptance-criteria/SKILL.md)).
2. Add or adjust **tests** proving the AC for this change ([validation-draft](../../validation/validation-draft/SKILL.md), [test-write](../../test/test-write/SKILL.md)).
3. If the change invalidates an undocumented assumption, add the **smallest** helpful ADR or architecture note ([architecture-decisions](../../architecture/architecture-decisions/SKILL.md) or consult) — **do not** document the entire system because one helper changed.
4. If the touch reveals a **large gap**, comment on the issue or open a follow-up; do not silently expand scope.

## Relation to architecture Retrofitting

[Architecture](../../architecture/SKILL.md) **Retrofitting** mode answers **what is**. `v-model-retrofit` adds **how we verify it** and links evidence to issues and artefacts.

## Related

- [plan](../../plan/SKILL.md) — optional V-model note during implementation planning
- [v-model-mapping](../v-model-mapping/SKILL.md)
