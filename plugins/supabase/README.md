# Supabase Plugin

Supabase and PostgreSQL expertise for row-level security policies and laneweaverTMS-specific database patterns.

## What This Plugin Provides

**Skills:**
- `supabase-rls-policy`: Row-level security (RLS) policy patterns and access control for Supabase
- `laneweaver-database-design`: laneweaverTMS-specific PostgreSQL patterns with UUIDs, ENUMs, audit trails, soft deletes, and atomic migrations

## Installation

```bash
/plugin marketplace add /path/to/linehaulai-claude-marketplace
/plugin install supabase
```

## Quick Start

### RLS Policies

Ask Claude: "Create RLS policies for [table/scenario]"
- The `supabase-rls-policy` skill activates for access control
- Provides policy patterns for common scenarios
- Handles multi-tenancy, team-based access, and complex rules

## Skills Overview

### supabase-rls-policy - Access Control

**Use when:**
- Implementing row-level security
- Designing multi-tenant access patterns
- Creating team-based permissions
- Setting up user-specific data access

**Covers:**
- RLS policy syntax and patterns
- Common access control scenarios
- Policy testing and debugging
- Performance considerations

### laneweaver-database-design - Domain-Specific Patterns

**Use when:**
- Designing schemas for laneweaverTMS
- Creating database migrations for TMS domain models
- Implementing audit trails and soft deletes
- Working with ENUMs for status workflows
- Following laneweaverTMS database conventions

**Covers:**
- UUID primary keys with exception for users table
- Required audit columns (created_at, updated_at, created_by, updated_by, deleted_at, deleted_by)
- Soft delete patterns (deleted_at IS NULL)
- ENUM types for status workflows (load_status, tender_status, etc.)
- Trigger patterns (updated_at, sync, validation)
- View patterns with RLS (security_invoker='on')
- Migration file structure and atomic migration strategy
- Polymorphic relationships (type + ID columns)

**References:**
- Authoritative schema: laneweaverTMS/erd.sql
- Migration examples: laneweaverTMS/supabase/migrations/

## Plugin Structure

```
.claude-plugin/supabase/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── skills/
│   ├── supabase-rls-policy/
│   │   └── SKILL.md             # RLS policy patterns
│   └── laneweaver-database-design/
│       └── SKILL.md             # laneweaverTMS domain-specific patterns
└── README.md                    # This file
```

## Plugin Type

**Pattern:** Hybrid Plugin
- Multiple specialized skills organized by concern
- Complete Supabase/PostgreSQL development coverage
- Each skill has comprehensive documentation with examples

## Skill Triggering

Skills automatically activate based on context:
- **supabase-rls-policy**: "RLS policy", "row-level security", "access control"
- **laneweaver-database-design**: "laneweaverTMS", "audit columns", "soft delete", "UUID primary key", "tender", "load"

## Development Workflow

1. **Access Control** (supabase-rls-policy skill)
   - Add RLS policies for data protection
   - Implement multi-tenancy or team-based access
   - Test policies thoroughly

2. **Domain-Specific Patterns** (laneweaver-database-design skill)
   - Use laneweaverTMS audit columns and soft deletes
   - Follow UUID primary key conventions
   - Implement required ENUM types

## Integration with Other Plugins

Works seamlessly with:
- **superpowers:brainstorming** - Design database architecture before implementation
- **superpowers:writing-plans** - Plan schema migrations and policy changes
- **superpowers:verification-before-completion** - Verify schema and policies before deployment

## Best Practices

1. **Implement RLS Early** - Add and test RLS policies with `supabase-rls-policy` skill
2. **Use Domain Patterns** - Follow `laneweaver-database-design` for TMS-specific conventions
3. **Test Thoroughly** - Verify RLS policies and audit patterns work correctly

## Documentation

See individual SKILL.md files for:
- Complete usage guides
- Code examples and patterns
- Troubleshooting sections
- Best practices
- Anti-patterns with fixes

## License

MIT
