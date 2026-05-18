---
name: mycarrierpackets
description: MyCarrierPackets API integration assistant for TMS development
argument-hint: "[auth | invite | carrier | monitor | documents | sync | block | fraud | vin | factoring | debug]"
allowed-tools: ["Read", "Glob", "Grep", "WebFetch"]
---

# MyCarrierPackets API Integration Assistant

Provide guidance for MyCarrierPackets (MCP) API integration based on the requested topic.

**Topic requested:** $ARGUMENTS

## Reference layout

The `mycarrierpackets-api` skill has progressive-disclosure references:

- `references/endpoints/INDEX.md` — Browse all 23 endpoints grouped by domain
- `references/endpoints/<kebab-name>.md` — One file per endpoint, self-contained (params + full response schema)
- `references/TMS-INTEGRATION.md` — Official numbered integration workflow

When routing a topic, **always load the specific endpoint files** listed below — not the SKILL.md alone. The SKILL provides workflow context; the endpoint files provide the exact schemas needed to write working code.

---

## Topic Routing

### `auth` | `authentication`

OAuth2 password grant flow.

**Load:**
- `skills/mycarrierpackets-api/SKILL.md` § Authentication (token request, Go client with thread-safe caching)

**Cover:**
- Token endpoint: `POST /token` with `grant_type=password`
- Bearer token usage: `Authorization: bearer <access_token>` on every call
- Token expiry handling (clear on 401, refresh 60s before `expires_in`)
- Credential management at `https://mycarrierpackets.com/IntegrationTools`
- Go implementation (sync.RWMutex pattern, double-checked locking)

### `invite` | `invitation` | `intellivite`

Carrier onboarding via Intellivite.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/preview-carrier.md` — preload approved emails, risk, cert before invite
- `skills/mycarrierpackets-api/references/endpoints/email-packet-invitation.md` — send invite (use `userName` to associate to MCP user)
- `skills/mycarrierpackets-api/references/endpoints/completed-packets.md` — poll for completed packets (5–15 min rolling window)
- `skills/mycarrierpackets-api/references/TMS-INTEGRATION.md` § 1. Intellivite

**Cover:**
- Three invitation methods (API, Link-based, Direct URL) — recommend API + user association
- Intellivite link formats from SKILL.md
- Intrastate carrier handling (omit DocketNumber)
- `notificationEmails` for CC list

### `carrier` | `carriers` | `data`

Carrier profile and contact retrieval.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/preview-carrier.md` — fast profile (no packet)
- `skills/mycarrierpackets-api/references/endpoints/get-carrier-data.md` — full profile **with** packet (W9, agreements, banking, lanes, drivers…)
- `skills/mycarrierpackets-api/references/endpoints/get-carrier-contacts.md` — authorized users
- `skills/mycarrierpackets-api/references/endpoints/get-carrier-risk-assessment.md` — risk only
- `skills/mycarrierpackets-api/references/endpoints/get-carrier-incident-reports.md` — incidents
- `skills/mycarrierpackets-api/references/endpoints/find-associated-carriers.md` — fraud-by-association

**Cover:**
- `PreviewCarrier` vs `GetCarrierData` tradeoff (prefer Preview pre-invite — faster, same risk/cert)
- Response schema differences (Preview returns array; GetCarrierData returns CarrierAADTO with full packet DTOs)
- Go struct examples mirroring the endpoint schema

### `monitor` | `monitoring` | `assure`

Assure Advantage carrier monitoring.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/request-monitoring.md` / `cancel-monitoring.md`
- `skills/mycarrierpackets-api/references/endpoints/monitored-carriers.md` — paginated list (header pagination)
- `skills/mycarrierpackets-api/references/endpoints/carriers-changes.md` — **primary monitoring loop** (incremental change feed, 5–15 min polling)
- `skills/mycarrierpackets-api/references/endpoints/monitored-carrier-data.md` — bulk full sync (body pagination, expensive)
- `skills/mycarrierpackets-api/references/endpoints/get-monitored-carriers-risk-assessment.md` — bulk risk
- `skills/mycarrierpackets-api/references/endpoints/get-monitored-carrier-contacts-data.md` — bulk contacts
- `skills/mycarrierpackets-api/references/TMS-INTEGRATION.md` § monitoring sections

**Cover:**
- Monitoring lifecycle: Request → CarriersChanges polling → Cancel
- `ChangeCategories[]` semantics, locking changed fields as read-only in TMS
- Pagination: `X-Pagination` header parsing
- Minimum 4-min poll interval enforced upstream; 5–15 min recommended

### `documents` | `document` | `coi` | `w9`

Document (PDF) retrieval.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/get-carrier-data.md` — extract blob names from response
- `skills/mycarrierpackets-api/references/endpoints/get-document.md` — fetch PDF bytes by blob name
- `skills/mycarrierpackets-api/references/TMS-INTEGRATION.md` § documents

**Cover:**
- Blob name flow: `GetCarrierData` → extract → `GetDocument(name=...)` → store locally
- Document types: COI, W9, eAgreement, company-agreement
- Portal URLs (no API token required):
  - View carrier: `https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dot}/DocketNumber/{mc}`
  - Full packet: `https://mycarrierpackets.com/Download/GetCarrierPacket?DOTNumber={dot}&inline=True`
- Browser view vs API download distinction

### `sync` | `synchronization` | `polling`

Data synchronization patterns.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/completed-packets.md` — invitation completion polling
- `skills/mycarrierpackets-api/references/endpoints/carriers-changes.md` — monitoring change feed
- `skills/mycarrierpackets-api/references/endpoints/monitored-carrier-data.md` — bulk reconciliation
- `skills/mycarrierpackets-api/SKILL.md` § Pagination (Go pagination loop example)

**Cover:**
- Push vs Pull model (MCP is poll-only — no webhooks)
- Rolling time windows for `CompletedPackets`
- Incremental sync via `CarriersChanges`
- Full reconciliation via `MonitoredCarrierData` (rare — expensive)
- Polling intervals (5–15 min)
- Pagination patterns: `X-Pagination` header vs response body

### `block` | `unblock` | `blocked` | `blocklist` | `denylist`

Per-customer carrier block list.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/block-carrier.md`
- `skills/mycarrierpackets-api/references/endpoints/unblock-carrier.md`
- `skills/mycarrierpackets-api/references/endpoints/blocked-carriers.md` — paginated list

**Cover:**
- Block/unblock with DOT or IntrastateNumber
- Periodic sync of `BlockedCarriers` to TMS deny-list (paginated)
- Idempotency considerations

### `fraud` | `associated` | `phone-check` | `email-check`

Fraud detection by phone/email association.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/find-associated-carriers.md`
- `skills/mycarrierpackets-api/references/endpoints/preview-carrier.md` — also returns `PossibleFraud`, `DoubleBrokering`, `FraudCallNumber` flags
- `skills/mycarrierpackets-api/references/endpoints/get-carrier-incident-reports.md` — incident history with fraud counts

**Cover:**
- `FindAssociatedCarriers?phone=X&email=Y` query pattern
- Response: `PhoneAssociationTypes[]`, `EmailAssociationTypes[]` per match
- Cross-source matching: MCP carriers + FMCSA carriers
- Combine with `PossibleFraud`/`DoubleBrokering` from PreviewCarrier for layered risk signals

### `vin` | `vin-verification` | `verify-vin`

VIN verification flow.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/request-vin-verification.md`
- `skills/mycarrierpackets-api/references/endpoints/get-carrier-vin-verifications.md`
- `skills/mycarrierpackets-api/references/endpoints/request-user-verification.md` — sibling identity-verification API

**Cover:**
- **⚠️ Only `deliveryOption=2` (phone) works**; email delivery is documented but not active
- Request → poll `GetCarrierVINVerifications` for status
- Difference vs `RequestUserVerification` (non-onboarding identity)

### `factoring`

Factoring company directory.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/get-updated-factoring-companies.md`

**Cover:**
- Returns list of MCP factoring companies with unique IDs
- Use to map carrier's `FactoringCompanyID` → name in TMS UI
- Incremental updates (sync periodically, not per-request)

### `debug` | `troubleshoot` | `errors`

Error handling and troubleshooting.

**Load:**
- `skills/mycarrierpackets-api/SKILL.md` § Error Handling and § Non-Obvious Behaviors

**Cover:**
- HTTP error codes (400, 401, 403, 404, 429, 500) and recommended action per status
- 401 → clear cached `accessToken`, next call re-authenticates
- Rate-limit handling: minimum 5-min polling, exponential backoff
- Non-obvious behaviors that cause silent failures:
  - VIN email option ignored
  - Intrastate carriers need `IntrastateNumber`, not DocketNumber
  - `notificationEmails` comma-separated format
  - `CarriersChanges` 4-min upstream minimum

### `endpoints` | `list` | `index` | no topic specified

Provide an overview.

**Load:**
- `skills/mycarrierpackets-api/references/endpoints/INDEX.md`

**Show available topics:**

| Topic | Purpose |
|-------|---------|
| `auth` | OAuth2 password-grant token flow |
| `invite` | Carrier onboarding (Intellivite) |
| `carrier` | Profile, contacts, risk, incidents |
| `monitor` | Assure Advantage monitoring + change feed |
| `documents` | COI / W9 / packet PDFs |
| `sync` | Polling patterns and pagination |
| `block` | Per-customer block list |
| `fraud` | Phone/email association lookup |
| `vin` | VIN verification flow |
| `factoring` | Factoring company directory |
| `debug` | Error handling, rate limits, gotchas |
| `endpoints` | Full endpoint INDEX |

Suggest starting with `auth` for new integrations, then `invite` for onboarding flow, then `monitor` for steady-state operations.

---

## Response Guidelines

1. **Load referenced endpoint files** before answering — schemas live there, not in this command file
2. Provide **Go code examples** as the primary language (mirror the existing client pattern in SKILL.md)
3. Include real endpoint paths and request/response field names (from the loaded endpoint file)
4. Note pagination shape (header vs body) when relevant
5. Flag any non-obvious behavior from SKILL.md § Non-Obvious Behaviors
6. Offer to explore related topics after answering

## Example Prompts by Topic

- `/mycarrierpackets auth` — "Show me how to authenticate with OAuth2"
- `/mycarrierpackets invite` — "How do I send carrier invitations?"
- `/mycarrierpackets carrier` — "Help me retrieve carrier profile data"
- `/mycarrierpackets monitor` — "Set up Assure Advantage monitoring"
- `/mycarrierpackets documents` — "How do I download COI certificates?"
- `/mycarrierpackets sync` — "What's the best polling strategy?"
- `/mycarrierpackets block` — "Sync our deny-list with MCP blocked carriers"
- `/mycarrierpackets fraud` — "Check if these phones/emails are associated with known fraud"
- `/mycarrierpackets vin` — "Request and poll VIN verifications"
- `/mycarrierpackets factoring` — "Map factoring company IDs to names"
- `/mycarrierpackets debug` — "I'm getting 401 errors, help!"
- `/mycarrierpackets endpoints` — "Show me the full endpoint catalog"
