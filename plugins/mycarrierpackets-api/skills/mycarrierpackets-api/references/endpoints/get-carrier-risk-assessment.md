# GetCarrierRiskAssessment

`POST /api/v1/Carrier/GetCarrierRiskAssessment`

Returns carrier's risk assessment with provided DOT number and Docket number.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `dotNumber` | `integer (int32)` |  | DOT number of the carrier. Example: 12345 |
| `docketNumber` | `string` |  | Docket number of the carrier. Example: MC010203. Optional |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `Array[CarrierRiskAssessmentDTO]`

### Top-level: CarrierRiskAssessmentDTO

**`CarrierRiskAssessmentDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `RiskAssessmentDetails` | `RiskAssessmentDetails` |  |  |


### Nested model: RiskAssessmentDetail

**`RiskAssessmentDetail`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `TotalPoints` | `integer (int32)` |  |  |
| `OverallRating` | `string` |  |  |
| `HasRuleOverride` | `boolean` |  |  |
| `Infractions` | `Array[RiskAssessmentInfraction]` |  |  |


### Nested model: RiskAssessmentDetails

**`RiskAssessmentDetails`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `IsIntrastateCarrier` | `boolean` |  |  |
| `TotalPoints` | `integer (int32)` |  |  |
| `OverallRating` | `string` |  |  |
| `ReviewState` | `string` |  |  |
| `Authority` | `RiskAssessmentDetail` |  |  |
| `Insurance` | `RiskAssessmentDetail` |  |  |
| `Safety` | `RiskAssessmentDetail` |  |  |
| `Operation` | `RiskAssessmentDetail` |  |  |
| `Other` | `RiskAssessmentDetail` |  |  |
| `ReviewDetails` | `ReviewDetails` |  |  |


### Nested model: RiskAssessmentInfraction

**`RiskAssessmentInfraction`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Points` | `integer (int32)` |  |  |
| `RuleName` | `string` |  |  |
| `RiskLevel` | `string` |  |  |
| `RuleText` | `string` |  |  |
| `RuleOutput` | `string` |  |  |
| `PreReviewScore` | `integer (int32)` |  |  |
| `PreReviewRiskLevel` | `string` |  |  |
| `RuleEnforced` | `boolean` |  |  |


### Nested model: ReviewDetails

**`ReviewDetails`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `ReviewID` | `integer (int32)` |  |  |
| `PreReviewOverall` | `string` |  |  |
| `PreReviewAuthority` | `string` |  |  |
| `PreReviewInsurance` | `string` |  |  |
| `PreReviewSafety` | `string` |  |  |
| `PreReviewOperation` | `string` |  |  |
| `PreReviewOther` | `string` |  |  |
| `ReviewUser` | `string` |  |  |
| `ReviewDate` | `string (date-time)` |  |  |
| `ReviewReason` | `string` |  |  |
| `ReviewNote` | `string` |  |  |
| `ReviewExpirationDate` | `string (date-time)` |  |  |


## See also

Related endpoints in **Carrier Data**:

- [PreviewCarrier](./preview-carrier.md)
- [GetCarrierData](./get-carrier-data.md)
- [GetCarrierContacts](./get-carrier-contacts.md)
- [GetCarrierIncidentReports](./get-carrier-incident-reports.md)
- [GetCarrierVINVerifications](./get-carrier-vin-verifications.md)
- [FindAssociatedCarriers](./find-associated-carriers.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
