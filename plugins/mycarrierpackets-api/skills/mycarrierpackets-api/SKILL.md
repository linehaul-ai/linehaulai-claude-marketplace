---
name: mycarrierpackets-api
description: "This skill should be used when the user asks to 'integrate with MyCarrierPackets', 'set up MCP API', 'onboard carriers', 'Intellivite invitation', 'monitor carriers', 'Assure Advantage', 'get carrier data', 'retrieve COI', 'get W9', 'carrier risk assessment', 'check completed packets', or when implementing TMS carrier management features. Provides comprehensive guidance for MyCarrierPackets API authentication, carrier invitations, data retrieval, monitoring, and document management."
keywords: [mcp, mycarrierpackets, carrier, tms, api, oauth2, monitoring, intellivite]
disable-model-invocation: false
user-invocable: true
---

# MyCarrierPackets API Integration Guide

**Base URL:** `https://api.mycarrierpackets.com`  
**Auth:** OAuth2 Bearer Token (password grant)  
**Format:** JSON default; XML with `Accept: text/xml`

## References

- **[references/endpoint-reference.md](references/endpoint-reference.md)** — All 23 endpoints: full request params, response schemas, pagination details. Load this when implementing any endpoint.
- **[references/TMS-INTEGRATION.md](references/TMS-INTEGRATION.md)** — Official MCP numbered integration workflow: Intellivite invitations, packet polling, monitoring setup, document retrieval. Load this for end-to-end integration architecture.

---

## Authentication

**Token Endpoint:** `POST https://api.mycarrierpackets.com/token`

```
Content-Type: application/x-www-form-urlencoded

grant_type=password&username={integration_username}&password={integration_password}
```

**Response:** `{ "access_token": "eyJ...", "token_type": "bearer", "expires_in": 3600 }`

Use `Authorization: bearer <access_token>` on every API request.

Manage credentials at: `https://mycarrierpackets.com/IntegrationTools`

### Go Client (thread-safe token caching)

```go
type MCPClient struct {
    baseURL     string
    httpClient  *http.Client
    username    string
    password    string
    accessToken string
    tokenExpiry time.Time
    tokenMu     sync.RWMutex
}

func (c *MCPClient) getToken(ctx context.Context) (string, error) {
    c.tokenMu.RLock()
    if c.accessToken != "" && time.Now().Before(c.tokenExpiry) {
        token := c.accessToken
        c.tokenMu.RUnlock()
        return token, nil
    }
    c.tokenMu.RUnlock()

    c.tokenMu.Lock()
    defer c.tokenMu.Unlock()

    data := url.Values{}
    data.Set("grant_type", "password")
    data.Set("username", c.username)
    data.Set("password", c.password)

    req, _ := http.NewRequestWithContext(ctx, "POST", c.baseURL+"/token", strings.NewReader(data.Encode()))
    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

    resp, err := c.httpClient.Do(req)
    if err != nil {
        return "", fmt.Errorf("token request: %w", err)
    }
    defer resp.Body.Close()

    var tokenResp struct {
        AccessToken string `json:"access_token"`
        ExpiresIn   int    `json:"expires_in"`
    }
    json.NewDecoder(resp.Body).Decode(&tokenResp)

    c.accessToken = tokenResp.AccessToken
    c.tokenExpiry = time.Now().Add(time.Duration(tokenResp.ExpiresIn-60) * time.Second)
    return c.accessToken, nil
}
```

---

## Key Workflows

### 1. Carrier Invitation (Intellivite)

```
PreviewCarrier  →  EmailPacketInvitation  →  Poll CompletedPackets
```

- `PreviewCarrier`: preload carrier email, risk, cert data before inviting
- `EmailPacketInvitation`: include `userName` to link invitation to MCP user
- Poll `CompletedPackets` every 5–15 min with a rolling time window

### 2. Assure Advantage Monitoring

```
RequestMonitoring  →  Poll CarriersChanges (5–15 min)
```

On changes, `CarriersChanges` returns `ChangeCategories[]` + full `CarrierDetails`. Lock monitored fields in TMS as read-only.

Full sync: `MonitoredCarrierData` (paginated, expensive — use sparingly).

### 3. Document Retrieval

Blob names come from `GetCarrierData` response. Pass to `GetDocument` to retrieve PDF bytes. Store locally; don't fetch on every request.

```
GetCarrierData  →  extract blob names  →  GetDocument (binary PDF)
```

Portal links (no API token required):
```
View carrier:  https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dot}/DocketNumber/{mc}
Full packet:   https://mycarrierpackets.com/Download/GetCarrierPacket?DOTNumber={dot}&inline=True
```

### 4. Fraud Detection

```
FindAssociatedCarriers?phone=X&email=Y
```

Returns all carriers sharing that phone/email across MCP+FMCSA. Each match includes `PhoneAssociationTypes` and `EmailAssociationTypes` arrays.

---

## Pagination

Three endpoints return pagination in the **`X-Pagination` response header**:
- `MonitoredCarriers` (default 2500, max 5000)
- `BlockedCarriers` (default 2500)
- `CarriersChanges` (default 250, max 500)

**`MonitoredCarrierData`** returns pagination in the **response body** (`pageNumber`, `pageSize`, `totalPages`, `totalCount`).

Parse `X-Pagination` as JSON: `{"pageNumber":1,"pageSize":250,"totalPages":10,"totalCount":2500}`

```go
func (c *MCPClient) GetAllMonitoredCarriers(ctx context.Context) ([]MonitoredCarrier, error) {
    var all []MonitoredCarrier
    page := 1
    for {
        endpoint := fmt.Sprintf("/api/v1/Carrier/MonitoredCarriers?pageNumber=%d&pageSize=2500", page)
        resp, err := c.doRequest(ctx, "POST", endpoint, nil)
        if err != nil {
            return nil, err
        }
        var carriers []MonitoredCarrier
        json.NewDecoder(resp.Body).Decode(&carriers)
        resp.Body.Close()
        all = append(all, carriers...)

        pag := resp.Header.Get("X-Pagination")
        if pag == "" || len(carriers) == 0 {
            break
        }
        var meta struct{ TotalPages int `json:"totalPages"` }
        json.Unmarshal([]byte(pag), &meta)
        if page >= meta.TotalPages {
            break
        }
        page++
    }
    return all, nil
}
```

---

## Intellivite Link Formats

```
# Full (recommended — pre-fills DOT+Docket, associates user)
https://mycarrierpackets.com/{IntelliviteID}/Carrier/Intellivite/{MCPUserID}/{DOT}/{MC}

# DOT only (intrastate carriers)
https://mycarrierpackets.com/{IntelliviteID}/Carrier/Intellivite/{MCPUserID}/{DOT}

# Basic (no pre-fill)
https://mycarrierpackets.com/{IntelliviteID}/Carrier/Intellivite
```

`IntelliviteID` is the customer GUID from Integration Tools. `MCPUserID` is the MCP username of the inviting user.

---

## Error Handling

| Status | Meaning | Action |
|--------|---------|--------|
| 400 | Bad request | Check parameter format |
| 401 | Unauthorized | Clear cached token, re-authenticate |
| 403 | Forbidden | Check API permissions in Integration Tools |
| 404 | Not found | Invalid DOT/Docket |
| 429 | Rate limited | Increase polling interval (min 5 min) |
| 500 | Server error | Retry with exponential backoff |

On 401: clear `accessToken` so next call re-authenticates automatically.

---

## Non-Obvious Behaviors

- **VIN verification**: Only `deliveryOption=2` (phone) works. Email option in spec is not active.
- **`requestInsurance=true`** query param on CarrierInformation portal URL triggers insurance request flow.
- **Intrastate carriers**: Use `IntrastateNumber` param for monitoring/blocking; omit DocketNumber.
- **`notificationEmails`** on `EmailPacketInvitation`: comma-separated CC list, e.g. `notify1@co.com, notify2@co.com`
- **Polling `CarriersChanges`**: minimum 4-minute interval enforced upstream; 5–15 min recommended.
- **`GetCarrierData` vs `PreviewCarrier`**: prefer `PreviewCarrier` for pre-invitation checks — same risk/cert data but faster since it skips packet retrieval.
