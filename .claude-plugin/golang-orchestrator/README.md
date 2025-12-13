# Golang Echo Orchestrator Plugin

**Orchestrate two specialized subagents to collaboratively design and configure production-ready Golang backends with Echo routing framework.**

## What This Plugin Does

This Claude Code plugin leverages subagent orchestration to create production-grade Golang backend systems. It spawns two specialized agents:

1. **Golang Expert** - Applies Golang best practices, idioms, and architectural patterns
2. **Echo Router Expert** - Specializes in Echo framework routing, middleware, and HTTP handling

These agents collaborate to deliver:
- ✅ Well-structured Go project layouts
- ✅ Type-safe routing configurations
- ✅ Professional middleware stacks
- ✅ Production-ready error handling
- ✅ Integrated testing strategies
- ✅ Docker and deployment configs
- ✅ Complete API documentation structure

## Installation

### Option 1: Install from Dotfiles (Recommended)

```bash
# From Claude Code terminal:
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

Then restart Claude Code.

### Option 2: Install from Local Directory (Development)

```bash
# From the Claude Code CLI or within Claude Code:
/plugin marketplace add /Users/fakebizprez/Developer/projects/golang-echo-orchestrator
/plugin install golang-echo-orchestrator@golang-echo-dev
```

Then restart Claude Code.

## Usage

### Method 1: Use the Skill Directly

Ask Claude Code to configure a backend:

```
Configure a production-ready REST API backend for a user management system using Golang and Echo Router.
Include JWT authentication, PostgreSQL integration, role-based access control, and Docker support.
```

The orchestrator skill will spawn both agents to collaborate.

### Method 2: Use the Command

```
/backend-setup Configure a real-time collaboration platform with WebSocket support, user authentication,
and multi-tenant database design using Golang and Echo.
```

## Plugin Components

### Agents

**`golang-expert`**
- Specializes in Go architecture and best practices (uses `effective-go` skill)
- Designs project structure, type definitions, service layers
- Defines interfaces for the HTTP layer to depend on
- Handles core business logic and data access patterns

**`echo-router-expert`**
- Specializes in Echo framework HTTP routing (uses `echo-router-skill` skill)
- Implements server setup, routes, middleware chains
- Builds HTTP handlers that call Golang agent's service interfaces
- Handles request validation, error responses, and security

### Skills

**`effective-go`**
- Go best practices from golang.org/doc/effective_go
- Used by golang-expert agent for idiomatic code decisions

**`echo-router-skill`**
- Echo v4 framework patterns and conventions
- Used by echo-router-expert agent for HTTP layer implementation

### Commands

**`/backend-setup`**
- Quick entry point for backend configuration
- Parses user requirements
- Triggers two-agent orchestration in parallel

**`/backend-setup-orchestration`**
- Detailed orchestration command with comprehensive checklists
- Structured requirement analysis
- Full agent coordination example

## Example Workflows

### Example 1: E-Commerce API

```
/backend-setup Build a production e-commerce REST API with:
- Product catalog management
- Shopping cart and order processing
- Payment gateway integration (Stripe)
- User authentication with JWT
- Admin dashboard backend
- PostgreSQL with proper indexing
- Redis caching layer
- Docker containerization
```

### Example 2: Real-Time Chat System

```
Configure a real-time messaging backend with Golang and Echo Router:
- WebSocket server for real-time messages
- User authentication and session management
- Message persistence in MongoDB
- Room-based chat organization
- Typing indicators and online status
- Media file upload handling
- Production-grade error handling
- Docker Compose setup for dev environment
```

### Example 3: Microservice Architecture

```
/backend-setup Design a microservice architecture using Golang and Echo with:
- API Gateway pattern
- Service-to-service communication
- Shared authentication service
- Event-driven updates (event bus)
- Circuit breaker patterns
- Distributed tracing setup
- Kubernetes deployment configs
- Prometheus metrics integration
```

## How Agent Orchestration Works

1. **You provide requirements** via skill or command
2. **Orchestrator parses** the requirements into structured components
3. **Two subagents spawn in parallel**:
   - Golang agent gets: architecture, structure, and core logic requirements
   - Echo agent gets: routing, middleware, and HTTP handling requirements
4. **Agents share context** through:
   - Coordinated interface definitions
   - Shared type contracts
   - Common error handling patterns
5. **Results are synthesized** into a complete, integrated backend design

## What You Get

For a typical backend configuration, you'll receive:

### Architecture & Structure
- Complete project layout
- Package organization diagram
- Dependency graph
- Layer separation strategy

### Code Examples
- Main application setup
- Route definitions with middleware
- Handler function patterns
- Model and type definitions
- Error handling utilities
- Configuration management

### Infrastructure
- Dockerfile and docker-compose.yml
- Environment configuration templates
- Database schema and migrations
- Build scripts

### Testing
- Unit test patterns
- Integration test setup
- Mock implementations
- Test coverage targets

### Documentation
- API endpoint listing
- Quick start guide
- Configuration reference
- Deployment instructions

## Plugin Structure

```
golang-echo-orchestrator/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest
│   └── marketplace.json         # Development marketplace
├── skills/
│   └── golang-echo-backend-orchestrator.md  # Orchestration skill
├── commands/
│   └── backend-setup.md         # Backend setup command
├── docs/
│   └── [additional documentation]
└── README.md                     # This file
```

## Customization

### For Different Architecture Styles

Specify your preferred architecture in requirements:
- Layered (traditional)
- Hexagonal (ports & adapters)
- DDD (domain-driven design)
- Clean Architecture
- Event-Driven Architecture

### For Different Databases

Agents support:
- PostgreSQL
- MySQL
- MongoDB
- Redis
- DynamoDB
- Firestore

### For Different Authentication Methods

- JWT (bearer tokens)
- OAuth2
- Session-based
- API keys
- Multi-factor authentication

### For Deployment Targets

- Docker/Docker Compose
- Kubernetes (Helm charts)
- AWS (ECS, Lambda)
- GCP (Cloud Run)
- Azure (Container Instances)

## Troubleshooting

### Plugin Not Loading

```bash
# Check installation
/plugin list

# Reinstall
/plugin uninstall golang-echo-orchestrator@golang-echo-dev
/plugin install golang-echo-orchestrator@golang-echo-dev

# Restart Claude Code
```

### Agents Not Spawning

Ensure your requirements are clear and specific:
- ❌ "Build a backend" (too vague)
- ✅ "Build a REST API for user management with JWT auth and PostgreSQL"

### Missing Skill Context

Make sure your Golang and Echo Router skills are properly installed and available before using this plugin.

## Advanced Usage

### Batch Multiple Configurations

Request multiple backend configurations in sequence or parallel:

```
/backend-setup First, configure the user service with authentication.
Then, configure the order service with payment processing.
Finally, design the API gateway to connect them.
```

### Incremental Development

Start with a basic configuration, then expand:

```
Initial: Basic REST API structure
Add: Authentication layer
Add: Database with migrations
Add: Caching layer
Add: Docker setup
Add: Kubernetes manifests
```

### Integration with Other Plugins

The generated code is compatible with other Claude Code plugins for:
- Testing (use testing suite plugins)
- Git workflow (use git-flow plugins)
- CI/CD (use deployment plugins)

## Contributing

To improve this plugin:

1. Test new agent briefs for better collaboration
2. Add new example workflows
3. Extend documentation
4. Submit improvements via pull request

## License

This plugin is provided as-is for use with Claude Code.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your Golang and Echo Router skills are properly installed
3. Ensure Claude Code is fully restarted after plugin installation

---

**Ready to orchestrate your backend?** Use `/backend-setup` or ask the skill directly to get started!
