# Complete OAuth Implementation

## OAuth Server Setup

```go
type OAuthHandler struct {
    clientID     string
    clientSecret string
    redirectURI  string
}

func (h *OAuthHandler) HandleInstall(w http.ResponseWriter, r *http.Request) {
    state := generateRandomState()
    storeState(state) // Store for verification

    authURL := fmt.Sprintf(
        "https://slack.com/oauth/v2/authorize?client_id=%s&scope=%s&redirect_uri=%s&state=%s",
        h.clientID,
        "chat:write,channels:read,commands",
        h.redirectURI,
        state,
    )

    http.Redirect(w, r, authURL, http.StatusTemporaryRedirect)
}
```

## OAuth Callback

```go
func (h *OAuthHandler) HandleCallback(w http.ResponseWriter, r *http.Request) {
    code := r.URL.Query().Get("code")
    state := r.URL.Query().Get("state")

    // Verify state
    if !verifyState(state) {
        http.Error(w, "Invalid state", http.StatusBadRequest)
        return
    }

    // Exchange code for token
    resp, err := slack.GetOAuthV2Response(
        http.DefaultClient,
        h.clientID,
        h.clientSecret,
        code,
        h.redirectURI,
    )
    if err != nil {
        http.Error(w, "OAuth failed", http.StatusInternalServerError)
        return
    }

    // Store token
    token := WorkspaceToken{
        TeamID:    resp.Team.ID,
        BotToken:  resp.AccessToken,
        BotUserID: resp.BotUserID,
    }
    storeToken(token)

    w.Write([]byte("Installation successful!"))
}
```

## State Management

```go
var stateStore = make(map[string]time.Time)
var stateMutex sync.RWMutex

func generateRandomState() string {
    b := make([]byte, 32)
    rand.Read(b)
    return base64.URLEncoding.EncodeToString(b)
}

func storeState(state string) {
    stateMutex.Lock()
    defer stateMutex.Unlock()
    stateStore[state] = time.Now().Add(10 * time.Minute)
}

func verifyState(state string) bool {
    stateMutex.Lock()
    defer stateMutex.Unlock()

    expiry, exists := stateStore[state]
    if !exists || time.Now().After(expiry) {
        return false
    }

    delete(stateStore, state)
    return true
}
```

## Production Pattern

```go
type OAuthConfig struct {
    ClientID     string
    ClientSecret string
    RedirectURI  string
    Scopes       []string
}

func NewOAuthServer(config OAuthConfig) *http.ServeMux {
    mux := http.NewServeMux()
    handler := &OAuthHandler{
        clientID:     config.ClientID,
        clientSecret: config.ClientSecret,
        redirectURI:  config.RedirectURI,
    }

    mux.HandleFunc("/slack/install", handler.HandleInstall)
    mux.HandleFunc("/slack/oauth/callback", handler.HandleCallback)

    return mux
}
```
