# Advanced Client Configuration

## Custom HTTP Client

Use a custom HTTP client for advanced control over requests:

```go
import (
    "net/http"
    "time"
    "github.com/slack-go/slack"
)

httpClient := &http.Client{
    Timeout: 30 * time.Second,
    Transport: &http.Transport{
        MaxIdleConns:        100,
        MaxIdleConnsPerHost: 100,
        IdleConnTimeout:     90 * time.Second,
    },
}

api := slack.New(
    "xoxb-your-bot-token",
    slack.OptionHTTPClient(httpClient),
)
```

## Debug Mode Configuration

Enable debug logging for development and troubleshooting:

```go
api := slack.New(
    token,
    slack.OptionDebug(true),
    slack.OptionLog(log.New(os.Stdout, "slack-bot: ", log.Lshortfile|log.LstdFlags)),
)
```

Custom logger implementation:

```go
type CustomLogger struct {
    logger *log.Logger
}

func (l *CustomLogger) Output(calldepth int, s string) error {
    return l.logger.Output(calldepth, s)
}

customLogger := &CustomLogger{
    logger: log.New(os.Stdout, "[SLACK] ", log.LstdFlags),
}

api := slack.New(
    token,
    slack.OptionLog(customLogger),
)
```

## Rate Limiting Strategies

Implement exponential backoff for rate limit handling:

```go
import "math"

func postMessageWithRetry(api *slack.Client, channelID, text string, maxRetries int) error {
    var err error
    for attempt := 0; attempt < maxRetries; attempt++ {
        _, _, err = api.PostMessage(
            channelID,
            slack.MsgOptionText(text, false),
        )

        if err == nil {
            return nil
        }

        if rateLimitErr, ok := err.(*slack.RateLimitedError); ok {
            // Wait for the specified retry duration
            waitDuration := rateLimitErr.RetryAfter
            if waitDuration == 0 {
                // Exponential backoff if RetryAfter not provided
                waitDuration = time.Duration(math.Pow(2, float64(attempt))) * time.Second
            }

            time.Sleep(waitDuration)
            continue
        }

        // Non-rate-limit error, return immediately
        return err
    }

    return fmt.Errorf("max retries exceeded: %w", err)
}
```

## Connection Pooling

Configure connection pooling for high-throughput applications:

```go
transport := &http.Transport{
    MaxIdleConns:          100,
    MaxIdleConnsPerHost:   100,
    MaxConnsPerHost:       100,
    IdleConnTimeout:       90 * time.Second,
    TLSHandshakeTimeout:   10 * time.Second,
    ExpectContinueTimeout: 1 * time.Second,
}

httpClient := &http.Client{
    Transport: transport,
    Timeout:   30 * time.Second,
}

api := slack.New(token, slack.OptionHTTPClient(httpClient))
```

## Custom API URL

For Slack Enterprise Grid or testing with mock servers:

```go
api := slack.New(
    token,
    slack.OptionAPIURL("https://custom-slack-api.example.com/api/"),
)
```

## Configuration from Environment

Production-ready configuration pattern:

```go
package config

import (
    "os"
    "time"
    "github.com/slack-go/slack"
)

type Config struct {
    SlackToken    string
    Debug         bool
    HTTPTimeout   time.Duration
}

func LoadFromEnv() *Config {
    return &Config{
        SlackToken:  os.Getenv("SLACK_BOT_TOKEN"),
        Debug:       os.Getenv("SLACK_DEBUG") == "true",
        HTTPTimeout: 30 * time.Second,
    }
}

func (c *Config) NewSlackClient() *slack.Client {
    options := []slack.Option{}

    if c.Debug {
        options = append(options, slack.OptionDebug(true))
    }

    httpClient := &http.Client{
        Timeout: c.HTTPTimeout,
    }
    options = append(options, slack.OptionHTTPClient(httpClient))

    return slack.New(c.SlackToken, options...)
}
```

Usage:

```go
cfg := config.LoadFromEnv()
api := cfg.NewSlackClient()
```

## Production Best Practices

1. **Never hardcode tokens** - Use environment variables or secrets managers
2. **Set reasonable timeouts** - Prevent hanging connections
3. **Configure connection pooling** - Optimize for throughput
4. **Implement retry logic** - Handle transient failures gracefully
5. **Use structured logging** - Make debugging easier
6. **Monitor rate limits** - Track API usage metrics
