# GetDocument

`POST /api/v1/Carrier/GetDocument`

Pulls PDF documents so the TMS/customer can store them locally for their records.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `name` | `string` | yes | The name of the document. Example: company-agreement/12/f9f10ed2-799a-4521-a09b-19fb088e16c2 |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `object`

## See also

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
