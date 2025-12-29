# Linehaul AI Claude Marketplace

<!-- AUTO-MANAGED: project-description -->
A Claude Code plugin marketplace containing production-ready plugins for business system integrations and backend development orchestration.

**Purpose**: Distribute reusable Claude Code plugins for common integration patterns and development workflows.

**Key Plugins**:
- `quickbooks-api-integration`: QuickBooks Online API integration guidance for ERP/CRM/TMS systems
- `golang-orchestrator`: Expert guidance for Golang backend development with Echo framework, including laneweaverTMS service patterns
- `sveltekit-spa`: SvelteKit SPA development patterns and configuration
- `shadcn-svelte-skill`: Svelte UI component management with shadcn-svelte, Skeleton UI, and Melt UI guidance (Tailwind CSS v4.1 + TypeScript)
- `svelte-flow`: Interactive node-based editors and flow diagrams with @xyflow/svelte (workflow editors, DAG editors, mindmaps)
- `layerchart`: Pre-built chart components for rapid data visualization (bar, line, pie, tree maps, geographic charts)
- `layercake`: Headless visualization framework for unlimited custom visualizations (maximum flexibility)
- `sequential-thinking`: Systematic problem-solving through iterative reasoning with revision and branching (complex analysis, design, debugging, planning)
- `supabase`: Supabase development plugin with PostgreSQL schema design, function creation with security best practices, RLS policy guidance, and laneweaverTMS-specific database patterns
- `svelte5-runes`: Svelte 5 runes system guidance for reactivity, props, effects, and Svelte 4→5 migration
- `composable-svelte-components`: UI component library reference for Composable Svelte applications with shadcn-svelte components, covering navigation, forms, data display, feedback, and layout patterns
- `goth-oauth`: Expert guidance for github.com/markbates/goth OAuth authentication in Go, covering provider setup (Google, Microsoft), Echo framework integration, session management, and security
- `mycarrierpackets-api`: MyCarrierPackets API integration for TMS systems, covering OAuth2 authentication, carrier invitations (Intellivite), Assure Advantage monitoring, document retrieval, and Go implementation patterns
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
│   └── skills/              # Orchestration skills
├── sveltekit-spa/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── references/          # Reference documentation
│   │   ├── backend-integration.md
│   │   └── routing-patterns.md
│   └── SKILL.md             # SvelteKit SPA development patterns
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
│   └── skills/
│       ├── postgres-style-guide/
│       │   └── SKILL.md     # SQL style conventions
│       ├── supabase-rls-policy/
│       │   └── SKILL.md     # RLS policy patterns and access control
│       └── laneweaver-database-design/
│           └── SKILL.md     # laneweaverTMS domain-specific patterns
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
├── composable-svelte-components/
│   └── SKILL.md             # UI component library reference
├── goth-oauth/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest
│   ├── skills/
│   │   ├── goth-fundamentals/
│   │   │   └── SKILL.md     # Core Goth concepts
│   │   ├── goth-providers/
│   │   │   └── SKILL.md     # Provider configuration
│   │   └── goth-echo-security/
│   │       └── SKILL.md     # Echo integration + security
│   ├── agents/
│   │   └── goth-expert.md   # OAuth troubleshooting expert
│   ├── references/
│   │   ├── google-oauth-setup.md
│   │   ├── microsoft-oauth-setup.md
│   │   ├── session-storage-options.md
│   │   └── security-checklist.md
│   ├── README.md
│   ├── INSTALL.md
│   └── QUICK_START.md
└── mycarrierpackets-api/
    ├── .claude-plugin/
    │   └── plugin.json      # Plugin manifest
    ├── commands/
    │   └── mycarrierpackets.md  # Topic-based API assistant
    ├── skills/
    │   └── mycarrierpackets-api/
    │       └── SKILL.md     # Comprehensive API documentation
    ├── README.md
    ├── INSTALL.md
    └── QUICK_START.md
```

**Structure**:
- All plugins consolidated under `.claude-plugin/` directory
- Full plugins (with commands/subagents) contain `.claude-plugin/plugin.json` manifests
- Skill-only plugins contain SKILL.md with optional reference documentation
- Top-level `marketplace.json` references all plugins with paths: `./.claude-plugin/{plugin-name}`

**Plugin Types**:
1. **Full Plugins** (svelte-flow, layerchart, layercake, svelte5-runes, goth-oauth, mycarrierpackets-api): Commands + Skills + Agents
2. **Skill Plugins** (sequential-thinking, composable-svelte-components): Standalone skills with reference docs, no manifest needed
3. **Hybrid Plugins** (quickbooks-api-integration, sveltekit-spa, shadcn-svelte-skill, golang-orchestrator, supabase): Skills with manifest and reference docs, minimal structure

**Golang Orchestrator Pattern**:
- Three complementary skills: effective-go (architecture) → backend-service-patterns (data layer) → echo-router-skill (HTTP layer)
- Clear separation: effective-go provides foundational architecture, backend-service-patterns implements service/repository patterns, echo-router-skill handles HTTP routing
- Hierarchical skill progression from general Golang best practices to specific TMS domain patterns to HTTP implementation
- Skills designed to work together: architecture informs data layer design, which integrates with HTTP handlers

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
- Hybrid plugin with multiple specialized skills for Supabase/PostgreSQL development
- Skills organized by concern:
  - `postgres-style-guide`: SQL style conventions
  - `supabase-rls-policy`: Row-level security policy patterns
  - `laneweaver-database-design`: laneweaverTMS domain-specific database patterns (UUIDs, audit columns, ENUMs, soft deletes, migrations)
- Covers SQL style, row-level security, and laneweaverTMS database patterns
- Each skill has comprehensive documentation with examples and best practices

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

**goth-oauth Pattern**:
- Full plugin for Go OAuth authentication using github.com/markbates/goth
- Three complementary skills: goth-fundamentals (core) → goth-providers (configuration) → goth-echo-security (framework + security)
- Agent: goth-expert for troubleshooting OAuth flows and architecture decisions
- Reference documentation organized by concern:
  - Provider-specific setup guides (Google, Microsoft/Azure AD)
  - Session storage comparison (cookies, Redis, PostgreSQL)
  - Security checklist for pre-deployment verification
- Designed to complement golang-orchestrator for complete Echo backend authentication

**mycarrierpackets-api Pattern**:
- Single comprehensive skill + command for MyCarrierPackets API integration
- Skill: Complete API reference covering all endpoints, authentication, and Go implementation
- Command: /mycarrierpackets with topic routing (auth, invite, carrier, monitor, documents, sync, debug)
- Focus areas:
  - OAuth2 password grant authentication with token management
  - Carrier invitations via Intellivite (API, link-based, direct URL)
  - Assure Advantage carrier monitoring and risk assessment
  - Document retrieval (COI, W9, eAgreement, full packets)
  - Synchronization patterns (push vs pull, polling strategies)
- Go-first code examples with idiomatic patterns
- Designed for TMS integration following golang-orchestrator patterns
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
/plugin install supabase
/plugin install svelte5-runes
/plugin install composable-svelte-components
/plugin install mycarrierpackets-api
```

### Development

To develop or modify plugins in this marketplace:

1. Navigate to `.claude-plugin/{plugin-name}/`
2. Modify skills, commands, or documentation
3. Update plugin version in `.claude-plugin/{plugin-name}/.claude-plugin/plugin.json`
4. Update marketplace.json if metadata changes
<!-- END MANUAL -->
