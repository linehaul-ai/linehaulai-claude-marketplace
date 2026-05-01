# MyCarrierPackets API — Complete Endpoint Reference

All 23 endpoints. Auth: `Authorization: bearer <access_token>` header on every request.
Base URL: `https://api.mycarrierpackets.com`
All parameters are query string unless noted. All endpoints use `POST`.

---

## Table of Contents

- [Carrier Data](#carrier-data)
- [Invitations & Verifications](#invitations--verifications)
- [Monitoring](#monitoring)
- [Block / Unblock](#block--unblock)
- [Factoring](#factoring)

---

## Carrier Data

### PreviewCarrier
`POST /api/v1/Carrier/PreviewCarrier`

Carrier profile + risk + certdata. **Excludes** packet data. Use before inviting — loads approved emails, risk, and cert status.

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| DOTNumber | integer | — | At least one identifier required |
| docketNumber | string | — | MC/FF/MX format |

**Response: PreviewCarrier object**
```
CarrierID            integer
DotNumber            integer
DocketNumber         string
CompanyName          string
DBAName              string
Street / City / State / ZipCode / Country / Phone  string
Status               string      (Active, Inactive, etc.)
StatusDate           string
InProcessState       string
PossibleFraud        string
DoubleBrokering      string
FraudCallNumber      string
HasSaferWatchKey     boolean
WatchdogReports      string
OnCurrentCustomerAgreement  boolean
IsIntrastateCarrier  boolean
IsMonitored          boolean
IsBlocked            boolean
FreightValidateStatus string
Source               integer
Emails               string[]
CarrierRating        CarrierRating
RiskAssessment       RiskAssessment      (Overall/Authority/Insurance/Safety/Operation: string)
RiskAssessmentDetails RiskAssessmentDetails
CertData             CertData
IncidentReports      IncidentReports
```

**CarrierRating fields:** `CarrierID, CustomerID, CustomerRating, RatingSum, TotalRatings, LowRatings, TotalRatingPercent, CustomerRatingPercent, RatingValue, RatingValueText, AvgRatingText, AvgRatingBasisText, HasCompletedPacket`

**CertData fields:** `Status (string), Noncoop (boolean), Certificates (array)`

**Certificate fields:** `CertificateID, ProducerName, ProducerAddress, ProducerCity, ProducerState, ProducerZip, ProducerPhone, ProducerFax, ProducerEmail, PaidFor, Coverages (array)`

**Coverage fields:** `InsurerName, Type, PolicyNumber, ExpirationDate, CoverageLimit, Deductible, ReferBreakdown, ReferBreakDeduct, CancellationDate`

---

### GetCarrierData
`POST /api/v1/Carrier/GetCarrierData`

Same as PreviewCarrier but **includes** full packet data (W9, agreements, bank info, payment terms, equipment details, lanes, etc.).

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| DOTNumber | integer | — | |
| DocketNumber | string | — | |

Response extends PreviewCarrier with packet data fields. Use `GetDocument` to retrieve actual PDF bytes using blob names returned here.

---

### GetCarrierContacts
`POST /api/v1/Carrier/GetCarrierContacts`

Authorized and verified users for a carrier.

| Param | Type | Req |
|-------|------|-----|
| DOTNumber | integer | — |
| docketNumber | string | — |

**Response:**
```
Success       boolean
Message       string
Carrier:
  DOTNumber   integer
  Contacts[]:
    FirstName              string
    LastName               string
    Title                  string
    Phone                  string
    Email                  string
    AuthorizedForPackets   boolean
    VerificationStatus     string
```

---

### FindAssociatedCarriers
`POST /api/v1/Carrier/FindAssociatedCarriers`

Fraud detection — finds carriers sharing a phone number or email. Supply at least one.

| Param | Type | Req |
|-------|------|-----|
| phone | string | — |
| email | string | — |

**Response:**
```
Success                  boolean
Message                  string
AssociatedCarriersCount  integer
AssociatedCarriers[]:
  DOTNumber              integer
  DocketNumber           string
  CompanyName            string
  DBAName                string
  Street/City/State/ZipCode/Country/Phone  string
  PhoneAssociationTypes[]: { AssociationType: integer, Description: string }
  EmailAssociationTypes[]: { AssociationType: integer, Description: string }
```

---

### GetCarrierIncidentReports
`POST /api/v1/Carrier/GetCarrierIncidentReports`

Incident report history for a carrier.

| Param | Type | Req |
|-------|------|-----|
| DOTNumber | integer | — |
| docketNumber | string | — |

**Response:**
```
DOTNumber       integer
DocketNumber    string
LegalName       string
DBAName         string
IncidentReports[]:
  IncidentDate               string
  OriginCity/State/Country   string
  DestinationCity/State/Country  string
  ReportedByCompany          string
  CarrierEmails              string
  CreatedBy / CreatedDate    string
  ModifiedBy / ModifiedDate  string
  IncidentTypes              string[]
  Comments[]:
    { Comment: string, CreatedBy: string, CreatedDate: string }
```

---

### GetCarrierVINVerifications
`POST /api/v1/Carrier/GetCarrierVINVerifications`

VIN verification status for all verifications associated with a carrier.

| Param | Type | Req |
|-------|------|-----|
| DOTNumber | integer | — |
| docketNumber | string | — |

**Response:**
```
DOTNumber       integer
DocketNumber    string
LegalName       string
DBAName         string
VINVerifications[]:
  VIN                    string
  VINVerificationStatus  object
  CreatedOnUtc           string
  ModifiedOnUtc          string
  OtherCarrier           object  (if VIN belongs to another carrier)
  Requests               array
```

---

### GetCarrierRiskAssessment
`POST /api/v1/Carrier/GetCarrierRiskAssessment`

Risk assessment for a single carrier.

| Param | Type | Req |
|-------|------|-----|
| dotNumber | integer | — |
| docketNumber | string | — |

**Response:**
```
DOTNumber            integer
DocketNumber         string
RiskAssessmentDetails:
  Authority:
    TotalPoints    integer
    OverallRating  string     (Pass / Warning / Fail)
    HasRuleOverride boolean
    Infractions    string[]
  Insurance:       same structure
  Safety:          same structure
  Operation:       same structure
  Other:           same structure
```

---

### GetDocument
`POST /api/v1/Carrier/GetDocument`

Retrieves a PDF document (COI, W9, eAgreement) as binary. Blob names come from `GetCarrierData` response.

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| name | string | **Yes** | Blob name, e.g. `company-agreement/12/guid-abc123` |

**Response:** Binary PDF stream. Store locally — do not regenerate on every request.

---

### CompletedPackets
`POST /api/v1/Carrier/CompletedPackets`

Carriers that completed packets in a date range. Poll every 5–15 minutes.

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| fromDate | string | **Yes** | `YYYY-MM-DDTHH:MM:SS` |
| toDate | string | **Yes** | `YYYY-MM-DDTHH:MM:SS` |

**Response:** Array of:
```
DOTNumber      integer
DocketNumber   string
LegalName      string
CompletedDate  string
```

---

## Invitations & Verifications

### EmailPacketInvitation
`POST /api/v1/Carrier/EmailPacketInvitation`

Sends Intellivite invitation email to carrier.

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| carrierEmail | string | **Yes** | |
| dotNumber | integer | — | |
| docketNumber | string | — | |
| userName | string | — | MCP username — enables MCP to communicate with inviting user |
| sendConfirmationEmail | boolean | — | Sends confirmation to inviter |
| notificationEmails | string | — | Comma-separated CC emails |

---

### RequestUserVerification
`POST /api/v1/Carrier/RequestUserVerification`

Requests non-onboarding Intellivite user verification (for existing contacts).

| Param | Type | Req |
|-------|------|-----|
| userVerificationEmail | string | **Yes** |
| dotNumber | integer | — |
| docketNumber | string | — |
| userName | string | — |

---

### RequestVINVerification
`POST /api/v1/Carrier/RequestVINVerification`

Requests VIN verification. **Only phone delivery (option 2) is currently supported** — email (option 1) is listed in spec but not active.

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| deliveryOption | integer | **Yes** | `2` = PhoneNumber (only supported value) |
| vinVerificationPhoneNumber | string | — | Required when deliveryOption=2 |
| vinVerificationEmail | string | — | Not currently active |
| dotNumber | integer | — | |
| docketNumber | string | — | |
| userName | string | — | |
| outputVINVerificationRequestID | boolean | — | Returns request ID in response |

---

## Monitoring

### MonitoredCarriers
`POST /api/v1/Carrier/MonitoredCarriers`

List of all monitored carriers. Pagination via `X-Pagination` response header.

| Param | Type | Default | Max |
|-------|------|---------|-----|
| pageNumber | integer | 1 | — |
| pageSize | integer | 2500 | 5000 |

**Pagination header:** `X-Pagination: {"pageNumber":1,"pageSize":2500,"totalPages":10,"totalCount":25000}`

**Response:** Array of:
```
DOTNumber          integer
DocketNumber       string
IntrastateNumber   string
CreatedDate        string
CreatedBy          string
LastModifiedDate   string
LastModifiedBy     string
```

---

### MonitoredCarrierData
`POST /api/v1/Carrier/MonitoredCarrierData`

Full `GetCarrierData` for all monitored carriers. Heavy operation — use for bulk sync only.

**Pagination is in the response body** (not the header — different from other paged endpoints).

| Param | Type | Default | Max |
|-------|------|---------|-----|
| pageNumber | integer | 1 | — |
| pageSize | integer | 250 | 500 |

**Response:**
```
pageNumber    integer
pageSize      integer
totalPages    integer
totalCount    integer
succeeded     boolean
message       string
data[]        CarrierDetails objects (same structure as CarriersChanges.CarrierDetails)
```

---

### GetMonitoredCarrierContactsData
`POST /api/v1/Carrier/GetMonitoredCarrierContactsData`

Contacts for every carrier on the monitored list.

| Param | Type | Default |
|-------|------|---------|
| pageNumber | integer | 1 |
| pageSize | integer | 250 |

**Response:** Array of carrier contact records:
```
FirstName / LastName / Title / Phone / Email   string
AuthorizedForPackets   boolean
VerificationStatus     string
```

---

### GetMonitoredCarriersRiskAssessment
`POST /api/v1/Carrier/GetMonitoredCarriersRiskAssessment`

Bulk risk assessments for all monitored carriers.

| Param | Type | Default | Max |
|-------|------|---------|-----|
| pageNumber | integer | 1 | — |
| pageSize | integer | 250 | 500 |

**Response:** Array of:
```
DOTNumber              integer
DocketNumber           string
RiskAssessmentDetails  (same structure as GetCarrierRiskAssessment)
```

---

### CarriersChanges
`POST /api/v1/Carrier/CarriersChanges`

Changes to carrier insurance, risk, authority, etc. Poll every 5–15 minutes. If no pagination params, all changes returned. With pagination, uses `X-Pagination` header.

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| fromDate | string | **Yes** | `YYYY-MM-DDTHH:MM:SS` |
| toDate | string | **Yes** | `YYYY-MM-DDTHH:MM:SS` |
| pageNumber | integer | — | |
| pageSize | integer | — | Default 250, max 500 |

**Pagination header:** `X-Pagination: {"pageNumber":1,"pageSize":250,"totalPages":10,"totalCount":2500}`

**Response:**
```
FromDate / ToDate / RequestDateTimeUtc   string
InsuranceChangeCount     integer
FMCSAChangeCount         integer
RiskAssessmentChangeCount integer
CarrierCount             integer
CarrierList[]:
  ChangeDateTime         string
  ChangeCategories       string[]   (e.g. ["Insurance", "Authority"])
  CarrierDetails:
    docketNumber         string
    dotNumber            object
    carrierType          string
    isMonitored          boolean
    isBlocked            boolean
    Identity             object (legalName, dbaName, address fields)
    Authority            object (authGrantDate, commonAuthority, contractAuthority, brokerAuthority, etc.)
    FMCSAInsurance       object (bipdRequired, bipdOnFile, cargoRequired, cargoOnFile, PolicyList)
    CertData             object
    Safety               object
    Inspection           object
    Crash                object
    Review               object
    Operation            object
    Cargo                object
    Drivers              object
    Equipment            object
    RiskAssessment       object (Overall/Authority/Insurance/Safety/Operation: string)
    RiskAssessmentDetails object
    LatestInvitation     object
    IncidentReports      object
```

---

### RequestMonitoring
`POST /api/v1/Carrier/RequestMonitoring`

Adds carrier to Assure Advantage monitoring list. Supply DOT+Docket for interstate, IntrastateNumber for intrastate-only.

| Param | Type | Req |
|-------|------|-----|
| DOTNumber | integer | — |
| DocketNumber | string | — |
| IntrastateNumber | string | — |

---

### CancelMonitoring
`POST /api/v1/Carrier/CancelMonitoring`

Removes carrier from monitoring list.

| Param | Type | Req |
|-------|------|-----|
| DOTNumber | integer | — |
| DocketNumber | string | — |
| IntrastateNumber | string | — |

---

## Block / Unblock

### BlockCarrier
`POST /api/v1/Carrier/BlockCarrier`

Adds carrier to block list.

| Param | Type |
|-------|------|
| DOTNumber | integer |
| DocketNumber | string |
| IntrastateNumber | string |

---

### UnblockCarrier
`POST /api/v1/Carrier/UnblockCarrier`

Removes carrier from block list. Same params as BlockCarrier.

---

### BlockedCarriers
`POST /api/v1/Carrier/BlockedCarriers`

Paginated list of blocked carriers. Uses `X-Pagination` response header.

| Param | Type | Default |
|-------|------|---------|
| pageNumber | integer | 1 |
| pageSize | integer | 2500 |

**Response:** Array of:
```
DOTNumber / DocketNumber / IntrastateNumber   string/integer
CreatedDate / CreatedBy / LastModifiedDate / LastModifiedBy   string
```

---

## Factoring

### GetUpdatedFactoringCompanies
`POST /api/v1/Carrier/GetUpdatedFactoringCompanies`

Returns MyCarrierPortal factoring companies with their unique IDs (used in carrier payment routing).

| Param | Type | Req | Notes |
|-------|------|-----|-------|
| fromDate | string | **Yes** | `YYYY-MM-DDTHH:MM:SS` |
| toDate | string | — | Defaults to now if omitted |

**Response:** Array of:
```
FactoringCompanyID           integer
FactoringCompanyName         string
FactoringRemitEmail          string
FactoringRemitAddress        string
FactoringRemitAddress2       string
FactoringRemitCity           string
FactoringRemitCountry        string
FactoringRemitStateProvince  string
FactoringRemitZipcode        string
FactoringPhone               string
CreatedDateTime              string
UpdatedDateTime              string
```

---

## Pagination Summary

| Endpoint | Page Source | Default Size | Max Size |
|----------|-------------|-------------|---------|
| MonitoredCarriers | `X-Pagination` header | 2500 | 5000 |
| BlockedCarriers | `X-Pagination` header | 2500 | — |
| CarriersChanges | `X-Pagination` header | 250 | 500 |
| MonitoredCarrierData | Response **body** | 250 | 500 |
| GetMonitoredCarriersRiskAssessment | Response body | 250 | 500 |
| GetMonitoredCarrierContactsData | Response body | 250 | — |

**Parse `X-Pagination` header as JSON:**
```json
{"pageNumber": 1, "pageSize": 250, "totalPages": 10, "totalCount": 2500}
```
