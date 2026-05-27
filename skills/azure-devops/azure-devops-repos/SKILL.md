---
name: azure-devops-repos
description: Creates, reviews, and completes Azure Repos pull requests and branch policies via az repos CLI. Use when opening ADO PRs, setting required reviewers, or configuring build validation policies.
---

# Azure DevOps Repos

Manages Azure Repos pull requests and branch policies.

## When to use

- Creating a pull request after local quality gates pass
- Requesting reviewers and recording review votes
- Completing (merging) a PR with squash or merge commit
- Configuring branch policies on `main` or release branches

## Branch naming

Use the same prefixes as the agnostic workflow:

- `feature/NNN-short-description`
- `hotfix/NNN-short-description`
- `chore/NNN-short-description`

Link every commit to a work item with `AB#NNN` in the message.

## Create a pull request

```bash
az repos pr create \
  --source-branch feature/123-hybrid-retrieval \
  --target-branch main \
  --title "feat: add hybrid retrieval" \
  --description "## Summary\n...\n\nRelated work: AB#123"
```

## List and view PRs

```bash
az repos pr list --status active
az repos pr show --id 42
```

## Request reviewers

```bash
az repos pr reviewer add --id 42 --reviewers user@example.com
```

Reviewers vote: `approve`, `approve-with-suggestions`, `wait-for-author`, or `reject`.

## Complete (merge) a PR

```bash
az repos pr update --id 42 --status completed --delete-source-branch true
```

Use `--squash true` when the team prefers a single commit on the target branch.

## Branch policies

Typical policies on `main`:

| Policy | Purpose |
|--------|---------|
| Required reviewers | At least one approval before merge |
| Build validation | Azure Pipeline must succeed on the PR |
| Comment resolution | All PR comments resolved |

```bash
az repos policy list --branch main
az repos policy build create \
  --branch main \
  --build-definition-id 12 \
  --display-name "CI validation" \
  --enabled true \
  --blocking true
```

## PR description template

```markdown
## Summary
[What and why]

## Changes
- ...

## Validation evidence
- [ ] Lint passed locally
- [ ] Tests passed locally
- [ ] Pipeline green on PR

Related work: AB#NNN
```

## Integration

- Orchestrator: [azure-devops](../SKILL.md)
- Agnostic discipline: [`docs/workflow/README.md`](../../../docs/workflow/README.md)
