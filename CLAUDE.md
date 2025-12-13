# Linehaul AI Claude Marketplace

<!-- AUTO-MANAGED: project-description -->
A Claude Code plugin marketplace containing production-ready plugins for business system integrations and backend development orchestration.

**Purpose**: Distribute reusable Claude Code plugins for common integration patterns and development workflows.

**Key Plugins**:
- `quickbooks-api-integration`: QuickBooks Online API integration guidance for ERP/CRM/TMS systems
- `golang-orchestrator`: Subagent orchestration for production Golang backends with Echo framework
- `sveltekit-spa`: SvelteKit SPA development patterns and configuration
- `shadcn-svelte-skill`: shadcn-svelte UI components with Tailwind CSS v4.1 and TypeScript
- `svelte-flow`: Interactive node-based editors and flow diagrams with @xyflow/svelte (workflow editors, DAG editors, mindmaps)
- `layerchart`: Pre-built chart components for rapid data visualization (bar, line, pie, tree maps, geographic charts)
- `layercake`: Headless visualization framework for unlimited custom visualizations (maximum flexibility)
- `sequential-thinking`: Systematic problem-solving through iterative reasoning with revision and branching (complex analysis, design, debugging, planning)
- `supabase-rls-policy`: Expert guidance for Supabase PostgreSQL row-level security (RLS) policies and access control patterns
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
│   ├── references/          # Reference documentation
│   │   ├── datatable-tanstack-svelte5.md
│   │   └── shadcn-datatable.md
│   └── SKILL.md             # Main skill definition
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
        └── supabase-rls-policy/
            └── SKILL.md             # RLS policy expert guidance
```

**Structure**:
- All plugins consolidated under `.claude-plugin/` directory
- Full plugins (with commands/subagents) contain `.claude-plugin/plugin.json` manifests
- Skill-only plugins contain SKILL.md with optional reference documentation
- Top-level `marketplace.json` references all plugins with paths: `./.claude-plugin/{plugin-name}`

**Plugin Types**:
1. **Full Plugins** (quickbooks-api-integration, golang-orchestrator, svelte-flow, layerchart, layercake): Commands + Skills + Manifest + Agents
2. **Skill Plugins** (shadcn-svelte-skill, sequential-thinking, supabase-rls-policy): Standalone skills with reference docs, no manifest needed
3. **Hybrid Plugins** (sveltekit-spa): Skills + Commands, minimal structure

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
- Skill-only plugin focused on UI component development
- References subdirectory contains specialized documentation (DataTable examples)
- Tailwind CSS v4.1 with Vite integration patterns
- TypeScript-first with Svelte 5 reactive variables
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
```

### Development

To develop or modify plugins in this marketplace:

1. Navigate to `.claude-plugin/{plugin-name}/`
2. Modify skills, commands, or documentation
3. Update plugin version in `.claude-plugin/{plugin-name}/.claude-plugin/plugin.json`
4. Update marketplace.json if metadata changes
<!-- END MANUAL -->
