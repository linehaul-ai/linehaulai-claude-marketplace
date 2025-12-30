# Slack Go SDK Plugin

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Go SDK](https://img.shields.io/badge/Go%20SDK-v0.12+-green)

## Overview

Comprehensive guidance for building Slack applications with the official Go SDK ([github.com/slack-go/slack](https://github.com/slack-go/slack)). This plugin provides expert knowledge for Web API operations, real-time event handling, OAuth flows, and security best practices.

## What's Included

- ✅ **Web API Operations**: Messages, channels, users, files
- ✅ **Socket Mode & Events API**: Real-time event handling via WebSocket and HTTP webhooks
- ✅ **OAuth Flows & Token Management**: Multi-workspace authentication and security
- ✅ **Block Kit Integration**: Rich message composition patterns
- ✅ **Production Security Practices**: Token management, request verification, deployment checklists

## Skills

### 🔧 slack-client-fundamentals
Foundation skill covering client initialization, architecture decisions, error handling, and testing strategies. Use when setting up a new Slack bot or understanding when to use Web API vs Socket Mode.

### 📤 slack-web-api
Comprehensive guidance for synchronous Slack API operations including messaging, channel management, user operations, file uploads, and Block Kit composition. Use when implementing message posting, channel creation, or any direct API calls.

### ⚡ slack-realtime-events
Real-time event handling with Socket Mode and Events API. Covers event routing, interactive components (buttons, modals), slash commands, and WebSocket connection management. Use when building interactive bots or event-driven applications.

### 🔐 slack-auth-security
OAuth 2.0 flows, token management, scopes, permissions, and security best practices. Covers multi-workspace installations, token rotation, and production deployment security. Use when implementing app distribution or managing workspace authentication.

## Quick Start

```go
package main

import (
    "fmt"
    "github.com/slack-go/slack"
)

func main() {
    // Initialize the Slack API client
    api := slack.New("xoxb-your-bot-token")

    // Send a message to a channel
    channelID := "C1234567890"
    text := "Hello from Slack Go SDK!"

    _, _, err := api.PostMessage(
        channelID,
        slack.MsgOptionText(text, false),
    )
    if err != nil {
        fmt.Printf("Error posting message: %s\n", err)
        return
    }

    fmt.Println("Message sent successfully!")
}
```

See [QUICK_START.md](QUICK_START.md) for complete setup instructions.

## Reference Documentation

18 detailed guides organized by concern in the `references/` directory:

**Core Setup** (2 guides):
- [client-configuration.md](references/client-configuration.md) - Advanced client setup, custom HTTP clients, retries
- [testing-patterns.md](references/testing-patterns.md) - Mocking strategies, integration tests

**Web API** (6 guides):
- [web-api-messaging.md](references/web-api-messaging.md) - Message posting, threading, updates
- [web-api-channels.md](references/web-api-channels.md) - Channel creation, management, metadata
- [web-api-users.md](references/web-api-users.md) - User info, presence, profiles
- [web-api-files.md](references/web-api-files.md) - File uploads, downloads, sharing
- [block-kit-integration.md](references/block-kit-integration.md) - Rich message composition
- [pagination-patterns.md](references/pagination-patterns.md) - Handling large result sets

**Real-time Events** (5 guides):
- [socket-mode-setup.md](references/socket-mode-setup.md) - WebSocket connection management
- [events-api-webhooks.md](references/events-api-webhooks.md) - HTTP webhook patterns
- [event-types.md](references/event-types.md) - Comprehensive event catalog
- [interactive-components.md](references/interactive-components.md) - Buttons, modals, shortcuts
- [slash-commands.md](references/slash-commands.md) - Command handling patterns

**Auth & Security** (5 guides):
- [oauth-flow.md](references/oauth-flow.md) - Complete OAuth implementation
- [token-management.md](references/token-management.md) - Token storage and rotation
- [scopes-permissions.md](references/scopes-permissions.md) - Scope selection guide
- [manifest-api.md](references/manifest-api.md) - Programmatic app configuration
- [security-checklist.md](references/security-checklist.md) - Production deployment security

## Prerequisites

- **Go**: Version 1.20 or later
- **Slack Workspace**: Admin access to create apps
- **Slack App**: Created in [Slack App Dashboard](https://api.slack.com/apps)

## Installation

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

```bash
# Add marketplace (if not already added)
/plugin marketplace add /path/to/linehaulai-claude-marketplace

# Install plugin
/plugin install slack-go-sdk

# Verify installation
/plugin list
```

## Plugin Architecture

See [PLUGIN_OVERVIEW.md](PLUGIN_OVERVIEW.md) for detailed architecture documentation.

```
slack-client-fundamentals (foundation)
    ↓
    ├─→ slack-web-api (synchronous operations)
    ├─→ slack-realtime-events (Socket Mode + Events API)
    └─→ slack-auth-security (OAuth + token management)
```

## Related Plugins

- **golang-orchestrator**: Go architecture best practices and idiomatic patterns
- **block-kit**: Advanced Slack UI layouts (optional enhancement)

## Resources

- [slack-go/slack GitHub Repository](https://github.com/slack-go/slack)
- [Slack API Documentation](https://api.slack.com)
- [Slack App Management Console](https://api.slack.com/apps)
- [Block Kit Builder](https://app.slack.com/block-kit-builder)

## Contributing

This plugin is part of the Linehaul AI Claude Marketplace. To suggest improvements or report issues, please contact the plugin maintainer.

## License

Copyright © 2025 Linehaul AI. All rights reserved.
