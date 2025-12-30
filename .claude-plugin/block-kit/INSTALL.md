# Slack Block Kit Plugin - Installation Guide

Complete installation guide for the Slack Block Kit plugin.

## Prerequisites

- **Claude Code CLI** installed and configured
- Basic understanding of JSON and Slack apps
- (Optional) Slack app for testing Block Kit examples

## Installation Methods

### Method 1: From Marketplace (Recommended)

**Step 1**: Add the marketplace

```bash
/plugin marketplace add /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace
```

**Step 2**: Install the plugin

```bash
/plugin install block-kit
```

**Step 3**: Verify installation

```bash
/plugin list | grep block-kit
```

You should see:
```
block-kit@1.0.0 - Comprehensive Slack Block Kit reference...
```

### Method 2: From Local Directory (Development)

For plugin development or local testing:

```bash
# Clone or navigate to plugin directory
cd /path/to/block-kit

# Run Claude Code with plugin directory
cc --plugin-dir .
```

## Verification Steps

### 1. Check Plugin List

```bash
/plugin list
```

Look for `block-kit` in the output.

### 2. Test Main Command

```bash
/block-kit
```

Should display interactive topic menu.

### 3. Test Specific Topic

```bash
/block-kit blocks
```

Should display block types reference with examples.

### 4. Verify Skill Access

Ask Claude:
```
"Help me create a Slack message with blocks"
```

The response should reference Block Kit skill and provide code examples.

## Troubleshooting

### Marketplace Not Found

**Error**: `Marketplace not found`

**Solution**:
- Verify marketplace path is correct
- Ensure you have read access to the marketplace directory
- Try absolute path instead of relative path

### Plugin Not Found

**Error**: `Plugin 'block-kit' not found in marketplace`

**Solution**:
- Check that `block-kit` entry exists in `marketplace.json`
- Verify plugin directory exists at `.claude-plugin/block-kit/`
- Refresh marketplace: `/plugin marketplace refresh`

### Command Not Recognized

**Error**: `/block-kit: command not found`

**Solution**:
- Verify plugin is installed: `/plugin list`
- Restart Claude Code CLI
- Reinstall plugin: `/plugin uninstall block-kit` then `/plugin install block-kit`

### Skill Not Available

**Error**: Block Kit skill doesn't activate

**Solution**:
- Check that `SKILL.md` exists in plugin directory
- Verify skill frontmatter is correctly formatted
- Try using explicit trigger phrases: "slack blocks", "block kit", "slack message"

### Permission Denied

**Error**: Permission denied accessing plugin files

**Solution**:
- Check file permissions: `ls -la .claude-plugin/block-kit/`
- Ensure files are readable: `chmod +r .claude-plugin/block-kit/*`
- Run Claude Code with appropriate permissions

## Updating the Plugin

To update to the latest version:

```bash
# Pull latest changes (if using git)
cd /path/to/marketplace
git pull

# Reinstall plugin
/plugin uninstall block-kit
/plugin install block-kit
```

## Uninstalling the Plugin

To remove the plugin:

```bash
/plugin uninstall block-kit
```

## Next Steps

After successful installation:

1. **Quick Start**: Read [QUICK_START.md](QUICK_START.md) to build your first Block Kit message
2. **Explore Topics**: Try different `/block-kit [topic]` commands
3. **Review Examples**: Check [references/](references/) for detailed documentation
4. **Test in Block Kit Builder**: Use https://app.slack.com/block-kit-builder to test your JSON

## Need Help?

- Review [PLUGIN_OVERVIEW.md](PLUGIN_OVERVIEW.md) for architecture details
- Check [README.md](README.md) for usage examples
- Use `/block-kit debug` for troubleshooting guidance
- Report issues via Claude Code marketplace

---

**Installation complete!** Start building with `/block-kit` or ask Claude about Block Kit topics.
