# MyCarrierPackets API Plugin

Expert guidance for integrating MyCarrierPackets (MCP) API with Transportation Management Systems.

## Features

- **OAuth2 Authentication** - Token management with automatic refresh
- **Carrier Invitations (Intellivite)** - API, link-based, and direct URL methods
- **Carrier Data Management** - Profile retrieval, contacts, fraud detection
- **Assure Advantage Monitoring** - Continuous carrier monitoring and risk assessment
- **Document Retrieval** - COI, W9, eAgreement, and full packet PDFs
- **Integration Patterns** - Push/pull synchronization, polling strategies

## Quick Start

```bash
# Install from marketplace
/plugin install mycarrierpackets-api

# Get help on a topic
/mycarrierpackets auth
/mycarrierpackets invite
/mycarrierpackets monitor
```

## Available Topics

| Topic | Description |
|-------|-------------|
| `auth` | OAuth2 authentication setup |
| `invite` | Carrier invitations (Intellivite) |
| `carrier` | Carrier data retrieval |
| `monitor` | Assure Advantage monitoring |
| `documents` | Document retrieval (COI, W9) |
| `sync` | Data synchronization patterns |
| `debug` | Error handling and troubleshooting |

## Prerequisites

- MyCarrierPackets account with API access
- Integration credentials from [IntegrationTools portal](https://mycarrierpackets.com/IntegrationTools)
- Go development environment (for code examples)

## API Overview

**Base URL:** `https://api.mycarrierpackets.com`
**Version:** v1
**Authentication:** OAuth2 Bearer Token

## License

MIT
