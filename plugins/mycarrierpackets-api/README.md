# MyCarrierPackets API Plugin

Expert guidance for integrating MyCarrierPackets (MCP) API with Transportation Management Systems. Covers all 23 endpoints with per-endpoint reference files generated directly from the official Swagger 2.0 spec.

## Features

- **OAuth2 Authentication** — Token management with automatic refresh, thread-safe Go client
- **Carrier Invitations (Intellivite)** — API, link-based, and direct URL methods
- **Carrier Data Management** — Profile retrieval, contacts, incident reports
- **Assure Advantage Monitoring** — Incremental change feed, full sync, per-carrier risk
- **Document Retrieval** — COI, W9, eAgreement, full packet PDFs
- **Block / Unblock** — Per-customer carrier deny-list management
- **Fraud Detection** — Phone/email association lookup across MCP + FMCSA
- **VIN Verification** — Vehicle identity verification workflow
- **Factoring Directory** — Sync MCP factoring company IDs to TMS
- **Integration Patterns** — Push/pull synchronization, header vs body pagination, polling strategies

## Quick Start

```bash
# Install from marketplace
/plugin install mycarrierpackets-api

# Get help on a topic
/mycarrierpackets auth
/mycarrierpackets invite
/mycarrierpackets monitor
/mycarrierpackets endpoints     # Browse the full endpoint catalog
```

## Available Topics

| Topic | Description |
|-------|-------------|
| `auth` | OAuth2 authentication setup |
| `invite` | Carrier invitations (Intellivite) |
| `carrier` | Carrier data retrieval (profile, contacts, risk, incidents) |
| `monitor` | Assure Advantage monitoring + change feed |
| `documents` | COI, W9, eAgreement, full packet PDFs |
| `sync` | Polling patterns and pagination |
| `block` | Per-customer carrier deny-list |
| `fraud` | Phone/email association lookup |
| `vin` | VIN verification flow |
| `factoring` | Factoring company directory |
| `debug` | Error handling, rate limits, gotchas |
| `endpoints` | Full endpoint INDEX |

## Documentation Layout

The plugin uses progressive disclosure:

```
skills/mycarrierpackets-api/
├── SKILL.md                                # Orientation: auth, workflows, gotchas
└── references/
    ├── TMS-INTEGRATION.md                  # Official numbered integration workflow
    └── endpoints/
        ├── INDEX.md                        # Catalog grouped by domain
        └── <endpoint>.md                   # 23 self-contained endpoint files
```

Each endpoint file contains: description, query/header parameter tables, full response schema with all nested model fields inlined, pagination notes, and cross-links to sibling endpoints.

## Prerequisites

- MyCarrierPackets account with API access
- Integration credentials from [IntegrationTools portal](https://mycarrierpackets.com/IntegrationTools)
- Go development environment (for code examples)

## API Overview

- **Base URL:** `https://api.mycarrierpackets.com`
- **Spec:** Swagger 2.0 (23 endpoints under `/api/v1/Carrier/*`, all `POST`)
- **Auth:** OAuth2 Bearer Token (password grant)
- **Format:** JSON default; XML via `Accept: text/xml`

## License

MIT
