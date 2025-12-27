# Block Kit - Layout and Composition Patterns

Best practices for composing blocks into effective layouts with proper nesting, ordering, and structure.

---

## Block Composition Fundamentals

### Nesting Rules

**Blocks cannot be nested inside other blocks**. Only elements can be nested within blocks.

**Valid nesting**:
- Elements inside actions block
- Element as accessory in section block
- Elements (text, images) in context block
- Element in input block

**Invalid nesting**:
- Blocks inside blocks
- Direct elements in `blocks` array (must be in a block)

### Element Limits Per Block

| Block Type | Element Limit | Notes |
|------------|---------------|-------|
| Actions | 25 elements | Only 5 visible on mobile |
| Section | 1 accessory | Single element only |
| Context | 10 elements | Text and images |
| Input | 1 element | Form input element |
| Context Actions | 5 elements | Feedback/icon buttons |

### Maximum Blocks Per Surface

- **Messages**: 50 blocks
- **Modals**: 100 blocks
- **Home Tabs**: 100 blocks

---

## Layout Patterns

### Hero Pattern

Key information at the top with prominent heading.

```json
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "Weekly Report"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Total Sales:* $45,000\n*New Customers:* 23\n*Conversion Rate:* 12.5%"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Detailed breakdown below..."
      }
    }
  ]
}
```

**When to use**: Reports, dashboards, announcements

---

### Card Layout

Grouped information with metadata.

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Task: Deploy to Production*\nStatus: Ready for deployment"
      },
      "accessory": {
        "type": "button",
        "text": {
          "type": "plain_text",
          "text": "Deploy"
        },
        "style": "primary",
        "action_id": "deploy_button"
      }
    },
    {
      "type": "context",
      "elements": [
        {
          "type": "mrkdwn",
          "text": "Assigned to: @developer • Due: Tomorrow"
        }
      ]
    },
    {
      "type": "divider"
    }
  ]
}
```

**When to use**: Task lists, item previews, cards

---

### List with Actions

Repeating items with action buttons.

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Pull Request #123*\nAdd authentication feature"
      },
      "accessory": {
        "type": "button",
        "text": {
          "type": "plain_text",
          "text": "Review"
        },
        "action_id": "review_123"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Pull Request #124*\nFix bug in payment flow"
      },
      "accessory": {
        "type": "button",
        "text": {
          "type": "plain_text",
          "text": "Review"
        },
        "action_id": "review_124"
      }
    }
  ]
}
```

**When to use**: Lists, queues, notifications

---

### Form Layout

Input collection with clear labels.

```json
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "Create New Task"
      }
    },
    {
      "type": "input",
      "block_id": "title",
      "element": {
        "type": "plain_text_input",
        "action_id": "title_input"
      },
      "label": {
        "type": "plain_text",
        "text": "Title"
      }
    },
    {
      "type": "input",
      "block_id": "assignee",
      "element": {
        "type": "users_select",
        "action_id": "assignee_select"
      },
      "label": {
        "type": "plain_text",
        "text": "Assignee"
      }
    },
    {
      "type": "input",
      "block_id": "priority",
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

**When to use**: Modals, data collection

---

### Dashboard Pattern

Key metrics in two-column fields layout.

```json
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "System Status"
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Uptime:*\n99.9%"
        },
        {
          "type": "mrkdwn",
          "text": "*Response Time:*\n245ms"
        },
        {
          "type": "mrkdwn",
          "text": "*Active Users:*\n1,234"
        },
        {
          "type": "mrkdwn",
          "text": "*Error Rate:*\n0.01%"
        }
      ]
    }
  ]
}
```

**When to use**: Dashboards, status pages, metrics

---

## Responsive Design

### Mobile Considerations

**Actions Block Limits**:
- Desktop: 25 elements supported
- Mobile: Only 5 elements visible (rest hidden in overflow)

**Best practice**: Place most important actions first in `elements` array.

```json
{
  "type": "actions",
  "elements": [
    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Primary Action"
      },
      "style": "primary",
      "action_id": "primary"
    },
    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Secondary"
      },
      "action_id": "secondary"
    }
  ]
}
```

### Text Truncation

- Button text truncates ~30 characters
- Section text: 3000 char limit
- Use concise labels

### Image Sizing

Images auto-scale to fit container. Provide appropriately sized images:
- Section accessory images: ~75x75px
- Image blocks: Variable based on surface
- Context images: Small thumbnails

---

## Accessibility Patterns

### Alt Text for Images

Always provide descriptive `alt_text`:

```json
{
  "type": "image",
  "image_url": "https://example.com/chart.png",
  "alt_text": "Bar chart showing monthly sales growth from January to December"
}
```

### Accessibility Labels

Use for icon-only or ambiguous buttons:

```json
{
  "type": "button",
  "text": {
    "type": "plain_text",
    "text": "🗑️"
  },
  "accessibility_label": "Delete this item permanently",
  "action_id": "delete"
}
```

### Screen Reader Considerations

- Keep text hierarchical (header → section → context)
- Use semantic block types
- Provide clear labels for all inputs
- Add helpful `hint` text in input blocks

---

## Performance Optimization

### Lazy Loading

For long lists, implement pagination:

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Showing items 1-10 of 100"
      }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Load More"
          },
          "action_id": "load_more",
          "value": "page_2"
        }
      ]
    }
  ]
}
```

### Efficient Updates

Update messages rather than posting new ones:

- Use message `ts` (timestamp) to update existing messages
- Only update changed blocks (Slack diffs automatically)
- Avoid recreating entire message payloads

### Block Caching

Cache frequently used blocks (templates):

```javascript
const approvalButtons = {
  type: "actions",
  elements: [
    // ... standard approval buttons
  ]
};

// Reuse across multiple messages
```

---

## Common Anti-Patterns

### ❌ Too Many Actions

```json
{
  "type": "actions",
  "elements": [
    // 10+ buttons - overwhelming!
  ]
}
```

**✅ Better**: Group related actions in overflow menu or use select menu.

---

### ❌ Nested Blocks

```json
{
  "type": "section",
  "blocks": [  // Invalid!
    {
      "type": "section"
    }
  ]
}
```

**✅ Better**: Blocks in top-level `blocks` array only.

---

### ❌ Unclear Hierarchy

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Random content"
      }
    },
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "Important Title"
      }
    }
  ]
}
```

**✅ Better**: Headers before content.

---

### ❌ Missing Dividers

Long content without visual breaks is hard to scan.

**✅ Better**: Use dividers between distinct sections.

---

## Block Ordering Best Practices

### Priority Order

1. **Header** - Section/page title
2. **Section** - Primary content
3. **Image** - Supporting visuals
4. **Actions** - User actions
5. **Context** - Metadata, timestamps
6. **Divider** - Section separator

### Logical Grouping

Group related blocks together:

```json
{
  "blocks": [
    // Task 1
    {"type": "section", "text": {"type": "mrkdwn", "text": "*Task 1*"}},
    {"type": "actions", "elements": [/* task 1 actions */]},
    {"type": "context", "elements": [/* task 1 metadata */]},
    {"type": "divider"},

    // Task 2
    {"type": "section", "text": {"type": "mrkdwn", "text": "*Task 2*"}},
    {"type": "actions", "elements": [/* task 2 actions */]},
    {"type": "context", "elements": [/* task 2 metadata */]}
  ]
}
```

---

**Content Source**: Context7 (`/websites/slack_dev_reference_block-kit`) + Best Practices
