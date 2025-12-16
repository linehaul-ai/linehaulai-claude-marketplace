# Fix Supabase Plugin Manifest Error

## Problem

The supabase plugin has an invalid `plugin.json` manifest with validation errors:
- `agents: Invalid input` - Not a valid plugin.json field
- `skills: Invalid input` - Not a valid plugin.json field
- `Unrecognized key(s) in object: 'categories'` - Not a valid plugin.json field

## Root Cause

The current `plugin.json` declares `skills`, `agents`, and `categories` fields that don't exist in the Claude Code plugin.json schema. Skills and agents are **auto-discovered** from directory structure, not declared in the manifest.

## Valid plugin.json Fields

According to the official documentation, plugin.json only supports:
- `name` (required)
- `version` (required)
- `description` (required)
- `author` (object with `name`, optional `email`, `url`)
- `homepage` (optional)
- `repository` (optional)
- `license` (optional)
- `keywords` (optional array)
- `mcpServers` (optional object)
- `hooks` (optional object for embedded hooks)

**NOT SUPPORTED:** `skills`, `agents`, `categories`

## Implementation Plan

### Task 1: Fix the supabase plugin.json manifest

**File:** `.claude-plugin/supabase/.claude-plugin/plugin.json`

**Current (invalid):**
```json
{
  "name": "supabase",
  "version": "1.0.0",
  "description": "...",
  "keywords": [...],
  "categories": ["database", "security", "backend"],  // INVALID
  "skills": [...]  // INVALID - auto-discovered
  "agents": [...]  // INVALID - auto-discovered
}
```

**Fix to (valid):**
```json
{
  "name": "supabase",
  "version": "1.0.0",
  "description": "PostgreSQL and Supabase expertise for database design, schema architecture, and row-level security policies. Includes PostgreSQL table design best practices and Supabase RLS policy guidance.",
  "author": {
    "name": "fakebizprez",
    "email": "anthony@linehaul.ai"
  },
  "keywords": ["supabase", "postgresql", "database", "rls", "row-level-security", "schema-design", "postgres"]
}
```

**Changes:**
1. Remove `categories` field (not supported)
2. Remove `skills` array (auto-discovered from `skills/` directory)
3. Remove `agents` array (auto-discovered from `agents/` directory)
4. Add `author` field (best practice, matches other plugins)

### Task 2: Verify directory structure supports auto-discovery

Confirm these paths exist for proper auto-discovery:
- `skills/postgres/SKILL.md`
- `skills/postgres-functions/SKILL.md`
- `skills/supabase-rls-policy/SKILL.md`
- `skills/postgres-style-guide/SKILL.md`
- `agents/postgres-table-design-expert.md`
- `agents/supabase-rls-expert.md`

### Task 3: Reinstall plugin and verify

After fixing:
```bash
/plugin uninstall supabase@linehaulai-claude-marketplace
/plugin install supabase@linehaulai-claude-marketplace
```

Then restart Claude Code and verify no errors.

## Verification

1. Plugin loads without errors in Claude Code
2. Skills appear in available skills list
3. Agents can be invoked via Task tool
