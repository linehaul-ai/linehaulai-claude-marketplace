# UnblockCarrier

`POST /api/v1/Carrier/UnblockCarrier`

Unblocks a carrier.

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

**Returns:** `UnblockCarrierOutput`

### Top-level: UnblockCarrierOutput

**`UnblockCarrierOutput`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Result` | `boolean` |  |  |
| `Message` | `string` |  |  |


## See also

Related endpoints in **Block / Unblock**:

- [BlockCarrier](./block-carrier.md)
- [BlockedCarriers](./blocked-carriers.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
