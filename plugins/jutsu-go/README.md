# jutsu-go

Advanced Go skills for concurrency, error handling, and interfaces.

## Skills

This plugin provides the following skills:

- **go-concurrency** - Goroutines, channels, sync primitives, and concurrent patterns
- **go-error-handling** - Error wrapping, sentinel errors, and error handling best practices
- **go-interfaces** - Interface design, composition, and idiomatic Go patterns

## Installation

Install from the Linehaul AI marketplace:

```
/plugin install jutsu-go@linehaulai-claude-marketplace
```

Or add to your project's `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "jutsu-go@linehaulai-claude-marketplace": true
  }
}
```

## Hooks

This plugin includes automatic hooks that run on `Stop` and `SubagentStop` events when Go files are modified:

| Hook | Event | Timeout |
|------|-------|---------|
| `go fmt ./...` | Stop, SubagentStop | 120s |
| `go vet ./...` | Stop | 60s |
| `go test ./...` | Stop | 900s |

Hooks only trigger when `.go`, `go.mod`, or `go.sum` files are written or edited.

## Usage

Once enabled, Claude will automatically apply these skills when working with Go code. The plugin provides context and expertise for:

- Writing idiomatic Go following best practices
- Implementing concurrent patterns safely
- Designing clean interfaces and error handling
- Catching common mistakes and anti-patterns

## License

MIT
