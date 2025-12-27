# Comprehensive Event Types

## Message Events

### message
New message posted to channel:
```go
func handleMessage(event *slackevents.MessageEvent) {
    fmt.Printf("User %s said: %s\n", event.User, event.Text)
}
```

### message_changed
Message edited:
```go
func handleMessageChanged(event *slackevents.MessageEvent) {
    if event.SubType == "message_changed" {
        fmt.Printf("Message updated to: %s\n", event.Message.Text)
    }
}
```

### message_deleted
Message deleted:
```go
func handleMessageDeleted(event *slackevents.MessageEvent) {
    if event.SubType == "message_deleted" {
        fmt.Printf("Message %s was deleted\n", event.DeletedTimestamp)
    }
}
```

## Interaction Events

### app_mention
Bot mentioned in message:
```go
func handleAppMention(event *slackevents.AppMentionEvent) {
    text := strings.TrimPrefix(event.Text, fmt.Sprintf("<@%s>", botID))
    // Process command
}
```

### reaction_added / reaction_removed
User added/removed emoji reaction:
```go
func handleReactionAdded(event *slackevents.ReactionAddedEvent) {
    fmt.Printf("Reaction :%s: added by %s\n", event.Reaction, event.User)
}
```

## Channel Events

### channel_created
New channel created:
```go
func handleChannelCreated(event *slackevents.ChannelCreatedEvent) {
    fmt.Printf("Channel created: %s (%s)\n", event.Channel.Name, event.Channel.ID)
}
```

### channel_rename
Channel renamed:
```go
func handleChannelRename(event *slackevents.ChannelRenameEvent) {
    fmt.Printf("Channel renamed to: %s\n", event.Channel.Name)
}
```

### channel_archive / channel_unarchive
Channel archived or unarchived.

## Team Events

### team_join
New member joined workspace:
```go
func handleTeamJoin(event *slackevents.TeamJoinEvent) {
    fmt.Printf("Welcome %s!\n", event.User.Profile.RealName)
}
```

### user_change
User profile updated:
```go
func handleUserChange(event *slackevents.UserChangeEvent) {
    fmt.Printf("User %s updated profile\n", event.User.ID)
}
```

## Event Filtering

```go
func shouldProcessEvent(event *slackevents.MessageEvent, botID string) bool {
    // Ignore bot messages
    if event.BotID != "" {
        return false
    }

    // Ignore own messages
    if event.User == botID {
        return false
    }

    // Ignore thread replies (optional)
    if event.ThreadTimestamp != "" && event.ThreadTimestamp != event.TimeStamp {
        return false
    }

    return true
}
```
