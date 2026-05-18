# CompletedPackets

`POST /api/v1/Carrier/CompletedPackets`

Displays carriers that have completed packets within a specified date range.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `fromDate` | `string (date-time)` | yes | From Date. Example: 2021-07-01T01:00:00 |
| `toDate` | `string (date-time)` | yes | To Date. Required parameter. Example: 2021-07-01T14:00:00 |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `Array[CompletedPacketDTO]`

### Top-level: CompletedPacketDTO

**`CompletedPacketDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `LegalName` | `string` |  |  |
| `CompletedDate` | `string (date-time)` |  |  |


## See also

Related endpoints in **Invitations & Verification**:

- [EmailPacketInvitation](./email-packet-invitation.md)
- [RequestUserVerification](./request-user-verification.md)
- [RequestVINVerification](./request-vin-verification.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
