# Microsoft (Azure AD) OAuth Setup Guide

Complete guide for configuring Microsoft/Azure AD OAuth with Goth.

## Azure Portal Setup

### Step 1: Access Azure AD

1. Go to [Azure Portal](https://portal.azure.com/)
2. Navigate to "Azure Active Directory"
3. Click "App registrations" in the left menu

### Step 2: Register Application

1. Click "New registration"
2. Fill in:
   - **Name**: Your application name
   - **Supported account types**: Choose based on your needs
   - **Redirect URI**: Select "Web" and enter callback URL

### Account Types

| Type | Description |
|------|-------------|
| Single tenant | Only accounts in your Azure AD directory |
| Multitenant | Accounts in any Azure AD directory |
| Multitenant + personal | Any Azure AD + personal Microsoft accounts |
| Personal only | Only personal Microsoft accounts (Xbox, Outlook.com) |

### Step 3: Configure Redirect URIs

1. Go to "Authentication" in your app
2. Under "Platform configurations" → "Web"
3. Add redirect URIs for all environments:

```
# Development
http://localhost:3000/auth/microsoft/callback

# Production
https://yourdomain.com/auth/microsoft/callback
```

### Step 4: Create Client Secret

1. Go to "Certificates & secrets"
2. Click "New client secret"
3. Enter description and expiration
4. **Copy the value immediately** (shown only once)

### Step 5: Get Application IDs

1. Go to "Overview"
2. Copy:
   - **Application (client) ID**: Your client ID
   - **Directory (tenant) ID**: Your tenant ID (if needed)

## Goth Configuration

### Using azureadv2 Provider

```go
import (
    "github.com/markbates/goth"
    "github.com/markbates/goth/providers/azureadv2"
)

func init() {
    goth.UseProviders(
        azureadv2.New(
            os.Getenv("AZURE_CLIENT_ID"),
            os.Getenv("AZURE_CLIENT_SECRET"),
            os.Getenv("AZURE_CALLBACK_URL"),
            azureadv2.ProviderOptions{
                Tenant: azureadv2.CommonTenant,
                Scopes: []string{
                    "openid",
                    "profile",
                    "email",
                },
            },
        ),
    )
}
```

### Tenant Options

```go
// Any Microsoft account (recommended for most apps)
Tenant: azureadv2.CommonTenant

// Only work/school accounts (any organization)
Tenant: azureadv2.OrganizationsTenant

// Only personal Microsoft accounts
Tenant: azureadv2.ConsumersTenant

// Specific organization only
Tenant: "your-tenant-id-here"
// Example: "12345678-1234-1234-1234-123456789012"
```

### Environment Variables

```bash
# .env
AZURE_CLIENT_ID=12345678-1234-1234-1234-123456789012
AZURE_CLIENT_SECRET=xxx~xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AZURE_CALLBACK_URL=http://localhost:3000/auth/microsoft/callback
AZURE_TENANT_ID=common  # or specific tenant ID
```

## Available Scopes

### Basic Scopes

| Scope | Description |
|-------|-------------|
| `openid` | OpenID Connect sign-in |
| `profile` | Basic profile (name, etc.) |
| `email` | Email address |
| `offline_access` | Refresh tokens |

### Microsoft Graph Scopes

| Scope | Description |
|-------|-------------|
| `User.Read` | Read user's full profile |
| `User.ReadBasic.All` | Read basic profiles of all users |
| `Calendars.Read` | Read user's calendar |
| `Calendars.ReadWrite` | Read/write calendar |
| `Mail.Read` | Read user's mail |
| `Files.Read` | Read user's OneDrive files |
| `Sites.Read.All` | Read SharePoint sites |

### Requesting Graph Scopes

```go
azureadv2.ProviderOptions{
    Tenant: azureadv2.CommonTenant,
    Scopes: []string{
        "openid",
        "profile",
        "email",
        "User.Read",
        "Calendars.Read",
    },
}
```

## User Data Returned

```go
user, _ := gothic.CompleteUserAuth(w, r)

// Available fields
user.Email        // "user@domain.com"
user.Name         // "John Doe"
user.FirstName    // "John"
user.LastName     // "Doe"
user.NickName     // Username/UPN
user.UserID       // Azure AD Object ID
user.AccessToken  // For Microsoft Graph API
user.RefreshToken // For token refresh
user.ExpiresAt    // Token expiration
user.IDToken      // JWT with claims
```

## ID Token Claims

The ID token (JWT) contains useful claims:

```go
import "github.com/golang-jwt/jwt/v5"

// Parse ID token (already validated by Goth)
token, _ := jwt.Parse(user.IDToken, nil)
claims := token.Claims.(jwt.MapClaims)

// Common claims
claims["oid"]   // Object ID
claims["tid"]   // Tenant ID
claims["upn"]   // User Principal Name
claims["email"] // Email address
claims["name"]  // Display name
claims["roles"] // App roles (if configured)
claims["groups"] // Group memberships (if configured)
```

## Using Access Token with Microsoft Graph

```go
import "github.com/microsoftgraph/msgraph-sdk-go"

func getProfile(accessToken string) (*models.User, error) {
    cred := NewTokenCredential(accessToken)
    client, err := msgraph.NewGraphServiceClientWithCredentials(cred, nil)
    if err != nil {
        return nil, err
    }

    return client.Me().Get(context.Background(), nil)
}
```

Or with raw HTTP:

```go
func getProfile(accessToken string) (map[string]interface{}, error) {
    req, _ := http.NewRequest("GET", "https://graph.microsoft.com/v1.0/me", nil)
    req.Header.Set("Authorization", "Bearer "+accessToken)

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    var result map[string]interface{}
    json.NewDecoder(resp.Body).Decode(&result)
    return result, nil
}
```

## API Permissions Configuration

In Azure Portal:

1. Go to "API permissions"
2. Click "Add a permission"
3. Select "Microsoft Graph"
4. Choose "Delegated permissions"
5. Select required permissions
6. Click "Grant admin consent" (if you're an admin)

### Permission Types

| Type | Description |
|------|-------------|
| Delegated | Acts on behalf of signed-in user |
| Application | App acts as itself (no user context) |

For Goth (user sign-in), use **Delegated** permissions.

## Enterprise Configuration

### Conditional Access

If your tenant uses Conditional Access policies:
- Ensure app is included/excluded appropriately
- MFA requirements apply to OAuth sign-in
- Device compliance policies apply

### App Roles

Define custom roles in "App roles":

```json
{
  "allowedMemberTypes": ["User"],
  "displayName": "Admin",
  "value": "admin"
}
```

Roles appear in the `roles` claim of the ID token.

### Group Claims

Enable group claims in "Token configuration":
1. Click "Add groups claim"
2. Select group types to include
3. Groups appear in `groups` claim

## Common Issues

### "AADSTS50011: Reply URL does not match"

- Redirect URI doesn't match exactly
- Check protocol, domain, port, path
- No trailing slash differences

### "AADSTS7000218: Request body must contain client_secret"

- Client secret not provided or expired
- Create new secret in Azure Portal

### "AADSTS65001: User or admin has not consented"

- User hasn't granted permissions
- Admin consent required for some permissions
- Click "Grant admin consent" in portal

### "AADSTS700016: Application not found"

- Client ID is wrong
- App deleted or in different tenant
- Check correct tenant is configured

## Security Recommendations

1. Use specific tenant when possible (not CommonTenant)
2. Request minimum necessary scopes
3. Enable admin consent for sensitive permissions
4. Rotate client secrets before expiration
5. Monitor sign-in logs in Azure Portal
6. Use Conditional Access policies
7. Consider using Managed Identity for server-to-server

## Single Tenant vs Multi-Tenant

### Single Tenant
- Only your organization's users
- Simpler security model
- No consent required for users

### Multi-Tenant
- Users from any Azure AD organization
- Must handle tenant-specific data carefully
- Consider tenant validation in callback

```go
func handleCallback(c echo.Context) error {
    user, _ := gothic.CompleteUserAuth(c.Response(), c.Request())

    // Parse ID token for tenant validation
    token, _ := jwt.Parse(user.IDToken, nil)
    claims := token.Claims.(jwt.MapClaims)
    tenantID := claims["tid"].(string)

    // Validate tenant is allowed
    if !isAllowedTenant(tenantID) {
        return c.String(403, "Organization not allowed")
    }

    // Continue...
}
```
