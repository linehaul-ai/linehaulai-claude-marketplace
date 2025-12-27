# Block Kit - Block Types Reference

Comprehensive reference for all Block Kit block types. Blocks are visual components that structure content in Slack messages, modals, and home tabs.

---

## Block Types Overview

Blocks can hold text, images, or interactive elements. Each surface supports different blocks:

- **All Surfaces** (Messages, Modals, Home tabs): section, actions, context, divider, header, image, input, rich_text, video
- **Messages Only**: file, markdown, table, context_actions

---

## Section Block

The most versatile block. Displays text with optional accessory element (button, image, select menu, etc.).

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"section"` |
| `text` | object | Conditional | Text object (mrkdwn or plain_text). Max 3000 chars. Required if no `fields`. |
| `block_id` | string | No | Unique identifier. Max 255 chars. |
| `fields` | array | Conditional | Array of text objects for two-column layout. Max 10 items, 2000 chars each. Required if no `text`. |
| `accessory` | object | No | Single interactive element (button, select, image, datepicker, etc.) |
| `expand` | boolean | No | If true, text always expands. Default false. |

###Basic Example

```json
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "A message *with some bold text* and _some italicized text_."
  }
}
```

### With Accessory (Button)

```json
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "*Task Complete*\nYour deployment is ready"
  },
  "accessory": {
    "type": "button",
    "text": {
      "type": "plain_text",
      "text": "View Details"
    },
    "action_id": "view_details"
  }
}
```

### With Fields (Two-Column Layout)

```json
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "Build Information"
  },
  "fields": [
    {
      "type": "mrkdwn",
      "text": "*Status:*\nSuccess"
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
}
```

---

## Actions Block

Container for interactive elements (buttons, select menus, datepickers). Use for user actions.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"actions"` |
| `elements` | array | Yes | Array of interactive elements. Max 25 elements (5 visible on mobile). |
| `block_id` | string | No | Unique identifier. Max 255 chars. |

### With Buttons

```json
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
      "action_id": "approve_action"
    },
    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Reject"
      },
      "style": "danger",
      "action_id": "reject_action"
    }
  ]
}
```

### With Select Menu and Button

```json
{
  "type": "actions",
  "block_id": "actions1",
  "elements": [
    {
      "type": "static_select",
      "placeholder": {
        "type": "plain_text",
        "text": "Select an option"
      },
      "action_id": "select_option",
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
      ]
    },
    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Cancel"
      },
      "action_id": "cancel_button"
    }
  ]
}
```

---

## Context Block

Displays supplemental information (metadata, timestamps, attribution). Supports text and small images.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"context"` |
| `elements` | array | Yes | Array of image and text objects. Max 10 items. |
| `block_id` | string | No | Unique identifier. Max 255 chars. |

### Example

```json
{
  "type": "context",
  "elements": [
    {
      "type": "image",
      "image_url": "https://example.com/avatar.png",
      "alt_text": "user avatar"
    },
    {
      "type": "mrkdwn",
      "text": "Created by <@U123456> • 5 minutes ago"
    }
  ]
}
```

---

## Divider Block

Visual separator between blocks.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"divider"` |
| `block_id` | string | No | Unique identifier. Max 255 chars. |

### Example

```json
{
  "type": "divider"
}
```

---

## Header Block

Large text for titles and headings.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"header"` |
| `text` | object | Yes | Plain text object. Max 150 chars. |
| `block_id` | string | No | Unique identifier. Max 255 chars. |

### Example

```json
{
  "type": "header",
  "text": {
    "type": "plain_text",
    "text": "Weekly Report"
  }
}
```

---

## Image Block

Displays standalone image (not in section block).

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"image"` |
| `alt_text` | string | Yes | Plain-text summary. Max 2000 chars. |
| `image_url` | string | Conditional | Publicly hosted image URL. Max 3000 chars. Required if no `slack_file`. |
| `slack_file` | object | Conditional | Slack file object with `url` or `id`. Required if no `image_url`. |
| `title` | object | No | Plain text title. Max 2000 chars. |
| `block_id` | string | No | Unique identifier. Max 255 chars. |

### Example

```json
{
  "type": "image",
  "title": {
    "type": "plain_text",
    "text": "System Architecture"
  },
  "image_url": "https://example.com/diagram.png",
  "alt_text": "System architecture diagram"
}
```

---

## Input Block

Collects user input in modals and messages. Contains single input element.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"input"` |
| `label` | object | Yes | Plain text label. Max 2000 chars. |
| `element` | object | Yes | Input element (plain_text_input, select, datepicker, etc.) |
| `block_id` | string | No | Unique identifier. Max 255 chars. |
| `hint` | object | No | Plain text hint below input. Max 2000 chars. |
| `optional` | boolean | No | If true, field may be empty. Default false. |
| `dispatch_action` | boolean | No | If true, sends block_actions payload on interaction. Default false. |

### Plain Text Input

```json
{
  "type": "input",
  "block_id": "title_block",
  "element": {
    "type": "plain_text_input",
    "action_id": "title_input",
    "placeholder": {
      "type": "plain_text",
      "text": "Enter title"
    }
  },
  "label": {
    "type": "plain_text",
    "text": "Title"
  }
}
```

### Multiline Text Input

```json
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
}
```

### Email Input

```json
{
  "type": "input",
  "block_id": "email_block",
  "element": {
    "type": "email_text_input",
    "action_id": "email_input",
    "placeholder": {
      "type": "plain_text",
      "text": "Enter email"
    }
  },
  "label": {
    "type": "plain_text",
    "text": "Email Address"
  }
}
```

### Number Input

```json
{
  "type": "input",
  "element": {
    "type": "number_input",
    "is_decimal_allowed": false,
    "action_id": "quantity_input",
    "placeholder": {
      "type": "plain_text",
      "text": "Enter quantity"
    }
  },
  "label": {
    "type": "plain_text",
    "text": "Quantity"
  }
}
```

### URL Input

```json
{
  "type": "input",
  "element": {
    "type": "url_text_input",
    "action_id": "url_input"
  },
  "label": {
    "type": "plain_text",
    "text": "Website URL"
  }
}
```

### Select Menu Input

```json
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
```

---

## Context Actions Block

Displays feedback buttons and icon buttons as contextual info. **Messages only**.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"context_actions"` |
| `elements` | array | Yes | Array of feedback_buttons and icon_button elements. Max 5 items. |
| `block_id` | string | No | Unique identifier. Max 255 chars. |

### With Feedback Buttons

```json
{
  "type": "context_actions",
  "elements": [
    {
      "type": "feedback_buttons",
      "action_id": "feedback_1",
      "positive_button": {
        "text": {
          "type": "plain_text",
          "text": "👍"
        },
        "value": "positive"
      },
      "negative_button": {
        "text": {
          "type": "plain_text",
          "text": "👎"
        },
        "value": "negative"
      }
    }
  ]
}
```

### With Icon Button

```json
{
  "type": "context_actions",
  "elements": [
    {
      "type": "icon_button",
      "icon": "trash",
      "text": {
        "type": "plain_text",
        "text": "Delete"
      },
      "action_id": "delete_button",
      "value": "delete_item"
    }
  ]
}
```

---

## Markdown Block

Displays formatted markdown. **Messages only**. Consider using section block with mrkdwn text instead.

### Example

```json
{
  "type": "markdown",
  "text": "**Lots of information here!!**"
}
```

---

## Best Practices

### Block Ordering
1. Start with header for section titles
2. Use section blocks for main content
3. Add dividers between distinct sections
4. Place actions blocks after related content
5. End with context for metadata

### Character Limits
- Section text: 3000 chars
- Header text: 150 chars
- Fields text: 2000 chars each
- Alt text: 2000 chars
- Block_id: 255 chars

### When to Use Which Block
- **Section**: Primary content, paragraphs, data
- **Actions**: Buttons and select menus
- **Context**: Metadata, timestamps, attribution
- **Header**: Section titles
- **Divider**: Visual separation
- **Input**: Form fields (modals primarily)
- **Image**: Standalone images, charts

### Accessibility
- Always provide `alt_text` for images
- Use clear, descriptive labels for inputs
- Keep text concise and scannable
- Use semantic structure (header → section → context)

---

**Content Source**: Context7 (`/websites/slack_dev_reference_block-kit`)
