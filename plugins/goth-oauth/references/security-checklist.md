# OAuth Security Checklist

Security verification checklist for Goth OAuth implementations.

## Pre-Deployment Checklist

### Session Configuration

- [ ] **SESSION_SECRET is cryptographically random**
  - At least 32 bytes of random data
  - Never hardcoded in source code
  - Never committed to version control
  ```bash
  # Generate secure secret
  openssl rand -base64 32
  ```

- [ ] **Cookie settings are secure**
  ```go
  store.Options.Secure = true     // HTTPS only
  store.Options.HttpOnly = true   // No JS access
  store.Options.SameSite = http.SameSiteLaxMode  // CSRF protection
  store.Options.Path = "/"        // Explicit path
  ```

- [ ] **Session expiration is appropriate**
  - MaxAge set based on security requirements
  - Consider shorter for sensitive apps (1-7 days)
  - Never infinite expiration

### HTTPS Configuration

- [ ] **HTTPS enforced in production**
  - All auth endpoints require HTTPS
  - HTTP redirects to HTTPS
  - HSTS header enabled

- [ ] **Callback URLs use HTTPS**
  - Provider callback URLs are HTTPS
  - No mixed content warnings

### Credential Management

- [ ] **OAuth credentials are in environment variables**
  ```bash
  # Correct
  CLIENT_ID=${GOOGLE_CLIENT_ID}

  # Never this
  CLIENT_ID="hardcoded-value"
  ```

- [ ] **Credentials not in version control**
  - `.env` files in `.gitignore`
  - No secrets in commit history
  - Use secret scanning in CI/CD

- [ ] **Client secrets are rotated regularly**
  - Set calendar reminder for rotation
  - Automate rotation if possible

### Token Handling

- [ ] **Access tokens stored server-side only**
  ```go
  // Store in server-side session
  session.Values["access_token"] = user.AccessToken

  // Never expose to client
  // Don't: return c.JSON(200, map[string]string{"token": token})
  ```

- [ ] **Refresh tokens are protected**
  - Stored encrypted if in database
  - Never sent to client
  - Rotation on use if supported

- [ ] **Token expiration is handled**
  - Check expiration before API calls
  - Refresh tokens before expiry
  - Force re-auth on refresh failure

### CSRF Protection

- [ ] **State parameter is validated**
  - Goth handles this automatically
  - Verify `gothic.CompleteUserAuth` errors include state issues

- [ ] **SameSite cookie attribute set**
  ```go
  store.Options.SameSite = http.SameSiteLaxMode
  // Or for stricter protection:
  store.Options.SameSite = http.SameSiteStrictMode
  ```

### Session Security

- [ ] **Session ID regenerated after login**
  ```go
  // After successful auth
  oldSession.Options.MaxAge = -1
  oldSession.Save(r, w)
  newSession, _ := store.New(r, "session")
  // Copy necessary values
  ```

- [ ] **Session fixation prevented**
  - Never accept session ID from URL
  - Only use cookie-based sessions

- [ ] **Concurrent session handling**
  - Consider single-session enforcement
  - Log concurrent logins for audit

### Rate Limiting

- [ ] **Auth endpoints are rate limited**
  ```go
  authGroup.Use(middleware.RateLimiter(
      middleware.NewRateLimiterMemoryStore(rate.Limit(10)),
  ))
  ```

- [ ] **Callback endpoints are protected**
  - Rate limit callback handler
  - Prevent callback replay attacks

### Error Handling

- [ ] **Errors don't leak sensitive info**
  ```go
  // Don't: return c.String(500, err.Error())
  // Do:
  log.Printf("Auth error: %v", err)
  return c.Redirect(302, "/login?error=auth_failed")
  ```

- [ ] **Failed logins are logged**
  - Log provider, timestamp, IP
  - Don't log credentials

- [ ] **Successful logins are logged**
  - Audit trail for compliance
  - Detect suspicious patterns

### Provider Configuration

- [ ] **Minimum necessary scopes requested**
  - Review each scope needed
  - Remove unused scopes
  - Document why each scope is needed

- [ ] **Callback URLs are explicit**
  - No wildcards
  - Exact match required
  - All environments registered

- [ ] **Provider apps are properly configured**
  - Consent screen complete
  - Privacy policy linked
  - Support contact provided

## Runtime Monitoring

### Logging

- [ ] **Authentication events logged**
  - Login attempts (success/failure)
  - Logout events
  - Token refresh events

- [ ] **Suspicious activity detected**
  - Multiple failed logins
  - Geographic anomalies
  - Unusual login patterns

### Alerts

- [ ] **Failed login spike alerts**
- [ ] **Token refresh failure alerts**
- [ ] **Session anomaly alerts**

## Periodic Review

### Monthly

- [ ] Review access logs for anomalies
- [ ] Check for leaked credentials
- [ ] Verify all test accounts removed from production

### Quarterly

- [ ] Rotate client secrets
- [ ] Review granted scopes
- [ ] Update OAuth libraries
- [ ] Review session settings

### Annually

- [ ] Full security audit
- [ ] Penetration testing
- [ ] Compliance review
- [ ] Update privacy policy

## Quick Security Test

Run these checks before each deployment:

```bash
# 1. Verify HTTPS redirect
curl -I http://yourdomain.com/auth/google
# Should redirect to https://

# 2. Check cookie settings
# Login and inspect cookies in browser
# Verify Secure, HttpOnly, SameSite flags

# 3. Test state parameter
# Try callback without state - should fail

# 4. Check error handling
# Use invalid credentials - should not leak details
```

## Security Headers

Add these headers to auth responses:

```go
e.Use(func(next echo.HandlerFunc) echo.HandlerFunc {
    return func(c echo.Context) error {
        c.Response().Header().Set("X-Content-Type-Options", "nosniff")
        c.Response().Header().Set("X-Frame-Options", "DENY")
        c.Response().Header().Set("X-XSS-Protection", "1; mode=block")
        c.Response().Header().Set("Referrer-Policy", "strict-origin-when-cross-origin")
        return next(c)
    }
})
```

## Incident Response

If credentials are compromised:

1. **Immediately** rotate affected client secrets
2. Revoke all active sessions
3. Review access logs for unauthorized access
4. Notify affected users if data accessed
5. Update secrets in all environments
6. Investigate root cause
7. Document incident and response

## Resources

- [OWASP OAuth Security](https://owasp.org/www-pdf-archive/OAuth_Security_Cheatsheet.pdf)
- [RFC 6819: OAuth Threat Model](https://tools.ietf.org/html/rfc6819)
- [Google OAuth Security](https://developers.google.com/identity/protocols/oauth2/security)
- [Microsoft Identity Security](https://docs.microsoft.com/en-us/azure/active-directory/develop/security-best-practices)
