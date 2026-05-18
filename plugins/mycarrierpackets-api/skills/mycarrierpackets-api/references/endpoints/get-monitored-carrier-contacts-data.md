# GetMonitoredCarrierContactsData

`POST /api/v1/Carrier/GetMonitoredCarrierContactsData`

Retrieves a list of authorized and verified users for every carrier in the monitored list.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `pageNumber` | `integer (int32)` |  | The current page number. |
| `pageSize` | `integer (int32)` |  | The number of carriers returned per page. The recommended and default value is 250. The max is 500. |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `MonitoredCarriersContactsDataDTO`

### Top-level: MonitoredCarriersContactsDataDTO

**`MonitoredCarriersContactsDataDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `pageNumber` | `integer (int32)` |  |  |
| `pageSize` | `integer (int32)` |  |  |
| `totalPages` | `integer (int32)` |  |  |
| `totalCount` | `integer (int32)` |  |  |
| `succeeded` | `boolean` |  |  |
| `message` | `string` |  |  |
| `data` | `Array[MonitoredCarriersContacts]` |  |  |


### Nested model: MonitoredCarriersContact

**`MonitoredCarriersContact`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `FirstName` | `string` |  |  |
| `LastName` | `string` |  |  |
| `Title` | `string` |  |  |
| `Phone` | `string` |  |  |
| `Email` | `string` |  |  |
| `AuthorizedForPackets` | `boolean` |  |  |
| `VerificationStatus` | `string` |  |  |


### Nested model: MonitoredCarriersContacts

**`MonitoredCarriersContacts`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `LegalName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `CarriersContacts` | `Array[MonitoredCarriersContact]` |  |  |
| `Success` | `boolean` |  |  |
| `Messages` | `Array[string]` |  |  |


## See also

Related endpoints in **Monitoring**:

- [RequestMonitoring](./request-monitoring.md)
- [CancelMonitoring](./cancel-monitoring.md)
- [MonitoredCarriers](./monitored-carriers.md)
- [MonitoredCarrierData](./monitored-carrier-data.md)
- [GetMonitoredCarriersRiskAssessment](./get-monitored-carriers-risk-assessment.md)
- [CarriersChanges](./carriers-changes.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
