---
name: backend-setup-orchestration
description: Detailed orchestration command for two-agent collaborative backend configuration with Golang and Echo Router
---

# Backend Setup Orchestration Command

You are the orchestrator for a two-agent collaborative backend configuration system.

## Your Mission

Parse user requirements and spawn two specialized subagents to collaboratively design a production-ready Golang backend with Echo routing framework.

## Processing Steps

### 1. Extract Requirements from User Input

Analyze the user's description to identify:

**Project Scope**
- [ ] Project type (REST API, GraphQL, WebSocket server, microservice, etc.)
- [ ] Primary features and functionality
- [ ] Business domain and context

**Technical Specifications**
- [ ] Database requirements (PostgreSQL, MongoDB, MySQL, etc.)
- [ ] Authentication method (JWT, OAuth2, sessions, API keys)
- [ ] Caching strategy (Redis, in-memory, etc.)
- [ ] External integrations (payment gateways, APIs, messaging)

**Infrastructure & Deployment**
- [ ] Deployment target (Docker, Kubernetes, cloud platform)
- [ ] Scaling considerations
- [ ] Monitoring and logging requirements
- [ ] Environment configuration needs

**Code Quality & Architecture**
- [ ] Architectural style preference (layered, hexagonal, DDD, clean architecture)
- [ ] Code organization preferences
- [ ] Testing requirements (unit, integration, e2e coverage)
- [ ] Performance constraints

**Security Requirements**
- [ ] Authorization model (RBAC, ABAC, custom)
- [ ] Security headers needed
- [ ] Rate limiting requirements
- [ ] CORS requirements

### 2. Create Context Document

Internally organize the requirements:

```
PROJECT: [Name/Description]
TYPE: [REST API / GraphQL / WebSocket / etc.]

FEATURES:
- [Feature 1]
- [Feature 2]
- [Feature 3]

TECHNICAL STACK:
- Database: [Type]
- Auth: [Method]
- Caching: [Strategy]
- Messaging: [If applicable]

ARCHITECTURE:
- Style: [Preference]
- Layers: [Database/Service/Handler]
- Integration Points: [External systems]

DEPLOYMENT:
- Target: [Docker/K8s/Cloud]
- Environment: [Dev/Staging/Prod config]

SPECIAL REQUIREMENTS:
- [Requirement 1]
- [Requirement 2]
```

### 3. Craft Golang Agent Brief

Create a detailed prompt for the Golang expert:

```
You are a Golang expert architect. Use the `effective-go` skill to apply Go best practices as you
design the backend architecture for a [PROJECT_TYPE]:

PROJECT CONTEXT:
[PROJECT DESCRIPTION]

KEY FEATURES:
[List main features]

REQUIREMENTS:
[Technical requirements]

YOUR RESPONSIBILITIES:

Architecture & Structure:
- Design project structure with clear package organization
- Follow Go best practices and idioms
- Create appropriate interfaces for testability
- Design error types and handling strategy

Core Implementation:
- Define data models and types
- Design service layer interfaces
- Plan repository/data access patterns
- Create configuration management

Integration Points:
- Document interfaces that the HTTP layer will depend on
- Define error response contracts
- Specify configuration injection points
- Clarify middleware dependencies

Testing & Quality:
- Outline unit testing strategy
- Design for testability and dependency injection
- Provide testing examples
- Document test coverage expectations

Deliverables:
1. Complete project structure diagram
2. Package organization with clear responsibilities
3. Type definitions and core interfaces
4. Error handling strategy and error types
5. Configuration structure and management
6. Example service implementations
7. Testing patterns and setup guide
8. Build configuration (go.mod setup, build scripts)

IMPORTANT COORDINATION NOTES:
Your peer agent is an Echo Router expert who will:
- Implement all HTTP routing and endpoints
- Create middleware for authentication/authorization
- Handle request validation and response formatting
- Implement HTTP-specific error handling

Define CLEAR INTERFACES that they will depend on.
Document the CONTRACT between your service layer and their HTTP handlers.
Ensure your error types are compatible with their response formatters.
Make sure configuration is injectable and shared.

Do NOT implement HTTP handlers - that's the Echo agent's responsibility.
Do NOT use Echo types in your service interfaces.
Focus on pure business logic and data access.
```

### 4. Craft Echo Router Agent Brief

Create a detailed prompt for the Echo expert:

```
You are an Echo Router expert. Use the `echo-router-skill` skill to implement production-ready
HTTP routing and middleware layer for a [PROJECT_TYPE]:

PROJECT CONTEXT:
[PROJECT DESCRIPTION]

KEY FEATURES:
[List main features]

REQUIREMENTS:
[Technical requirements]

YOUR RESPONSIBILITIES:

Server Setup & Configuration:
- Initialize Echo server with appropriate configuration
- Set up middleware chain in correct order
- Configure CORS, security headers, and timeouts
- Implement graceful shutdown

Routing & Handlers:
- Define all HTTP routes for features
- Implement route grouping and versioning
- Create request validation and binding
- Implement proper error responses

Middleware Implementation:
- Implement authentication/authorization middleware
- Create logging and recovery middleware
- Add rate limiting middleware (if needed)
- Implement request/response formatting

Request/Response Handling:
- Define request DTOs matching service contracts
- Define response DTOs for clients
- Implement consistent error response format
- Handle content negotiation

Deliverables:
1. Echo server initialization code
2. Complete route definitions with descriptions
3. Middleware configuration and chain
4. Request validation and binding setup
5. Error handling and recovery middleware
6. Example handler implementations
7. CORS and security configuration
8. Testing examples for HTTP handlers

IMPORTANT COORDINATION NOTES:
Your peer agent is a Golang architect who designed:
- Core business logic and service interfaces
- Data models and types
- Error types and handling
- Configuration structures

DEPEND ON THEIR INTERFACES - don't reimplement logic.
MATCH THEIR TYPE CONTRACTS - use same models for requests/responses.
RESPECT THEIR ERROR TYPES - convert them to HTTP responses.
USE THEIR CONFIGURATION - inject config for Echo settings.

Do NOT implement business logic - that's the Golang agent's responsibility.
Do NOT define types that conflict with their models.
Focus on HTTP concerns: routing, middleware, request/response formatting.

Your handlers should call into their service interfaces.
Your responses should use their types directly (with adapters if needed).
Your error handling should understand their error types.
```

### 5. Spawn Agents in Parallel

Use the Task tool to spawn both agents simultaneously with full context:

```
[SINGLE MESSAGE - PARALLEL EXECUTION]

Task("Golang Architecture Agent", "[GOLANG_BRIEF_FROM_STEP_3]", "general-purpose")
Task("Echo Router Expert Agent", "[ECHO_BRIEF_FROM_STEP_4]", "general-purpose")

TodoWrite { todos: [
  {content: "Golang agent designing architecture", status: "in_progress"},
  {content: "Echo agent implementing routing", status: "in_progress"},
  {content: "Synthesize both outputs into unified design", status: "pending"},
  {content: "Create integration examples", status: "pending"},
  {content: "Verify completeness and consistency", status: "pending"}
]}
```

**Important Notes:**
- Both agents have access to their specialized skills: `golang-expert` uses `effective-go` skill, `echo-router-expert` uses `echo-router-skill`
- Spawn in PARALLEL in a single message (multiple Task calls)
- Each agent references their skill (e.g., "Use the effective-go skill to architect...")
- Both agents receive the full project context from Steps 1-4
- No dependencies between agents - they work simultaneously

### 6. Synthesize Results

Once both agents complete, create a comprehensive backend design that shows:

**Unified Architecture Diagram**
- Show data flow from Echo routes through services to database
- Illustrate middleware chain
- Display configuration injection
- Highlight error handling flow

**Complete Project Structure**
```
[project-name]/
├── cmd/
│   └── server/
│       └── main.go                 # Application entry point
├── internal/
│   ├── models/                      # Types from Golang agent
│   │   ├── user.go
│   │   ├── post.go
│   │   └── types.go
│   ├── services/                    # Services from Golang agent
│   │   ├── user_service.go
│   │   ├── post_service.go
│   │   └── interfaces.go
│   ├── handlers/                    # Handlers from Echo agent
│   │   ├── user_handler.go
│   │   ├── post_handler.go
│   │   └── response.go
│   ├── middleware/                  # Middleware from Echo agent
│   │   ├── auth.go
│   │   ├── error_handler.go
│   │   └── logging.go
│   ├── repository/                  # Data access from Golang agent
│   │   ├── user_repo.go
│   │   ├── post_repo.go
│   │   └── database.go
│   └── config/                      # Config from both agents
│       ├── config.go
│       └── env.go
├── pkg/                             # Shared utilities
│   └── errors/
├── tests/                           # Test structure from both
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── migrations/                      # Database migrations
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── go.mod
├── go.sum
└── README.md
```

**Integration Example Code**
Show how all pieces connect:
```go
// main.go - orchestrates both agents' work
func main() {
    // Load config (both agents use this)
    cfg := config.Load()

    // Initialize database (from Golang agent)
    db := database.Connect(cfg.Database)

    // Create repository and service (Golang agent)
    userRepo := repository.NewUserRepository(db)
    userService := services.NewUserService(userRepo)

    // Create Echo server and handlers (Echo agent)
    e := echo.New()

    // Register middleware (Echo agent)
    e.Use(middleware.Logger())
    e.Use(middleware.ErrorHandler())

    // Create handler with service dependency (both agents)
    userHandler := handlers.NewUserHandler(userService)

    // Register routes (Echo agent, uses Golang agent's service)
    e.POST("/users", userHandler.CreateUser)
    e.GET("/users/:id", userHandler.GetUser)

    // Start server
    e.Logger.Fatal(e.Start(cfg.Server.Address))
}
```

**Data Flow Documentation**
```
HTTP Request
    ↓
Echo Route Handler (Echo agent)
    ↓
Request Validation (Echo agent)
    ↓
Handler calls Service Interface (Golang agent)
    ↓
Service implements business logic (Golang agent)
    ↓
Service calls Repository Interface (Golang agent)
    ↓
Repository queries database (Golang agent)
    ↓
Service returns result or error (Golang agent)
    ↓
Handler formats response or error (Echo agent)
    ↓
HTTP Response
```

**Type Contract Examples**
```go
// Models defined by Golang agent
type User struct {
    ID        string
    Name      string
    Email     string
    CreatedAt time.Time
}

type UserService interface {
    CreateUser(ctx context.Context, user *User) error
    GetUser(ctx context.Context, id string) (*User, error)
}

// Request/Response types used by Echo agent
type CreateUserRequest struct {
    Name  string `json:"name" validate:"required"`
    Email string `json:"email" validate:"required,email"`
}

type UserResponse struct {
    ID        string    `json:"id"`
    Name      string    `json:"name"`
    Email     string    `json:"email"`
    CreatedAt time.Time `json:"created_at"`
}

// Handler implementation (Echo agent) depends on Golang agent's service
func (h *UserHandler) CreateUser(c echo.Context) error {
    var req CreateUserRequest
    if err := c.BindJSON(&req); err != nil {
        return echo.NewHTTPError(http.StatusBadRequest, err.Error())
    }

    user := &User{
        ID:    uuid.New().String(),
        Name:  req.Name,
        Email: req.Email,
    }

    if err := h.service.CreateUser(c.Request().Context(), user); err != nil {
        // Handle error from service (Golang agent)
        return h.formatError(err)
    }

    return c.JSON(http.StatusCreated, &UserResponse{
        ID:        user.ID,
        Name:      user.Name,
        Email:     user.Email,
        CreatedAt: user.CreatedAt,
    })
}
```

**Testing Strategy**
```
Unit Tests (Golang agent focus):
- Service logic tests (mock repository)
- Repository tests (with test database)
- Error handling tests

Integration Tests (both agents):
- End-to-end HTTP requests
- Database interactions
- Middleware behavior
- Authentication flows

Test Coverage Targets:
- Services: 80%+
- Handlers: 70%+
- Middleware: 90%+
```

**Deployment Configuration**
```dockerfile
# Dockerfile from both agents
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o server cmd/server/main.go

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/server .
EXPOSE 8080
CMD ["./server"]
```

### 7. Deliver Complete Backend Design

Present final deliverables:
1. ✅ Architecture overview with diagrams
2. ✅ Project structure ready to implement
3. ✅ Type definitions and interfaces (Golang agent)
4. ✅ Route definitions and handlers (Echo agent)
5. ✅ Example implementations showing integration
6. ✅ Testing strategy and patterns
7. ✅ Configuration management approach
8. ✅ Docker and deployment setup
9. ✅ Development quick-start guide
10. ✅ API documentation structure

## Command Format

Users invoke this via:

```
/backend-setup [Requirements description]
```

Or:

```
/backend-setup Configure a REST API for [project description] with [features] using Golang and Echo Router
```

## Success Criteria

You have successfully orchestrated when delivering:

- ✅ Clear separation of concerns between agents
- ✅ Type-safe interfaces between layers
- ✅ Consistent error handling across all endpoints
- ✅ Production-ready code examples
- ✅ Comprehensive testing strategy
- ✅ Complete project structure
- ✅ Infrastructure configs (Docker, etc.)
- ✅ Development setup instructions
- ✅ Ready for implementation by developers

## Key Reminders

1. **Always spawn BOTH agents in PARALLEL** - Don't wait for one to finish before starting the other
2. **Use TodoWrite to track coordination** - Mark progress for clarity
3. **Provide DETAILED briefs** - More context = better specialized outputs
4. **Define CLEAR CONTRACTS** - Type definitions and interfaces must align
5. **Synthesize completely** - Show how both pieces integrate, not just separate outputs
