# Golang Echo Orchestrator Plugin - Complete Overview

## Executive Summary

This Claude Code plugin orchestrates two specialized subagents to collaboratively design and configure production-ready Golang backends with Echo routing framework.

**What it does**: Spawns a Golang expert and Echo Router expert that work together to generate complete backend architectures with proper separation of concerns.

**Where to use it**: In Claude Code CLI or IDE to get architecture designs for new Golang/Echo backends.

**Installation**: `https://github.com/fakebizprez/dotfiles`

---

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Plugin Name** | `golang-echo-orchestrator` |
| **Version** | 1.0.0 |
| **Purpose** | Orchestrate Golang + Echo Router subagents for backend configuration |
| **Install From** | `fakebizprez/dotfiles` (GitHub) |
| **Prerequisites** | Claude Code + Golang skill + Echo Router skill |
| **Install Command** | `/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator` |
| **Activation** | `/plugin install golang-echo-orchestrator` |
| **Output** | Complete backend design, architecture, type definitions, routes, configuration |

---

## How It Works

```
Your Requirement
      ↓
Plugin Parses Needs
      ↓
Spawns 2 Subagents (Parallel)
   ↙              ↘
Golang Agent    Echo Agent
(skill-based)   (skill-based)
   ↖              ↙
Synthesizes into Unified Design
      ↓
Complete Backend Architecture
```

### Agent Responsibilities

**Golang Agent** (uses your Golang skill)
- Project structure and organization
- Type definitions and models
- Service interfaces and business logic
- Repository/data access patterns
- Error handling strategy
- Configuration management
- Testing structure

**Echo Agent** (uses your Echo Router skill)
- HTTP server setup
- Route definitions
- Middleware chains
- Request/response handling
- Authentication/authorization
- Error recovery
- Static file serving

**Coordination**
- Shared context on requirements
- Clear type contracts
- Error handling alignment
- Configuration compatibility
- Integration patterns

---

## What You'll Receive

After running the plugin with your backend requirements, you get:

### Architecture & Design
- System architecture diagram
- Component responsibilities
- Data flow illustrations
- Integration patterns
- Deployment considerations

### Code Structure
- Complete project layout
- Package organization
- Type definitions
- Interface contracts
- Example implementations
- Integration examples

### Implementation Guidance
- Service layer patterns
- Handler implementations
- Middleware setup
- Configuration management
- Error handling across layers
- Testing strategy

### Infrastructure
- Dockerfile
- Docker Compose setup
- Environment templates
- Build scripts
- Deployment instructions

### Documentation
- API endpoint reference
- Configuration guide
- Quick-start guide
- Development setup
- Troubleshooting

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

### Using the Plugin

**Method 1: Direct Request**
```
Configure a REST API backend for a user management system using Golang and Echo Router.
Include JWT authentication, PostgreSQL, and Docker support.
```

**Method 2: Command**
```
/backend-setup Build an e-commerce REST API with product catalog, shopping cart,
and Stripe integration using Golang and Echo Router.
```

---

## Plugin Structure

```
golang-echo-orchestrator/
├── .claude-plugin/
│   ├── plugin.json                 # Plugin manifest (required)
│   └── marketplace.json            # Marketplace config (development)
│
├── agents/
│   ├── golang-expert.md                       # Golang architecture specialist
│   ├── echo-router-expert.md                  # Echo framework specialist
│   ├── golang-echo-backend-orchestrator.md    # Main orchestrator
│   └── backend-orchestration-workflow.md      # Detailed workflow
│
├── skills/
│   ├── effective-go/SKILL.md                  # Go best practices (golang.org/doc/effective_go)
│   └── echo-router-skill/SKILL.md             # Echo framework patterns and conventions
│
├── commands/
│   ├── backend-setup.md                       # Basic orchestration command
│   └── backend-setup-orchestration.md         # Detailed orchestration with checklists
│
└── Documentation/
    ├── README.md                   # Feature overview
    ├── INSTALL.md                  # Installation guide
    ├── QUICK_START.md              # 3-step quickstart
    ├── NEXT_STEPS.md               # Copy-paste commands
    ├── DOTFILES_SETUP.md           # Dotfiles integration
    ├── DEPLOYMENT_CHECKLIST.md     # Pre-deployment
    ├── PLUGIN_OVERVIEW.md          # This file
    └── QUICK_FACTS.md              # Quick reference
```

---

## Key Features

### 1. Two-Agent Orchestration
- Spawns specialized subagents in parallel
- Each uses domain-specific skill knowledge
- Agents coordinate through shared context
- Results synthesize into unified design

### 2. Type-Safe Integration
- Clear contract definitions between layers
- Type definitions that both agents understand
- Service interfaces that handlers depend on
- Consistent error handling

### 3. Production-Ready Output
- Complete project structure
- Docker support out of the box
- Testing patterns included
- Configuration management
- Security best practices
- Error handling strategies

### 4. Flexible Architecture Support
- Layered architecture
- Hexagonal architecture
- Domain-driven design
- Clean architecture
- Event-driven patterns
- Microservice patterns

### 5. Database Agnostic
- PostgreSQL, MySQL, MongoDB support
- Database abstraction layer guidance
- Migration strategy included
- ORM integration patterns

### 6. Authentication Methods
- JWT implementation
- OAuth2 patterns
- Session-based authentication
- API key authentication
- Multi-factor authentication support

---

## Example Use Cases

### 1. E-Commerce Platform
```
Configure a REST API backend for an e-commerce platform with:
- Product catalog management
- Shopping cart
- Order processing
- Stripe payment integration
- User authentication
- Inventory management
- Admin API
- PostgreSQL persistence
- Docker containerization
```

### 2. Real-Time Chat System
```
/backend-setup Build a real-time chat backend with:
- WebSocket server
- User authentication
- Message persistence (PostgreSQL)
- Room management
- Typing indicators
- Online status
- File uploads
- Production Docker setup
```

### 3. User Management Service
```
Design a user management microservice with:
- User registration and profile management
- JWT authentication
- Role-based access control
- Email verification
- Password reset functionality
- PostgreSQL with migrations
- Redis caching
- Comprehensive tests
- Docker and Kubernetes manifests
```

### 4. API Gateway
```
Create an API Gateway backend with:
- Route aggregation
- Service-to-service authentication
- Request rate limiting
- Circuit breaker patterns
- Service discovery integration
- Distributed tracing
- Prometheus metrics
- Kubernetes deployment
```

---

## Customization Guide

### Architecture Preference
Specify in requirements:
- "hexagonal architecture"
- "layered architecture"
- "DDD (domain-driven design)"
- "clean architecture"

### Database Choice
Mention in requirements:
- PostgreSQL (default)
- MySQL
- MongoDB
- DynamoDB
- Firestore

### Authentication Method
Specify in requirements:
- JWT (default)
- OAuth2
- Session-based
- API keys
- Multi-factor authentication

### Deployment Target
Include in requirements:
- Docker (default)
- Docker Compose
- Kubernetes
- AWS (ECS, Lambda)
- GCP (Cloud Run)
- Azure Container Instances

### Code Organization
Request specific patterns:
- Layered (traditional)
- Hexagonal (ports & adapters)
- DDD (domain-driven)
- Microservice-focused
- Monolithic

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
/skill list  # Check for Golang and Echo Router skills
# Both must be installed before using plugin
```

### Command Not Found
```bash
/plugin list  # Verify plugin installed
# Restart Claude Code if just installed
```

### Agents Not Spawning
- Ensure requirements are clear and specific
- Check that skills are available
- Verify Claude Code is fully restarted
- Check error messages for specific issues

---

## File Reference Guide

| File | Purpose | Read When |
|------|---------|-----------|
| **README.md** | Feature overview and capabilities | First time |
| **QUICK_START.md** | Get started in 3 steps | Need quick setup |
| **INSTALL.md** | Detailed installation guide | Installation issues |
| **NEXT_STEPS.md** | Copy-paste commands | Ready to deploy |
| **DOTFILES_SETUP.md** | Dotfiles integration steps | Adding to dotfiles |
| **DEPLOYMENT_CHECKLIST.md** | Pre-deployment verification | Before pushing to GitHub |
| **PLUGIN_OVERVIEW.md** | This complete reference | Need full context |

---

## Architecture Patterns Supported

### Layered Architecture
```
HTTP Layer (Echo)
    ↓
Service Layer (Business Logic)
    ↓
Repository Layer (Data Access)
    ↓
Database
```

### Hexagonal (Ports & Adapters)
```
HTTP Adapter (Echo)
    ↓
Application Core (Services)
    ↓
Database Adapter (Repositories)
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
Databases (Database per service)
```

---

## Integration Examples

### Service to Handler
```go
// Service interface (Golang agent)
type UserService interface {
    CreateUser(ctx context.Context, user *User) error
    GetUser(ctx context.Context, id string) (*User, error)
}

// Handler (Echo agent) depends on service
func (h *UserHandler) CreateUser(c echo.Context) error {
    // Call service
    h.service.CreateUser(...)
}
```

### Error Handling Flow
```go
// Error types (Golang agent)
type ValidationError struct { ... }
type NotFoundError struct { ... }

// Error responses (Echo agent)
handler → service.Method() → returns error
    → middleware catches error type
    → converts to appropriate HTTP response
```

### Configuration Sharing
```go
// Config structure (both agents use)
type Config struct {
    Database DatabaseConfig
    Server   ServerConfig
}

// Golang agent: uses for DB
// Echo agent: uses for server settings
```

---

## Deployment Path

1. **Develop Locally** (in `/Developer/projects/golang-echo-orchestrator`)
2. **Copy to Dotfiles** (in `~/.dotfiles/.claude/plugins/`)
3. **Push to GitHub** (in `fakebizprez/dotfiles`)
4. **Install Everywhere** (via `/plugin marketplace add ...`)
5. **Keep in Sync** (git pull + reinstall)

---

## Performance & Efficiency

### What's Fast
- Parallel agent spawning
- Single-request orchestration
- Cached skill knowledge
- Efficient context passing

### Typical Usage
1. Request takes 2-3 minutes
2. Agents work simultaneously
3. Results synthesize automatically
4. You get complete design in one interaction

---

## Advanced Usage

### Iterative Development
```
First: Build basic REST API structure
Then: Add authentication layer
Then: Add database with migrations
Then: Add caching layer
Then: Add Docker setup
```

### Team Coordination
```
Share generated architecture with team
Use as blueprint for development
Ensures consistency across microservices
```

### Multi-Service Design
```
Design user service first
Design order service
Design product service
Show how they integrate
```

---

## Support Resources

### Built-in Documentation
- All `.md` files in plugin directory
- Skill files contain detailed examples
- Command files show orchestration logic

### External References
- Claude Code official documentation
- Golang effective-go guide
- Echo framework documentation
- Architecture pattern resources

---

## What Makes This Different

✅ **Two-Agent Orchestration** - Not just code generation, but coordinated design
✅ **Skill-Based** - Uses your specialized Golang and Echo Router skills
✅ **Production-Ready** - Includes Docker, testing, configuration patterns
✅ **Type-Safe** - Enforces contracts between layers
✅ **Flexible** - Supports multiple architectures and patterns
✅ **Comprehensive** - Architecture + code structure + examples + deployment
✅ **Integrated** - Lives in your dotfiles for consistent everywhere

---

## Next Actions

1. **Copy to Dotfiles** - Follow NEXT_STEPS.md
2. **Push to GitHub** - Integrate with your dotfiles
3. **Install in Claude Code** - Make it available
4. **Test It Out** - Try a simple backend configuration
5. **Iterate** - Use for real projects

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2024 | Initial release with full orchestration |

---

## Author & License

Created for orchestrating Golang and Echo Router backends in Claude Code.

All documentation and structure designed to be:
- Clear and actionable
- Production-ready
- Extensible
- Framework-agnostic

---

## Final Checklist

Before using in production:
- [ ] Plugin installed from dotfiles
- [ ] Both required skills available (`/skill list`)
- [ ] Test with simple backend first
- [ ] Review generated architecture
- [ ] Understand integration patterns
- [ ] Ready to implement

---

**You're all set! This plugin brings expert-level backend architecture coordination to Claude Code.**

For quick start, see: `QUICK_START.md`
For setup, see: `NEXT_STEPS.md`
For full details, see: `README.md`
