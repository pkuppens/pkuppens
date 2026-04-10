---
name: governance-audit-trail
description: Maintains a defensible record of decisions, approvals, and changes for reviewers or regulators. Use when evidence must link requirements to code, deployments, or access control.
---

# Governance audit trail

**Evidence chain**, not live scanning — pair with [operations-audit](../../operations/operations-audit/SKILL.md) when you also need runtime checks.

## When to use

- Compliance, SOC2, ISO, or internal audits ask “show your work”
- You must prove **who** approved **what** and **when**
- Change management requires a ticket per deploy

## Instructions

1. **Scope** — system, time window, regulation or policy reference.
2. **Artefacts** — issues, PRs, ADRs, CI runs, signed tags, access logs (what is available in *this* repo).
3. **Traceability** — map requirement → issue → PR → merge → release tag (best effort).
4. **Gaps** — missing links, manual steps, debt items as issues.

## Output format

- Scope
- Artefact table (type, link, date)
- Gaps and remediation

## Anti-patterns

- Claiming “full traceability” when merges lack issue references
- Storing secrets or PII in evidence docs
