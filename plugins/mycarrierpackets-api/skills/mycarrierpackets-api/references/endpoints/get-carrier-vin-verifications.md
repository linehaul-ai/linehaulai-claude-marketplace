# GetCarrierVINVerifications

`POST /api/v1/Carrier/GetCarrierVINVerifications`

Retrieves Carrier VIN Verification status details.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  | DOT number of the carrier.For example: 12345 |
| `docketNumber` | `string` |  | Docket number of the carrier. Example: MC12345 |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `CarrierVINVerificationDTO`

### Top-level: CarrierVINVerificationDTO

**`CarrierVINVerificationDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `LegalName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `VINVerifications` | `Array[CarrierVINVerificationDetailDTO]` |  |  |


### Nested model: CarrierVINVerificationDetailDTO

**`CarrierVINVerificationDetailDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `VIN` | `string` |  |  |
| `VINVerificationStatus` | `VINVerificationStatusDTO` |  |  |
| `CreatedOnUtc` | `string (date-time)` |  |  |
| `ModifiedOnUtc` | `string (date-time)` |  |  |
| `OtherCarrier` | `CarrierVINVerificationDetailOtherCarrierDTO` |  |  |
| `Requests` | `Array[CarrierVINVerificationRequestDTO]` |  |  |


### Nested model: CarrierVINVerificationDetailOtherCarrierDTO

**`CarrierVINVerificationDetailOtherCarrierDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `CompanyName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `Street` | `string` |  |  |
| `City` | `string` |  |  |
| `StateProvince` | `string` |  |  |
| `Zipcode` | `string` |  |  |
| `Country` | `string` |  |  |
| `Phone` | `string` |  |  |


### Nested model: CarrierVINVerificationRequestDTO

**`CarrierVINVerificationRequestDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `RequestSentTo` | `string` |  |  |
| `RequestedByUser` | `string` |  |  |
| `RequestedDateTime` | `string (date-time)` |  |  |
| `ImageUploadedByFirstName` | `string` |  |  |
| `ImageUploadedByLastName` | `string` |  |  |
| `ImageUploadedFromIPAddress` | `string` |  |  |
| `ImageUploadedDateTime` | `string (date-time)` |  |  |
| `ImageFileName` | `string` |  |  |
| `ImageBlobName` | `string` |  |  |
| `VIN` | `string` |  |  |
| `VINVerificationStatus` | `VINVerificationStatusDTO` |  |  |
| `OtherCarrier` | `CarrierVINVerificationDetailOtherCarrierDTO` |  |  |


### Nested model: VINVerificationStatusDTO

**`VINVerificationStatusDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `StatusID` | `integer (int32)` |  |  |
| `Description` | `string` |  |  |


## See also

Related endpoints in **Carrier Data**:

- [PreviewCarrier](./preview-carrier.md)
- [GetCarrierData](./get-carrier-data.md)
- [GetCarrierContacts](./get-carrier-contacts.md)
- [GetCarrierRiskAssessment](./get-carrier-risk-assessment.md)
- [GetCarrierIncidentReports](./get-carrier-incident-reports.md)
- [FindAssociatedCarriers](./find-associated-carriers.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
