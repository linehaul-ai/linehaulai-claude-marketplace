# RequestMonitoring

`POST /api/v1/Carrier/RequestMonitoring`

Adds a carrier to the monitoring list.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  | DOT Number |
| `DocketNumber` | `string` |  | Docket number or MC Number |
| `IntrastateNumber` | `string` |  | Intrastate Number |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `RequestMonitoringOutput`

### Top-level: RequestMonitoringOutput

**`RequestMonitoringOutput`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `MonitoringID` | `integer (int64)` |  |  |
| `RequestDate` | `string (date-time)` |  |  |


## See also

Related endpoints in **Monitoring**:

- [CancelMonitoring](./cancel-monitoring.md)
- [MonitoredCarriers](./monitored-carriers.md)
- [MonitoredCarrierData](./monitored-carrier-data.md)
- [GetMonitoredCarrierContactsData](./get-monitored-carrier-contacts-data.md)
- [GetMonitoredCarriersRiskAssessment](./get-monitored-carriers-risk-assessment.md)
- [CarriersChanges](./carriers-changes.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
