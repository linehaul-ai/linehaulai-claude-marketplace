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

### 3. Start Using the Skills

```
/effective-go How should I structure a REST API backend with handlers, services, and repositories?
```

Or:

```
/echo-router-skill How do I set up middleware chains and authentication in Echo?
```

## What It Provides

Two complementary skills for Golang and Echo Router development:

**`effective-go`** - Golang Best Practices
- Project structure and package organization
- Error handling patterns
- Configuration management
- Concurrency patterns
- Testing strategies
- Dependency injection

**`echo-router-skill`** - Echo Framework Patterns
- Server setup and configuration
- Route definitions and organization
- Middleware chains
- Request validation and binding
- Authentication patterns
- Error handling and recovery

## What You Get

When using the skills, you receive:
- ✅ Architecture and design guidance
- ✅ Implementation patterns and examples
- ✅ Best practice recommendations
- ✅ Common pitfall warnings
- ✅ Code structure guidance
- ✅ Integration patterns

## File Structure Reference

```
golang-orchestrator/
├── .claude-plugin/
│   └── plugin.json                 # Plugin manifest
├── skills/
│   ├── effective-go/
│   │   └── SKILL.md                # Go best practices
│   └── echo-router-skill/
│       └── SKILL.md                # Echo routing patterns
├── README.md                        # Full documentation
├── INSTALL.md                       # Installation guide
├── PLUGIN_OVERVIEW.md              # Complete reference
└── QUICK_START.md                  # This file
```

## Key Documentation Files

| File | Purpose |
|------|---------|
| **README.md** | Feature overview and capabilities |
| **INSTALL.md** | Installation & troubleshooting |
| **PLUGIN_OVERVIEW.md** | Complete reference guide |
| **QUICK_START.md** | This quick reference |

## Troubleshooting

**Plugin not appearing after install?**
```bash
# Restart Claude Code completely
# Close and reopen the application
```

**Skills not working?**
- Check available skills: `/skill list`
- Verify effective-go and echo-router-skill are installed

**Need to reinstall?**
```bash
/plugin uninstall golang-echo-orchestrator
/plugin marketplace remove fakebizprez/dotfiles
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

## Example Usage

### Ask About Project Structure
```
/effective-go How should I structure a REST API with separate handlers, services, and repositories layers?
```

### Ask About Middleware
```
/echo-router-skill How do I set up middleware for authentication, logging, and error handling?
```

### Ask About Error Handling
```
/effective-go What patterns should I use for custom error types and error handling in a Go backend?
```

### Ask About Configuration
```
/effective-go What's the best approach for managing environment-specific configuration in Go?
```

### Ask About Testing
```
/effective-go How should I structure unit and integration tests for a Go backend?
```

## Next Steps

1. **Install Plugin** - Follow the TL;DR above
2. **Try a Skill** - Ask `/effective-go` or `/echo-router-skill` a question
3. **Reference as Needed** - Use the skills while developing
4. **Iterate** - Ask follow-up questions for clarification
5. **Build Your Project** - Apply guidance to your real projects

## How to Use These Skills

### For Architecture Planning
1. Ask `/effective-go` about project structure
2. Get guidance on package organization
3. Understand layer separation
4. Plan your design

### For Implementation
1. Ask `/echo-router-skill` about specific patterns
2. Get code examples
3. Understand middleware ordering
4. Implement with confidence

### Combining Both
1. Design architecture with `/effective-go`
2. Implement HTTP layer with `/echo-router-skill`
3. Iterate on both as needed
4. Build complete solution

## Key Concepts

### Expert Guidance
Both skills provide expert-level guidance based on:
- golang.org/doc/effective_go (Golang best practices)
- Echo v4 framework documentation (HTTP routing)

### Production-Ready Patterns
Guidance includes:
- Proper error handling
- Configuration management
- Testing structure
- Security best practices
- Concurrency patterns

### Practical Examples
Skills provide:
- Code patterns and examples
- Common pitfalls to avoid
- Alternative approaches
- Trade-off explanations

## Resources

- **Golang Documentation**: Read effective-go SKILL.md
- **Echo Documentation**: Read echo-router-skill SKILL.md
- **Installation**: Check INSTALL.md for troubleshooting
- **Complete Reference**: See PLUGIN_OVERVIEW.md
- **Setup**: See DOTFILES_SETUP.md

## Remember

This plugin provides **expert guidance**, not code generation. Use the skills to:
- Learn best practices
- Design your architecture
- Implement patterns correctly
- Make informed decisions
- Build production-ready solutions

---

**Ready to get started?** Follow the TL;DR section above!
