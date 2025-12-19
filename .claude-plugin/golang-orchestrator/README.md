# Golang Echo Orchestrator Plugin

**Comprehensive guidance plugin for building production-ready Golang backends with Echo Router framework.**

## What This Plugin Does

This Claude Code plugin provides expert-level guidance for Golang backend development using the Echo Router framework. It includes two complementary skills:

1. **effective-go** - Golang best practices, idioms, and architectural patterns from golang.org/doc/effective_go
2. **echo-router-skill** - Echo framework routing, middleware, and HTTP handling patterns

These skills help you build:
- ✅ Well-structured Go project layouts
- ✅ Type-safe code with idiomatic patterns
- ✅ Professional middleware stacks
- ✅ Production-ready error handling
- ✅ Integrated testing strategies
- ✅ Best practices for configuration and concurrency

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

### Using the Skills Directly

Ask Claude Code for guidance on specific topics:

**For Golang architecture and patterns:**
```
/effective-go How should I structure a typical Go backend project with proper package organization?
```

**For Echo Router HTTP implementation:**
```
/echo-router-skill How do I set up middleware chains and implement authentication in Echo?
```

### Using the Backend Setup Command

Get guidance on both skills together:

```
/backend-setup I need to build a REST API for user management. What's a good project structure?
```

## Plugin Components

### Skills

**`effective-go`** - Golang Best Practices
- Package organization and project structure
- Error handling patterns and custom error types
- Concurrency, goroutines, and parallelism
- Configuration management
- Dependency injection patterns
- Testing strategies and conventions
- Build and deployment considerations

**`echo-router-skill`** - Echo Framework Patterns
- Server setup and configuration
- Route definitions and route grouping
- Middleware chains and ordering
- Request validation and binding
- Authentication and authorization patterns
- Error handling in HTTP context
- CORS and security headers

### Commands

**`/backend-setup`**
- Overview of available skills
- Guidance on using effective-go and echo-router-skill
- Development workflow suggestions

## Example Usage Scenarios

### Building a REST API

Use `/effective-go` to plan your project structure, then `/echo-router-skill` for routing:

1. Ask about Go package organization for a typical REST API
2. Get guidance on error handling patterns
3. Ask about Echo route definitions and middleware
4. Implement authentication middleware patterns

### Setting Up Middleware

Use `/echo-router-skill` to get guidance on:
- CORS middleware setup
- Authentication middleware chains
- Request validation middleware
- Error recovery and logging

### Concurrency Patterns

Use `/effective-go` for guidance on:
- Goroutine management
- Channel patterns for communication
- Worker pool implementations
- Avoiding common concurrency pitfalls

### Database Integration

Use `/effective-go` to design your data layer, then `/echo-router-skill` for:
- Request binding and validation
- Response serialization
- Transaction handling in handlers

## What You Can Achieve

With these skills, you can:

### Architecture Planning
- Determine appropriate project structure
- Design package organization
- Plan layer separation (handlers, services, repositories)
- Define error handling strategy

### Implementation Patterns
- Set up Echo server with proper initialization
- Implement middleware chains
- Build handler functions with validation
- Create consistent error responses
- Handle authentication and authorization

### Best Practices
- Write idiomatic Go code
- Follow Go conventions and idioms
- Apply proven patterns from the Go community
- Implement proper configuration management
- Set up testable code structures

## Plugin Structure

```
golang-echo-orchestrator/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── skills/
│   ├── effective-go/
│   │   └── SKILL.md             # Go best practices skill
│   └── echo-router-skill/
│       └── SKILL.md             # Echo routing skill
├── commands/
│   └── backend-setup.md         # Backend setup guidance
├── docs/
│   └── [reference documentation]
└── README.md                     # This file
```

## Using These Skills Effectively

### Golang Design Decisions

Ask `/effective-go` when deciding on:
- **Project Structure**: Package organization for your specific use case
- **Error Handling**: How to define and handle errors consistently
- **Configuration**: Methods for managing environment-specific settings
- **Testing**: Strategies for unit and integration testing
- **Concurrency**: Goroutine patterns and channels for your workload

### Echo Implementation Decisions

Ask `/echo-router-skill` when implementing:
- **Server Setup**: Initial Echo server configuration
- **Routes**: Organizing routes for scalability
- **Middleware**: Building middleware stacks in the right order
- **Validation**: Request validation and binding strategies
- **Authentication**: Implementing auth middleware patterns
- **Error Responses**: Consistent error response formatting

## Troubleshooting

### Plugin Not Loading

```bash
# Check installation
/plugin list

# Reinstall
/plugin uninstall golang-echo-orchestrator
/plugin install golang-echo-orchestrator

# Restart Claude Code
```

### Skills Not Available

Verify the skills are properly installed:
- Run `/effective-go` to test the Golang skill
- Run `/echo-router-skill` to test the Echo skill
- If either fails, reinstall the plugin

### Getting Better Guidance

Be specific with your questions:
- ❌ "How do I structure a Go project?" (too general)
- ✅ "How should I organize a REST API backend with separate handlers, services, and repositories?" (specific)

## Tips for Using These Skills

### Combine Both Skills

Many problems benefit from guidance from both skills:

1. Ask `/effective-go` about architecture and project structure
2. Then ask `/echo-router-skill` about implementing HTTP handlers for that structure

### Reference the Skills While Implementing

Keep both skills available as you code:
- Check `/effective-go` when making design decisions
- Refer to `/echo-router-skill` when implementing handlers
- Use both for error handling patterns

### Iterate on Patterns

1. Get initial guidance from a skill
2. Implement based on that guidance
3. Ask for clarification or alternatives if needed
4. Refine your approach based on feedback

## Integration with Other Plugins

The guidance from these skills complements other Claude Code plugins:
- Git workflow plugins for version control
- Testing plugins for test implementation strategies
- Deployment plugins for containerization and orchestration

## License

This plugin is provided as-is for use with Claude Code.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your Golang and Echo Router skills are properly installed
3. Ensure Claude Code is fully restarted after plugin installation

---

**Ready to orchestrate your backend?** Use `/backend-setup` or ask the skill directly to get started!
