# GetMonitoredCarriersRiskAssessment

`POST /api/v1/Carrier/GetMonitoredCarriersRiskAssessment`

Returns all monitored carrier risk assessments in bulk. Includes paging.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `pageNumber` | `integer (int32)` |  | Default: 1 |
| `pageSize` | `integer (int32)` |  | Default: 250. If set to more than 500, or less than 1, the default value will be used. |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `MonitoredCarriersRiskAssessmentDTO`

### Top-level: MonitoredCarriersRiskAssessmentDTO

**`MonitoredCarriersRiskAssessmentDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `pageNumber` | `integer (int32)` |  |  |
| `pageSize` | `integer (int32)` |  |  |
| `totalPages` | `integer (int32)` |  |  |
| `totalCount` | `integer (int32)` |  |  |
| `succeeded` | `boolean` |  |  |
| `message` | `string` |  |  |
| `data` | `Array[CarrierRiskAssessmentDTO]` |  |  |


### Nested model: CarrierRiskAssessmentDTO

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

Related endpoints in **Monitoring**:

- [RequestMonitoring](./request-monitoring.md)
- [CancelMonitoring](./cancel-monitoring.md)
- [MonitoredCarriers](./monitored-carriers.md)
- [MonitoredCarrierData](./monitored-carrier-data.md)
- [GetMonitoredCarrierContactsData](./get-monitored-carrier-contacts-data.md)
- [CarriersChanges](./carriers-changes.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
