# Align postgres-functions Skill with Marketplace Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Properly integrate the postgres-functions skill into the supabase plugin structure, aligning with marketplace conventions

**Architecture:** The postgres-functions skill currently exists at `.claude-plugin/supabase/skills/postgres-functions/` but is not properly documented or aligned with the marketplace. The supabase plugin already exists in marketplace.json as a registered plugin. We need to ensure the skill follows naming conventions, add a README if needed, update CLAUDE.md documentation, and ensure the supabase plugin structure is complete.

**Tech Stack:** Markdown, JSON

---

## Task 1: Verify Current Structure

**Files:**
- Verify: `.claude-plugin/supabase/` directory structure
- Verify: `.claude-plugin/supabase/skills/postgres-functions/SKILL.MD` exists

**Step 1: Check supabase plugin structure**

Run: `tree .claude-plugin/supabase/ -L 3`
Expected: Shows directory with skills/, agents/, and potentially other directories

**Step 2: Verify postgres-functions skill exists**

Run: `ls -la .claude-plugin/supabase/skills/postgres-functions/`
Expected: Shows SKILL.MD file (320 lines)

**Step 3: Check if supabase plugin has plugin.json**

Run: `ls -la .claude-plugin/supabase/.claude-plugin/plugin.json`
Expected: File exists with plugin manifest

**Step 4: Check current supabase entry in marketplace.json**

Run: `jq '.plugins[] | select(.name == "supabase")' .claude-plugin/marketplace.json`
Expected: Shows supabase plugin entry with version 1.0.0

**Step 5: No commit needed** (verification only)

---

## Task 2: Update CLAUDE.md Key Plugins List

**Files:**
- Modify: `CLAUDE.md` (line ~16)

**Step 1: Check current supabase entry in Key Plugins**

Run: `grep -n "supabase" CLAUDE.md | head -3`
Expected: Shows line with supabase-rls-policy mention

**Step 2: Update Key Plugins list to include postgres-functions**

Current line (~16):
```markdown
- `supabase-rls-policy`: Expert guidance for Supabase PostgreSQL row-level security (RLS) policies and access control patterns
```

Replace with:
```markdown
- `supabase`: Supabase development plugin with PostgreSQL schema design, function creation with security best practices, and RLS policy guidance
```

**Step 3: Verify update**

Run: `grep -A 1 "supabase.*Supabase development" CLAUDE.md`
Expected: Shows updated line

**Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update supabase plugin description in CLAUDE.md

Expand description to cover all supabase skills:
- PostgreSQL schema design (postgres skill)
- Function creation with security (postgres-functions skill)
- RLS policy guidance (supabase-rls-policy skill)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Document Supabase Plugin Structure in CLAUDE.md Architecture

**Files:**
- Modify: `CLAUDE.md` (Architecture section, after sequential-thinking)

**Step 1: Find supabase plugin location in architecture section**

Run: `grep -n "supabase-rls-policy" CLAUDE.md | grep -v "sequential-thinking"`
Expected: Shows line number in architecture section

**Step 2: Replace old structure with complete supabase plugin structure**

Find the section (likely around line 100-110):
```markdown
├── supabase-rls-policy/
│   └── SKILL.md             # RLS policy expert guidance
```

Replace with:
```markdown
├── supabase/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── agents/
│   │   └── postgres-table-design-expert.md  # Schema design specialist
│   └── skills/
│       ├── postgres/
│       │   └── SKILL.md     # PostgreSQL schema design guidance
│       ├── postgres-functions/
│       │   └── SKILL.MD     # PostgreSQL function creation with security
│       └── supabase-rls-policy/
│           └── SKILL.md     # RLS policy patterns and access control
```

**Step 3: Verify structure update**

Run: `grep -A 10 "├── supabase/" CLAUDE.md | grep -E "(skills|agents|postgres)"`
Expected: Shows all three skills and agents directory

**Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: document complete supabase plugin structure in CLAUDE.md

Show all components:
- agents/postgres-table-design-expert.md
- skills/postgres/ (schema design)
- skills/postgres-functions/ (function creation)
- skills/supabase-rls-policy/ (RLS policies)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Update Plugin Types Documentation

**Files:**
- Modify: `CLAUDE.md` (Plugin Types section)

**Step 1: Find Plugin Types section**

Run: `grep -n "^\*\*Plugin Types\*\*:" CLAUDE.md`
Expected: Shows line number (likely ~135-145)

**Step 2: Update Skill Plugins entry**

Current:
```markdown
2. **Skill Plugins** (sequential-thinking, supabase-rls-policy, git-worktree): Standalone skills with reference docs, no manifest needed
```

This is INCORRECT - supabase IS a full plugin with manifest. Update to:
```markdown
2. **Skill Plugins** (sequential-thinking, git-worktree): Standalone skills with reference docs, no manifest needed
```

**Step 3: Update Full Plugins entry**

Current:
```markdown
1. **Full Plugins** (quickbooks-api-integration, golang-orchestrator, svelte-flow, layerchart, layercake, svelte5-runes): Commands + Skills + Agents
```

Add supabase:
```markdown
1. **Full Plugins** (quickbooks-api-integration, golang-orchestrator, svelte-flow, layerchart, layercake, svelte5-runes, supabase): Commands + Skills + Agents
```

**Step 4: Verify updates**

Run: `grep "^\*\*Full Plugins\*\*.*supabase" CLAUDE.md`
Expected: Shows supabase in Full Plugins list

Run: `grep "^\*\*Skill Plugins\*\*" CLAUDE.md`
Expected: Does NOT show supabase (should only show sequential-thinking, git-worktree)

**Step 5: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: correct supabase plugin classification in CLAUDE.md

Move supabase from Skill Plugins to Full Plugins:
- Has .claude-plugin/plugin.json manifest
- Contains multiple skills and agents
- Properly classified as Full Plugin

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 5: Add Supabase Plugin Pattern Documentation

**Files:**
- Modify: `CLAUDE.md` (add new pattern section after sequential-thinking, before svelte5-runes)

**Step 1: Find pattern documentation section**

Run: `grep -n "^\*\*sequential-thinking Pattern\*\*:" CLAUDE.md`
Expected: Shows line number for patterns section

**Step 2: Add supabase pattern after sequential-thinking**

Insert after sequential-thinking pattern documentation (likely around line 180):

```markdown
**supabase Pattern**:
- Full plugin with multiple specialized skills for Supabase/PostgreSQL development
- Skills organized by concern:
  - `postgres`: Schema design with PostgreSQL best practices
  - `postgres-functions`: Function creation with security (SECURITY INVOKER, search_path)
  - `supabase-rls-policy`: Row-level security policy patterns
- Agent: postgres-table-design-expert for schema design decisions
- Covers full Supabase development lifecycle: schema → functions → RLS policies
- Each skill has comprehensive documentation with examples and anti-patterns
```

**Step 3: Verify pattern added**

Run: `grep -A 5 "^\*\*supabase Pattern\*\*:" CLAUDE.md`
Expected: Shows complete pattern documentation

**Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add supabase plugin pattern documentation

Document supabase as multi-skill full plugin:
- Three specialized skills by concern
- Schema design agent
- Full development lifecycle coverage

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 6: Create Supabase Plugin README

**Files:**
- Create: `.claude-plugin/supabase/README.md`

**Step 1: Check if README already exists**

Run: `ls -la .claude-plugin/supabase/README.md`
Expected: May or may not exist

**Step 2: Write comprehensive README**

```markdown
# Supabase Plugin

Comprehensive Supabase and PostgreSQL development guidance for schema design, secure function creation, and row-level security policies.

## What This Plugin Provides

**Skills:**
- `postgres`: PostgreSQL schema design with best practices, data types, indexing, and performance patterns
- `postgres-functions`: Secure PostgreSQL function creation with SECURITY INVOKER, search_path configuration, and anti-patterns
- `supabase-rls-policy`: Row-level security (RLS) policy patterns and access control for Supabase

**Agent:**
- `postgres-table-design-expert`: Specialized agent for production-ready schema architecture decisions

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

## Plugin Structure

```
.claude-plugin/supabase/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── agents/
│   └── postgres-table-design-expert.md  # Schema design specialist
├── skills/
│   ├── postgres/
│   │   └── SKILL.md             # Schema design guidance
│   ├── postgres-functions/
│   │   └── SKILL.MD             # Function creation with security
│   └── supabase-rls-policy/
│       └── SKILL.md             # RLS policy patterns
└── README.md                    # This file
```

## Plugin Type

**Pattern:** Full Plugin
- Multiple specialized skills organized by concern
- Agent for complex schema decisions
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
5. **Leverage Agent** - Use postgres-table-design-expert for complex schema decisions

## Documentation

See individual SKILL.md files for:
- Complete usage guides
- Code examples and patterns
- Troubleshooting sections
- Best practices
- Anti-patterns with fixes

## License

MIT
```

**Step 3: Verify README exists and has content**

Run: `wc -l .claude-plugin/supabase/README.md`
Expected: Shows > 150 lines

**Step 4: Commit**

```bash
git add .claude-plugin/supabase/README.md
git commit -m "docs: create comprehensive supabase plugin README

Add README documenting:
- Three specialized skills (postgres, postgres-functions, supabase-rls-policy)
- Schema design agent
- Installation and quick start
- Development workflow
- Skill triggering patterns

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 7: Update Installation Instructions in CLAUDE.md

**Files:**
- Verify: `CLAUDE.md` Usage section already has supabase

**Step 1: Check if supabase in installation list**

Run: `grep "/plugin install supabase" CLAUDE.md`
Expected: May or may not exist (it's currently listed as supabase-rls-policy)

**Step 2: If shows "supabase-rls-policy", update to "supabase"**

Find section (likely line ~225):
```markdown
/plugin install supabase-rls-policy
```

If it exists as `supabase-rls-policy`, it's WRONG (that's a skill, not the plugin). Should be:
```markdown
/plugin install supabase
```

The marketplace.json entry is `supabase` not `supabase-rls-policy`.

**Step 3: Verify correct entry**

Run: `grep -n "/plugin install supabase$" CLAUDE.md`
Expected: Shows line with correct plugin name

**Step 4: Commit if changed**

```bash
git add CLAUDE.md
git commit -m "docs: fix supabase plugin installation command

Change from 'supabase-rls-policy' to 'supabase':
- Matches marketplace.json plugin name
- supabase-rls-policy is a skill, not the plugin

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 8: Verify No Orphaned References

**Files:**
- Verify: No references to standalone "supabase-rls-policy" plugin remain

**Step 1: Search for incorrect references**

Run: `grep -n "supabase-rls-policy" CLAUDE.md | grep -v "skills/supabase-rls-policy"`
Expected: Only shows references to the SKILL path, not as a standalone plugin

**Step 2: Check marketplace.json doesn't have duplicate**

Run: `jq '.plugins[] | select(.name == "supabase-rls-policy")' .claude-plugin/marketplace.json`
Expected: Empty output (no such plugin, only skill)

**Step 3: Verify supabase plugin in marketplace**

Run: `jq '.plugins[] | select(.name == "supabase")' .claude-plugin/marketplace.json`
Expected: Shows supabase plugin entry

**Step 4: No commit needed** (verification only)

---

## Task 9: Final Verification

**Files:**
- Verify: All changes are complete and consistent

**Step 1: Verify CLAUDE.md consistency**

Run: `grep -c "supabase" CLAUDE.md`
Expected: Multiple matches for plugin, skills, patterns

**Step 2: Verify marketplace.json has supabase (not supabase-rls-policy)**

Run: `jq '.plugins | length' .claude-plugin/marketplace.json`
Expected: 11 plugins (no change from before)

**Step 3: Verify directory structure**

Run: `tree .claude-plugin/supabase/ -L 3`
Expected: Shows complete structure with README, skills, agents

**Step 4: Count commits**

Run: `git log --oneline --grep="supabase" -10 | head -5`
Expected: Shows 4-5 recent commits for supabase alignment

**Step 5: No commit needed** (verification only)

---

## Verification Checklist

After completing all tasks, verify:

- [ ] `.claude-plugin/supabase/README.md` exists with comprehensive documentation
- [ ] `CLAUDE.md` Key Plugins list mentions supabase with all three skills
- [ ] `CLAUDE.md` Architecture section shows complete supabase plugin structure
- [ ] `CLAUDE.md` Plugin Types classifies supabase as Full Plugin (not Skill Plugin)
- [ ] `CLAUDE.md` Pattern documentation describes supabase multi-skill organization
- [ ] `CLAUDE.md` Installation instructions use `/plugin install supabase`
- [ ] No orphaned references to "supabase-rls-policy" as standalone plugin
- [ ] marketplace.json contains "supabase" (not "supabase-rls-policy")
- [ ] All changes committed with meaningful messages
- [ ] Directory structure matches documented architecture

## Notes

- The supabase plugin already exists in marketplace.json as "supabase"
- The postgres-functions skill already exists at `.claude-plugin/supabase/skills/postgres-functions/SKILL.MD`
- This plan aligns documentation to match the actual structure
- No changes to marketplace.json needed (already correct)
- Focus is on updating CLAUDE.md documentation and adding README
