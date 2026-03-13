---
name: openclaw-security
description: Enforces OpenClaw security constraints and mandates security audit before every code-change PR. Use when working on OpenClaw projects, before opening a PR, or when configuring or hardening OpenClaw.
---

# OpenClaw Security

Enforces the security posture required for OpenClaw. Mandatory for every code-change PR in OpenClaw projects.

## When to use

- Before every PR that changes OpenClaw code or configuration
- When configuring or hardening an OpenClaw deployment
- When adding tools, gateways, or shared inboxes
- As part of [quality-gate](../quality-gate/SKILL.md) for OpenClaw repos

## Mandatory PR requirement

**Every code-change PR must include a passing OpenClaw security audit.** Run before opening the PR:

```bash
openclaw security audit --deep
openclaw security audit --fix
```

Both must complete successfully. Do not bypass. If audit fails, fix issues before integration-commit and integration-pr.

## Security constraints (non-negotiable)

OpenClaw is a hobby project in beta. Expect sharp edges. These constraints apply:

### Trust boundary

- **Personal agent by default** — one trusted operator boundary.
- Bot can read files and run actions if tools are enabled.
- A bad prompt can trick it into doing unsafe things.
- OpenClaw is **not** a hostile multi-tenant boundary by default.
- If multiple users can message one tool-enabled agent, they **share** that delegated tool authority.

### Before running

- If you are not comfortable with security hardening and access control, do not run OpenClaw.
- Ask someone experienced before enabling tools or exposing it to the internet.

### Recommended baseline

| Control | Requirement |
|---------|-------------|
| Pairing/allowlists | Use pairing and mention gating |
| Multi-user/shared inbox | Split trust boundaries: separate gateway/credentials, ideally separate OS users/hosts |
| Sandbox | Use sandbox + least-privilege tools |
| Shared inboxes | Isolate DM sessions: `session.dmScope: per-channel-peer`; keep tool access minimal |
| Secrets | Keep secrets out of the agent's reachable filesystem |
| Model choice | Use the strongest available model for any bot with tools or untrusted inboxes |

## Regular audit commands

Run regularly (at least before each PR):

```bash
openclaw security audit --deep
openclaw security audit --fix
```

## Integration with existing skills

| Skill | Integration |
|-------|-------------|
| [quality-gate](../quality-gate/SKILL.md) | For OpenClaw repos: run `openclaw security audit --deep` and `openclaw security audit --fix` as mandatory checks before integration-commit. Report pass/fail in Quality Gate Results. |
| [integration-pr](../integration/integration-pr/SKILL.md) | PR checklist must include: security audit passed. Do not open PR until audit passes. |
| [integration-commit](../integration/integration-commit/SKILL.md) | Never commit without passing security audit when working on OpenClaw. |

## Output format

Include in Quality Gate Results when applicable:

```markdown
## OpenClaw Security Audit

- [x] openclaw security audit --deep — clean
- [x] openclaw security audit --fix — applied
```

If audit fails, list findings and remediation steps. Block commit/PR until resolved.

## Reference

Must read: https://docs.openclaw.ai/gateway/security
