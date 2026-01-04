# laneweaver-tms-agents

Development agents and freight domain skills for laneweaverTMS.

## Overview

This plugin provides:
- **2 context-isolated agents** for database and frontend work
- **6 domain skills** covering freight terminology, business logic, and architecture patterns

Key principle: Agents exist for **context isolation**, not role anthropomorphization.

## Agents

### schema-migration-agent
Isolates the massive erd.sql (~500KB) from the main session for database schema work.

**Triggers:** "add a new table", "create migration", "database schema"

### frontend-component-agent
Isolates Svelte 5 reactive patterns from Go imperative patterns.

**Triggers:** "create component", "svelte", "runes", "$state"

## Skills

### Freight Domain
- **freight-domain-glossary** - Industry terminology (loads, tenders, carriers, accessorials)
- **load-lifecycle-patterns** - Load status transitions, billing workflows, TONU handling

### Architecture
- **rbac-authorization-patterns** - Multi-tenant RBAC, role definitions, Echo middleware
- **geospatial-postgis-patterns** - Geofences, spatial queries, real-time tracking

### Development
- **laneweaverTMS-feature-workflow** - Step-by-step guide orchestrating other skills
- **api-integration-patterns** - OAuth2, webhooks, rate limiting, error handling

## Integration with Existing Plugins

This plugin complements (does not duplicate):
- `golang-orchestrator:backend-service-patterns` - Go handler/service/repo patterns
- `supabase:laneweaver-database-design` - Database conventions
- `svelte5-runes` - Svelte 5 reactivity patterns
- `goth-oauth` - OAuth authentication foundation

## Usage

Skills are invoked automatically based on their descriptions. Agents are invoked when context isolation is needed.

```
/plugin install laneweaver-tms-agents@linehaulai-claude-marketplace
```
