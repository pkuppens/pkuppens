---
name: azure-devops
description: Orchestrates Azure DevOps work item, repo, and pipeline workflows using az CLI. Use when working with Azure DevOps, Azure Repos, Azure Boards, Azure Pipelines, or az devops commands.
---

# Azure DevOps Workflow

Orchestrates the Azure DevOps lifecycle for work items, pull requests, and pipelines. Mirrors the platform-agnostic discipline in [`docs/workflow/README.md`](../../docs/workflow/README.md).

## When to use

- Creating or refining Azure Boards work items (Epic, Feature, PBI, Task, Bug)
- Opening, reviewing, or completing pull requests in Azure Repos
- Authoring or validating Azure Pipelines YAML and branch policies
- Mapping repo workflow conventions to Azure DevOps tooling

## Prerequisites

```bash
az extension add --name azure-devops
az devops login --organization https://dev.azure.com/{org}
az devops configure --defaults organization=https://dev.azure.com/{org} project={project}
```

## Flow

1. **Work items** — [azure-devops-work-items](azure-devops-work-items/SKILL.md). Create, query, update, link work items.
2. **Branching** — Same git branch prefixes as the agnostic workflow (`feature/NNN-description`). Link commits with `AB#NNN` in messages.
3. **Pull requests** — [azure-devops-repos](azure-devops-repos/SKILL.md). Create PR, request reviewers, complete merge.
4. **Quality gate** — Local checks (lint, test, format) before push; build validation policy on the target branch.
5. **Pipelines** — [azure-devops-pipelines](azure-devops-pipelines/SKILL.md). CI validation on PR; staged deploy after merge.
6. **Cleanup** — Prune branches; delete old pipeline runs when repo conventions require it.

## Work item hierarchy

| Type | Role |
|------|------|
| Epic | Large initiative spanning multiple features |
| Feature | Deliverable slice under an epic |
| Product Backlog Item / User Story | User-facing requirement |
| Task | Implementation step |
| Bug | Defect (separate from feature hierarchy) |

## Output templates

Work item body (adapt fields to project process template):

```markdown
## Goal
[One sentence: what and why]

## Tasks
- [ ] ...

## Acceptance Criteria
- [ ] ... (copy-pastable validation steps)

## Out of Scope
- ...

## Estimate
Size: S | M | L
```

Pull request description:

```markdown
## Summary
[What and why]

## Changes
- ...

Related work: AB#NNN
```

## Integration

- Platform mapping: [`docs/workflow/azure-devops.md`](../../docs/workflow/azure-devops.md)
- Agnostic source of truth: [`docs/workflow/README.md`](../../docs/workflow/README.md)
- GitHub equivalent skills: [`issue-workflow`](../issue-workflow/SKILL.md), [`integration`](../integration/SKILL.md), [`deployment`](../deployment/SKILL.md)
