# Installation & Setup Guide

## Prerequisites

Before installing this plugin, ensure you have:

1. **Claude Code installed and running**
   ```bash
   # Verify Claude Code is available
   which claude
   ```

2. **Your Golang skill installed**
   - This is your custom skill for Golang best practices
   - Verify it's available: `/skill list` in Claude Code

3. **Your Echo Router skill installed**
   - This is your custom skill for Echo framework patterns
   - Verify it's available: `/skill list` in Claude Code

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

Make sure your Golang and Echo Router skills are available:

```bash
/skill list
```

Look for both skills in the list. If either is missing, add them before using the plugin.

## Testing the Plugin

### Test 1: Use the Orchestrator Skill

Try triggering the skill directly:

```
I need to configure a production REST API for a user authentication system using Golang and Echo Router.
Features: user registration, login with JWT, profile management, and role-based access control.
Database: PostgreSQL. Deployment: Docker.
```

The plugin should:
1. Parse your requirements
2. Spawn two subagents (Golang and Echo)
3. Generate coordinated architecture and code

### Test 2: Use the Command

Try the `/backend-setup` command:

```
/backend-setup Configure a real-time chat application backend with:
- User authentication and sessions
- Chat room management
- Message persistence (PostgreSQL)
- WebSocket support for real-time messages
- Production Docker setup
```

### Test 3: Verify Agent Coordination

The output should show:
- ✅ Both agents' work coordinated
- ✅ Type definitions that match between layers
- ✅ Service interfaces that handlers depend on
- ✅ Consistent error handling
- ✅ Complete project structure
- ✅ Integration examples

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

### Skills Not Found When Plugin Runs

**Problem**: Agents don't have access to Golang or Echo Router skills

**Solution**:
1. Verify your skills are installed: `/skill list`
2. Add missing skills if needed
3. Restart Claude Code
4. Try plugin again

### Command Not Available

**Problem**: `/backend-setup` command not found

**Solution**:
1. Verify plugin is installed: `/plugin list`
2. Check that plugin is enabled (not disabled in settings)
3. Restart Claude Code
4. Try a fresh session

## Configuration (Optional)

### Update Agent Type References

If your Golang and Echo Router skills have different agent types, update the plugin's command:

1. Edit `/Users/fakebizprez/Developer/projects/golang-echo-orchestrator/commands/backend-setup-orchestration.md`
2. Find the Task tool calls in Step 5
3. Replace `[YOUR_GOLANG_AGENT_TYPE]` and `[YOUR_ECHO_AGENT_TYPE]` with your actual agent type names
4. Save and restart Claude Code

Example:
```markdown
Task("Golang Architecture Agent", "[GOLANG_BRIEF]", "effective-go-architect")
Task("Echo Router Expert Agent", "[ECHO_BRIEF]", "echo-router-expert")
```

## Using the Plugin

### Basic Usage

Ask for a backend configuration:

```
Configure a REST API backend for an e-commerce platform using Golang and Echo Router.
Include product catalog, shopping cart, order processing, and Stripe payment integration.
Use PostgreSQL for persistence and Redis for caching.
Support Docker containerization.
```

### Advanced Usage

Specify architectural preferences:

```
/backend-setup Build a microservice-oriented user service using:
- Golang with hexagonal architecture
- Echo Router for HTTP interface
- PostgreSQL with schema migrations
- JWT authentication
- Comprehensive unit and integration tests
- Docker and Kubernetes manifests
```

### Iterative Development

Build backends incrementally:

```
First, configure the basic REST API structure with user management.
Then, add product catalog functionality.
Finally, add order processing and payment handling.
```

## Next Steps

Once installed and verified:

1. **Start with a simple backend** to get familiar with the output format
2. **Review the generated architecture** carefully
3. **Customize the agent briefs** if needed for your specific use case
4. **Use the generated structure** as a starting point for your implementation
5. **Iterate** with more complex requirements as you get comfortable

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Ensure Claude Code is fully restarted
4. Check that your Golang and Echo Router skills are properly installed
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
