# Installation Guide

## Prerequisites

- Go 1.21 or later
- A registered OAuth application with your provider(s)
- Environment for storing secrets securely

## Install Goth Package

```bash
go get github.com/markbates/goth
```

## Install Provider Packages

Install only the providers you need:

```bash
# Google
go get github.com/markbates/goth/providers/google

# Microsoft (Azure AD v2)
go get github.com/markbates/goth/providers/azureadv2

# Other common providers
go get github.com/markbates/goth/providers/github
go get github.com/markbates/goth/providers/facebook
```

## Install Session Store

Gothic uses gorilla/sessions by default:

```bash
go get github.com/gorilla/sessions
```

For Redis sessions:

```bash
go get github.com/rbcervilla/redisstore/v9
go get github.com/redis/go-redis/v9
```

For PostgreSQL sessions:

```bash
go get github.com/antonlindstrom/pgstore
```

## Environment Setup

Create a `.env` file (never commit this):

```bash
# Required
SESSION_SECRET=your-32-byte-random-string

# Google OAuth
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret

# Microsoft OAuth (optional)
AZURE_CLIENT_ID=your-azure-app-id
AZURE_CLIENT_SECRET=your-azure-secret
```

Generate a secure session secret:

```bash
openssl rand -base64 32
```

## Load Environment Variables

Using godotenv:

```bash
go get github.com/joho/godotenv
```

```go
import "github.com/joho/godotenv"

func init() {
    godotenv.Load()
}
```

## Verify Installation

Create a test file:

```go
package main

import (
    "fmt"
    "os"

    "github.com/markbates/goth"
    "github.com/markbates/goth/providers/google"
)

func main() {
    goth.UseProviders(
        google.New(
            os.Getenv("GOOGLE_CLIENT_ID"),
            os.Getenv("GOOGLE_CLIENT_SECRET"),
            "http://localhost:3000/callback",
        ),
    )

    providers := goth.GetProviders()
    fmt.Printf("Registered %d providers\n", len(providers))
    for name := range providers {
        fmt.Printf("  - %s\n", name)
    }
}
```

Run:

```bash
go run main.go
# Output: Registered 1 providers
#           - google
```

## Next Steps

1. Configure your OAuth provider (see reference guides)
2. Implement authentication routes
3. Set up session management
4. Review security checklist before deployment

See [QUICK_START.md](QUICK_START.md) for a complete working example.
