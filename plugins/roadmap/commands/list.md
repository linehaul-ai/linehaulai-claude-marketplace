---
name: list
description: Display current roadmap status in a formatted table
allowed-tools:
  - Read
---

# List Roadmap

Display the current roadmap from `specs/ROADMAP.toml` in a readable format.

## Steps

1. Read `specs/ROADMAP.toml`
   - If file doesn't exist, inform user and suggest `/roadmap:init`

2. Parse the TOML content and extract:
   - Project name
   - All items with their fields

3. Display in a formatted table, grouped by status:

```
📋 Roadmap: laneweaverTMS_launch

🔴 Pending (3 items)
┌────┬─────────────────────┬──────────┬──────────┬──────────┬────────────┬─────────────────────────────┐
│ P  │ Title               │ Type     │ Layer    │ Label    │ Started    │ Description                 │
├────┼─────────────────────┼──────────┼──────────┼──────────┼────────────┼─────────────────────────────┤
│ P0 │ User Authentication │ feature  │ backend  │ auth     │ 2024-01-15 │ OAuth login with providers  │
│ P1 │ Carrier Onboarding  │ feature  │ backend  │ carrier  │ 2024-01-16 │ MCP integration for...      │
│ P3 │ UI Polish           │ task     │ frontend │ ui-fix   │ 2024-01-17 │ Minor styling adjustments   │
└────┴─────────────────────┴──────────┴──────────┴──────────┴────────────┴─────────────────────────────┘

🟡 In Progress (1 item)
...

🟢 Done (2 items)
...

Summary: 3 pending, 1 in progress, 2 done (6 total)
By Layer: 2 backend, 1 frontend, 0 devops
By Type: 2 features, 0 bugs, 1 task
```

4. If items exist, mention sync status:
   - "Run `/roadmap:sync` to push changes to GitHub Projects"
