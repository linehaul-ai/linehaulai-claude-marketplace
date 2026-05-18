# GetCarrierIncidentReports

`POST /api/v1/Carrier/GetCarrierIncidentReports`

Retrieves incident report details for a given carrier.

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

**Returns:** `CarrierIncidentReportDTO`

### Top-level: CarrierIncidentReportDTO

**`CarrierIncidentReportDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `LegalName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `IncidentReports` | `Array[CarrierIncidentReportDetailDTO]` |  |  |


### Nested model: CarrierIncidentReportCommentDTO

**`CarrierIncidentReportCommentDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `CommenterType` | `string` |  |  |
| `CommentBy` | `string` |  |  |
| `CommentDate` | `string (date-time)` |  |  |
| `Comment` | `string` |  |  |


### Nested model: CarrierIncidentReportDetailDTO

**`CarrierIncidentReportDetailDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `IncidentDate` | `string` |  |  |
| `OriginCity` | `string` |  |  |
| `OriginStateProvinceName` | `string` |  |  |
| `OriginCountryName` | `string` |  |  |
| `DestinationCity` | `string` |  |  |
| `DestinationStateProvinceName` | `string` |  |  |
| `DestinationCountryName` | `string` |  |  |
| `ReportedByCompany` | `string` |  |  |
| `CarrierEmails` | `string` |  |  |
| `CreatedBy` | `string` |  |  |
| `CreatedDate` | `string (date-time)` |  |  |
| `ModifiedBy` | `string` |  |  |
| `ModifiedDate` | `string (date-time)` |  |  |
| `IncidentTypes` | `Array[string]` |  |  |
| `Comments` | `Array[CarrierIncidentReportCommentDTO]` |  |  |


## See also

Related endpoints in **Carrier Data**:

- [PreviewCarrier](./preview-carrier.md)
- [GetCarrierData](./get-carrier-data.md)
- [GetCarrierContacts](./get-carrier-contacts.md)
- [GetCarrierRiskAssessment](./get-carrier-risk-assessment.md)
- [GetCarrierVINVerifications](./get-carrier-vin-verifications.md)
- [FindAssociatedCarriers](./find-associated-carriers.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
