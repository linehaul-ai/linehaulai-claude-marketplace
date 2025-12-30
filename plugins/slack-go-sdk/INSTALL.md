# Installation Instructions

## Add Marketplace

If you haven't already added the Linehaul AI Claude Marketplace:

```bash
/plugin marketplace add /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace
```

Or use your custom path to the marketplace repository.

## Install Plugin

```bash
/plugin install slack-go-sdk
```

## Verify Installation

Check that the plugin was installed successfully:

```bash
/plugin list
```

You should see `slack-go-sdk` in the list of installed plugins.

## Skill Availability

After installation, the following skills are available for use:

1. **slack-client-fundamentals** - Foundation skill for Slack Go SDK setup and architecture
2. **slack-web-api** - Web API operations (messaging, channels, users, files)
3. **slack-realtime-events** - Socket Mode and Events API patterns
4. **slack-auth-security** - OAuth flows and token management

## Test Skill Access

Ask Claude about Slack Go SDK topics to verify skills are working:

```
"How do I initialize a Slack client in Go?"
"Show me how to send a message with the Slack Go SDK"
"How do I handle Slack events with Socket Mode?"
"How do I implement OAuth for my Slack app?"
```

## Troubleshooting

### Plugin Not Found

If you receive a "plugin not found" error:

1. Verify marketplace path is correct
2. Ensure you've added the marketplace with `/plugin marketplace add`
3. Check that `slack-go-sdk` exists in `.claude-plugin/` directory

### Skills Not Triggering

If skills don't activate when asking questions:

1. Use specific trigger phrases from skill descriptions
2. Check plugin is enabled: `/plugin list`
3. Try reinstalling: `/plugin uninstall slack-go-sdk` then `/plugin install slack-go-sdk`

### Reference Documentation Not Loading

Reference files are located in `.claude-plugin/slack-go-sdk/references/`. Ensure:

1. All reference files were installed correctly
2. File permissions allow reading
3. Path references in skills are correct

## Uninstall

To remove the plugin:

```bash
/plugin uninstall slack-go-sdk
```

## Update Plugin

To update to the latest version:

```bash
/plugin update slack-go-sdk
```

Or reinstall:

```bash
/plugin uninstall slack-go-sdk
/plugin install slack-go-sdk
```

## Next Steps

- Read [README.md](README.md) for plugin overview
- Follow [QUICK_START.md](QUICK_START.md) for hands-on tutorial
- See [PLUGIN_OVERVIEW.md](PLUGIN_OVERVIEW.md) for architecture details
