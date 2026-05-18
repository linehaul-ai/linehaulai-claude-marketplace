# PreviewCarrier

`POST /api/v1/Carrier/PreviewCarrier`

Retrieves carrier profile data, risk assessment, certdata. **Excludes** carrier packet data.

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

**Returns:** `Array[PreviewCarrier]`

### Top-level: PreviewCarrier

**`PreviewCarrier`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `CarrierID` | `integer (int32)` |  |  |
| `DotNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `CompanyName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `Street` | `string` |  |  |
| `City` | `string` |  |  |
| `State` | `string` |  |  |
| `ZipCode` | `string` |  |  |
| `Country` | `string` |  |  |
| `Phone` | `string` |  |  |
| `Status` | `string` |  |  |
| `StatusDate` | `string (date-time)` |  |  |
| `InProcessState` | `string` |  |  |
| `PossibleFraud` | `string` |  |  |
| `DoubleBrokering` | `string` |  |  |
| `IncidentReports` | `IncidentReports` |  |  |
| `FraudCallNumber` | `string` |  |  |
| `HasSaferWatchKey` | `boolean` |  |  |
| `WatchdogReports` | `string` |  |  |
| `OnCurrentCustomerAgreement` | `boolean` |  |  |
| `CarrierRating` | `CarrierRating` |  |  |
| `RiskAssessment` | `RiskAssessment` |  |  |
| `RiskAssessmentDetails` | `RiskAssessmentDetails` |  |  |
| `CertData` | `CertData` |  |  |
| `Emails` | `Array[CarrierEmail]` |  |  |
| `Source` | `integer (int32)` |  | Value/Type List: 0 = Unknown, 1 = ThirdParty, 2 = MyCarrierPackets, 3 = FMCSAData; Value Only List: (enum: [0, 1, 2, 3]) |
| `IsIntrastateCarrier` | `boolean` |  |  |
| `IsMonitored` | `boolean` |  |  |
| `IsBlocked` | `boolean` |  |  |
| `FreightValidateStatus` | `string` |  |  |


### Nested model: CarrierRating

**`CarrierRating`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `CarrierID` | `integer (int32)` |  |  |
| `CustomerID` | `integer (int32)` |  |  |
| `CustomerRating` | `integer (int32)` |  |  |
| `RatingSum` | `integer (int32)` |  |  |
| `TotalRatings` | `integer (int32)` |  |  |
| `LowRatings` | `integer (int32)` |  |  |
| `TotalRatingPercent` | `integer (int32)` |  |  |
| `CustomerRatingPercent` | `integer (int32)` |  |  |
| `RatingValue` | `number (double)` |  |  |
| `RatingValueText` | `string` |  |  |
| `AvgRatingText` | `string` |  |  |
| `AvgRatingBasisText` | `string` |  |  |
| `AvgRatingTextPlusRatingBasisText` | `string` |  |  |
| `CustomerRatingText` | `string` |  |  |
| `HasCompletedPacket` | `boolean` |  |  |


### Nested model: CarrierEmail

**`CarrierEmail`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `EmailType` | `integer (int32)` |  | Value/Type List: 1 = McpEmail, 2 = CompanyEmail, 3 = FMCSAEmail; Value Only List: (enum: [1, 2, 3]) |
| `Description` | `string` |  |  |
| `Email` | `string` |  |  |


### Nested model: CertData

**`CertData`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Status` | `string` |  |  |
| `Noncoop` | `boolean` |  |  |
| `Certificates` | `Array[Certificate]` |  |  |


### Nested model: Certificate

**`Certificate`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `CertificateID` | `string` |  |  |
| `ProducerName` | `string` |  |  |
| `ProducerAddress` | `string` |  |  |
| `ProducerCity` | `string` |  |  |
| `ProducerState` | `string` |  |  |
| `ProducerZip` | `string` |  |  |
| `ProducerPhone` | `string` |  |  |
| `ProducerFax` | `string` |  |  |
| `ProducerEmail` | `string` |  |  |
| `PaidFor` | `string` |  |  |
| `Coverages` | `Array[Coverage]` |  |  |


### Nested model: Coverage

**`Coverage`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `InsurerName` | `string` |  |  |
| `Type` | `string` |  |  |
| `PolicyNumber` | `string` |  |  |
| `ExpirationDate` | `string` |  |  |
| `CoverageLimit` | `string` |  |  |
| `Deductible` | `string` |  |  |
| `ReferBreakdown` | `string` |  |  |
| `ReferBreakDeduct` | `string` |  |  |
| `CancellationDate` | `string` |  |  |


### Nested model: IncidentReports

**`IncidentReports`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `TotalIncidentReports` | `integer (int32)` |  |  |
| `TotalIncidentReportsWithFraud` | `integer (int32)` |  |  |


### Nested model: RiskAssessment

**`RiskAssessment`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Overall` | `string` |  |  |
| `Authority` | `string` |  |  |
| `Insurance` | `string` |  |  |
| `Safety` | `string` |  |  |
| `Operation` | `string` |  |  |
| `Other` | `string` |  |  |


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
| `Authority` | `RiskAssessmentDetail` |  |  |
| `Insurance` | `RiskAssessmentDetail` |  |  |
| `Safety` | `RiskAssessmentDetail` |  |  |
| `Operation` | `RiskAssessmentDetail` |  |  |
| `Other` | `RiskAssessmentDetail` |  |  |
| `ReviewState` | `string` |  |  |
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

- [GetCarrierData](./get-carrier-data.md)
- [GetCarrierContacts](./get-carrier-contacts.md)
- [GetCarrierRiskAssessment](./get-carrier-risk-assessment.md)
- [GetCarrierIncidentReports](./get-carrier-incident-reports.md)
- [GetCarrierVINVerifications](./get-carrier-vin-verifications.md)
- [FindAssociatedCarriers](./find-associated-carriers.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
