# Google OAuth Setup Guide

Complete guide for configuring Google OAuth with Goth.

## Google Cloud Console Setup

### Step 1: Create or Select Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click project dropdown at top
3. Click "New Project" or select existing project
4. Enter project name and click "Create"

### Step 2: Enable APIs

1. Navigate to "APIs & Services" → "Library"
2. Search for and enable:
   - "Google+ API" (for basic profile)
   - Or "People API" (newer, recommended)

### Step 3: Configure OAuth Consent Screen

1. Go to "APIs & Services" → "OAuth consent screen"
2. Select user type:
   - **Internal**: Only users in your Google Workspace org
   - **External**: Any Google user (requires verification for production)
3. Fill in required fields:
   - App name
   - User support email
   - Developer contact email
4. Add scopes:
   - `email`
   - `profile`
   - `openid`
5. Add test users (required for external apps in testing)

### Step 4: Create OAuth Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. Select "Web application"
4. Configure:
   - **Name**: Your app name
   - **Authorized JavaScript origins**: (optional)
   - **Authorized redirect URIs**: Add your callback URLs

### Redirect URI Configuration

Add all environments:

```
# Development
http://localhost:3000/auth/google/callback

# Staging
https://staging.yourdomain.com/auth/google/callback

# Production
https://yourdomain.com/auth/google/callback
```

### Step 5: Get Credentials

1. Copy the **Client ID** and **Client secret**
2. Store securely (never commit to git)

## Goth Configuration

### Basic Setup

```go
import (
    "github.com/markbates/goth"
    "github.com/markbates/goth/providers/google"
)

func init() {
    goth.UseProviders(
        google.New(
            os.Getenv("GOOGLE_CLIENT_ID"),
            os.Getenv("GOOGLE_CLIENT_SECRET"),
            os.Getenv("GOOGLE_CALLBACK_URL"),
            "email", "profile",
        ),
    )
}
```

### Environment Variables

```bash
# .env
GOOGLE_CLIENT_ID=123456789-abc.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-xxxxxxxxxxxx
GOOGLE_CALLBACK_URL=http://localhost:3000/auth/google/callback
```

## Available Scopes

### Basic Scopes

| Scope | Description |
|-------|-------------|
| `email` | User's email address |
| `profile` | Name, picture, locale |
| `openid` | OpenID Connect (for ID token) |

### Extended Scopes

| Scope | Description |
|-------|-------------|
| `https://www.googleapis.com/auth/calendar.readonly` | Read calendars |
| `https://www.googleapis.com/auth/calendar` | Read/write calendars |
| `https://www.googleapis.com/auth/drive.readonly` | Read Drive files |
| `https://www.googleapis.com/auth/drive.file` | Access Drive files created by app |
| `https://www.googleapis.com/auth/gmail.readonly` | Read Gmail messages |

### Requesting Extended Scopes

```go
google.New(
    clientID,
    clientSecret,
    callbackURL,
    "email",
    "profile",
    "https://www.googleapis.com/auth/calendar.readonly",
)
```

## User Data Returned

```go
user, _ := gothic.CompleteUserAuth(w, r)

// Available fields
user.Email        // "user@gmail.com"
user.Name         // "John Doe"
user.FirstName    // "John"
user.LastName     // "Doe"
user.NickName     // May be empty
user.AvatarURL    // Profile picture URL
user.UserID       // Google's unique user ID
user.AccessToken  // For Google API calls
user.RefreshToken // For token refresh (if offline access requested)
user.ExpiresAt    // Token expiration time
user.IDToken      // JWT with claims (if openid scope)
```

## Offline Access (Refresh Tokens)

To get refresh tokens for long-lived access:

```go
// Request offline access
google.New(
    clientID,
    clientSecret,
    callbackURL,
    "email", "profile",
).SetAccessType("offline").SetPrompt("consent")
```

Note: `SetPrompt("consent")` forces consent screen to always appear, ensuring refresh token is returned.

## Using Access Token with Google APIs

```go
import "google.golang.org/api/calendar/v3"

func getCalendar(accessToken string) (*calendar.Events, error) {
    ctx := context.Background()

    tokenSource := oauth2.StaticTokenSource(&oauth2.Token{
        AccessToken: accessToken,
    })

    client := oauth2.NewClient(ctx, tokenSource)
    calendarService, err := calendar.NewService(ctx, option.WithHTTPClient(client))
    if err != nil {
        return nil, err
    }

    return calendarService.Events.List("primary").Do()
}
```

## Publishing Your App

For production use with external users:

1. Complete OAuth consent screen verification
2. Provide privacy policy and terms of service URLs
3. Verify domain ownership
4. Submit for Google review (may take several days)

Until verified, app is limited to 100 test users.

## Common Issues

### "Access blocked: App has not completed verification"

- App is external and not verified
- Add user as test user in consent screen
- Or complete verification process

### "redirect_uri_mismatch"

- Callback URL doesn't match exactly
- Check protocol (http vs https)
- Check port number
- Check for trailing slash

### "invalid_scope"

- Requested scope not enabled in console
- Scope syntax is wrong
- API not enabled in project

## Security Recommendations

1. Use environment variables for credentials
2. Never expose client secret in frontend code
3. Use HTTPS in production
4. Request minimum necessary scopes
5. Regularly rotate client secrets
6. Monitor OAuth activity in console
