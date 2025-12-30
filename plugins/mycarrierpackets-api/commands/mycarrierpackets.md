---
name: mycarrierpackets
description: MyCarrierPackets API integration assistant for TMS development
argument-hint: "[auth | invite | carrier | monitor | documents | sync | debug]"
allowed-tools: ["Read", "Glob", "Grep", "WebFetch"]
---

# MyCarrierPackets API Integration Assistant

Provide guidance for MyCarrierPackets (MCP) API integration based on the requested topic.

**Topic requested:** $ARGUMENTS

## Topic Routing

If topic is **auth** or **authentication**:
- Focus on OAuth2 password grant flow
- Explain token endpoint and request format
- Provide Go implementation for token management
- Cover token refresh and expiration handling
- Reference credential management via IntegrationTools portal

If topic is **invite** or **invitation** or **intellivite**:
- Explain the three invitation methods (API, Link-based, Direct URL)
- Recommend API-based EmailPacketInvitation with user association
- Cover PreviewCarrier API for preloading data
- Provide link templates for TMS-generated emails
- Handle intrastate carrier scenarios

If topic is **carrier** or **carriers** or **data**:
- Cover GetCarrierData for full carrier profiles
- Explain GetCarrierContacts for authorized users
- Include FindAssociatedCarriers for fraud detection
- Cover GetCarrierIncidentReports and GetCarrierVINVerifications
- Provide Go implementation examples

If topic is **monitor** or **monitoring** or **assure**:
- Explain Assure Advantage monitoring overview
- Cover MonitoredCarriers list management
- Detail RequestMonitoring and CancelMonitoring operations
- Explain CarriersChanges polling (5-15 min intervals)
- Cover risk assessment APIs
- Include pagination handling with X-Pagination header

If topic is **documents** or **document** or **coi** or **w9**:
- Explain GetDocument API with blob names
- Cover document types: COI, W9, eAgreement
- Detail full packet PDF retrieval
- Provide "View Carrier" button URLs
- Handle browser view vs API download differences

If topic is **sync** or **synchronization** or **polling**:
- Compare Push vs Pull integration models
- Detail CompletedPackets polling pattern
- Explain CarriersChanges incremental sync
- Cover MonitoredCarrierData bulk sync
- Provide Go polling implementation
- Recommend polling intervals (5-15 minutes)

If topic is **debug** or **troubleshoot** or **errors**:
- Cover common HTTP error codes (400, 401, 403, 404, 429, 500)
- Explain authentication issues and token expiration
- Detail rate limiting and polling frequency
- Provide error handling implementation
- Cover retry with exponential backoff

If **no topic specified** or topic is empty:
- Provide overview of MyCarrierPackets API capabilities
- List available topics with brief descriptions:
  - **auth**: OAuth2 authentication setup
  - **invite**: Carrier invitations (Intellivite)
  - **carrier**: Carrier data retrieval
  - **monitor**: Assure Advantage monitoring
  - **documents**: COI, W9, eAgreement retrieval
  - **sync**: Data synchronization patterns
  - **debug**: Error handling and troubleshooting
- Suggest starting with `auth` topic for new integrations

## Response Guidelines

1. Reference the mycarrierpackets-api skill for detailed information
2. Provide Go code examples as the primary language
3. Include endpoint URLs and request/response examples
4. Link to relevant sections of the comprehensive API documentation
5. Offer to explore related topics after answering

## Example Prompts by Topic

- `/mycarrierpackets auth` - "Show me how to authenticate with OAuth2"
- `/mycarrierpackets invite` - "How do I send carrier invitations?"
- `/mycarrierpackets carrier` - "Help me retrieve carrier profile data"
- `/mycarrierpackets monitor` - "Set up Assure Advantage monitoring"
- `/mycarrierpackets documents` - "How do I download COI certificates?"
- `/mycarrierpackets sync` - "What's the best polling strategy?"
- `/mycarrierpackets debug` - "I'm getting 401 errors, help!"
