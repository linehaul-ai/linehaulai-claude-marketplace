# Next Steps - Copy & Paste Ready

Follow these exact commands to integrate the plugin into your dotfiles.

## Step 1: Copy to Dotfiles

Replace `/path/to/dotfiles` with your actual dotfiles directory path.

```bash
# Example: if your dotfiles is at ~/code/dotfiles
# Replace /path/to/dotfiles with ~/code/dotfiles

cp -r /Users/fakebizprez/Developer/projects/golang-echo-orchestrator \
    /path/to/dotfiles/.claude/plugins/golang-echo-orchestrator
```

**Verify the copy:**
```bash
ls -la /path/to/dotfiles/.claude/plugins/golang-echo-orchestrator/
```

You should see:
```
.claude-plugin/
DEPLOYMENT_CHECKLIST.md
DOTFILES_SETUP.md
INSTALL.md
NEXT_STEPS.md
QUICK_START.md
README.md
commands/
skills/
```

## Step 2: Commit and Push to GitHub

```bash
# Navigate to dotfiles
cd /path/to/dotfiles

# Check what will be staged
git status

# Stage the plugin
git add .claude/plugins/golang-echo-orchestrator/

# Verify staging
git status

# Commit
git commit -m "Add golang-echo-orchestrator plugin for Golang/Echo backend coordination"

# Push to GitHub
git push origin main
```

**Expected output:**
```
 create mode 100644 .claude/plugins/golang-echo-orchestrator/.claude-plugin/plugin.json
 create mode 100644 .claude/plugins/golang-echo-orchestrator/.claude-plugin/marketplace.json
 create mode 100644 .claude/plugins/golang-echo-orchestrator/skills/...
 ...
```

## Step 3: Install from Claude Code

In Claude Code terminal:

```bash
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

**Then restart Claude Code completely** (close and reopen).

## Step 4: Verify Installation

```bash
/plugin list
```

You should see:
```
golang-echo-orchestrator     v1.0.0     installed
```

## Step 5: Test It Works

In Claude Code, type:

```
Configure a production REST API for a user management system using Golang and Echo Router.
Include JWT authentication, PostgreSQL integration, role-based access control, and Docker support.
```

Or use the command:

```
/backend-setup Configure a REST API backend for a user management system using Golang and Echo Router.
```

## If Something Goes Wrong

### Plugin won't install

```bash
# Uninstall and retry
/plugin uninstall golang-echo-orchestrator

# Try again
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator

# Restart Claude Code
```

### Plugin installs but command not available

```bash
# Verify plugin loaded
/plugin list

# Make sure Golang and Echo Router skills are available
/skill list

# If skills missing, add them first
# Then restart Claude Code
```

### Skills not found during execution

```bash
# Check if skills are available
/skill list

# Must see both:
# - Your Golang skill
# - Your Echo Router skill

# If missing, install them before using the plugin
```

## Using the Plugin

### Method 1: Direct Prompt

Simply ask Claude Code to configure a backend:

```
I need a production-ready REST API for [your project description]
using Golang and Echo Router with [your requirements].
```

### Method 2: Command

Use the built-in command:

```
/backend-setup [Your backend requirements]
```

### What You'll Get

The plugin will:
1. Parse your requirements
2. Spawn two subagents in parallel:
   - **Golang Expert** - Designs architecture, services, data models
   - **Echo Router Expert** - Implements routing, middleware, handlers
3. Coordinate their outputs
4. Deliver a complete backend design with:
   - Project structure
   - Type definitions
   - Service interfaces
   - Route definitions
   - Middleware setup
   - Configuration patterns
   - Docker setup
   - Testing strategy
   - Integration examples

## Example Prompts to Try

### Simple: Basic REST API
```
Configure a REST API for a user management system with:
- User registration and login
- JWT authentication
- PostgreSQL database
- Docker support

Use Golang and Echo Router.
```

### Medium: E-Commerce Platform
```
/backend-setup Build a REST API backend for an e-commerce platform with:
- Product catalog management
- Shopping cart functionality
- Order processing
- Stripe payment integration
- User authentication with JWT
- PostgreSQL for data
- Redis for caching
- Docker containerization

Use Golang with Echo routing.
```

### Complex: Real-Time System
```
Design a production backend for a real-time chat application using Golang and Echo Router:
- WebSocket server for live messaging
- User authentication and session management
- Message persistence in PostgreSQL
- Room-based chat organization
- Typing indicators and online status
- User profile management
- Direct messaging between users
- File attachment support
- Comprehensive error handling
- Docker and docker-compose setup for development
```

## Troubleshooting Command Reference

```bash
# List installed plugins
/plugin list

# List available skills
/skill list

# Uninstall plugin
/plugin uninstall golang-echo-orchestrator

# Remove marketplace
/plugin marketplace remove fakebizprez/dotfiles

# Clean reinstall
/plugin uninstall golang-echo-orchestrator
/plugin marketplace remove fakebizprez/dotfiles
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator

# Check Claude Code installation
which claude

# Verify dotfiles plugin location
ls -la /path/to/dotfiles/.claude/plugins/golang-echo-orchestrator/
```

## File References

- **README.md** - Full feature documentation
- **INSTALL.md** - Detailed installation guide
- **QUICK_START.md** - 3-step getting started
- **DOTFILES_SETUP.md** - Dotfiles integration details
- **DEPLOYMENT_CHECKLIST.md** - Pre-deployment verification

## Next: Update Other Machines

Once your dotfiles are on GitHub, on any other machine:

```bash
# Clone dotfiles (or pull latest)
git clone https://github.com/fakebizprez/dotfiles.git
cd dotfiles

# Install the plugin
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator

# Restart Claude Code
```

The plugin is now available everywhere your dotfiles are!

## Questions?

Refer to:
1. `QUICK_START.md` - Quick overview
2. `INSTALL.md` - Installation help
3. `README.md` - Feature details
4. `DOTFILES_SETUP.md` - Dotfiles specifics

---

**You're all set! Follow the steps above and you'll have a production-ready plugin orchestrating your Golang and Echo Router backend configurations.**
