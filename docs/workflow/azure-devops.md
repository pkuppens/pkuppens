# Azure DevOps Workflow Mapping (Platform-Specific)

This guide maps the platform-agnostic workflow in [`docs/workflow/README.md`](README.md) to Azure DevOps conventions and `az` CLI commands.

When in doubt, follow the agnostic workflow first, then apply the matching Azure DevOps tool examples below.

---

## Mapping: platform-agnostic areas to Azure DevOps specifics

| Workflow area | Azure DevOps tool | Skill(s) |
|---|---|---|
| Work item discipline | `az boards work-item create/show/update` | [`azure-devops`](../../skills/azure-devops/SKILL.md), [`azure-devops-work-items`](../../skills/azure-devops/azure-devops-work-items/SKILL.md) |
| Duplicate check | WIQL via `az boards query` | [`azure-devops-work-items`](../../skills/azure-devops/azure-devops-work-items/SKILL.md) |
| Metadata | Area Path, Iteration, Tags, Assignee | [`azure-devops-work-items`](../../skills/azure-devops/azure-devops-work-items/SKILL.md) |
| Bulk creation | `az boards work-item create` in a loop | [`azure-devops-work-items`](../../skills/azure-devops/azure-devops-work-items/SKILL.md) |
| Branching | `git checkout -b feature/NNN-...` + branch policies | [`plan-branch-strategy`](../../skills/plan-branch-strategy/SKILL.md), [`azure-devops-repos`](../../skills/azure-devops/azure-devops-repos/SKILL.md) |
| Commit linking | `AB#NNN` in commit message | git (auto-links in Azure DevOps) |
| PR creation | `az repos pr create` | [`azure-devops-repos`](../../skills/azure-devops/azure-devops-repos/SKILL.md) |
| PR merge | `az repos pr update --status completed` | [`azure-devops-repos`](../../skills/azure-devops/azure-devops-repos/SKILL.md) |
| Code review | Required reviewers, vote on PR | [`code-review`](../../skills/code-review/SKILL.md), [`azure-devops-repos`](../../skills/azure-devops/azure-devops-repos/SKILL.md) |
| Quality gate | pre-commit + build validation policy | [`quality-gate`](../../skills/quality-gate/SKILL.md) |
| CI/CD | `azure-pipelines.yml` (stages, environments) | [`azure-devops-pipelines`](../../skills/azure-devops/azure-devops-pipelines/SKILL.md), [`deployment`](../../skills/deployment/SKILL.md) |
| Cleanup | `az pipelines runs delete`, branch prune | [`maintenance-cleanup`](../../skills/maintenance/maintenance-cleanup/SKILL.md) |
| Monitoring | Azure Monitor, Application Insights, pipeline logs | [`operations-monitoring`](../../skills/operations/operations-monitoring/SKILL.md) |

---

## Setup

```bash
az extension add --name azure-devops
az devops login --organization https://dev.azure.com/{org}
az devops configure --defaults organization=https://dev.azure.com/{org} project={project}
```

---

## Work item lifecycle

### Create a work item

```bash
az boards work-item create \
  --title "[FEAT]: verb + object" \
  --type "Product Backlog Item" \
  --description "## Goal\n...\n\n## Acceptance Criteria\n- [ ] ..."
```

### Query for duplicates

```bash
az boards query --wiql "SELECT [System.Id], [System.Title] FROM WorkItems \
  WHERE [System.TeamProject] = @project AND [System.Title] CONTAINS 'search terms'"
```

### Update metadata

```bash
az boards work-item update --id 12345 \
  --fields "System.AssignedTo=user@example.com System.IterationPath=Project\\Sprint 1"
```

---

## Branching and commits

Use the same branch prefixes as the agnostic workflow (`feature/NNN-description`, etc.).

Link commits to work items:

```text
AB#12345: feat: add hybrid retrieval
```

---

## Pull requests

### Create PR

```bash
az repos pr create \
  --source-branch feature/123-short-description \
  --target-branch main \
  --title "feat: ..." \
  --description "## Summary\n...\n\nRelated work: AB#123"
```

### Complete PR (merge)

```bash
az repos pr update --id 42 --status completed --delete-source-branch true
```

---

## Quality gate and CI/CD

### Local quality gate

Run lint, format, and tests locally before push (same sequence as the agnostic workflow). See [`quality-gate`](../../skills/quality-gate/SKILL.md).

### Pipeline validation on PR

Configure a build validation branch policy so the PR pipeline must pass before merge. Example pipeline skeleton:

```yaml
pr:
  branches:
    include:
      - main

stages:
  - stage: Validate
    jobs:
      - job: QualityGate
        pool:
          vmImage: ubuntu-latest
        steps:
          - checkout: self
          - script: uv run pytest
            displayName: Run tests
```

Full patterns: [`azure-devops-pipelines`](../../skills/azure-devops/azure-devops-pipelines/SKILL.md).

### Staged deployment

Use pipeline **environments** with approval checks for production promotion after staging smoke tests pass.

---

## Post-merge cleanup

- Delete merged source branches (`az repos pr update --delete-source-branch true` on complete, or manual git prune)
- Remove stale pipeline runs: `az pipelines runs delete --id <run-id>`

See [`maintenance-cleanup`](../../skills/maintenance/maintenance-cleanup/SKILL.md) for hygiene patterns.

---

## Human-in-the-loop pause (when using agents)

From [`skills/COOPERATION.md`](../../skills/COOPERATION.md):

After work item refinement and planning, a maintainer may review before coding. Invoke implementation only when the work item has `execution:ai-ok` and an explicit go-ahead.

---

## Related docs

- Agnostic source of truth: [`README.md`](README.md)
- GitHub mapping: [`github.md`](github.md)
- Skill orchestrator: [`azure-devops`](../../skills/azure-devops/SKILL.md)
