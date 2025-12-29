# Quick Start Guide

Complete working example of Goth OAuth with Google provider.

## 1. Get Google OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the "People API"
4. Configure OAuth consent screen
5. Create OAuth 2.0 credentials (Web application)
6. Add `http://localhost:3000/auth/google/callback` as redirect URI
7. Copy Client ID and Client Secret

## 2. Set Environment Variables

```bash
export GOOGLE_CLIENT_ID="your-client-id.apps.googleusercontent.com"
export GOOGLE_CLIENT_SECRET="your-client-secret"
export SESSION_SECRET=$(openssl rand -base64 32)
```

## 3. Create the Application

```go
// main.go
package main

import (
    "fmt"
    "html/template"
    "log"
    "net/http"
    "os"

    "github.com/gorilla/sessions"
    "github.com/markbates/goth"
    "github.com/markbates/goth/gothic"
    "github.com/markbates/goth/providers/google"
)

var sessionStore *sessions.CookieStore

func init() {
    // Initialize session store
    key := os.Getenv("SESSION_SECRET")
    if key == "" {
        log.Fatal("SESSION_SECRET environment variable required")
    }
    sessionStore = sessions.NewCookieStore([]byte(key))
    sessionStore.Options.HttpOnly = true
    gothic.Store = sessionStore

    // Initialize providers
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
    http.HandleFunc("/", handleHome)
    http.HandleFunc("/auth/google", handleAuth)
    http.HandleFunc("/auth/google/callback", handleCallback)
    http.HandleFunc("/dashboard", handleDashboard)
    http.HandleFunc("/logout", handleLogout)

    log.Println("Server starting on http://localhost:3000")
    log.Fatal(http.ListenAndServe(":3000", nil))
}

func handleHome(w http.ResponseWriter, r *http.Request) {
    tmpl := `<!DOCTYPE html>
<html>
<head><title>Goth OAuth Demo</title></head>
<body>
    <h1>Welcome</h1>
    <p><a href="/auth/google">Sign in with Google</a></p>
</body>
</html>`
    w.Header().Set("Content-Type", "text/html")
    fmt.Fprint(w, tmpl)
}

func handleAuth(w http.ResponseWriter, r *http.Request) {
    // Set provider for gothic
    q := r.URL.Query()
    q.Set("provider", "google")
    r.URL.RawQuery = q.Encode()

    gothic.BeginAuthHandler(w, r)
}

func handleCallback(w http.ResponseWriter, r *http.Request) {
    // Set provider for gothic
    q := r.URL.Query()
    q.Set("provider", "google")
    r.URL.RawQuery = q.Encode()

    user, err := gothic.CompleteUserAuth(w, r)
    if err != nil {
        log.Printf("Auth error: %v", err)
        http.Redirect(w, r, "/?error=auth_failed", http.StatusTemporaryRedirect)
        return
    }

    // Store user in session
    session, _ := sessionStore.Get(r, "user-session")
    session.Values["user_id"] = user.UserID
    session.Values["email"] = user.Email
    session.Values["name"] = user.Name
    session.Values["avatar"] = user.AvatarURL
    session.Save(r, w)

    http.Redirect(w, r, "/dashboard", http.StatusTemporaryRedirect)
}

func handleDashboard(w http.ResponseWriter, r *http.Request) {
    session, _ := sessionStore.Get(r, "user-session")
    email, ok := session.Values["email"].(string)
    if !ok || email == "" {
        http.Redirect(w, r, "/", http.StatusTemporaryRedirect)
        return
    }

    name := session.Values["name"].(string)
    avatar := session.Values["avatar"].(string)

    tmpl := template.Must(template.New("dashboard").Parse(`<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
    <h1>Welcome, {{.Name}}!</h1>
    <img src="{{.Avatar}}" alt="Profile" style="width:100px;border-radius:50%">
    <p>Email: {{.Email}}</p>
    <p><a href="/logout">Logout</a></p>
</body>
</html>`))

    tmpl.Execute(w, map[string]string{
        "Name":   name,
        "Email":  email,
        "Avatar": avatar,
    })
}

func handleLogout(w http.ResponseWriter, r *http.Request) {
    session, _ := sessionStore.Get(r, "user-session")
    session.Options.MaxAge = -1
    session.Save(r, w)

    gothic.Logout(w, r)
    http.Redirect(w, r, "/", http.StatusTemporaryRedirect)
}
```

## 4. Install Dependencies

```bash
go mod init myapp
go mod tidy
```

## 5. Run the Application

```bash
go run main.go
```

## 6. Test

1. Open http://localhost:3000
2. Click "Sign in with Google"
3. Complete Google sign-in
4. View dashboard with your profile
5. Click "Logout" to end session

## What's Next?

- Add more providers (Microsoft, GitHub)
- Use Redis for session storage
- Add rate limiting
- Review security checklist
- Deploy with HTTPS

## Echo Framework Version

For Echo framework, see the `goth-echo-security` skill for integration patterns.
