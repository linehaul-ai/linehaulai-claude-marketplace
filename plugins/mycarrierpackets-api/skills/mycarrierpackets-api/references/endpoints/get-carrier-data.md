# GetCarrierData

`POST /api/v1/Carrier/GetCarrierData`

Retrieves carrier profile data, risk assessment, certdata. **Includes** carrier packet data.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  | DOT number of the carrier. Example: 12345 |
| `DocketNumber` | `string` |  | Docket number of the carrier. Example: MC12345 |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `CarrierAADTO`

### Top-level: CarrierAADTO

**`CarrierAADTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `LegalName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `Address1` | `string` |  |  |
| `Address2` | `string` |  |  |
| `City` | `string` |  |  |
| `Zipcode` | `string` |  |  |
| `State` | `string` |  |  |
| `Country` | `string` |  |  |
| `CellPhone` | `string` |  |  |
| `Phone` | `string` |  |  |
| `Fax` | `string` |  |  |
| `FreePhone` | `string` |  |  |
| `EmergencyPhone` | `string` |  |  |
| `Email` | `string` |  |  |
| `FraudIdentityTheftStatus` | `string` |  |  |
| `MCNumber` | `string` |  |  |
| `SCAC` | `string` |  |  |
| `MailingAddress1` | `string` |  |  |
| `MailingAddress2` | `string` |  |  |
| `MailingCity` | `string` |  |  |
| `MailingState` | `string` |  |  |
| `MailingZipcode` | `string` |  |  |
| `MailingCountry` | `string` |  |  |
| `AfterHrsWkDaySupportName` | `string` |  |  |
| `AfterHrsWkDaySupportPhone` | `string` |  |  |
| `AfterHrsWkDaySupportFax` | `string` |  |  |
| `AfterHrsWkDaySupportFrom` | `string` |  |  |
| `AfterHrsWkDaySupportTo` | `string` |  |  |
| `AfterHrsWkEndSupportName` | `string` |  |  |
| `AfterHrsWkEndSupportPhone` | `string` |  |  |
| `AfterHrsWkEndSupportFax` | `string` |  |  |
| `AfterHrsWkEndSupportFrom` | `string` |  |  |
| `AfterHrsWkEndSupportTo` | `string` |  |  |
| `Website` | `string` |  |  |
| `OperationManagerName` | `string` |  |  |
| `OnlineAccessToAvailableLoads` | `boolean` |  |  |
| `AvailableLoadsEmail` | `string` |  |  |
| `DriverLogsSafeyDeptManagerName` | `string` |  |  |
| `DriverLogsSafeyDeptManagerPhone` | `string` |  |  |
| `Dispatchers` | `string` |  |  |
| `ClaimsContactName` | `string` |  |  |
| `ClaimsContactPhone` | `string` |  |  |
| `ClaimsContactEmail` | `string` |  |  |
| `DispatchServiceUsed` | `boolean` |  |  |
| `DispatchServiceName` | `string` |  |  |
| `DispatchServicePhone` | `string` |  |  |
| `BrokerOutExtraFreight` | `boolean` |  |  |
| `References1` | `string` |  |  |
| `References2` | `string` |  |  |
| `References3` | `string` |  |  |
| `DriversTrackedBy` | `string` |  |  |
| `AccessOnlineGPSTracking` | `boolean` |  |  |
| `DriversTrackedByOtherMethod` | `string` |  |  |
| `CreatedDateTime` | `string (date-time)` |  |  |
| `ModifiedDateTime` | `string (date-time)` |  |  |
| `CarrierCustomerAgreements` | `Array[CarrierCustomerAgreementDTO]` |  |  |
| `CarrierCustomerPacketStatuses` | `Array[CarrierCustomerPacketStatusDTO]` |  |  |
| `CarrierCargoHauled` | `CarrierCargoHauledDTO` |  |  |
| `CarrierCompanyClassification` | `CarrierCompanyClassificationDTO` |  |  |
| `CarrierDrivers` | `Array[CarrierDriverDTO]` |  |  |
| `CarrierDispatchers` | `Array[CarrierDispatcherDTO]` |  |  |
| `CarrierLane` | `CarrierLaneDTO` |  |  |
| `CarrierOperationalDetail` | `CarrierOperationalDetailDTO` |  |  |
| `CarrierPaymentInfo` | `CarrierPaymentInfoDTO` |  |  |
| `CarrierRemit` | `CarrierRemitDTO` |  |  |
| `FactoringRemit` | `FactoringRemitDTO` |  |  |
| `CarrierBank` | `CarrierBankDTO` |  |  |
| `CarrierPaymentTerms` | `Array[CarrierPaymentTermDTO]` |  |  |
| `CarrierPaymentTypes` | `Array[CarrierPaymentTypeDTO]` |  |  |
| `CarrierPayerType` | `PayerTypeDTO` |  |  |
| `CarrierTruckClass` | `CarrierTruckClassDTO` |  |  |
| `CarrierTruckType` | `CarrierTruckTypeDTO` |  |  |
| `CarrierW9Forms` | `Array[CarrierW9FormDTO]` |  |  |
| `CarrierCertification` | `CarrierCertificationDTO` |  |  |
| `AssureAdvantage` | `Array[FMCSACarrier]` |  |  |
| `CarrierMode` | `CarrierModeDTO` |  |  |
| `CarrierELDProvider` | `CarrierELDProviderDTO` |  |  |
| `OwnerContactName` | `string` |  |  |
| `OwnerContactPhone` | `string` |  |  |
| `OwnerContactEmail` | `string` |  |  |
| `CarrierTINMatchings` | `Array[CarrierTINMatchingDTO]` |  |  |
| `Message` | `string` |  |  |


### Nested model: CarrierBankDTO

**`CarrierBankDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `CarrierBankRoutingNumber` | `string` |  |  |
| `CarrierBankAccountNumber` | `string` |  |  |
| `CarrierBankAccountName` | `string` |  |  |
| `CarrierBankName` | `string` |  |  |
| `CarrierBankAddress` | `string` |  |  |
| `CarrierBankPhone` | `string` |  |  |
| `CarrierBankFax` | `string` |  |  |
| `CarrierBankAccountType` | `string` |  |  |


### Nested model: CarrierCargoHauledDTO

**`CarrierCargoHauledDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `GeneralFreight` | `boolean` |  |  |
| `LiquidsGas` | `boolean` |  |  |
| `Chemicals` | `boolean` |  |  |
| `HouseholdGoods` | `boolean` |  |  |
| `IntermodalContainers` | `boolean` |  |  |
| `CommoditiesDryBulk` | `boolean` |  |  |
| `MetalSheetsCoilsRolls` | `boolean` |  |  |
| `Passengers` | `boolean` |  |  |
| `RefrigeratedFood` | `boolean` |  |  |
| `MotorVehicles` | `boolean` |  |  |
| `OilfieldEquipment` | `boolean` |  |  |
| `Beverages` | `boolean` |  |  |
| `DrivewayTowaway` | `boolean` |  |  |
| `LivestockContainers` | `boolean` |  |  |
| `PaperProducts` | `boolean` |  |  |
| `LogsPolesBeamsLumber` | `boolean` |  |  |
| `GrainFeedHay` | `boolean` |  |  |
| `Utility` | `boolean` |  |  |
| `BuildingMaterials` | `boolean` |  |  |
| `CoalCoke` | `boolean` |  |  |
| `FarmSupplies` | `boolean` |  |  |
| `MobileHomes` | `boolean` |  |  |
| `Meat` | `boolean` |  |  |
| `Construction` | `boolean` |  |  |
| `MachineryLargeObjects` | `boolean` |  |  |
| `GarbageRefuseTrash` | `boolean` |  |  |
| `WaterWell` | `boolean` |  |  |
| `FreshProduce` | `boolean` |  |  |
| `USMail` | `boolean` |  |  |
| `Other` | `string` |  |  |


### Nested model: CarrierCertificationDTO

**`CarrierCertificationDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Hazmat` | `boolean` |  |  |
| `HazmatNumber` | `string` |  |  |
| `SmartWay` | `boolean` |  |  |
| `CARB` | `boolean` |  |  |
| `TWIC` | `boolean` |  |  |
| `CTPATCertified` | `boolean` |  |  |
| `CTPATSVINumber` | `string` |  |  |
| `TankerEndorsed` | `boolean` |  |  |
| `TankerEndorsedNumOfDrivers` | `integer (int32)` |  |  |
| `CBP` | `boolean` |  |  |
| `CBSA` | `boolean` |  |  |
| `ANAM` | `boolean` |  |  |
| `ACE` | `boolean` |  |  |
| `ACI` | `boolean` |  |  |
| `CSA` | `boolean` |  |  |
| `FAST` | `boolean` |  |  |
| `PIP` | `boolean` |  |  |


### Nested model: CarrierCompanyClassificationDTO

**`CarrierCompanyClassificationDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `AuthForHire` | `boolean` |  |  |
| `Migrant` | `boolean` |  |  |
| `IndianNation` | `boolean` |  |  |
| `ExemptForHire` | `boolean` |  |  |
| `USMail` | `boolean` |  |  |
| `PrivateProperty` | `boolean` |  |  |
| `FederalGovernment` | `boolean` |  |  |
| `PrivPassBusiness` | `boolean` |  |  |
| `StateGovernment` | `boolean` |  |  |
| `PrivPassNonBusiness` | `boolean` |  |  |
| `LocalGovernment` | `boolean` |  |  |
| `WOSB` | `boolean` |  |  |
| `VOSB` | `boolean` |  |  |
| `MBE` | `boolean` |  |  |
| `AsianPacificAmerican` | `boolean` |  |  |
| `SubcontinentAmerican` | `boolean` |  |  |
| `NOB` | `boolean` |  |  |
| `HispanicAmerican` | `boolean` |  |  |
| `AfricanAmerican` | `boolean` |  |  |
| `WBE` | `boolean` |  |  |
| `DBE` | `boolean` |  |  |
| `SBA8a` | `boolean` |  |  |
| `EDWOSB` | `boolean` |  |  |
| `SDVOSB` | `boolean` |  |  |
| `HUBZone` | `boolean` |  |  |
| `LGBTQIA` | `boolean` |  |  |
| `Other` | `string` |  |  |


### Nested model: CarrierCustomerAgreementDTO

**`CarrierCustomerAgreementDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `SignatureDate` | `string (date-time)` |  |  |
| `SignaturePerson` | `string` |  |  |
| `SignaturePersonTitle` | `string` |  |  |
| `SignaturePersonUserName` | `string` |  |  |
| `SignaturePersonEmail` | `string` |  |  |
| `SignaturePersonPhoneNumber` | `string` |  |  |
| `OnCurrentCustomerAgreement` | `boolean` |  |  |
| `CustomerAgreement` | `CustomerAgreementDTO` |  |  |
| `CarrierCustomerAgreementImages` | `Array[CarrierCustomerAgreementImageDTO]` |  |  |
| `IsActive` | `boolean` |  |  |
| `IPAddress` | `string` |  |  |
| `GeoLocLat` | `number (double)` |  |  |
| `GeoLocLng` | `number (double)` |  |  |
| `GeoLocMethod` | `string` |  |  |


### Nested model: CarrierCustomerAgreementImageDTO

**`CarrierCustomerAgreementImageDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `BlobName` | `string` |  |  |
| `CreatedDate` | `string (date-time)` |  |  |


### Nested model: CarrierCustomerPacketStatusDTO

**`CarrierCustomerPacketStatusDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Customer` | `CustomerDTO` |  |  |
| `CarrierPacketStatus` | `string` |  |  |
| `CustomerID` | `integer (int32)` |  |  |


### Nested model: CarrierDispatcherDTO

**`CarrierDispatcherDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DispatcherName` | `string` |  |  |
| `PhoneNumber` | `string` |  |  |
| `Email` | `string` |  |  |


### Nested model: CarrierDriverDTO

**`CarrierDriverDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DriverName` | `string` |  |  |
| `CellPhone` | `string` |  |  |
| `ComCheck` | `boolean` |  |  |
| `FuelAdvance` | `boolean` |  |  |


### Nested model: CarrierELDProviderDTO

**`CarrierELDProviderDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `ComplianceStatusID` | `integer (int32)` |  |  |
| `ComplianceStatus` | `string` |  |  |
| `ProviderName` | `string` |  |  |
| `ProviderIdentifier` | `string` |  |  |
| `ExemptionID` | `integer (int32)` |  |  |
| `Exemption` | `string` |  |  |
| `CompliantBy` | `string` |  |  |


### Nested model: CarrierLaneDTO

**`CarrierLaneDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `UnitedStates` | `boolean` |  |  |
| `Mexico` | `boolean` |  |  |
| `Canada` | `boolean` |  |  |
| `NortheastRegion` | `boolean` |  |  |
| `MidwestRegion` | `boolean` |  |  |
| `SouthRegion` | `boolean` |  |  |
| `WestRegion` | `boolean` |  |  |
| `Alabama` | `boolean` |  |  |
| `Alaska` | `boolean` |  |  |
| `Arizona` | `boolean` |  |  |
| `Arkansas` | `boolean` |  |  |
| `California` | `boolean` |  |  |
| `Colorado` | `boolean` |  |  |
| `Delaware` | `boolean` |  |  |
| `Florida` | `boolean` |  |  |
| `Georgia` | `boolean` |  |  |
| `Hawaii` | `boolean` |  |  |
| `Idaho` | `boolean` |  |  |
| `Illinois` | `boolean` |  |  |
| `Indiana` | `boolean` |  |  |
| `Iowa` | `boolean` |  |  |
| `Kansas` | `boolean` |  |  |
| `Kentucky` | `boolean` |  |  |
| `Louisiana` | `boolean` |  |  |
| `Maine` | `boolean` |  |  |
| `Maryland` | `boolean` |  |  |
| `Massachusetts` | `boolean` |  |  |
| `Michigan` | `boolean` |  |  |
| `Minnesota` | `boolean` |  |  |
| `Mississippi` | `boolean` |  |  |
| `Missouri` | `boolean` |  |  |
| `Montana` | `boolean` |  |  |
| `Nebraska` | `boolean` |  |  |
| `Nevada` | `boolean` |  |  |
| `NewHampshire` | `boolean` |  |  |
| `NewJersey` | `boolean` |  |  |
| `NewMexico` | `boolean` |  |  |
| `NewYork` | `boolean` |  |  |
| `NorthCarolina` | `boolean` |  |  |
| `NorthDakota` | `boolean` |  |  |
| `Ohio` | `boolean` |  |  |
| `Oklahoma` | `boolean` |  |  |
| `Oregon` | `boolean` |  |  |
| `Pennsylvania` | `boolean` |  |  |
| `RhodeIsland` | `boolean` |  |  |
| `SouthCarolina` | `boolean` |  |  |
| `SouthDakota` | `boolean` |  |  |
| `Tennessee` | `boolean` |  |  |
| `Utah` | `boolean` |  |  |
| `Vermont` | `boolean` |  |  |
| `Virginia` | `boolean` |  |  |
| `Washington` | `boolean` |  |  |
| `WashingtonDC` | `boolean` |  |  |
| `WestVirginia` | `boolean` |  |  |
| `Wisconsin` | `boolean` |  |  |
| `Wyoming` | `boolean` |  |  |
| `Connecticut` | `boolean` |  |  |
| `Texas` | `boolean` |  |  |
| `Alberta` | `boolean` |  |  |
| `BritishColumbia` | `boolean` |  |  |
| `Manitoba` | `boolean` |  |  |
| `NewBrunswick` | `boolean` |  |  |
| `NewfoundlandAndLabrador` | `boolean` |  |  |
| `NorthwestTerritories` | `boolean` |  |  |
| `NovaScotia` | `boolean` |  |  |
| `Nunavut` | `boolean` |  |  |
| `Ontario` | `boolean` |  |  |
| `PrinceEdwardIsland` | `boolean` |  |  |
| `Quebec` | `boolean` |  |  |
| `Saskatchewan` | `boolean` |  |  |
| `YukonTerritory` | `boolean` |  |  |
| `Aguascalientes` | `boolean` |  |  |
| `BajaCalifornia` | `boolean` |  |  |
| `BajaCaliforniaNorte` | `boolean` |  |  |
| `BajaCaliforniaSur` | `boolean` |  |  |
| `Chihuahua` | `boolean` |  |  |
| `Colima` | `boolean` |  |  |
| `Campeche` | `boolean` |  |  |
| `Coahuila` | `boolean` |  |  |
| `Chiapas` | `boolean` |  |  |
| `Durango` | `boolean` |  |  |
| `Guerrero` | `boolean` |  |  |
| `Guanajuato` | `boolean` |  |  |
| `Hidalgo` | `boolean` |  |  |
| `Jalisco` | `boolean` |  |  |
| `MexicoCity` | `boolean` |  |  |
| `MexicoState` | `boolean` |  |  |
| `Michoacan` | `boolean` |  |  |
| `Morelos` | `boolean` |  |  |
| `Nayarit` | `boolean` |  |  |
| `NuevoLeon` | `boolean` |  |  |
| `Oaxaca` | `boolean` |  |  |
| `Puebla` | `boolean` |  |  |
| `QuintanaRoo` | `boolean` |  |  |
| `Queretaro` | `boolean` |  |  |
| `Sinaloa` | `boolean` |  |  |
| `SanLuisPotosi` | `boolean` |  |  |
| `Sonora` | `boolean` |  |  |
| `Tabasco` | `boolean` |  |  |
| `Tlaxcala` | `boolean` |  |  |
| `Tamaulipas` | `boolean` |  |  |
| `Veracruz` | `boolean` |  |  |
| `Yucatan` | `boolean` |  |  |
| `Zacatecas` | `boolean` |  |  |


### Nested model: CarrierModeDTO

**`CarrierModeDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `LessThanTruckLoad` | `boolean` |  |  |
| `Partial` | `boolean` |  |  |
| `Truckload` | `boolean` |  |  |
| `Rail` | `boolean` |  |  |
| `Intermodal` | `boolean` |  |  |
| `Air` | `boolean` |  |  |
| `Expedite` | `boolean` |  |  |
| `Ocean` | `boolean` |  |  |
| `Drayage` | `boolean` |  |  |


### Nested model: CarrierOperationalDetailDTO

**`CarrierOperationalDetailDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `FleetSize` | `integer (int32)` |  |  |
| `TotalPowerUnits` | `integer (int32)` |  |  |
| `NumberOfVehicles` | `integer (int32)` |  |  |
| `ReeferEquipment` | `boolean` |  |  |
| `VanEquipment` | `boolean` |  |  |
| `FlatbedStepDeckEquipment` | `boolean` |  |  |
| `OwnedTractors` | `integer (int32)` |  |  |
| `OwnedTrucks` | `integer (int32)` |  |  |
| `OwnedTrailers` | `integer (int32)` |  |  |
| `TermLeasedTractors` | `integer (int32)` |  |  |
| `TermLeasedTrucks` | `integer (int32)` |  |  |
| `TermLeasedTrailers` | `integer (int32)` |  |  |
| `TripLeasedTractors` | `integer (int32)` |  |  |
| `TripLeasedTrucks` | `integer (int32)` |  |  |
| `TripLeasedTrailers` | `integer (int32)` |  |  |
| `InterstateAndIntrastateDrivers` | `integer (int32)` |  |  |
| `CDLEmployedDrivers` | `integer (int32)` |  |  |
| `MonthlyAverageLeasedDrivers` | `integer (int32)` |  |  |
| `InterstateDriversTotal` | `integer (int32)` |  |  |
| `InterstateDriversGT100Miles` | `integer (int32)` |  |  |
| `InterstateDriversLT100Miles` | `integer (int32)` |  |  |
| `IntrastateDriversTotal` | `integer (int32)` |  |  |
| `IntrastateDriversGT100Miles` | `integer (int32)` |  |  |
| `IntrastateDriversLT100Miles` | `integer (int32)` |  |  |
| `PowerOnly` | `boolean` |  |  |
| `SatelliteEquipment` | `boolean` |  |  |
| `TeamDrivers` | `boolean` |  |  |
| `DropTrailer` | `boolean` |  |  |
| `ELDCompliant` | `boolean` |  |  |
| `ELDCompliantBy` | `string` |  |  |
| `ELDIdentifier` | `string` |  |  |
| `NumberOfTractors` | `integer (int32)` |  |  |
| `NumberOfVans` | `integer (int32)` |  |  |
| `NumberOfReefers` | `integer (int32)` |  |  |
| `NumberOfFlats` | `integer (int32)` |  |  |
| `NumberOfStepDecks` | `integer (int32)` |  |  |
| `NumberOfTanks` | `integer (int32)` |  |  |


### Nested model: CarrierPaymentInfoDTO

**`CarrierPaymentInfoDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `BankRoutingNumber` | `string` |  |  |
| `BankAccountNumber` | `string` |  |  |
| `BankAccountName` | `string` |  |  |
| `BankName` | `string` |  |  |
| `BankAddress` | `string` |  |  |
| `BankPhone` | `string` |  |  |
| `BankFax` | `string` |  |  |
| `FactoringCompanyName` | `string` |  |  |
| `RemitAddress1` | `string` |  |  |
| `RemitAddress2` | `string` |  |  |
| `RemitCity` | `string` |  |  |
| `RemitZipCode` | `string` |  |  |
| `BankAccountType` | `string` |  |  |
| `RemitState` | `string` |  |  |
| `RemitCountry` | `string` |  |  |
| `RemitEmail` | `string` |  |  |
| `Require1099` | `boolean` |  |  |
| `EpayManagerID` | `integer (int32)` |  |  |
| `RemitCurrency` | `string` |  |  |
| `PayAdvanceOptionID` | `integer (int32)` |  |  |
| `PayAdvanceOptionType` | `string` |  |  |


### Nested model: CarrierPaymentTermDTO

**`CarrierPaymentTermDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `PaymentTerm` | `CustomerPaymentTermDTO` |  |  |


### Nested model: CarrierPaymentTypeDTO

**`CarrierPaymentTypeDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `PaymentType` | `CustomerPaymentTypeDTO` |  |  |


### Nested model: CarrierRemitDTO

**`CarrierRemitDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `CarrierRemitEmail` | `string` |  |  |
| `CarrierRemitAddress1` | `string` |  |  |
| `CarrierRemitAddress2` | `string` |  |  |
| `CarrierRemitCity` | `string` |  |  |
| `CarrierRemitCountry` | `string` |  |  |
| `CarrierRemitStateProvince` | `string` |  |  |
| `CarrierRemitZipCode` | `string` |  |  |


### Nested model: CarrierTINMatchingDTO

**`CarrierTINMatchingDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `TINTypeID` | `integer (int32)` |  |  |
| `TIN` | `string` |  |  |
| `TINName` | `string` |  |  |
| `TINMatchingStatusID` | `integer (int32)` |  |  |
| `TINMatchingResultID` | `integer (int32)` |  |  |
| `CreatedOnUtc` | `string (date-time)` |  |  |
| `SubmittedOnUtc` | `string (date-time)` |  |  |
| `ProcessedOnUtc` | `string (date-time)` |  |  |
| `ContactEmail` | `string` |  |  |
| `ContactPhoneNumber` | `string` |  |  |
| `MatchingResult` | `string` |  |  |
| `MatchingStatus` | `string` |  |  |


### Nested model: CarrierTruckClassDTO

**`CarrierTruckClassDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Conestoga` | `boolean` |  |  |
| `Containers` | `boolean` |  |  |
| `DecksSpecialized` | `boolean` |  |  |
| `DecksStandard` | `boolean` |  |  |
| `DryBulk` | `boolean` |  |  |
| `Flatbeds` | `boolean` |  |  |
| `HazardousMaterials` | `boolean` |  |  |
| `Reefers` | `boolean` |  |  |
| `Tankers` | `boolean` |  |  |
| `VansSpecialized` | `boolean` |  |  |
| `VansStandard` | `boolean` |  |  |
| `Other` | `string` |  |  |


### Nested model: CarrierTruckTypeDTO

**`CarrierTruckTypeDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `AFrameTrailer` | `boolean` |  |  |
| `AFrameTrailerCount` | `integer (int32)` |  |  |
| `AcidTanker` | `boolean` |  |  |
| `AcidTankerCount` | `integer (int32)` |  |  |
| `AugerTrailer` | `boolean` |  |  |
| `AugerTrailerCount` | `integer (int32)` |  |  |
| `AutoCarrier` | `boolean` |  |  |
| `AutoCarrierCount` | `integer (int32)` |  |  |
| `BeamTrailer` | `boolean` |  |  |
| `BeamTrailerCount` | `integer (int32)` |  |  |
| `BellyDumpTrailer` | `boolean` |  |  |
| `BellyDumpTrailerCount` | `integer (int32)` |  |  |
| `BTrain` | `boolean` |  |  |
| `BTrainCount` | `integer (int32)` |  |  |
| `BoatTrailer` | `boolean` |  |  |
| `BoatTrailerCount` | `integer (int32)` |  |  |
| `Chassis` | `boolean` |  |  |
| `ChassisCount` | `integer (int32)` |  |  |
| `ChemicalTankTrailer` | `boolean` |  |  |
| `ChemicalTankTrailerCount` | `integer (int32)` |  |  |
| `CompressedGasTanker` | `boolean` |  |  |
| `CompressedGasTankerCount` | `integer (int32)` |  |  |
| `Conestoga` | `boolean` |  |  |
| `ConestogaCount` | `integer (int32)` |  |  |
| `Container` | `boolean` |  |  |
| `ContainerCount` | `integer (int32)` |  |  |
| `ContainerChassisTrailer20Foot` | `boolean` |  |  |
| `ContainerChassisTrailer20FootCount` | `integer (int32)` |  |  |
| `ContainerChassisTrailer40Foot` | `boolean` |  |  |
| `ContainerChassisTrailer40FootCount` | `integer (int32)` |  |  |
| `ContainerChassisTrailerComboChassis` | `boolean` |  |  |
| `ContainerChassisTrailerComboChassisCount` | `integer (int32)` |  |  |
| `ContainerInsulated` | `boolean` |  |  |
| `ContainerInsulatedCount` | `integer (int32)` |  |  |
| `ContainerRefrigerated` | `boolean` |  |  |
| `ContainerRefrigeratedCount` | `integer (int32)` |  |  |
| `ContainerStandard` | `boolean` |  |  |
| `ContainerStandardCount` | `integer (int32)` |  |  |
| `ConvertibleTrailer` | `boolean` |  |  |
| `ConvertibleTrailerCount` | `integer (int32)` |  |  |
| `Conveyor` | `boolean` |  |  |
| `ConveyorCount` | `integer (int32)` |  |  |
| `CryogenicLiquidTanker` | `boolean` |  |  |
| `CryogenicLiquidTankerCount` | `integer (int32)` |  |  |
| `Dolly` | `boolean` |  |  |
| `DollyCount` | `integer (int32)` |  |  |
| `DoubleDrop` | `boolean` |  |  |
| `DoubleDropCount` | `integer (int32)` |  |  |
| `DropDeckLandoll` | `boolean` |  |  |
| `DropDeckLandollCount` | `integer (int32)` |  |  |
| `DryBulkTanker` | `boolean` |  |  |
| `DryBulkTankerCount` | `integer (int32)` |  |  |
| `DualLaneTrailer` | `boolean` |  |  |
| `DualLaneTrailerCount` | `integer (int32)` |  |  |
| `DumpTrailer` | `boolean` |  |  |
| `DumpTrailerCount` | `integer (int32)` |  |  |
| `EightToTenCarHauler` | `boolean` |  |  |
| `EightToTenCarHaulerCount` | `integer (int32)` |  |  |
| `EndDumpTrailer` | `boolean` |  |  |
| `EndDumpTrailerCount` | `integer (int32)` |  |  |
| `ExtendableFlatbedTrailer` | `boolean` |  |  |
| `ExtendableFlatbedTrailerCount` | `integer (int32)` |  |  |
| `FertilizerHopperTrailer` | `boolean` |  |  |
| `FertilizerHopperTrailerCount` | `integer (int32)` |  |  |
| `Flatbed` | `boolean` |  |  |
| `FlatbedCount` | `integer (int32)` |  |  |
| `FlatbedAirRide` | `boolean` |  |  |
| `FlatbedAirRideCount` | `integer (int32)` |  |  |
| `FlatbedConestoga` | `boolean` |  |  |
| `FlatbedConestogaCount` | `integer (int32)` |  |  |
| `FlatbedDouble` | `boolean` |  |  |
| `FlatbedDoubleCount` | `integer (int32)` |  |  |
| `FlatbedHazMat` | `boolean` |  |  |
| `FlatbedHazMatCount` | `integer (int32)` |  |  |
| `FlatbedHotshot` | `boolean` |  |  |
| `FlatbedHotshotCount` | `integer (int32)` |  |  |
| `FlatbedMaxi` | `boolean` |  |  |
| `FlatbedMaxiCount` | `integer (int32)` |  |  |
| `FlatbedOrStepDeck` | `boolean` |  |  |
| `FlatbedOrStepDeckCount` | `integer (int32)` |  |  |
| `FlatbedOverdimension` | `boolean` |  |  |
| `FlatbedOverdimensionCount` | `integer (int32)` |  |  |
| `FlatbedSpecialized` | `boolean` |  |  |
| `FlatbedSpecializedCount` | `integer (int32)` |  |  |
| `FlatbedWithchains` | `boolean` |  |  |
| `FlatbedWithchainsCount` | `integer (int32)` |  |  |
| `FlatbedWithSides` | `boolean` |  |  |
| `FlatbedWithSidesCount` | `integer (int32)` |  |  |
| `FlatbedWithTarps` | `boolean` |  |  |
| `FlatbedWithTarpsCount` | `integer (int32)` |  |  |
| `FlatbedWithTeam` | `boolean` |  |  |
| `FlatbedWithTeamCount` | `integer (int32)` |  |  |
| `FlatbedVanReefer` | `boolean` |  |  |
| `FlatbedVanReeferCount` | `integer (int32)` |  |  |
| `FoodGradeTankTrailer` | `boolean` |  |  |
| `FoodGradeTankTrailerCount` | `integer (int32)` |  |  |
| `FourToFiveCarHauler` | `boolean` |  |  |
| `FourToFiveCarHaulerCount` | `integer (int32)` |  |  |
| `FuelTankTrailer` | `boolean` |  |  |
| `FuelTankTrailerCount` | `integer (int32)` |  |  |
| `GasCylinderTrailer` | `boolean` |  |  |
| `GasCylinderTrailerCount` | `integer (int32)` |  |  |
| `GrainHopperTrailer` | `boolean` |  |  |
| `GrainHopperTrailerCount` | `integer (int32)` |  |  |
| `HazmatTanker` | `boolean` |  |  |
| `HazmatTankerCount` | `integer (int32)` |  |  |
| `HopperBottom` | `boolean` |  |  |
| `HopperBottomCount` | `integer (int32)` |  |  |
| `HopperHighSide` | `boolean` |  |  |
| `HopperHighSideCount` | `integer (int32)` |  |  |
| `HopperLowSide` | `boolean` |  |  |
| `HopperLowSideCount` | `integer (int32)` |  |  |
| `HopperTrailer` | `boolean` |  |  |
| `HopperTrailerCount` | `integer (int32)` |  |  |
| `HorseTrailer` | `boolean` |  |  |
| `HorseTrailerCount` | `integer (int32)` |  |  |
| `HotshotTrailer` | `boolean` |  |  |
| `HotshotTrailerCount` | `integer (int32)` |  |  |
| `InsulatedVanOrReefer` | `boolean` |  |  |
| `InsulatedVanOrReeferCount` | `integer (int32)` |  |  |
| `Landoll` | `boolean` |  |  |
| `LandollCount` | `integer (int32)` |  |  |
| `LivestockTrailer` | `boolean` |  |  |
| `LivestockTrailerCount` | `integer (int32)` |  |  |
| `LiveBottomTrailer` | `boolean` |  |  |
| `LiveBottomTrailerCount` | `integer (int32)` |  |  |
| `LoggingTrailer` | `boolean` |  |  |
| `LoggingTrailerCount` | `integer (int32)` |  |  |
| `Lowboy` | `boolean` |  |  |
| `LowboyCount` | `integer (int32)` |  |  |
| `LowboyOrRemGooseneck` | `boolean` |  |  |
| `LowboyOrRemGooseneckCount` | `integer (int32)` |  |  |
| `LowboyOverdimension` | `boolean` |  |  |
| `LowboyOverdimensionCount` | `integer (int32)` |  |  |
| `MiniDeckTrailer` | `boolean` |  |  |
| `MiniDeckTrailerCount` | `integer (int32)` |  |  |
| `MilkTankTrailer` | `boolean` |  |  |
| `MilkTankTrailerCount` | `integer (int32)` |  |  |
| `MovingVan` | `boolean` |  |  |
| `MovingVanCount` | `integer (int32)` |  |  |
| `MultiAxleHeavyHaulTrailer` | `boolean` |  |  |
| `MultiAxleHeavyHaulTrailerCount` | `integer (int32)` |  |  |
| `MultiLevelCarHauler` | `boolean` |  |  |
| `MultiLevelCarHaulerCount` | `integer (int32)` |  |  |
| `OneToTwoCarHauler` | `boolean` |  |  |
| `OneToTwoCarHaulerCount` | `integer (int32)` |  |  |
| `PerimeterTrailer` | `boolean` |  |  |
| `PerimeterTrailerCount` | `integer (int32)` |  |  |
| `PintleHitch` | `boolean` |  |  |
| `PintleHitchCount` | `integer (int32)` |  |  |
| `PintleHitchTrailer` | `boolean` |  |  |
| `PintleHitchTrailerCount` | `integer (int32)` |  |  |
| `PoleTrailer` | `boolean` |  |  |
| `PoleTrailerCount` | `integer (int32)` |  |  |
| `Pneumatic` | `boolean` |  |  |
| `PneumaticCount` | `integer (int32)` |  |  |
| `PowerOnly` | `boolean` |  |  |
| `PowerOnlyCount` | `integer (int32)` |  |  |
| `Reefer` | `boolean` |  |  |
| `ReeferCount` | `integer (int32)` |  |  |
| `ReeferAirRide` | `boolean` |  |  |
| `ReeferAirRideCount` | `integer (int32)` |  |  |
| `ReeferDouble` | `boolean` |  |  |
| `ReeferDoubleCount` | `integer (int32)` |  |  |
| `ReeferHazMat` | `boolean` |  |  |
| `ReeferHazMatCount` | `integer (int32)` |  |  |
| `ReeferIntermodal` | `boolean` |  |  |
| `ReeferIntermodalCount` | `integer (int32)` |  |  |
| `ReeferLogistics` | `boolean` |  |  |
| `ReeferLogisticsCount` | `integer (int32)` |  |  |
| `ReeferOrVentedVan` | `boolean` |  |  |
| `ReeferOrVentedVanCount` | `integer (int32)` |  |  |
| `ReeferPalletExchange` | `boolean` |  |  |
| `ReeferPalletExchangeCount` | `integer (int32)` |  |  |
| `ReeferSpecialized` | `boolean` |  |  |
| `ReeferSpecializedCount` | `integer (int32)` |  |  |
| `ReeferStandard48Foot` | `boolean` |  |  |
| `ReeferStandard48FootCount` | `integer (int32)` |  |  |
| `ReeferStandard53Foot` | `boolean` |  |  |
| `ReeferStandard53FootCount` | `integer (int32)` |  |  |
| `ReeferWithTeam` | `boolean` |  |  |
| `ReeferWithTeamCount` | `integer (int32)` |  |  |
| `RemovableGooseneck` | `boolean` |  |  |
| `RemovableGooseneckCount` | `integer (int32)` |  |  |
| `SideDumpTrailer` | `boolean` |  |  |
| `SideDumpTrailerCount` | `integer (int32)` |  |  |
| `SingleLevelCarHauler` | `boolean` |  |  |
| `SingleLevelCarHaulerCount` | `integer (int32)` |  |  |
| `SixToSevenCarHauler` | `boolean` |  |  |
| `SixToSevenCarHaulerCount` | `integer (int32)` |  |  |
| `StandardFlatbed48Foot` | `boolean` |  |  |
| `StandardFlatbed48FootCount` | `integer (int32)` |  |  |
| `StandardFlatbed53Foot` | `boolean` |  |  |
| `StandardFlatbed53FootCount` | `integer (int32)` |  |  |
| `SteerableStepDeckStretch` | `boolean` |  |  |
| `SteerableStepDeckStretchCount` | `integer (int32)` |  |  |
| `StepDeck` | `boolean` |  |  |
| `StepDeckCount` | `integer (int32)` |  |  |
| `StepDeckOrRemGooseneck` | `boolean` |  |  |
| `StepDeckOrRemGooseneckCount` | `integer (int32)` |  |  |
| `StepDeckSpecialized` | `boolean` |  |  |
| `StepDeckSpecializedCount` | `integer (int32)` |  |  |
| `StepDeckStandard48Foot` | `boolean` |  |  |
| `StepDeckStandard48FootCount` | `integer (int32)` |  |  |
| `StepDeckStandard53Foot` | `boolean` |  |  |
| `StepDeckStandard53FootCount` | `integer (int32)` |  |  |
| `StepdeckConestoga` | `boolean` |  |  |
| `StepdeckConestogaCount` | `integer (int32)` |  |  |
| `StraightBoxTruck` | `boolean` |  |  |
| `StraightBoxTruckCount` | `integer (int32)` |  |  |
| `StretchFlatbed` | `boolean` |  |  |
| `StretchFlatbedCount` | `integer (int32)` |  |  |
| `StretchRGN` | `boolean` |  |  |
| `StretchRGNCount` | `integer (int32)` |  |  |
| `StretchStepDeck` | `boolean` |  |  |
| `StretchStepDeckCount` | `integer (int32)` |  |  |
| `StretchTrailer` | `boolean` |  |  |
| `StretchTrailerCount` | `integer (int32)` |  |  |
| `TankerAluminum` | `boolean` |  |  |
| `TankerAluminumCount` | `integer (int32)` |  |  |
| `TankerIntermodal` | `boolean` |  |  |
| `TankerIntermodalCount` | `integer (int32)` |  |  |
| `TankerSteel` | `boolean` |  |  |
| `TankerSteelCount` | `integer (int32)` |  |  |
| `ThreeCarHauler` | `boolean` |  |  |
| `ThreeCarHaulerCount` | `integer (int32)` |  |  |
| `TinWideTrailer` | `boolean` |  |  |
| `TinWideTrailerCount` | `integer (int32)` |  |  |
| `Toter` | `boolean` |  |  |
| `ToterCount` | `integer (int32)` |  |  |
| `TruckAndTrailer` | `boolean` |  |  |
| `TruckAndTrailerCount` | `integer (int32)` |  |  |
| `Van` | `boolean` |  |  |
| `VanCount` | `integer (int32)` |  |  |
| `VanAirRide` | `boolean` |  |  |
| `VanAirRideCount` | `integer (int32)` |  |  |
| `VanBlanketWrap` | `boolean` |  |  |
| `VanBlanketWrapCount` | `integer (int32)` |  |  |
| `VanConestoga` | `boolean` |  |  |
| `VanConestogaCount` | `integer (int32)` |  |  |
| `VanDouble` | `boolean` |  |  |
| `VanDoubleCount` | `integer (int32)` |  |  |
| `VanHazMat` | `boolean` |  |  |
| `VanHazMatCount` | `integer (int32)` |  |  |
| `VanHeated` | `boolean` |  |  |
| `VanHeatedCount` | `integer (int32)` |  |  |
| `VanHotshot` | `boolean` |  |  |
| `VanHotshotCount` | `integer (int32)` |  |  |
| `VanInsulated` | `boolean` |  |  |
| `VanInsulatedCount` | `integer (int32)` |  |  |
| `VanIntermodal` | `boolean` |  |  |
| `VanIntermodalCount` | `integer (int32)` |  |  |
| `VanLiftGate` | `boolean` |  |  |
| `VanLiftGateCount` | `integer (int32)` |  |  |
| `VanLogistics` | `boolean` |  |  |
| `VanLogisticsCount` | `integer (int32)` |  |  |
| `VanOpenTop` | `boolean` |  |  |
| `VanOpenTopCount` | `integer (int32)` |  |  |
| `VanOrFlatbed` | `boolean` |  |  |
| `VanOrFlatbedCount` | `integer (int32)` |  |  |
| `VanOrFlatbedwTarps` | `boolean` |  |  |
| `VanOrFlatbedwTarpsCount` | `integer (int32)` |  |  |
| `VanOrReefer` | `boolean` |  |  |
| `VanOrReeferCount` | `integer (int32)` |  |  |
| `VanPalletExchange` | `boolean` |  |  |
| `VanPalletExchangeCount` | `integer (int32)` |  |  |
| `VanRollerBed` | `boolean` |  |  |
| `VanRollerBedCount` | `integer (int32)` |  |  |
| `VanSpecialized` | `boolean` |  |  |
| `VanSpecializedCount` | `integer (int32)` |  |  |
| `VanSprinter` | `boolean` |  |  |
| `VanSprinterCount` | `integer (int32)` |  |  |
| `VanStandard` | `boolean` |  |  |
| `VanStandardCount` | `integer (int32)` |  |  |
| `VanTriple` | `boolean` |  |  |
| `VanTripleCount` | `integer (int32)` |  |  |
| `VanVented` | `boolean` |  |  |
| `VanVentedCount` | `integer (int32)` |  |  |
| `VanWithCurtains` | `boolean` |  |  |
| `VanWithCurtainsCount` | `integer (int32)` |  |  |
| `VanWithTeam` | `boolean` |  |  |
| `VanWithTeamCount` | `integer (int32)` |  |  |
| `WalkingFloorTrailer` | `boolean` |  |  |
| `WalkingFloorTrailerCount` | `integer (int32)` |  |  |


### Nested model: CarrierW9FormDTO

**`CarrierW9FormDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `FullName` | `string` |  |  |
| `BusinessName` | `string` |  |  |
| `IndividualOrSingleMemberLLC` | `boolean` |  |  |
| `CCorporation` | `boolean` |  |  |
| `SCorporation` | `boolean` |  |  |
| `Partnership` | `boolean` |  |  |
| `RequesterNameAddress` | `string` |  |  |
| `TrustOrEstate` | `boolean` |  |  |
| `LimitedLiabilityCompany` | `boolean` |  |  |
| `TaxClassification` | `string` |  |  |
| `Other` | `boolean` |  |  |
| `OtherDetail` | `string` |  |  |
| `ExemptPayeeCode` | `string` |  |  |
| `ExemptionFATCACode` | `string` |  |  |
| `Address` | `string` |  |  |
| `CityStateZipCode` | `string` |  |  |
| `ListAccountNumber` | `string` |  |  |
| `SSN` | `string` |  |  |
| `EIN` | `string` |  |  |
| `SignatureDate` | `string (date-time)` |  |  |
| `SignaturePerson` | `string` |  |  |
| `IsActive` | `boolean` |  |  |
| `City` | `string` |  |  |
| `State` | `string` |  |  |
| `ZipCode` | `string` |  |  |
| `CarrierW9FormImages` | `Array[CarrierW9FormImageDTO]` |  |  |


### Nested model: CarrierW9FormImageDTO

**`CarrierW9FormImageDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `BlobName` | `string` |  |  |
| `CreatedDate` | `string (date-time)` |  |  |
| `FileName` | `string` |  |  |
| `CreatedBy` | `string` |  |  |


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


### Nested model: CustomerAgreementDTO

**`CustomerAgreementDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `AgreementName` | `string` |  |  |
| `CreatedDate` | `string (date-time)` |  |  |
| `CreatedBy` | `string` |  |  |
| `BlobName` | `string` |  |  |
| `Customer` | `CustomerDTO` |  |  |


### Nested model: CustomerDTO

**`CustomerDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `CustomerID` | `integer (int32)` |  |  |
| `Title` | `string` |  |  |
| `FirstName` | `string` |  |  |
| `MiddleName` | `string` |  |  |
| `LastName` | `string` |  |  |
| `CompanyName` | `string` |  |  |
| `TypeCompany` | `string` |  |  |
| `CellPhone` | `string` |  |  |
| `Phone` | `string` |  |  |
| `Fax` | `string` |  |  |
| `Address1` | `string` |  |  |
| `Address2` | `string` |  |  |
| `Apartment` | `string` |  |  |
| `City` | `string` |  |  |
| `State` | `string` |  |  |
| `Zipcode` | `string` |  |  |
| `Country` | `string` |  |  |
| `CustomerKey` | `string` |  |  |
| `PacketCompletionNotificationType` | `integer (int32)` |  |  |
| `PacketCompletionNotificationEmail` | `string` |  |  |


### Nested model: CustomerPaymentTermDTO

**`CustomerPaymentTermDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `PaymentTermID` | `integer (int32)` |  |  |
| `Days` | `integer (int32)` |  |  |
| `Term` | `string` |  |  |
| `QuickPay` | `boolean` |  |  |
| `PaymentFeeType` | `string` |  |  |
| `PaymentFeeAmount` | `number (double)` |  |  |
| `CustomerID` | `integer (int32)` |  |  |


### Nested model: CustomerPaymentTypeDTO

**`CustomerPaymentTypeDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `PaymentTypeID` | `integer (int32)` |  |  |
| `Type` | `string` |  |  |
| `CustomerID` | `integer (int32)` |  |  |
| `PaymentType` | `PaymentTypeDTO` |  |  |


### Nested model: FactoringRemitDTO

**`FactoringRemitDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `FactoringCompanyID` | `integer (int32)` |  |  |
| `FactoringCompanyName` | `string` |  |  |
| `FactoringRemitEmail` | `string` |  |  |
| `FactoringRemitAddress` | `string` |  |  |
| `FactoringRemitAddress2` | `string` |  |  |
| `FactoringRemitCity` | `string` |  |  |
| `FactoringRemitCountry` | `string` |  |  |
| `FactoringRemitStateProvince` | `string` |  |  |
| `FactoringRemitZipcode` | `string` |  |  |
| `FactoringPhone` | `string` |  |  |
| `BankRoutingNumber` | `string` |  |  |
| `BankAccountNumber` | `string` |  |  |


### Nested model: PayerTypeDTO

**`PayerTypeDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `PayerTypeID` | `integer (int32)` |  |  |
| `Name` | `string` |  |  |


### Nested model: PaymentTypeDTO

**`PaymentTypeDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Name` | `string` |  |  |


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


### Nested model: FMCSACarrier

**`FMCSACarrier`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
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

Related endpoints in **Carrier Data**:

- [PreviewCarrier](./preview-carrier.md)
- [GetCarrierContacts](./get-carrier-contacts.md)
- [GetCarrierRiskAssessment](./get-carrier-risk-assessment.md)
- [GetCarrierIncidentReports](./get-carrier-incident-reports.md)
- [GetCarrierVINVerifications](./get-carrier-vin-verifications.md)
- [FindAssociatedCarriers](./find-associated-carriers.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
