# Events API Webhooks

## HTTP Webhook Server

```go
import (
    "encoding/json"
    "net/http"
)

func handleEventsEndpoint(w http.ResponseWriter, r *http.Request) {
    var payload slackevents.EventsAPIEvent
    if err := json.NewDecoder(r.Body).Decode(&payload); err != nil {
        http.Error(w, "Invalid JSON", http.StatusBadRequest)
        return
    }

    // URL Verification Challenge
    if payload.Type == slackevents.URLVerification {
        var challengeResponse slackevents.ChallengeResponse
        json.NewDecoder(r.Body).Decode(&challengeResponse)
        w.Header().Set("Content-Type", "text/plain")
        w.Write([]byte(challengeResponse.Challenge))
        return
    }

    // Event Callback
    if payload.Type == slackevents.CallbackEvent {
        handleEvent(payload.InnerEvent)
    }

    w.WriteHeader(http.StatusOK)
}
```

## Request Verification

```go
import (
    "github.com/slack-go/slack"
)

func verifyRequest(r *http.Request, signingSecret string) bool {
    verifier, err := slack.NewSecretsVerifier(r.Header, signingSecret)
    if err != nil {
        return false
    }

    body, _ := ioutil.ReadAll(r.Body)
    verifier.Write(body)

    return verifier.Ensure() == nil
}
```

## Production Server

```go
func main() {
    http.HandleFunc("/slack/events", func(w http.ResponseWriter, r *http.Request) {
        if !verifyRequest(r, os.Getenv("SLACK_SIGNING_SECRET")) {
            http.Error(w, "Unauthorized", http.StatusUnauthorized)
            return
        }
        handleEventsEndpoint(w, r)
    })

    log.Fatal(http.ListenAndServe(":3000", nil))
}
```

## Best Practices

1. Verify request signatures
2. Respond within 3 seconds
3. Process events asynchronously
4. Handle retries idempotently
5. Use HTTPS in production
