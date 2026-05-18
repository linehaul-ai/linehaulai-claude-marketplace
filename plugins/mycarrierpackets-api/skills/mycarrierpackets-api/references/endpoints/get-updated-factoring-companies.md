# GetUpdatedFactoringCompanies

`POST /api/v1/Carrier/GetUpdatedFactoringCompanies`

Returns list of MyCarrierPortal Factoring Companies with their unique identifiers.

## Parameters

**Query string:**

| Name | Type | Req | Description |
|------|------|-----|-------------|
| `fromDate` | `string (date-time)` | yes | Start date for the update period. For example: 2024-01-01T00:00:00Z |
| `toDate` | `string (date-time)` |  | End date for the update period. For example: 2024-01-01T23:59:59Z |

**Headers:**

| Name | Required | Description |
|------|----------|-------------|
| `Authorization` |  | bearer access_token |

> All endpoints require `Authorization: bearer <access_token>`.

## Response (200)

**Returns:** `UpdatedFactoringCompaniesDTO`

### Top-level: UpdatedFactoringCompaniesDTO

**`UpdatedFactoringCompaniesDTO`**

| Field | Type | Req | Description |
|-------|------|-----|-------------|
| `FromDate` | `string (date-time)` |  |  |
| `ToDate` | `string (date-time)` |  |  |
| `RequestDateTimeUtc` | `string (date-time)` |  |  |
| `FactoringCompaniesCount` | `integer (int32)` |  |  |
| `FactoringCompanies` | `Array[UpdatedFactoring]` |  |  |


### Nested model: UpdatedFactoring

**`UpdatedFactoring`**

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
| `CreatedDateTime` | `string (date-time)` |  |  |
| `UpdatedDateTime` | `string (date-time)` |  |  |


## See also

- [Endpoint INDEX](./INDEX.md)
- [SKILL.md](../../SKILL.md) — workflow guidance, auth, pagination, error handling
- [TMS-INTEGRATION.md](../TMS-INTEGRATION.md) — official numbered integration workflow
