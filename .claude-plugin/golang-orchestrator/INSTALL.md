# Installation & Setup Guide

## Prerequisites

Before installing this plugin, ensure you have:

1. **Claude Code installed and running**
   ```bash
   # Verify Claude Code is available
   which claude
   ```

## Installation Steps

### Step 1: Install from Dotfiles (GitHub)

From Claude Code, add the marketplace and install:

```bash
# From Claude Code terminal:
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

Then **restart Claude Code** to activate the plugin.

### Step 1 (Alternative): Install from Local Development

If developing locally before pushing to dotfiles:

```bash
# From Claude Code terminal:
/plugin marketplace add /Users/fakebizprez/Developer/projects/golang-echo-orchestrator
/plugin install golang-echo-orchestrator@golang-echo-dev
```

Then **restart Claude Code** to activate the plugin.

### Step 2: Verify Installation

Check that the plugin loaded correctly:

```bash
/plugin list
```

You should see `golang-echo-orchestrator` in the output.

### Step 3: Verify Skills Are Available

Verify that the skills are available:

```bash
/skill list
```

You should see all three skills:
- `effective-go` - For Golang architecture guidance
- `backend-service-patterns` - For laneweaverTMS backend patterns
- `echo-router-skill` - For Echo routing patterns

## Testing the Plugin

### Test 1: Try the effective-go Skill

Ask about Golang architecture:

```
/effective-go How should I structure a REST API backend with separate layers?
```

You should receive guidance on project structure and package organization.

### Test 2: Try the backend-service-patterns Skill

Ask about backend patterns:

```
/backend-service-patterns How do I structure a service layer with pgx and PostgreSQL?
```

You should receive guidance on service layer architecture and database operations.

### Test 3: Try the echo-router-skill

Ask about Echo routing:

```
/echo-router-skill How do I set up middleware chains in Echo?
```

You should receive guidance on middleware setup and route organization.

## Troubleshooting Installation

### Plugin Not Appearing

**Problem**: `/plugin list` doesn't show `golang-echo-orchestrator`

**Solution**:
```bash
# If installing from dotfiles:
/plugin uninstall golang-echo-orchestrator
/plugin marketplace remove fakebizprez/dotfiles
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator

# If installing locally:
/plugin uninstall golang-echo-orchestrator@golang-echo-dev
/plugin marketplace remove /Users/fakebizprez/Developer/projects/golang-echo-orchestrator
/plugin marketplace add /Users/fakebizprez/Developer/projects/golang-echo-orchestrator
/plugin install golang-echo-orchestrator@golang-echo-dev

# Restart Claude Code completely
# Close and reopen Claude Code
```

### Skills Not Showing

**Problem**: Skills don't appear when you run `/skill list`

**Solution**:
1. Verify plugin is installed: `/plugin list`
2. Restart Claude Code completely
3. Run `/skill list` again
4. The skills should now be available

### Command Not Available

**Problem**: `/backend-setup` command not found

**Solution**:
1. Verify plugin is installed: `/plugin list`
2. Check that plugin is enabled (not disabled in settings)
3. Restart Claude Code
4. Try a fresh session

## Using the Skills

### Basic Usage - Ask About Architecture

```
/effective-go How should I structure a REST API backend with handlers, services, and repositories?
```

### Basic Usage - Ask About Routing

```
/echo-router-skill How do I set up middleware chains for authentication and logging?
```

### Advanced Usage - Ask About Patterns

Specify what you want to build:

```
/effective-go I'm building a microservice-oriented user service. What architecture patterns should I use?
Should I use hexagonal architecture or layered architecture?
```

### Iterative Development

Build knowledge incrementally:

```
Step 1: /effective-go How should I organize packages for a REST API?
Step 2: /echo-router-skill How do I set up my Echo server with middleware?
Step 3: /effective-go What patterns should I use for error handling?
Step 4: /echo-router-skill How do I implement request validation in Echo?
```

## Next Steps

Once installed and verified:

1. **Try the effective-go skill** with a simple question about architecture
2. **Try the echo-router-skill** with a question about routing
3. **Combine both skills** for comprehensive guidance
4. **Reference the skills** as you build your project
5. **Iterate** with more specific questions as you develop

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure Claude Code is fully restarted
3. Verify the plugin is installed: `/plugin list`
4. Verify the skills are available: `/skill list`
5. Review the plugin's README for additional context

## Uninstallation

To uninstall the plugin:

```bash
# If installed from dotfiles:
/plugin uninstall golang-echo-orchestrator
/plugin marketplace remove fakebizprez/dotfiles

# If installed locally:
/plugin uninstall golang-echo-orchestrator@golang-echo-dev
/plugin marketplace remove /Users/fakebizprez/Developer/projects/golang-echo-orchestrator
```

Restart Claude Code to complete removal.
