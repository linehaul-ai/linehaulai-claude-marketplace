# Web API: Messaging Patterns

## Basic Messaging

### Simple Text Message

```go
func sendSimpleMessage(api *slack.Client, channelID, text string) error {
    _, _, err := api.PostMessage(
        channelID,
        slack.MsgOptionText(text, false),
    )
    return err
}
```

### Markdown Formatting

```go
text := "*Bold text* and _italic text_\n• Bullet point\n> Quote"

_, _, err := api.PostMessage(
    channelID,
    slack.MsgOptionText(text, false),
)
```

## Message Threading

### Reply to a Thread

```go
func replyToThread(api *slack.Client, channelID, threadTS, text string) error {
    _, _, err := api.PostMessage(
        channelID,
        slack.MsgOptionText(text, false),
        slack.MsgOptionTS(threadTS), // Parent message timestamp
    )
    return err
}
```

### Start a New Thread

```go
// Post initial message
timestamp, _, err := api.PostMessage(
    channelID,
    slack.MsgOptionText("Thread starter", false),
)
if err != nil {
    return err
}

// Reply in thread
_, _, err = api.PostMessage(
    channelID,
    slack.MsgOptionText("Thread reply", false),
    slack.MsgOptionTS(timestamp),
)
```

## Ephemeral Messages

Send messages visible only to a specific user:

```go
func sendEphemeral(api *slack.Client, channelID, userID, text string) error {
    _, err := api.PostEphemeral(
        channelID,
        userID,
        slack.MsgOptionText(text, false),
    )
    return err
}
```

## Block Kit Composition

### Rich Message with Sections and Buttons

```go
func sendInteractiveMessage(api *slack.Client, channelID string) error {
    // Header section
    headerText := slack.NewTextBlockObject(
        "mrkdwn",
        "*Deployment Request*",
        false,
        false,
    )
    headerSection := slack.NewSectionBlock(headerText, nil, nil)

    // Divider
    divider := slack.NewDividerBlock()

    // Details section
    detailsText := slack.NewTextBlockObject(
        "mrkdwn",
        "*Environment:* Production\n*Version:* v2.1.0\n*Requested by:* <@U123456>",
        false,
        false,
    )
    detailsSection := slack.NewSectionBlock(detailsText, nil, nil)

    // Action buttons
    approveButton := slack.NewButtonBlockElement(
        "approve_deployment",
        "v2.1.0",
        slack.NewTextBlockObject("plain_text", "Approve", true, false),
    )
    approveButton.Style = slack.StylePrimary

    rejectButton := slack.NewButtonBlockElement(
        "reject_deployment",
        "v2.1.0",
        slack.NewTextBlockObject("plain_text", "Reject", true, false),
    )
    rejectButton.Style = slack.StyleDanger

    actionBlock := slack.NewActionBlock(
        "deployment_actions",
        approveButton,
        rejectButton,
    )

    // Send message
    _, _, err := api.PostMessage(
        channelID,
        slack.MsgOptionBlocks(
            headerSection,
            divider,
            detailsSection,
            actionBlock,
        ),
    )
    return err
}
```

## Message Updates

### Update Existing Message

```go
func updateMessage(api *slack.Client, channelID, timestamp, newText string) error {
    _, _, _, err := api.UpdateMessage(
        channelID,
        timestamp,
        slack.MsgOptionText(newText, false),
    )
    return err
}
```

### Update with New Blocks

```go
func updateWithBlocks(api *slack.Client, channelID, timestamp string) error {
    successText := slack.NewTextBlockObject(
        "mrkdwn",
        ":white_check_mark: *Deployment Approved*",
        false,
        false,
    )
    successBlock := slack.NewSectionBlock(successText, nil, nil)

    _, _, _, err := api.UpdateMessage(
        channelID,
        timestamp,
        slack.MsgOptionBlocks(successBlock),
    )
    return err
}
```

## Message Deletion

```go
func deleteMessage(api *slack.Client, channelID, timestamp string) error {
    _, _, err := api.DeleteMessage(channelID, timestamp)
    return err
}
```

## Scheduled Messages

### Schedule for Later

```go
import "time"

func scheduleMessage(api *slack.Client, channelID, text string, sendTime time.Time) error {
    timestamp := sendTime.Unix()

    _, err := api.ScheduleMessage(
        channelID,
        strconv.FormatInt(timestamp, 10),
        slack.MsgOptionText(text, false),
    )
    return err
}
```

## Error Handling

### Comprehensive Error Handling

```go
func sendMessageWithErrorHandling(api *slack.Client, channelID, text string) error {
    _, _, err := api.PostMessage(
        channelID,
        slack.MsgOptionText(text, false),
    )

    if err != nil {
        switch {
        case strings.Contains(err.Error(), "channel_not_found"):
            return fmt.Errorf("channel %s does not exist", channelID)

        case strings.Contains(err.Error(), "not_in_channel"):
            return fmt.Errorf("bot is not a member of channel %s", channelID)

        case strings.Contains(err.Error(), "is_archived"):
            return fmt.Errorf("channel %s is archived", channelID)

        default:
            if rateLimitErr, ok := err.(*slack.RateLimitedError); ok {
                return fmt.Errorf("rate limited, retry after %v", rateLimitErr.RetryAfter)
            }
            return fmt.Errorf("failed to post message: %w", err)
        }
    }

    return nil
}
```

## Production-Ready Message Sender

Complete implementation with retries and error handling:

```go
func SendMessageWithRetry(
    ctx context.Context,
    api *slack.Client,
    channelID string,
    options ...slack.MsgOption,
) (string, error) {
    maxRetries := 3
    backoff := time.Second

    for attempt := 0; attempt < maxRetries; attempt++ {
        select {
        case <-ctx.Done():
            return "", ctx.Err()
        default:
        }

        timestamp, _, err := api.PostMessageContext(ctx, channelID, options...)
        if err == nil {
            return timestamp, nil
        }

        // Handle rate limiting
        if rateLimitErr, ok := err.(*slack.RateLimitedError); ok {
            sleepDuration := rateLimitErr.RetryAfter
            if sleepDuration == 0 {
                sleepDuration = backoff * time.Duration(attempt+1)
            }

            select {
            case <-time.After(sleepDuration):
                continue
            case <-ctx.Done():
                return "", ctx.Err()
            }
        }

        // Permanent errors - don't retry
        if strings.Contains(err.Error(), "channel_not_found") ||
            strings.Contains(err.Error(), "invalid_auth") {
            return "", err
        }

        // Exponential backoff for other errors
        select {
        case <-time.After(backoff):
            backoff *= 2
        case <-ctx.Done():
            return "", ctx.Err()
        }
    }

    return "", fmt.Errorf("max retries exceeded")
}
```

## Common Pitfalls

1. **Not escaping user input** - Sanitize text before posting
2. **Forgetting thread context** - Use MsgOptionTS for replies
3. **Ignoring rate limits** - Implement exponential backoff
4. **Hardcoding message content** - Use templates or configuration
5. **Not handling message updates** - Store timestamps for later updates
