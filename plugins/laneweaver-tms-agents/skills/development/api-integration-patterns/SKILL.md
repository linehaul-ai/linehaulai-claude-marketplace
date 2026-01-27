---
name: api-integration-patterns
description: Unified patterns for external API integrations including OAuth2 token lifecycle, exponential backoff, webhooks vs polling, rate limiting, error handling, multi-tenant isolation, and webhook security. Use when integrating with QuickBooks, MyCarrierPackets, Slack, or any external OAuth2-based API in laneweaverTMS.
keywords: [oauth2, webhooks, rate-limiting, token-management, api-integration]
---

# API Integration Patterns

Unified patterns for building robust, secure external API integrations in laneweaverTMS. These patterns apply across all integrations (QuickBooks, MyCarrierPackets, Slack, and future APIs).

## When to Use This Skill

- Implementing OAuth2 authentication with any external service
- Building token refresh and storage mechanisms
- Choosing between webhooks and polling for data sync
- Implementing rate limiting and backoff strategies
- Handling API errors consistently across integrations
- Designing multi-tenant token isolation
- Securing webhook endpoints
- Writing integration tests for external APIs

## OAuth2 Token Lifecycle

### Token Types and Responsibilities

| Token Type | Purpose | Typical Lifetime | Storage Location |
|------------|---------|------------------|------------------|
| Access Token | API authorization | 1-3 hours | Memory or encrypted DB |
| Refresh Token | Obtain new access token | 30-100 days | Encrypted database only |
| ID Token | User identity (OIDC) | 1-24 hours | Session or memory |

### Token Storage Pattern

Store tokens in encrypted database columns, never in JWTs or local storage.

```go
type OAuthTokenStore struct {
    AccountID    string    `db:"account_id"`    // Multi-tenant isolation
    Provider     string    `db:"provider"`      // "quickbooks", "slack", etc.
    AccessToken  string    `db:"access_token"`  // Encrypted at rest
    RefreshToken string    `db:"refresh_token"` // Encrypted at rest
    ExpiresAt    time.Time `db:"expires_at"`
    Scopes       []string  `db:"scopes"`        // Granted permissions
    CreatedAt    time.Time `db:"created_at"`
    UpdatedAt    time.Time `db:"updated_at"`
}
```

### Proactive Token Refresh

Refresh tokens before expiry to avoid request failures. Refresh when 80% of lifetime has elapsed.

```go
func (c *OAuthClient) getValidToken(ctx context.Context, accountID string) (string, error) {
    c.tokenMu.RLock()
    token, exists := c.tokens[accountID]
    c.tokenMu.RUnlock()

    if !exists {
        return "", fmt.Errorf("no token for account %s", accountID)
    }

    // Proactive refresh: refresh at 80% of lifetime
    // For 1-hour token, refresh after 48 minutes
    refreshThreshold := token.ExpiresAt.Add(-time.Duration(float64(time.Hour) * 0.2))

    if time.Now().After(refreshThreshold) {
        return c.refreshToken(ctx, accountID, token.RefreshToken)
    }

    return token.AccessToken, nil
}

func (c *OAuthClient) refreshToken(ctx context.Context, accountID, refreshToken string) (string, error) {
    c.tokenMu.Lock()
    defer c.tokenMu.Unlock()

    // Double-check after acquiring lock (another goroutine may have refreshed)
    if token, ok := c.tokens[accountID]; ok {
        if time.Now().Before(token.ExpiresAt.Add(-5 * time.Minute)) {
            return token.AccessToken, nil
        }
    }

    // Perform refresh with provider
    newToken, err := c.provider.RefreshToken(ctx, refreshToken)
    if err != nil {
        return "", fmt.Errorf("token refresh failed: %w", err)
    }

    // Store new tokens
    c.tokens[accountID] = &OAuthTokenStore{
        AccountID:    accountID,
        AccessToken:  newToken.AccessToken,
        RefreshToken: newToken.RefreshToken, // May be new or same
        ExpiresAt:    newToken.ExpiresAt,
    }

    // Persist to database
    if err := c.repo.SaveToken(ctx, c.tokens[accountID]); err != nil {
        return "", fmt.Errorf("failed to persist token: %w", err)
    }

    return newToken.AccessToken, nil
}
```

### Token Refresh Flow Diagram

```
Request API → Check Token Expiry → [Not Expired] → Use Token → API Call
                    ↓
              [Near Expiry]
                    ↓
            Acquire Lock → Refresh Token → Store New Token → Use Token → API Call
                    ↓ (on failure)
            Clear Token → Return Error → Prompt Re-authentication
```

## Exponential Backoff

### Standard Backoff Implementation

Use exponential backoff with jitter for all retryable operations.

```go
import (
    "math"
    "math/rand"
    "time"
)

type BackoffConfig struct {
    BaseDelay   time.Duration // Starting delay (e.g., 1 second)
    MaxDelay    time.Duration // Maximum delay cap (e.g., 60 seconds)
    MaxRetries  int           // Maximum attempts (e.g., 5)
    JitterRatio float64       // Random jitter 0-1 (e.g., 0.2 for 20%)
}

func DefaultBackoffConfig() BackoffConfig {
    return BackoffConfig{
        BaseDelay:   1 * time.Second,
        MaxDelay:    60 * time.Second,
        MaxRetries:  5,
        JitterRatio: 0.2,
    }
}

func (c BackoffConfig) Delay(attempt int) time.Duration {
    if attempt >= c.MaxRetries {
        return 0 // Signal to stop retrying
    }

    // Calculate exponential delay: base * 2^attempt
    delay := float64(c.BaseDelay) * math.Pow(2, float64(attempt))

    // Cap at maximum
    if delay > float64(c.MaxDelay) {
        delay = float64(c.MaxDelay)
    }

    // Add jitter: delay * (1 +/- jitterRatio)
    jitter := delay * c.JitterRatio * (2*rand.Float64() - 1)
    delay += jitter

    return time.Duration(delay)
}
```

### Retry Wrapper Pattern

```go
func RetryWithBackoff[T any](
    ctx context.Context,
    config BackoffConfig,
    operation func(context.Context) (T, error),
    isRetryable func(error) bool,
) (T, error) {
    var zero T
    var lastErr error

    for attempt := 0; attempt < config.MaxRetries; attempt++ {
        result, err := operation(ctx)
        if err == nil {
            return result, nil
        }

        lastErr = err

        // Check if error is retryable
        if !isRetryable(err) {
            return zero, fmt.Errorf("non-retryable error: %w", err)
        }

        // Calculate delay
        delay := config.Delay(attempt)
        if delay == 0 {
            break // Max retries exceeded
        }

        // Wait with context cancellation support
        select {
        case <-ctx.Done():
            return zero, ctx.Err()
        case <-time.After(delay):
            // Continue to next attempt
        }
    }

    return zero, fmt.Errorf("max retries exceeded: %w", lastErr)
}

// Usage example
result, err := RetryWithBackoff(ctx, DefaultBackoffConfig(),
    func(ctx context.Context) (*Response, error) {
        return client.MakeAPICall(ctx, request)
    },
    func(err error) bool {
        // Retry on 429, 500, 502, 503, 504
        var apiErr *APIError
        if errors.As(err, &apiErr) {
            return apiErr.StatusCode == 429 || apiErr.StatusCode >= 500
        }
        return false
    },
)
```

### Circuit Breaker Integration

Combine backoff with circuit breaker for cascading failure prevention.

```go
type CircuitBreaker struct {
    failures    int32
    threshold   int32         // Failures before opening
    resetAfter  time.Duration // Time before attempting reset
    openedAt    time.Time
    mu          sync.RWMutex
    state       CircuitState
}

type CircuitState int

const (
    CircuitClosed CircuitState = iota // Normal operation
    CircuitOpen                        // Failing, reject requests
    CircuitHalfOpen                    // Testing if service recovered
)

func (cb *CircuitBreaker) Execute(operation func() error) error {
    cb.mu.RLock()
    state := cb.state
    cb.mu.RUnlock()

    switch state {
    case CircuitOpen:
        if time.Since(cb.openedAt) > cb.resetAfter {
            cb.mu.Lock()
            cb.state = CircuitHalfOpen
            cb.mu.Unlock()
        } else {
            return fmt.Errorf("circuit breaker open")
        }
    }

    err := operation()

    cb.mu.Lock()
    defer cb.mu.Unlock()

    if err != nil {
        cb.failures++
        if cb.failures >= cb.threshold {
            cb.state = CircuitOpen
            cb.openedAt = time.Now()
        }
        return err
    }

    // Success - reset state
    cb.failures = 0
    cb.state = CircuitClosed
    return nil
}
```

## Webhook vs Polling Decision Matrix

Choose the right data synchronization strategy based on these factors.

| Factor | Use Webhooks | Use Polling |
|--------|-------------|-------------|
| **Real-time requirement** | Immediate updates needed | Minutes-to-hours delay acceptable |
| **Webhook reliability** | Provider has high uptime | Provider webhooks unreliable |
| **Data volume** | Low-medium event frequency | High volume (batch more efficient) |
| **API support** | Provider offers webhooks | No webhook support |
| **Network reliability** | Your endpoint highly available | Intermittent connectivity |
| **Ordering guarantees** | Order not critical | Strict ordering required |
| **Initial sync** | Need polling for backfill | Polling for all data |
| **Cost** | Lower API calls | More API calls but predictable |

### Hybrid Approach (Recommended)

Use webhooks for real-time updates with polling as backup for reliability.

```go
type SyncManager struct {
    webhookHandler  *WebhookHandler
    pollingInterval time.Duration
    lastSyncTime    time.Time
}

// Primary: Webhook receives real-time updates
func (m *SyncManager) HandleWebhook(event WebhookEvent) error {
    if err := m.processEvent(event); err != nil {
        // Log for reconciliation during next poll
        m.logFailedEvent(event)
        return err
    }
    m.lastSyncTime = time.Now()
    return nil
}

// Backup: Polling catches missed webhooks and handles initial sync
func (m *SyncManager) Poll(ctx context.Context) error {
    changes, err := m.api.GetChangesSince(m.lastSyncTime)
    if err != nil {
        return err
    }

    for _, change := range changes {
        if err := m.processChange(change); err != nil {
            return err
        }
    }

    m.lastSyncTime = time.Now()
    return nil
}

// Run polling on interval as safety net
func (m *SyncManager) StartBackgroundPolling(ctx context.Context) {
    ticker := time.NewTicker(m.pollingInterval)
    defer ticker.Stop()

    for {
        select {
        case <-ctx.Done():
            return
        case <-ticker.C:
            if err := m.Poll(ctx); err != nil {
                log.Printf("polling error: %v", err)
            }
        }
    }
}
```

## Rate Limiting Patterns

### Reading Rate Limit Headers

Most APIs return rate limit information in response headers.

```go
type RateLimitInfo struct {
    Limit     int       // Max requests allowed
    Remaining int       // Requests remaining in window
    Reset     time.Time // When limit resets
}

func ParseRateLimitHeaders(resp *http.Response) *RateLimitInfo {
    info := &RateLimitInfo{}

    // Common header patterns
    if limit := resp.Header.Get("X-RateLimit-Limit"); limit != "" {
        info.Limit, _ = strconv.Atoi(limit)
    }
    if remaining := resp.Header.Get("X-RateLimit-Remaining"); remaining != "" {
        info.Remaining, _ = strconv.Atoi(remaining)
    }
    if reset := resp.Header.Get("X-RateLimit-Reset"); reset != "" {
        // Unix timestamp
        if ts, err := strconv.ParseInt(reset, 10, 64); err == nil {
            info.Reset = time.Unix(ts, 0)
        }
    }

    // Slack uses different header
    if retryAfter := resp.Header.Get("Retry-After"); retryAfter != "" {
        if seconds, err := strconv.Atoi(retryAfter); err == nil {
            info.Reset = time.Now().Add(time.Duration(seconds) * time.Second)
        }
    }

    return info
}
```

### Token Bucket Rate Limiter

Client-side rate limiting to avoid hitting server limits.

```go
type TokenBucket struct {
    tokens     float64
    maxTokens  float64
    refillRate float64       // Tokens per second
    lastRefill time.Time
    mu         sync.Mutex
}

func NewTokenBucket(maxTokens, refillRate float64) *TokenBucket {
    return &TokenBucket{
        tokens:     maxTokens,
        maxTokens:  maxTokens,
        refillRate: refillRate,
        lastRefill: time.Now(),
    }
}

func (tb *TokenBucket) Take(ctx context.Context) error {
    tb.mu.Lock()
    defer tb.mu.Unlock()

    // Refill tokens based on elapsed time
    now := time.Now()
    elapsed := now.Sub(tb.lastRefill).Seconds()
    tb.tokens = math.Min(tb.maxTokens, tb.tokens+elapsed*tb.refillRate)
    tb.lastRefill = now

    if tb.tokens >= 1 {
        tb.tokens--
        return nil
    }

    // Calculate wait time for next token
    waitTime := time.Duration((1 - tb.tokens) / tb.refillRate * float64(time.Second))

    select {
    case <-ctx.Done():
        return ctx.Err()
    case <-time.After(waitTime):
        tb.tokens = 0 // Consumed the partial token + waited
        return nil
    }
}
```

### Request Queue with Priority

Queue requests with priority handling for rate-limited APIs.

```go
type PriorityRequest struct {
    Priority int // Lower = higher priority
    Request  func(context.Context) error
    Done     chan error
}

type RequestQueue struct {
    queue       *heap.Heap[*PriorityRequest]
    rateLimiter *TokenBucket
}

func (q *RequestQueue) Submit(ctx context.Context, priority int, req func(context.Context) error) error {
    done := make(chan error, 1)
    q.queue.Push(&PriorityRequest{
        Priority: priority,
        Request:  req,
        Done:     done,
    })

    select {
    case <-ctx.Done():
        return ctx.Err()
    case err := <-done:
        return err
    }
}

func (q *RequestQueue) Process(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            return
        default:
            item := q.queue.Pop()
            if item == nil {
                time.Sleep(10 * time.Millisecond)
                continue
            }

            // Wait for rate limit token
            if err := q.rateLimiter.Take(ctx); err != nil {
                item.Done <- err
                continue
            }

            // Execute request
            item.Done <- item.Request(ctx)
        }
    }
}
```

## Error Handling Taxonomy

### HTTP Status Code Response Matrix

| Status | Category | Meaning | Action |
|--------|----------|---------|--------|
| 400 | Client Error | Bad request syntax | Fix request, do not retry |
| 401 | Auth Error | Token expired/invalid | Refresh token, retry once |
| 403 | Auth Error | Forbidden | Check permissions, log, do not retry |
| 404 | Client Error | Resource not found | Handle gracefully, do not retry |
| 409 | Client Error | Conflict (stale data) | Re-fetch, merge, retry |
| 422 | Client Error | Validation failed | Fix data, do not retry |
| 429 | Rate Limit | Too many requests | Backoff, retry with delay |
| 500 | Server Error | Internal error | Retry with backoff |
| 502 | Server Error | Bad gateway | Retry with backoff |
| 503 | Server Error | Service unavailable | Retry with backoff |
| 504 | Server Error | Gateway timeout | Retry with backoff |

### Unified Error Type

```go
type APIError struct {
    StatusCode int               `json:"statusCode"`
    Code       string            `json:"code"`       // Provider-specific code
    Message    string            `json:"message"`
    Details    map[string]any    `json:"details,omitempty"`
    Provider   string            `json:"provider"`   // "quickbooks", "slack", etc.
    RequestID  string            `json:"requestId,omitempty"`
    Retryable  bool              `json:"retryable"`
    RetryAfter *time.Duration    `json:"retryAfter,omitempty"`
}

func (e *APIError) Error() string {
    return fmt.Sprintf("[%s] %d %s: %s", e.Provider, e.StatusCode, e.Code, e.Message)
}

func ClassifyError(statusCode int, provider string, body []byte) *APIError {
    err := &APIError{
        StatusCode: statusCode,
        Provider:   provider,
    }

    // Parse provider-specific error format
    switch provider {
    case "quickbooks":
        err.parseQuickBooksError(body)
    case "slack":
        err.parseSlackError(body)
    case "mycarrierpackets":
        err.parseMCPError(body)
    }

    // Determine retryability
    switch statusCode {
    case 429:
        err.Retryable = true
        // Parse Retry-After if present
    case 500, 502, 503, 504:
        err.Retryable = true
    case 401:
        err.Retryable = true // After token refresh
    default:
        err.Retryable = false
    }

    return err
}
```

### Error Handler Pattern

```go
func (c *APIClient) handleResponse(resp *http.Response, body []byte) error {
    if resp.StatusCode >= 200 && resp.StatusCode < 300 {
        return nil
    }

    apiErr := ClassifyError(resp.StatusCode, c.provider, body)
    apiErr.RequestID = resp.Header.Get("X-Request-ID")

    switch resp.StatusCode {
    case 401:
        // Clear cached token, trigger refresh
        c.clearToken()
        return fmt.Errorf("authentication required: %w", apiErr)

    case 429:
        // Parse retry timing
        if retryAfter := resp.Header.Get("Retry-After"); retryAfter != "" {
            if seconds, err := strconv.Atoi(retryAfter); err == nil {
                d := time.Duration(seconds) * time.Second
                apiErr.RetryAfter = &d
            }
        }
        return apiErr

    default:
        return apiErr
    }
}
```

## Multi-Tenant Token Isolation

### Database Schema

Each tenant (account/workspace) has isolated credentials.

```sql
CREATE TABLE oauth_tokens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES accounts(id),
    provider VARCHAR(50) NOT NULL,  -- 'quickbooks', 'slack', 'mycarrierpackets'

    -- Encrypted token storage
    access_token_encrypted BYTEA NOT NULL,
    refresh_token_encrypted BYTEA NOT NULL,

    -- Token metadata
    expires_at TIMESTAMPTZ NOT NULL,
    scopes TEXT[],

    -- Provider-specific identifiers
    external_id VARCHAR(255),       -- realm_id, team_id, etc.
    external_user_id VARCHAR(255),  -- user who authorized

    -- Audit
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Ensure one token per account per provider
    UNIQUE(account_id, provider)
);

-- Index for token lookup
CREATE INDEX idx_oauth_tokens_account_provider ON oauth_tokens(account_id, provider);
```

### Token Isolation in Code

```go
type MultiTenantTokenManager struct {
    repo      TokenRepository
    encryptor Encryptor
    cache     sync.Map // account_id:provider -> *OAuthTokenStore
}

func (m *MultiTenantTokenManager) GetToken(ctx context.Context, accountID, provider string) (*OAuthTokenStore, error) {
    cacheKey := fmt.Sprintf("%s:%s", accountID, provider)

    // Check cache
    if cached, ok := m.cache.Load(cacheKey); ok {
        token := cached.(*OAuthTokenStore)
        if time.Now().Before(token.ExpiresAt) {
            return token, nil
        }
    }

    // Load from database
    encrypted, err := m.repo.GetToken(ctx, accountID, provider)
    if err != nil {
        return nil, err
    }

    // Decrypt
    token := &OAuthTokenStore{
        AccountID:    accountID,
        Provider:     provider,
        AccessToken:  m.encryptor.Decrypt(encrypted.AccessTokenEncrypted),
        RefreshToken: m.encryptor.Decrypt(encrypted.RefreshTokenEncrypted),
        ExpiresAt:    encrypted.ExpiresAt,
        Scopes:       encrypted.Scopes,
    }

    // Cache
    m.cache.Store(cacheKey, token)

    return token, nil
}

// CRITICAL: Always scope API clients to specific account
func (m *MultiTenantTokenManager) GetClientForAccount(ctx context.Context, accountID, provider string) (*APIClient, error) {
    token, err := m.GetToken(ctx, accountID, provider)
    if err != nil {
        return nil, err
    }

    // Client is scoped to this account's token
    return NewAPIClient(provider, token.AccessToken, token.ExternalID), nil
}
```

## Webhook Security

### Signature Verification

Always verify webhook signatures to prevent spoofing.

```go
import (
    "crypto/hmac"
    "crypto/sha256"
    "encoding/hex"
)

type WebhookVerifier struct {
    secrets map[string]string // provider -> secret
}

func (v *WebhookVerifier) Verify(provider string, payload []byte, signature string, timestamp string) error {
    secret, ok := v.secrets[provider]
    if !ok {
        return fmt.Errorf("unknown provider: %s", provider)
    }

    switch provider {
    case "slack":
        return v.verifySlack(payload, signature, timestamp, secret)
    case "quickbooks":
        return v.verifyQuickBooks(payload, signature, secret)
    default:
        return v.verifyHMACSHA256(payload, signature, secret)
    }
}

// Slack uses version:timestamp:body format
func (v *WebhookVerifier) verifySlack(payload []byte, signature, timestamp, secret string) error {
    // Check timestamp freshness (prevent replay attacks)
    ts, err := strconv.ParseInt(timestamp, 10, 64)
    if err != nil {
        return fmt.Errorf("invalid timestamp")
    }
    if time.Since(time.Unix(ts, 0)) > 5*time.Minute {
        return fmt.Errorf("timestamp too old")
    }

    // Compute expected signature
    baseString := fmt.Sprintf("v0:%s:%s", timestamp, string(payload))
    mac := hmac.New(sha256.New, []byte(secret))
    mac.Write([]byte(baseString))
    expected := "v0=" + hex.EncodeToString(mac.Sum(nil))

    if !hmac.Equal([]byte(expected), []byte(signature)) {
        return fmt.Errorf("signature mismatch")
    }

    return nil
}

// Generic HMAC-SHA256 verification
func (v *WebhookVerifier) verifyHMACSHA256(payload []byte, signature, secret string) error {
    mac := hmac.New(sha256.New, []byte(secret))
    mac.Write(payload)
    expected := hex.EncodeToString(mac.Sum(nil))

    if !hmac.Equal([]byte(expected), []byte(signature)) {
        return fmt.Errorf("signature mismatch")
    }

    return nil
}
```

### Replay Protection

Prevent replay attacks with timestamp validation and idempotency.

```go
type WebhookHandler struct {
    verifier      *WebhookVerifier
    idempotencyDB IdempotencyStore
    maxAge        time.Duration // e.g., 5 minutes
}

func (h *WebhookHandler) Handle(w http.ResponseWriter, r *http.Request) {
    provider := mux.Vars(r)["provider"]

    // Read body
    body, err := io.ReadAll(r.Body)
    if err != nil {
        http.Error(w, "Failed to read body", http.StatusBadRequest)
        return
    }

    // Get signature and timestamp from headers
    signature := r.Header.Get("X-Signature")
    timestamp := r.Header.Get("X-Timestamp")

    // 1. Verify signature
    if err := h.verifier.Verify(provider, body, signature, timestamp); err != nil {
        http.Error(w, "Invalid signature", http.StatusUnauthorized)
        return
    }

    // 2. Check timestamp freshness
    ts, _ := strconv.ParseInt(timestamp, 10, 64)
    if time.Since(time.Unix(ts, 0)) > h.maxAge {
        http.Error(w, "Request expired", http.StatusBadRequest)
        return
    }

    // 3. Check idempotency key
    eventID := r.Header.Get("X-Event-ID")
    if eventID == "" {
        eventID = fmt.Sprintf("%s-%s", signature[:16], timestamp)
    }

    if h.idempotencyDB.Exists(eventID) {
        // Already processed, return success (idempotent)
        w.WriteHeader(http.StatusOK)
        return
    }

    // 4. Process webhook
    if err := h.processWebhook(r.Context(), provider, body); err != nil {
        http.Error(w, "Processing failed", http.StatusInternalServerError)
        return
    }

    // 5. Mark as processed
    h.idempotencyDB.Set(eventID, 24*time.Hour) // Keep for 24h

    w.WriteHeader(http.StatusOK)
}
```

## Integration Testing Patterns

### Mock Server for Unit Tests

```go
import (
    "net/http"
    "net/http/httptest"
)

type MockAPIServer struct {
    *httptest.Server
    Responses map[string]MockResponse
}

type MockResponse struct {
    StatusCode int
    Body       string
    Headers    map[string]string
}

func NewMockAPIServer() *MockAPIServer {
    m := &MockAPIServer{
        Responses: make(map[string]MockResponse),
    }

    m.Server = httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        key := fmt.Sprintf("%s %s", r.Method, r.URL.Path)

        resp, ok := m.Responses[key]
        if !ok {
            w.WriteHeader(http.StatusNotFound)
            return
        }

        for k, v := range resp.Headers {
            w.Header().Set(k, v)
        }
        w.WriteHeader(resp.StatusCode)
        w.Write([]byte(resp.Body))
    }))

    return m
}

// Usage in tests
func TestGetCarrierData(t *testing.T) {
    server := NewMockAPIServer()
    defer server.Close()

    server.Responses["POST /api/v1/Carrier/GetCarrierData"] = MockResponse{
        StatusCode: 200,
        Body:       `{"DOTNumber": 12345, "LegalName": "Test Carrier"}`,
    }

    client := NewMCPClient(server.URL, "user", "pass")
    carrier, err := client.GetCarrierData(context.Background(), 12345, "MC123")

    assert.NoError(t, err)
    assert.Equal(t, "Test Carrier", carrier.LegalName)
}
```

### HTTP Interaction Recording

Record and replay HTTP interactions for integration tests.

```go
import (
    "gopkg.in/dnaeon/go-vcr.v3/recorder"
)

func TestWithRecording(t *testing.T) {
    // Record mode: captures real API responses
    // Replay mode: uses recorded responses
    r, err := recorder.New("fixtures/carrier_data")
    if err != nil {
        t.Fatal(err)
    }
    defer r.Stop()

    client := &http.Client{
        Transport: r,
    }

    // Use recorded responses in tests
    apiClient := NewAPIClient(WithHTTPClient(client))
    result, err := apiClient.GetData(context.Background())

    assert.NoError(t, err)
    assert.NotNil(t, result)
}
```

### Sandbox Environment Testing

```go
type IntegrationTestSuite struct {
    suite.Suite
    client *APIClient
}

func (s *IntegrationTestSuite) SetupSuite() {
    // Use sandbox/test environment
    baseURL := os.Getenv("API_SANDBOX_URL")
    if baseURL == "" {
        s.T().Skip("Sandbox URL not configured")
    }

    s.client = NewAPIClient(
        WithBaseURL(baseURL),
        WithCredentials(
            os.Getenv("SANDBOX_CLIENT_ID"),
            os.Getenv("SANDBOX_CLIENT_SECRET"),
        ),
    )
}

func (s *IntegrationTestSuite) TestTokenRefresh() {
    // Test with real sandbox
    token, err := s.client.RefreshToken(context.Background())
    s.Require().NoError(err)
    s.NotEmpty(token.AccessToken)
}

func TestIntegration(t *testing.T) {
    if testing.Short() {
        t.Skip("Skipping integration tests in short mode")
    }
    suite.Run(t, new(IntegrationTestSuite))
}
```

## Provider-Specific Considerations

For detailed provider-specific implementation:

| Provider | Reference Skill |
|----------|-----------------|
| QuickBooks | `quickbooks-api-integration:quickbooks-online-api` |
| MyCarrierPackets | `mycarrierpackets-api:mycarrierpackets-api` |
| Slack | `slack-go-sdk:slack-auth-security` |
| Goth OAuth | `goth-oauth:goth-fundamentals` |

## Quick Reference Checklist

### New Integration Checklist

```
[ ] OAuth2 implementation
    [ ] Authorization URL generation
    [ ] Token exchange endpoint
    [ ] Token refresh logic
    [ ] Proactive refresh (80% lifetime)
    [ ] Secure token storage (encrypted DB)

[ ] Error handling
    [ ] Unified error type
    [ ] Status code classification
    [ ] Retry logic for transient errors
    [ ] Clear token on 401

[ ] Rate limiting
    [ ] Parse rate limit headers
    [ ] Client-side rate limiter
    [ ] Backoff on 429

[ ] Reliability
    [ ] Exponential backoff with jitter
    [ ] Circuit breaker
    [ ] Timeout configuration

[ ] Multi-tenancy
    [ ] Per-account token isolation
    [ ] Scoped API clients

[ ] Webhook security (if applicable)
    [ ] Signature verification
    [ ] Timestamp validation
    [ ] Idempotency handling

[ ] Testing
    [ ] Mock server for unit tests
    [ ] Sandbox environment tests
    [ ] Recorded HTTP interactions
```
