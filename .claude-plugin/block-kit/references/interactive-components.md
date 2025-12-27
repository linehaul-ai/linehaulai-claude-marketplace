# Block Kit - Interactive Components Reference

Comprehensive reference for all Block Kit interactive elements. Elements are components that users interact with (buttons, select menus, inputs).

---

## Element Types Overview

Interactive elements live inside blocks, primarily:
- **Actions block**: Buttons, select menus, overflow menus, datepickers
- **Section block accessory**: Single element alongside text
- **Input block**: Form input elements

---

## Button Element

Clickable button for actions or URLs.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"button"` |
| `text` | object | Yes | Plain text object. Max 75 chars, truncates ~30. |
| `action_id` | string | No | Unique identifier. Max 255 chars. |
| `url` | string | No | External URL to open. Max 3000 chars. |
| `value` | string | No | Payload value. Max 2000 chars. |
| `style` | string | No | `"primary"` (green) or `"danger"` (red). |
| `confirm` | object | No | Confirmation dialog object. |
| `accessibility_label` | string | No | Screen reader label. Max 75 chars. |

### Basic Button

```json
{
  "type": "button",
  "text": {
    "type": "plain_text",
    "text": "Click Me"
  },
  "action_id": "button_click",
  "value": "button_value"
}
```

### Styled Buttons

```json
{
  "type": "button",
  "text": {
    "type": "plain_text",
    "text": "Approve"
  },
  "style": "primary",
  "action_id": "approve",
  "value": "approve_action"
}
```

```json
{
  "type": "button",
  "text": {
    "type": "plain_text",
    "text": "Delete"
  },
  "style": "danger",
  "action_id": "delete",
  "value": "delete_action"
}
```

### URL Button

```json
{
  "type": "button",
  "text": {
    "type": "plain_text",
    "text": "View Documentation"
  },
  "url": "https://docs.slack.dev/block-kit"
}
```

---

## Static Select Menu

Dropdown with predefined options.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"static_select"` |
| `action_id` | string | Yes | Unique identifier. Max 255 chars. |
| `placeholder` | object | No | Plain text placeholder. Max 150 chars. |
| `options` | array | Yes | Array of option objects. Max 100 options. |
| `option_groups` | array | No | Array of option group objects. Alternative to `options`. |
| `initial_option` | object | No | Pre-selected option. |
| `confirm` | object | No | Confirmation dialog. |
| `focus_on_load` | boolean | No | Auto-focus on load. Default false. |

### Example

```json
{
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
}
```

---

## Users Select Menu

Select from Slack workspace users.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"users_select"` |
| `action_id` | string | Yes | Unique identifier. |
| `placeholder` | object | No | Plain text placeholder. |
| `initial_user` | string | No | Pre-selected user ID. |
| `confirm` | object | No | Confirmation dialog. |
| `focus_on_load` | boolean | No | Auto-focus on load. |

### Example

```json
{
  "type": "users_select",
  "action_id": "assign_user",
  "placeholder": {
    "type": "plain_text",
    "text": "Select a user"
  }
}
```

---

## Conversations Select Menu

Select from channels, DMs, or group messages.

### Example

```json
{
  "type": "conversations_select",
  "action_id": "select_conversation",
  "placeholder": {
    "type": "plain_text",
    "text": "Select a channel"
  }
}
```

---

## Channels Select Menu

Select from public channels only.

### Example

```json
{
  "type": "channels_select",
  "action_id": "select_channel",
  "placeholder": {
    "type": "plain_text",
    "text": "Select a channel"
  }
}
```

---

## Datepicker

Calendar date selection.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"datepicker"` |
| `action_id` | string | Yes | Unique identifier. |
| `placeholder` | object | No | Plain text placeholder. |
| `initial_date` | string | No | Initial date (YYYY-MM-DD format). |
| `confirm` | object | No | Confirmation dialog. |
| `focus_on_load` | boolean | No | Auto-focus on load. |

### Example

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

---

## Timepicker

Time selection.

### Example

```json
{
  "type": "timepicker",
  "action_id": "time_select",
  "placeholder": {
    "type": "plain_text",
    "text": "Select a time"
  },
  "initial_time": "14:30"
}
```

---

## Datetime Picker

Combined date and time selection.

### Example

```json
{
  "type": "datetimepicker",
  "action_id": "datetime_select"
}
```

---

## Overflow Menu

Compact menu for multiple options.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"overflow"` |
| `action_id` | string | Yes | Unique identifier. |
| `options` | array | Yes | Array of option objects. Max 5 options. |
| `confirm` | object | No | Confirmation dialog. |

### Example

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
        "text": "Duplicate"
      },
      "value": "duplicate"
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

---

## Checkboxes

Multiple option selection.

### Example

```json
{
  "type": "checkboxes",
  "action_id": "checkbox_selection",
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
      "description": {
        "type": "mrkdwn",
        "text": "*Additional description*"
      },
      "value": "option_2"
    }
  ]
}
```

---

## Radio Buttons

Single option selection.

### Example

```json
{
  "type": "radio_buttons",
  "action_id": "radio_selection",
  "options": [
    {
      "text": {
        "type": "plain_text",
        "text": "Option A"
      },
      "value": "a"
    },
    {
      "text": {
        "type": "plain_text",
        "text": "Option B"
      },
      "value": "b"
    }
  ]
}
```

---

## Plain Text Input

Single-line or multi-line text input.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"plain_text_input"` |
| `action_id` | string | No | Unique identifier. |
| `placeholder` | object | No | Plain text placeholder. Max 150 chars. |
| `initial_value` | string | No | Pre-filled value. |
| `multiline` | boolean | No | If true, shows textarea. Default false. |
| `min_length` | number | No | Minimum character length (0-3000). |
| `max_length` | number | No | Maximum character length (1-3000). |
| `dispatch_action_config` | object | No | When to dispatch block_actions. |
| `focus_on_load` | boolean | No | Auto-focus on load. |

### Single Line

```json
{
  "type": "plain_text_input",
  "action_id": "title_input",
  "placeholder": {
    "type": "plain_text",
    "text": "Enter title"
  }
}
```

### Multi-line

```json
{
  "type": "plain_text_input",
  "action_id": "description_input",
  "multiline": true,
  "placeholder": {
    "type": "plain_text",
    "text": "Enter description"
  }
}
```

---

## Email Text Input

Email input with validation.

### Example

```json
{
  "type": "email_text_input",
  "action_id": "email_input",
  "placeholder": {
    "type": "plain_text",
    "text": "Enter email address"
  }
}
```

---

## URL Text Input

URL input with validation.

### Example

```json
{
  "type": "url_text_input",
  "action_id": "url_input"
}
```

---

## Number Input

Numeric input (integer or decimal).

### Example

```json
{
  "type": "number_input",
  "is_decimal_allowed": false,
  "action_id": "quantity_input",
  "placeholder": {
    "type": "plain_text",
    "text": "Enter quantity"
  }
}
```

---

## File Input

File upload (modals only).

### Example

```json
{
  "type": "file_input",
  "action_id": "file_upload",
  "filetypes": ["jpg", "png", "pdf"],
  "max_files": 5
}
```

---

## Feedback Buttons

Quick positive/negative feedback. **Messages only, in context_actions block**.

### Example

```json
{
  "type": "feedback_buttons",
  "action_id": "feedback_1",
  "positive_button": {
    "text": {
      "type": "plain_text",
      "text": "👍"
    },
    "value": "positive",
    "accessibility_label": "Mark as helpful"
  },
  "negative_button": {
    "text": {
      "type": "plain_text",
      "text": "👎"
    },
    "value": "negative",
    "accessibility_label": "Mark as not helpful"
  }
}
```

---

## Icon Button

Icon-based button. **Messages only, in context_actions block**.

### Example

```json
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
```

---

## Best Practices

### Action IDs
- Make descriptive and unique
- Use for identifying interactions
- Max 255 characters

### Button Styles
- Use `primary` sparingly (one per view)
- Use `danger` for destructive actions
- Default style for most buttons

### Select Menus
- Static select: Known, fixed options
- Users select: User assignment
- Channels select: Channel routing
- Conversations select: Any conversation type

### Input Validation
- Set `min_length` and `max_length` for text inputs
- Use `is_decimal_allowed` for number inputs
- Mark fields `optional` in input blocks when appropriate

### Accessibility
- Provide `accessibility_label` for icon-only buttons
- Use clear, descriptive `placeholder` text
- Keep button text concise but meaningful

---

**Content Source**: Context7 (`/websites/slack_dev_reference_block-kit`)
