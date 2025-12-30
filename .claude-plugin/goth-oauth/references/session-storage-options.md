# Session Storage Options

Comparison of session storage backends for Goth OAuth implementations.

## Overview

| Storage | Best For | Pros | Cons |
|---------|----------|------|------|
| Cookie Store | Single server, simple apps | Zero infrastructure, fast | Size limit (4KB), all data in cookie |
| Redis | Multi-server, high traffic | Fast, scalable, easy to clear | Requires Redis server |
| PostgreSQL | Audit requirements, existing DB | Durable, auditable, queryable | Slower than in-memory |
| Filesystem | Simple multi-instance | No external dependencies | Shared filesystem needed |

## Cookie Store (Default)

Gothic uses gorilla/sessions CookieStore by default.

### Configuration

```go
import "github.com/gorilla/sessions"

func initCookieStore() {
    key := []byte(os.Getenv("SESSION_SECRET"))

    store := sessions.NewCookieStore(key)
    store.MaxAge(86400 * 30)  // 30 days
    store.Options.Path = "/"
    store.Options.HttpOnly = true
    store.Options.Secure = true  // HTTPS only
    store.Options.SameSite = http.SameSiteLaxMode

    gothic.Store = store
}
```

### Encrypted Cookie Store

For sensitive data, use encrypted cookies:

```go
import "github.com/gorilla/securecookie"

func initEncryptedCookieStore() {
    // 32-byte keys for AES-256
    hashKey := []byte(os.Getenv("SESSION_HASH_KEY"))   // 32 bytes
    blockKey := []byte(os.Getenv("SESSION_BLOCK_KEY")) // 32 bytes

    store := sessions.NewCookieStore(hashKey, blockKey)
    gothic.Store = store
}
```

### Pros
- No external dependencies
- Fast (no network calls)
- Automatically scales
- No session cleanup needed

### Cons
- 4KB size limit
- All data sent with every request
- Can't invalidate from server
- Vulnerable to replay attacks

### When to Use
- Single-server deployments
- Simple applications
- Development environments
- Minimal session data

## Redis Store

Ideal for distributed systems and high-traffic applications.

### Installation

```bash
go get github.com/rbcervilla/redisstore/v9
```

### Configuration

```go
import (
    "github.com/redis/go-redis/v9"
    "github.com/rbcervilla/redisstore/v9"
)

func initRedisStore() {
    client := redis.NewClient(&redis.Options{
        Addr:     os.Getenv("REDIS_URL"),
        Password: os.Getenv("REDIS_PASSWORD"),
        DB:       0,
    })

    store, err := redisstore.NewRedisStore(context.Background(), client)
    if err != nil {
        log.Fatal(err)
    }

    store.KeyPrefix("session:")
    store.Options(sessions.Options{
        Path:     "/",
        MaxAge:   86400 * 30,
        HttpOnly: true,
        Secure:   true,
        SameSite: http.SameSiteLaxMode,
    })

    gothic.Store = store
}
```

### Redis Sentinel (High Availability)

```go
client := redis.NewFailoverClient(&redis.FailoverOptions{
    MasterName:    "mymaster",
    SentinelAddrs: []string{":26379", ":26380", ":26381"},
    Password:      os.Getenv("REDIS_PASSWORD"),
})
```

### Redis Cluster

```go
client := redis.NewClusterClient(&redis.ClusterOptions{
    Addrs:    []string{":7000", ":7001", ":7002"},
    Password: os.Getenv("REDIS_PASSWORD"),
})
```

### Pros
- Extremely fast
- Horizontally scalable
- Supports session expiration
- Can invalidate sessions from server
- Small cookie (just session ID)

### Cons
- Requires Redis server
- Additional infrastructure
- Data loss if Redis restarts (without persistence)

### When to Use
- Multi-server deployments
- High-traffic applications
- Need to invalidate sessions server-side
- Microservices architecture

## PostgreSQL Store

For applications requiring session auditing or already using PostgreSQL.

### Installation

```bash
go get github.com/antonlindstrom/pgstore
```

### Configuration

```go
import "github.com/antonlindstrom/pgstore"

func initPgStore() {
    store, err := pgstore.NewPGStore(
        os.Getenv("DATABASE_URL"),
        []byte(os.Getenv("SESSION_SECRET")),
    )
    if err != nil {
        log.Fatal(err)
    }

    store.Options = &sessions.Options{
        Path:     "/",
        MaxAge:   86400 * 30,
        HttpOnly: true,
        Secure:   true,
        SameSite: http.SameSiteLaxMode,
    }

    // Cleanup expired sessions
    defer store.Close()
    store.StopCleanup(store.Cleanup(time.Hour))

    gothic.Store = store
}
```

### With pgx Pool

```go
import "github.com/antonlindstrom/pgstore"

func initPgStoreWithPool() {
    store, err := pgstore.NewPGStoreFromPool(
        dbPool,  // *pgxpool.Pool
        []byte(os.Getenv("SESSION_SECRET")),
    )
    if err != nil {
        log.Fatal(err)
    }

    gothic.Store = store
}
```

### Session Table Schema

pgstore creates this table automatically:

```sql
CREATE TABLE http_sessions (
    id BYTEA PRIMARY KEY,
    key BYTEA,
    data BYTEA,
    created_on TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    modified_on TIMESTAMPTZ,
    expires_on TIMESTAMPTZ
);

CREATE INDEX http_sessions_expiry_idx ON http_sessions (expires_on);
```

### Custom Session Queries

For audit purposes:

```sql
-- Active sessions for a user
SELECT id, created_on, modified_on
FROM http_sessions
WHERE data LIKE '%"user_id":"123"%'
AND expires_on > NOW();

-- Sessions by provider
SELECT COUNT(*)
FROM http_sessions
WHERE data LIKE '%"provider":"google"%';
```

### Pros
- Durable storage
- Auditable (can query sessions)
- Works with existing PostgreSQL
- Transaction support

### Cons
- Slower than in-memory stores
- Requires periodic cleanup
- Database connection overhead

### When to Use
- Compliance/audit requirements
- Need to query sessions
- Already using PostgreSQL
- Session data persistence critical

## Filesystem Store

For simple multi-instance deployments with shared filesystem.

### Installation

```bash
go get github.com/gorilla/sessions
```

### Configuration

```go
import "github.com/gorilla/sessions"

func initFilesystemStore() {
    store := sessions.NewFilesystemStore(
        "/var/lib/app/sessions",  // Shared path
        []byte(os.Getenv("SESSION_SECRET")),
    )

    store.MaxAge(86400 * 30)
    store.Options.Path = "/"
    store.Options.HttpOnly = true
    store.Options.Secure = true

    gothic.Store = store
}
```

### Pros
- No external dependencies beyond filesystem
- Simple to configure
- Works with NFS or similar

### Cons
- Requires shared filesystem
- Filesystem I/O overhead
- Manual cleanup needed
- Not suitable for containerized environments

### When to Use
- Simple multi-instance with shared storage
- Legacy infrastructure
- No Redis/database available

## Comparison Table

| Feature | Cookie | Redis | PostgreSQL | Filesystem |
|---------|--------|-------|------------|------------|
| Speed | Fast | Very Fast | Moderate | Slow |
| Size Limit | 4KB | None | None | None |
| Server Invalidation | No | Yes | Yes | Yes |
| Persistence | Yes | Optional | Yes | Yes |
| Scalability | Automatic | Excellent | Good | Limited |
| Infrastructure | None | Redis | PostgreSQL | Shared FS |
| Session Query | No | Limited | Yes | No |
| Cleanup | Automatic | Automatic | Required | Required |

## Security Considerations

### All Stores

- Use strong SESSION_SECRET (32+ random bytes)
- Set `Secure: true` in production
- Set `HttpOnly: true` always
- Use `SameSite: Lax` or `Strict`
- Implement session regeneration on login

### Cookie Store Specific

- Use encrypted cookies for sensitive data
- Keep session data minimal
- Never store access tokens in unencrypted cookies

### Redis Specific

- Use authentication (`Password` option)
- Use TLS in production
- Set appropriate TTLs
- Consider Redis ACLs

### PostgreSQL Specific

- Use prepared statements (automatic with pgstore)
- Encrypt sensitive columns if needed
- Implement cleanup job

## Migration Between Stores

When migrating between stores:

1. Deploy new store configuration
2. New sessions use new store
3. Old sessions expire naturally
4. No explicit migration needed

For immediate migration:
1. Force all users to re-authenticate
2. Clear old session data
3. Deploy new store
