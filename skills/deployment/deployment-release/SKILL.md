---
name: deployment-release
description: Releases validated artefacts to staging or production; runs smoke tests; triggers rollback on failure. Use when deploying a new version to an environment, updating infrastructure, or executing a release checklist.
---

# Deployment Release

Deploys validated artefacts to target environments and verifies successful rollout.

**When to use:**
- Deploying a new version to staging or production
- Executing a release checklist after `deployment-build` passes
- Updating infrastructure (Compose stack, Kubernetes manifests, cloud service)
- When rollback criteria must be defined before release

**Pre-conditions:**
- `deployment-build` completed and artefact digest recorded
- `quality-gate` passed (lint, tests, type check)
- `integration-merge` completed (main branch up to date)

**Instructions:**

1. **Define rollback criteria** before deploying:
   - Smoke test failure threshold
   - Error rate spike above baseline
   - Response time regression >20%

2. **Deploy to staging first** (if applicable):
   - Docker Compose: `docker compose pull && docker compose up -d`
   - Cloud (fly.io, Railway, Render): `fly deploy` / push to deploy branch
   - Kubernetes: `kubectl set image deployment/<name> <container>=<image>:<tag>`

3. **Run smoke tests** against staging:
   - Health endpoint: `curl -f https://<host>/health`
   - Key API endpoint: expected status 200 + non-empty response
   - Document results in `tmp/deployment/smoke-<version>.md`

4. **Promote to production** (after staging passes):
   - Repeat deploy command targeting production environment
   - Monitor logs for 5 minutes post-deploy: `docker logs -f <container>` / `fly logs`

5. **Verify rollout**:
   - Check health endpoint on production
   - Confirm version header or `/version` endpoint matches expected tag
   - Check error rate in monitoring dashboard

6. **On failure — rollback**:
   - Container: `docker compose down && docker compose up -d --scale <service>=0` then redeploy previous tag
   - Cloud: `fly releases rollback <previous-version>`
   - Document incident in `tmp/deployment/incident-<version>.md`

7. **Update release record** in `tmp/deployment/release-<version>.md`:
   - Deployed version, environment, timestamp
   - Smoke test results
   - Rollback decision (if any)

**Output format:**

```
## Release Summary
- Version: <tag>
- Environment: staging | production
- Deploy time: <timestamp>
- Smoke tests: ✅ passed / ❌ failed
- Rollback triggered: yes | no
- Notes: <any issues>
```

**Integration:** Follows `deployment-build`. Composes with `operations-monitoring` post-deploy. See COOPERATION.md.
