# Web API: User Operations

## Getting User Information

### Get Single User

```go
user, err := api.GetUserInfo("U1234567890")
if err != nil {
    return err
}

fmt.Printf("Name: %s\n", user.Profile.RealName)
fmt.Printf("Email: %s\n", user.Profile.Email)
fmt.Printf("Display Name: %s\n", user.Profile.DisplayName)
fmt.Printf("Title: %s\n", user.Profile.Title)
fmt.Printf("Status: %s\n", user.Profile.StatusText)
```

### Get Multiple Users

```go
func getUsersInfo(api *slack.Client, userIDs []string) ([]*slack.User, error) {
    var users []*slack.User

    for _, userID := range userIDs {
        user, err := api.GetUserInfo(userID)
        if err != nil {
            return nil, fmt.Errorf("failed to get user %s: %w", userID, err)
        }
        users = append(users, user)
    }

    return users, nil
}
```

## Listing Users

### Get All Workspace Users

```go
users, err := api.GetUsers()
if err != nil {
    return err
}

for _, user := range users {
    if !user.IsBot && !user.Deleted {
        fmt.Printf("- %s (%s) - %s\n", user.Profile.RealName, user.Name, user.ID)
    }
}
```

### Get Active Users Only

```go
users, err := api.GetUsers()
if err != nil {
    return err
}

var activeUsers []slack.User
for _, user := range users {
    if !user.IsBot && !user.Deleted && !user.IsRestricted {
        activeUsers = append(activeUsers, user)
    }
}
```

## User Presence

### Get User Presence

```go
presence, err := api.GetUserPresence("U1234567890")
if err != nil {
    return err
}

fmt.Printf("Presence: %s\n", presence.Presence) // "active" or "away"
```

### Set Bot Presence

```go
err := api.SetUserPresence("auto") // or "away"
if err != nil {
    return err
}
```

## User Profile Updates

### Update Profile Field

```go
// Update status
err := api.SetUserCustomStatus(
    "In a meeting",
    ":calendar:",
    time.Now().Add(1*time.Hour).Unix(), // Expires in 1 hour
)
```

### Clear Status

```go
err := api.UnsetUserCustomStatus()
```

## User Groups

### Get User Groups

```go
groups, err := api.GetUserGroups(
    slack.GetUserGroupsOptionIncludeUsers(true),
)
if err != nil {
    return err
}

for _, group := range groups {
    fmt.Printf("Group: %s (%s)\n", group.Name, group.ID)
    fmt.Printf("Members: %d\n", len(group.Users))
}
```

### Get Members of User Group

```go
func getUserGroupMembers(api *slack.Client, groupID string) ([]string, error) {
    groups, err := api.GetUserGroups(
        slack.GetUserGroupsOptionIncludeUsers(true),
    )
    if err != nil {
        return nil, err
    }

    for _, group := range groups {
        if group.ID == groupID {
            return group.Users, nil
        }
    }

    return nil, fmt.Errorf("user group %s not found", groupID)
}
```

## User Lookups

### Find User by Email

```go
func findUserByEmail(api *slack.Client, email string) (*slack.User, error) {
    user, err := api.GetUserByEmail(email)
    if err != nil {
        return nil, fmt.Errorf("user not found: %w", err)
    }
    return user, nil
}
```

### Find User by Display Name

```go
func findUserByName(api *slack.Client, displayName string) (*slack.User, error) {
    users, err := api.GetUsers()
    if err != nil {
        return nil, err
    }

    for _, user := range users {
        if user.Profile.DisplayName == displayName || user.Name == displayName {
            return &user, nil
        }
    }

    return nil, fmt.Errorf("user %s not found", displayName)
}
```

## Direct Messages

### Open DM Channel

```go
_, _, channelID, err := api.OpenConversation(&slack.OpenConversationParameters{
    Users: []string{"U1234567890"},
})
if err != nil {
    return err
}

// Send DM
_, _, err = api.PostMessage(
    channelID,
    slack.MsgOptionText("Hello via DM!", false),
)
```

### Send DM to Multiple Users

```go
func sendDirectMessage(api *slack.Client, userID, message string) error {
    _, _, channelID, err := api.OpenConversation(&slack.OpenConversationParameters{
        Users: []string{userID},
    })
    if err != nil {
        return fmt.Errorf("failed to open DM: %w", err)
    }

    _, _, err = api.PostMessage(channelID, slack.MsgOptionText(message, false))
    if err != nil {
        return fmt.Errorf("failed to send DM: %w", err)
    }

    return nil
}
```

## Production Patterns

### User Cache

```go
type UserCache struct {
    api   *slack.Client
    cache map[string]*slack.User
    mu    sync.RWMutex
    ttl   time.Duration
}

func NewUserCache(api *slack.Client, ttl time.Duration) *UserCache {
    return &UserCache{
        api:   api,
        cache: make(map[string]*slack.User),
        ttl:   ttl,
    }
}

func (uc *UserCache) GetUser(userID string) (*slack.User, error) {
    uc.mu.RLock()
    user, exists := uc.cache[userID]
    uc.mu.RUnlock()

    if exists {
        return user, nil
    }

    // Fetch from API
    user, err := uc.api.GetUserInfo(userID)
    if err != nil {
        return nil, err
    }

    // Store in cache
    uc.mu.Lock()
    uc.cache[userID] = user
    uc.mu.Unlock()

    // Auto-expire after TTL
    go func() {
        time.Sleep(uc.ttl)
        uc.mu.Lock()
        delete(uc.cache, userID)
        uc.mu.Unlock()
    }()

    return user, nil
}
```

### Batch User Lookup

```go
func batchGetUsers(api *slack.Client, userIDs []string) (map[string]*slack.User, error) {
    result := make(map[string]*slack.User)
    var mu sync.Mutex
    var wg sync.WaitGroup
    errors := make(chan error, len(userIDs))

    // Limit concurrency
    semaphore := make(chan struct{}, 10)

    for _, userID := range userIDs {
        wg.Add(1)
        go func(id string) {
            defer wg.Done()
            semaphore <- struct{}{}
            defer func() { <-semaphore }()

            user, err := api.GetUserInfo(id)
            if err != nil {
                errors <- fmt.Errorf("failed to get user %s: %w", id, err)
                return
            }

            mu.Lock()
            result[id] = user
            mu.Unlock()
        }(userID)
    }

    wg.Wait()
    close(errors)

    // Check for errors
    if len(errors) > 0 {
        return result, <-errors
    }

    return result, nil
}
```

### User Mention Formatter

```go
func formatUserMention(userID string) string {
    return fmt.Sprintf("<@%s>", userID)
}

func formatUserListMention(userIDs []string) string {
    mentions := make([]string, len(userIDs))
    for i, id := range userIDs {
        mentions[i] = fmt.Sprintf("<@%s>", id)
    }
    return strings.Join(mentions, ", ")
}
```

## Common Pitfalls

1. **Not caching user data** - API calls are rate-limited, cache frequently accessed users
2. **Forgetting bot vs human users** - Filter `IsBot` field
3. **Deleted users** - Check `Deleted` field before operations
4. **Email privacy** - Some users hide emails, check for empty string
5. **Rate limits on bulk lookups** - Implement concurrency limits and backoff
