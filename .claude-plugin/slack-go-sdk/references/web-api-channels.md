# Web API: Channel Management

## Creating Channels

### Create Public Channel

```go
channelName := "project-launch"
isPrivate := false

channel, err := api.CreateConversation(channelName, isPrivate)
if err != nil {
    return fmt.Errorf("failed to create channel: %w", err)
}

fmt.Printf("Created channel: %s (ID: %s)\n", channel.Name, channel.ID)
```

### Create Private Channel

```go
channelName := "executive-team"
isPrivate := true

channel, err := api.CreateConversation(channelName, isPrivate)
```

## Listing Channels

### List All Public Channels

```go
params := &slack.GetConversationsParameters{
    Types: []string{"public_channel"},
    Limit: 100,
}

channels, nextCursor, err := api.GetConversations(params)
if err != nil {
    return err
}

for _, channel := range channels {
    fmt.Printf("- #%s (%s)\n", channel.Name, channel.ID)
}
```

### List Private Channels Bot is Member Of

```go
params := &slack.GetConversationsParameters{
    Types:           []string{"private_channel"},
    ExcludeArchived: true,
}

channels, _, err := api.GetConversations(params)
```

### List All Channel Types with Pagination

```go
func listAllChannels(api *slack.Client) ([]slack.Channel, error) {
    var allChannels []slack.Channel
    cursor := ""

    params := &slack.GetConversationsParameters{
        Types:           []string{"public_channel", "private_channel"},
        ExcludeArchived: true,
        Limit:           200,
    }

    for {
        params.Cursor = cursor

        channels, nextCursor, err := api.GetConversations(params)
        if err != nil {
            return nil, err
        }

        allChannels = append(allChannels, channels...)

        if nextCursor == "" {
            break
        }
        cursor = nextCursor
    }

    return allChannels, nil
}
```

## Channel Information

### Get Channel Details

```go
channel, err := api.GetConversationInfo(&slack.GetConversationInfoInput{
    ChannelID: "C1234567890",
})
if err != nil {
    return err
}

fmt.Printf("Name: %s\n", channel.Name)
fmt.Printf("Topic: %s\n", channel.Topic.Value)
fmt.Printf("Purpose: %s\n", channel.Purpose.Value)
fmt.Printf("Members: %d\n", channel.NumMembers)
```

## Channel Membership

### Invite Users to Channel

```go
channelID := "C1234567890"
userIDs := []string{"U111", "U222", "U333"}

_, err := api.InviteUsersToConversation(channelID, userIDs...)
if err != nil {
    return fmt.Errorf("failed to invite users: %w", err)
}
```

### Remove User from Channel

```go
err := api.KickUserFromConversation(channelID, userID)
```

### List Channel Members

```go
params := &slack.GetUsersInConversationParameters{
    ChannelID: channelID,
    Limit:     100,
}

members, nextCursor, err := api.GetUsersInConversation(params)
if err != nil {
    return err
}

for _, userID := range members {
    fmt.Printf("- %s\n", userID)
}
```

## Channel Metadata

### Set Channel Topic

```go
topic := "Weekly project updates and announcements"

_, err := api.SetTopicOfConversation(channelID, topic)
if err != nil {
    return fmt.Errorf("failed to set topic: %w", err)
}
```

### Set Channel Purpose

```go
purpose := "Coordinate the Q1 product launch"

_, err := api.SetPurposeOfConversation(channelID, purpose)
```

### Rename Channel

```go
newName := "product-launch-q1"

_, err := api.RenameConversation(channelID, newName)
```

## Archiving and Unarchiving

### Archive Channel

```go
err := api.ArchiveConversation(channelID)
if err != nil {
    return fmt.Errorf("failed to archive channel: %w", err)
}
```

### Unarchive Channel

```go
err := api.UnarchiveConversation(channelID)
```

## Channel History

### Get Recent Messages

```go
params := &slack.GetConversationHistoryParameters{
    ChannelID: channelID,
    Limit:     50,
}

history, err := api.GetConversationHistory(params)
if err != nil {
    return err
}

for _, msg := range history.Messages {
    fmt.Printf("[%s] %s: %s\n", msg.Timestamp, msg.User, msg.Text)
}
```

### Get Messages from Date Range

```go
import "time"

// Messages from last 24 hours
yesterday := time.Now().Add(-24 * time.Hour)

params := &slack.GetConversationHistoryParameters{
    ChannelID: channelID,
    Oldest:    fmt.Sprintf("%d", yesterday.Unix()),
    Limit:     100,
}

history, err := api.GetConversationHistory(params)
```

## Production Patterns

### Find or Create Channel

```go
func findOrCreateChannel(api *slack.Client, name string, isPrivate bool) (*slack.Channel, error) {
    // Search for existing channel
    params := &slack.GetConversationsParameters{
        Types: []string{"public_channel", "private_channel"},
        Limit: 1000,
    }

    channels, _, err := api.GetConversations(params)
    if err != nil {
        return nil, err
    }

    for _, ch := range channels {
        if ch.Name == name {
            return &ch, nil
        }
    }

    // Create if not found
    channel, err := api.CreateConversation(name, isPrivate)
    if err != nil {
        return nil, fmt.Errorf("failed to create channel: %w", err)
    }

    return channel, nil
}
```

### Bulk Channel Creation

```go
func createProjectChannels(api *slack.Client, projectName string) error {
    channels := []struct {
        name      string
        isPrivate bool
        topic     string
    }{
        {
            name:      fmt.Sprintf("%s-general", projectName),
            isPrivate: false,
            topic:     "General discussion and updates",
        },
        {
            name:      fmt.Sprintf("%s-dev", projectName),
            isPrivate: false,
            topic:     "Development coordination",
        },
        {
            name:      fmt.Sprintf("%s-leads", projectName),
            isPrivate: true,
            topic:     "Project leadership discussions",
        },
    }

    for _, ch := range channels {
        channel, err := api.CreateConversation(ch.name, ch.isPrivate)
        if err != nil {
            return fmt.Errorf("failed to create %s: %w", ch.name, err)
        }

        if ch.topic != "" {
            _, err = api.SetTopicOfConversation(channel.ID, ch.topic)
            if err != nil {
                // Log but don't fail
                fmt.Printf("Warning: failed to set topic for %s: %v\n", ch.name, err)
            }
        }
    }

    return nil
}
```

## Common Pitfalls

1. **Channel name restrictions** - Must be lowercase, no spaces, < 80 chars
2. **Not checking bot membership** - Verify bot is in channel before operations
3. **Archived channels** - Check channel status before operations
4. **Rate limits** - Implement backoff for bulk operations
5. **Permission errors** - Ensure bot has required scopes (channels:manage, groups:write)
