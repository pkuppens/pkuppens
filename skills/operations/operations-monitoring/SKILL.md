---
name: operations-monitoring
description: Monitors production logs, metrics, and alerts; detects anomalies; surfaces health status. Use when reviewing production health, investigating a spike in errors or latency, setting up observability for a new service, or verifying post-deploy stability.
---

# Operations Monitoring

Provides structured observability of production systems: logs, metrics, alerts, and health.

**When to use:**
- After a deployment, to verify stability
- When error rates or latency spike above baseline
- When setting up observability for a new service or endpoint
- During on-call investigation of a production issue

**Instructions:**

1. **Identify observability signals** available in the repo:
   - Logs: `docker logs`, structured JSON logs, cloud provider log viewer
   - Metrics: Prometheus `/metrics`, uptime checks, response time histograms
   - Alerts: GitHub Actions scheduled checks, uptime monitors (UptimeRobot, Better Uptime)
   - Health endpoint: `GET /health` returning `{"status": "ok", "version": "..."}`

2. **Check health** (always first):
   ```bash
   curl -sf https://<host>/health | jq .
   ```
   Expected: `{"status": "ok"}` with HTTP 200.

3. **Review recent logs** for errors and warnings:
   ```bash
   docker logs --since 15m <container> | grep -E "ERROR|WARN|Exception"
   ```
   Flag: repeated error patterns, stack traces, connection timeouts.

4. **Check key metrics**:
   - Request rate: compare to baseline (same time yesterday)
   - Error rate: target <1% of requests
   - P95 response time: target <500ms for API endpoints
   - Memory/CPU: flag if container uses >80% of limit

5. **Anomaly detection**:
   - Sudden spike in 5xx responses → likely deploy regression or dependency failure
   - Memory growth without plateau → memory leak
   - Latency spike on one endpoint → N+1 query or missing index

6. **Document findings** in `tmp/operations/monitoring-<date>.md`:
   - Health status
   - Error count and patterns
   - Metric deviations from baseline
   - Action items (if any)

**Output format:**

```
## Monitoring Report — <date>
- Health: ✅ OK / ⚠️ degraded / ❌ down
- Error rate: <value>% (baseline: <value>%)
- P95 latency: <value>ms (baseline: <value>ms)
- Notable patterns: <list>
- Action items: <list or "none">
```

**Integration:** Triggered after `deployment-release`. Feeds `operations-incident` if anomalies found. See COOPERATION.md.
