# Golang Echo Orchestrator Plugin - Complete Overview

## Executive Summary

This Claude Code plugin provides comprehensive guidance for building production-ready Golang backends using the Echo Router framework.

**What it does**: Offers two expert-level skills for Golang architecture and Echo routing patterns, plus reference documentation.

**Where to use it**: In Claude Code CLI or IDE when designing Golang backends and implementing HTTP routing.

**Installation**: `https://github.com/fakebizprez/dotfiles`

---

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Plugin Name** | `golang-echo-orchestrator` |
| **Version** | 1.0.0 |
| **Purpose** | Provide expert guidance for Golang + Echo Router development |
| **Install From** | `fakebizprez/dotfiles` (GitHub) |
| **Prerequisites** | Claude Code |
| **Install Command** | `/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator` |
| **Activation** | `/plugin install golang-echo-orchestrator` |
| **Available Skills** | `/effective-go` and `/echo-router-skill` |

---

## How It Works

```
Your Development Task
      ↓
Ask /effective-go OR /echo-router-skill
      ↓
Receive Expert Guidance
      ↓
Apply to Your Project
```

---

## Plugin Components

### Skills

**`effective-go`** - Golang Best Practices & Architecture
- **Based on**: golang.org/doc/effective_go
- **Use for**:
  - Project structure and package organization
  - Error handling patterns
  - Configuration management
  - Concurrency and goroutines
  - Testing strategies
  - Dependency injection
  - Code style decisions

**`echo-router-skill`** - Echo Framework HTTP Patterns
- **Based on**: Echo v4 framework best practices
- **Use for**:
  - Server setup and initialization
  - Route definitions and organization
  - Middleware chains and ordering
  - Request validation and binding
  - Authentication/authorization patterns
  - Error handling in HTTP context
  - Security headers and CORS

---

## What You'll Receive

When using the skills, you get:

### Architecture & Design Guidance
- Project structure recommendations
- Package organization patterns
- Layer separation strategies
- Component responsibilities
- Integration patterns

### Implementation Patterns
- Code examples and snippets
- Best practice demonstrations
- Common pitfall warnings
- Alternative approaches
- Trade-off explanations

### Best Practice References
- Go idiomatic patterns
- Echo framework conventions
- Testing strategies
- Configuration approaches
- Error handling patterns

---

## Installation & Usage

### For New Machines (From Dotfiles)

```bash
# Add marketplace
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator

# Install plugin
/plugin install golang-echo-orchestrator

# Restart Claude Code
```

### For Development (From Local)

```bash
# Add local marketplace
/plugin marketplace add /Users/fakebizprez/Developer/projects/golang-echo-orchestrator

# Install dev version
/plugin install golang-echo-orchestrator@golang-echo-dev

# Restart Claude Code
```

### Using the Skills

**Direct Skill Call**
```
/effective-go How should I organize packages for a REST API backend?
```

**Or Ask Directly**
```
Using the Golang skill, help me design the project structure for a user authentication service.
```

---

## Plugin Structure

```
golang-orchestrator/
├── .claude-plugin/
│   └── plugin.json                 # Plugin manifest (required)
│
├── skills/
│   ├── effective-go/
│   │   └── SKILL.md                # Go best practices
│   └── echo-router-skill/
│       └── SKILL.md                # Echo framework patterns
│
└── Documentation/
    ├── README.md                   # Feature overview
    ├── INSTALL.md                  # Installation guide
    ├── QUICK_START.md              # 3-step quickstart
    ├── NEXT_STEPS.md               # Next steps after setup
    ├── DEPLOYMENT_CHECKLIST.md     # Deployment verification
    ├── DOTFILES_SETUP.md           # Dotfiles integration
    └── PLUGIN_OVERVIEW.md          # This file
```

---

## Key Features

### 1. Expert-Level Golang Guidance
- Implements golang.org/doc/effective_go principles
- Covers idiomatic Go patterns and conventions
- Addresses common architectural decisions
- Includes concurrency and testing patterns

### 2. Comprehensive Echo Router Patterns
- Server setup and configuration
- Complete routing and middleware guidance
- Request validation and binding
- Authentication and security patterns

### 3. Production-Ready Practices
- Error handling strategies
- Configuration management
- Testing patterns
- Docker considerations
- Deployment guidance

### 4. Flexible Development Support
- Layered architecture patterns
- Hexagonal architecture guidance
- Microservice organization
- Testing strategies
- Integration patterns

### 5. Database Agnostic
- General data access patterns
- Repository/DAO guidance
- Configuration for various databases
- Migration strategy thinking

### 6. Authentication Methods
- JWT implementation patterns
- OAuth2 flow guidance
- Session-based approaches
- API key strategies
- Security best practices

---

## Example Use Cases

### 1. Starting a New REST API Project
```
/effective-go How should I structure a REST API backend with handlers, services, and repositories?
```

### 2. Setting Up Middleware
```
/echo-router-skill How do I set up a middleware chain for authentication, logging, and error handling?
```

### 3. Error Handling Architecture
```
/effective-go What are the Go patterns for custom error types and error handling across layers?
```

### 4. Configuration Management
```
/effective-go How should I handle configuration management for environment-specific settings?
```

### 5. Testing Strategy
```
/effective-go What's a good testing strategy for a Go backend with mocks and interfaces?
```

### 6. Request Validation
```
/echo-router-skill How do I implement request validation and binding in Echo handlers?
```

---

## Customization Guide

### Architecture Styles
Request guidance for:
- Layered architecture
- Hexagonal architecture
- Domain-driven design
- Clean architecture
- Microservice architecture

### Database Integration
Ask about patterns for:
- PostgreSQL
- MySQL
- MongoDB
- Redis
- Firestore

### Authentication Methods
Get guidance on:
- JWT (bearer tokens)
- OAuth2
- Session-based
- API keys
- Multi-factor authentication

### Deployment Targets
Learn about considerations for:
- Docker containerization
- Kubernetes deployments
- AWS (ECS, Lambda)
- GCP (Cloud Run)
- Azure Container Instances

---

## Troubleshooting

### Plugin Not Appearing
```bash
/plugin list                    # Check if installed
/plugin marketplace remove ...  # Remove and retry
/plugin marketplace add ...     # Add again
/plugin install golang-echo-orchestrator
# Restart Claude Code
```

### Skills Not Available
```bash
/skill list  # Check for effective-go and echo-router-skill
# Both should be available after plugin installation
```

### Command Not Found
```bash
/plugin list  # Verify plugin installed
# Restart Claude Code if just installed
```

---

## File Reference Guide

| File | Purpose | Read When |
|------|---------|-----------|
| **README.md** | Feature overview and capabilities | First time |
| **QUICK_START.md** | Get started in 3 steps | Need quick setup |
| **INSTALL.md** | Detailed installation guide | Installation issues |
| **NEXT_STEPS.md** | Next steps after installation | Ready to continue |
| **DEPLOYMENT_CHECKLIST.md** | Verification checklist | Before deploying |
| **DOTFILES_SETUP.md** | Dotfiles integration steps | Adding to dotfiles |
| **PLUGIN_OVERVIEW.md** | This complete reference | Need full context |

---

## Architecture Patterns

### Layered Architecture
```
HTTP Handlers (Echo)
    ↓
Business Logic Services
    ↓
Data Access Repository
    ↓
Database
```

### Hexagonal (Ports & Adapters)
```
HTTP Adapter (Echo)
    ↓
Application Core (Services)
    ↓
Repository Adapter
    ↓
External Services
```

### Microservice Architecture
```
API Gateway
    ↓
Microservices (User, Order, Product, etc.)
    ↓
Shared Services (Auth, Logging)
    ↓
Databases (per service)
```

---

## Integration Examples

### Service to Handler
```go
// Service interface (from effective-go guidance)
type UserService interface {
    CreateUser(ctx context.Context, user *User) error
    GetUser(ctx context.Context, id string) (*User, error)
}

// Handler (from echo-router-skill guidance)
func (h *UserHandler) CreateUser(c echo.Context) error {
    // Call service
    h.service.CreateUser(...)
}
```

### Error Handling Flow
```go
// Error types (from effective-go guidance)
type ValidationError struct { ... }
type NotFoundError struct { ... }

// Error responses (from echo-router-skill guidance)
handler → service.Method() → returns error
    → middleware catches error type
    → converts to appropriate HTTP response
```

### Configuration Sharing
```go
// Config structure (used by both skills)
type Config struct {
    Database DatabaseConfig
    Server   ServerConfig
}

// Golang considerations: DB configuration
// Echo considerations: Server settings
```

---

## Usage Workflow

### Step 1: Architecture Planning
Ask `/effective-go` about:
- Project structure
- Package organization
- Service layer design
- Error handling strategy

### Step 2: Implementation Planning
Ask `/echo-router-skill` about:
- Server setup
- Route organization
- Middleware setup
- Request handling

### Step 3: Development
Reference both skills as you code:
- Check patterns when making decisions
- Ask for clarification if needed
- Apply best practices

### Step 4: Refinement
Iterate with more specific questions:
- Alternative patterns
- Edge cases
- Optimization strategies

---

## Best Practices

### When Using effective-go
- Be specific about your architecture style
- Ask about constraints and trade-offs
- Reference idiomatic Go patterns
- Consider testing implications

### When Using echo-router-skill
- Ask about middleware ordering
- Clarify security requirements
- Reference error handling strategies
- Consider performance implications

### Combining Both Skills
1. Design with `/effective-go`
2. Implement with `/echo-router-skill`
3. Iterate on both for refinement

---

## Advanced Usage

### Iterative Development
```
Step 1: Design basic REST API structure
Step 2: Add authentication layer
Step 3: Add database with migrations
Step 4: Add caching layer
Step 5: Add error handling
```

### Team Coordination
```
Share architectural decisions from /effective-go
Share implementation patterns from /echo-router-skill
Ensure consistency across team
```

### Multi-Service Design
```
Design user service with effective-go
Design order service with effective-go
Design how they communicate with echo-router-skill
```

---

## Support Resources

### Built-in Documentation
- All `.md` files in plugin directory
- Skill files contain detailed examples
- Command files provide guidance

### External References
- [golang.org/doc/effective_go](https://golang.org/doc/effective_go)
- [Echo Framework Documentation](https://echo.labstack.com)
- Architecture pattern resources

---

## What Makes This Plugin Different

✅ **Expert Guidance** - Based on official Go and Echo best practices
✅ **Two Complementary Skills** - Architecture (Go) + Implementation (Echo)
✅ **Production-Ready Patterns** - Real-world tested approaches
✅ **Flexible** - Supports multiple architectures and patterns
✅ **Referenced** - Clear sources for guidance (golang.org, Echo docs)
✅ **Practical** - Examples and real code patterns
✅ **Integrated** - Lives in your dotfiles for consistency

---

## Next Actions

1. **Install Plugin** - Follow INSTALL.md
2. **Try a Skill** - Use `/effective-go` or `/echo-router-skill`
3. **Build Something** - Apply guidance to your project
4. **Iterate** - Use for real projects
5. **Share** - Help your team adopt patterns

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2024 | Initial release as guidance-only skill plugin |

---

## Author & License

Created for guiding Golang and Echo Router development in Claude Code.

All documentation and structure designed to be:
- Clear and actionable
- Based on proven best practices
- Extensible
- Framework-agnostic

---

## Final Checklist

Before using in production:
- [ ] Plugin installed from dotfiles
- [ ] Both skills available (`/skill list`)
- [ ] Test with simple project first
- [ ] Understand available guidance
- [ ] Ready to implement

---

**You're all set! This plugin brings expert-level guidance for Golang and Echo Router development to Claude Code.**

For quick start, see: `QUICK_START.md`
For next steps, see: `NEXT_STEPS.md`
For full details, see: `README.md`
