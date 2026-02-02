# Supabase Plugin

Supabase and PostgreSQL expertise for laneweaverTMS-specific database patterns.

## What This Plugin Provides

**Skills:**
- `laneweaver-database-design`: laneweaverTMS-specific PostgreSQL patterns with UUIDs, ENUMs, audit trails, soft deletes, and atomic migrations

## Installation

```bash
/plugin marketplace add /path/to/linehaulai-claude-marketplace
/plugin install supabase
```

## Quick Start

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
- **laneweaver-database-design**: "laneweaverTMS", "audit columns", "soft delete", "UUID primary key", "tender", "load"

## Development Workflow

**Domain-Specific Patterns** (laneweaver-database-design skill)
- Use laneweaverTMS audit columns and soft deletes
- Follow UUID primary key conventions
- Implement required ENUM types

## Integration with Other Plugins

Works seamlessly with:
- **superpowers:brainstorming** - Design database architecture before implementation
- **superpowers:writing-plans** - Plan schema migrations and policy changes
- **superpowers:verification-before-completion** - Verify schema and policies before deployment

## Best Practices

1. **Use Domain Patterns** - Follow `laneweaver-database-design` for TMS-specific conventions
2. **Test Thoroughly** - Verify audit patterns and migrations work correctly

## Documentation

See individual SKILL.md files for:
- Complete usage guides
- Code examples and patterns
- Troubleshooting sections
- Best practices
- Anti-patterns with fixes

## License

MIT
