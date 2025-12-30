# Slack Block Kit - Quick Start Guide

Build your first Block Kit message in 5 minutes.

## Goal

Create a simple interactive Slack message with text and buttons using Block Kit.

## Step 1: Verify Installation

```bash
/plugin list | grep block-kit
```

If not installed, see [INSTALL.md](INSTALL.md).

## Step 2: Understand Basic Structure

All Block Kit content uses this structure:

```json
{
  "blocks": [
    // Array of block objects
  ]
}
```

## Step 3: Build a Simple Message

Create a message with formatted text:

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Hello! This is your first *Block Kit* message with _formatting_."
      }
    }
  ]
}
```

**Key parts**:
- `blocks`: Array of blocks
- `type: "section"`: Most common block type
- `type: "mrkdwn"`: Supports formatting (*bold*, _italic_, etc.)

## Step 4: Add a Button

Add an interactive button:

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Deployment Ready*\nEnvironment: Production\nBranch: main"
      }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Deploy Now"
          },
          "style": "primary",
          "action_id": "deploy_button",
          "value": "prod_deploy"
        }
      ]
    }
  ]
}
```

**New additions**:
- `type: "actions"`: Container for interactive elements
- `type: "button"`: Button element
- `style: "primary"`: Green button (use `"danger"` for red)
- `action_id`: Identifier for handling clicks

## Step 5: Test in Block Kit Builder

1. Go to https://app.slack.com/block-kit-builder
2. Paste your JSON into the left panel
3. See live preview on the right
4. Click "Send to Slack" to test in your workspace

## Step 6: Create a Modal

Build a simple modal for collecting input:

```json
{
  "type": "modal",
  "title": {
    "type": "plain_text",
    "text": "Create Task"
  },
  "submit": {
    "type": "plain_text",
    "text": "Create"
  },
  "close": {
    "type": "plain_text",
    "text": "Cancel"
  },
  "blocks": [
    {
      "type": "input",
      "block_id": "task_title",
      "element": {
        "type": "plain_text_input",
        "action_id": "title_input",
        "placeholder": {
          "type": "plain_text",
          "text": "Enter task title"
        }
      },
      "label": {
        "type": "plain_text",
        "text": "Title"
      }
    },
    {
      "type": "input",
      "block_id": "task_priority",
      "element": {
        "type": "static_select",
        "action_id": "priority_select",
        "placeholder": {
          "type": "plain_text",
          "text": "Select priority"
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "High"
            },
            "value": "high"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Medium"
            },
            "value": "medium"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Low"
            },
            "value": "low"
          }
        ]
      },
      "label": {
        "type": "plain_text",
        "text": "Priority"
      }
    }
  ]
}
```

**Modal-specific**:
- `type: "modal"`: Modal surface
- `title`, `submit`, `close`: Required modal fields (max 24 chars each)
- `type: "input"`: Form input blocks
- `block_id` and `action_id`: For retrieving submitted values

## Next Steps

### Explore More Topics

```bash
/block-kit blocks        # Learn all block types
/block-kit components    # Explore interactive elements
/block-kit layout        # Composition patterns
```

### Try More Complex Patterns

**Approval Workflow**:
```bash
/block-kit messages
```
See multi-button approval patterns.

**Form Validation**:
```bash
/block-kit modals
```
Learn input validation and multi-step modals.

**Dashboards**:
```bash
/block-kit layout
```
See dashboard and metric display patterns.

### Dive into References

- [references/blocks.md](references/blocks.md) - All 11+ block types
- [references/interactive-components.md](references/interactive-components.md) - 15+ interactive elements
- [references/layout-patterns.md](references/layout-patterns.md) - Composition best practices
- [references/surfaces.md](references/surfaces.md) - Messages, modals, home tabs

### Get Help

```bash
/block-kit debug
```

Troubleshoot common errors and validation issues.

## Common Patterns Cheat Sheet

**Bold text**: `*bold*`
**Italic text**: `_italic_`
**Link**: `<https://url|Link Text>`
**User mention**: `<@USER_ID>`
**Channel mention**: `<#CHANNEL_ID>`

**Button styles**:
- `"style": "primary"` - Green
- `"style": "danger"` - Red
- No style - Default gray

**Text object types**:
- `"type": "mrkdwn"` - Supports formatting
- `"type": "plain_text"` - Plain text only (required for buttons, labels)

## You're Ready!

You now know how to:
- ✅ Create basic messages with formatting
- ✅ Add interactive buttons
- ✅ Build modals with form inputs
- ✅ Test in Block Kit Builder

Start building your Slack app interfaces with Block Kit!

---

**Need help?** Use `/block-kit` for guided assistance or ask Claude about specific Block Kit topics.
