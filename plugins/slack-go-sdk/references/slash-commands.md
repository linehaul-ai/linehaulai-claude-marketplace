# Slash Commands

## Command Handler

```go
func handleSlashCommand(envelope socketmode.Event, client *socketmode.Client) {
    command, ok := envelope.Data.(slack.SlashCommand)
    if !ok {
        return
    }

    client.Ack(*envelope.Request)

    switch command.Command {
    case "/deploy":
        handleDeployCommand(command)

    case "/status":
        handleStatusCommand(command)
    }
}
```

## Immediate Response

```go
func handleDeployCommand(command slack.SlashCommand) {
    response := slack.Message{
        ResponseType: "in_channel", // or "ephemeral"
        Text:         fmt.Sprintf("Deploying %s...", command.Text),
    }
    // Response sent automatically by acknowledging with payload
}
```

## Delayed Response

```go
func handleLongCommand(command slack.SlashCommand, api *slack.Client) {
    // Send immediate acknowledgment
    api.PostMessage(
        command.ChannelID,
        slack.MsgOptionText("Processing...", false),
    )

    // Do long-running work
    go func() {
        time.Sleep(5 * time.Second)
        result := performWork()

        // Send final result using response_url
        webhook := slack.NewWebhook(command.ResponseURL)
        webhook.Post(&slack.WebhookMessage{
            Text: result,
        })
    }()
}
```

## Command Parsing

```go
func parseCommand(text string) (action string, args []string) {
    parts := strings.Fields(text)
    if len(parts) == 0 {
        return "", nil
    }
    return parts[0], parts[1:]
}
```

## Best Practices

1. Respond within 3 seconds
2. Use ephemeral for errors/private messages
3. Use in_channel for public updates
4. Parse and validate arguments
5. Provide help text for invalid input
