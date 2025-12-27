# Pagination Patterns

## Overview

Slack API uses cursor-based pagination for most list operations. This guide covers patterns for handling large result sets efficiently.

## Basic Cursor Pagination

### Simple Pagination Loop

```go
func getAllChannels(api *slack.Client) ([]slack.Channel, error) {
    var allChannels []slack.Channel
    cursor := ""

    for {
        params := &slack.GetConversationsParameters{
            Cursor: cursor,
            Limit:  200, // Max items per request
        }

        channels, nextCursor, err := api.GetConversations(params)
        if err != nil {
            return nil, err
        }

        allChannels = append(allChannels, channels...)

        if nextCursor == "" {
            break // No more pages
        }
        cursor = nextCursor
    }

    return allChannels, nil
}
```

## Advanced Pagination Patterns

### Pagination with Context and Cancellation

```go
func getAllUsers(ctx context.Context, api *slack.Client) ([]slack.User, error) {
    var allUsers []slack.User
    cursor := ""

    for {
        select {
        case <-ctx.Done():
            return allUsers, ctx.Err()
        default:
        }

        params := &slack.GetConversationsParameters{
            Cursor: cursor,
            Limit:  200,
        }

        users, nextCursor, err := api.GetUsers()
        if err != nil {
            return nil, err
        }

        allUsers = append(allUsers, users...)

        if nextCursor == "" {
            break
        }
        cursor = nextCursor

        // Optional: rate limiting delay
        time.Sleep(100 * time.Millisecond)
    }

    return allUsers, nil
}
```

### Pagination with Progress Callback

```go
type PaginationProgress struct {
    CurrentPage int
    TotalFetched int
}

func getAllChannelsWithProgress(
    api *slack.Client,
    progressCallback func(PaginationProgress),
) ([]slack.Channel, error) {
    var allChannels []slack.Channel
    cursor := ""
    page := 0

    for {
        page++
        params := &slack.GetConversationsParameters{
            Cursor: cursor,
            Limit:  200,
        }

        channels, nextCursor, err := api.GetConversations(params)
        if err != nil {
            return nil, err
        }

        allChannels = append(allChannels, channels...)

        if progressCallback != nil {
            progressCallback(PaginationProgress{
                CurrentPage:  page,
                TotalFetched: len(allChannels),
            })
        }

        if nextCursor == "" {
            break
        }
        cursor = nextCursor
    }

    return allChannels, nil
}
```

## Message History Pagination

### Get All Messages from Channel

```go
func getAllMessages(api *slack.Client, channelID string) ([]slack.Message, error) {
    var allMessages []slack.Message
    cursor := ""

    for {
        params := &slack.GetConversationHistoryParameters{
            ChannelID: channelID,
            Cursor:    cursor,
            Limit:     100,
        }

        history, err := api.GetConversationHistory(params)
        if err != nil {
            return nil, err
        }

        allMessages = append(allMessages, history.Messages...)

        if !history.HasMore {
            break
        }
        cursor = history.ResponseMetaData.NextCursor
    }

    return allMessages, nil
}
```

### Time-Based Pagination

```go
func getMessagesSince(
    api *slack.Client,
    channelID string,
    since time.Time,
) ([]slack.Message, error) {
    var messages []slack.Message
    cursor := ""

    for {
        params := &slack.GetConversationHistoryParameters{
            ChannelID: channelID,
            Oldest:    fmt.Sprintf("%d", since.Unix()),
            Cursor:    cursor,
            Limit:     100,
        }

        history, err := api.GetConversationHistory(params)
        if err != nil {
            return nil, err
        }

        messages = append(messages, history.Messages...)

        if !history.HasMore {
            break
        }
        cursor = history.ResponseMetaData.NextCursor
    }

    return messages, nil
}
```

## Concurrent Pagination

### Fetch Multiple Channels Concurrently

```go
func getMessagesFromChannels(
    api *slack.Client,
    channelIDs []string,
) (map[string][]slack.Message, error) {
    results := make(map[string][]slack.Message)
    var mu sync.Mutex
    var wg sync.WaitGroup
    errors := make(chan error, len(channelIDs))

    semaphore := make(chan struct{}, 5) // Limit concurrency

    for _, channelID := range channelIDs {
        wg.Add(1)
        go func(chID string) {
            defer wg.Done()
            semaphore <- struct{}{}
            defer func() { <-semaphore }()

            messages, err := getAllMessages(api, chID)
            if err != nil {
                errors <- err
                return
            }

            mu.Lock()
            results[chID] = messages
            mu.Unlock()
        }(channelID)
    }

    wg.Wait()
    close(errors)

    if len(errors) > 0 {
        return results, <-errors
    }

    return results, nil
}
```

## Performance Optimization

### Batch Processing with Pagination

```go
func processChannelsInBatches(
    api *slack.Client,
    processor func([]slack.Channel) error,
    batchSize int,
) error {
    cursor := ""
    var batch []slack.Channel

    for {
        params := &slack.GetConversationsParameters{
            Cursor: cursor,
            Limit:  200,
        }

        channels, nextCursor, err := api.GetConversations(params)
        if err != nil {
            return err
        }

        batch = append(batch, channels...)

        // Process when batch is full or no more pages
        if len(batch) >= batchSize || nextCursor == "" {
            if err := processor(batch); err != nil {
                return err
            }
            batch = batch[:0] // Clear batch
        }

        if nextCursor == "" {
            break
        }
        cursor = nextCursor
    }

    return nil
}
```

## Handling Large Datasets

### Stream Processing Pattern

```go
type ChannelStream struct {
    api    *slack.Client
    cursor string
    buffer []slack.Channel
    done   bool
}

func NewChannelStream(api *slack.Client) *ChannelStream {
    return &ChannelStream{
        api:    api,
        buffer: make([]slack.Channel, 0, 200),
    }
}

func (cs *ChannelStream) Next() (*slack.Channel, error) {
    if len(cs.buffer) == 0 && !cs.done {
        if err := cs.fetchNextPage(); err != nil {
            return nil, err
        }
    }

    if len(cs.buffer) == 0 {
        return nil, io.EOF
    }

    channel := cs.buffer[0]
    cs.buffer = cs.buffer[1:]
    return &channel, nil
}

func (cs *ChannelStream) fetchNextPage() error {
    params := &slack.GetConversationsParameters{
        Cursor: cs.cursor,
        Limit:  200,
    }

    channels, nextCursor, err := cs.api.GetConversations(params)
    if err != nil {
        return err
    }

    cs.buffer = channels
    cs.cursor = nextCursor
    cs.done = nextCursor == ""

    return nil
}

// Usage
stream := NewChannelStream(api)
for {
    channel, err := stream.Next()
    if err == io.EOF {
        break
    }
    if err != nil {
        return err
    }
    // Process channel
    fmt.Printf("Channel: %s\n", channel.Name)
}
```

## Best Practices

1. **Use appropriate limit** - Max 200 for most endpoints, balances requests vs response size
2. **Implement rate limiting** - Add delays between requests to avoid throttling
3. **Handle errors gracefully** - Network issues can occur mid-pagination
4. **Use context for cancellation** - Allow long-running pagination to be cancelled
5. **Consider memory usage** - Process in batches for very large datasets
6. **Store cursors for resumability** - Save cursor to resume after failures
7. **Monitor pagination performance** - Track pages fetched and time taken

## Common Pitfalls

1. **Not checking HasMore/NextCursor** - Causes infinite loops
2. **Ignoring rate limits** - Leads to throttling
3. **Loading entire dataset in memory** - Use streaming for large datasets
4. **Not handling partial failures** - Save progress for resumption
5. **Hardcoding page limits** - Use configurable limits for flexibility
