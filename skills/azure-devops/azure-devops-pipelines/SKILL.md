---
name: azure-devops-pipelines
description: Guides Azure Pipelines YAML structure, build validation on PRs, and staged deployment with environments and approvals. Use when authoring azure-pipelines.yml or configuring CI/CD on Azure DevOps.
---

# Azure DevOps Pipelines

Defines CI/CD patterns for Azure Pipelines aligned with the agnostic workflow.

## When to use

- Authoring or updating `azure-pipelines.yml`
- Configuring build validation on pull requests
- Setting up staged deployment (staging → production) with approvals
- Cleaning up old pipeline runs

## CI/CD principles

1. **Validation on PR** — lint, test, type check, security scan run when a PR is created or updated.
2. **Deploy after merge** — staging deploy triggers on merge to `main`; production requires approval.
3. **Rollback** — previous artefact tag or release can be redeployed if smoke tests fail.
4. **Evidence** — record pipeline run URL and smoke test outcome before claiming release success.

## Minimal validation pipeline

```yaml
trigger:
  branches:
    include:
      - main

pr:
  branches:
    include:
      - main

pool:
  vmImage: ubuntu-latest

stages:
  - stage: Validate
    jobs:
      - job: QualityGate
        steps:
          - checkout: self
          - task: UsePythonVersion@0
            inputs:
              versionSpec: "3.12"
          - script: |
              pip install uv
              uv sync --group dev
              uv run ruff check .
              uv run pytest
            displayName: Lint and test
```

## Staged deployment with environments

```yaml
  - stage: DeployStaging
    dependsOn: Validate
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: Staging
        environment: staging
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploy to staging"
                  displayName: Deploy staging

  - stage: DeployProduction
    dependsOn: DeployStaging
    jobs:
      - deployment: Production
        environment: production   # configure approval check in ADO UI
        strategy:
          runOnce:
            deploy:
              steps:
                - script: echo "Deploy to production"
                  displayName: Deploy production
```

## Build validation policy

Link a pipeline to a branch policy so PRs cannot merge until the build succeeds. See [azure-devops-repos](../azure-devops-repos/SKILL.md) for `az repos policy build create`.

## Service connections

Store credentials (container registry, cloud subscription, package feed) as service connections in Project Settings → Service connections. Reference them in YAML:

```yaml
- task: Docker@2
  inputs:
    containerRegistry: my-acr-connection
    command: buildAndPush
```

## Pipeline run cleanup

```bash
az pipelines runs list --pipeline-ids 12 --top 50
az pipelines runs delete --id 98765
```

Delete failed or stale runs periodically to reduce noise.

## Integration

- Orchestrator: [azure-devops](../SKILL.md)
- Release checklist patterns: [deployment-release](../../deployment/deployment-release/SKILL.md) (adapt commands to ADO tasks)
- Agnostic discipline: [`docs/workflow/README.md`](../../../docs/workflow/README.md)
