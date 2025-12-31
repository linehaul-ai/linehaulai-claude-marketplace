---
name: laneweaverTMS-feature-workflow
description: Step-by-step guide for implementing new features in laneweaverTMS, orchestrating use of specialized skills and agents for database, backend, and frontend work.
---

# laneweaverTMS Feature Workflow

An orchestration guide for implementing end-to-end features in laneweaverTMS. This skill coordinates other skills and agents rather than duplicating their content.

## When to Use This Skill

Use when:
- Implementing a new feature that spans multiple layers (database, backend, frontend)
- Adding a new entity/resource to the system
- Planning feature implementation order
- Deciding which skills or agents to invoke

## Pre-Implementation Checklist

Before writing any code, ensure:

| Requirement | Questions to Answer |
|-------------|---------------------|
| **Feature Requirements** | What does the user story say? What are the acceptance criteria? |
| **Database Schema** | New tables needed? New columns on existing tables? New ENUMs? |
| **API Endpoints** | What REST endpoints are needed? Request/response shapes? |
| **Frontend Components** | New pages? New components? Which existing patterns apply? |
| **Domain Knowledge** | Any freight-specific terminology or business logic involved? |

## Step-by-Step Implementation Workflow

### Step 1: Database Schema (If Changes Needed)

**When**: New tables, columns, ENUMs, or constraints required.

**How to Execute**:
1. Invoke `schema-migration-agent` for database work
   - Isolates the 500KB erd.sql context
   - Generates migration files in `supabase/migrations/`
2. Use `supabase:laneweaver-database-design` skill for conventions

**Output**: Migration file(s) in `supabase/migrations/`

**Key Conventions** (see `supabase:laneweaver-database-design` for details):
- UUID primary keys (except users table)
- Required audit columns: `created_at`, `updated_at`, `created_by`, `updated_by`, `deleted_at`, `deleted_by`
- Soft deletes via `deleted_at` column
- Manual FK indexes (PostgreSQL does not auto-index)

---

### Step 2: Models (/internal/models/)

**When**: Always, for any new entity or DTO.

**How to Execute**:
1. Use `golang-orchestrator:backend-service-patterns` skill
2. Create Go structs with proper tags

**Pattern**:
```go
type MyEntity struct {
    ID        string     `db:"id" json:"id"`
    Name      string     `db:"name" json:"name"`
    Status    MyStatus   `db:"status" json:"status"`

    // Audit fields (always include)
    CreatedAt time.Time  `db:"created_at" json:"createdAt"`
    UpdatedAt time.Time  `db:"updated_at" json:"updatedAt"`
    CreatedBy *int32     `db:"created_by" json:"createdBy,omitempty"`
    UpdatedBy *int32     `db:"updated_by" json:"updatedBy,omitempty"`
    DeletedAt *time.Time `db:"deleted_at" json:"deletedAt,omitempty"`
}
```

**Output**: Model file in `/internal/models/`

---

### Step 3: Repository (/internal/repository/)

**When**: Always, for any new entity.

**How to Execute**:
1. Use `golang-orchestrator:backend-service-patterns` skill
2. Implement SQL queries with soft delete handling

**Key Requirements**:
- All queries include `WHERE deleted_at IS NULL`
- Use transactions for multi-table operations
- Use QueryBuilder for complex filters
- Handle `pgx.ErrNoRows` for not-found cases

**Output**: Repository file in `/internal/repository/`

---

### Step 4: Service (/internal/services/)

**When**: Always, for any new entity or business operation.

**How to Execute**:
1. Use `golang-orchestrator:backend-service-patterns` skill
2. Implement business logic and validation

**Key Requirements**:
- Validate requests at method start
- Return `ValidationErrors` for business rule failures
- Orchestrate multiple repositories as needed
- Use `context.Context` throughout

**Output**: Service file in `/internal/services/`

---

### Step 5: Handler (/internal/handlers/)

**When**: Always, for any new API endpoint.

**How to Execute**:
1. Use `golang-orchestrator:backend-service-patterns` skill
2. Implement HTTP handlers with Echo

**Key Requirements**:
- Bind request with `c.Bind()`
- Return `APIResponse` wrapper for all responses
- Add Swagger/OpenAPI annotations
- Type-assert `ValidationErrors` for 400 responses

**Output**: Handler file in `/internal/handlers/`

---

### Step 6: Router (/internal/router/)

**When**: Always, for any new endpoint.

**How to Execute**:
1. Register endpoints in `Setup` function
2. Follow RESTful conventions

**Pattern**:
```go
// In router/router.go Setup function
myEntities := api.Group("/my-entities")
myEntities.GET("", myEntityHandler.List)
myEntities.POST("", myEntityHandler.Create)
myEntities.GET("/:id", myEntityHandler.GetByID)
myEntities.PUT("/:id", myEntityHandler.Update)
myEntities.DELETE("/:id", myEntityHandler.Delete)
```

**Output**: Updated `/internal/router/router.go`

---

### Step 7: Frontend (If UI Needed)

**When**: Feature requires user-facing components.

**How to Execute**:
1. Invoke `frontend-component-agent` for Svelte work
   - Isolates frontend context (different mental model from Go)
   - Knows Svelte 5, SvelteKit, shadcn-svelte patterns
2. Use `svelte5-runes` skill for reactivity patterns
3. Use `shadcn-svelte-skill` for UI components

**Output**: Svelte components in frontend project

---

## Skill Reference Matrix

Choose the right skill for each concern:

| Concern | Skill to Use |
|---------|--------------|
| Database tables, migrations, indexes | `supabase:laneweaver-database-design` |
| Row-level security policies | `supabase:supabase-rls-policy` |
| Go handlers, services, repositories | `golang-orchestrator:backend-service-patterns` |
| Go idioms and best practices | `golang-orchestrator:effective-go` |
| Echo router and middleware | `golang-orchestrator:echo-router-skill` |
| Svelte 5 reactivity ($state, $derived) | `svelte5-runes` |
| UI components (buttons, forms, dialogs) | `shadcn-svelte-skill` |
| Freight industry terminology | `freight-domain-glossary` |
| Load status lifecycle | `load-lifecycle-patterns` |

## Agent Reference Matrix

Use agents for context isolation:

| Agent | When to Use | Why Isolate? |
|-------|-------------|--------------|
| `schema-migration-agent` | Database schema work | Isolates 500KB erd.sql from main context |
| `frontend-component-agent` | Svelte component work | Different mental model (reactive vs imperative) |

## Implementation Order Rules

1. **Database first**: Schema changes must exist before Go code references them
2. **Models before repository**: Structs must exist before SQL mapping
3. **Repository before service**: Data access before business logic
4. **Service before handler**: Business logic before HTTP layer
5. **Handler before router**: Handler must exist before route registration
6. **Backend before frontend**: API must exist before UI calls it

## Common Feature Patterns

### Adding a New Entity (CRUD)

```
1. schema-migration-agent → Create table + indexes
2. /internal/models/ → Entity struct + DTOs
3. /internal/repository/ → CRUD queries
4. /internal/services/ → Business logic + validation
5. /internal/handlers/ → HTTP handlers
6. /internal/router/ → Route registration
7. frontend-component-agent → List page + form (if UI needed)
```

### Adding a Field to Existing Entity

```
1. schema-migration-agent → ALTER TABLE + index (if needed)
2. /internal/models/ → Add field to struct
3. /internal/repository/ → Update queries
4. /internal/handlers/ → Update DTOs (if exposed via API)
```

### Adding a Status Workflow

```
1. schema-migration-agent → Create ENUM + add column
2. /internal/models/ → Define enum constants + validation
3. /internal/services/ → Implement state machine logic
4. Use load-lifecycle-patterns skill for reference
```

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Do This Instead |
|--------------|--------------|-----------------|
| Skipping database migration | Go code references non-existent columns | Always start with schema |
| Business logic in handlers | Untestable, duplicated code | Move logic to services |
| Raw SQL strings everywhere | SQL injection, hard to maintain | Use parameterized queries |
| Ignoring soft deletes | Orphaned data, broken queries | Always check `deleted_at IS NULL` |
| Frontend before API | UI calls non-existent endpoints | Build API first |

## Quick Decision Guide

```
Need database changes? → schema-migration-agent + supabase:laneweaver-database-design
Need Go backend code? → golang-orchestrator:backend-service-patterns
Need frontend UI? → frontend-component-agent + svelte5-runes + shadcn-svelte-skill
Unclear on freight terms? → freight-domain-glossary
Implementing load states? → load-lifecycle-patterns
```

---

**Remember**: This skill orchestrates other skills. When you need implementation details, invoke the appropriate specialized skill rather than trying to implement from memory.
