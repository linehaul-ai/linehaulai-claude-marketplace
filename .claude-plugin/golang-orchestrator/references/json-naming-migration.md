# JSON Naming Convention Migration Guide

## Overview

This guide helps developers migrate existing Go/Echo APIs from `snake_case` JSON field names to `camelCase` naming conventions. This change improves compatibility with JavaScript/TypeScript frontends and aligns with industry standards for REST APIs.

## Why Migrate to camelCase?

### Industry Standard
- **JavaScript/TypeScript conventions**: camelCase is the idiomatic naming convention for JavaScript objects
- **REST API best practices**: camelCase is recommended in major frameworks (Express, NestJS, Spring Boot)
- **Developer experience**: Frontends work with camelCase natively, reducing friction and transformation logic

### Code Quality
- **Reduced boilerplate**: Eliminates the need for JSON transformers or custom serializers
- **Type safety**: Removes mismatch between database schemas and API contracts
- **Consistency**: Frontend code follows JavaScript conventions, backend follows Go conventions

### Examples of the Change
```go
// Before (snake_case)
type User struct {
    FirstName string `json:"first_name"`
    LastName  string `json:"last_name"`
    Email     string `json:"email"`
}

// After (camelCase)
type User struct {
    FirstName string `json:"firstName"`
    LastName  string `json:"lastName"`
    Email     string `json:"email"`
}
```

## Migration Strategies

### Strategy 1: Breaking Change (Clean Slate)
**Best for**: New projects or major version releases

- Migrate all structs at once
- Update API version (e.g., `/api/v2`)
- Communicate clearly with API consumers
- Provide migration timeline (e.g., 3 months deprecation)
- Implement new endpoints alongside old ones during transition

**Pros**: Clean, no legacy code
**Cons**: Requires all clients to update simultaneously

**Implementation Timeline**:
1. Week 1-2: Create new endpoints with camelCase
2. Week 3-4: Deprecate old endpoints
3. Month 2-3: Support both versions
4. Month 4: Remove snake_case endpoints

### Strategy 2: Gradual Migration (Per-Endpoint)
**Best for**: Large codebases with many API consumers

- Migrate endpoints incrementally
- Run snake_case and camelCase endpoints in parallel
- Move to camelCase when stable
- Retire snake_case endpoints last

**Pros**: Minimizes disruption, allows staggered client updates
**Cons**: More code maintenance during transition

**Implementation Example**:
```go
// Old endpoint (snake_case)
router.GET("/users/:id", getUser) // returns snake_case

// New endpoint (camelCase)
router.GET("/v1/users/:id", getUserV1) // returns camelCase

// In getUser handler - transform to camelCase for new clients if header present
if req.Header.Get("Accept-Format") == "camelCase" {
    return transformToJSON(user) // handles field name transformation
}
```

### Strategy 3: Versioned API (Recommended)
**Best for**: Production systems with established API contracts

- Create new API version (v1.0, v2.0)
- Implement version negotiation via header or URL path
- Support multiple versions for extended period
- Document deprecation schedule

**Pros**: Clear separation, explicit versioning, easy rollback
**Cons**: More server-side complexity

**Implementation Example**:
```go
// Version detection
func getAPIVersion(c echo.Context) string {
    version := c.QueryParam("api_version")
    if version == "" {
        version = c.Request().Header.Get("API-Version")
    }
    if version == "" {
        version = "v1" // default
    }
    return version
}

// Handler with version-aware response
func GetUser(c echo.Context) error {
    user := &User{...}
    version := getAPIVersion(c)

    if version == "v2" {
        return c.JSON(200, user) // uses camelCase tags
    }
    return c.JSON(200, transform.ToSnakeCase(user)) // legacy
}
```

## Database vs JSON Distinction

### Key Principle
Database naming and JSON naming are independent concerns:

**Database layer** (PostgreSQL): Use `snake_case` for tables, columns, functions
- Follows SQL conventions
- Consistent with PostgreSQL documentation
- Database tools expect snake_case

**API/JSON layer**: Use `camelCase` in JSON responses
- JavaScript conventions
- HTTP API standards
- Frontend expectations

**Go struct layer**: Use PascalCase for exported fields
- Go conventions
- Database field mapping via tags
- JSON serialization tags separate from field names

### Example: Complete Layer Stack

```go
// Database: snake_case
CREATE TABLE users (
    id UUID PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email_address VARCHAR UNIQUE NOT NULL,
    phone_number VARCHAR,
    created_at TIMESTAMP DEFAULT NOW()
);

// Go struct: PascalCase + tags
type User struct {
    ID        uuid.UUID `json:"id" db:"id"`
    FirstName string    `json:"firstName" db:"first_name"`
    LastName  string    `json:"lastName" db:"last_name"`
    Email     string    `json:"email" db:"email_address"`
    Phone     string    `json:"phone" db:"phone_number"`
    CreatedAt time.Time `json:"createdAt" db:"created_at"`
}

// JSON output: camelCase
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "phone": "+1-555-0100",
    "createdAt": "2024-01-15T10:30:00Z"
}

// SQL query: snake_case
SELECT id, first_name, last_name, email_address, phone_number, created_at
FROM users WHERE id = $1;
```

## Frontend Changes Needed

### JavaScript/TypeScript
Transform API responses to match camelCase:

**Before** (manual transformation):
```typescript
interface User {
  firstName: string;
  lastName: string;
  email: string;
}

const response = await fetch('/api/users/123');
const data = response.json(); // receives { first_name, last_name, email }

// Manual transformation
const user: User = {
  firstName: data.first_name,
  lastName: data.last_name,
  email: data.email
};
```

**After** (direct usage):
```typescript
interface User {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
}

const response = await fetch('/api/v1/users/123');
const user: User = await response.json(); // directly matches interface
```

### Axios Interceptor for Automatic Transformation
If you need to support both naming conventions:

```typescript
import axios from 'axios';

// Transform response keys from camelCase to snake_case if needed
function transformKeys(obj: any, transformation: 'toSnake' | 'toCamel'): any {
  if (obj === null || typeof obj !== 'object') return obj;

  if (Array.isArray(obj)) {
    return obj.map(item => transformKeys(item, transformation));
  }

  const transformed: any = {};
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      const newKey = transformation === 'toSnake'
        ? key.replace(/([A-Z])/g, '_$1').toLowerCase()
        : key.replace(/_([a-z])/g, (_, char) => char.toUpperCase());
      transformed[newKey] = transformKeys(obj[key], transformation);
    }
  }
  return transformed;
}

// Create axios instance with transformation
const api = axios.create({
  baseURL: '/api/v1',
  transformResponse: [
    (data) => {
      try {
        const parsed = JSON.parse(data);
        return transformKeys(parsed, 'toCamel');
      } catch {
        return data;
      }
    }
  ]
});
```

### SvelteKit/Svelte Example
```svelte
<script lang="ts">
  import { onMount } from 'svelte';

  interface User {
    id: string;
    firstName: string;
    lastName: string;
    email: string;
  }

  let user: User | null = null;

  onMount(async () => {
    const response = await fetch('/api/v1/users/123');
    user = await response.json();
  });
</script>

{#if user}
  <h1>{user.firstName} {user.lastName}</h1>
  <p>{user.email}</p>
{/if}
```

## Query Parameter Conventions

### Recommendation: Keep Query Parameters in snake_case
Query parameters follow form-data conventions, traditionally snake_case:

```
GET /api/v1/users?page=1&page_size=10&sort_by=created_at&sort_order=desc
```

**Reason**: Query parameters are often generated programmatically and match HTML form conventions.

### Alternative: camelCase Query Parameters
If preferring consistency with JSON response:

```
GET /api/v1/users?page=1&pageSize=10&sortBy=createdAt&sortOrder=desc
```

**Recommendation**: Choose one convention and document it clearly. Most APIs use snake_case for query parameters.

### Go Handler Implementation
```go
type ListUserFilter struct {
    Page     int    `query:"page"`
    PageSize int    `query:"page_size"` // snake_case in URL
    SortBy   string `query:"sort_by"`
    SortOrder string `query:"sort_order"`
}

func ListUsers(c echo.Context) error {
    var filter ListUserFilter
    c.Bind(&filter)

    users, err := svc.ListUsers(c.Request().Context(), filter)
    if err != nil {
        return c.JSON(400, ErrorResponse{Message: err.Error()})
    }

    // JSON response uses camelCase
    return c.JSON(200, users) // serialized with camelCase tags
}
```

## Conversion Reference Table

| Database Column | Go Field | JSON Field | Query Param |
|---|---|---|---|
| `id` | `ID` | `id` | `id` |
| `first_name` | `FirstName` | `firstName` | `first_name` |
| `last_name` | `LastName` | `lastName` | `last_name` |
| `email_address` | `Email` | `email` | `email_address` |
| `phone_number` | `Phone` | `phone` | `phone_number` |
| `user_role` | `Role` | `role` | `user_role` |
| `is_active` | `IsActive` | `isActive` | `is_active` |
| `created_at` | `CreatedAt` | `createdAt` | `created_at` |
| `updated_at` | `UpdatedAt` | `updatedAt` | `updated_at` |
| `last_login_at` | `LastLoginAt` | `lastLoginAt` | `last_login_at` |
| `organization_id` | `OrganizationID` | `organizationId` | `organization_id` |
| `parent_entity_id` | `ParentEntityID` | `parentEntityId` | `parent_entity_id` |

## Automated Refactoring Tips

### Go Struct Tag Migration
Use regular expressions to batch update JSON tags:

**VS Code Find and Replace**:
```
Find:  `json:"([a-z_]+)"`
Replace: `json:"$1"` with transform function
```

Or use a Go script:

```go
package main

import (
    "fmt"
    "regexp"
    "strings"
)

func snakeToCamel(s string) string {
    parts := strings.Split(s, "_")
    for i := 1; i < len(parts); i++ {
        parts[i] = strings.ToUpper(parts[i][:1]) + parts[i][1:]
    }
    return strings.Join(parts, "")
}

func migrateJSONTag(input string) string {
    re := regexp.MustCompile(`json:"([a-z_]+)"`)
    return re.ReplaceAllStringFunc(input, func(match string) string {
        parts := re.FindStringSubmatch(match)
        original := parts[1]
        camel := snakeToCamel(original)
        return fmt.Sprintf(`json:"%s"`, camel)
    })
}

func main() {
    example := `type User struct {
        FirstName string json:"first_name"
        LastName  string json:"last_name"
        Email     string json:"email"
    }`

    fmt.Println(migrateJSONTag(example))
}
```

### Database Migration (PostgreSQL)
Create a comprehensive migration that adds views/functions:

```sql
-- Create migration file: migrations/20240115_add_camelcase_aliases.sql

-- Add comment documenting API change
COMMENT ON TABLE users IS 'API returns camelCase JSON via application layer';

-- If using Supabase/PostgREST, document in schema comments
ALTER TABLE users ALTER COLUMN first_name SET COMMENT 'Returns as firstName in JSON API';

-- For direct API generation, use PostgREST views with renamed columns
CREATE OR REPLACE VIEW users_api AS
SELECT
    id,
    first_name as "firstName",
    last_name as "lastName",
    email_address as "email",
    phone_number as "phone",
    created_at as "createdAt",
    updated_at as "updatedAt"
FROM users;
```

### Grep/Sed Batch Updates
Find all struct definitions and review:

```bash
# Find all JSON tags with snake_case
grep -r 'json:"[a-z_]*_[a-z_]*"' ./internal --include="*.go"

# Use sed for bulk replacement (Unix/Mac)
sed -i '' 's/json:"\([a-z]*\)_\([a-z]*\)"/json:"\1\U\2"/g' ./internal/**/*.go
```

## Implementation Checklist

- [ ] **Identify affected endpoints**: List all API routes returning JSON
- [ ] **Choose migration strategy**: Breaking change, gradual, or versioned
- [ ] **Update struct tags**: Convert JSON tags to camelCase
- [ ] **Update handlers**: Verify serialization behavior
- [ ] **Test serialization**: Run unit tests on JSON output
- [ ] **Update API documentation**: Document new JSON format
- [ ] **Create database migration**: Document schema mapping
- [ ] **Update frontend code**: Transform API integrations
- [ ] **Communication plan**: Notify API consumers
- [ ] **Monitor transition**: Track client adoption of new format
- [ ] **Deprecation timeline**: Plan removal of legacy endpoints

## Troubleshooting

### Issue: "Unexpected field in JSON"
**Cause**: Request body uses camelCase but Go struct expects different casing
**Solution**: Ensure request binding respects JSON tags on struct fields

```go
type CreateUserRequest struct {
    FirstName string `json:"firstName"`
    LastName  string `json:"lastName"`
}
```

### Issue: Database queries failing after migration
**Cause**: SQL queries using old field names while struct tags changed
**Solution**: Keep database schema unchanged; only change JSON tags
```go
// Database: first_name
// Struct DB tag: db:"first_name"
// Struct JSON tag: json:"firstName"
type User struct {
    FirstName string `json:"firstName" db:"first_name"`
}
```

### Issue: Tests failing with unexpected JSON structure
**Cause**: Tests expecting snake_case but now receiving camelCase
**Solution**: Update test fixtures and assertions
```go
// Before
assert.Equal(t, user["first_name"], "John")

// After
assert.Equal(t, user["firstName"], "John")
```

## References

- [Go JSON tag documentation](https://golang.org/pkg/encoding/json/)
- [Echo framework JSON binding](https://echo.labstack.com/docs/binding)
- [REST API Naming Conventions](https://restfulapi.net/resource-naming/)
- [Google JSON Style Guide](https://google.github.io/styleguide/jsoncpp.html)
- [JavaScript Naming Conventions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide#naming_conventions)
