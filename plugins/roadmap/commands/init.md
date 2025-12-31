---
name: init
description: Create initial specs/ROADMAP.toml with template structure
allowed-tools:
  - Write
  - Read
  - Bash
---

# Initialize Roadmap

Create a new `specs/ROADMAP.toml` file with the standard template structure.

## Steps

1. Check if `specs/ROADMAP.toml` already exists
   - If it exists, ask the user if they want to overwrite it
   - If they decline, exit gracefully

2. Create the `specs/` directory if it doesn't exist

3. Create `specs/ROADMAP.toml` with this template:

```toml
# Project Roadmap
# Managed by roadmap plugin - sync with GitHub Projects via /roadmap:sync

project = "laneweaverTMS_launch"

# Example item (remove or modify):
[[items]]
title = "Example Feature"
label = "example"
description = "Replace this with your first roadmap item"
type = "feature"          # bug | feature | task
stack_layer = "backend"   # backend | frontend | devops
priority = "P1"           # P0 | P1 | P3
status = "pending"        # pending | in_progress | done
start_date = "2024-01-15" # auto-filled when adding items
```

4. Confirm creation to the user and suggest next steps:
   - Edit the file to add real items
   - Use `/roadmap:add` to add items interactively
   - Use `/roadmap:sync` to push to GitHub Projects
