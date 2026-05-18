---
name: mycarrierpackets-api
description: "This skill should be used when the user asks to 'integrate with MyCarrierPackets', 'set up MCP API', 'onboard carriers', 'Intellivite invitation', 'monitor carriers', 'Assure Advantage', 'get carrier data', 'retrieve COI', 'get W9', 'carrier risk assessment', 'check completed packets', 'block carrier', 'find associated carriers', 'fraud check', 'VIN verification', or when implementing TMS carrier management features. Provides comprehensive guidance for MyCarrierPackets API authentication, carrier invitations, data retrieval, monitoring, blocking, fraud detection, and document management."
keywords: [mcp, mycarrierpackets, carrier, tms, api, oauth2, monitoring, intellivite, fraud, vin, coi, w9]
disable-model-invocation: false
user-invocable: true
---

# MyCarrierPackets API Integration Guide

**Base URL:** `https://api.mycarrierpackets.com`
**Auth:** OAuth2 Bearer Token (password grant)
**Format:** JSON default; XML with `Accept: text/xml`
**Spec:** Swagger 2.0 — 23 endpoints under `/api/v1/Carrier/*`, all `POST`

## References

This skill uses progressive disclosure. Read SKILL.md for orientation, then load the specific endpoint file you need.

- **[references/endpoints/INDEX.md](references/endpoints/INDEX.md)** — Browse all 23 endpoints grouped by domain (Carrier Data, Invitations, Monitoring, Block/Unblock, Documents, Factoring). Start here when you don't know which endpoint you need.
- **[references/TMS-INTEGRATION.md](references/TMS-INTEGRATION.md)** — Official numbered integration workflow: Intellivite invitations, packet polling, monitoring setup, document retrieval. Load this for end-to-end integration architecture.
- **[references/endpoints/<name>.md](references/endpoints/)** — 23 self-contained files (one per endpoint) with: full param table, response schema, all nested model fields inlined. Load the specific file when implementing that endpoint.

### Endpoint quick map

**Carrier Data**
- [PreviewCarrier](references/endpoints/preview-carrier.md) — profile + risk + cert (no packet)
- [GetCarrierData](references/endpoints/get-carrier-data.md) — full profile **with** packet (W9, agreements, banking, lanes…)
- [GetCarrierContacts](references/endpoints/get-carrier-contacts.md) — authorized/verified users
- [GetCarrierRiskAssessment](references/endpoints/get-carrier-risk-assessment.md) — risk only
- [GetCarrierIncidentReports](references/endpoints/get-carrier-incident-reports.md) — incident history
- [GetCarrierVINVerifications](references/endpoints/get-carrier-vin-verifications.md) — VIN status
- [FindAssociatedCarriers](references/endpoints/find-associated-carriers.md) — phone/email fraud check

**Invitations & Verification**
- [EmailPacketInvitation](references/endpoints/email-packet-invitation.md) — send Intellivite
- [CompletedPackets](references/endpoints/completed-packets.md) — poll for finished onboarding
- [RequestUserVerification](references/endpoints/request-user-verification.md) — non-onboarding identity check
- [RequestVINVerification](references/endpoints/request-vin-verification.md) — VIN verify (phone only, see Non-Obvious)

**Monitoring (Assure Advantage)**
- [RequestMonitoring](references/endpoints/request-monitoring.md) / [CancelMonitoring](references/endpoints/cancel-monitoring.md) — add/remove from watch list
- [MonitoredCarriers](references/endpoints/monitored-carriers.md) — list (paginated)
- [MonitoredCarrierData](references/endpoints/monitored-carrier-data.md) — bulk full data (paginated, expensive)
- [GetMonitoredCarrierContactsData](references/endpoints/get-monitored-carrier-contacts-data.md) — bulk contacts
- [GetMonitoredCarriersRiskAssessment](references/endpoints/get-monitored-carriers-risk-assessment.md) — bulk risk
- [CarriersChanges](references/endpoints/carriers-changes.md) — incremental change feed (paginated, **primary monitoring loop**)

**Block / Unblock**
- [BlockCarrier](references/endpoints/block-carrier.md) / [UnblockCarrier](references/endpoints/unblock-carrier.md)
- [BlockedCarriers](references/endpoints/blocked-carriers.md) — list (paginated)

**Documents**
- [GetDocument](references/endpoints/get-document.md) — download PDF by blob name

**Factoring**
- [GetUpdatedFactoringCompanies](references/endpoints/get-updated-factoring-companies.md) — factoring company ID list

---

## Authentication

> See also: [TMS-INTEGRATION.md § Authentication](references/TMS-INTEGRATION.md#authentication) — Postman testing notes, XML response format.

**Token Endpoint:** `POST https://api.mycarrierpackets.com/token`

```
Content-Type: application/x-www-form-urlencoded

grant_type=password&username={integration_username}&password={integration_password}
```

**Response:** `{ "access_token": "eyJ...", "token_type": "bearer", "expires_in": 3600 }`

Use `Authorization: bearer <access_token>` on every API request. Manage credentials at `https://mycarrierpackets.com/IntegrationTools`.

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

> Official workflow: [TMS-INTEGRATION.md § 1. Intellivite](references/TMS-INTEGRATION.md#1-intellivite--invite-carriers-to-complete-packets) (§1.1 invite API, §1.2 link in TMS email, §1.3 URL to MCP) + [§ 2.1 Completed packets](references/TMS-INTEGRATION.md#21-check-for-completed-carrier-packets).

```
PreviewCarrier  →  EmailPacketInvitation  →  Poll CompletedPackets
```

- [PreviewCarrier](references/endpoints/preview-carrier.md): preload carrier email, risk, cert data before inviting
- [EmailPacketInvitation](references/endpoints/email-packet-invitation.md): include `userName` to link invitation to MCP user
- [CompletedPackets](references/endpoints/completed-packets.md): poll every 5–15 min with a rolling time window

### 2. Assure Advantage Monitoring

> Official workflow: [TMS-INTEGRATION.md § 3. Assure Advantage](references/TMS-INTEGRATION.md#3-assure-advantage-carrier-monitoring) — §3.1 initial/periodic sync, §3.2 batch updates (4-min minimum), §3.6 monitor/unmonitor lifecycle.

```
RequestMonitoring  →  Poll CarriersChanges (5–15 min)
```

- [RequestMonitoring](references/endpoints/request-monitoring.md): add carriers to watch list
- [CarriersChanges](references/endpoints/carriers-changes.md): incremental feed. Returns `ChangeCategories[]` + full `CarrierDetails`. Lock changed fields in TMS as read-only.
- [MonitoredCarrierData](references/endpoints/monitored-carrier-data.md): full sync (paginated, expensive — use sparingly)

See [TMS-INTEGRATION.md § Integration Notes](references/TMS-INTEGRATION.md#integration-notes) for field-locking convention: when a carrier is monitored, fields should be read-only in the TMS so the data always reflects MCP's source of truth.

### 3. Document Retrieval

> Official workflow: [TMS-INTEGRATION.md § 4. Pull Carrier Packet and Assure Advantage Images](references/TMS-INTEGRATION.md#4-pull-carrier-packet-and-assure-advantage-images) — §4.1 per-document blob fetch, §4.2 full packet URL (logged-in), §4.3 full packet PDF API with **separate token endpoint**.

```
GetCarrierData  →  extract blob names  →  GetDocument (binary PDF)
```

- Blob names come from [GetCarrierData](references/endpoints/get-carrier-data.md) response
- Pass to [GetDocument](references/endpoints/get-document.md) to retrieve PDF bytes
- Store locally; don't fetch on every request

**Portal links (no API token required):**
```
View carrier:  https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dot}/DocketNumber/{mc}
Full packet:   https://mycarrierpackets.com/Download/GetCarrierPacket?DOTNumber={dot}&inline=True
```

For the full-packet PDF API in TMS-INTEGRATION.md § 4.3, note the token endpoint is **`/api/token`** (not the main `/token` from § Authentication).

### 4. Fraud Detection

> Not covered in TMS-INTEGRATION.md; combine with the `PossibleFraud` and `DoubleBrokering` flags from [PreviewCarrier](references/endpoints/preview-carrier.md) for layered risk signals.

```
FindAssociatedCarriers?phone=X&email=Y
```

[FindAssociatedCarriers](references/endpoints/find-associated-carriers.md) returns all carriers sharing that phone/email across MCP+FMCSA. Each match includes `PhoneAssociationTypes` and `EmailAssociationTypes` arrays.

### 5. Block / Unblock Carriers

> Not covered in TMS-INTEGRATION.md; this workflow is documented only in the per-endpoint references. Use it to maintain a per-customer carrier deny-list.

```
BlockCarrier  ↔  UnblockCarrier   |   List: BlockedCarriers
```

- [BlockCarrier](references/endpoints/block-carrier.md) / [UnblockCarrier](references/endpoints/unblock-carrier.md): per-customer block list
- [BlockedCarriers](references/endpoints/blocked-carriers.md): paginated list (sync with TMS deny-list)

### 6. VIN Verification

> Not covered in TMS-INTEGRATION.md; this is a standalone verification flow alongside `RequestUserVerification`.

```
RequestVINVerification (deliveryOption=2)  →  Poll GetCarrierVINVerifications
```

- [RequestVINVerification](references/endpoints/request-vin-verification.md): initiate (phone only — see Non-Obvious)
- [GetCarrierVINVerifications](references/endpoints/get-carrier-vin-verifications.md): poll for status

---

## Pagination

Three endpoints return pagination in the **`X-Pagination` response header**:
- [MonitoredCarriers](references/endpoints/monitored-carriers.md) (default 2500, max 5000)
- [BlockedCarriers](references/endpoints/blocked-carriers.md) (default 2500)
- [CarriersChanges](references/endpoints/carriers-changes.md) (default 250, max 500)

[MonitoredCarrierData](references/endpoints/monitored-carrier-data.md) returns pagination in the **response body** (`pageNumber`, `pageSize`, `totalPages`, `totalCount`).

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

> Source: [TMS-INTEGRATION.md § 1.2 Intellivite Link in TMS-Generated Email](references/TMS-INTEGRATION.md#12-intellivite-link-in-tms-generated-email).

```
# Full (recommended — pre-fills DOT+Docket, associates user)
https://mycarrierpackets.com/{IntelliviteID}/Carrier/Intellivite/{MCPUserID}/{DOT}/{MC}

# DOT only (intrastate carriers)
https://mycarrierpackets.com/{IntelliviteID}/Carrier/Intellivite/{MCPUserID}/{DOT}

# Basic (no pre-fill)
https://mycarrierpackets.com/{IntelliviteID}/Carrier/Intellivite
```

`IntelliviteID` is the customer GUID from Integration Tools. `MCPUserID` is the MCP username of the inviting user.

### TMS UI Button Patterns

Common patterns from [TMS-INTEGRATION.md § 2.3 "View Carrier" Button](references/TMS-INTEGRATION.md#23-view-carrier-button) and [§ 3.3 Request COI](references/TMS-INTEGRATION.md#33-request-certificates-of-insurance):

```
View carrier:        https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dot}/DocketNumber/{mc}
Request insurance:   https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dot}/DocketNumber/{mc}?requestInsurance=true
Update carrier now:  call GetCarrierData in real-time (TMS-INTEGRATION § 3.4)
```

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

- **VIN verification**: Only `deliveryOption=2` (phone) works. Email option in spec is not active. See [RequestVINVerification](references/endpoints/request-vin-verification.md).
- **`requestInsurance=true`** query param on CarrierInformation portal URL triggers insurance request flow.
- **Intrastate carriers**: Use `IntrastateNumber` param for monitoring/blocking; omit DocketNumber. Applies to [RequestMonitoring](references/endpoints/request-monitoring.md), [CancelMonitoring](references/endpoints/cancel-monitoring.md), [BlockCarrier](references/endpoints/block-carrier.md), [UnblockCarrier](references/endpoints/unblock-carrier.md).
- **`notificationEmails`** on [EmailPacketInvitation](references/endpoints/email-packet-invitation.md): comma-separated CC list, e.g. `notify1@co.com, notify2@co.com`.
- **Polling [CarriersChanges](references/endpoints/carriers-changes.md)**: minimum 4-minute interval enforced upstream; 5–15 min recommended.
- **[GetCarrierData](references/endpoints/get-carrier-data.md) vs [PreviewCarrier](references/endpoints/preview-carrier.md)**: prefer `PreviewCarrier` for pre-invitation checks — same risk/cert data but faster since it skips packet retrieval.
- **All endpoints are POST** even read operations (no GET). Use query string for params.
- **All param locations are query+header** (no request bodies in this API).
