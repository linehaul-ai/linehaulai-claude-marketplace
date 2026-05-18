# MonitoredCarriers

`POST /api/v1/Carrier/MonitoredCarriers`

Provides a list of monitored carriers.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `pageNumber` | `integer (int32)` |  | The current page number. |
| `pageSize` | `integer (int32)` |  | The number of carriers returned per page. The recommended and default value is 2500. The max is 5000. |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

> **Pagination:** returned in `X-Pagination` response header as JSON: `{pageNumber, pageSize, totalPages, totalCount}`.

## Response (200)

**Returns:** `Array[MonitoredCarrierDTO]`

### Top-level: MonitoredCarrierDTO

**`MonitoredCarrierDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `IntrastateNumber` | `string` |  |  |
| `CreatedDate` | `string (date-time)` |  |  |
| `CreatedBy` | `string` |  |  |
| `LastModifiedDate` | `string (date-time)` |  |  |
| `LastModifiedBy` | `string` |  |  |


## See also

Related endpoints in **Monitoring**:

- [RequestMonitoring](./request-monitoring.md)
- [CancelMonitoring](./cancel-monitoring.md)
- [MonitoredCarrierData](./monitored-carrier-data.md)
- [GetMonitoredCarrierContactsData](./get-monitored-carrier-contacts-data.md)
- [GetMonitoredCarriersRiskAssessment](./get-monitored-carriers-risk-assessment.md)
- [CarriersChanges](./carriers-changes.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
