# Scopes and Permissions Guide

## Bot Scopes

### Messaging
- `chat:write` - Send messages as bot
- `chat:write.public` - Post to channels bot isn't member of
- `chat:write.customize` - Send messages with custom username/icon

### Channels
- `channels:read` - View public channels
- `channels:manage` - Create and manage public channels
- `channels:join` - Join public channels
- `channels:history` - View message history in public channels

### Users
- `users:read` - View users in workspace
- `users:read.email` - View user email addresses
- `users:write` - Modify user information

### Files
- `files:read` - View files
- `files:write` - Upload and share files

### Reactions
- `reactions:read` - View reactions
- `reactions:write` - Add/remove reactions

## User Scopes

Used when acting on behalf of specific user:
- `chat:write` - Send messages as user
- `users:read` - View user information
- `search:read` - Search messages and files

## Scope Selection Guide

### Basic Bot
```
chat:write
channels:read
users:read
```

### Interactive Bot
```
chat:write
channels:read
users:read
reactions:write
commands
```

### Full-Featured Bot
```
chat:write
chat:write.public
channels:read
channels:manage
users:read
users:read.email
files:read
files:write
reactions:read
reactions:write
commands
```

## Requesting Scopes

```go
scopes := []string{
    "chat:write",
    "channels:read",
    "users:read",
}
scopeString := strings.Join(scopes, ",")
```
