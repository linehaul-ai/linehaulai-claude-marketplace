---
name: pull
description: Fetch GitHub Project state and update ROADMAP.toml
allowed-tools:
  - Read
  - Edit
  - Bash
  - AskUserQuestion
---

# Pull from GitHub Projects

Fetch the current state from GitHub Projects and update `specs/ROADMAP.toml`.

## Prerequisites

- `gh` CLI installed and authenticated
- GitHub Project exists with items synced via `/roadmap:sync`

## Steps

1. Read `specs/ROADMAP.toml` to get:
   - Project name
   - Current items (for matching)

2. Fetch project items from GitHub:
   ```bash
   gh project item-list <PROJECT_NUMBER> --owner @me --format json
   ```

3. For each item in GitHub Project:

   a. Match to TOML item by title or label

   b. Get current status from project column:
      - "Todo" → `status = "pending"`
      - "In Progress" → `status = "in_progress"`
      - "Done" → `status = "done"`

   c. If item exists in TOML but status differs:
      - Update the status in TOML

   d. If item exists in GitHub but not in TOML:
      - Ask user: "Found new item in GitHub: '<title>'. Add to TOML?"
      - If yes, append to TOML with defaults:
        - `type = "task"`
        - `stack_layer = "backend"`
        - `priority = "P3"`
        - `start_date` = today's date

   e. If item exists in TOML but not in GitHub:
      - Warn user: "Item '<title>' not found in GitHub. Keep in TOML?"

4. Write updated TOML preserving formatting

5. Report changes:
   - Items updated (status changes)
   - Items added from GitHub
   - Items only in TOML (warnings)

## Notes

- TOML remains source of truth for descriptions, types, layers, and priorities
- Only status is pulled from GitHub by default
- New items from GitHub get defaults:
  - `type = "task"`
  - `stack_layer = "backend"`
  - `priority = "P3"` (lowest)
  - `start_date` = current date
