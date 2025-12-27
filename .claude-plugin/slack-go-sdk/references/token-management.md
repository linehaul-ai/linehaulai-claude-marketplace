# Token Management

## Secure Token Storage

### Database Storage

```go
type TokenStore struct {
    db *sql.DB
}

func (ts *TokenStore) StoreToken(token WorkspaceToken) error {
    encrypted := encrypt(token.BotToken)

    _, err := ts.db.Exec(`
        INSERT INTO workspace_tokens (team_id, bot_token, bot_user_id, installed_at)
        VALUES ($1, $2, $3, $4)
        ON CONFLICT (team_id) DO UPDATE
        SET bot_token = $2, bot_user_id = $3, installed_at = $4
    `, token.TeamID, encrypted, token.BotUserID, time.Now())

    return err
}

func (ts *TokenStore) GetToken(teamID string) (string, error) {
    var encrypted string
    err := ts.db.QueryRow(`
        SELECT bot_token FROM workspace_tokens WHERE team_id = $1
    `, teamID).Scan(&encrypted)

    if err != nil {
        return "", err
    }

    return decrypt(encrypted), nil
}
```

### Secrets Manager

```go
import "github.com/aws/aws-sdk-go/service/secretsmanager"

func storeTokenInSecretsManager(teamID, token string) error {
    svc := secretsmanager.New(session.New())

    _, err := svc.PutSecretValue(&secretsmanager.PutSecretValueInput{
        SecretId:     aws.String(fmt.Sprintf("slack/%s/bot-token", teamID)),
        SecretString: aws.String(token),
    })

    return err
}
```

## Token Rotation

```go
func rotateToken(api *slack.Client, refreshToken string) error {
    newTokenResp, err := api.RotateTokens(refreshToken)
    if err != nil {
        return err
    }

    // Update stored token
    return updateStoredToken(newTokenResp.Token)
}
```

## Token Validation

```go
func validateToken(token string) (bool, error) {
    api := slack.New(token)
    authTest, err := api.AuthTest()
    if err != nil {
        return false, err
    }

    return authTest.UserID != "", nil
}
```
