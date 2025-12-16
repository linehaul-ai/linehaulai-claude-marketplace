# Linehaul AI Claude Marketplace

<!-- AUTO-MANAGED: project-description -->
A Claude Code plugin marketplace containing production-ready plugins for business system integrations and backend development orchestration.

**Purpose**: Distribute reusable Claude Code plugins for common integration patterns and development workflows.

**Key Plugins**:
- `quickbooks-api-integration`: QuickBooks Online API integration guidance for ERP/CRM/TMS systems
- `golang-orchestrator`: Subagent orchestration for production Golang backends with Echo framework
- `sveltekit-spa`: SvelteKit SPA development patterns and configuration
- `shadcn-svelte-skill`: Svelte UI component management with shadcn-svelte, Skeleton UI, and Melt UI guidance (Tailwind CSS v4.1 + TypeScript)
- `svelte-flow`: Interactive node-based editors and flow diagrams with @xyflow/svelte (workflow editors, DAG editors, mindmaps)
- `layerchart`: Pre-built chart components for rapid data visualization (bar, line, pie, tree maps, geographic charts)
- `layercake`: Headless visualization framework for unlimited custom visualizations (maximum flexibility)
- `sequential-thinking`: Systematic problem-solving through iterative reasoning with revision and branching (complex analysis, design, debugging, planning)
- `supabase`: Supabase development plugin with PostgreSQL schema design, function creation with security best practices, and RLS policy guidance
- `svelte5-runes`: Svelte 5 runes system guidance for reactivity, props, effects, and Svelte 4→5 migration
- `git-worktree`: Isolated Git worktree management for parallel feature development with helper scripts
<!-- END AUTO-MANAGED -->

<!-- AUTO-MANAGED: architecture -->
## Architecture

```
.claude-plugin/
├── marketplace.json          # Plugin registry and metadata
├── quickbooks-api-integration/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── commands/            # Slash commands
│   ├── skills/              # Plugin skills
│   ├── README.md
│   ├── INSTALL.md
│   ├── PLUGIN_OVERVIEW.md
│   └── QUICK_START.md
├── golang-orchestrator/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── agents/              # Specialized subagent definitions
│   │   ├── echo-router-expert.md  # Echo framework HTTP routing specialist
│   │   └── golang-expert.md       # Golang architecture specialist
│   ├── commands/            # Slash commands
│   │   └── backend-setup-orchestration.md  # Detailed orchestration workflow
│   ├── skills/              # Orchestration skills
│   ├── docs/
│   ├── README.md
│   ├── INSTALL.md
│   ├── PLUGIN_OVERVIEW.md
│   ├── DEPLOYMENT_CHECKLIST.md
│   ├── DOTFILES_SETUP.md
│   └── NEXT_STEPS.md
├── sveltekit-spa/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── commands/            # Slash commands
│   ├── skills/              # SvelteKit skills
│   └── README.md
├── shadcn-svelte-skill/
│   ├── commands/            # Slash commands
│   │   └── shadcn.md        # Component development assistant
│   ├── references/          # Reference documentation
│   │   ├── datatable-tanstack-svelte5.md
│   │   ├── shadcn-datatable.md
│   │   └── workflows.md     # Complex multi-component build workflows
│   └── SKILL.md             # Main skill definition (shadcn-svelte + Skeleton UI + Melt UI)
├── svelte-flow/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── agents/              # Specialized subagents
│   │   └── svelte-flow-expert.md  # Svelte Flow implementation expert
│   ├── commands/            # Slash commands
│   │   └── create-editor.md  # Interactive editor orchestration
│   ├── skills/
│   │   └── svelte-flow/SKILL.md  # Comprehensive Svelte Flow documentation
│   ├── README.md
│   ├── QUICK_START.md
│   └── PLUGIN_OVERVIEW.md
├── layerchart/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── agents/
│   │   └── layerchart-expert.md  # Chart components expert
│   ├── skills/
│   │   └── layerchart/SKILL.md   # LayerChart component documentation
│   ├── README.md
│   ├── QUICK_START.md
│   └── PLUGIN_OVERVIEW.md
├── layercake/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── agents/
│   │   └── layercake-expert.md   # Custom visualization framework expert
│   ├── skills/
│   │   └── layercake/SKILL.md    # Layer Cake framework documentation
│   ├── README.md
│   ├── QUICK_START.md
│   └── PLUGIN_OVERVIEW.md
├── sequential-thinking/
│   ├── SKILL.md             # Main skill definition (MCP-based reasoning)
│   └── references/
│       ├── advanced.md      # Revision and branching patterns
│       └── examples.md      # Real-world use cases
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
├── svelte5-runes/
│   ├── commands/            # Slash commands
│   │   └── runes.md         # Runes assistant for reactivity and migration
│   ├── agents/              # Specialized subagents
│   │   └── runes-expert.md  # Svelte 5 runes implementation expert
│   ├── references/          # Reference documentation
│   │   ├── common-mistakes.md     # Anti-patterns with fixes
│   │   ├── component-api.md       # $props, $bindable patterns
│   │   ├── migration-gotchas.md   # Svelte 4 → 5 translation
│   │   ├── reactivity-patterns.md # When to use each rune
│   │   └── snippets-vs-slots.md   # New snippet syntax
│   ├── examples/            # Code examples
│   │   ├── bindable-props.svelte
│   │   └── effect-vs-derived.svelte
│   ├── SKILL.md             # Main skill definition
│   └── README.md
└── git-worktree/
    ├── scripts/             # Helper scripts
    │   └── worktree-manager.sh  # Worktree management CLI
    ├── SKILL.md             # Git worktree guidance
    └── README.md
```

**Structure**:
- All plugins consolidated under `.claude-plugin/` directory
- Full plugins (with commands/subagents) contain `.claude-plugin/plugin.json` manifests
- Skill-only plugins contain SKILL.md with optional reference documentation
- Top-level `marketplace.json` references all plugins with paths: `./.claude-plugin/{plugin-name}`

**Plugin Types**:
1. **Full Plugins** (quickbooks-api-integration, golang-orchestrator, svelte-flow, layerchart, layercake, svelte5-runes, supabase): Commands + Skills + Agents
2. **Skill Plugins** (sequential-thinking, git-worktree): Standalone skills with reference docs, no manifest needed
3. **Hybrid Plugins** (sveltekit-spa, shadcn-svelte-skill): Skills + Commands, minimal structure

**Golang Orchestrator Pattern**:
- Two-agent orchestration: Golang Expert (architecture) + Echo Router Expert (HTTP layer)
- Agents spawned in parallel via backend-setup-orchestration command
- Clear separation: Golang agent defines interfaces, Echo agent implements HTTP handlers
- Detailed workflow with requirement extraction, context creation, and agent coordination

**Visualization Plugins Pattern** (svelte-flow, layerchart, layercake):
- **svelte-flow**: Interactive node-based editors with @xyflow/svelte
  - Specialized agent: svelte-flow-expert (layout algorithms, performance optimization)
  - Command: create-editor (orchestrates editor setup)
  - Skill: comprehensive Svelte Flow library documentation
- **layerchart**: Pre-built chart components built on Layer Cake
  - Specialized agent: layerchart-expert (component selection, composition patterns)
  - Skill: component types, data binding, styling
  - No command needed (declarative component usage)
- **layercake**: Headless visualization framework for custom charts
  - Specialized agent: layercake-expert (scales, dimensions, custom rendering)
  - Skill: framework architecture, D3 integration, reactivity patterns
  - No command needed (framework-based development)
- Relationship: LayerChart is built on LayerCake, but both independently useful
- Full plugin structure: plugin.json + agents/ + skills/ + documentation

**shadcn-svelte-skill Pattern**:
- Hybrid plugin with skill + command for Svelte UI component development
- Primary focus: shadcn-svelte with Tailwind CSS v4.1 and TypeScript
- Also covers: Skeleton UI and Melt UI for library selection guidance
- Command: /shadcn for guided component development (add, form, table, dialog, theme, debug)
- References subdirectory contains specialized documentation:
  - DataTable examples (TanStack Table v8 integration)
  - Complex multi-component build workflows
- TypeScript-first with Svelte 5 reactive variables

**supabase Pattern**:
- Full plugin with multiple specialized skills for Supabase/PostgreSQL development
- Skills organized by concern:
  - `postgres`: Schema design with PostgreSQL best practices
  - `postgres-functions`: Function creation with security (SECURITY INVOKER, search_path)
  - `supabase-rls-policy`: Row-level security policy patterns
- Agent: postgres-table-design-expert for schema design decisions
- Covers full Supabase development lifecycle: schema → functions → RLS policies
- Each skill has comprehensive documentation with examples and anti-patterns

**svelte5-runes Pattern**:
- Full plugin for Svelte 5 reactivity system guidance
- Command: /runes for topic-based assistance (state, derived, effect, props, migrate, snippets, debug)
- Agent: runes-expert for deep implementation decisions and migration strategies
- Comprehensive reference documentation:
  - Reactivity patterns ($state vs $derived vs $effect decisions)
  - Migration gotchas (Svelte 4 → 5 translation)
  - Component API ($props, $bindable patterns)
  - Snippet syntax (replacing legacy slots)
  - Common mistakes with fixes
- Code examples for bindable props and effect vs derived patterns

**git-worktree Pattern**:
- Skill-only plugin with bundled helper scripts
- Provides Git worktree management guidance
- Includes bash script for common operations (create, list, switch, cleanup)
- Follows "Skill with Bundled Resources" pattern
- No plugin.json needed (pure skill plugin)
<!-- END AUTO-MANAGED -->

<!-- AUTO-MANAGED: conventions -->
## Conventions

**Plugin Structure**:
- Plugin directories nested under `.claude-plugin/`
- Full plugins have dedicated subdirectories: `commands/`, `skills/`, `docs/`
- Skill-only plugins: SKILL.md with optional `references/` subdirectory for specialized docs
- Documentation files (full plugins): README.md, INSTALL.md, PLUGIN_OVERVIEW.md, QUICK_START.md

**Marketplace Registry**:
- `marketplace.json` contains plugin metadata with owner info
- Plugin sources specified as relative paths: `./.claude-plugin/{name}`
- Each plugin entry includes: name, source, version, author
<!-- END AUTO-MANAGED -->

<!-- MANUAL -->
## Usage

### Installing Plugins from this Marketplace

```bash
# Add this marketplace to Claude Code
/plugin marketplace add /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace

# Install a specific plugin
/plugin install quickbooks-api-integration
/plugin install golang-orchestrator
/plugin install sveltekit-spa
/plugin install shadcn-svelte-skill
/plugin install svelte-flow
/plugin install layerchart
/plugin install layercake
/plugin install sequential-thinking
/plugin install supabase-rls-policy
/plugin install svelte5-runes
/plugin install git-worktree
```

### Development

To develop or modify plugins in this marketplace:

1. Navigate to `.claude-plugin/{plugin-name}/`
2. Modify skills, commands, or documentation
3. Update plugin version in `.claude-plugin/{plugin-name}/.claude-plugin/plugin.json`
4. Update marketplace.json if metadata changes
<!-- END MANUAL -->
