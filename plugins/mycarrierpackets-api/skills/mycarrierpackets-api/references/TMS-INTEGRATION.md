# TMS Integration Guide

Official MyCarrierPackets (MCP) integration guide for Transportation Management Systems. Source: MCP API Demo.

## Authentication

**Security Token:** `POST https://api.mycarrierpackets.com/token` (`grant_type: password`)

Requires customer integration username and password. Admins manage credentials at:

`https://mycarrierpackets.com/IntegrationTools`

Postman can be used for testing.

**Response Format:** Default is JSON. To receive XML, add header `Accept: text/xml`.

---

## 1. Intellivite — Invite Carriers to Complete Packets

### 1.1 RECOMMENDED: TMS Invite Screen Calling Invite API

Create an invite screen in the TMS that allows users to enter a carrier DOT and email (preload Intellivite-approved carrier email addresses and other data using the preview API in 1.1.2.1) to call the invite API (Post call / Token required).

#### 1.1.1 With MCP User (Recommended)

Allows MCP to communicate with the user who sent the invitation:

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/EmailPacketInvitation
  ?dotNumber={DOTNumber}
  &docketNumber={MC,FF,MX}
  &carrierEmail={carrieremail}
  &username={customerusername}
```

#### 1.1.2 Without MCP User

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/EmailPacketInvitation
  ?dotNumber={DOTNumber}
  &docketNumber={MC,FF,MX}
  &carrierEmail={carrieremail}
```

#### 1.1.2.1 Preview Carrier (preload data)

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/PreviewCarrier
  ?DOTNumber={DOTNumber}
  &docketNumber={MC,FF,MX}
```

Use to preload approved emails, risk assessment, and preloaded certificate data, making invitation more efficient.

### 1.2 Intellivite Link in TMS-Generated Email

#### 1.2.1 (Recommended) User-Specific Link with DOT and Docket

```
https://mycarrierpackets.com/{CustomerIntelliviteID}/Carrier/Intellivite/{CustomerMCPUserID}/{DOTNumber}/{DocketNumber}
```

Example:
```
https://mycarrierpackets.com/ea72823e-1506-4b72-a3b0-a488e1ba2f1e/Carrier/Intellivite/brenda/23868/MC113843
```

Adding the DOT and Docket eliminates the need for carriers to add their DOT. User-specific Intellivite links allow communication of who the carrier is working with at the company. This is the most efficient method for overrides, communication, and ease of registration.

#### 1.2.2 User-Specific Link Without DOT and Docket

```
https://mycarrierpackets.com/{CustomerIntelliviteID}/Carrier/Intellivite/{CustomerMCPUserID}
```

Note: Cannot send Docket without DOT, but DOT-only is allowed for intrastate carriers.

#### 1.2.3 Basic Intellivite (no user/Docket/DOT)

```
https://mycarrierpackets.com/{CustomerIntelliviteID}/Carrier/Intellivite
```

##### 1.2.3.1 Preview Carrier (same as 1.1.2.1)

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/PreviewCarrier
  ?DOTNumber={DOTNumber}
  &DocketNumber={MC,FF,MX}
```

**Note:** Customers find the basic Intellivite link in the Integration Tools page (admins). Users access their Intellivite links under their MyCarrierPackets profile.

### 1.3 URL to MCP to Invite Carrier

#### 1.3.1 (Recommended)

```
https://mycarrierpackets.com/RegisteredCustomer/SendCarrierPacket?dotNumber={dotNumber}&docketNumber={docketNumber}
```

#### 1.3.2 Intrastate Only

```
https://mycarrierpackets.com/RegisteredCustomer/SendCarrierPacket?dotNumber={dotNumber}
```

---

## 2. MyCarrierPackets

### 2.1 Check for Completed Carrier Packets

#### 2.1.1 Completed Packets API

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/completedpackets
  ?fromDate={YYYY-MM-DDTHH:MM:SS}
  &toDate={YYYY-MM-DDTHH:MM:SS}
```

#### 2.1.2 Customer-Hosted Callback

Provide MCP with an API to call. Provide a field for DOT. Example:

```
https://api.SampleCustomer.com/{DOTNumber}/{DocketNumber}
```

### 2.2 Update or Add Carrier Packets

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/GetCarrierData
  ?DOTNumber={DOTNumber}
  &Docket={MC,FF,MXNumber}
```

### 2.3 "View Carrier" Button

Add a "View Carrier" button to each carrier profile in the TMS to view MyCarrierPacket and/or Assure Advantage data.

#### 2.3.1 (Recommended)

```
https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dotNumber}/DocketNumber/{docketNumber}
```

#### 2.3.2 Intrastate Only

```
https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dotNumber}
```

---

## 3. Assure Advantage Carrier Monitoring

### 3.1 Initial and Periodic Full Carrier Sync

#### 3.1.1 Get Monitored List from MCP

##### 3.1.1.1 (Recommended) Monitored Carriers API

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/MonitoredCarriers
  ?pageNumber={1}
  &pageSize={default 2500, max 5000}
```

Pagination is returned in the **response header**:

- Header Name: `X-Pagination`
- Header Value: `{"pageNumber":1,"pageSize":2500,"totalPages":10,"totalCount":25000}`

Alternative: customer manually exports the list at `https://mycarrierpackets.com/CarrierMonitoring`.

#### 3.1.2 Compare MCP/TMS Carrier Lists

##### 3.1.2.1 Add Missing Carriers

For carriers monitored in TMS but not in MCP, add to MCP monitored list:

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/RequestMonitoring
```

##### 3.1.2.2 Remove Extra Carriers

For carriers monitored in MCP but not in TMS, remove from MCP monitored list:

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/CancelMonitoring
```

#### 3.1.3 Update Carrier List

##### 3.1.3.1 Batch Update All Carriers

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/MonitoredCarrierData
  ?pageNumber={1}
  &pageSize={default 250, max 500}
```

Pagination is returned in the **body** of the response.

##### 3.1.3.2 Per-Carrier Update

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/GetCarrierData
  ?DOTNumber={DOTNumber}
  &Docket={MC,FF,MXNumber}
```

### 3.2 Carrier Batch Updates

Call APIs at no less than 4-minute intervals.

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/CarriersChanges
  ?fromDate={YYYY-MM-DDTHH:MM:SS}
  &toDate={YYYY-MM-DDTHH:MM:SS}
  &pageNumber={1}
  &pageSize={default 250, max 500}
```

Pagination in **response header**:

- Header Name: `X-Pagination`
- Header Value: `{"pageNumber":1,"pageSize":250,"totalPages":10,"totalCount":2500}`

### 3.3 Request Certificates of Insurance

#### 3.3.1 (Recommended)

```
https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dotNumber}/DocketNumber/{docketNumber}?requestInsurance=true
```

#### 3.3.2 Intrastate Only

```
https://mycarrierpackets.com/CarrierInformation/DOTNumber/{dotNumber}?requestInsurance=true
```

### 3.4 Update Carrier Now Button

Pulls carrier data in real-time using the GetCarrierData API (section 2.2).

### 3.5 Pull Image of Certificate of Insurance

See section 4.1 below.

### 3.6 Monitor Carrier

#### 3.6.1 Add to Monitored List

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/RequestMonitoring
```

##### 3.6.1.1 Body

`DOTNumber`, `DocketNumber`, and/or `IntrastateNumber`

#### 3.6.2 Remove from Monitored List

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/CancelMonitoring
```

##### 3.6.2.1 Body

`DOTNumber`, `DocketNumber`, and/or `IntrastateNumber`

---

## 4. Pull Carrier Packet and Assure Advantage Images

### 4.1 Pull Each Document Individually

```
POST https://api.mycarrierpackets.com/api/v1/Carrier/GetDocument?name={Blobname}
```

For Certificate of Insurance, W9, and eAgreement, blob names come from the GetCarrierData API in section 2.2.

#### 4.1.1 Postman Testing

If testing in Postman, click **Save Response** to download.

### 4.2 Pull Full Packet via URL (Logged-In User)

```
https://mycarrierpackets.com/Download/GetCarrierPacket?DOTNumber={DOTNumber}&inline=True
```

#### 4.2.1 Requires user to be logged in.

### 4.3 Pull Full Packet as PDF via API

```
GET https://mycarrierpackets.com/api/Download/CarrierPacket/{DotNumber}
```

#### 4.3.1 Use Separate Token API

```
GET https://mycarrierpackets.com/api/token
```
(`grant_type: password`)

Note: This is a different token endpoint from the main API token in section "Authentication" above.

#### 4.3.2 Postman Testing

If testing in Postman, click **Save Response** to download.

---

## Integration Notes

1. When mapping data fields, if a carrier is set to monitor and no data is sent from The Descartes Systems Group, Inc., the fields should be blank.

2. When mapping data fields, fields should be locked — not allowing users to type information in unless the carrier is unchecked for monitoring. This way, the system always reflects whose data is being viewed.

3. **Initial sync and periodic update process:**

   a. The user should be able to run a report of all carriers monitored within the TMS.

   b. Customers can upload their list of monitored carriers in the Upload page of MyCarrierPackets.

   c. The TMS should clear all mapped monitoring fields, and pull an update on all carriers using the GetCarrierData API in section 2.2 above.
