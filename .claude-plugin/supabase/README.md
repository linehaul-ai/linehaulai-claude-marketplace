# Supabase Plugin

Comprehensive Supabase and PostgreSQL development guidance for schema design, secure function creation, and row-level security policies.

## What This Plugin Provides

**Skills:**
- `postgres`: PostgreSQL schema design with best practices, data types, indexing, and performance patterns
- `postgres-functions`: Secure PostgreSQL function creation with SECURITY INVOKER, search_path configuration, and anti-patterns
- `supabase-rls-policy`: Row-level security (RLS) policy patterns and access control for Supabase

**Agents:**
- `postgres-table-design-expert`: Specialized agent for production-ready schema architecture decisions
- `supabase-rls-expert`: Specialized agent for RLS policy implementation and optimization

## Installation

```bash
/plugin marketplace add /path/to/linehaulai-claude-marketplace
/plugin install supabase
```

## Quick Start

### Schema Design

Ask Claude: "Design a PostgreSQL schema for [your use case]"
- The `postgres` skill activates for schema design tasks
- Uses postgres-table-design-expert agent for complex decisions
- Provides production-ready schemas with proper data types, constraints, and indexing

### Function Creation

Ask Claude: "Create a PostgreSQL function to [task]"
- The `postgres-functions` skill activates for function creation
- Ensures SECURITY INVOKER and search_path configuration
- Shows anti-patterns with ❌/✅ comparisons
- Prevents common security vulnerabilities

### RLS Policies

Ask Claude: "Create RLS policies for [table/scenario]"
- The `supabase-rls-policy` skill activates for access control
- Provides policy patterns for common scenarios
- Handles multi-tenancy, team-based access, and complex rules

## Skills Overview

### postgres - Schema Design

**Use when:**
- Designing new database schemas
- Choosing data types and constraints
- Planning indexes for performance
- Implementing referential integrity

**Covers:**
- PostgreSQL-specific data types (JSONB, arrays, enums)
- Indexing strategies (B-tree, GiST, GIN)
- Constraint patterns (CHECK, UNIQUE, foreign keys)
- Normalization and denormalization decisions

### postgres-functions - Secure Functions

**Use when:**
- Creating PostgreSQL functions or stored procedures
- Writing trigger functions
- Implementing database-side business logic

**Covers:**
- Security principles (SECURITY INVOKER, search_path)
- Function patterns (basic, triggers, error handling)
- Anti-patterns with corrections
- Volatility levels (IMMUTABLE, STABLE, VOLATILE)

**Security Features:**
- Prevents schema search path attacks
- Prevents privilege escalation
- Prevents SQL injection
- Shows wrong vs. right implementations

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

## Agents

### postgres-table-design-expert

Schema design specialist that provides:
- Production-ready database architecture
- Best practices for data types and constraints
- Indexing strategies for performance
- Normalization and denormalization guidance

**Use for:**
- Complex schema design decisions
- Performance optimization questions
- Database architecture reviews
- Migration planning

### supabase-rls-expert

RLS policy specialist that provides:
- Row-level security implementation
- Access control pattern recommendations
- Policy optimization strategies
- Security audit guidance

**Use for:**
- Complex RLS policy scenarios
- Multi-tenancy patterns
- Performance-critical access control
- Security reviews

## Plugin Structure

```
.claude-plugin/supabase/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── agents/
│   ├── postgres-table-design-expert.md  # Schema design specialist
│   └── supabase-rls-expert.md           # RLS policy specialist
├── skills/
│   ├── postgres/
│   │   └── SKILL.md             # Schema design guidance
│   ├── postgres-functions/
│   │   └── SKILL.md             # Function creation with security
│   └── supabase-rls-policy/
│       └── SKILL.md             # RLS policy patterns
└── README.md                    # This file
```

## Plugin Type

**Pattern:** Full Plugin
- Multiple specialized skills organized by concern
- Agents for complex schema and RLS decisions
- Complete Supabase/PostgreSQL development coverage
- Each skill has comprehensive documentation with examples

## Skill Triggering

Skills automatically activate based on context:
- **postgres**: "design schema", "create table", "data types"
- **postgres-functions**: "create function", "trigger", "stored procedure"
- **supabase-rls-policy**: "RLS policy", "row-level security", "access control"

## Development Workflow

1. **Schema Design** (postgres skill)
   - Design tables with proper types and constraints
   - Plan indexes for query patterns
   - Use postgres-table-design-expert for complex decisions

2. **Function Creation** (postgres-functions skill)
   - Implement business logic in secure functions
   - Follow SECURITY INVOKER and search_path patterns
   - Avoid anti-patterns shown in skill

3. **Access Control** (supabase-rls-policy skill)
   - Add RLS policies for data protection
   - Implement multi-tenancy or team-based access
   - Test policies thoroughly

## Integration with Other Plugins

Works seamlessly with:
- **superpowers:brainstorming** - Design database architecture before implementation
- **superpowers:writing-plans** - Plan schema migrations and policy changes
- **superpowers:verification-before-completion** - Verify schema and policies before deployment

## Best Practices

1. **Start with Schema** - Design schema first with `postgres` skill
2. **Secure Functions** - Always use `postgres-functions` for function creation
3. **Test RLS Early** - Add and test RLS policies with `supabase-rls-policy` skill
4. **Use Anti-Patterns** - Learn from ❌ WRONG / ✅ CORRECT examples in skills
5. **Leverage Agents** - Use postgres-table-design-expert for complex schema decisions

## Documentation

See individual SKILL.md files for:
- Complete usage guides
- Code examples and patterns
- Troubleshooting sections
- Best practices
- Anti-patterns with fixes

## License

MIT
