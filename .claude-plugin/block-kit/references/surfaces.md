# Block Kit - Surfaces Reference

Comprehensive reference for messages, modals, and home tabs - the three surfaces where Block Kit content appears.

---

## Surface Types Overview

| Surface | Max Blocks | Input Collection | Update Method | Visibility |
|---------|------------|------------------|---------------|------------|
| **Messages** | 50 | Buttons/selects | Update via `ts` | Channel/user |
| **Modals** | 100 | Input blocks | Push/update view | User-specific |
| **Home Tabs** | 100 | Input blocks | Publish view | User-specific |

---

## Messages

Messages appear in channels, DMs, and threads. Two types: channel messages (visible to all) and ephemeral messages (visible to one user).

### Message Structure

```json
{
  "blocks": [
    // Array of blocks (max 50)
  ],
  "text": "Fallback text for notifications"
}
```

### Simple Message

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Hello! This is a message."
      }
    }
  ]
}
```

### Message with Actions

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Deployment Request*\nEnvironment: Production"
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
          "action_id": "approve"
        },
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Deny"
          },
          "style": "danger",
          "action_id": "deny"
        }
      ]
    }
  ]
}
```

### Ephemeral Messages

Visible to one user only. Same structure, but posted with `postEphemeral` API method:

```javascript
// Post ephemeral message to specific user
client.chat.postEphemeral({
  channel: "C1234567890",
  user: "U0987654321",
  blocks: [/* blocks */]
});
```

### Updating Messages

Use message timestamp (`ts`) to update:

```javascript
client.chat.update({
  channel: "C1234567890",
  ts: "1234567890.123456",  // Original message ts
  blocks: [/* updated blocks */]
});
```

### Deleting Messages

```javascript
client.chat.delete({
  channel: "C1234567890",
  ts: "1234567890.123456"
});
```

### Thread Replies

Post message in thread using `thread_ts`:

```javascript
client.chat.postMessage({
  channel: "C1234567890",
  thread_ts: "1234567890.123456",  // Parent message ts
  blocks: [/* blocks */]
});
```

---

## Modals

Focused surfaces for input collection, multi-step workflows, or displaying information.

### Modal Structure

```json
{
  "type": "modal",
  "title": {
    "type": "plain_text",
    "text": "Modal Title"
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
    // Array of blocks (max 100)
  ],
  "callback_id": "modal_callback"
}
```

### Modal Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `"modal"` |
| `title` | object | Yes | Plain text. Max 24 chars. |
| `blocks` | array | Yes | Array of blocks. Max 100. |
| `submit` | object | No | Submit button text. Max 24 chars. |
| `close` | object | No | Close button text. Max 24 chars. |
| `callback_id` | string | No | Identifier for view submission. Max 255 chars. |
| `private_metadata` | string | No | Private string passed to app. Max 3000 chars. |
| `clear_on_close` | boolean | No | Clear view stack on close. Default false. |
| `notify_on_close` | boolean | No | Send view_closed event on close. Default false. |

### Simple Modal

```json
{
  "type": "modal",
  "title": {
    "type": "plain_text",
    "text": "Task Details"
  },
  "close": {
    "type": "plain_text",
    "text": "Close"
  },
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Task:* Deploy to production\n*Status:* Ready\n*Assigned:* @developer"
      }
    }
  ]
}
```

### Form Modal (Input Collection)

```json
{
  "type": "modal",
  "title": {
    "type": "plain_text",
    "text": "Create Issue"
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
  ],
  "callback_id": "create_issue_modal"
}
```

### Opening Modals

```javascript
client.views.open({
  trigger_id: trigger_id,  // From interaction payload
  view: {
    // Modal structure
  }
});
```

### Updating Modals

```javascript
client.views.update({
  view_id: view_id,  // From interaction payload
  view: {
    // Updated modal structure
  }
});
```

### Multi-Step Modals

Push new view onto stack:

```javascript
client.views.push({
  trigger_id: trigger_id,
  view: {
    // New modal view
  }
});
```

### Accessing Submitted Values

When user submits modal:

```javascript
// In view_submission handler
const values = payload.view.state.values;
const title = values.title_block.title_input.value;
const priority = values.priority_block.priority_select.selected_option.value;
```

### Validation Errors

Return errors from view_submission:

```javascript
return {
  response_action: "errors",
  errors: {
    "title_block": "Title must be at least 5 characters",
    "priority_block": "Please select a priority"
  }
};
```

---

## Home Tabs

Personalized app home page for each user.

### Home Tab Structure

```json
{
  "type": "home",
  "blocks": [
    // Array of blocks (max 100)
  ]
}
```

### Example Home Tab

```json
{
  "type": "home",
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "Welcome to App Home"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Here's your personalized dashboard."
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Tasks:*\n5 open"
        },
        {
          "type": "mrkdwn",
          "text": "*Notifications:*\n3 new"
        }
      ]
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "View Tasks"
          },
          "action_id": "view_tasks"
        },
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Settings"
          },
          "action_id": "settings"
        }
      ]
    }
  ]
}
```

### Publishing Home Tab

```javascript
client.views.publish({
  user_id: user_id,
  view: {
    // Home tab structure
  }
});
```

### Dynamic Content

Home tabs can show user-specific data:

```json
{
  "type": "home",
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Hello <@U123456>! You have *3* tasks assigned."
      }
    }
  ]
}
```

---

## Surface Comparison

### Messages vs Modals vs Home Tabs

**Use Messages when**:
- Broadcasting to channels
- Real-time notifications
- Collaborative interactions
- Permanent record needed

**Use Modals when**:
- Collecting structured input
- Multi-step workflows
- Focus required (no distractions)
- Temporary interaction

**Use Home Tabs when**:
- Personalized dashboards
- User-specific content
- App homepage
- Persistent app interface

---

## Best Practices

### Messages

- Keep concise (max 50 blocks)
- Use ephemeral for private responses
- Update existing messages vs posting new
- Include fallback `text` for notifications
- Thread replies to reduce channel noise

### Modals

- Clear, short titles (max 24 chars)
- Group related inputs together
- Mark non-required fields `optional`
- Provide helpful hint text
- Validate on submission
- Consider multi-step for complex forms

### Home Tabs

- Show personalized, user-specific content
- Update dynamically based on user state
- Provide quick actions
- Keep layout consistent
- Refresh on app_home_opened event

---

**Content Source**: Context7 (`/websites/slack_dev_reference_block-kit`) + Slack API Documentation
