# EmailPacketInvitation

`POST /api/v1/Carrier/EmailPacketInvitation`

Sends an email with a packet to the carrier based on set parameters.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `carrierEmail` | `string` | yes | Email of the carrier. Example: abc@somedomain.com |
| `dotNumber` | `integer (int32)` |  | DOT number of the carrier. Example: 12345 |
| `docketNumber` | `string` |  | Docket number of the carrier. Example: MC12345 |
| `userName` | `string` |  | Username of the customer. Optional parameter. Example: abc |
| `sendConfirmationEmail` | `boolean` |  | Indicates whether or not to send a confirmation email that the invitation was sent. Optional Parameter. |
| `notificationEmails` | `string` |  | Comma-separated list of additional emails to notify. Example: notify1@domain.com, notify2@domain.com |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `object`

## See also

Related endpoints in **Invitations & Verification**:

- [CompletedPackets](./completed-packets.md)
- [RequestUserVerification](./request-user-verification.md)
- [RequestVINVerification](./request-vin-verification.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
