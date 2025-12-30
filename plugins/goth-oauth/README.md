# Goth OAuth Plugin

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Go](https://img.shields.io/badge/Go-1.21+-00ADD8)
![Goth](https://img.shields.io/badge/Goth-1.80+-purple)

Expert guidance for implementing OAuth authentication in Go using [github.com/markbates/goth](https://github.com/markbates/goth).

## Overview

This plugin provides comprehensive guidance for:
- Setting up OAuth authentication with Goth
- Configuring providers (Google, Microsoft/Azure AD)
- Integrating with the Echo web framework
- Implementing secure session management
- Following security best practices

## What's Included

- **3 Skills** for progressive learning and quick reference
- **1 Expert Agent** for troubleshooting and architecture decisions
- **4 Reference Guides** for detailed provider and security documentation

## Skills

### goth-fundamentals

Core concepts and basic usage:
- Package installation and imports
- Provider and Session interfaces
- Gothic helper package
- Basic authentication flow
- Environment variables pattern

**Triggers**: "goth setup", "oauth go", "authentication golang", "goth package"

### goth-providers

Provider configuration and management:
- Provider registration pattern
- Google OAuth setup
- Microsoft (Azure AD) setup
- Multiple providers pattern
- Callback URL configuration

**Triggers**: "add provider", "google oauth", "microsoft login", "azure ad"

### goth-echo-security

Framework integration and security:
- Echo framework integration
- Session management
- Cookie and Redis stores
- Security best practices
- Token refresh patterns

**Triggers**: "goth echo", "oauth security", "session management", "gorilla sessions"

## Expert Agent

### goth-expert

For complex troubleshooting and architecture decisions:
- Debug OAuth flow issues
- Provider selection guidance
- Security review
- Implementation best practices

## Quick Start

```go
package main

import (
    "net/http"
    "os"

    "github.com/markbates/goth"
    "github.com/markbates/goth/gothic"
    "github.com/markbates/goth/providers/google"
)

func init() {
    goth.UseProviders(
        google.New(
            os.Getenv("GOOGLE_CLIENT_ID"),
            os.Getenv("GOOGLE_CLIENT_SECRET"),
            "http://localhost:3000/auth/google/callback",
            "email", "profile",
        ),
    )
}

func main() {
    http.HandleFunc("/auth/google", func(w http.ResponseWriter, r *http.Request) {
        gothic.BeginAuthHandler(w, r)
    })

    http.HandleFunc("/auth/google/callback", func(w http.ResponseWriter, r *http.Request) {
        user, err := gothic.CompleteUserAuth(w, r)
        if err != nil {
            http.Error(w, err.Error(), 500)
            return
        }
        // User authenticated! user.Email, user.Name available
    })

    http.ListenAndServe(":3000", nil)
}
```

## Reference Documentation

| Guide | Description |
|-------|-------------|
| [google-oauth-setup.md](references/google-oauth-setup.md) | Google Cloud Console configuration |
| [microsoft-oauth-setup.md](references/microsoft-oauth-setup.md) | Azure AD app registration |
| [session-storage-options.md](references/session-storage-options.md) | Cookie vs Redis vs PostgreSQL |
| [security-checklist.md](references/security-checklist.md) | Pre-deployment security verification |

## Environment Variables

```bash
# Google OAuth
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret

# Microsoft OAuth
AZURE_CLIENT_ID=your-azure-app-id
AZURE_CLIENT_SECRET=your-azure-secret

# Session
SESSION_SECRET=your-32-byte-random-string
```

## Related Plugins

- **golang-orchestrator** - Go/Echo backend development patterns
- **supabase** - Database design and RLS policies

## Requirements

- Go 1.21+
- github.com/markbates/goth v1.80+
- github.com/gorilla/sessions v1.2+

## Author

Linehaul AI - support@linehaul.ai

## License

MIT
