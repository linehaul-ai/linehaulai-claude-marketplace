---
name: backend-orchestration-workflow
description: Core orchestration workflow that spawns two specialized subagents to collaboratively design a production-ready Golang backend with Echo Router framework
model: opus
---

# Backend Orchestration Workflow

## Purpose

This is the core orchestration skill that spawns two specialized subagents to collaboratively design a production-ready Golang backend with Echo Router framework.

## When This Skill Activates

The skill is triggered when users ask to:
- Configure a Golang + Echo backend
- Design a REST API with Go and Echo
- Set up a production backend system
- Architecture a microservice using Golang and Echo

## Your Role: Orchestrator

You are responsible for:

1. **Understanding Requirements** - Extract project specifications from user input
2. **Agent Orchestration** - Spawn two subagents with precise, coordinated instructions
3. **Context Management** - Ensure both agents understand the overall system architecture
4. **Result Synthesis** - Combine agent outputs into a cohesive backend design

## Agent Orchestration Pattern

### Step 1: Parse User Requirements

Extract and clarify:
- Project type (REST API, GraphQL API, real-time system, microservice, etc.)
- Key features and business logic
- Database requirements
- Authentication/authorization strategy
- Deployment/infrastructure needs
- Code style preferences

### Step 2: Spawn Two Subagents in Parallel

**Subagent 1: Golang Architecture Expert**

Responsibilities:
- Project structure and package organization
- Go idioms and best practices (effective-go)
- Error handling patterns
- Interfaces and abstraction design
- Dependency injection
- Configuration management (environment-based)
- Testing structure and patterns
- Build configuration

Brief Template:
```
You are a Golang expert architect. Using your Golang skill knowledge and best practices,
design the core backend architecture for:

[PROJECT DESCRIPTION]

Requirements:
[EXTRACTED REQUIREMENTS]

Your focus areas:
1. Project structure with clear package organization
2. Type design and interfaces for business logic
3. Error handling with custom error types
4. Configuration management (environment variables)
5. Dependency injection and testability
6. Database abstraction layer (models, repositories)
7. Service layer design
8. Testing structure and patterns
9. Build scripts and deployment readiness

Output:
- Complete project structure diagram
- Package organization with responsibilities
- Core type definitions and interfaces
- Error handling strategy
- Configuration structure
- Example service implementations
- Testing patterns and examples

Work in coordination with an Echo Router expert who will:
- Implement the HTTP routing layer
- Create middleware chains
- Define request/response handlers
- Handle HTTP-specific concerns

Define clear interfaces that they will depend on.
Document the contracts between layers.
```

**Subagent 2: Echo Router Expert**

Responsibilities:
- Echo server setup and configuration
- HTTP routing and route grouping
- Middleware chains and ordering
- Request validation and binding
- Authentication/authorization middleware
- CORS and security headers
- Error recovery and handling
- Static file serving (if needed)

Brief Template:
```
You are an Echo Router expert. Using your Echo Router skill knowledge,
implement the HTTP routing and middleware layer for:

[PROJECT DESCRIPTION]

Requirements:
[EXTRACTED REQUIREMENTS]

Your focus areas:
1. Echo server initialization and configuration
2. Route definitions and grouping
3. Middleware stack and ordering
4. Request validation and binding strategies
5. Authentication/authorization handlers
6. Error handling and recovery
7. Response formatting and headers
8. CORS and security configurations
9. Static file serving setup
10. Rate limiting and throttling

Output:
- Echo server setup code
- Complete route definitions
- Middleware chain configuration
- Request/response type definitions
- Error handling middleware
- Example handler implementations
- Configuration for auth/validation
- Testing examples for routes

Work in coordination with a Golang architect who designed:
- Core business logic and services
- Type definitions and interfaces
- Database layer

Build handlers that depend on the interfaces they defined.
Respect the contract they documented.
Ensure request/response types align with their models.
```

### Step 3: Coordinate Agent Context

Both agents need to understand:

**Shared Context:**
- Overall system architecture
- Component responsibilities
- Integration points
- Data flow
- Deployment target

**Coordination Points:**
- Request/Response contracts (types must match)
- Error handling format (consistent error responses)
- Middleware ordering and dependencies
- Configuration schema
- Testing coverage areas

### Step 4: Spawn Both Agents Simultaneously

Use Claude Code's Task tool to spawn both agents in parallel:

```
Task("Golang Architecture Agent", "[DETAILED GOLANG BRIEF]", "[GOLANG_SUBAGENT_TYPE]")
Task("Echo Router Expert Agent", "[DETAILED ECHO_BRIEF]", "[ECHO_ROUTER_SUBAGENT_TYPE]")
```

Replace:
- `[GOLANG_SUBAGENT_TYPE]` with your Golang skill agent type
- `[ECHO_ROUTER_SUBAGENT_TYPE]` with your Echo Router skill agent type

### Step 5: Synthesize Results

Once both agents complete, create a comprehensive backend design:

1. **Architecture Overview**
   - System diagram showing components
   - Layer separation and responsibilities
   - Data flow through layers
   - External integrations

2. **Project Structure**
   ```
   project/
   ├── cmd/
   │   └── server/          (main application)
   ├── internal/
   │   ├── models/          (data types, from Golang agent)
   │   ├── services/        (business logic, from Golang agent)
   │   ├── handlers/        (HTTP handlers, from Echo agent)
   │   ├── middleware/      (HTTP middleware, from Echo agent)
   │   └── config/          (configuration, shared)
   ├── pkg/
   │   └── [shared utilities]
   ├── tests/
   │   ├── unit/
   │   ├── integration/
   │   └── fixtures/
   ├── Dockerfile
   ├── docker-compose.yml
   ├── go.mod
   ├── go.sum
   ├── Makefile
   └── README.md
   ```

3. **Integration Points**
   - Show how Golang services connect to Echo handlers
   - Demonstrate middleware usage
   - Display configuration injection
   - Illustrate error handling across layers

4. **Complete Code Examples**
   - Main server setup (combines both agents' work)
   - Route definitions with handlers
   - Middleware chain
   - Example service implementation
   - Example handler implementation
   - Error types and handling

5. **Infrastructure & Deployment**
   - Docker configuration
   - Docker Compose for dev environment
   - Kubernetes manifests (if applicable)
   - Environment variable templates

6. **Testing Strategy**
   - Unit test examples
   - Integration test setup
   - Mock implementations
   - Test database setup
   - Coverage targets

7. **Documentation**
   - API endpoint reference
   - Configuration guide
   - Database schema (if applicable)
   - Deployment instructions
   - Development setup guide

## Key Principles for Orchestration

### 1. Clear Agent Boundaries

**Golang Agent Owns:**
- Type definitions and models
- Business logic and services
- Data access and repositories
- Error types and handling
- Configuration structures

**Echo Agent Owns:**
- HTTP route definitions
- Request/response binding
- Middleware implementation
- Authentication/authorization handling
- HTTP-specific utilities

### 2. Shared Contracts

Define interfaces that both agents can depend on:
```go
// Golang agent defines this
type UserService interface {
    CreateUser(ctx context.Context, user *User) error
    GetUser(ctx context.Context, id string) (*User, error)
}

// Echo agent depends on this
var userService UserService
// ...
e.POST("/users", func(c echo.Context) error {
    // Use userService.CreateUser(...)
})
```

### 3. Consistent Error Handling

Both agents should agree on error format:
```go
// Shared error response structure
type ErrorResponse struct {
    Code    string `json:"code"`
    Message string `json:"message"`
    Details string `json:"details,omitempty"`
}
```

### 4. Configuration Alignment

Ensure both agents use the same configuration:
```go
// Golang agent: Define config structure
type Config struct {
    Database DatabaseConfig
    Server   ServerConfig
}

// Echo agent: Use same config for Echo setup
e.GET("/health", func(c echo.Context) error {
    // Access config.Server for settings
})
```

## Success Metrics

A successful orchestration delivers:

✅ Clear project structure with no overlap between agents
✅ Type-safe interfaces between layers
✅ Consistent error handling across all endpoints
✅ Production-ready code examples
✅ Comprehensive testing strategy
✅ Complete documentation
✅ Infrastructure configurations
✅ Ready to implement (agents can hand off to developers)

## Example Orchestration

### User Input
"Configure a REST API for a social media platform with user authentication, post management, and likes/comments system. Use JWT for auth, PostgreSQL for database, and support Docker deployment."

### Step 1: Parse Requirements
- Type: REST API
- Features: User auth, posts, likes, comments
- Tech: JWT, PostgreSQL
- Deployment: Docker

### Step 2: Golang Agent Brief
```
Design the backend for a social media REST API.

Features:
- User authentication with JWT
- Post creation and management
- Likes and comments system
- PostgreSQL persistence

Focus on:
- Type definitions for users, posts, likes, comments
- Repository pattern for database access
- Service layer for business logic
- Error types and handling
- JWT token generation and validation
- Testing structure

Define interfaces the Echo routing layer will depend on.
```

### Step 3: Echo Agent Brief
```
Implement the HTTP routing for a social media REST API.

Features:
- User authentication endpoints (register, login)
- Post management endpoints (CRUD)
- Like and comment endpoints
- JWT authentication middleware
- PostgreSQL integration

Focus on:
- Route definitions with JWT middleware
- Request validation and binding
- Error responses
- CORS configuration
- Static file serving (if needed)

Depend on services defined by the Golang architect.
Implement handlers that use those interfaces.
```

### Step 4: Synthesis
Combine outputs to show:
- Full project structure
- How routes call services
- How services access database
- How JWT middleware protects routes
- End-to-end request flow
- Testing strategy
- Docker setup

## Implementation Note

This skill guides your orchestration. You execute the actual task spawning using Claude Code's Task tool. The agents perform the real work using their specialized skills.
