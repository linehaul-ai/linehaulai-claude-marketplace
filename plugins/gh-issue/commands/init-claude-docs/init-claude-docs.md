---
description: Generate tailored CLAUDE.md files for each directory in the monorepo
model: sonnet
---

# Initialize Claude Documentation

Generate CLAUDE.md files tailored to each directory in this monorepo by analyzing existing code patterns.

## Parameters

- `$ARGUMENTS` - Optional: Specify which directory to generate (e.g., "root", "frontend", "backend", "supabase"). If omitted, generates all CLAUDE.md files.

## Target Directories

| Directory | Technology | Purpose |
|-----------|------------|---------|
| `./` (root) | Project overview | High-level architecture, cross-cutting concerns |
| `./laneweaver-frontend/` | Svelte 5 + SvelteKit | Frontend best practices |
| `./cmd/` + `./internal/` | Go + Echo | Backend best practices |
| `./supabase/` | PostgreSQL | Database migrations and SQL |

## Workflow

### Step 1: Analyze Target Directory

For each target directory, perform deep analysis:

1. **Scan file structure** - Identify key files, patterns, and organization
2. **Extract conventions** - Naming patterns, import structures, code style
3. **Identify patterns** - Architecture patterns, common abstractions
4. **Find examples** - Exemplary files that demonstrate best practices

### Step 2: Generate CLAUDE.md Content

Each CLAUDE.md should include:

```markdown
# [Directory Name] Guidelines

## Overview
Brief description of this directory's purpose and role in the project.

## Architecture
Key architectural patterns and directory structure.

## Conventions
- Naming conventions
- File organization
- Import patterns

## Best Practices
Technology-specific best practices extracted from existing code.

## Common Patterns
Reusable patterns found in this codebase with examples.

## Testing
Testing conventions and patterns.

## Do's and Don'ts
Specific guidance based on codebase analysis.
```

### Step 3: Write Files

Write each CLAUDE.md to its target directory.

## Analysis Guidelines by Technology

### Root Project (`./CLAUDE.md`)

Analyze:
- `go.mod` for dependencies and module structure
- `.mcp.json` for MCP configuration
- Directory structure for overall architecture
- Integration patterns between frontend/backend/database

Include:
- Project purpose and tech stack overview
- How services communicate
- Development workflow
- Environment setup

### Svelte 5 Frontend (`./laneweaver-frontend/CLAUDE.md`)

Analyze:
- `src/` directory structure
- Component patterns in `src/lib/` or `src/components/`
- Route structure in `src/routes/`
- State management patterns
- `svelte.config.js` and `vite.config.ts` for build configuration

Reference: `references/svelte5-patterns.md`

Include:
- Svelte 5 runes syntax (`$state`, `$derived`, `$effect`)
- Component composition patterns
- SvelteKit routing conventions
- Styling approach
- State management patterns used

### Go Backend (`./cmd/CLAUDE.md` or `./internal/CLAUDE.md`)

Analyze:
- `internal/` package structure
- Handler patterns in `internal/handlers/`
- Service layer in `internal/services/`
- Repository pattern in `internal/repository/`
- Model definitions in `internal/models/`
- Router setup in `internal/router/`

Reference: `references/go-echo-patterns.md`

Include:
- Echo framework patterns
- Handler → Service → Repository flow
- Error handling patterns
- Database interaction patterns
- Middleware usage

### Supabase/PostgreSQL (`./supabase/CLAUDE.md`)

Analyze:
- `migrations/` for schema patterns
- `seed.sql` for data patterns
- `config.toml` for configuration

Reference: `references/postgres-patterns.md`

Include:
- Migration naming conventions
- SQL style guide
- RLS policy patterns
- Common query patterns
- Index strategies

## Execution Steps

1. Use TodoWrite to create a task list for each directory
2. For each directory:
   a. Read reference file if available
   b. Scan and analyze code patterns
   c. Extract conventions and best practices
   d. Generate CLAUDE.md content
   e. Write the file
3. Summarize what was created

## Examples

```bash
# Generate all CLAUDE.md files
/init-claude-docs

# Generate only frontend documentation
/init-claude-docs frontend

# Generate only backend documentation
/init-claude-docs backend

# Generate only root project overview
/init-claude-docs root
```
