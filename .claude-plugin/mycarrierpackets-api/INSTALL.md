# Installation

## From Marketplace

```bash
# Add the Linehaul AI marketplace (if not already added)
/plugin marketplace add /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace

# Install the plugin
/plugin install mycarrierpackets-api
```

## Local Development

```bash
# Test with plugin directory flag
cc --plugin-dir /path/to/mycarrierpackets-api
```

## Verify Installation

```bash
# Check plugin is loaded
/help

# Look for mycarrierpackets command
/mycarrierpackets
```

## Configuration

Set environment variables for API credentials:

```bash
export MCP_USERNAME="your_integration_username"
export MCP_PASSWORD="your_integration_password"
```

Obtain credentials from:
https://mycarrierpackets.com/IntegrationTools
