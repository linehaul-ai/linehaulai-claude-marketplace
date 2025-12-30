---
description: Build Slack Block Kit UIs for messages, modals, and Home tabs
---

# /block-kit Command

Build interactive Slack UIs using Block Kit.

## Usage

```bash
/block-kit [surface] [requirements]
```

## Surfaces

- `message` - Channel messages, DMs, ephemeral responses
- `modal` - Interactive dialogs with forms and confirmations
- `home` - App Home tab dashboards

## Examples

### Example 1: Notification Message
```bash
/block-kit message Create a deploy notification with:
- Header showing "Deployment Complete"
- Section with environment, version, and timestamp fields
- Context showing who triggered the deploy
- Button to view logs
```

### Example 2: Form Modal
```bash
/block-kit modal Build a feedback form with:
- Title "Submit Feedback"
- Dropdown to select feedback type (bug, feature, general)
- Multi-line text input for description
- Optional file upload
- Submit and cancel buttons
```

### Example 3: App Home Dashboard
```bash
/block-kit home Design a task dashboard showing:
- Header with user greeting
- Section listing assigned tasks with checkboxes
- Actions section with "New Task" and "View All" buttons
- Dividers between sections
```

## What This Command Does

1. **Analyzes Requirements** - Determines optimal block structure for the use case

2. **Selects Components**
   - Appropriate blocks (Section, Actions, Input, etc.)
   - Interactive elements (Buttons, Selects, Date pickers)
   - Composition objects (Text formatting, Confirmations)

3. **Generates Code**
   - Complete JSON payload ready for Slack API
   - Equivalent slack-block-builder JavaScript code
   - action_id and block_id naming suggestions

4. **Provides Validation**
   - Block limit checks (50 messages, 100 modals)
   - Element compatibility verification
   - Required field validation

5. **Offers Enhancements**
   - Accessibility improvements
   - Mobile-responsive patterns
   - Error state handling

## Integration

This command invokes the `block-kit-expert` agent for:
- Complex layout decisions
- Multi-modal workflows
- Performance optimization
- Interaction handling patterns

## Common Patterns

### Notification Messages
- Header + Section (fields) + Context + Actions
- Use mrkdwn for formatting
- Include timestamps and user mentions

### Forms (Modals)
- Input blocks with various elements
- Validation via dispatch_action_config
- Multi-step with view.push/update

### Dashboards (Home)
- Section blocks with accessories
- Actions for quick interactions
- Rich text for formatted content

## Tips

- Use `block_id` and `action_id` consistently for payload handling
- Keep messages under 50 blocks, modals under 100
- Test in Slack Block Kit Builder before deploying
- Use confirmation dialogs for destructive actions
- Consider mobile display (shorter text, fewer columns)

## See Also

- `slack-block-kit` skill - Comprehensive Block Kit documentation
- `block-kit-expert` agent - Implementation guidance
- Slack Block Kit Builder - https://app.slack.com/block-kit-builder
