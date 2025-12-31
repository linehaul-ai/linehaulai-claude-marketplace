# Roadmap Plugin

Project roadmap management with GitHub Projects integration.

## Overview

Manage your project roadmap in a `specs/ROADMAP.toml` file and sync it with GitHub Projects. Uses a spec-driven approach where the roadmap serves as the ultimate "to-do list" for development.

## Features

- **TOML-based roadmap**: Simple, version-controlled roadmap format
- **GitHub Projects sync**: Push roadmap items to GitHub Projects via `gh` CLI
- **Pull from GitHub**: Fetch status updates from GitHub back to TOML
- **Rich metadata**: Track type (bug/feature/task), stack layer (backend/frontend/devops), priority (P0/P1/P3), and start dates

## Commands

| Command | Description |
|---------|-------------|
| `/roadmap:init` | Create initial `specs/ROADMAP.toml` |
| `/roadmap:add` | Add a new item to the roadmap |
| `/roadmap:list` | Display current roadmap status |
| `/roadmap:sync` | Push roadmap to GitHub Projects |
| `/roadmap:pull` | Fetch GitHub state into TOML |

## Agent

| Agent | Description |
|-------|-------------|
| `roadmap-planner` | Helps brainstorm and structure your roadmap |

## TOML Format

```toml
project = "your-project-name"

[[items]]
title = "Feature Name"
label = "feature-label"
description = "What this feature does"
type = "feature"          # bug | feature | task
stack_layer = "backend"   # backend | frontend | devops
priority = "P1"           # P0 (critical) | P1 (high) | P3 (low)
status = "pending"        # pending | in_progress | done
start_date = "2024-01-15" # auto-filled when using /roadmap:add
```

### Field Reference

| Field | Values | Description |
|-------|--------|-------------|
| `type` | `bug`, `feature`, `task` | Type of work item |
| `stack_layer` | `backend`, `frontend`, `devops` | Which part of the stack |
| `priority` | `P0`, `P1`, `P3` | P0 = critical, P1 = high, P3 = low |
| `status` | `pending`, `in_progress`, `done` | Current status |
| `start_date` | `YYYY-MM-DD` | Auto-set to today when adding |

## Prerequisites

- `gh` CLI installed and authenticated
- GitHub Project created (e.g., using PRODUCT LAUNCH template)
- Project scope for gh CLI: `gh auth refresh -s read:project`

## Installation

From the linehaulai-claude-marketplace:

```bash
/plugin install roadmap@linehaulai-claude-marketplace
```

Or for local development:

```bash
claude --plugin-dir /path/to/plugins/roadmap
```
