# CarriersChanges

`POST /api/v1/Carrier/CarriersChanges`

Monitors changes to carrier insurance, risk assessment, and other important details.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `fromDate` | `string (date-time)` | yes | From Date. Required parameter. Example: 2021-07-01T01:00:00 |
| `toDate` | `string (date-time)` | yes | To Date. Required parameter. Example: 2021-07-01T23:00:00 |
| `pageNumber` | `integer (int32)` |  | The current page number. |
| `pageSize` | `integer (int32)` |  | The number of carriers returned per page. The recommended and default value is 250. The max is 500. |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

> **Pagination:** returned in `X-Pagination` response header as JSON: `{pageNumber, pageSize, totalPages, totalCount}`.

## Response (200)

**Returns:** `CarrierChangesResultDTO`

### Top-level: CarrierChangesResultDTO

**`CarrierChangesResultDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `FromDate` | `string (date-time)` |  |  |
| `ToDate` | `string (date-time)` |  |  |
| `RequestDateTimeUtc` | `string (date-time)` |  |  |
| `InsuranceChangeCount` | `integer (int32)` |  |  |
| `FMCSAChangeCount` | `integer (int32)` |  |  |
| `RiskAssessmentChangeCount` | `integer (int32)` |  |  |
| `CarrierCount` | `integer (int32)` |  |  |
| `CarrierList` | `Array[FMCSACarrierChanged]` |  |  |


### Nested model: CertificateDTO

**`CertificateDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `certificateID` | `string` |  |  |
| `producerName` | `string` |  |  |
| `producerAddress` | `string` |  |  |
| `producerCity` | `string` |  |  |
| `producerState` | `string` |  |  |
| `producerZip` | `string` |  |  |
| `producerPhone` | `string` |  |  |
| `producerFax` | `string` |  |  |
| `producerEmail` | `string` |  |  |
| `paidFor` | `string` |  |  |
| `BlobName` | `string` |  |  |
| `Coverage` | `Array[CoverageDTO]` |  |  |


### Nested model: CoverageDTO

**`CoverageDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `insurerName` | `string` |  |  |
| `insurerAMBestRating` | `string` |  |  |
| `type` | `string` |  |  |
| `policyNumber` | `string` |  |  |
| `expirationDate` | `string` |  |  |
| `coverageLimit` | `string` |  |  |
| `deductable` | `string` |  |  |
| `referBreakdown` | `string` |  |  |
| `referBreakDeduct` | `string` |  |  |
| `cancellationDate` | `string` |  |  |


### Nested model: PolicyOutput

**`PolicyOutput`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `companyName` | `string` |  |  |
| `attnToName` | `string` |  |  |
| `address` | `string` |  |  |
| `city` | `string` |  |  |
| `stateCode` | `string` |  |  |
| `postalCode` | `string` |  |  |
| `countryCode` | `string` |  |  |
| `phone` | `string` |  |  |
| `fax` | `string` |  |  |
| `insuranceType` | `string` |  |  |
| `policyNumber` | `string` |  |  |
| `postedDate` | `string` |  |  |
| `effectiveDate` | `string` |  |  |
| `cancelationDate` | `string` |  |  |
| `coverageFrom` | `string` |  |  |
| `coverageTo` | `string` |  |  |
| `amBestRating` | `string` |  |  |


### Nested model: ResponseDO

**`ResponseDO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `status` | `string` |  |  |
| `action` | `string` |  |  |
| `code` | `string` |  |  |
| `displayMsg` | `string` |  |  |
| `techMsg` | `string` |  |  |


### Nested model: Authority

**`Authority`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `authGrantDate` | `string` |  |  |
| `commonAuthority` | `string` |  |  |
| `commonAuthorityPending` | `string` |  |  |
| `commonAuthorityRevocation` | `string` |  |  |
| `contractAuthority` | `string` |  |  |
| `contractAuthorityPending` | `string` |  |  |
| `contractAuthorityRevocation` | `string` |  |  |
| `brokerAuthority` | `string` |  |  |
| `brokerAuthorityPending` | `string` |  |  |
| `brokerAuthorityRevocation` | `string` |  |  |
| `freight` | `string` |  |  |
| `passenger` | `string` |  |  |
| `householdGoods` | `string` |  |  |
| `private` | `string` |  |  |
| `enterprise` | `string` |  |  |


### Nested model: Cargo

**`Cargo`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `hazmatIndicator` | `string` |  |  |
| `cargoGenFreight` | `string` |  |  |
| `cargoHousehold` | `string` |  |  |
| `cargoMetal` | `string` |  |  |
| `cargoMotorVeh` | `string` |  |  |
| `cargoDriveTow` | `string` |  |  |
| `cargoLogPole` | `string` |  |  |
| `cargoBldgMaterial` | `string` |  |  |
| `cargoMobileHome` | `string` |  |  |
| `cargoMachLarge` | `string` |  |  |
| `cargoProduce` | `string` |  |  |
| `cargoLiqGas` | `string` |  |  |
| `cargoIntermodal` | `string` |  |  |
| `cargoPassengers` | `string` |  |  |
| `cargoOilfield` | `string` |  |  |
| `cargoLivestock` | `string` |  |  |
| `cargoGrainfeed` | `string` |  |  |
| `cargoCoalcoke` | `string` |  |  |
| `cargoMeat` | `string` |  |  |
| `cargoGarbage` | `string` |  |  |
| `cargoUSMail` | `string` |  |  |
| `cargoChemicals` | `string` |  |  |
| `cargoDryBulk` | `string` |  |  |
| `cargoRefrigerated` | `string` |  |  |
| `cargoBeverages` | `string` |  |  |
| `cargoPaperProd` | `string` |  |  |
| `cargoUtilities` | `string` |  |  |
| `cargoFarmSupplies` | `string` |  |  |
| `cargoConstruction` | `string` |  |  |
| `cargoWaterwell` | `string` |  |  |
| `cargoOther` | `string` |  |  |
| `cargoOtherDesc` | `string` |  |  |


### Nested model: CarrierDetails

**`CarrierDetails`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `docketNumber` | `string` |  |  |
| `dotNumber` | `DotNumber` |  |  |
| `carrierType` | `string` |  |  |
| `isMonitored` | `boolean` |  |  |
| `isBlocked` | `boolean` |  |  |
| `Identity` | `Identity` |  |  |
| `Authority` | `Authority` |  |  |
| `FMCSAInsurance` | `FMCSAInsurance` |  |  |
| `CertData` | `CertData` |  |  |
| `Safety` | `Safety` |  |  |
| `Inspection` | `Inspection` |  |  |
| `Crash` | `Crash` |  |  |
| `Review` | `Review` |  |  |
| `Operation` | `Operation` |  |  |
| `Cargo` | `Cargo` |  |  |
| `Drivers` | `Drivers` |  |  |
| `Equipment` | `Equipment` |  |  |
| `Other` | `Other` |  |  |
| `RiskAssessment` | `RiskAssessment` |  |  |
| `RiskAssessmentDetails` | `RiskAssessmentDetails` |  |  |
| `CarrierRatings` | `CarrierRatings` |  |  |
| `LatestInvitation` | `LatestInvitation` |  |  |
| `IncidentReports` | `IncidentReports` |  |  |


### Nested model: CarrierRatings

**`CarrierRatings`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `myRating` | `integer (int32)` |  |  |
| `totalRatings` | `integer (int32)` |  |  |
| `lowRatings` | `integer (int32)` |  |  |
| `avgRating` | `number (double)` |  |  |


### Nested model: CertData

**`CertData`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `status` | `string` |  |  |
| `noncoop` | `boolean` |  |  |
| `Certificate` | `Array[CertificateDTO]` |  |  |


### Nested model: Crash

**`Crash`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `crashFatalUS` | `string` |  |  |
| `crashInjuryUS` | `string` |  |  |
| `crashTowUS` | `string` |  |  |
| `crashTotalUS` | `string` |  |  |
| `crashFatalCAN` | `string` |  |  |
| `crashInjuryCAN` | `string` |  |  |
| `crashTowCAN` | `string` |  |  |
| `crashTotalCAN` | `string` |  |  |


### Nested model: DotNumber

**`DotNumber`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `status` | `string` |  |  |
| `Value` | `string` |  |  |


### Nested model: Drivers

**`Drivers`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `driversTotal` | `string` |  |  |
| `driversAvgLeased` | `string` |  |  |
| `driversCDL` | `string` |  |  |
| `driversInter` | `string` |  |  |
| `driversInterLT100` | `string` |  |  |
| `driversInterGT100` | `string` |  |  |
| `driversIntra` | `string` |  |  |
| `driversIntraLT100` | `string` |  |  |
| `driversIntraGT100` | `string` |  |  |


### Nested model: Equipment

**`Equipment`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `trucksTotal` | `string` |  |  |
| `totalPower` | `string` |  |  |
| `fleetsize` | `string` |  |  |
| `trucksOwned` | `string` |  |  |
| `trucksTerm` | `string` |  |  |
| `trucksTrip` | `string` |  |  |
| `trailersOwned` | `string` |  |  |
| `trailersTerm` | `string` |  |  |
| `trailersTrip` | `string` |  |  |
| `tractorsOwned` | `string` |  |  |
| `tractorsTerm` | `string` |  |  |
| `tractorsTrip` | `string` |  |  |


### Nested model: FMCSACarrierChanged

**`FMCSACarrierChanged`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `ChangeDateTime` | `string (date-time)` |  |  |
| `ChangeCategories` | `Array[string]` |  |  |
| `CarrierDetails` | `CarrierDetails` |  |  |
| `ResponseDO` | `ResponseDO` |  |  |


### Nested model: FMCSAInsurance

**`FMCSAInsurance`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `bipdRequired` | `string` |  |  |
| `bipdOnFile` | `string` |  |  |
| `cargoRequired` | `string` |  |  |
| `cargoOnFile` | `string` |  |  |
| `bondSuretyRequired` | `string` |  |  |
| `bondSuretyOnFile` | `string` |  |  |
| `PolicyList` | `Array[PolicyOutput]` |  |  |


### Nested model: Identity

**`Identity`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `legalName` | `string` |  |  |
| `dbaName` | `string` |  |  |
| `businessStreet` | `string` |  |  |
| `businessCity` | `string` |  |  |
| `businessState` | `string` |  |  |
| `businessZipCode` | `string` |  |  |
| `businessColonia` | `string` |  |  |
| `businessCountry` | `string` |  |  |
| `businessPhone` | `string` |  |  |
| `businessFax` | `string` |  |  |
| `mailingStreet` | `string` |  |  |
| `mailingCity` | `string` |  |  |
| `mailingState` | `string` |  |  |
| `mailingZipCode` | `string` |  |  |
| `mailingColonia` | `string` |  |  |
| `mailingCountry` | `string` |  |  |
| `mailingPhone` | `string` |  |  |
| `mailingFax` | `string` |  |  |
| `undeliverableMail` | `string` |  |  |
| `companyRep1` | `string` |  |  |
| `companyRep2` | `string` |  |  |
| `cellPhone` | `string` |  |  |
| `emailAddress` | `string` |  |  |
| `dunBradstreetNum` | `string` |  |  |
| `organization` | `string` |  |  |


### Nested model: IncidentReports

**`IncidentReports`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `TotalIncidentReports` | `integer (int32)` |  |  |
| `TotalIncidentReportsWithFraud` | `integer (int32)` |  |  |


### Nested model: Inspection

**`Inspection`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `inspectVehUS` | `string` |  |  |
| `inspectVehOOSUS` | `string` |  |  |
| `inspectVehOOSPctUS` | `string` |  |  |
| `inspectDrvUS` | `string` |  |  |
| `inspectDrvOOSUS` | `string` |  |  |
| `inspectDrvOOSPctUS` | `string` |  |  |
| `inspectHazUS` | `string` |  |  |
| `inspectHazOOSUS` | `string` |  |  |
| `inspectHazOOSPctUS` | `string` |  |  |
| `inspectIEPUS` | `string` |  |  |
| `inspectIEPOOSUS` | `string` |  |  |
| `inspectIEPOOSPctUS` | `string` |  |  |
| `inspectTotalIEPUS` | `string` |  |  |
| `inspectTotalUS` | `string` |  |  |
| `inspectVehCAN` | `string` |  |  |
| `inspectVehOOSCAN` | `string` |  |  |
| `inspectVehOOSPctCAN` | `string` |  |  |
| `inspectDrvCAN` | `string` |  |  |
| `inspectDrvOOSCAN` | `string` |  |  |
| `inspectDrvOOSPctCAN` | `string` |  |  |
| `inspectTotalCAN` | `string` |  |  |


### Nested model: LatestInvitation

**`LatestInvitation`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `InvitedByUserName` | `string` |  |  |
| `InvitedByEmail` | `string` |  |  |
| `InvitedByFirstName` | `string` |  |  |
| `InvitedByLastName` | `string` |  |  |
| `InvitationSentDate` | `string (date-time)` |  |  |
| `InvitationRecipient` | `string` |  |  |


### Nested model: Operation

**`Operation`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `dotAddDate` | `string` |  |  |
| `carrierOperation` | `string` |  |  |
| `shipperOperation` | `string` |  |  |
| `mxOperationType` | `string` |  |  |
| `mxRFCNumber` | `string` |  |  |
| `outOfService` | `string` |  |  |
| `outOfServiceDate` | `string` |  |  |
| `outOfServiceReason` | `string` |  |  |
| `entityCarrier` | `string` |  |  |
| `entityShipper` | `string` |  |  |
| `entityBroker` | `string` |  |  |
| `entityFreightFowarder` | `string` |  |  |
| `entityCargoTank` | `string` |  |  |
| `classAuthForHire` | `string` |  |  |
| `classMigrant` | `string` |  |  |
| `classIndianNation` | `string` |  |  |
| `classExemptForHire` | `string` |  |  |
| `classUSMail` | `string` |  |  |
| `classPrivateProperty` | `string` |  |  |
| `classFederalGovernment` | `string` |  |  |
| `classPrivPassBusiness` | `string` |  |  |
| `classStateGovernment` | `string` |  |  |
| `classPrivPassNonBusiness` | `string` |  |  |
| `classLocalGovernment` | `string` |  |  |
| `classOther` | `string` |  |  |
| `operatingStatus` | `string` |  |  |


### Nested model: Other

**`Other`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `carbTru` | `string` |  |  |
| `smartway` | `string` |  |  |
| `watchdogReports` | `string` |  |  |


### Nested model: Review

**`Review`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `reviewType` | `string` |  |  |
| `reviewDate` | `string` |  |  |
| `reviewDocNum` | `string` |  |  |
| `reviewMiles` | `string` |  |  |
| `mcs150Date` | `string` |  |  |
| `mcs150MileYear` | `string` |  |  |
| `mcs150Miles` | `string` |  |  |
| `accidentRate` | `string` |  |  |
| `accidentRatePrevent` | `string` |  |  |


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


### Nested model: Safety

**`Safety`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `rating` | `string` |  |  |
| `ratingDate` | `string` |  |  |
| `unsafeDrvPCT` | `string` |  |  |
| `unsafeDrvOT` | `string` |  |  |
| `unsafeDrvSV` | `string` |  |  |
| `unsafeDrvAlert` | `string` |  |  |
| `unsafeDrvTrend` | `string` |  |  |
| `unsafeDrvCNT` | `integer (int32)` |  |  |
| `hosPCT` | `string` |  |  |
| `hosOT` | `string` |  |  |
| `hosSV` | `string` |  |  |
| `hosAlert` | `string` |  |  |
| `hosTrend` | `string` |  |  |
| `hosCNT` | `integer (int32)` |  |  |
| `drvFitPCT` | `string` |  |  |
| `drvFitOT` | `string` |  |  |
| `drvFitSV` | `string` |  |  |
| `drvFitAlert` | `string` |  |  |
| `drvFitTrend` | `string` |  |  |
| `drvFitCNT` | `integer (int32)` |  |  |
| `controlSubPCT` | `string` |  |  |
| `controlSubOT` | `string` |  |  |
| `controlSubSV` | `string` |  |  |
| `controlSubAlert` | `string` |  |  |
| `controlSubTrend` | `string` |  |  |
| `controlSubCNT` | `integer (int32)` |  |  |
| `vehMaintPCT` | `string` |  |  |
| `vehMaintOT` | `string` |  |  |
| `vehMaintSV` | `string` |  |  |
| `vehMaintAlert` | `string` |  |  |
| `vehMaintTrend` | `string` |  |  |
| `vehMaintCNT` | `integer (int32)` |  |  |
| `hazMatPCT` | `string` |  |  |
| `hazMatOT` | `string` |  |  |
| `hazMatSV` | `string` |  |  |
| `hazMatAlert` | `string` |  |  |
| `hazMatTrend` | `string` |  |  |
| `hazMatCNT` | `integer (int32)` |  |  |


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
- [GetMonitoredCarriersRiskAssessment](./get-monitored-carriers-risk-assessment.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
