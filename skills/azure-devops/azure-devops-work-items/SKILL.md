---
name: azure-devops-work-items
description: Creates, queries, updates, and links Azure Boards work items via az boards CLI. Use when filing ADO work items, running WIQL queries, or setting area path, iteration, tags, and assignee.
---

# Azure DevOps Work Items

Manages Azure Boards work items with the same discipline as the agnostic issue workflow.

## When to use

- Creating a new Epic, Feature, PBI/User Story, Task, or Bug
- Searching for duplicates before starting work
- Updating metadata (area path, iteration, tags, assignee)
- Linking parent/child or related work items

## Create a work item

```bash
az boards work-item create \
  --title "[FEAT]: Add hybrid retrieval" \
  --type "Product Backlog Item" \
  --description "## Goal\n...\n\n## Acceptance Criteria\n- [ ] ..." \
  --fields "System.AssignedTo=user@example.com"
```

Common types vary by process template: `Epic`, `Feature`, `Product Backlog Item`, `User Story`, `Task`, `Bug`.

## View and update

```bash
az boards work-item show --id 12345
az boards work-item update --id 12345 --title "Updated title"
az boards work-item update --id 12345 --fields "System.Tags=ready-for-agent"
```

## Duplicate check (WIQL)

```bash
az boards query --wiql "SELECT [System.Id], [System.Title] FROM WorkItems \
  WHERE [System.TeamProject] = @project \
  AND [System.Title] CONTAINS 'hybrid retrieval' \
  AND [System.State] <> 'Removed' \
  ORDER BY [System.ChangedDate] DESC"
```

## Link work items

```bash
az boards work-item relation add --id 12345 \
  --relation-type parent \
  --target-id 12340
```

Relation types include `parent`, `child`, `related`, and `duplicate`.

## Commit linking

Include `AB#12345` in commit messages so Azure DevOps links commits to the work item automatically.

## Required sections

Every work item should include:

- **Goal** — one sentence outcome and why
- **Tasks** — numbered actionable steps
- **Acceptance Criteria** — testable checkboxes with validation steps
- **Out of Scope** — explicit exclusions
- **Estimate** — T-shirt size or hours

## Integration

- Orchestrator: [azure-devops](../SKILL.md)
- Agnostic discipline: [`docs/workflow/README.md`](../../../docs/workflow/README.md)
