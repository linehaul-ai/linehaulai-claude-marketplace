---
name: block-kit
description: |
  Comprehensive Slack Block Kit reference for building interactive messages, modals, and home tabs. Use when creating Slack app UI, composing rich messages, building modal workflows, or designing interactive components.
  Triggers: "slack blocks", "block kit", "slack message", "slack modal", "interactive message", "slack ui", "slack components", "slack button", "slack form"
---

# Slack Block Kit Reference

Block Kit is Slack's JSON-based UI framework for building visually rich and interactive messages, modals, and home tabs. Use this reference when building Slack app interfaces.

## Overview

Block Kit consists of three layers:

1. **Surfaces** - Where blocks are displayed (messages, modals, home tabs)
2. **Blocks** - Visual components that structure content
3. **Elements** - Interactive components (buttons, select menus, inputs)

**Capacity Limits**:
- Messages: Up to 50 blocks
- Modals and Home tabs: Up to 100 blocks

**Progressive Disclosure**: For detailed documentation, see the `references/` directory for comprehensive guides on blocks, components, layouts, and surfaces.

---

## Core Concepts

### Surfaces

Block Kit content appears on three types of surfaces:

- **Messages**: Channel messages, DMs, threads, ephemeral messages
- **Modals**: Focused surfaces for input collection and workflows
- **Home Tabs**: Personalized app home pages for each user

### Blocks

Blocks are container components arranged in arrays. Each message, modal, or home tab has a `blocks` array.

**Available Block Types**:

| Block Type | Description | Surfaces |
|------------|-------------|----------|
| `section` | Main content with text and optional accessory | All |
| `actions` | Container for interactive elements (buttons, selects) | All |
| `context` | Supplemental information with small text/images | All |
| `divider` | Visual separator | All |
| `header` | Large text for titles | All |
| `image` | Display images with alt text | All |
| `input` | Form fields for data collection | All |
| `file` | Display remote file information | Messages |
| `video` | Embedded video player | All |
| `rich_text` | Formatted, structured text | All |
| `markdown` | Formatted markdown text | Messages |
| `table` | Structured table data | Messages |
| `context_actions` | Contextual actions with feedback/icon buttons | Messages |

### Elements

Elements are interactive components that live inside blocks (primarily `actions` blocks or as accessories in `section` blocks).

**Common Interactive Elements**:

| Element Type | Description | Use Case |
|--------------|-------------|----------|
| `button` | Clickable button (action or URL) | Approvals, actions |
| `static_select` | Dropdown with static options | Option selection |
| `users_select` | Select from Slack users | User assignment |
| `conversations_select` | Select from channels/DMs | Channel routing |
| `channels_select` | Select from public channels | Channel selection |
| `external_select` | Options from external data | Dynamic lists |
| `datepicker` | Calendar date selection | Deadlines, dates |
| `timepicker` | Time selection | Scheduling |
| `overflow` | Compact menu for actions | More actions |
| `checkboxes` | Multiple option selection | Multi-select |
| `radio_buttons` | Single option selection | Exclusive choice |
| `plain_text_input` | Text input field | Text entry |
| `email_text_input` | Email input with validation | Email collection |
| `number_input` | Numeric input | Numbers |
| `url_text_input` | URL input with validation | Link collection |
| `feedback_buttons` | Positive/negative feedback | Quick feedback |
| `icon_button` | Icon-based action button | Compact actions |

### Composition Objects

Composition objects define text, options, and features within blocks and elements:

- **Text object**: Formatted text (`mrkdwn` or `plain_text`)
- **Option object**: Single selectable item
- **Option group object**: Grouped options in selects
- **Confirmation dialog object**: Confirmation before action
- **Conversation filter object**: Filter conversation lists
- **Dispatch action configuration**: Control when inputs trigger actions

---

## Quick Reference Tables

### Block Types Matrix

| Block | Text Support | Interactive Elements | Max Count | Common Use |
|-------|--------------|---------------------|-----------|------------|
| `section` | Yes (mrkdwn/plain_text, max 3000 chars) | 1 accessory | 50/100 | Primary content |
| `actions` | No | Up to 25 elements (5 on mobile) | 50/100 | Buttons, selects |
| `context` | Yes (max 10 elements) | Images only | 50/100 | Metadata |
| `divider` | No | No | 50/100 | Visual separator |
| `header` | Yes (plain_text only, max 150 chars) | No | 50/100 | Titles |
| `image` | No (alt_text required) | No | 50/100 | Visual content |
| `input` | No | 1 element (input type) | 100 | Form fields |

### Element Types Matrix

| Element | Compatible Blocks | Required Fields | Character Limits |
|---------|------------------|-----------------|------------------|
| `button` | section (accessory), actions | type, text, action_id | text: 75 chars |
| `static_select` | section (accessory), actions, input | type, action_id, options | option text: 75 chars |
| `datepicker` | section (accessory), actions, input | type, action_id | N/A |
| `plain_text_input` | input | type, action_id | No hard limit |
| `checkboxes` | section (accessory), actions, input | type, action_id, options | option text: 75 chars |

### Surface Comparison

| Surface | Max Blocks | Input Collection | Update Capability | Visibility |
|---------|------------|------------------|-------------------|------------|
| Messages | 50 | Via buttons/selects | Yes (via `ts`) | Channel/user |
| Modals | 100 | Via `input` blocks | Yes (push/update) | User-specific |
| Home Tabs | 100 | Via `input` blocks | Yes (publish) | User-specific |

---

## Common Patterns

### 1. Simple Message with Text

Display basic formatted content:

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Hello! This is a message with *bold* and _italic_ text."
      }
    }
  ]
}
```

### 2. Message with Button

Add an interactive button:

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Deployment Ready*\nEnvironment: Production"
      }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Deploy"
          },
          "style": "primary",
          "action_id": "deploy_action",
          "value": "prod_deploy"
        }
      ]
    }
  ]
}
```

### 3. Approval Flow with Multiple Buttons

Create approve/reject pattern:

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Pull Request #123*\nTitle: Add new feature\nAuthor: @developer"
      }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Approve"
          },
          "style": "primary",
          "action_id": "approve",
          "value": "pr_123"
        },
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Request Changes"
          },
          "action_id": "request_changes",
          "value": "pr_123"
        },
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Reject"
          },
          "style": "danger",
          "action_id": "reject",
          "value": "pr_123"
        }
      ]
    }
  ]
}
```

### 4. Form Modal for Input Collection

Collect structured data:

```json
{
  "type": "modal",
  "title": {
    "type": "plain_text",
    "text": "Create Issue"
  },
  "submit": {
    "type": "plain_text",
    "text": "Submit"
  },
  "close": {
    "type": "plain_text",
    "text": "Cancel"
  },
  "blocks": [
    {
      "type": "input",
      "block_id": "title_block",
      "element": {
        "type": "plain_text_input",
        "action_id": "title_input",
        "placeholder": {
          "type": "plain_text",
          "text": "Enter issue title"
        }
      },
      "label": {
        "type": "plain_text",
        "text": "Title"
      }
    },
    {
      "type": "input",
      "block_id": "description_block",
      "element": {
        "type": "plain_text_input",
        "action_id": "description_input",
        "multiline": true
      },
      "label": {
        "type": "plain_text",
        "text": "Description"
      },
      "optional": true
    },
    {
      "type": "input",
      "block_id": "priority_block",
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

### 5. Data Display with Context

Show structured information:

```json
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "Build #1234 Completed"
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Status:*\n:white_check_mark: Success"
        },
        {
          "type": "mrkdwn",
          "text": "*Duration:*\n2m 34s"
        },
        {
          "type": "mrkdwn",
          "text": "*Branch:*\nmain"
        },
        {
          "type": "mrkdwn",
          "text": "*Commit:*\nabc1234"
        }
      ]
    },
    {
      "type": "context",
      "elements": [
        {
          "type": "mrkdwn",
          "text": "Triggered by <@U123456> • 5 minutes ago"
        }
      ]
    }
  ]
}
```

### 6. Rich Formatting with Mrkdwn

Use Slack's markdown syntax:

```json
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "*Bold Text*\n_Italic Text_\n~Strikethrough~\n`Code`\n```Code Block```\n<https://slack.com|Link Text>\n• Bullet point\n1. Numbered list\n> Quote"
  }
}
```

**Mrkdwn Syntax Quick Reference**:
- Bold: `*text*`
- Italic: `_text_`
- Strikethrough: `~text~`
- Code: `` `code` ``
- Code block: ` ```code block``` `
- Link: `<url|text>`
- User mention: `<@USER_ID>`
- Channel mention: `<#CHANNEL_ID>`
- Bullet: `•` or `-`
- Quote: `>`

---

## Composition Best Practices

### Block Ordering Strategies

**Hero Pattern** (important information first):
1. Header block (title)
2. Section block (key information)
3. Divider
4. Additional sections

**Card Pattern** (grouped content):
1. Section with accessory button
2. Context with metadata
3. Divider
4. Repeat for additional cards

**Form Pattern** (input collection):
1. Header (form title)
2. Input blocks (fields)
3. Actions block (submit/cancel buttons)

### When to Use Which Block

- **Section**: Primary content, paragraphs, lists, data with optional button/image
- **Actions**: Multiple buttons or select menus for user actions
- **Context**: Metadata, timestamps, attribution, supplemental info
- **Header**: Page/section titles, prominent headings
- **Divider**: Separate distinct sections or cards
- **Input**: Form fields in modals or messages
- **Image**: Standalone images, charts, diagrams

### Accessibility Considerations

- Always provide `alt_text` for images
- Use `accessibility_label` for buttons when text is not descriptive
- Ensure color is not the only indicator (don't rely solely on button `style`)
- Keep text concise and scannable
- Use semantic structure (header → section → context)

### Performance Tips

- Minimize block count (50 max for messages)
- Use `fields` array in section blocks for compact two-column layout
- Lazy load large lists (use pagination)
- Cache frequently used blocks
- Update messages efficiently (use `ts` to update existing messages vs posting new)

---

## Interactive Component Basics

### Button Element

Simple clickable button for actions:

**Fields**:
- `type`: "button"
- `text`: plain_text object (max 75 chars, truncates ~30)
- `action_id`: unique identifier (max 255 chars)
- `value`: payload value (max 2000 chars)
- `style`: "primary" (green) or "danger" (red)
- `url`: external link (max 3000 chars)
- `confirm`: confirmation dialog object

**Example**:
```json
{
  "type": "button",
  "text": {
    "type": "plain_text",
    "text": "Click Me"
  },
  "style": "primary",
  "action_id": "button_click",
  "value": "button_value"
}
```

### Static Select Menu

Dropdown with predefined options:

**Fields**:
- `type`: "static_select"
- `action_id`: unique identifier
- `placeholder`: plain_text object
- `options`: array of option objects
- `initial_option`: pre-selected option

**Example**:
```json
{
  "type": "static_select",
  "placeholder": {
    "type": "plain_text",
    "text": "Select an option"
  },
  "options": [
    {
      "text": {
        "type": "plain_text",
        "text": "Option 1"
      },
      "value": "option_1"
    },
    {
      "text": {
        "type": "plain_text",
        "text": "Option 2"
      },
      "value": "option_2"
    }
  ],
  "action_id": "select_action"
}
```

### Datepicker

Calendar-based date selection:

**Example**:
```json
{
  "type": "datepicker",
  "action_id": "date_select",
  "placeholder": {
    "type": "plain_text",
    "text": "Select a date"
  },
  "initial_date": "2024-01-15"
}
```

### Overflow Menu

Compact menu for multiple options:

**Example**:
```json
{
  "type": "overflow",
  "action_id": "overflow_menu",
  "options": [
    {
      "text": {
        "type": "plain_text",
        "text": "Edit"
      },
      "value": "edit"
    },
    {
      "text": {
        "type": "plain_text",
        "text": "Delete"
      },
      "value": "delete"
    }
  ]
}
```

**For comprehensive component documentation**, see [references/interactive-components.md](references/interactive-components.md).

---

## Troubleshooting Quick Reference

### Common Validation Errors

**Missing Required Fields**:
- ❌ `{"type": "section"}` - Missing `text` or `fields`
- ✅ `{"type": "section", "text": {"type": "mrkdwn", "text": "Content"}}`

**Type Mismatches**:
- ❌ Button with mrkdwn text: `{"type": "button", "text": {"type": "mrkdwn", "text": "*Bold*"}}`
- ✅ Button with plain_text: `{"type": "button", "text": {"type": "plain_text", "text": "Bold"}}`

**Character Limit Violations**:
- Section text: 3000 chars max
- Button text: 75 chars max
- Modal title: 24 chars max
- action_id: 255 chars max
- value: 2000 chars max

**Nesting Violations**:
- ❌ Blocks cannot be nested inside blocks
- ✅ Elements can be nested in blocks (e.g., buttons in actions block)
- ❌ Too many elements in actions block (max 25, only 5 visible on mobile)

**Invalid Element Placement**:
- ❌ Button directly in `blocks` array
- ✅ Button in `actions` block or as `accessory` in `section` block

### Validation Tools

**Block Kit Builder**: https://app.slack.com/block-kit-builder
- Paste JSON and see live preview
- Get immediate validation errors
- Test interactivity
- Copy validated code

### Debugging Strategy

1. Validate JSON syntax first
2. Check all required fields are present
3. Verify text object types (mrkdwn vs plain_text)
4. Confirm character limits
5. Check block/element compatibility
6. Test in Block Kit Builder

---

## Resources

### Command Usage

Use the `/block-kit` command for guided topic exploration:
- `/block-kit` - Interactive topic menu
- `/block-kit blocks` - Block types reference
- `/block-kit components` - Interactive elements
- `/block-kit modals` - Modal patterns
- `/block-kit messages` - Message composition
- `/block-kit layout` - Composition patterns
- `/block-kit debug` - Troubleshooting

### Reference Documentation

**Detailed Guides**:
- [references/blocks.md](references/blocks.md) - Comprehensive block types documentation
- [references/interactive-components.md](references/interactive-components.md) - All interactive elements
- [references/layout-patterns.md](references/layout-patterns.md) - Composition and nesting best practices
- [references/surfaces.md](references/surfaces.md) - Messages, modals, and home tabs

### External Resources

- **Block Kit Builder**: https://app.slack.com/block-kit-builder - Visual builder and validator
- **Official Slack Documentation**: https://docs.slack.dev/reference/block-kit/
- **Block Kit Playground**: Test and validate your JSON structures

---

**Version**: 1.0.0
**Last Updated**: 2025-12-27
