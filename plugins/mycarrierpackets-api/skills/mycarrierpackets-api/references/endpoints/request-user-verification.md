# RequestUserVerification

`POST /api/v1/Carrier/RequestUserVerification`

Requests user verification (non-onboarding Intellivite).

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `userVerificationEmail` | `string` | yes | Email of the user. Example: abc@somedomain.com |
| `dotNumber` | `integer (int32)` |  | DOT number of the carrier. Example: 12345 |
| `docketNumber` | `string` |  | Docket number of the carrier. Example: MC12345 |
| `userName` | `string` |  | Username of the customer. Optional parameter. Example: abc |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `object`

## See also

Related endpoints in **Invitations & Verification**:

- [EmailPacketInvitation](./email-packet-invitation.md)
- [CompletedPackets](./completed-packets.md)
- [RequestVINVerification](./request-vin-verification.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
