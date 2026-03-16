---
name: operations
description: Monitors production; handles incidents; audits. Use when monitoring, responding to incidents, or performing audits. Sub-skills (13.1–13.3) available.
---

# Operations

Production monitoring, incident response, and audit per SKILL_TREE §13.

## When to use

- Monitoring logs, metrics, alerts
- Responding to incidents
- Performing compliance or security audits

## Sub-skills

| Sub-skill | Use when |
|-----------|----------|
| [operations-monitoring](operations-monitoring/SKILL.md) (13.1) | Post-deploy verification; investigating spikes; setting up observability |
| [operations-incident](operations-incident/SKILL.md) (13.2) | Service down/degraded; alert fires; post-incident report |
| [operations-audit](operations-audit/SKILL.md) (13.3) | Security review; quarterly hygiene; GDPR/HIPAA compliance check |

## Flow

1. **Monitoring** — Run [operations-monitoring](operations-monitoring/SKILL.md) after deploy; escalate to incident on anomaly
2. **Incident** — Run [operations-incident](operations-incident/SKILL.md) when alert fires; rollback via [deployment-release](../deployment/deployment-release/SKILL.md) if needed
3. **Audit** — Run [operations-audit](operations-audit/SKILL.md) before reviews or quarterly

## Integration

- Composes with [deployment](../deployment/SKILL.md).
- See [COOPERATION.md](../COOPERATION.md).
