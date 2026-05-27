# GitHub Workflow Mapping (Platform-Specific)

This guide maps the platform-agnostic workflow in [`docs/workflow/README.md`](README.md) to concrete GitHub conventions and commands used in this repository.

When in doubt, follow the agnostic workflow, then apply the matching GitHub tool examples below.

---

## Mapping: platform-agnostic areas to GitHub specifics

| Workflow area | GitHub tool | Existing skill(s) |
|---|---|---|
| Issue discipline | `gh issue create/view/edit` | [`issue-workflow`](../../skills/issue-workflow/SKILL.md) |
| Duplicate check | `gh issue list` + search | [`issue-check-duplicates`](../../skills/issue-workflow/issue-check-duplicates/SKILL.md) |
| Metadata | labels, milestones, `--assignee @me` | [`issue-metadata`](../../skills/issue-workflow/issue-metadata/SKILL.md) |
| Bulk creation | `gh issue create` in a loop | [`issue-gh-bulk-scratch`](../../skills/issue-workflow/issue-gh-bulk-scratch/SKILL.md) |
| Branching | `git checkout -b feature/NNN-...` | [`plan-branch-strategy`](../../skills/plan-branch-strategy/SKILL.md) |
| Commit linking | `#NNN` in commit message | [`integration-commit`](../../skills/integration/integration-commit/SKILL.md) |
| PR creation | `gh pr create --assignee @me` | [`integration-pr`](../../skills/integration/integration-pr/SKILL.md) |
| PR merge | `gh pr merge --squash --delete-branch` | [`integration-merge`](../../skills/integration/integration-merge/SKILL.md) |
| Code review | PR review workflow on GitHub | [`code-review`](../../skills/code-review/SKILL.md) |
| Quality gate | pre-commit + GitHub Actions checks | [`quality-gate`](../../skills/quality-gate/SKILL.md) |
| CI/CD | `.github/workflows/` validations + deploy steps | [`deployment`](../../skills/deployment/SKILL.md) + [`deployment-release`](../../skills/deployment/deployment-release/SKILL.md) |
| Cleanup | `gh run delete`, branch pruning | [`maintenance-cleanup`](../../skills/maintenance/maintenance-cleanup/SKILL.md), [`branch-cleanup-after-pr`](../../skills/branch-cleanup-after-pr/SKILL.md) |
| Monitoring | Actions logs as evidence | [`operations-monitoring`](../../skills/operations/operations-monitoring/SKILL.md) |

---

## Issue lifecycle (GitHub commands)

### Create / view / edit an issue

- Create:

```bash
gh issue create \
  --title "[FEAT]: verb + object #NNN" \
  --body "## Goal\n...\n\n## Acceptance Criteria\n- [ ] ...\n"
```

- View:

```bash
gh issue view NNN
```

- Edit (example: add assignee / update body):

```bash
gh issue edit NNN --add-assignee @me
```

### Duplicate check

Use a targeted list/search before implementing anything new:

```bash
gh issue list --state open --search "\"[FEAT]\" label:enhancement"
gh issue list --state closed --search "duplicate query terms"
```

This aligns with [`issue-check-duplicates`](../../skills/issue-workflow/issue-check-duplicates/SKILL.md).

---

## Branching and commits

### Branch per issue

Use the issue number prefix so later automation can link work:

```bash
git checkout -b feature/NNN-short-description
```

This aligns with [`plan-branch-strategy`](../../skills/plan-branch-strategy/SKILL.md).

### Commit messages link back to issues

Every commit should include `#NNN` so history remains navigable:

```text
#123: feat: add workflow docs
```

This aligns with [`integration-commit`](../../skills/integration/integration-commit/SKILL.md).

---

## Pull requests and merge flow

### Create PR

```bash
gh pr create --assignee @me --title "feat: ..." --body "Summary...\n\nCloses #NNN"
```

This aligns with [`integration-pr`](../../skills/integration/integration-pr/SKILL.md).

### Code review

Use the PR review checklist defined in [`code-review`](../../skills/code-review/SKILL.md). When review reveals risk or missing acceptance coverage, ensure the PR is blocked until addressed.

### Merge PR

```bash
gh pr merge --squash --delete-branch
```

This aligns with [`integration-merge`](../../skills/integration/integration-merge/SKILL.md).

---

## Quality gate and CI/CD on GitHub

### Quality gate sequence

The agnostic workflow says: “run checks before claiming done”. On GitHub, this typically means:

1. Local: pre-commit (lint/format/etc.)
2. PR: GitHub Actions checks
3. Evidence: record what ran and what passed

This aligns with [`quality-gate`](../../skills/quality-gate/SKILL.md).

### CI/CD documentation pattern

Use a `CI/CD expectations` table in project docs (e.g. root `CLAUDE.md`) so the review can verify that the repository actually runs what it claims.

Even without a specialised CI-orchestration skill, the same expectations table helps reviewers check that CI/CD behavior matches the project contract.

---

## Post-merge cleanup and monitoring

### Cleanup

After merge:

- prune local branches (`git fetch --prune` + delete merged branches)
- clean CI run history as appropriate

The skills to follow are [`maintenance-cleanup`](../../skills/maintenance/maintenance-cleanup/SKILL.md) and [`branch-cleanup-after-pr`](../../skills/branch-cleanup-after-pr/SKILL.md).

Example run cleanup pattern:

```bash
gh run list --state completed --limit 100
gh run delete <run-id>
```

### Monitoring evidence

Monitoring is done by reviewing Actions logs and status, then escalating to incident handling when needed. See [`operations-monitoring`](../../skills/operations/operations-monitoring/SKILL.md).

---

## Human-in-the-loop pause (when using agents)

The workflow can include an optional maintainer pause before coding. The default guidance is:

From [`skills/COOPERATION.md`](../../skills/COOPERATION.md):

```text
Human-in-the-loop pause: After `issue-workflow` and `plan`, a maintainer may review the issue before coding.
Invoke issue-coding only after that review, or when the issue has execution:ai-ok and an explicit go-ahead.
```
