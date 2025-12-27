# Block Kit Integration with Go SDK

## Overview

Block Kit enables rich, interactive messages in Slack. The Go SDK provides builder functions for creating blocks programmatically.

## Core Block Types

### Section Block

Display text with optional accessories:

```go
// Simple text section
text := slack.NewTextBlockObject("mrkdwn", "*Bold* and _italic_ text", false, false)
section := slack.NewSectionBlock(text, nil, nil)

// Section with button accessory
button := slack.NewButtonBlockElement("action_id", "value", slack.NewTextBlockObject("plain_text", "Click Me", true, false))
sectionWithButton := slack.NewSectionBlock(text, nil, slack.NewAccessory(button))

// Section with image accessory
imageElement := slack.NewImageBlockElement("https://example.com/image.png", "alt text")
sectionWithImage := slack.NewSectionBlock(text, nil, slack.NewAccessory(imageElement))
```

### Divider Block

Visual separator:

```go
divider := slack.NewDividerBlock()
```

### Image Block

Full-width image:

```go
imageBlock := slack.NewImageBlock(
    "https://example.com/banner.png",
    "Alt text",
    "image_block_id",
    slack.NewTextBlockObject("plain_text", "Image title", false, false),
)
```

### Context Block

Supplementary information:

```go
elements := []slack.MixedElement{
    slack.NewImageBlockElement("https://example.com/icon.png", "icon"),
    slack.NewTextBlockObject("mrkdwn", "Last updated: 2024-01-15", false, false),
}
contextBlock := slack.NewContextBlock("context_id", elements...)
```

## Interactive Elements

### Buttons

```go
// Primary button
approveBtn := slack.NewButtonBlockElement(
    "approve_action",
    "approve_value",
    slack.NewTextBlockObject("plain_text", "Approve", true, false),
)
approveBtn.Style = slack.StylePrimary

// Danger button
rejectBtn := slack.NewButtonBlockElement(
    "reject_action",
    "reject_value",
    slack.NewTextBlockObject("plain_text", "Reject", true, false),
)
rejectBtn.Style = slack.StyleDanger

// Action block with buttons
actionBlock := slack.NewActionBlock("actions", approveBtn, rejectBtn)
```

### Select Menus

```go
// Static select menu
options := []*slack.OptionBlockObject{
    slack.NewOptionBlockObject("value1", slack.NewTextBlockObject("plain_text", "Option 1", false, false), nil),
    slack.NewOptionBlockObject("value2", slack.NewTextBlockObject("plain_text", "Option 2", false, false), nil),
    slack.NewOptionBlockObject("value3", slack.NewTextBlockObject("plain_text", "Option 3", false, false), nil),
}

placeholder := slack.NewTextBlockObject("plain_text", "Select an option", false, false)
selectMenu := slack.NewOptionsSelectBlockElement("static_select", placeholder, "select_action", options...)

actionBlock := slack.NewActionBlock("select_actions", selectMenu)
```

### Multi-Select

```go
multiSelect := slack.NewOptionsMultiSelectBlockElement(
    "multi_static_select",
    placeholder,
    "multiselect_action",
    options...,
)
```

## Complete Message Examples

### Approval Workflow

```go
func buildApprovalMessage(requester, environment, version string) []slack.Block {
    // Header
    headerText := slack.NewTextBlockObject("mrkdwn", "*Deployment Approval Required*", false, false)
    headerBlock := slack.NewSectionBlock(headerText, nil, nil)

    divider := slack.NewDividerBlock()

    // Details section
    detailsMarkdown := fmt.Sprintf(
        "*Requester:* <@%s>\n*Environment:* %s\n*Version:* `%s`\n*Time:* <!date^%d^{date_short_pretty} at {time}|%s>",
        requester,
        environment,
        version,
        time.Now().Unix(),
        time.Now().Format(time.RFC3339),
    )
    detailsText := slack.NewTextBlockObject("mrkdwn", detailsMarkdown, false, false)
    detailsBlock := slack.NewSectionBlock(detailsText, nil, nil)

    // Approval buttons
    approveBtn := slack.NewButtonBlockElement(
        "approve_deploy",
        fmt.Sprintf("%s:%s", environment, version),
        slack.NewTextBlockObject("plain_text", "Approve", true, false),
    )
    approveBtn.Style = slack.StylePrimary

    rejectBtn := slack.NewButtonBlockElement(
        "reject_deploy",
        fmt.Sprintf("%s:%s", environment, version),
        slack.NewTextBlockObject("plain_text", "Reject", true, false),
    )
    rejectBtn.Style = slack.StyleDanger

    actionBlock := slack.NewActionBlock("approval_actions", approveBtn, rejectBtn)

    // Context footer
    footerElements := []slack.MixedElement{
        slack.NewTextBlockObject("mrkdwn", ":information_source: This request expires in 1 hour", false, false),
    }
    contextBlock := slack.NewContextBlock("footer_context", footerElements...)

    return []slack.Block{
        headerBlock,
        divider,
        detailsBlock,
        actionBlock,
        contextBlock,
    }
}

// Send the message
blocks := buildApprovalMessage("U123456", "production", "v2.1.0")
_, _, err := api.PostMessage(
    channelID,
    slack.MsgOptionBlocks(blocks...),
)
```

### Form with Input Blocks

```go
func buildFeedbackForm() []slack.Block {
    // Header
    headerText := slack.NewTextBlockObject("mrkdwn", "*Submit Feedback*", false, false)
    headerBlock := slack.NewSectionBlock(headerText, nil, nil)

    // Rating select
    ratingOptions := []*slack.OptionBlockObject{
        slack.NewOptionBlockObject("5", slack.NewTextBlockObject("plain_text", "⭐⭐⭐⭐⭐ Excellent", false, false), nil),
        slack.NewOptionBlockObject("4", slack.NewTextBlockObject("plain_text", "⭐⭐⭐⭐ Good", false, false), nil),
        slack.NewOptionBlockObject("3", slack.NewTextBlockObject("plain_text", "⭐⭐⭐ Average", false, false), nil),
        slack.NewOptionBlockObject("2", slack.NewTextBlockObject("plain_text", "⭐⭐ Poor", false, false), nil),
        slack.NewOptionBlockObject("1", slack.NewTextBlockObject("plain_text", "⭐ Very Poor", false, false), nil),
    }

    ratingSelect := slack.NewOptionsSelectBlockElement(
        "static_select",
        slack.NewTextBlockObject("plain_text", "Select rating", false, false),
        "rating_select",
        ratingOptions...,
    )

    ratingBlock := slack.NewInputBlock(
        "rating_block",
        slack.NewTextBlockObject("plain_text", "Rating", false, false),
        nil,
        ratingSelect,
    )

    // Comments input
    commentsInput := slack.NewPlainTextInputBlockElement(
        slack.NewTextBlockObject("plain_text", "Enter your comments", false, false),
        "comments_input",
    )
    commentsInput.Multiline = true

    commentsBlock := slack.NewInputBlock(
        "comments_block",
        slack.NewTextBlockObject("plain_text", "Comments", false, false),
        nil,
        commentsInput,
    )

    return []slack.Block{
        headerBlock,
        ratingBlock,
        commentsBlock,
    }
}
```

## Layout Patterns

### Two-Column Layout

Use fields for side-by-side content:

```go
fields := []*slack.TextBlockObject{
    slack.NewTextBlockObject("mrkdwn", "*Status:*\n:white_check_mark: Healthy", false, false),
    slack.NewTextBlockObject("mrkdwn", "*Uptime:*\n99.9%", false, false),
    slack.NewTextBlockObject("mrkdwn", "*Response Time:*\n45ms", false, false),
    slack.NewTextBlockObject("mrkdwn", "*Error Rate:*\n0.01%", false, false),
}

section := slack.NewSectionBlock(nil, fields, nil)
```

### Image Gallery

```go
func buildImageGallery(imageURLs []string) []slack.Block {
    var blocks []slack.Block

    for i, url := range imageURLs {
        imageBlock := slack.NewImageBlock(
            url,
            fmt.Sprintf("Image %d", i+1),
            fmt.Sprintf("image_%d", i),
            nil,
        )
        blocks = append(blocks, imageBlock)
    }

    return blocks
}
```

## Common Patterns

### Progress Indicator

```go
func buildProgressMessage(current, total int, message string) []slack.Block {
    progress := float64(current) / float64(total) * 100
    barLength := 20
    filled := int(float64(barLength) * progress / 100)

    progressBar := strings.Repeat("█", filled) + strings.Repeat("░", barLength-filled)

    text := slack.NewTextBlockObject(
        "mrkdwn",
        fmt.Sprintf("%s\n`%s` %.1f%% (%d/%d)", message, progressBar, progress, current, total),
        false,
        false,
    )

    return []slack.Block{slack.NewSectionBlock(text, nil, nil)}
}
```

## Best Practices

1. **Keep it simple** - Don't overuse blocks, maintain readability
2. **Use markdown sparingly** - Too much formatting reduces clarity
3. **Provide fallback text** - For notifications and search
4. **Test interactivity** - Ensure buttons and selects work as expected
5. **Consider mobile** - Blocks should work on small screens
6. **Use Block Kit Builder** - Test layouts at app.slack.com/block-kit-builder

For advanced Block Kit patterns, see the block-kit plugin (if available).
