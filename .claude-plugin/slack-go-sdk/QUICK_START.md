# Quick Start Guide

## Prerequisites Checklist

- [ ] Go 1.20 or later installed
- [ ] Slack workspace where you have admin access
- [ ] Basic understanding of Go programming

## Step 1: Install the SDK

```bash
go get -u github.com/slack-go/slack
```

## Step 2: Create a Slack App

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps)
2. Click **"Create New App"**
3. Choose **"From scratch"**
4. Enter app name (e.g., "My Bot")
5. Select your development workspace
6. Click **"Create App"**

## Step 3: Configure Bot Token Scopes

1. In your app settings, navigate to **OAuth & Permissions**
2. Scroll to **Bot Token Scopes**
3. Add the following scopes:
   - `chat:write` - Send messages
   - `channels:read` - View channels
   - `app_mentions:read` - Receive mentions
4. Click **"Save Changes"**

## Step 4: Install App to Workspace

1. Scroll to **OAuth Tokens for Your Workspace**
2. Click **"Install to Workspace"**
3. Review permissions and click **"Allow"**
4. Copy the **Bot User OAuth Token** (starts with `xoxb-`)

## Step 5: Send Your First Message

Create a file `main.go`:

```go
package main

import (
    "fmt"
    "os"
    "github.com/slack-go/slack"
)

func main() {
    // Initialize client with your bot token
    api := slack.New(os.Getenv("SLACK_BOT_TOKEN"))

    // Send a message to a channel
    channelID := "C1234567890" // Replace with your channel ID
    text := "Hello from my Slack bot!"

    _, _, err := api.PostMessage(
        channelID,
        slack.MsgOptionText(text, false),
    )
    if err != nil {
        fmt.Printf("Error posting message: %s\n", err)
        return
    }

    fmt.Println("Message sent successfully!")
}
```

Set your environment variable:

```bash
export SLACK_BOT_TOKEN="xoxb-your-token-here"
```

Run the program:

```bash
go run main.go
```

## Step 6: Get a Channel ID

To find a channel ID:

1. Open Slack in your browser
2. Navigate to the channel
3. Look at the URL: `https://app.slack.com/client/T.../C1234567890`
4. The last part (`C1234567890`) is your channel ID

Or programmatically:

```go
params := &slack.GetConversationsParameters{
    Types: []string{"public_channel"},
}

channels, _, err := api.GetConversations(params)
if err != nil {
    fmt.Printf("Error: %s\n", err)
    return
}

for _, channel := range channels {
    fmt.Printf("Channel: %s (ID: %s)\n", channel.Name, channel.ID)
}
```

## Step 7: Handle Events (Optional)

For interactive bots, set up Socket Mode:

### Enable Socket Mode

1. In app settings, go to **Socket Mode**
2. Enable Socket Mode
3. Generate an **App-Level Token** with `connections:write` scope
4. Copy the token (starts with `xapp-`)

### Create Event Handler

```go
package main

import (
    "fmt"
    "os"
    "github.com/slack-go/slack"
    "github.com/slack-go/slack/slackevents"
    "github.com/slack-go/slack/socketmode"
)

func main() {
    api := slack.New(
        os.Getenv("SLACK_BOT_TOKEN"),
        slack.OptionAppLevelToken(os.Getenv("SLACK_APP_TOKEN")),
    )

    client := socketmode.New(api)

    go func() {
        for envelope := range client.Events {
            switch envelope.Type {
            case socketmode.EventTypeEventsAPI:
                eventsAPI, ok := envelope.Data.(slackevents.EventsAPIEvent)
                if !ok {
                    continue
                }

                client.Ack(*envelope.Request)

                switch event := eventsAPI.InnerEvent.Data.(type) {
                case *slackevents.AppMentionEvent:
                    fmt.Printf("Bot mentioned: %s\n", event.Text)
                    api.PostMessage(
                        event.Channel,
                        slack.MsgOptionText("Hello! You mentioned me!", false),
                    )
                }
            }
        }
    }()

    fmt.Println("Bot is running...")
    client.Run()
}
```

Set environment variables:

```bash
export SLACK_BOT_TOKEN="xoxb-your-bot-token"
export SLACK_APP_TOKEN="xapp-your-app-token"
```

Run:

```bash
go run main.go
```

### Subscribe to Events

1. Go to **Event Subscriptions** in app settings
2. Enable events
3. Add **Bot Events**:
   - `app_mention` - When bot is @mentioned
   - `message.channels` - Messages in channels
4. Save changes
5. Reinstall app to workspace

## Next Steps

### Learn More

- **Explore Skills**: Ask Claude about specific topics
  - "How do I send a Block Kit message?"
  - "How do I handle button clicks?"
  - "How do I implement OAuth?"

- **Read References**: Check the `references/` directory for detailed guides

- **Try Examples**:
  - Send messages with attachments
  - Create interactive buttons
  - Build a slash command
  - Upload files

### Common Next Features

1. **Send Rich Messages**: Use Block Kit for formatted messages
2. **Handle Interactions**: Respond to button clicks and form submissions
3. **Create Commands**: Build custom slash commands
4. **Multi-Workspace**: Add OAuth for app distribution

## Troubleshooting

### "not_in_channel" Error

Add your bot to the channel:
```
/invite @your-bot-name
```

### "invalid_auth" Error

Check your token:
- Starts with `xoxb-` for bot token
- Starts with `xapp-` for app-level token
- No extra spaces or quotes

### "missing_scope" Error

Add required scopes in OAuth & Permissions, then reinstall the app.

## Resources

- [Slack API Documentation](https://api.slack.com)
- [slack-go/slack GitHub](https://github.com/slack-go/slack)
- [Block Kit Builder](https://app.slack.com/block-kit-builder)
