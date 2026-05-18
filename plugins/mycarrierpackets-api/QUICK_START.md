# Quick Start

## 1. Authentication Setup

Get your API credentials from the [IntegrationTools portal](https://mycarrierpackets.com/IntegrationTools).

```bash
export MCP_USERNAME="your_username"
export MCP_PASSWORD="your_password"
```

## 2. Get an Access Token

```go
// Token endpoint
POST https://api.mycarrierpackets.com/token
Content-Type: application/x-www-form-urlencoded

grant_type=password&username={username}&password={password}
```

Response:
```json
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

## 3. Make API Calls

Use the bearer token for all API requests:

```go
// Get carrier data
POST https://api.mycarrierpackets.com/api/v1/Carrier/GetCarrierData
    ?DOTNumber=23868
    &DocketNumber=MC113843
Authorization: bearer {access_token}
```

## 4. Common Operations

### Preview a Carrier Before Invitation
```
POST /api/v1/Carrier/PreviewCarrier?DOTNumber=23868&docketNumber=MC113843
```

### Send Carrier Invitation
```
POST /api/v1/Carrier/EmailPacketInvitation
    ?dotNumber=23868
    &docketNumber=MC113843
    &carrierEmail=carrier@example.com
```

### Add Carrier to Monitoring
```
POST /api/v1/Carrier/RequestMonitoring
Body: { "DOTNumber": 23868, "DocketNumber": "MC113843" }
```

### Poll for Changes
```
POST /api/v1/Carrier/CarriersChanges
    ?fromDate=2024-01-01T00:00:00
    &toDate=2024-01-02T00:00:00
```

## 5. Get Detailed Help

Use the `/mycarrierpackets` command for topic-specific guidance:

```
/mycarrierpackets auth        # Authentication details
/mycarrierpackets invite      # Invitation patterns
/mycarrierpackets carrier     # Profile, contacts, risk, incidents
/mycarrierpackets monitor     # Monitoring setup
/mycarrierpackets documents   # COI, W9, packet PDFs
/mycarrierpackets sync        # Polling strategies
/mycarrierpackets block       # Per-customer deny-list
/mycarrierpackets fraud       # Phone/email association lookup
/mycarrierpackets vin         # VIN verification
/mycarrierpackets factoring   # Factoring directory
/mycarrierpackets debug       # Error handling
/mycarrierpackets endpoints   # Full endpoint INDEX
```

## Next Steps

- Browse `skills/mycarrierpackets-api/references/endpoints/INDEX.md` for the full endpoint catalog
- Read `skills/mycarrierpackets-api/references/TMS-INTEGRATION.md` for the official numbered integration workflow
- Set up polling for `CompletedPackets` (5–15 min intervals)
- Configure Assure Advantage monitoring (`CarriersChanges` poll, 5–15 min)
- Implement error handling with retry + exponential backoff (clear cached token on 401)
