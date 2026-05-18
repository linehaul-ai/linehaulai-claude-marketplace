# GetCarrierContacts

`POST /api/v1/Carrier/GetCarrierContacts`

Retrieves a list of authorized and verified users for a carrier.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  | DOT number of the carrier. For example: 12345 |
| `docketNumber` | `string` |  | Docket number of the carrier. Example: MC12345 |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `Array[GetCarrierContactsResponse]`

### Top-level: GetCarrierContactsResponse

**`GetCarrierContactsResponse`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Success` | `boolean` |  |  |
| `Message` | `string` |  |  |
| `Carrier` | `Carrier` |  |  |


### Nested model: Carrier

**`Carrier`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `LegalName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `Contacts` | `Array[CarrierContact]` |  |  |


### Nested model: CarrierContact

**`CarrierContact`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `FirstName` | `string` |  |  |
| `LastName` | `string` |  |  |
| `Title` | `string` |  |  |
| `Phone` | `string` |  |  |
| `Email` | `string` |  |  |
| `AuthorizedForPackets` | `boolean` |  |  |
| `VerificationStatus` | `string` |  |  |


## See also

Related endpoints in **Carrier Data**:

- [PreviewCarrier](./preview-carrier.md)
- [GetCarrierData](./get-carrier-data.md)
- [GetCarrierRiskAssessment](./get-carrier-risk-assessment.md)
- [GetCarrierIncidentReports](./get-carrier-incident-reports.md)
- [GetCarrierVINVerifications](./get-carrier-vin-verifications.md)
- [FindAssociatedCarriers](./find-associated-carriers.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
