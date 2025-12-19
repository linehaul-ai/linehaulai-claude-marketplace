# Slack Block Kit Builder Plugin

Build Slack Block Kit UIs for messages, modals, and Home tabs with expert guidance.

## Features

- **Comprehensive Skill**: Complete Block Kit reference with blocks, elements, and composition objects
- **Interactive Command**: `/block-kit` command for guided UI building
- **Expert Agent**: `block-kit-expert` subagent for implementation decisions

## Installation

```bash
/plugin marketplace add /path/to/linehaulai-claude-marketplace
/plugin install slack-block-kit-builder
```

## Usage

### Using the Skill

The skill is automatically invoked when you ask about:
- Building Slack messages, modals, or Home tabs
- Block Kit blocks, elements, or composition objects
- slack-block-builder library patterns

### Using the Command

```bash
/block-kit message Create a notification for new orders
/block-kit modal Build a feedback form
/block-kit home Design a task dashboard
```

### Using the Agent

The `block-kit-expert` agent is invoked for complex decisions about:
- Multi-modal workflows
- Layout optimization
- Interaction handling patterns

## What's Included

- All 12 block types (Header, Section, Actions, Input, etc.)
- All interactive elements (Buttons, Selects, Date pickers, etc.)
- Composition objects (Text, Confirmations, Options)
- slack-block-builder library patterns
- Best practices and troubleshooting guides

## Resources

- [Slack Block Kit Builder](https://app.slack.com/block-kit-builder)
- [Slack Block Kit Docs](https://api.slack.com/block-kit)
- [slack-block-builder GitHub](https://github.com/raycharius/slack-block-builder)
