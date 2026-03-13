---
name: operations-incident
description: Triages, mitigates, and communicates production incidents; produces a post-incident timeline. Use when a service is degraded or down, when an alert fires, or when preparing an incident report.
---

# Operations Incident

Structured incident response: triage, mitigation, communication, and post-incident record.

**When to use:**
- Service is down or returning errors above threshold
- Alert fires (health check failure, error rate spike, latency regression)
- Preparing a post-incident report or timeline

**Instructions:**

1. **Triage** (within 5 minutes of alert):
   - Is the service down or degraded? Run `operations-monitoring` first.
   - Determine blast radius: which users/endpoints are affected?
   - Identify likely cause: recent deploy, dependency failure, data issue, infrastructure

2. **Mitigate immediately**:
   - Recent bad deploy → rollback: `deployment-release` rollback procedure
   - Dependency down → enable fallback or circuit breaker; update status page
   - Resource exhaustion → scale up or restart container: `docker restart <container>`
   - Data corruption → isolate affected data; do not overwrite until root cause known

3. **Communicate status**:
   - Update status page or team channel with: "Incident started at HH:MM. Investigating."
   - Give ETA for next update within 15 minutes
   - Escalate if mitigation not found within 30 minutes

4. **Root cause analysis**:
   - Trace error back to specific commit, config change, or external dependency
   - Reproduce in staging if possible
   - Identify contributing factors (missing tests, no canary deploy, etc.)

5. **Resolve and verify**:
   - Apply fix (or confirm rollback is stable)
   - Verify health endpoint and error rate back to baseline
   - Run `operations-monitoring` report to confirm

6. **Post-incident record** in `tmp/operations/incident-<date>-<slug>.md`:
   - Timeline: alert → triage → mitigation → resolution
   - Root cause
   - Impact (duration, users affected)
   - Action items to prevent recurrence (with issue links)

**Output format:**

```
## Incident Report — <slug>
- Status: resolved | ongoing
- Started: <timestamp>
- Resolved: <timestamp>
- Cause: <one sentence>
- Impact: <duration>, <scope>
- Mitigation: <what was done>
- Follow-up issues: #NNN, #NNN
```

**Integration:** Triggered by `operations-monitoring` anomalies. Post-incident action items feed back into `issue-workflow`. See COOPERATION.md.
