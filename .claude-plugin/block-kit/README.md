# Slack Block Kit Plugin

Comprehensive Slack Block Kit reference for building interactive messages, modals, and home tabs with blocks, interactive components, and layout patterns.

## Overview

Block Kit is Slack's JSON-based UI framework for creating visually rich and interactive app interfaces. This plugin provides complete documentation, code examples, and best practices for building production Slack apps.

## What It Does

- **Block Types Reference** (11+ types): Section, actions, context, divider, header, image, input, and more
- **Interactive Components** (15+ elements): Buttons, select menus, datepickers, checkboxes, inputs
- **Layout Patterns**: Composition strategies, nesting rules, responsive design
- **Surface Documentation**: Messages, modals, and home tabs
- **Troubleshooting**: Common errors, validation, debugging strategies
- **Code Examples**: Complete, runnable JSON for every pattern

## Target Audience

- Slack app developers building interactive interfaces
- Backend engineers integrating with Slack APIs
- Integration developers creating Slack workflows

## Installation

### From Marketplace (Recommended)

```bash
# Add marketplace
/plugin marketplace add /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace

# Install plugin
/plugin install block-kit

# Verify
/plugin list | grep block-kit
```

### From Local Directory (Development)

```bash
cc --plugin-dir /path/to/block-kit
```

## Usage

### Interactive Command

Use `/block-kit` for guided topic exploration:

```bash
# Overview menu
/block-kit

# Specific topics
/block-kit blocks        # Block types reference
/block-kit components    # Interactive elements
/block-kit modals        # Modal patterns
/block-kit messages      # Message composition
/block-kit layout        # Composition patterns
/block-kit debug         # Troubleshooting
```

### Skill Access

The `block-kit` skill activates automatically when you mention Block Kit topics:

- "Help me create a Slack message with blocks"
- "How do I build a modal with form inputs?"
- "Show me button element examples"

## Features

- **Context7-Powered**: Documentation sourced from official Slack Block Kit reference
- **Production-Ready Examples**: Complete JSON that works out of the box
- **Progressive Disclosure**: Lean core skill + detailed reference files
- **Comprehensive Coverage**: All block types, elements, and composition patterns
- **Best Practices**: Layout patterns, accessibility, performance

## Available Topics

| Topic | Command | Description |
|-------|---------|-------------|
| **Blocks** | `/block-kit blocks` | All block types (section, actions, context, etc.) |
| **Components** | `/block-kit components` | Interactive elements (buttons, selects, inputs) |
| **Modals** | `/block-kit modals` | Modal structure, forms, validation |
| **Messages** | `/block-kit messages` | Message composition, updates, threading |
| **Layout** | `/block-kit layout` | Composition patterns, nesting, responsive design |
| **Debug** | `/block-kit debug` | Troubleshooting, validation, common errors |

## Example Use Cases

- **Interactive Notifications**: Approval workflows, deployment confirmations
- **Form Workflows**: Data collection, user input, multi-step processes
- **Approval Systems**: PR reviews, request approvals, voting
- **Status Dashboards**: Metrics, reports, system status
- **User Feedback**: Surveys, feedback buttons, ratings

## Documentation Files

- [INSTALL.md](INSTALL.md) - Installation and setup guide
- [QUICK_START.md](QUICK_START.md) - Build your first Block Kit message in 5 minutes
- [PLUGIN_OVERVIEW.md](PLUGIN_OVERVIEW.md) - Architecture and design principles
- [references/blocks.md](references/blocks.md) - Comprehensive block types documentation
- [references/interactive-components.md](references/interactive-components.md) - All interactive elements
- [references/layout-patterns.md](references/layout-patterns.md) - Composition best practices
- [references/surfaces.md](references/surfaces.md) - Messages, modals, home tabs

## Technical Requirements

- Claude Code CLI
- Slack app with appropriate permissions
- Access to Slack Web API (for posting messages/modals)

## Support & Resources

- **Block Kit Builder**: https://app.slack.com/block-kit-builder
- **Official Docs**: https://docs.slack.dev/reference/block-kit/
- **Plugin Issues**: Report via Claude Code marketplace

## Version

1.0.0

## Author

fakebizprez (anthony@linehaul.ai)

## Keywords

slack, block-kit, ui, messages, modals, interactive, blocks, components
