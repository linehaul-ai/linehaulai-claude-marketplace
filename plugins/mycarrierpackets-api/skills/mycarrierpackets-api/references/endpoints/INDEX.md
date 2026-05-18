# MyCarrierPackets API — Endpoint Index

**Base URL:** `https://api.mycarrierpackets.com`
**Version:** v1
**Auth:** `Authorization: bearer <access_token>` (OAuth2 password grant — see [SKILL.md](../../SKILL.md#authentication))
**Format:** JSON default; XML via `Accept: text/xml`

All endpoints use `POST`. 23 total endpoints across 6 domains.

## Carrier Data

| Endpoint | Path | Summary |
|----------|------|---------|
| [PreviewCarrier](./preview-carrier.md) | `/api/v1/Carrier/PreviewCarrier` | Retrieves carrier profile data, risk assessment, certdata. Excludes carrier packet data. |
| [GetCarrierData](./get-carrier-data.md) | `/api/v1/Carrier/GetCarrierData` | Retrieves carrier profile data, risk assessment, certdata. Includes carrier packet data. |
| [GetCarrierContacts](./get-carrier-contacts.md) | `/api/v1/Carrier/GetCarrierContacts` | Retrieves a list of authorized and verified users for a carrier. |
| [GetCarrierRiskAssessment](./get-carrier-risk-assessment.md) | `/api/v1/Carrier/GetCarrierRiskAssessment` | Returns carrier's risk assessment with provided DOT number and Docket number. |
| [GetCarrierIncidentReports](./get-carrier-incident-reports.md) | `/api/v1/Carrier/GetCarrierIncidentReports` | Retrieves incident report details for a given carrier. |
| [GetCarrierVINVerifications](./get-carrier-vin-verifications.md) | `/api/v1/Carrier/GetCarrierVINVerifications` | Retrieves Carrier VIN Verification status details. |
| [FindAssociatedCarriers](./find-associated-carriers.md) | `/api/v1/Carrier/FindAssociatedCarriers` | Searches carrier contact sources within MCP/FMCSA for associated carriers. |

## Invitations & Verification

| Endpoint | Path | Summary |
|----------|------|---------|
| [EmailPacketInvitation](./email-packet-invitation.md) | `/api/v1/Carrier/EmailPacketInvitation` | Sends an email with a packet to the carrier based on set parameters. |
| [CompletedPackets](./completed-packets.md) | `/api/v1/Carrier/CompletedPackets` | Displays carriers that have completed packets within a specified date range. |
| [RequestUserVerification](./request-user-verification.md) | `/api/v1/Carrier/RequestUserVerification` | Requests user verification (non-onboarding Intellivite). |
| [RequestVINVerification](./request-vin-verification.md) | `/api/v1/Carrier/RequestVINVerification` | Requests Vehicle Identification Number (VIN) verification. |

## Monitoring

| Endpoint | Path | Summary |
|----------|------|---------|
| [RequestMonitoring](./request-monitoring.md) | `/api/v1/Carrier/RequestMonitoring` | Adds a carrier to the monitoring list. |
| [CancelMonitoring](./cancel-monitoring.md) | `/api/v1/Carrier/CancelMonitoring` | Removes a carrier from the monitoring list. |
| [MonitoredCarriers](./monitored-carriers.md) | `/api/v1/Carrier/MonitoredCarriers` | Provides a list of monitored carriers. _📄 paginated (header)_ |
| [MonitoredCarrierData](./monitored-carrier-data.md) | `/api/v1/Carrier/MonitoredCarrierData` | Calls GetCarrierData for all carriers on the monitored list. _📄 paginated (body)_ |
| [GetMonitoredCarrierContactsData](./get-monitored-carrier-contacts-data.md) | `/api/v1/Carrier/GetMonitoredCarrierContactsData` | Retrieves a list of authorized and verified users for every carrier in the monitored list. |
| [GetMonitoredCarriersRiskAssessment](./get-monitored-carriers-risk-assessment.md) | `/api/v1/Carrier/GetMonitoredCarriersRiskAssessment` | Returns all monitored carrier risk assessments in bulk. Includes paging. |
| [CarriersChanges](./carriers-changes.md) | `/api/v1/Carrier/CarriersChanges` | Monitors changes to carrier insurance, risk assessment, and other important details. _📄 paginated (header)_ |

## Block / Unblock

| Endpoint | Path | Summary |
|----------|------|---------|
| [BlockCarrier](./block-carrier.md) | `/api/v1/Carrier/BlockCarrier` | Blocks a carrier. |
| [UnblockCarrier](./unblock-carrier.md) | `/api/v1/Carrier/UnblockCarrier` | Unblocks a carrier. |
| [BlockedCarriers](./blocked-carriers.md) | `/api/v1/Carrier/BlockedCarriers` | Provides a list of blocked carriers. _📄 paginated (header)_ |

## Documents

| Endpoint | Path | Summary |
|----------|------|---------|
| [GetDocument](./get-document.md) | `/api/v1/Carrier/GetDocument` | Pulls PDF documents so the TMS/customer can store them locally for their records. |

## Factoring

| Endpoint | Path | Summary |
|----------|------|---------|
| [GetUpdatedFactoringCompanies](./get-updated-factoring-companies.md) | `/api/v1/Carrier/GetUpdatedFactoringCompanies` | Returns list of MyCarrierPortal Factoring Companies with their unique identifiers. |

## See also

- [SKILL.md](../../SKILL.md) — auth, workflows, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
