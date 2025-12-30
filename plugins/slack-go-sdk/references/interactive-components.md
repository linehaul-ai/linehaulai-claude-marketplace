# Interactive Components

## Button Interactions

### Handling Button Clicks

```go
func handleInteraction(envelope socketmode.Event, client *socketmode.Client) {
    interaction, ok := envelope.Data.(slack.InteractionCallback)
    if !ok {
        return
    }

    client.Ack(*envelope.Request)

    switch interaction.Type {
    case slack.InteractionTypeBlockActions:
        handleBlockActions(interaction)

    case slack.InteractionTypeViewSubmission:
        handleModalSubmission(interaction)

    case slack.InteractionTypeShortcut:
        handleShortcut(interaction)
    }
}
```

### Block Actions

```go
func handleBlockActions(interaction slack.InteractionCallback) {
    for _, action := range interaction.ActionCallback.BlockActions {
        switch action.ActionID {
        case "approve_button":
            handleApproval(interaction, action.Value)

        case "reject_button":
            handleRejection(interaction, action.Value)
        }
    }
}
```

## Modal Interactions

### Opening a Modal

```go
func openModal(api *slack.Client, triggerID string) error {
    modalView := slack.ModalViewRequest{
        Type:  slack.ViewType("modal"),
        Title: slack.NewTextBlockObject("plain_text", "Feedback Form", false, false),
        Close: slack.NewTextBlockObject("plain_text", "Cancel", false, false),
        Submit: slack.NewTextBlockObject("plain_text", "Submit", false, false),
        Blocks: slack.Blocks{
            BlockSet: []slack.Block{
                slack.NewInputBlock(
                    "feedback_block",
                    slack.NewTextBlockObject("plain_text", "Your Feedback", false, false),
                    nil,
                    slack.NewPlainTextInputBlockElement(
                        slack.NewTextBlockObject("plain_text", "Enter feedback", false, false),
                        "feedback_input",
                    ),
                ),
            },
        },
    }

    _, err := api.OpenView(triggerID, modalView)
    return err
}
```

### Handling Modal Submission

```go
func handleModalSubmission(interaction slack.InteractionCallback) {
    values := interaction.View.State.Values
    feedback := values["feedback_block"]["feedback_input"].Value
    // Process feedback
}
```

## Select Menu Interactions

### Static Select

```go
func handleSelectMenu(interaction slack.InteractionCallback) {
    action := interaction.ActionCallback.BlockActions[0]
    selectedValue := action.SelectedOption.Value
    // Process selection
}
```

## Best Practices

1. Always acknowledge interactions immediately
2. Use goroutines for long-running operations
3. Update messages to provide feedback
4. Handle errors gracefully
5. Validate user input from modals
