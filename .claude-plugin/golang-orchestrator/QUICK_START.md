# Quick Start Guide

## TL;DR - 3 Steps to Get Started

### 1. Push to Dotfiles

```bash
# Copy plugin to your dotfiles
cp -r /Users/fakebizprez/Developer/projects/golang-echo-orchestrator \
    /path/to/dotfiles/.claude/plugins/

# Commit and push
cd /path/to/dotfiles
git add .claude/plugins/golang-echo-orchestrator/
git commit -m "Add golang-echo-orchestrator plugin"
git push
```

### 2. Install from Claude Code

```bash
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

Restart Claude Code.

### 3. Start Using It

```
Configure a REST API backend for a user management system using Golang and Echo Router.
Include JWT authentication, PostgreSQL integration, and Docker support.
```

Or use the command:

```
/backend-setup Build an e-commerce REST API with product catalog, shopping cart,
and Stripe integration using Golang and Echo Router.
```

## What It Does

The plugin spawns two specialized subagents:
- **Golang Expert** - Designs architecture, services, data models
- **Echo Router Expert** - Implements HTTP routing, middleware, handlers

They coordinate to generate production-ready backend designs.

## What You Get

After running the plugin, you'll have:
- ✅ Complete project structure
- ✅ Type definitions and service interfaces
- ✅ Route definitions and handlers
- ✅ Configuration management
- ✅ Docker setup
- ✅ Testing strategy
- ✅ Integration examples

## File Structure Reference

```
golang-echo-orchestrator/
├── .claude-plugin/
│   ├── plugin.json           # Plugin manifest
│   └── marketplace.json      # Dev marketplace config
├── skills/
│   ├── golang-echo-backend-orchestrator.md
│   └── backend-orchestration-workflow.md
├── commands/
│   ├── backend-setup.md
│   └── backend-setup-orchestration.md
├── README.md                 # Full documentation
├── INSTALL.md                # Installation guide
├── DOTFILES_SETUP.md         # Dotfiles integration
└── QUICK_START.md           # This file
```

## Key Documentation Files

| File | Purpose |
|------|---------|
| **README.md** | Feature overview and usage |
| **INSTALL.md** | Installation & troubleshooting |
| **DOTFILES_SETUP.md** | How to add to dotfiles |
| **QUICK_START.md** | This quick reference |

## Troubleshooting

**Plugin not appearing after install?**
```bash
# Restart Claude Code completely
# Close and reopen the application
```

**Commands/skills not working?**
- Verify your Golang and Echo Router skills: `/skill list`
- Both skills must be installed before using the plugin

**Need to reinstall?**
```bash
/plugin uninstall golang-echo-orchestrator
/plugin marketplace remove fakebizprez/dotfiles
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

## Example Prompts

### Basic REST API
```
Configure a production REST API for a user authentication system using Golang and Echo Router.
Features: user registration, login with JWT, profile management, role-based access control.
Database: PostgreSQL. Deployment: Docker.
```

### E-Commerce Platform
```
/backend-setup Build a complete e-commerce backend with:
- Product catalog management
- Shopping cart
- Order processing
- Stripe payment integration
- User authentication with JWT
- Admin dashboard endpoints
- PostgreSQL with proper indexing
- Redis caching
- Docker containerization
```

### Real-Time System
```
Design a real-time chat application backend using Golang and Echo with:
- WebSocket server for live messaging
- User authentication and sessions
- Message persistence in PostgreSQL
- Room-based organization
- Typing indicators
- Media file uploads
- Production error handling
- Docker and docker-compose setup
```

## Next Steps

1. **Copy to dotfiles** - Add plugin to your GitHub dotfiles
2. **Push to GitHub** - Make it available across machines
3. **Install** - Run the installation commands above
4. **Test** - Try a simple backend configuration
5. **Review Output** - Understand the generated architecture
6. **Use as Template** - Apply to your real projects

## Key Concepts

### Agent Orchestration
Two subagents work together:
- Golang agent focuses on business logic, types, services
- Echo agent focuses on HTTP routing, middleware, handlers
- Clear contracts ensure they integrate seamlessly

### Type Safety
Both agents agree on:
- Request/response types
- Error formats
- Configuration structures
- Interface contracts

### Production Ready
Generated code includes:
- Proper error handling
- Docker support
- Testing structure
- Configuration management
- Security best practices

## Resources

- **Official Docs**: Read skill files in `./skills/` directory
- **Examples**: See `./commands/` for detailed orchestration logic
- **Troubleshooting**: Check INSTALL.md for common issues
- **Dotfiles**: See DOTFILES_SETUP.md for repository integration

## Remember

The plugin is a **design tool**, not a code generator. It provides:
- Architecture guidance
- Integration patterns
- Type structure
- Middleware setup
- Testing strategy

Use the generated design as a starting point for your implementation.

---

**Ready to get started?** Follow the TL;DR section above!
