# FindAssociatedCarriers

`POST /api/v1/Carrier/FindAssociatedCarriers`

Searches carrier contact sources within MCP/FMCSA for associated carriers.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `phone` | `string` |  | The phone number to search for associated carriers. |
| `email` | `string` |  | The email address to search for associated carriers. |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `FindAssociatedCarriersDTO`

### Top-level: FindAssociatedCarriersDTO

**`FindAssociatedCarriersDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `Success` | `boolean` |  |  |
| `Message` | `string` |  |  |
| `AssociatedCarriersCount` | `integer (int32)` |  |  |
| `AssociatedCarriers` | `Array[AssociatedCarriersDTO]` |  | The list of associated carriers. |


### Nested model: AssociatedCarriersDTO

**`AssociatedCarriersDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `DOTNumber` | `integer (int32)` |  |  |
| `DocketNumber` | `string` |  |  |
| `CompanyName` | `string` |  |  |
| `DBAName` | `string` |  |  |
| `Street` | `string` |  |  |
| `City` | `string` |  |  |
| `State` | `string` |  |  |
| `ZipCode` | `string` |  |  |
| `Country` | `string` |  |  |
| `Phone` | `string` |  |  |
| `PhoneAssociationTypes` | `Array[AssociationTypeDTO]` |  |  |
| `EmailAssociationTypes` | `Array[AssociationTypeDTO]` |  |  |


### Nested model: AssociationTypeDTO

**`AssociationTypeDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `AssociationType` | `integer (int32)` |  | Value/Type List: 1 = Company, 2 = Support, 3 = Claims, 4 = SafetyManager, 5 = DispatchService, 6 = Owner, 7 = AvailableLoads, 8 = AuthorizedUser, 9 = UserAuthorizationPending, 10 = UserAuthorizationDenied, 11 = UserAuthorizationFollowUp, 12 = VerifiedUser, 13 = UserVerificationPending, 14 = UserVerificationDenied, 15 = UserVerificationFollowUp, 16 = Driver, 17 = Dispatcher, 18 = MCRecord, 19 = DOTRecord; Value Only List: (enum: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) |
| `Description` | `string` |  |  |


## See also

Related endpoints in **Carrier Data**:

- [PreviewCarrier](./preview-carrier.md)
- [GetCarrierData](./get-carrier-data.md)
- [GetCarrierContacts](./get-carrier-contacts.md)
- [GetCarrierRiskAssessment](./get-carrier-risk-assessment.md)
- [GetCarrierIncidentReports](./get-carrier-incident-reports.md)
- [GetCarrierVINVerifications](./get-carrier-vin-verifications.md)

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
