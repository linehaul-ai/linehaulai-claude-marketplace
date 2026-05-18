# BlockedCarriers

`POST /api/v1/Carrier/BlockedCarriers`

Provides a list of blocked carriers.

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

**Returns:** `Array[CustomerBlockedCarrierDTO]`

### Top-level: CustomerBlockedCarrierDTO

**`CustomerBlockedCarrierDTO`**

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

Related endpoints in **Block / Unblock**:

- [BlockCarrier](./block-carrier.md)
- [UnblockCarrier](./unblock-carrier.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
