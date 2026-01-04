---
name: add
description: Add a new item to the roadmap interactively
allowed-tools:
  - Read
  - Edit
  - AskUserQuestion
---

# Add Roadmap Item

Interactively add a new item to `specs/ROADMAP.toml`.

## Steps

1. Read `specs/ROADMAP.toml` to understand current items
   - If file doesn't exist, suggest running `/roadmap:init` first

2. Ask the user for item details using AskUserQuestion:
   - **Title**: What is this feature/task called?
   - **Label**: Short identifier (kebab-case, e.g., "user-auth", "billing-v2")
   - **Description**: Brief description of what this accomplishes
   - **Type**: bug | feature | task
   - **Stack Layer**: backend | frontend | devops
   - **Priority**: P0 (critical) | P1 (high) | P3 (low)
   - **Status**: Default to "pending" unless specified

3. Auto-generate today's date for `start_date` using the current date (YYYY-MM-DD format)

4. Append the new item to the TOML file:

```toml
[[items]]
title = "User provided title"
label = "user-provided-label"
description = "User provided description"
type = "feature"
stack_layer = "backend"
priority = "P1"
status = "pending"
start_date = "2024-01-15"
```

5. Confirm the item was added and show the updated item count

## Notes

- Labels should be unique and kebab-case
- `start_date` is always auto-filled with today's date (YYYY-MM-DD)
- Valid types: `bug`, `feature`, `task`
- Valid stack layers: `backend`, `frontend`, `devops`
- Valid priorities: `P0` (critical), `P1` (high), `P3` (low)
- Keep descriptions concise but meaningful
