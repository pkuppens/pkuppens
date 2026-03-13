---
name: operations-audit
description: Performs compliance, security, and performance audits of a service or codebase. Use when preparing for a security review, assessing technical debt, validating GDPR/HIPAA compliance posture, or running a performance baseline.
---

# Operations Audit

Structured audit covering security, compliance, performance, and data handling.

**When to use:**
- Before a client or regulatory review
- Quarterly security and dependency hygiene check
- Assessing technical debt and risk (feeds `architecture-risks-debt`)
- Validating GDPR/HIPAA compliance posture for healthcare/personal data systems

**Instructions:**

1. **Security audit**:
   - Dependency vulnerabilities: `uv run pip-audit` or `npm audit`
   - Secrets in code: `git log --all --oneline | head -50`; check for hardcoded keys
   - Authentication: verify all endpoints require auth where expected
   - OWASP Top 10: check for SQL injection, XSS, CSRF, broken auth, excessive data exposure

2. **Dependency audit**:
   - Outdated packages: `uv run pip list --outdated`
   - Deprecated APIs in use: search for known deprecation patterns
   - Transitive dependency conflicts: `uv tree`

3. **Performance audit**:
   - Identify slow endpoints from logs (P95 > 500ms)
   - Check for N+1 queries: look for loops with DB calls inside
   - Check index coverage for frequent queries
   - Memory baseline: measure container memory under typical load

4. **Data compliance (if applicable)**:
   - PII fields: are they encrypted at rest and in transit?
   - Retention policy: is stale data purged per policy?
   - Audit log: are sensitive operations logged with user identity and timestamp?
   - Data residency: is data stored in permitted regions?

5. **Code quality audit**:
   - Test coverage: `uv run pytest --cov` — flag modules below 60%
   - Lint/format: `uv run ruff check .` — count and categorise violations
   - Type coverage: `uv run pyright` or `mypy` — flag untyped public APIs

6. **Document findings** in `tmp/operations/audit-<date>.md`:
   - Findings by category (Critical / High / Medium / Low)
   - Recommended actions with effort estimate
   - Link to issues created for remediation

**Output format:**

```
## Audit Report — <date>
### Critical
- <finding>: <recommendation> (#NNN)

### High
- <finding>: <recommendation>

### Medium / Low
- <summary>

### Summary
- Findings: <C>/<H>/<M>/<L>
- Issues created: #NNN, #NNN
```

**Integration:** Findings feed `issue-workflow` (create issues) and `architecture-risks-debt`. See COOPERATION.md.
