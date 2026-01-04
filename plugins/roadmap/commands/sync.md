---
name: sync
description: Push roadmap items to GitHub Projects via gh CLI
allowed-tools:
  - Read
  - Bash
  - AskUserQuestion
---

# Sync Roadmap to GitHub

Push `specs/ROADMAP.toml` items to GitHub Projects using the `gh` CLI.

## Prerequisites

- `gh` CLI installed and authenticated
- GitHub Project exists (specified in TOML `project` field)

## Steps

1. Read `specs/ROADMAP.toml` and parse items
   - If file doesn't exist, suggest `/roadmap:init`

2. Get the project name from TOML header (`project = "..."`)
   - If not set, ask user for project name

3. Verify `gh` CLI is available:
   ```bash
   gh --version
   ```

4. Get the GitHub Project ID:
   ```bash
   gh project list --owner @me --format json
   ```
   - Find the project matching the name
   - If not found, inform user and exit

5. For each item in the roadmap:

   a. Check if item already exists in project (by title):
   ```bash
   gh project item-list <PROJECT_NUMBER> --owner @me --format json
   ```

   b. If item exists, update it:
   ```bash
   gh project item-edit --project-id <PROJECT_ID> --id <ITEM_ID> --field-id <STATUS_FIELD_ID> --single-select-option-id <STATUS_OPTION_ID>
   ```

   c. If item doesn't exist, create it as a draft issue:
   ```bash
   gh project item-create <PROJECT_NUMBER> --owner @me --title "<TITLE>" --body "<DESCRIPTION>"
   ```

6. Map status values:
   - `pending` → Project "Todo" column
   - `in_progress` → Project "In Progress" column
   - `done` → Project "Done" column

7. Map custom fields if the project has them configured:
   - `type` → "Type" field (Bug, Feature, Task)
   - `stack_layer` → "Stack Layer" field (Backend, Frontend, Devops)
   - `priority` → "Priority" field (P0, P1, P3)
   - `start_date` → "Start Date" field

8. Report sync results:
   - Items created
   - Items updated
   - Any errors encountered

## Notes

- Uses draft issues (not repo issues) for roadmap items
- If custom fields don't exist in GitHub Project, include them in the item body:
  ```
  **Type:** feature | **Layer:** backend | **Priority:** P1 | **Started:** 2024-01-15
  ```
- Label is used to identify items for updates
