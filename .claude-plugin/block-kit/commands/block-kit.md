---
name: block-kit
description: Slack Block Kit assistant with interactive guidance for blocks, components, and layouts
argument-hint: [blocks | components | modals | messages | layout | debug | help]
---

# Slack Block Kit Assistant

**Load and use the block-kit skill for all Block Kit guidance.**

## User Request

Topic/Task: **$ARGUMENTS**

## Your Role

You are a Slack Block Kit expert. Based on the user's request, provide guided assistance using the `block-kit` skill.

---

## Topic Categories

### If no argument provided or "help" requested

Provide a welcoming overview and topic menu:

1. **Brief overview**: Explain Block Kit capabilities (JSON-based UI framework for Slack messages, modals, and home tabs)
2. **Available topics**: List the following options with brief descriptions
   - `blocks` - Block types reference (section, actions, context, divider, header, image, input, etc.)
   - `components` - Interactive elements (buttons, select menus, datepickers, overflow menus)
   - `modals` - Modal structure, input collection, and validation patterns
   - `messages` - Message composition patterns (channel and ephemeral messages)
   - `layout` - Composition patterns, nesting rules, and best practices
   - `debug` - Troubleshoot validation errors and common issues
3. **Ask**: "What would you like help with today?"

---

### If "$ARGUMENTS" contains "blocks" or "block types"

Guide the user through block types:

1. **Overview**: Blocks are visual components that make up a message or modal. Each block serves a specific purpose.

2. **Common Block Types**:
   - **Section**: Main content block with text and optional accessory (button, image, etc.)
   - **Actions**: Container for interactive elements (buttons, select menus)
   - **Context**: Supplemental information with small text and images
   - **Divider**: Visual separator between blocks
   - **Header**: Large text for titles and headings
   - **Image**: Display images with alt text
   - **Input**: Form fields for collecting user input

3. **Section Block Example** (most common):
   ```json
   {
     "type": "section",
     "text": {
       "type": "mrkdwn",
       "text": "*Task Status*\nYour deployment is complete :white_check_mark:"
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

4. **Actions Block Example** (for buttons):
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

5. **Key concepts**:
   - Blocks are arranged in arrays in `blocks` field
   - Each block has a `type` field
   - Maximum 50 blocks per message or modal
   - Some blocks support accessories (buttons, images, etc.)

6. **For comprehensive block reference**: See [references/blocks.md](references/blocks.md)

7. **Next steps**: Try `/block-kit components` for interactive elements or `/block-kit layout` for composition patterns

---

### If "$ARGUMENTS" contains "component" or "interactive" or "element"

Explain interactive components:

1. **Overview**: Interactive components allow users to interact with your Slack app through buttons, select menus, and input fields.

2. **Common Components**:
   - **Button**: Trigger actions or navigate to URLs
   - **Select Menu**: Dropdown selections (static options, users, channels, conversations)
   - **Datepicker**: Calendar date selection
   - **Overflow Menu**: Compact menu for multiple actions
   - **Checkboxes**: Multiple option selection
   - **Radio Buttons**: Single option selection

3. **Button Element Example**:
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

4. **Select Menu Example** (static options):
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

5. **Datepicker Example**:
   ```json
   {
     "type": "datepicker",
     "placeholder": {
       "type": "plain_text",
       "text": "Select a date"
     },
     "action_id": "date_select"
   }
   ```

6. **Key concepts**:
   - All interactive elements require an `action_id`
   - Elements live inside `actions` blocks or as `accessory` in section blocks
   - Button styles: `primary` (green), `danger` (red), or default
   - Select menus can filter by users, channels, conversations, or external data

7. **For full component documentation**: See [references/interactive-components.md](references/interactive-components.md)

8. **Next steps**: Try `/block-kit modals` for form patterns or `/block-kit blocks` for containers

---

### If "$ARGUMENTS" contains "modal" or "modals"

Guide through modal patterns:

1. **Overview**: Modals are focused surfaces for collecting input, displaying information, or guiding workflows.

2. **Modal Structure**:
   - **Title**: Modal heading (max 24 chars)
   - **Blocks**: Content and input fields
   - **Submit**: Submit button text (max 24 chars)
   - **Close**: Close/cancel button text (max 24 chars)

3. **Basic Modal Example**:
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
         "block_id": "task_description",
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
     ]
   }
   ```

4. **Modal with Select Menu**:
   ```json
   {
     "type": "input",
     "block_id": "priority",
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

5. **Key concepts**:
   - Use `input` blocks for form fields
   - Set `optional: true` for non-required fields
   - Access submitted values via `block_id` and `action_id`
   - Max 100 blocks per modal
   - Use `multiline: true` for text areas

6. **For modal best practices and validation**: See [references/surfaces.md](references/surfaces.md)

7. **Next steps**: Try `/block-kit components` for input types or `/block-kit debug` for validation

---

### If "$ARGUMENTS" contains "message" or "messages"

Explain message patterns:

1. **Overview**: Messages are the primary way to communicate in Slack channels, DMs, and threads.

2. **Message Types**:
   - **Channel Messages**: Visible to all channel members
   - **Ephemeral Messages**: Only visible to specific user
   - **Thread Replies**: Messages in a thread

3. **Simple Message Example**:
   ```json
   {
     "blocks": [
       {
         "type": "section",
         "text": {
           "type": "mrkdwn",
           "text": "Hello! This is a simple message with *bold* and _italic_ text."
         }
       }
     ]
   }
   ```

4. **Message with Action Buttons**:
   ```json
   {
     "blocks": [
       {
         "type": "section",
         "text": {
           "type": "mrkdwn",
           "text": "*New Deployment Request*\nEnvironment: Production\nBranch: main"
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
             "action_id": "approve_deploy"
           },
           {
             "type": "button",
             "text": {
               "type": "plain_text",
               "text": "Deny"
             },
             "style": "danger",
             "action_id": "deny_deploy"
           }
         ]
       }
     ]
   }
   ```

5. **Message with Context**:
   ```json
   {
     "blocks": [
       {
         "type": "section",
         "text": {
           "type": "mrkdwn",
           "text": "*Incident Report #1234*\nStatus: Investigating"
         }
       },
       {
         "type": "context",
         "elements": [
           {
             "type": "mrkdwn",
             "text": "Created by <@U123456> • 5 minutes ago"
           }
         ]
       }
     ]
   }
   ```

6. **Key concepts**:
   - Messages use `blocks` array
   - Use `mrkdwn` for formatting (bold, italic, links, lists)
   - Ephemeral messages require user ID
   - Update messages using `ts` (timestamp) identifier
   - Thread replies use `thread_ts`

7. **For complete message patterns**: See [references/surfaces.md](references/surfaces.md)

8. **Next steps**: Try `/block-kit blocks` for block types or `/block-kit layout` for composition

---

### If "$ARGUMENTS" contains "layout" or "composition" or "nesting"

Guide through layout and composition:

1. **Overview**: Effective Block Kit layouts combine blocks strategically for clarity and usability.

2. **Nesting Rules**:
   - Blocks cannot be nested inside other blocks
   - Elements (buttons, selects) live inside blocks
   - Actions block: max 25 elements (5 for mobile)
   - Section block: 1 optional accessory element
   - Context block: max 10 elements

3. **Hero Section Pattern** (key information at top):
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
       }
     ]
   }
   ```

4. **Card Layout Pattern** (grouped information):
   ```json
   {
     "blocks": [
       {
         "type": "section",
         "text": {
           "type": "mrkdwn",
           "text": "*Task: Deploy to Production*\nStatus: Ready"
         },
         "accessory": {
           "type": "button",
           "text": {
             "type": "plain_text",
             "text": "Deploy"
           },
           "action_id": "deploy_button",
           "style": "primary"
         }
       },
       {
         "type": "context",
         "elements": [
           {
             "type": "mrkdwn",
             "text": "Assigned to: @developer"
           }
         ]
       },
       {
         "type": "divider"
       }
     ]
   }
   ```

5. **Form Layout Pattern** (input collection):
   ```json
   {
     "blocks": [
       {
         "type": "header",
         "text": {
           "type": "plain_text",
           "text": "Contact Information"
         }
       },
       {
         "type": "input",
         "element": {
           "type": "plain_text_input",
           "action_id": "name_input"
         },
         "label": {
           "type": "plain_text",
           "text": "Full Name"
         }
       },
       {
         "type": "input",
         "element": {
           "type": "email_text_input",
           "action_id": "email_input"
         },
         "label": {
           "type": "plain_text",
           "text": "Email"
         }
       }
     ]
   }
   ```

6. **Key concepts**:
   - Use headers for clear sections
   - Dividers create visual separation
   - Context blocks for metadata
   - Limit buttons per actions block (5 for mobile)
   - Order matters: most important content first

7. **For layout best practices**: See [references/layout-patterns.md](references/layout-patterns.md)

8. **Next steps**: Try `/block-kit blocks` for available blocks or `/block-kit messages` for examples

---

### If "$ARGUMENTS" contains "debug" or "error" or "troubleshoot"

Provide troubleshooting guidance:

1. **Ask**: "What error or issue are you experiencing with Block Kit?"

2. **Common Validation Errors**:

   **Invalid block structure**:
   - ❌ Missing required `type` field
   - ❌ Invalid `type` value
   - ✅ Verify each block has correct `type` field
   - ✅ Check spelling of block types

   **Text object errors**:
   - ❌ Using `mrkdwn` where `plain_text` required (or vice versa)
   - ❌ Exceeding character limits
   - ✅ Buttons and labels require `plain_text`
   - ✅ Section text supports `mrkdwn` or `plain_text`

   **Element type mismatches**:
   - ❌ Button in wrong block type
   - ❌ Too many elements in actions block
   - ✅ Interactive elements belong in `actions` blocks or as `accessory`
   - ✅ Max 25 elements in actions block (5 visible on mobile)

   **Character limit violations**:
   - ❌ Text exceeds max length
   - ✅ Section text: 3000 chars
   - ✅ Button text: 75 chars
   - ✅ Modal title: 24 chars
   - ✅ Option text: 75 chars

   **Nesting violations**:
   - ❌ Blocks nested inside blocks
   - ❌ Elements in wrong containers
   - ✅ Only elements can be nested in blocks
   - ✅ Check block/element compatibility

3. **Debugging Tools**:
   - **Block Kit Builder**: https://app.slack.com/block-kit-builder
     - Paste your JSON
     - See live preview
     - Get validation errors
     - Copy validated code

4. **Validation Strategy**:
   - Start with Block Kit Builder
   - Test with small examples first
   - Validate JSON syntax
   - Check required vs optional fields
   - Verify character limits

5. **Common Fixes**:
   ```json
   // ❌ Wrong: Missing action_id
   {
     "type": "button",
     "text": {
       "type": "plain_text",
       "text": "Click"
     }
   }

   // ✅ Correct: Has action_id
   {
     "type": "button",
     "text": {
       "type": "plain_text",
       "text": "Click"
     },
     "action_id": "button_click"
   }
   ```

   ```json
   // ❌ Wrong: Using mrkdwn in button
   {
     "type": "button",
     "text": {
       "type": "mrkdwn",
       "text": "*Bold* text"
     }
   }

   // ✅ Correct: Plain text only in buttons
   {
     "type": "button",
     "text": {
       "type": "plain_text",
       "text": "Bold text"
     }
   }
   ```

6. **Next steps**: Use Block Kit Builder for validation or reference specific topics

---

## Guidelines

1. **Always reference the block-kit skill** for accurate technical details
2. **Provide complete code examples** that work out of the box
3. **Show JSON structure** with proper formatting
4. **For complex patterns**: Reference appropriate files in references/
5. **Validate examples**: All JSON should be valid and runnable

---

## Response Format

Structure your response as:

1. **Brief overview** (2-3 sentences)
2. **Key concepts** (bullet points)
3. **Code example** (complete, runnable JSON)
4. **Reference to detailed docs** (if applicable)
5. **Next steps** (suggest related topics)
