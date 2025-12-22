# Adding to Dotfiles

This guide explains how to integrate the Golang Echo Orchestrator plugin into your `fakebizprez/dotfiles` repository.

## Directory Structure

Add the plugin to your dotfiles in this structure:

```
dotfiles/
├── .claude/
│   ├── plugins/
│   │   └── golang-echo-orchestrator/
│   │       ├── .claude-plugin/
│   │       │   ├── plugin.json
│   │       │   └── marketplace.json
│   │       ├── skills/
│   │       │   ├── effective-go/
│   │       │   │   └── SKILL.md
│   │       │   ├── backend-service-patterns/
│   │       │   │   └── SKILL.md
│   │       │   └── echo-router-skill/
│   │       │       └── SKILL.md
│   │       ├── README.md
│   │       ├── INSTALL.md
│   │       ├── QUICK_START.md
│   │       ├── NEXT_STEPS.md
│   │       ├── DEPLOYMENT_CHECKLIST.md
│   │       └── DOTFILES_SETUP.md
```

## Steps to Add to Dotfiles

### 1. Copy Plugin to Dotfiles

```bash
# Copy the entire plugin directory
cp -r /Users/fakebizprez/Developer/projects/golang-echo-orchestrator \
    /path/to/dotfiles/.claude/plugins/golang-echo-orchestrator
```

### 2. Update Git

```bash
cd /path/to/dotfiles
git add .claude/plugins/golang-echo-orchestrator/
git commit -m "Add golang-echo-orchestrator plugin for Golang/Echo backend coordination"
git push origin main
```

### 3. Tag Release (Optional)

```bash
# Create a semantic version tag
git tag plugins/golang-echo-orchestrator/v1.0.0
git push origin plugins/golang-echo-orchestrator/v1.0.0
```

## Installation from Dotfiles

Once in your dotfiles repo, users (including yourself on other machines) can install with:

```bash
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

## Marketplace Configuration (Optional)

If you have multiple plugins in your dotfiles, create a `.claude-plugin/marketplace.json` at the dotfiles root:

```json
{
  "name": "fakebizprez-tools",
  "owner": {
    "name": "fakebizprez"
  },
  "plugins": [
    {
      "name": "golang-echo-orchestrator",
      "source": {
        "source": "path",
        "path": "./.claude/plugins/golang-echo-orchestrator"
      },
      "version": "1.1.0",
      "description": "Expert guidance for Golang backend development with Echo Router framework, including laneweaverTMS backend patterns"
    }
  ]
}
```

Then install with:

```bash
/plugin marketplace add fakebizprez/dotfiles
/plugin install golang-echo-orchestrator
```

## Keeping Dotfiles Updated

### When You Update the Plugin

1. Make changes to the plugin locally
2. Commit and push to dotfiles
3. Optionally update version in `.claude-plugin/plugin.json`
4. Reinstall on other machines:
   ```bash
   /plugin uninstall golang-echo-orchestrator
   /plugin install golang-echo-orchestrator
   ```

### Syncing Across Machines

After pulling latest dotfiles on a new machine:

```bash
# If marketplace is configured:
/plugin install golang-echo-orchestrator

# Or if installing first time:
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

## Dotfiles Integration with Other Plugins

If you have other Claude Code plugins in dotfiles, keep them organized:

```
dotfiles/.claude/plugins/
├── golang-echo-orchestrator/
├── [other-plugin]/
└── [another-plugin]/
```

And update the marketplace.json at dotfiles root to include all plugins.

## Development Workflow

If you're actively developing the plugin:

1. **Keep local copy in dotfiles**:
   ```bash
   # Work directly in dotfiles
   cd /path/to/dotfiles/.claude/plugins/golang-echo-orchestrator
   # Make edits
   ```

2. **Test changes locally**:
   ```bash
   /plugin marketplace remove fakebizprez/dotfiles
   /plugin marketplace add /path/to/dotfiles/.claude/plugins/golang-echo-orchestrator
   /plugin install golang-echo-orchestrator@localhost
   # Restart Claude Code and test
   ```

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Update golang-echo-orchestrator: [what changed]"
   git push
   ```

4. **Install updated version**:
   ```bash
   /plugin uninstall golang-echo-orchestrator
   /plugin marketplace remove /path/to/dotfiles/.claude/plugins/golang-echo-orchestrator
   /plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
   /plugin install golang-echo-orchestrator
   ```

## Quick Reference

**Clone and setup dotfiles with this plugin:**
```bash
git clone https://github.com/fakebizprez/dotfiles.git
cd dotfiles

# Set up Claude Code plugins
/plugin marketplace add fakebizprez/dotfiles golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

**Update plugin from dotfiles:**
```bash
cd /path/to/dotfiles
git pull
/plugin uninstall golang-echo-orchestrator
/plugin install golang-echo-orchestrator
```

**Contribute improvements back to dotfiles:**
```bash
cd /path/to/dotfiles
# Make changes to .claude/plugins/golang-echo-orchestrator
git add .
git commit -m "Improve golang-echo-orchestrator plugin"
git push
```

## Support

For issues with plugin in dotfiles context:
1. Verify dotfiles repository is cloned correctly
2. Ensure Claude Code is fully restarted after installation
3. Check that all three skills are available:
   - `/effective-go` - Golang architecture guidance
   - `/backend-service-patterns` - laneweaverTMS backend patterns
   - `/echo-router-skill` - Echo routing patterns
4. Review INSTALL.md for general troubleshooting
