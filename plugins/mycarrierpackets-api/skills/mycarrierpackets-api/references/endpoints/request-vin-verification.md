# RequestVINVerification

`POST /api/v1/Carrier/RequestVINVerification`

Requests Vehicle Identification Number (VIN) verification.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `deliveryOption` | `integer (int32)` | yes | Method for sending the request. Only PhoneNumber (2) is supported.Value/Type List: 1 = Email, 2 = PhoneNumber; Value Only List: (enum: [1, 2]) |
| `vinVerificationEmail` | `string` |  | Not used. Email VIN validations are no longer supported. |
| `vinVerificationPhoneNumber` | `string` |  | Phone number to send the request to |
| `dotNumber` | `integer (int32)` |  | DOT number of the carrier. Example: 12345 |
| `docketNumber` | `string` |  | Docket number of the carrier. Example: MC12345 |
| `userName` | `string` |  | Username of the customer. Optional parameter. Example: abc |
| `outputVINVerificationRequestID` | `boolean` |  | Output VIN Verification Request ID. Example: false |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

Returns either a plain text string containing a message when outputVINVerificationRequestID is false, or an object with 'VinVerificationRequestID' and 'Message' when outputVINVerificationRequestID is true.

**Returns:** `RequestVINVerificationOutput`

### Top-level: RequestVINVerificationOutput

**`RequestVINVerificationOutput`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `VinVerificationRequestID` | `integer (int32)` |  |  |
| `Message` | `string` |  |  |


## See also

Related endpoints in **Invitations & Verification**:

- [EmailPacketInvitation](./email-packet-invitation.md)
- [CompletedPackets](./completed-packets.md)
- [RequestUserVerification](./request-user-verification.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
