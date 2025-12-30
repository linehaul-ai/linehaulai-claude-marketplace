# Socket Mode Setup

## Overview

Socket Mode uses WebSocket connections to receive events, allowing apps to run behind firewalls without public URLs.

## Basic Setup

```go
import (
    "github.com/slack-go/slack"
    "github.com/slack-go/slack/socketmode"
)

func main() {
    api := slack.New(
        os.Getenv("SLACK_BOT_TOKEN"),
        slack.OptionAppLevelToken(os.Getenv("SLACK_APP_TOKEN")),
        slack.OptionDebug(true),
    )

    client := socketmode.New(
        api,
        socketmode.OptionDebug(true),
    )

    go handleSocketModeEvents(client)

    if err := client.Run(); err != nil {
        log.Fatal(err)
    }
}
```

## Event Handler Pattern

```go
func handleSocketModeEvents(client *socketmode.Client) {
    for envelope := range client.Events {
        switch envelope.Type {
        case socketmode.EventTypeEventsAPI:
            handleEventsAPI(envelope, client)

        case socketmode.EventTypeInteractive:
            handleInteractive(envelope, client)

        case socketmode.EventTypeSlashCommand:
            handleSlashCommand(envelope, client)

        case socketmode.EventTypeConnectionError:
            log.Printf("Connection error: %v\n", envelope.Data)
        }
    }
}
```

## Production Pattern

```go
type EventHandler struct {
    api    *slack.Client
    botID  string
}

func (h *EventHandler) HandleEvent(envelope socketmode.Event, client *socketmode.Client) {
    client.Ack(*envelope.Request)

    eventsAPIEvent, ok := envelope.Data.(slackevents.EventsAPIEvent)
    if !ok {
        return
    }

    switch eventsAPIEvent.InnerEvent.Type {
    case string(slackevents.Message):
        h.handleMessage(eventsAPIEvent.InnerEvent.Data.(*slackevents.MessageEvent))

    case string(slackevents.AppMention):
        h.handleAppMention(eventsAPIEvent.InnerEvent.Data.(*slackevents.AppMentionEvent))
    }
}
```

## Connection Lifecycle

- Automatic reconnection on disconnect
- Heartbeat mechanism for connection health
- Graceful shutdown support
- Error handling for connection issues

## Best Practices

1. Always acknowledge events with `client.Ack()`
2. Handle events in goroutines for non-blocking processing
3. Implement reconnection logic
4. Use context for cancellation
5. Monitor connection health
