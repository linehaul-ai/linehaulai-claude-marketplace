[![swagger](https://api.mycarrierpackets.com/swagger/ui/images/logo_small-png)swagger](http://swagger.io/)

[Explore](https://api.mycarrierpackets.com/swagger/ui/index#)

My Carrier Packets Api

- ## [CarrierController](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController)



  - [Show/Hide](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController)
  - [List Operations](https://api.mycarrierpackets.com/swagger/ui/index#)
  - [Expand Operations](https://api.mycarrierpackets.com/swagger/ui/index#)

  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_PreviewCarrier)[/api/v1/Carrier/PreviewCarrier](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_PreviewCarrier)



    - [Retrieves carrier profile data, risk assessment, certdata. **Excludes** carrier packet data.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_PreviewCarrier)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model \[\
\
Inline Model 1\
\
\]

Inline Model 1 {

CarrierID (integer, optional),

DotNumber (integer, optional),

DocketNumber (string, optional),

CompanyName (string, optional),

DBAName (string, optional),

Street (string, optional),

City (string, optional),

State (string, optional),

ZipCode (string, optional),

Country (string, optional),

Phone (string, optional),

Status (string, optional),

StatusDate (string, optional),

InProcessState (string, optional),

PossibleFraud (string, optional),

DoubleBrokering (string, optional),

IncidentReports (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.IncidentReports, optional),

FraudCallNumber (string, optional),

HasSaferWatchKey (boolean, optional),

WatchdogReports (string, optional),

OnCurrentCustomerAgreement (boolean, optional),

CarrierRating (MyCarrierPacketsBusiness.Carriers.CarrierRating, optional),

RiskAssessment (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessment, optional),

RiskAssessmentDetails (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetails, optional),

CertData (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.CertData, optional),

Emails (Array\[MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.CarrierEmail\], optional),

Source (integer, optional):
Value/Type List: 0 = Unknown, 1 = ThirdParty, 2 = MyCarrierPackets, 3 = FMCSAData; Value Only List:
= \['0', '1', '2', '3'\]

| integer |
| --- |
| Enum: | 0, 1, 2, 3 |

,

IsIntrastateCarrier (boolean, optional),

IsMonitored (boolean, optional),

IsBlocked (boolean, optional),

FreightValidateStatus (string, optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.IncidentReports {

TotalIncidentReports (integer, optional),

TotalIncidentReportsWithFraud (integer, optional)

}

MyCarrierPacketsBusiness.Carriers.CarrierRating {

CarrierID (integer, optional),

CustomerID (integer, optional),

CustomerRating (integer, optional),

RatingSum (integer, optional),

TotalRatings (integer, optional),

LowRatings (integer, optional),

TotalRatingPercent (integer, optional, read only),

CustomerRatingPercent (integer, optional, read only),

RatingValue (number, optional, read only),

RatingValueText (string, optional, read only),

AvgRatingText (string, optional, read only),

AvgRatingBasisText (string, optional, read only),

AvgRatingTextPlusRatingBasisText (string, optional, read only),

CustomerRatingText (string, optional, read only),

HasCompletedPacket (boolean, optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessment {

Overall (string, optional),

Authority (string, optional),

Insurance (string, optional),

Safety (string, optional),

Operation (string, optional),

Other (string, optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetails {

IsIntrastateCarrier (boolean, optional),

TotalPoints (integer, optional),

OverallRating (string, optional),

Authority (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetail, optional),

Insurance (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetail, optional),

Safety (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetail, optional),

Operation (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetail, optional),

Other (MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetail, optional),

ReviewState (string, optional),

ReviewDetails (MyCarrierPacketsRiskAssessmentModels.ReviewDetails, optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.CertData {

Status (string, optional),

Noncoop (boolean, optional),

Certificates (Array\[MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.Certificate\], optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.CarrierEmail {

EmailType (integer, optional):
Value/Type List: 1 = McpEmail, 2 = CompanyEmail, 3 = FMCSAEmail; Value Only List:
= \['1', '2', '3'\]

| integer |
| --- |
| Enum: | 1, 2, 3 |

,

Description (string, optional),

Email (string, optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentDetail {

TotalPoints (integer, optional),

OverallRating (string, optional),

HasRuleOverride (boolean, optional, read only),

Infractions (Array\[MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentInfraction\], optional)

}

MyCarrierPacketsRiskAssessmentModels.ReviewDetails {

ReviewID (integer, optional),

PreReviewOverall (string, optional),

PreReviewAuthority (string, optional),

PreReviewInsurance (string, optional),

PreReviewSafety (string, optional),

PreReviewOperation (string, optional),

PreReviewOther (string, optional),

ReviewUser (string, optional),

ReviewDate (string, optional),

ReviewReason (string, optional),

ReviewNote (string, optional),

ReviewExpirationDate (string, optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.Certificate {

CertificateID (string, optional),

ProducerName (string, optional),

ProducerAddress (string, optional),

ProducerCity (string, optional),

ProducerState (string, optional),

ProducerZip (string, optional),

ProducerPhone (string, optional),

ProducerFax (string, optional),

ProducerEmail (string, optional),

PaidFor (string, optional),

Coverages (Array\[MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.Coverage\], optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.RiskAssessmentInfraction {

Points (integer, optional),

RuleName (string, optional),

RiskLevel (string, optional),

RuleText (string, optional),

RuleOutput (string, optional),

PreReviewScore (integer, optional),

PreReviewRiskLevel (string, optional),

RuleEnforced (boolean, optional)

}

MyCarrierPacketsBusiness.Services.FMCSACarrierServices.Data.Coverage {

InsurerName (string, optional),

Type (string, optional),

PolicyNumber (string, optional),

ExpirationDate (string, optional),

CoverageLimit (string, optional),

Deductible (string, optional),

ReferBreakdown (string, optional),

ReferBreakDeduct (string, optional),

CancellationDate (string, optional)

}

```
[\
  {\
    "CarrierID": 0,\
    "DotNumber": 0,\
    "DocketNumber": "string",\
    "CompanyName": "string",\
    "DBAName": "string",\
    "Street": "string",\
    "City": "string",\
    "State": "string",\
    "ZipCode": "string",\
    "Country": "string",\
    "Phone": "string",\
    "Status": "string",\
    "StatusDate": "2026-05-17T23:54:51.247Z",\
    "InProcessState": "string",\
    "PossibleFraud": "string",\
    "DoubleBrokering": "string",\
    "IncidentReports": {\
      "TotalIncidentReports": 0,\
      "TotalIncidentReportsWithFraud": 0\
    },\
    "FraudCallNumber": "string",\
    "HasSaferWatchKey": true,\
    "WatchdogReports": "string",\
    "OnCurrentCustomerAgreement": true,\
    "CarrierRating": {\
      "CarrierID": 0,\
      "CustomerID": 0,\
      "CustomerRating": 0,\
      "RatingSum": 0,\
      "TotalRatings": 0,\
      "LowRatings": 0,\
      "TotalRatingPercent": 0,\
      "CustomerRatingPercent": 0,\
      "RatingValue": 0,\
      "RatingValueText": "string",\
      "AvgRatingText": "string",\
      "AvgRatingBasisText": "string",\
      "AvgRatingTextPlusRatingBasisText": "string",\
      "CustomerRatingText": "string",\
      "HasCompletedPacket": true\
    },\
    "RiskAssessment": {\
      "Overall": "string",\
      "Authority": "string",\
      "Insurance": "string",\
      "Safety": "string",\
      "Operation": "string",\
      "Other": "string"\
    },\
    "RiskAssessmentDetails": {\
      "IsIntrastateCarrier": true,\
      "TotalPoints": 0,\
      "OverallRating": "string",\
      "Authority": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Insurance": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Safety": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Operation": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Other": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "ReviewState": "string",\
      "ReviewDetails": {\
        "ReviewID": 0,\
        "PreReviewOverall": "string",\
        "PreReviewAuthority": "string",\
        "PreReviewInsurance": "string",\
        "PreReviewSafety": "string",\
        "PreReviewOperation": "string",\
        "PreReviewOther": "string",\
        "ReviewUser": "string",\
        "ReviewDate": "2026-05-17T23:54:51.247Z",\
        "ReviewReason": "string",\
        "ReviewNote": "string",\
        "ReviewExpirationDate": "2026-05-17T23:54:51.247Z"\
      }\
    },\
    "CertData": {\
      "Status": "string",\
      "Noncoop": true,\
      "Certificates": [\
        {\
          "CertificateID": "string",\
          "ProducerName": "string",\
          "ProducerAddress": "string",\
          "ProducerCity": "string",\
          "ProducerState": "string",\
          "ProducerZip": "string",\
          "ProducerPhone": "string",\
          "ProducerFax": "string",\
          "ProducerEmail": "string",\
          "PaidFor": "string",\
          "Coverages": [\
            {\
              "InsurerName": "string",\
              "Type": "string",\
              "PolicyNumber": "string",\
              "ExpirationDate": "string",\
              "CoverageLimit": "string",\
              "Deductible": "string",\
              "ReferBreakdown": "string",\
              "ReferBreakDeduct": "string",\
              "CancellationDate": "string"\
            }\
          ]\
        }\
      ]\
    },\
    "Emails": [\
      {\
        "EmailType": 1,\
        "Description": "string",\
        "Email": "string"\
      }\
    ],\
    "Source": 0,\
    "IsIntrastateCarrier": true,\
    "IsMonitored": true,\
    "IsBlocked": true,\
    "FreightValidateStatus": "string"\
  }\
]
```

```
<?xml version="1.0"?>
<Inline Model>
  <CarrierID>1</CarrierID>
  <DotNumber>1</DotNumber>
  <DocketNumber>string</DocketNumber>
  <CompanyName>string</CompanyName>
  <DBAName>string</DBAName>
  <Street>string</Street>
  <City>string</City>
  <State>string</State>
  <ZipCode>string</ZipCode>
  <Country>string</Country>
  <Phone>string</Phone>
  <Status>string</Status>
  <StatusDate>1970-01-01T00:00:00.001Z</StatusDate>
  <InProcessState>string</InProcessState>
  <PossibleFraud>string</PossibleFraud>
  <DoubleBrokering>string</DoubleBrokering>
  <IncidentReports>
    <TotalIncidentReports>1</TotalIncidentReports>
    <TotalIncidentReportsWithFraud>1</TotalIncidentReportsWithFraud>
  </IncidentReports>
  <FraudCallNumber>string</FraudCallNumber>
  <HasSaferWatchKey>true</HasSaferWatchKey>
  <WatchdogReports>string</WatchdogReports>
  <OnCurrentCustomerAgreement>true</OnCurrentCustomerAgreement>
  <CarrierRating>
    <CarrierID>1</CarrierID>
    <CustomerID>1</CustomerID>
    <CustomerRating>1</CustomerRating>
    <RatingSum>1</RatingSum>
    <TotalRatings>1</TotalRatings>
    <LowRatings>1</LowRatings>
    <TotalRatingPercent>1</TotalRatingPercent>
    <CustomerRatingPercent>1</CustomerRatingPercent>
    <RatingValue>1.1</RatingValue>
    <RatingValueText>string</RatingValueText>
    <AvgRatingText>string</AvgRatingText>
    <AvgRatingBasisText>string</AvgRatingBasisText>
    <AvgRatingTextPlusRatingBasisText>string</AvgRatingTextPlusRatingBasisText>
    <CustomerRatingText>string</CustomerRatingText>
    <HasCompletedPacket>true</HasCompletedPacket>
  </CarrierRating>
  <RiskAssessment>
    <Overall>string</Overall>
    <Authority>string</Authority>
    <Insurance>string</Insurance>
    <Safety>string</Safety>
    <Operation>string</Operation>
    <Other>string</Other>
  </RiskAssessment>
  <RiskAssessmentDetails>
    <IsIntrastateCarrier>true</IsIntrastateCarrier>
    <TotalPoints>1</TotalPoints>
    <OverallRating>string</OverallRating>
    <Authority>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Authority>
    <Insurance>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Insurance>
    <Safety>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Safety>
    <Operation>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Operation>
    <Other>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Other>
    <ReviewState>string</ReviewState>
    <ReviewDetails>
      <ReviewID>1</ReviewID>
      <PreReviewOverall>string</PreReviewOverall>
      <PreReviewAuthority>string</PreReviewAuthority>
      <PreReviewInsurance>string</PreReviewInsurance>
      <PreReviewSafety>string</PreReviewSafety>
      <PreReviewOperation>string</PreReviewOperation>
      <PreReviewOther>string</PreReviewOther>
      <ReviewUser>string</ReviewUser>
      <ReviewDate>1970-01-01T00:00:00.001Z</ReviewDate>
      <ReviewReason>string</ReviewReason>
      <ReviewNote>string</ReviewNote>
      <ReviewExpirationDate>1970-01-01T00:00:00.001Z</ReviewExpirationDate>
    </ReviewDetails>
  </RiskAssessmentDetails>
  <CertData>
    <Status>string</Status>
    <Noncoop>true</Noncoop>
    <Certificates>
      <CertificateID>string</CertificateID>
      <ProducerName>string</ProducerName>
      <ProducerAddress>string</ProducerAddress>
      <ProducerCity>string</ProducerCity>
      <ProducerState>string</ProducerState>
      <ProducerZip>string</ProducerZip>
      <ProducerPhone>string</ProducerPhone>
      <ProducerFax>string</ProducerFax>
      <ProducerEmail>string</ProducerEmail>
      <PaidFor>string</PaidFor>
      <Coverages>
        <InsurerName>string</InsurerName>
        <Type>string</Type>
        <PolicyNumber>string</PolicyNumber>
        <ExpirationDate>string</ExpirationDate>
        <CoverageLimit>string</CoverageLimit>
        <Deductible>string</Deductible>
        <ReferBreakdown>string</ReferBreakdown>
        <ReferBreakDeduct>string</ReferBreakDeduct>
        <CancellationDate>string</CancellationDate>
      </Coverages>
    </Certificates>
  </CertData>
  <Emails>
    <EmailType>1</EmailType>
    <Description>string</Description>
    <Email>string</Email>
  </Emails>
  <Source>0</Source>
  <IsIntrastateCarrier>true</IsIntrastateCarrier>
  <IsMonitored>true</IsMonitored>
  <IsBlocked>true</IsBlocked>
  <FreightValidateStatus>string</FreightValidateStatus>
</Inline Model>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT number of the carrier. For example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierData)[/api/v1/Carrier/GetCarrierData](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierData)



    - [Retrieves carrier profile data, risk assessment, certdata. **Includes** carrier packet data.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetCarrierData)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.CarrierAADTO {

DOTNumber (integer, optional),

LegalName (string, optional),

DBAName (string, optional),

Address1 (string, optional),

Address2 (string, optional),

City (string, optional),

Zipcode (string, optional),

State (string, optional),

Country (string, optional),

CellPhone (string, optional),

Phone (string, optional),

Fax (string, optional),

FreePhone (string, optional),

EmergencyPhone (string, optional),

Email (string, optional),

FraudIdentityTheftStatus (string, optional),

MCNumber (string, optional),

SCAC (string, optional),

MailingAddress1 (string, optional),

MailingAddress2 (string, optional),

MailingCity (string, optional),

MailingState (string, optional),

MailingZipcode (string, optional),

MailingCountry (string, optional),

AfterHrsWkDaySupportName (string, optional),

AfterHrsWkDaySupportPhone (string, optional),

AfterHrsWkDaySupportFax (string, optional),

AfterHrsWkDaySupportFrom (string, optional),

AfterHrsWkDaySupportTo (string, optional),

AfterHrsWkEndSupportName (string, optional),

AfterHrsWkEndSupportPhone (string, optional),

AfterHrsWkEndSupportFax (string, optional),

AfterHrsWkEndSupportFrom (string, optional),

AfterHrsWkEndSupportTo (string, optional),

Website (string, optional),

OperationManagerName (string, optional),

OnlineAccessToAvailableLoads (boolean, optional),

AvailableLoadsEmail (string, optional),

DriverLogsSafeyDeptManagerName (string, optional),

DriverLogsSafeyDeptManagerPhone (string, optional),

Dispatchers (string, optional),

ClaimsContactName (string, optional),

ClaimsContactPhone (string, optional),

ClaimsContactEmail (string, optional),

DispatchServiceUsed (boolean, optional),

DispatchServiceName (string, optional),

DispatchServicePhone (string, optional),

BrokerOutExtraFreight (boolean, optional),

References1 (string, optional),

References2 (string, optional),

References3 (string, optional),

DriversTrackedBy (string, optional),

AccessOnlineGPSTracking (boolean, optional),

DriversTrackedByOtherMethod (string, optional),

CreatedDateTime (string, optional),

ModifiedDateTime (string, optional),

CarrierCustomerAgreements (Array\[MyCarrierPacketsApi.DTOs.CarrierCustomerAgreementDTO\], optional),

CarrierCustomerPacketStatuses (Array\[MyCarrierPacketsApi.DTOs.CarrierCustomerPacketStatusDTO\], optional),

CarrierCargoHauled (MyCarrierPacketsApi.DTOs.CarrierCargoHauledDTO, optional),

CarrierCompanyClassification (MyCarrierPacketsApi.DTOs.CarrierCompanyClassificationDTO, optional),

CarrierDrivers (Array\[MyCarrierPacketsApi.DTOs.CarrierDriverDTO\], optional),

CarrierDispatchers (Array\[MyCarrierPacketsApi.DTOs.CarrierDispatcherDTO\], optional),

CarrierLane (MyCarrierPacketsApi.DTOs.CarrierLaneDTO, optional),

CarrierOperationalDetail (MyCarrierPacketsApi.DTOs.CarrierOperationalDetailDTO, optional),

CarrierPaymentInfo (MyCarrierPacketsApi.DTOs.CarrierPaymentInfoDTO, optional),

CarrierRemit (MyCarrierPacketsApi.DTOs.CarrierRemitDTO, optional),

FactoringRemit (MyCarrierPacketsApi.DTOs.FactoringRemitDTO, optional),

CarrierBank (MyCarrierPacketsApi.DTOs.CarrierBankDTO, optional),

CarrierPaymentTerms (Array\[MyCarrierPacketsApi.DTOs.CarrierPaymentTermDTO\], optional),

CarrierPaymentTypes (Array\[MyCarrierPacketsApi.DTOs.CarrierPaymentTypeDTO\], optional),

CarrierPayerType (MyCarrierPacketsApi.DTOs.PayerTypeDTO, optional),

CarrierTruckClass (MyCarrierPacketsApi.DTOs.CarrierTruckClassDTO, optional),

CarrierTruckType (MyCarrierPacketsApi.DTOs.CarrierTruckTypeDTO, optional),

CarrierW9Forms (Array\[MyCarrierPacketsApi.DTOs.CarrierW9FormDTO\], optional),

CarrierCertification (MyCarrierPacketsApi.DTOs.CarrierCertificationDTO, optional),

AssureAdvantage (Array\[MyCarrierPacketsApi.FMCSA.FMCSACarrier\], optional),

CarrierMode (MyCarrierPacketsApi.DTOs.CarrierModeDTO, optional),

CarrierELDProvider (MyCarrierPacketsApi.DTOs.CarrierELDProviderDTO, optional),

OwnerContactName (string, optional),

OwnerContactPhone (string, optional),

OwnerContactEmail (string, optional),

CarrierTINMatchings (Array\[MyCarrierPacketsApi.DTOs.CarrierTINMatchingDTO\], optional),

Message (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierCustomerAgreementDTO {

SignatureDate (string, optional),

SignaturePerson (string, optional),

SignaturePersonTitle (string, optional),

SignaturePersonUserName (string, optional),

SignaturePersonEmail (string, optional),

SignaturePersonPhoneNumber (string, optional),

OnCurrentCustomerAgreement (boolean, optional),

CustomerAgreement (MyCarrierPacketsApi.DTOs.CustomerAgreementDTO, optional),

CarrierCustomerAgreementImages (Array\[MyCarrierPacketsApi.DTOs.CarrierCustomerAgreementImageDTO\], optional),

IsActive (boolean, optional),

IPAddress (string, optional),

GeoLocLat (number, optional),

GeoLocLng (number, optional),

GeoLocMethod (string, optional, read only)

}

MyCarrierPacketsApi.DTOs.CarrierCustomerPacketStatusDTO {

Customer (MyCarrierPacketsApi.DTOs.CustomerDTO, optional),

CarrierPacketStatus (string, optional),

CustomerID (integer, optional)

}

MyCarrierPacketsApi.DTOs.CarrierCargoHauledDTO {

GeneralFreight (boolean, optional),

LiquidsGas (boolean, optional),

Chemicals (boolean, optional),

HouseholdGoods (boolean, optional),

IntermodalContainers (boolean, optional),

CommoditiesDryBulk (boolean, optional),

MetalSheetsCoilsRolls (boolean, optional),

Passengers (boolean, optional),

RefrigeratedFood (boolean, optional),

MotorVehicles (boolean, optional),

OilfieldEquipment (boolean, optional),

Beverages (boolean, optional),

DrivewayTowaway (boolean, optional),

LivestockContainers (boolean, optional),

PaperProducts (boolean, optional),

LogsPolesBeamsLumber (boolean, optional),

GrainFeedHay (boolean, optional),

Utility (boolean, optional),

BuildingMaterials (boolean, optional),

CoalCoke (boolean, optional),

FarmSupplies (boolean, optional),

MobileHomes (boolean, optional),

Meat (boolean, optional),

Construction (boolean, optional),

MachineryLargeObjects (boolean, optional),

GarbageRefuseTrash (boolean, optional),

WaterWell (boolean, optional),

FreshProduce (boolean, optional),

USMail (boolean, optional),

Other (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierCompanyClassificationDTO {

AuthForHire (boolean, optional),

Migrant (boolean, optional),

IndianNation (boolean, optional),

ExemptForHire (boolean, optional),

USMail (boolean, optional),

PrivateProperty (boolean, optional),

FederalGovernment (boolean, optional),

PrivPassBusiness (boolean, optional),

StateGovernment (boolean, optional),

PrivPassNonBusiness (boolean, optional),

LocalGovernment (boolean, optional),

WOSB (boolean, optional),

VOSB (boolean, optional),

MBE (boolean, optional),

AsianPacificAmerican (boolean, optional),

SubcontinentAmerican (boolean, optional),

NOB (boolean, optional),

HispanicAmerican (boolean, optional),

AfricanAmerican (boolean, optional),

WBE (boolean, optional),

DBE (boolean, optional),

SBA8a (boolean, optional),

EDWOSB (boolean, optional),

SDVOSB (boolean, optional),

HUBZone (boolean, optional),

LGBTQIA (boolean, optional),

Other (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierDriverDTO {

DriverName (string, optional),

CellPhone (string, optional),

ComCheck (boolean, optional),

FuelAdvance (boolean, optional)

}

MyCarrierPacketsApi.DTOs.CarrierDispatcherDTO {

DispatcherName (string, optional),

PhoneNumber (string, optional),

Email (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierLaneDTO {

UnitedStates (boolean, optional),

Mexico (boolean, optional),

Canada (boolean, optional),

NortheastRegion (boolean, optional),

MidwestRegion (boolean, optional),

SouthRegion (boolean, optional),

WestRegion (boolean, optional),

Alabama (boolean, optional),

Alaska (boolean, optional),

Arizona (boolean, optional),

Arkansas (boolean, optional),

California (boolean, optional),

Colorado (boolean, optional),

Delaware (boolean, optional),

Florida (boolean, optional),

Georgia (boolean, optional),

Hawaii (boolean, optional),

Idaho (boolean, optional),

Illinois (boolean, optional),

Indiana (boolean, optional),

Iowa (boolean, optional),

Kansas (boolean, optional),

Kentucky (boolean, optional),

Louisiana (boolean, optional),

Maine (boolean, optional),

Maryland (boolean, optional),

Massachusetts (boolean, optional),

Michigan (boolean, optional),

Minnesota (boolean, optional),

Mississippi (boolean, optional),

Missouri (boolean, optional),

Montana (boolean, optional),

Nebraska (boolean, optional),

Nevada (boolean, optional),

NewHampshire (boolean, optional),

NewJersey (boolean, optional),

NewMexico (boolean, optional),

NewYork (boolean, optional),

NorthCarolina (boolean, optional),

NorthDakota (boolean, optional),

Ohio (boolean, optional),

Oklahoma (boolean, optional),

Oregon (boolean, optional),

Pennsylvania (boolean, optional),

RhodeIsland (boolean, optional),

SouthCarolina (boolean, optional),

SouthDakota (boolean, optional),

Tennessee (boolean, optional),

Utah (boolean, optional),

Vermont (boolean, optional),

Virginia (boolean, optional),

Washington (boolean, optional),

WashingtonDC (boolean, optional),

WestVirginia (boolean, optional),

Wisconsin (boolean, optional),

Wyoming (boolean, optional),

Connecticut (boolean, optional),

Texas (boolean, optional),

Alberta (boolean, optional),

BritishColumbia (boolean, optional),

Manitoba (boolean, optional),

NewBrunswick (boolean, optional),

NewfoundlandAndLabrador (boolean, optional),

NorthwestTerritories (boolean, optional),

NovaScotia (boolean, optional),

Nunavut (boolean, optional),

Ontario (boolean, optional),

PrinceEdwardIsland (boolean, optional),

Quebec (boolean, optional),

Saskatchewan (boolean, optional),

YukonTerritory (boolean, optional),

Aguascalientes (boolean, optional),

BajaCalifornia (boolean, optional),

BajaCaliforniaNorte (boolean, optional),

BajaCaliforniaSur (boolean, optional),

Chihuahua (boolean, optional),

Colima (boolean, optional),

Campeche (boolean, optional),

Coahuila (boolean, optional),

Chiapas (boolean, optional),

Durango (boolean, optional),

Guerrero (boolean, optional),

Guanajuato (boolean, optional),

Hidalgo (boolean, optional),

Jalisco (boolean, optional),

MexicoCity (boolean, optional),

MexicoState (boolean, optional),

Michoacan (boolean, optional),

Morelos (boolean, optional),

Nayarit (boolean, optional),

NuevoLeon (boolean, optional),

Oaxaca (boolean, optional),

Puebla (boolean, optional),

QuintanaRoo (boolean, optional),

Queretaro (boolean, optional),

Sinaloa (boolean, optional),

SanLuisPotosi (boolean, optional),

Sonora (boolean, optional),

Tabasco (boolean, optional),

Tlaxcala (boolean, optional),

Tamaulipas (boolean, optional),

Veracruz (boolean, optional),

Yucatan (boolean, optional),

Zacatecas (boolean, optional)

}

MyCarrierPacketsApi.DTOs.CarrierOperationalDetailDTO {

FleetSize (integer, optional),

TotalPowerUnits (integer, optional),

NumberOfVehicles (integer, optional),

ReeferEquipment (boolean, optional),

VanEquipment (boolean, optional),

FlatbedStepDeckEquipment (boolean, optional),

OwnedTractors (integer, optional),

OwnedTrucks (integer, optional),

OwnedTrailers (integer, optional),

TermLeasedTractors (integer, optional),

TermLeasedTrucks (integer, optional),

TermLeasedTrailers (integer, optional),

TripLeasedTractors (integer, optional),

TripLeasedTrucks (integer, optional),

TripLeasedTrailers (integer, optional),

InterstateAndIntrastateDrivers (integer, optional),

CDLEmployedDrivers (integer, optional),

MonthlyAverageLeasedDrivers (integer, optional),

InterstateDriversTotal (integer, optional),

InterstateDriversGT100Miles (integer, optional),

InterstateDriversLT100Miles (integer, optional),

IntrastateDriversTotal (integer, optional),

IntrastateDriversGT100Miles (integer, optional),

IntrastateDriversLT100Miles (integer, optional),

PowerOnly (boolean, optional),

SatelliteEquipment (boolean, optional),

TeamDrivers (boolean, optional),

DropTrailer (boolean, optional),

ELDCompliant (boolean, optional),

ELDCompliantBy (string, optional),

ELDIdentifier (string, optional),

NumberOfTractors (integer, optional),

NumberOfVans (integer, optional),

NumberOfReefers (integer, optional),

NumberOfFlats (integer, optional),

NumberOfStepDecks (integer, optional),

NumberOfTanks (integer, optional)

}

MyCarrierPacketsApi.DTOs.CarrierPaymentInfoDTO {

BankRoutingNumber (string, optional),

BankAccountNumber (string, optional),

BankAccountName (string, optional),

BankName (string, optional),

BankAddress (string, optional),

BankPhone (string, optional),

BankFax (string, optional),

FactoringCompanyName (string, optional),

RemitAddress1 (string, optional),

RemitAddress2 (string, optional),

RemitCity (string, optional),

RemitZipCode (string, optional),

BankAccountType (string, optional),

RemitState (string, optional),

RemitCountry (string, optional),

RemitEmail (string, optional),

Require1099 (boolean, optional),

EpayManagerID (integer, optional),

RemitCurrency (string, optional),

PayAdvanceOptionID (integer, optional),

PayAdvanceOptionType (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierRemitDTO {

CarrierRemitEmail (string, optional),

CarrierRemitAddress1 (string, optional),

CarrierRemitAddress2 (string, optional),

CarrierRemitCity (string, optional),

CarrierRemitCountry (string, optional),

CarrierRemitStateProvince (string, optional),

CarrierRemitZipCode (string, optional)

}

MyCarrierPacketsApi.DTOs.FactoringRemitDTO {

FactoringCompanyID (integer, optional),

FactoringCompanyName (string, optional),

FactoringRemitEmail (string, optional),

FactoringRemitAddress (string, optional),

FactoringRemitAddress2 (string, optional),

FactoringRemitCity (string, optional),

FactoringRemitCountry (string, optional),

FactoringRemitStateProvince (string, optional),

FactoringRemitZipcode (string, optional),

FactoringPhone (string, optional),

BankRoutingNumber (string, optional),

BankAccountNumber (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierBankDTO {

CarrierBankRoutingNumber (string, optional),

CarrierBankAccountNumber (string, optional),

CarrierBankAccountName (string, optional),

CarrierBankName (string, optional),

CarrierBankAddress (string, optional),

CarrierBankPhone (string, optional),

CarrierBankFax (string, optional),

CarrierBankAccountType (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierPaymentTermDTO {

PaymentTerm (MyCarrierPacketsApi.DTOs.CustomerPaymentTermDTO, optional)

}

MyCarrierPacketsApi.DTOs.CarrierPaymentTypeDTO {

PaymentType (MyCarrierPacketsApi.DTOs.CustomerPaymentTypeDTO, optional)

}

MyCarrierPacketsApi.DTOs.PayerTypeDTO {

PayerTypeID (integer, optional),

Name (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierTruckClassDTO {

Conestoga (boolean, optional),

Containers (boolean, optional),

DecksSpecialized (boolean, optional),

DecksStandard (boolean, optional),

DryBulk (boolean, optional),

Flatbeds (boolean, optional),

HazardousMaterials (boolean, optional),

Reefers (boolean, optional),

Tankers (boolean, optional),

VansSpecialized (boolean, optional),

VansStandard (boolean, optional),

Other (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierTruckTypeDTO {

AFrameTrailer (boolean, optional),

AFrameTrailerCount (integer, optional),

AcidTanker (boolean, optional),

AcidTankerCount (integer, optional),

AugerTrailer (boolean, optional),

AugerTrailerCount (integer, optional),

AutoCarrier (boolean, optional),

AutoCarrierCount (integer, optional),

BeamTrailer (boolean, optional),

BeamTrailerCount (integer, optional),

BellyDumpTrailer (boolean, optional),

BellyDumpTrailerCount (integer, optional),

BTrain (boolean, optional),

BTrainCount (integer, optional),

BoatTrailer (boolean, optional),

BoatTrailerCount (integer, optional),

Chassis (boolean, optional),

ChassisCount (integer, optional),

ChemicalTankTrailer (boolean, optional),

ChemicalTankTrailerCount (integer, optional),

CompressedGasTanker (boolean, optional),

CompressedGasTankerCount (integer, optional),

Conestoga (boolean, optional),

ConestogaCount (integer, optional),

Container (boolean, optional),

ContainerCount (integer, optional),

ContainerChassisTrailer20Foot (boolean, optional),

ContainerChassisTrailer20FootCount (integer, optional),

ContainerChassisTrailer40Foot (boolean, optional),

ContainerChassisTrailer40FootCount (integer, optional),

ContainerChassisTrailerComboChassis (boolean, optional),

ContainerChassisTrailerComboChassisCount (integer, optional),

ContainerInsulated (boolean, optional),

ContainerInsulatedCount (integer, optional),

ContainerRefrigerated (boolean, optional),

ContainerRefrigeratedCount (integer, optional),

ContainerStandard (boolean, optional),

ContainerStandardCount (integer, optional),

ConvertibleTrailer (boolean, optional),

ConvertibleTrailerCount (integer, optional),

Conveyor (boolean, optional),

ConveyorCount (integer, optional),

CryogenicLiquidTanker (boolean, optional),

CryogenicLiquidTankerCount (integer, optional),

Dolly (boolean, optional),

DollyCount (integer, optional),

DoubleDrop (boolean, optional),

DoubleDropCount (integer, optional),

DropDeckLandoll (boolean, optional),

DropDeckLandollCount (integer, optional),

DryBulkTanker (boolean, optional),

DryBulkTankerCount (integer, optional),

DualLaneTrailer (boolean, optional),

DualLaneTrailerCount (integer, optional),

DumpTrailer (boolean, optional),

DumpTrailerCount (integer, optional),

EightToTenCarHauler (boolean, optional),

EightToTenCarHaulerCount (integer, optional),

EndDumpTrailer (boolean, optional),

EndDumpTrailerCount (integer, optional),

ExtendableFlatbedTrailer (boolean, optional),

ExtendableFlatbedTrailerCount (integer, optional),

FertilizerHopperTrailer (boolean, optional),

FertilizerHopperTrailerCount (integer, optional),

Flatbed (boolean, optional),

FlatbedCount (integer, optional),

FlatbedAirRide (boolean, optional),

FlatbedAirRideCount (integer, optional),

FlatbedConestoga (boolean, optional),

FlatbedConestogaCount (integer, optional),

FlatbedDouble (boolean, optional),

FlatbedDoubleCount (integer, optional),

FlatbedHazMat (boolean, optional),

FlatbedHazMatCount (integer, optional),

FlatbedHotshot (boolean, optional),

FlatbedHotshotCount (integer, optional),

FlatbedMaxi (boolean, optional),

FlatbedMaxiCount (integer, optional),

FlatbedOrStepDeck (boolean, optional),

FlatbedOrStepDeckCount (integer, optional),

FlatbedOverdimension (boolean, optional),

FlatbedOverdimensionCount (integer, optional),

FlatbedSpecialized (boolean, optional),

FlatbedSpecializedCount (integer, optional),

FlatbedWithchains (boolean, optional),

FlatbedWithchainsCount (integer, optional),

FlatbedWithSides (boolean, optional),

FlatbedWithSidesCount (integer, optional),

FlatbedWithTarps (boolean, optional),

FlatbedWithTarpsCount (integer, optional),

FlatbedWithTeam (boolean, optional),

FlatbedWithTeamCount (integer, optional),

FlatbedVanReefer (boolean, optional),

FlatbedVanReeferCount (integer, optional),

FoodGradeTankTrailer (boolean, optional),

FoodGradeTankTrailerCount (integer, optional),

FourToFiveCarHauler (boolean, optional),

FourToFiveCarHaulerCount (integer, optional),

FuelTankTrailer (boolean, optional),

FuelTankTrailerCount (integer, optional),

GasCylinderTrailer (boolean, optional),

GasCylinderTrailerCount (integer, optional),

GrainHopperTrailer (boolean, optional),

GrainHopperTrailerCount (integer, optional),

HazmatTanker (boolean, optional),

HazmatTankerCount (integer, optional),

HopperBottom (boolean, optional),

HopperBottomCount (integer, optional),

HopperHighSide (boolean, optional),

HopperHighSideCount (integer, optional),

HopperLowSide (boolean, optional),

HopperLowSideCount (integer, optional),

HopperTrailer (boolean, optional),

HopperTrailerCount (integer, optional),

HorseTrailer (boolean, optional),

HorseTrailerCount (integer, optional),

HotshotTrailer (boolean, optional),

HotshotTrailerCount (integer, optional),

InsulatedVanOrReefer (boolean, optional),

InsulatedVanOrReeferCount (integer, optional),

Landoll (boolean, optional),

LandollCount (integer, optional),

LivestockTrailer (boolean, optional),

LivestockTrailerCount (integer, optional),

LiveBottomTrailer (boolean, optional),

LiveBottomTrailerCount (integer, optional),

LoggingTrailer (boolean, optional),

LoggingTrailerCount (integer, optional),

Lowboy (boolean, optional),

LowboyCount (integer, optional),

LowboyOrRemGooseneck (boolean, optional),

LowboyOrRemGooseneckCount (integer, optional),

LowboyOverdimension (boolean, optional),

LowboyOverdimensionCount (integer, optional),

MiniDeckTrailer (boolean, optional),

MiniDeckTrailerCount (integer, optional),

MilkTankTrailer (boolean, optional),

MilkTankTrailerCount (integer, optional),

MovingVan (boolean, optional),

MovingVanCount (integer, optional),

MultiAxleHeavyHaulTrailer (boolean, optional),

MultiAxleHeavyHaulTrailerCount (integer, optional),

MultiLevelCarHauler (boolean, optional),

MultiLevelCarHaulerCount (integer, optional),

OneToTwoCarHauler (boolean, optional),

OneToTwoCarHaulerCount (integer, optional),

PerimeterTrailer (boolean, optional),

PerimeterTrailerCount (integer, optional),

PintleHitch (boolean, optional),

PintleHitchCount (integer, optional),

PintleHitchTrailer (boolean, optional),

PintleHitchTrailerCount (integer, optional),

PoleTrailer (boolean, optional),

PoleTrailerCount (integer, optional),

Pneumatic (boolean, optional),

PneumaticCount (integer, optional),

PowerOnly (boolean, optional),

PowerOnlyCount (integer, optional),

Reefer (boolean, optional),

ReeferCount (integer, optional),

ReeferAirRide (boolean, optional),

ReeferAirRideCount (integer, optional),

ReeferDouble (boolean, optional),

ReeferDoubleCount (integer, optional),

ReeferHazMat (boolean, optional),

ReeferHazMatCount (integer, optional),

ReeferIntermodal (boolean, optional),

ReeferIntermodalCount (integer, optional),

ReeferLogistics (boolean, optional),

ReeferLogisticsCount (integer, optional),

ReeferOrVentedVan (boolean, optional),

ReeferOrVentedVanCount (integer, optional),

ReeferPalletExchange (boolean, optional),

ReeferPalletExchangeCount (integer, optional),

ReeferSpecialized (boolean, optional),

ReeferSpecializedCount (integer, optional),

ReeferStandard48Foot (boolean, optional),

ReeferStandard48FootCount (integer, optional),

ReeferStandard53Foot (boolean, optional),

ReeferStandard53FootCount (integer, optional),

ReeferWithTeam (boolean, optional),

ReeferWithTeamCount (integer, optional),

RemovableGooseneck (boolean, optional),

RemovableGooseneckCount (integer, optional),

SideDumpTrailer (boolean, optional),

SideDumpTrailerCount (integer, optional),

SingleLevelCarHauler (boolean, optional),

SingleLevelCarHaulerCount (integer, optional),

SixToSevenCarHauler (boolean, optional),

SixToSevenCarHaulerCount (integer, optional),

StandardFlatbed48Foot (boolean, optional),

StandardFlatbed48FootCount (integer, optional),

StandardFlatbed53Foot (boolean, optional),

StandardFlatbed53FootCount (integer, optional),

SteerableStepDeckStretch (boolean, optional),

SteerableStepDeckStretchCount (integer, optional),

StepDeck (boolean, optional),

StepDeckCount (integer, optional),

StepDeckOrRemGooseneck (boolean, optional),

StepDeckOrRemGooseneckCount (integer, optional),

StepDeckSpecialized (boolean, optional),

StepDeckSpecializedCount (integer, optional),

StepDeckStandard48Foot (boolean, optional),

StepDeckStandard48FootCount (integer, optional),

StepDeckStandard53Foot (boolean, optional),

StepDeckStandard53FootCount (integer, optional),

StepdeckConestoga (boolean, optional),

StepdeckConestogaCount (integer, optional),

StraightBoxTruck (boolean, optional),

StraightBoxTruckCount (integer, optional),

StretchFlatbed (boolean, optional),

StretchFlatbedCount (integer, optional),

StretchRGN (boolean, optional),

StretchRGNCount (integer, optional),

StretchStepDeck (boolean, optional),

StretchStepDeckCount (integer, optional),

StretchTrailer (boolean, optional),

StretchTrailerCount (integer, optional),

TankerAluminum (boolean, optional),

TankerAluminumCount (integer, optional),

TankerIntermodal (boolean, optional),

TankerIntermodalCount (integer, optional),

TankerSteel (boolean, optional),

TankerSteelCount (integer, optional),

ThreeCarHauler (boolean, optional),

ThreeCarHaulerCount (integer, optional),

TinWideTrailer (boolean, optional),

TinWideTrailerCount (integer, optional),

Toter (boolean, optional),

ToterCount (integer, optional),

TruckAndTrailer (boolean, optional),

TruckAndTrailerCount (integer, optional),

Van (boolean, optional),

VanCount (integer, optional),

VanAirRide (boolean, optional),

VanAirRideCount (integer, optional),

VanBlanketWrap (boolean, optional),

VanBlanketWrapCount (integer, optional),

VanConestoga (boolean, optional),

VanConestogaCount (integer, optional),

VanDouble (boolean, optional),

VanDoubleCount (integer, optional),

VanHazMat (boolean, optional),

VanHazMatCount (integer, optional),

VanHeated (boolean, optional),

VanHeatedCount (integer, optional),

VanHotshot (boolean, optional),

VanHotshotCount (integer, optional),

VanInsulated (boolean, optional),

VanInsulatedCount (integer, optional),

VanIntermodal (boolean, optional),

VanIntermodalCount (integer, optional),

VanLiftGate (boolean, optional),

VanLiftGateCount (integer, optional),

VanLogistics (boolean, optional),

VanLogisticsCount (integer, optional),

VanOpenTop (boolean, optional),

VanOpenTopCount (integer, optional),

VanOrFlatbed (boolean, optional),

VanOrFlatbedCount (integer, optional),

VanOrFlatbedwTarps (boolean, optional),

VanOrFlatbedwTarpsCount (integer, optional),

VanOrReefer (boolean, optional),

VanOrReeferCount (integer, optional),

VanPalletExchange (boolean, optional),

VanPalletExchangeCount (integer, optional),

VanRollerBed (boolean, optional),

VanRollerBedCount (integer, optional),

VanSpecialized (boolean, optional),

VanSpecializedCount (integer, optional),

VanSprinter (boolean, optional),

VanSprinterCount (integer, optional),

VanStandard (boolean, optional),

VanStandardCount (integer, optional),

VanTriple (boolean, optional),

VanTripleCount (integer, optional),

VanVented (boolean, optional),

VanVentedCount (integer, optional),

VanWithCurtains (boolean, optional),

VanWithCurtainsCount (integer, optional),

VanWithTeam (boolean, optional),

VanWithTeamCount (integer, optional),

WalkingFloorTrailer (boolean, optional),

WalkingFloorTrailerCount (integer, optional)

}

MyCarrierPacketsApi.DTOs.CarrierW9FormDTO {

FullName (string, optional),

BusinessName (string, optional),

IndividualOrSingleMemberLLC (boolean, optional),

CCorporation (boolean, optional),

SCorporation (boolean, optional),

Partnership (boolean, optional),

RequesterNameAddress (string, optional),

TrustOrEstate (boolean, optional),

LimitedLiabilityCompany (boolean, optional),

TaxClassification (string, optional),

Other (boolean, optional),

OtherDetail (string, optional),

ExemptPayeeCode (string, optional),

ExemptionFATCACode (string, optional),

Address (string, optional),

CityStateZipCode (string, optional),

ListAccountNumber (string, optional),

SSN (string, optional),

EIN (string, optional),

SignatureDate (string, optional),

SignaturePerson (string, optional),

IsActive (boolean, optional),

City (string, optional),

State (string, optional),

ZipCode (string, optional),

CarrierW9FormImages (Array\[MyCarrierPacketsApi.DTOs.CarrierW9FormImageDTO\], optional)

}

MyCarrierPacketsApi.DTOs.CarrierCertificationDTO {

Hazmat (boolean, optional),

HazmatNumber (string, optional),

SmartWay (boolean, optional),

CARB (boolean, optional),

TWIC (boolean, optional),

CTPATCertified (boolean, optional),

CTPATSVINumber (string, optional),

TankerEndorsed (boolean, optional),

TankerEndorsedNumOfDrivers (integer, optional),

CBP (boolean, optional),

CBSA (boolean, optional),

ANAM (boolean, optional),

ACE (boolean, optional),

ACI (boolean, optional),

CSA (boolean, optional),

FAST (boolean, optional),

PIP (boolean, optional)

}

MyCarrierPacketsApi.FMCSA.FMCSACarrier {

CarrierDetails (MyCarrierPacketsApi.FMCSA.CarrierDetails, optional),

ResponseDO (MyCarrierPacketsApi.DTOs.ResponseDO, optional)

}

MyCarrierPacketsApi.DTOs.CarrierModeDTO {

LessThanTruckLoad (boolean, optional),

Partial (boolean, optional),

Truckload (boolean, optional),

Rail (boolean, optional),

Intermodal (boolean, optional),

Air (boolean, optional),

Expedite (boolean, optional),

Ocean (boolean, optional),

Drayage (boolean, optional)

}

MyCarrierPacketsApi.DTOs.CarrierELDProviderDTO {

ComplianceStatusID (integer, optional),

ComplianceStatus (string, optional),

ProviderName (string, optional),

ProviderIdentifier (string, optional),

ExemptionID (integer, optional),

Exemption (string, optional),

CompliantBy (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierTINMatchingDTO {

TINTypeID (integer, optional),

TIN (string, optional),

TINName (string, optional),

TINMatchingStatusID (integer, optional),

TINMatchingResultID (integer, optional),

CreatedOnUtc (string, optional),

SubmittedOnUtc (string, optional),

ProcessedOnUtc (string, optional),

ContactEmail (string, optional),

ContactPhoneNumber (string, optional),

MatchingResult (string, optional),

MatchingStatus (string, optional)

}

MyCarrierPacketsApi.DTOs.CustomerAgreementDTO {

AgreementName (string, optional),

CreatedDate (string, optional),

CreatedBy (string, optional),

BlobName (string, optional),

Customer (MyCarrierPacketsApi.DTOs.CustomerDTO, optional)

}

MyCarrierPacketsApi.DTOs.CarrierCustomerAgreementImageDTO {

BlobName (string, optional),

CreatedDate (string, optional)

}

MyCarrierPacketsApi.DTOs.CustomerDTO {

CustomerID (integer, optional),

Title (string, optional),

FirstName (string, optional),

MiddleName (string, optional),

LastName (string, optional),

CompanyName (string, optional),

TypeCompany (string, optional),

CellPhone (string, optional),

Phone (string, optional),

Fax (string, optional),

Address1 (string, optional),

Address2 (string, optional),

Apartment (string, optional),

City (string, optional),

State (string, optional),

Zipcode (string, optional),

Country (string, optional),

CustomerKey (string, optional),

PacketCompletionNotificationType (integer, optional),

PacketCompletionNotificationEmail (string, optional)

}

MyCarrierPacketsApi.DTOs.CustomerPaymentTermDTO {

PaymentTermID (integer, optional),

Days (integer, optional),

Term (string, optional),

QuickPay (boolean, optional),

PaymentFeeType (string, optional),

PaymentFeeAmount (number, optional),

CustomerID (integer, optional)

}

MyCarrierPacketsApi.DTOs.CustomerPaymentTypeDTO {

PaymentTypeID (integer, optional),

Type (string, optional),

CustomerID (integer, optional),

PaymentType (MyCarrierPacketsApi.DTOs.PaymentTypeDTO, optional)

}

MyCarrierPacketsApi.DTOs.CarrierW9FormImageDTO {

BlobName (string, optional),

CreatedDate (string, optional),

FileName (string, optional),

CreatedBy (string, optional)

}

MyCarrierPacketsApi.FMCSA.CarrierDetails {

docketNumber (string, optional),

dotNumber (MyCarrierPacketsApi.FMCSA.DotNumber, optional),

carrierType (string, optional),

isMonitored (boolean, optional),

isBlocked (boolean, optional),

Identity (MyCarrierPacketsApi.FMCSA.Identity, optional),

Authority (MyCarrierPacketsApi.FMCSA.Authority, optional),

FMCSAInsurance (MyCarrierPacketsApi.FMCSA.FMCSAInsurance, optional),

CertData (MyCarrierPacketsApi.FMCSA.CertData, optional),

Safety (MyCarrierPacketsApi.FMCSA.Safety, optional),

Inspection (MyCarrierPacketsApi.FMCSA.Inspection, optional),

Crash (MyCarrierPacketsApi.FMCSA.Crash, optional),

Review (MyCarrierPacketsApi.FMCSA.Review, optional),

Operation (MyCarrierPacketsApi.FMCSA.Operation, optional),

Cargo (MyCarrierPacketsApi.FMCSA.Cargo, optional),

Drivers (MyCarrierPacketsApi.FMCSA.Drivers, optional),

Equipment (MyCarrierPacketsApi.FMCSA.Equipment, optional),

Other (MyCarrierPacketsApi.FMCSA.Other, optional),

RiskAssessment (MyCarrierPacketsApi.FMCSA.RiskAssessment, optional),

RiskAssessmentDetails (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails, optional),

CarrierRatings (MyCarrierPacketsApi.FMCSA.CarrierRatings, optional),

LatestInvitation (MyCarrierPacketsApi.FMCSA.LatestInvitation, optional),

IncidentReports (MyCarrierPacketsApi.FMCSA.IncidentReports, optional)

}

MyCarrierPacketsApi.DTOs.ResponseDO {

status (string, optional),

action (string, optional),

code (string, optional),

displayMsg (string, optional),

techMsg (string, optional)

}

MyCarrierPacketsApi.DTOs.PaymentTypeDTO {

Name (string, optional)

}

MyCarrierPacketsApi.FMCSA.DotNumber {

status (string, optional),

Value (string, optional)

}

MyCarrierPacketsApi.FMCSA.Identity {

legalName (string, optional),

dbaName (string, optional),

businessStreet (string, optional),

businessCity (string, optional),

businessState (string, optional),

businessZipCode (string, optional),

businessColonia (string, optional),

businessCountry (string, optional),

businessPhone (string, optional),

businessFax (string, optional),

mailingStreet (string, optional),

mailingCity (string, optional),

mailingState (string, optional),

mailingZipCode (string, optional),

mailingColonia (string, optional),

mailingCountry (string, optional),

mailingPhone (string, optional),

mailingFax (string, optional),

undeliverableMail (string, optional),

companyRep1 (string, optional),

companyRep2 (string, optional),

cellPhone (string, optional),

emailAddress (string, optional),

dunBradstreetNum (string, optional),

organization (string, optional)

}

MyCarrierPacketsApi.FMCSA.Authority {

authGrantDate (string, optional),

commonAuthority (string, optional),

commonAuthorityPending (string, optional),

commonAuthorityRevocation (string, optional),

contractAuthority (string, optional),

contractAuthorityPending (string, optional),

contractAuthorityRevocation (string, optional),

brokerAuthority (string, optional),

brokerAuthorityPending (string, optional),

brokerAuthorityRevocation (string, optional),

freight (string, optional),

passenger (string, optional),

householdGoods (string, optional),

private (string, optional),

enterprise (string, optional)

}

MyCarrierPacketsApi.FMCSA.FMCSAInsurance {

bipdRequired (string, optional),

bipdOnFile (string, optional),

cargoRequired (string, optional),

cargoOnFile (string, optional),

bondSuretyRequired (string, optional),

bondSuretyOnFile (string, optional),

PolicyList (Array\[MyCarrierPacketsApi.DTOs.PolicyOutput\], optional)

}

MyCarrierPacketsApi.FMCSA.CertData {

status (string, optional),

noncoop (boolean, optional),

Certificate (Array\[MyCarrierPacketsApi.DTOs.CertificateDTO\], optional)

}

MyCarrierPacketsApi.FMCSA.Safety {

rating (string, optional),

ratingDate (string, optional),

unsafeDrvPCT (string, optional),

unsafeDrvOT (string, optional),

unsafeDrvSV (string, optional),

unsafeDrvAlert (string, optional),

unsafeDrvTrend (string, optional),

unsafeDrvCNT (integer, optional),

hosPCT (string, optional),

hosOT (string, optional),

hosSV (string, optional),

hosAlert (string, optional),

hosTrend (string, optional),

hosCNT (integer, optional),

drvFitPCT (string, optional),

drvFitOT (string, optional),

drvFitSV (string, optional),

drvFitAlert (string, optional),

drvFitTrend (string, optional),

drvFitCNT (integer, optional),

controlSubPCT (string, optional),

controlSubOT (string, optional),

controlSubSV (string, optional),

controlSubAlert (string, optional),

controlSubTrend (string, optional),

controlSubCNT (integer, optional),

vehMaintPCT (string, optional),

vehMaintOT (string, optional),

vehMaintSV (string, optional),

vehMaintAlert (string, optional),

vehMaintTrend (string, optional),

vehMaintCNT (integer, optional),

hazMatPCT (string, optional),

hazMatOT (string, optional),

hazMatSV (string, optional),

hazMatAlert (string, optional),

hazMatTrend (string, optional),

hazMatCNT (integer, optional)

}

MyCarrierPacketsApi.FMCSA.Inspection {

inspectVehUS (string, optional),

inspectVehOOSUS (string, optional),

inspectVehOOSPctUS (string, optional),

inspectDrvUS (string, optional),

inspectDrvOOSUS (string, optional),

inspectDrvOOSPctUS (string, optional),

inspectHazUS (string, optional),

inspectHazOOSUS (string, optional),

inspectHazOOSPctUS (string, optional),

inspectIEPUS (string, optional),

inspectIEPOOSUS (string, optional),

inspectIEPOOSPctUS (string, optional),

inspectTotalIEPUS (string, optional),

inspectTotalUS (string, optional),

inspectVehCAN (string, optional),

inspectVehOOSCAN (string, optional),

inspectVehOOSPctCAN (string, optional),

inspectDrvCAN (string, optional),

inspectDrvOOSCAN (string, optional),

inspectDrvOOSPctCAN (string, optional),

inspectTotalCAN (string, optional)

}

MyCarrierPacketsApi.FMCSA.Crash {

crashFatalUS (string, optional),

crashInjuryUS (string, optional),

crashTowUS (string, optional),

crashTotalUS (string, optional),

crashFatalCAN (string, optional),

crashInjuryCAN (string, optional),

crashTowCAN (string, optional),

crashTotalCAN (string, optional)

}

MyCarrierPacketsApi.FMCSA.Review {

reviewType (string, optional),

reviewDate (string, optional),

reviewDocNum (string, optional),

reviewMiles (string, optional),

mcs150Date (string, optional),

mcs150MileYear (string, optional),

mcs150Miles (string, optional),

accidentRate (string, optional),

accidentRatePrevent (string, optional)

}

MyCarrierPacketsApi.FMCSA.Operation {

dotAddDate (string, optional),

carrierOperation (string, optional),

shipperOperation (string, optional),

mxOperationType (string, optional),

mxRFCNumber (string, optional),

outOfService (string, optional),

outOfServiceDate (string, optional),

outOfServiceReason (string, optional),

entityCarrier (string, optional),

entityShipper (string, optional),

entityBroker (string, optional),

entityFreightFowarder (string, optional),

entityCargoTank (string, optional),

classAuthForHire (string, optional),

classMigrant (string, optional),

classIndianNation (string, optional),

classExemptForHire (string, optional),

classUSMail (string, optional),

classPrivateProperty (string, optional),

classFederalGovernment (string, optional),

classPrivPassBusiness (string, optional),

classStateGovernment (string, optional),

classPrivPassNonBusiness (string, optional),

classLocalGovernment (string, optional),

classOther (string, optional),

operatingStatus (string, optional)

}

MyCarrierPacketsApi.FMCSA.Cargo {

hazmatIndicator (string, optional),

cargoGenFreight (string, optional),

cargoHousehold (string, optional),

cargoMetal (string, optional),

cargoMotorVeh (string, optional),

cargoDriveTow (string, optional),

cargoLogPole (string, optional),

cargoBldgMaterial (string, optional),

cargoMobileHome (string, optional),

cargoMachLarge (string, optional),

cargoProduce (string, optional),

cargoLiqGas (string, optional),

cargoIntermodal (string, optional),

cargoPassengers (string, optional),

cargoOilfield (string, optional),

cargoLivestock (string, optional),

cargoGrainfeed (string, optional),

cargoCoalcoke (string, optional),

cargoMeat (string, optional),

cargoGarbage (string, optional),

cargoUSMail (string, optional),

cargoChemicals (string, optional),

cargoDryBulk (string, optional),

cargoRefrigerated (string, optional),

cargoBeverages (string, optional),

cargoPaperProd (string, optional),

cargoUtilities (string, optional),

cargoFarmSupplies (string, optional),

cargoConstruction (string, optional),

cargoWaterwell (string, optional),

cargoOther (string, optional),

cargoOtherDesc (string, optional)

}

MyCarrierPacketsApi.FMCSA.Drivers {

driversTotal (string, optional),

driversAvgLeased (string, optional),

driversCDL (string, optional),

driversInter (string, optional),

driversInterLT100 (string, optional),

driversInterGT100 (string, optional),

driversIntra (string, optional),

driversIntraLT100 (string, optional),

driversIntraGT100 (string, optional)

}

MyCarrierPacketsApi.FMCSA.Equipment {

trucksTotal (string, optional),

totalPower (string, optional),

fleetsize (string, optional),

trucksOwned (string, optional),

trucksTerm (string, optional),

trucksTrip (string, optional),

trailersOwned (string, optional),

trailersTerm (string, optional),

trailersTrip (string, optional),

tractorsOwned (string, optional),

tractorsTerm (string, optional),

tractorsTrip (string, optional)

}

MyCarrierPacketsApi.FMCSA.Other {

carbTru (string, optional),

smartway (string, optional),

watchdogReports (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessment {

Overall (string, optional),

Authority (string, optional),

Insurance (string, optional),

Safety (string, optional),

Operation (string, optional),

Other (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails {

IsIntrastateCarrier (boolean, optional),

TotalPoints (integer, optional),

OverallRating (string, optional),

ReviewState (string, optional),

Authority (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Insurance (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Safety (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Operation (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Other (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

ReviewDetails (MyCarrierPacketsRiskAssessmentModels.ReviewDetails, optional)

}

MyCarrierPacketsApi.FMCSA.CarrierRatings {

myRating (integer, optional),

totalRatings (integer, optional),

lowRatings (integer, optional),

avgRating (number, optional)

}

MyCarrierPacketsApi.FMCSA.LatestInvitation {

InvitedByUserName (string, optional),

InvitedByEmail (string, optional),

InvitedByFirstName (string, optional),

InvitedByLastName (string, optional),

InvitationSentDate (string, optional),

InvitationRecipient (string, optional)

}

MyCarrierPacketsApi.FMCSA.IncidentReports {

TotalIncidentReports (integer, optional),

TotalIncidentReportsWithFraud (integer, optional)

}

MyCarrierPacketsApi.DTOs.PolicyOutput {

companyName (string, optional),

attnToName (string, optional),

address (string, optional),

city (string, optional),

stateCode (string, optional),

postalCode (string, optional),

countryCode (string, optional),

phone (string, optional),

fax (string, optional),

insuranceType (string, optional),

policyNumber (string, optional),

postedDate (string, optional),

effectiveDate (string, optional),

cancelationDate (string, optional),

coverageFrom (string, optional),

coverageTo (string, optional),

amBestRating (string, optional)

}

MyCarrierPacketsApi.DTOs.CertificateDTO {

certificateID (string, optional),

producerName (string, optional),

producerAddress (string, optional),

producerCity (string, optional),

producerState (string, optional),

producerZip (string, optional),

producerPhone (string, optional),

producerFax (string, optional),

producerEmail (string, optional),

paidFor (string, optional),

BlobName (string, optional),

Coverage (Array\[MyCarrierPacketsApi.DTOs.CoverageDTO\], optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail {

TotalPoints (integer, optional),

OverallRating (string, optional),

HasRuleOverride (boolean, optional, read only),

Infractions (Array\[MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction\], optional)

}

MyCarrierPacketsRiskAssessmentModels.ReviewDetails {

ReviewID (integer, optional),

PreReviewOverall (string, optional),

PreReviewAuthority (string, optional),

PreReviewInsurance (string, optional),

PreReviewSafety (string, optional),

PreReviewOperation (string, optional),

PreReviewOther (string, optional),

ReviewUser (string, optional),

ReviewDate (string, optional),

ReviewReason (string, optional),

ReviewNote (string, optional),

ReviewExpirationDate (string, optional)

}

MyCarrierPacketsApi.DTOs.CoverageDTO {

insurerName (string, optional),

insurerAMBestRating (string, optional),

type (string, optional),

policyNumber (string, optional),

expirationDate (string, optional),

coverageLimit (string, optional),

deductable (string, optional),

referBreakdown (string, optional),

referBreakDeduct (string, optional),

cancellationDate (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction {

Points (integer, optional),

RuleName (string, optional),

RiskLevel (string, optional),

RuleText (string, optional),

RuleOutput (string, optional),

PreReviewScore (integer, optional),

PreReviewRiskLevel (string, optional),

RuleEnforced (boolean, optional)

}

```
{
  "DOTNumber": 0,
  "LegalName": "string",
  "DBAName": "string",
  "Address1": "string",
  "Address2": "string",
  "City": "string",
  "Zipcode": "string",
  "State": "string",
  "Country": "string",
  "CellPhone": "string",
  "Phone": "string",
  "Fax": "string",
  "FreePhone": "string",
  "EmergencyPhone": "string",
  "Email": "string",
  "FraudIdentityTheftStatus": "string",
  "MCNumber": "string",
  "SCAC": "string",
  "MailingAddress1": "string",
  "MailingAddress2": "string",
  "MailingCity": "string",
  "MailingState": "string",
  "MailingZipcode": "string",
  "MailingCountry": "string",
  "AfterHrsWkDaySupportName": "string",
  "AfterHrsWkDaySupportPhone": "string",
  "AfterHrsWkDaySupportFax": "string",
  "AfterHrsWkDaySupportFrom": "string",
  "AfterHrsWkDaySupportTo": "string",
  "AfterHrsWkEndSupportName": "string",
  "AfterHrsWkEndSupportPhone": "string",
  "AfterHrsWkEndSupportFax": "string",
  "AfterHrsWkEndSupportFrom": "string",
  "AfterHrsWkEndSupportTo": "string",
  "Website": "string",
  "OperationManagerName": "string",
  "OnlineAccessToAvailableLoads": true,
  "AvailableLoadsEmail": "string",
  "DriverLogsSafeyDeptManagerName": "string",
  "DriverLogsSafeyDeptManagerPhone": "string",
  "Dispatchers": "string",
  "ClaimsContactName": "string",
  "ClaimsContactPhone": "string",
  "ClaimsContactEmail": "string",
  "DispatchServiceUsed": true,
  "DispatchServiceName": "string",
  "DispatchServicePhone": "string",
  "BrokerOutExtraFreight": true,
  "References1": "string",
  "References2": "string",
  "References3": "string",
  "DriversTrackedBy": "string",
  "AccessOnlineGPSTracking": true,
  "DriversTrackedByOtherMethod": "string",
  "CreatedDateTime": "2026-05-17T23:54:51.262Z",
  "ModifiedDateTime": "2026-05-17T23:54:51.262Z",
  "CarrierCustomerAgreements": [\
    {\
      "SignatureDate": "2026-05-17T23:54:51.262Z",\
      "SignaturePerson": "string",\
      "SignaturePersonTitle": "string",\
      "SignaturePersonUserName": "string",\
      "SignaturePersonEmail": "string",\
      "SignaturePersonPhoneNumber": "string",\
      "OnCurrentCustomerAgreement": true,\
      "CustomerAgreement": {\
        "AgreementName": "string",\
        "CreatedDate": "2026-05-17T23:54:51.262Z",\
        "CreatedBy": "string",\
        "BlobName": "string",\
        "Customer": {\
          "CustomerID": 0,\
          "Title": "string",\
          "FirstName": "string",\
          "MiddleName": "string",\
          "LastName": "string",\
          "CompanyName": "string",\
          "TypeCompany": "string",\
          "CellPhone": "string",\
          "Phone": "string",\
          "Fax": "string",\
          "Address1": "string",\
          "Address2": "string",\
          "Apartment": "string",\
          "City": "string",\
          "State": "string",\
          "Zipcode": "string",\
          "Country": "string",\
          "CustomerKey": "string",\
          "PacketCompletionNotificationType": 0,\
          "PacketCompletionNotificationEmail": "string"\
        }\
      },\
      "CarrierCustomerAgreementImages": [\
        {\
          "BlobName": "string",\
          "CreatedDate": "2026-05-17T23:54:51.262Z"\
        }\
      ],\
      "IsActive": true,\
      "IPAddress": "string",\
      "GeoLocLat": 0,\
      "GeoLocLng": 0,\
      "GeoLocMethod": "string"\
    }\
  ],
  "CarrierCustomerPacketStatuses": [\
    {\
      "Customer": {\
        "CustomerID": 0,\
        "Title": "string",\
        "FirstName": "string",\
        "MiddleName": "string",\
        "LastName": "string",\
        "CompanyName": "string",\
        "TypeCompany": "string",\
        "CellPhone": "string",\
        "Phone": "string",\
        "Fax": "string",\
        "Address1": "string",\
        "Address2": "string",\
        "Apartment": "string",\
        "City": "string",\
        "State": "string",\
        "Zipcode": "string",\
        "Country": "string",\
        "CustomerKey": "string",\
        "PacketCompletionNotificationType": 0,\
        "PacketCompletionNotificationEmail": "string"\
      },\
      "CarrierPacketStatus": "string",\
      "CustomerID": 0\
    }\
  ],
  "CarrierCargoHauled": {
    "GeneralFreight": true,
    "LiquidsGas": true,
    "Chemicals": true,
    "HouseholdGoods": true,
    "IntermodalContainers": true,
    "CommoditiesDryBulk": true,
    "MetalSheetsCoilsRolls": true,
    "Passengers": true,
    "RefrigeratedFood": true,
    "MotorVehicles": true,
    "OilfieldEquipment": true,
    "Beverages": true,
    "DrivewayTowaway": true,
    "LivestockContainers": true,
    "PaperProducts": true,
    "LogsPolesBeamsLumber": true,
    "GrainFeedHay": true,
    "Utility": true,
    "BuildingMaterials": true,
    "CoalCoke": true,
    "FarmSupplies": true,
    "MobileHomes": true,
    "Meat": true,
    "Construction": true,
    "MachineryLargeObjects": true,
    "GarbageRefuseTrash": true,
    "WaterWell": true,
    "FreshProduce": true,
    "USMail": true,
    "Other": "string"
  },
  "CarrierCompanyClassification": {
    "AuthForHire": true,
    "Migrant": true,
    "IndianNation": true,
    "ExemptForHire": true,
    "USMail": true,
    "PrivateProperty": true,
    "FederalGovernment": true,
    "PrivPassBusiness": true,
    "StateGovernment": true,
    "PrivPassNonBusiness": true,
    "LocalGovernment": true,
    "WOSB": true,
    "VOSB": true,
    "MBE": true,
    "AsianPacificAmerican": true,
    "SubcontinentAmerican": true,
    "NOB": true,
    "HispanicAmerican": true,
    "AfricanAmerican": true,
    "WBE": true,
    "DBE": true,
    "SBA8a": true,
    "EDWOSB": true,
    "SDVOSB": true,
    "HUBZone": true,
    "LGBTQIA": true,
    "Other": "string"
  },
  "CarrierDrivers": [\
    {\
      "DriverName": "string",\
      "CellPhone": "string",\
      "ComCheck": true,\
      "FuelAdvance": true\
    }\
  ],
  "CarrierDispatchers": [\
    {\
      "DispatcherName": "string",\
      "PhoneNumber": "string",\
      "Email": "string"\
    }\
  ],
  "CarrierLane": {
    "UnitedStates": true,
    "Mexico": true,
    "Canada": true,
    "NortheastRegion": true,
    "MidwestRegion": true,
    "SouthRegion": true,
    "WestRegion": true,
    "Alabama": true,
    "Alaska": true,
    "Arizona": true,
    "Arkansas": true,
    "California": true,
    "Colorado": true,
    "Delaware": true,
    "Florida": true,
    "Georgia": true,
    "Hawaii": true,
    "Idaho": true,
    "Illinois": true,
    "Indiana": true,
    "Iowa": true,
    "Kansas": true,
    "Kentucky": true,
    "Louisiana": true,
    "Maine": true,
    "Maryland": true,
    "Massachusetts": true,
    "Michigan": true,
    "Minnesota": true,
    "Mississippi": true,
    "Missouri": true,
    "Montana": true,
    "Nebraska": true,
    "Nevada": true,
    "NewHampshire": true,
    "NewJersey": true,
    "NewMexico": true,
    "NewYork": true,
    "NorthCarolina": true,
    "NorthDakota": true,
    "Ohio": true,
    "Oklahoma": true,
    "Oregon": true,
    "Pennsylvania": true,
    "RhodeIsland": true,
    "SouthCarolina": true,
    "SouthDakota": true,
    "Tennessee": true,
    "Utah": true,
    "Vermont": true,
    "Virginia": true,
    "Washington": true,
    "WashingtonDC": true,
    "WestVirginia": true,
    "Wisconsin": true,
    "Wyoming": true,
    "Connecticut": true,
    "Texas": true,
    "Alberta": true,
    "BritishColumbia": true,
    "Manitoba": true,
    "NewBrunswick": true,
    "NewfoundlandAndLabrador": true,
    "NorthwestTerritories": true,
    "NovaScotia": true,
    "Nunavut": true,
    "Ontario": true,
    "PrinceEdwardIsland": true,
    "Quebec": true,
    "Saskatchewan": true,
    "YukonTerritory": true,
    "Aguascalientes": true,
    "BajaCalifornia": true,
    "BajaCaliforniaNorte": true,
    "BajaCaliforniaSur": true,
    "Chihuahua": true,
    "Colima": true,
    "Campeche": true,
    "Coahuila": true,
    "Chiapas": true,
    "Durango": true,
    "Guerrero": true,
    "Guanajuato": true,
    "Hidalgo": true,
    "Jalisco": true,
    "MexicoCity": true,
    "MexicoState": true,
    "Michoacan": true,
    "Morelos": true,
    "Nayarit": true,
    "NuevoLeon": true,
    "Oaxaca": true,
    "Puebla": true,
    "QuintanaRoo": true,
    "Queretaro": true,
    "Sinaloa": true,
    "SanLuisPotosi": true,
    "Sonora": true,
    "Tabasco": true,
    "Tlaxcala": true,
    "Tamaulipas": true,
    "Veracruz": true,
    "Yucatan": true,
    "Zacatecas": true
  },
  "CarrierOperationalDetail": {
    "FleetSize": 0,
    "TotalPowerUnits": 0,
    "NumberOfVehicles": 0,
    "ReeferEquipment": true,
    "VanEquipment": true,
    "FlatbedStepDeckEquipment": true,
    "OwnedTractors": 0,
    "OwnedTrucks": 0,
    "OwnedTrailers": 0,
    "TermLeasedTractors": 0,
    "TermLeasedTrucks": 0,
    "TermLeasedTrailers": 0,
    "TripLeasedTractors": 0,
    "TripLeasedTrucks": 0,
    "TripLeasedTrailers": 0,
    "InterstateAndIntrastateDrivers": 0,
    "CDLEmployedDrivers": 0,
    "MonthlyAverageLeasedDrivers": 0,
    "InterstateDriversTotal": 0,
    "InterstateDriversGT100Miles": 0,
    "InterstateDriversLT100Miles": 0,
    "IntrastateDriversTotal": 0,
    "IntrastateDriversGT100Miles": 0,
    "IntrastateDriversLT100Miles": 0,
    "PowerOnly": true,
    "SatelliteEquipment": true,
    "TeamDrivers": true,
    "DropTrailer": true,
    "ELDCompliant": true,
    "ELDCompliantBy": "string",
    "ELDIdentifier": "string",
    "NumberOfTractors": 0,
    "NumberOfVans": 0,
    "NumberOfReefers": 0,
    "NumberOfFlats": 0,
    "NumberOfStepDecks": 0,
    "NumberOfTanks": 0
  },
  "CarrierPaymentInfo": {
    "BankRoutingNumber": "string",
    "BankAccountNumber": "string",
    "BankAccountName": "string",
    "BankName": "string",
    "BankAddress": "string",
    "BankPhone": "string",
    "BankFax": "string",
    "FactoringCompanyName": "string",
    "RemitAddress1": "string",
    "RemitAddress2": "string",
    "RemitCity": "string",
    "RemitZipCode": "string",
    "BankAccountType": "string",
    "RemitState": "string",
    "RemitCountry": "string",
    "RemitEmail": "string",
    "Require1099": true,
    "EpayManagerID": 0,
    "RemitCurrency": "string",
    "PayAdvanceOptionID": 0,
    "PayAdvanceOptionType": "string"
  },
  "CarrierRemit": {
    "CarrierRemitEmail": "string",
    "CarrierRemitAddress1": "string",
    "CarrierRemitAddress2": "string",
    "CarrierRemitCity": "string",
    "CarrierRemitCountry": "string",
    "CarrierRemitStateProvince": "string",
    "CarrierRemitZipCode": "string"
  },
  "FactoringRemit": {
    "FactoringCompanyID": 0,
    "FactoringCompanyName": "string",
    "FactoringRemitEmail": "string",
    "FactoringRemitAddress": "string",
    "FactoringRemitAddress2": "string",
    "FactoringRemitCity": "string",
    "FactoringRemitCountry": "string",
    "FactoringRemitStateProvince": "string",
    "FactoringRemitZipcode": "string",
    "FactoringPhone": "string",
    "BankRoutingNumber": "string",
    "BankAccountNumber": "string"
  },
  "CarrierBank": {
    "CarrierBankRoutingNumber": "string",
    "CarrierBankAccountNumber": "string",
    "CarrierBankAccountName": "string",
    "CarrierBankName": "string",
    "CarrierBankAddress": "string",
    "CarrierBankPhone": "string",
    "CarrierBankFax": "string",
    "CarrierBankAccountType": "string"
  },
  "CarrierPaymentTerms": [\
    {\
      "PaymentTerm": {\
        "PaymentTermID": 0,\
        "Days": 0,\
        "Term": "string",\
        "QuickPay": true,\
        "PaymentFeeType": "string",\
        "PaymentFeeAmount": 0,\
        "CustomerID": 0\
      }\
    }\
  ],
  "CarrierPaymentTypes": [\
    {\
      "PaymentType": {\
        "PaymentTypeID": 0,\
        "Type": "string",\
        "CustomerID": 0,\
        "PaymentType": {\
          "Name": "string"\
        }\
      }\
    }\
  ],
  "CarrierPayerType": {
    "PayerTypeID": 0,
    "Name": "string"
  },
  "CarrierTruckClass": {
    "Conestoga": true,
    "Containers": true,
    "DecksSpecialized": true,
    "DecksStandard": true,
    "DryBulk": true,
    "Flatbeds": true,
    "HazardousMaterials": true,
    "Reefers": true,
    "Tankers": true,
    "VansSpecialized": true,
    "VansStandard": true,
    "Other": "string"
  },
  "CarrierTruckType": {
    "AFrameTrailer": true,
    "AFrameTrailerCount": 0,
    "AcidTanker": true,
    "AcidTankerCount": 0,
    "AugerTrailer": true,
    "AugerTrailerCount": 0,
    "AutoCarrier": true,
    "AutoCarrierCount": 0,
    "BeamTrailer": true,
    "BeamTrailerCount": 0,
    "BellyDumpTrailer": true,
    "BellyDumpTrailerCount": 0,
    "BTrain": true,
    "BTrainCount": 0,
    "BoatTrailer": true,
    "BoatTrailerCount": 0,
    "Chassis": true,
    "ChassisCount": 0,
    "ChemicalTankTrailer": true,
    "ChemicalTankTrailerCount": 0,
    "CompressedGasTanker": true,
    "CompressedGasTankerCount": 0,
    "Conestoga": true,
    "ConestogaCount": 0,
    "Container": true,
    "ContainerCount": 0,
    "ContainerChassisTrailer20Foot": true,
    "ContainerChassisTrailer20FootCount": 0,
    "ContainerChassisTrailer40Foot": true,
    "ContainerChassisTrailer40FootCount": 0,
    "ContainerChassisTrailerComboChassis": true,
    "ContainerChassisTrailerComboChassisCount": 0,
    "ContainerInsulated": true,
    "ContainerInsulatedCount": 0,
    "ContainerRefrigerated": true,
    "ContainerRefrigeratedCount": 0,
    "ContainerStandard": true,
    "ContainerStandardCount": 0,
    "ConvertibleTrailer": true,
    "ConvertibleTrailerCount": 0,
    "Conveyor": true,
    "ConveyorCount": 0,
    "CryogenicLiquidTanker": true,
    "CryogenicLiquidTankerCount": 0,
    "Dolly": true,
    "DollyCount": 0,
    "DoubleDrop": true,
    "DoubleDropCount": 0,
    "DropDeckLandoll": true,
    "DropDeckLandollCount": 0,
    "DryBulkTanker": true,
    "DryBulkTankerCount": 0,
    "DualLaneTrailer": true,
    "DualLaneTrailerCount": 0,
    "DumpTrailer": true,
    "DumpTrailerCount": 0,
    "EightToTenCarHauler": true,
    "EightToTenCarHaulerCount": 0,
    "EndDumpTrailer": true,
    "EndDumpTrailerCount": 0,
    "ExtendableFlatbedTrailer": true,
    "ExtendableFlatbedTrailerCount": 0,
    "FertilizerHopperTrailer": true,
    "FertilizerHopperTrailerCount": 0,
    "Flatbed": true,
    "FlatbedCount": 0,
    "FlatbedAirRide": true,
    "FlatbedAirRideCount": 0,
    "FlatbedConestoga": true,
    "FlatbedConestogaCount": 0,
    "FlatbedDouble": true,
    "FlatbedDoubleCount": 0,
    "FlatbedHazMat": true,
    "FlatbedHazMatCount": 0,
    "FlatbedHotshot": true,
    "FlatbedHotshotCount": 0,
    "FlatbedMaxi": true,
    "FlatbedMaxiCount": 0,
    "FlatbedOrStepDeck": true,
    "FlatbedOrStepDeckCount": 0,
    "FlatbedOverdimension": true,
    "FlatbedOverdimensionCount": 0,
    "FlatbedSpecialized": true,
    "FlatbedSpecializedCount": 0,
    "FlatbedWithchains": true,
    "FlatbedWithchainsCount": 0,
    "FlatbedWithSides": true,
    "FlatbedWithSidesCount": 0,
    "FlatbedWithTarps": true,
    "FlatbedWithTarpsCount": 0,
    "FlatbedWithTeam": true,
    "FlatbedWithTeamCount": 0,
    "FlatbedVanReefer": true,
    "FlatbedVanReeferCount": 0,
    "FoodGradeTankTrailer": true,
    "FoodGradeTankTrailerCount": 0,
    "FourToFiveCarHauler": true,
    "FourToFiveCarHaulerCount": 0,
    "FuelTankTrailer": true,
    "FuelTankTrailerCount": 0,
    "GasCylinderTrailer": true,
    "GasCylinderTrailerCount": 0,
    "GrainHopperTrailer": true,
    "GrainHopperTrailerCount": 0,
    "HazmatTanker": true,
    "HazmatTankerCount": 0,
    "HopperBottom": true,
    "HopperBottomCount": 0,
    "HopperHighSide": true,
    "HopperHighSideCount": 0,
    "HopperLowSide": true,
    "HopperLowSideCount": 0,
    "HopperTrailer": true,
    "HopperTrailerCount": 0,
    "HorseTrailer": true,
    "HorseTrailerCount": 0,
    "HotshotTrailer": true,
    "HotshotTrailerCount": 0,
    "InsulatedVanOrReefer": true,
    "InsulatedVanOrReeferCount": 0,
    "Landoll": true,
    "LandollCount": 0,
    "LivestockTrailer": true,
    "LivestockTrailerCount": 0,
    "LiveBottomTrailer": true,
    "LiveBottomTrailerCount": 0,
    "LoggingTrailer": true,
    "LoggingTrailerCount": 0,
    "Lowboy": true,
    "LowboyCount": 0,
    "LowboyOrRemGooseneck": true,
    "LowboyOrRemGooseneckCount": 0,
    "LowboyOverdimension": true,
    "LowboyOverdimensionCount": 0,
    "MiniDeckTrailer": true,
    "MiniDeckTrailerCount": 0,
    "MilkTankTrailer": true,
    "MilkTankTrailerCount": 0,
    "MovingVan": true,
    "MovingVanCount": 0,
    "MultiAxleHeavyHaulTrailer": true,
    "MultiAxleHeavyHaulTrailerCount": 0,
    "MultiLevelCarHauler": true,
    "MultiLevelCarHaulerCount": 0,
    "OneToTwoCarHauler": true,
    "OneToTwoCarHaulerCount": 0,
    "PerimeterTrailer": true,
    "PerimeterTrailerCount": 0,
    "PintleHitch": true,
    "PintleHitchCount": 0,
    "PintleHitchTrailer": true,
    "PintleHitchTrailerCount": 0,
    "PoleTrailer": true,
    "PoleTrailerCount": 0,
    "Pneumatic": true,
    "PneumaticCount": 0,
    "PowerOnly": true,
    "PowerOnlyCount": 0,
    "Reefer": true,
    "ReeferCount": 0,
    "ReeferAirRide": true,
    "ReeferAirRideCount": 0,
    "ReeferDouble": true,
    "ReeferDoubleCount": 0,
    "ReeferHazMat": true,
    "ReeferHazMatCount": 0,
    "ReeferIntermodal": true,
    "ReeferIntermodalCount": 0,
    "ReeferLogistics": true,
    "ReeferLogisticsCount": 0,
    "ReeferOrVentedVan": true,
    "ReeferOrVentedVanCount": 0,
    "ReeferPalletExchange": true,
    "ReeferPalletExchangeCount": 0,
    "ReeferSpecialized": true,
    "ReeferSpecializedCount": 0,
    "ReeferStandard48Foot": true,
    "ReeferStandard48FootCount": 0,
    "ReeferStandard53Foot": true,
    "ReeferStandard53FootCount": 0,
    "ReeferWithTeam": true,
    "ReeferWithTeamCount": 0,
    "RemovableGooseneck": true,
    "RemovableGooseneckCount": 0,
    "SideDumpTrailer": true,
    "SideDumpTrailerCount": 0,
    "SingleLevelCarHauler": true,
    "SingleLevelCarHaulerCount": 0,
    "SixToSevenCarHauler": true,
    "SixToSevenCarHaulerCount": 0,
    "StandardFlatbed48Foot": true,
    "StandardFlatbed48FootCount": 0,
    "StandardFlatbed53Foot": true,
    "StandardFlatbed53FootCount": 0,
    "SteerableStepDeckStretch": true,
    "SteerableStepDeckStretchCount": 0,
    "StepDeck": true,
    "StepDeckCount": 0,
    "StepDeckOrRemGooseneck": true,
    "StepDeckOrRemGooseneckCount": 0,
    "StepDeckSpecialized": true,
    "StepDeckSpecializedCount": 0,
    "StepDeckStandard48Foot": true,
    "StepDeckStandard48FootCount": 0,
    "StepDeckStandard53Foot": true,
    "StepDeckStandard53FootCount": 0,
    "StepdeckConestoga": true,
    "StepdeckConestogaCount": 0,
    "StraightBoxTruck": true,
    "StraightBoxTruckCount": 0,
    "StretchFlatbed": true,
    "StretchFlatbedCount": 0,
    "StretchRGN": true,
    "StretchRGNCount": 0,
    "StretchStepDeck": true,
    "StretchStepDeckCount": 0,
    "StretchTrailer": true,
    "StretchTrailerCount": 0,
    "TankerAluminum": true,
    "TankerAluminumCount": 0,
    "TankerIntermodal": true,
    "TankerIntermodalCount": 0,
    "TankerSteel": true,
    "TankerSteelCount": 0,
    "ThreeCarHauler": true,
    "ThreeCarHaulerCount": 0,
    "TinWideTrailer": true,
    "TinWideTrailerCount": 0,
    "Toter": true,
    "ToterCount": 0,
    "TruckAndTrailer": true,
    "TruckAndTrailerCount": 0,
    "Van": true,
    "VanCount": 0,
    "VanAirRide": true,
    "VanAirRideCount": 0,
    "VanBlanketWrap": true,
    "VanBlanketWrapCount": 0,
    "VanConestoga": true,
    "VanConestogaCount": 0,
    "VanDouble": true,
    "VanDoubleCount": 0,
    "VanHazMat": true,
    "VanHazMatCount": 0,
    "VanHeated": true,
    "VanHeatedCount": 0,
    "VanHotshot": true,
    "VanHotshotCount": 0,
    "VanInsulated": true,
    "VanInsulatedCount": 0,
    "VanIntermodal": true,
    "VanIntermodalCount": 0,
    "VanLiftGate": true,
    "VanLiftGateCount": 0,
    "VanLogistics": true,
    "VanLogisticsCount": 0,
    "VanOpenTop": true,
    "VanOpenTopCount": 0,
    "VanOrFlatbed": true,
    "VanOrFlatbedCount": 0,
    "VanOrFlatbedwTarps": true,
    "VanOrFlatbedwTarpsCount": 0,
    "VanOrReefer": true,
    "VanOrReeferCount": 0,
    "VanPalletExchange": true,
    "VanPalletExchangeCount": 0,
    "VanRollerBed": true,
    "VanRollerBedCount": 0,
    "VanSpecialized": true,
    "VanSpecializedCount": 0,
    "VanSprinter": true,
    "VanSprinterCount": 0,
    "VanStandard": true,
    "VanStandardCount": 0,
    "VanTriple": true,
    "VanTripleCount": 0,
    "VanVented": true,
    "VanVentedCount": 0,
    "VanWithCurtains": true,
    "VanWithCurtainsCount": 0,
    "VanWithTeam": true,
    "VanWithTeamCount": 0,
    "WalkingFloorTrailer": true,
    "WalkingFloorTrailerCount": 0
  },
  "CarrierW9Forms": [\
    {\
      "FullName": "string",\
      "BusinessName": "string",\
      "IndividualOrSingleMemberLLC": true,\
      "CCorporation": true,\
      "SCorporation": true,\
      "Partnership": true,\
      "RequesterNameAddress": "string",\
      "TrustOrEstate": true,\
      "LimitedLiabilityCompany": true,\
      "TaxClassification": "string",\
      "Other": true,\
      "OtherDetail": "string",\
      "ExemptPayeeCode": "string",\
      "ExemptionFATCACode": "string",\
      "Address": "string",\
      "CityStateZipCode": "string",\
      "ListAccountNumber": "string",\
      "SSN": "string",\
      "EIN": "string",\
      "SignatureDate": "2026-05-17T23:54:51.263Z",\
      "SignaturePerson": "string",\
      "IsActive": true,\
      "City": "string",\
      "State": "string",\
      "ZipCode": "string",\
      "CarrierW9FormImages": [\
        {\
          "BlobName": "string",\
          "CreatedDate": "2026-05-17T23:54:51.263Z",\
          "FileName": "string",\
          "CreatedBy": "string"\
        }\
      ]\
    }\
  ],
  "CarrierCertification": {
    "Hazmat": true,
    "HazmatNumber": "string",
    "SmartWay": true,
    "CARB": true,
    "TWIC": true,
    "CTPATCertified": true,
    "CTPATSVINumber": "string",
    "TankerEndorsed": true,
    "TankerEndorsedNumOfDrivers": 0,
    "CBP": true,
    "CBSA": true,
    "ANAM": true,
    "ACE": true,
    "ACI": true,
    "CSA": true,
    "FAST": true,
    "PIP": true
  },
  "AssureAdvantage": [\
    {\
      "CarrierDetails": {\
        "docketNumber": "string",\
        "dotNumber": {\
          "status": "string",\
          "Value": "string"\
        },\
        "carrierType": "string",\
        "isMonitored": true,\
        "isBlocked": true,\
        "Identity": {\
          "legalName": "string",\
          "dbaName": "string",\
          "businessStreet": "string",\
          "businessCity": "string",\
          "businessState": "string",\
          "businessZipCode": "string",\
          "businessColonia": "string",\
          "businessCountry": "string",\
          "businessPhone": "string",\
          "businessFax": "string",\
          "mailingStreet": "string",\
          "mailingCity": "string",\
          "mailingState": "string",\
          "mailingZipCode": "string",\
          "mailingColonia": "string",\
          "mailingCountry": "string",\
          "mailingPhone": "string",\
          "mailingFax": "string",\
          "undeliverableMail": "string",\
          "companyRep1": "string",\
          "companyRep2": "string",\
          "cellPhone": "string",\
          "emailAddress": "string",\
          "dunBradstreetNum": "string",\
          "organization": "string"\
        },\
        "Authority": {\
          "authGrantDate": "string",\
          "commonAuthority": "string",\
          "commonAuthorityPending": "string",\
          "commonAuthorityRevocation": "string",\
          "contractAuthority": "string",\
          "contractAuthorityPending": "string",\
          "contractAuthorityRevocation": "string",\
          "brokerAuthority": "string",\
          "brokerAuthorityPending": "string",\
          "brokerAuthorityRevocation": "string",\
          "freight": "string",\
          "passenger": "string",\
          "householdGoods": "string",\
          "private": "string",\
          "enterprise": "string"\
        },\
        "FMCSAInsurance": {\
          "bipdRequired": "string",\
          "bipdOnFile": "string",\
          "cargoRequired": "string",\
          "cargoOnFile": "string",\
          "bondSuretyRequired": "string",\
          "bondSuretyOnFile": "string",\
          "PolicyList": [\
            {\
              "companyName": "string",\
              "attnToName": "string",\
              "address": "string",\
              "city": "string",\
              "stateCode": "string",\
              "postalCode": "string",\
              "countryCode": "string",\
              "phone": "string",\
              "fax": "string",\
              "insuranceType": "string",\
              "policyNumber": "string",\
              "postedDate": "string",\
              "effectiveDate": "string",\
              "cancelationDate": "string",\
              "coverageFrom": "string",\
              "coverageTo": "string",\
              "amBestRating": "string"\
            }\
          ]\
        },\
        "CertData": {\
          "status": "string",\
          "noncoop": true,\
          "Certificate": [\
            {\
              "certificateID": "string",\
              "producerName": "string",\
              "producerAddress": "string",\
              "producerCity": "string",\
              "producerState": "string",\
              "producerZip": "string",\
              "producerPhone": "string",\
              "producerFax": "string",\
              "producerEmail": "string",\
              "paidFor": "string",\
              "BlobName": "string",\
              "Coverage": [\
                {\
                  "insurerName": "string",\
                  "insurerAMBestRating": "string",\
                  "type": "string",\
                  "policyNumber": "string",\
                  "expirationDate": "string",\
                  "coverageLimit": "string",\
                  "deductable": "string",\
                  "referBreakdown": "string",\
                  "referBreakDeduct": "string",\
                  "cancellationDate": "string"\
                }\
              ]\
            }\
          ]\
        },\
        "Safety": {\
          "rating": "string",\
          "ratingDate": "string",\
          "unsafeDrvPCT": "string",\
          "unsafeDrvOT": "string",\
          "unsafeDrvSV": "string",\
          "unsafeDrvAlert": "string",\
          "unsafeDrvTrend": "string",\
          "unsafeDrvCNT": 0,\
          "hosPCT": "string",\
          "hosOT": "string",\
          "hosSV": "string",\
          "hosAlert": "string",\
          "hosTrend": "string",\
          "hosCNT": 0,\
          "drvFitPCT": "string",\
          "drvFitOT": "string",\
          "drvFitSV": "string",\
          "drvFitAlert": "string",\
          "drvFitTrend": "string",\
          "drvFitCNT": 0,\
          "controlSubPCT": "string",\
          "controlSubOT": "string",\
          "controlSubSV": "string",\
          "controlSubAlert": "string",\
          "controlSubTrend": "string",\
          "controlSubCNT": 0,\
          "vehMaintPCT": "string",\
          "vehMaintOT": "string",\
          "vehMaintSV": "string",\
          "vehMaintAlert": "string",\
          "vehMaintTrend": "string",\
          "vehMaintCNT": 0,\
          "hazMatPCT": "string",\
          "hazMatOT": "string",\
          "hazMatSV": "string",\
          "hazMatAlert": "string",\
          "hazMatTrend": "string",\
          "hazMatCNT": 0\
        },\
        "Inspection": {\
          "inspectVehUS": "string",\
          "inspectVehOOSUS": "string",\
          "inspectVehOOSPctUS": "string",\
          "inspectDrvUS": "string",\
          "inspectDrvOOSUS": "string",\
          "inspectDrvOOSPctUS": "string",\
          "inspectHazUS": "string",\
          "inspectHazOOSUS": "string",\
          "inspectHazOOSPctUS": "string",\
          "inspectIEPUS": "string",\
          "inspectIEPOOSUS": "string",\
          "inspectIEPOOSPctUS": "string",\
          "inspectTotalIEPUS": "string",\
          "inspectTotalUS": "string",\
          "inspectVehCAN": "string",\
          "inspectVehOOSCAN": "string",\
          "inspectVehOOSPctCAN": "string",\
          "inspectDrvCAN": "string",\
          "inspectDrvOOSCAN": "string",\
          "inspectDrvOOSPctCAN": "string",\
          "inspectTotalCAN": "string"\
        },\
        "Crash": {\
          "crashFatalUS": "string",\
          "crashInjuryUS": "string",\
          "crashTowUS": "string",\
          "crashTotalUS": "string",\
          "crashFatalCAN": "string",\
          "crashInjuryCAN": "string",\
          "crashTowCAN": "string",\
          "crashTotalCAN": "string"\
        },\
        "Review": {\
          "reviewType": "string",\
          "reviewDate": "string",\
          "reviewDocNum": "string",\
          "reviewMiles": "string",\
          "mcs150Date": "string",\
          "mcs150MileYear": "string",\
          "mcs150Miles": "string",\
          "accidentRate": "string",\
          "accidentRatePrevent": "string"\
        },\
        "Operation": {\
          "dotAddDate": "string",\
          "carrierOperation": "string",\
          "shipperOperation": "string",\
          "mxOperationType": "string",\
          "mxRFCNumber": "string",\
          "outOfService": "string",\
          "outOfServiceDate": "string",\
          "outOfServiceReason": "string",\
          "entityCarrier": "string",\
          "entityShipper": "string",\
          "entityBroker": "string",\
          "entityFreightFowarder": "string",\
          "entityCargoTank": "string",\
          "classAuthForHire": "string",\
          "classMigrant": "string",\
          "classIndianNation": "string",\
          "classExemptForHire": "string",\
          "classUSMail": "string",\
          "classPrivateProperty": "string",\
          "classFederalGovernment": "string",\
          "classPrivPassBusiness": "string",\
          "classStateGovernment": "string",\
          "classPrivPassNonBusiness": "string",\
          "classLocalGovernment": "string",\
          "classOther": "string",\
          "operatingStatus": "string"\
        },\
        "Cargo": {\
          "hazmatIndicator": "string",\
          "cargoGenFreight": "string",\
          "cargoHousehold": "string",\
          "cargoMetal": "string",\
          "cargoMotorVeh": "string",\
          "cargoDriveTow": "string",\
          "cargoLogPole": "string",\
          "cargoBldgMaterial": "string",\
          "cargoMobileHome": "string",\
          "cargoMachLarge": "string",\
          "cargoProduce": "string",\
          "cargoLiqGas": "string",\
          "cargoIntermodal": "string",\
          "cargoPassengers": "string",\
          "cargoOilfield": "string",\
          "cargoLivestock": "string",\
          "cargoGrainfeed": "string",\
          "cargoCoalcoke": "string",\
          "cargoMeat": "string",\
          "cargoGarbage": "string",\
          "cargoUSMail": "string",\
          "cargoChemicals": "string",\
          "cargoDryBulk": "string",\
          "cargoRefrigerated": "string",\
          "cargoBeverages": "string",\
          "cargoPaperProd": "string",\
          "cargoUtilities": "string",\
          "cargoFarmSupplies": "string",\
          "cargoConstruction": "string",\
          "cargoWaterwell": "string",\
          "cargoOther": "string",\
          "cargoOtherDesc": "string"\
        },\
        "Drivers": {\
          "driversTotal": "string",\
          "driversAvgLeased": "string",\
          "driversCDL": "string",\
          "driversInter": "string",\
          "driversInterLT100": "string",\
          "driversInterGT100": "string",\
          "driversIntra": "string",\
          "driversIntraLT100": "string",\
          "driversIntraGT100": "string"\
        },\
        "Equipment": {\
          "trucksTotal": "string",\
          "totalPower": "string",\
          "fleetsize": "string",\
          "trucksOwned": "string",\
          "trucksTerm": "string",\
          "trucksTrip": "string",\
          "trailersOwned": "string",\
          "trailersTerm": "string",\
          "trailersTrip": "string",\
          "tractorsOwned": "string",\
          "tractorsTerm": "string",\
          "tractorsTrip": "string"\
        },\
        "Other": {\
          "carbTru": "string",\
          "smartway": "string",\
          "watchdogReports": "string"\
        },\
        "RiskAssessment": {\
          "Overall": "string",\
          "Authority": "string",\
          "Insurance": "string",\
          "Safety": "string",\
          "Operation": "string",\
          "Other": "string"\
        },\
        "RiskAssessmentDetails": {\
          "IsIntrastateCarrier": true,\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "ReviewState": "string",\
          "Authority": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Insurance": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Safety": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Operation": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Other": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "ReviewDetails": {\
            "ReviewID": 0,\
            "PreReviewOverall": "string",\
            "PreReviewAuthority": "string",\
            "PreReviewInsurance": "string",\
            "PreReviewSafety": "string",\
            "PreReviewOperation": "string",\
            "PreReviewOther": "string",\
            "ReviewUser": "string",\
            "ReviewDate": "2026-05-17T23:54:51.263Z",\
            "ReviewReason": "string",\
            "ReviewNote": "string",\
            "ReviewExpirationDate": "2026-05-17T23:54:51.263Z"\
          }\
        },\
        "CarrierRatings": {\
          "myRating": 0,\
          "totalRatings": 0,\
          "lowRatings": 0,\
          "avgRating": 0\
        },\
        "LatestInvitation": {\
          "InvitedByUserName": "string",\
          "InvitedByEmail": "string",\
          "InvitedByFirstName": "string",\
          "InvitedByLastName": "string",\
          "InvitationSentDate": "2026-05-17T23:54:51.263Z",\
          "InvitationRecipient": "string"\
        },\
        "IncidentReports": {\
          "TotalIncidentReports": 0,\
          "TotalIncidentReportsWithFraud": 0\
        }\
      },\
      "ResponseDO": {\
        "status": "string",\
        "action": "string",\
        "code": "string",\
        "displayMsg": "string",\
        "techMsg": "string"\
      }\
    }\
  ],
  "CarrierMode": {
    "LessThanTruckLoad": true,
    "Partial": true,
    "Truckload": true,
    "Rail": true,
    "Intermodal": true,
    "Air": true,
    "Expedite": true,
    "Ocean": true,
    "Drayage": true
  },
  "CarrierELDProvider": {
    "ComplianceStatusID": 0,
    "ComplianceStatus": "string",
    "ProviderName": "string",
    "ProviderIdentifier": "string",
    "ExemptionID": 0,
    "Exemption": "string",
    "CompliantBy": "string"
  },
  "OwnerContactName": "string",
  "OwnerContactPhone": "string",
  "OwnerContactEmail": "string",
  "CarrierTINMatchings": [\
    {\
      "TINTypeID": 0,\
      "TIN": "string",\
      "TINName": "string",\
      "TINMatchingStatusID": 0,\
      "TINMatchingResultID": 0,\
      "CreatedOnUtc": "2026-05-17T23:54:51.263Z",\
      "SubmittedOnUtc": "2026-05-17T23:54:51.263Z",\
      "ProcessedOnUtc": "2026-05-17T23:54:51.263Z",\
      "ContactEmail": "string",\
      "ContactPhoneNumber": "string",\
      "MatchingResult": "string",\
      "MatchingStatus": "string"\
    }\
  ],
  "Message": "string"
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.CarrierAADTO>
  <DOTNumber>1</DOTNumber>
  <LegalName>string</LegalName>
  <DBAName>string</DBAName>
  <Address1>string</Address1>
  <Address2>string</Address2>
  <City>string</City>
  <Zipcode>string</Zipcode>
  <State>string</State>
  <Country>string</Country>
  <CellPhone>string</CellPhone>
  <Phone>string</Phone>
  <Fax>string</Fax>
  <FreePhone>string</FreePhone>
  <EmergencyPhone>string</EmergencyPhone>
  <Email>string</Email>
  <FraudIdentityTheftStatus>string</FraudIdentityTheftStatus>
  <MCNumber>string</MCNumber>
  <SCAC>string</SCAC>
  <MailingAddress1>string</MailingAddress1>
  <MailingAddress2>string</MailingAddress2>
  <MailingCity>string</MailingCity>
  <MailingState>string</MailingState>
  <MailingZipcode>string</MailingZipcode>
  <MailingCountry>string</MailingCountry>
  <AfterHrsWkDaySupportName>string</AfterHrsWkDaySupportName>
  <AfterHrsWkDaySupportPhone>string</AfterHrsWkDaySupportPhone>
  <AfterHrsWkDaySupportFax>string</AfterHrsWkDaySupportFax>
  <AfterHrsWkDaySupportFrom>string</AfterHrsWkDaySupportFrom>
  <AfterHrsWkDaySupportTo>string</AfterHrsWkDaySupportTo>
  <AfterHrsWkEndSupportName>string</AfterHrsWkEndSupportName>
  <AfterHrsWkEndSupportPhone>string</AfterHrsWkEndSupportPhone>
  <AfterHrsWkEndSupportFax>string</AfterHrsWkEndSupportFax>
  <AfterHrsWkEndSupportFrom>string</AfterHrsWkEndSupportFrom>
  <AfterHrsWkEndSupportTo>string</AfterHrsWkEndSupportTo>
  <Website>string</Website>
  <OperationManagerName>string</OperationManagerName>
  <OnlineAccessToAvailableLoads>true</OnlineAccessToAvailableLoads>
  <AvailableLoadsEmail>string</AvailableLoadsEmail>
  <DriverLogsSafeyDeptManagerName>string</DriverLogsSafeyDeptManagerName>
  <DriverLogsSafeyDeptManagerPhone>string</DriverLogsSafeyDeptManagerPhone>
  <Dispatchers>string</Dispatchers>
  <ClaimsContactName>string</ClaimsContactName>
  <ClaimsContactPhone>string</ClaimsContactPhone>
  <ClaimsContactEmail>string</ClaimsContactEmail>
  <DispatchServiceUsed>true</DispatchServiceUsed>
  <DispatchServiceName>string</DispatchServiceName>
  <DispatchServicePhone>string</DispatchServicePhone>
  <BrokerOutExtraFreight>true</BrokerOutExtraFreight>
  <References1>string</References1>
  <References2>string</References2>
  <References3>string</References3>
  <DriversTrackedBy>string</DriversTrackedBy>
  <AccessOnlineGPSTracking>true</AccessOnlineGPSTracking>
  <DriversTrackedByOtherMethod>string</DriversTrackedByOtherMethod>
  <CreatedDateTime>1970-01-01T00:00:00.001Z</CreatedDateTime>
  <ModifiedDateTime>1970-01-01T00:00:00.001Z</ModifiedDateTime>
  <CarrierCustomerAgreements>
    <SignatureDate>1970-01-01T00:00:00.001Z</SignatureDate>
    <SignaturePerson>string</SignaturePerson>
    <SignaturePersonTitle>string</SignaturePersonTitle>
    <SignaturePersonUserName>string</SignaturePersonUserName>
    <SignaturePersonEmail>string</SignaturePersonEmail>
    <SignaturePersonPhoneNumber>string</SignaturePersonPhoneNumber>
    <OnCurrentCustomerAgreement>true</OnCurrentCustomerAgreement>
    <CustomerAgreement>
      <AgreementName>string</AgreementName>
      <CreatedDate>1970-01-01T00:00:00.001Z</CreatedDate>
      <CreatedBy>string</CreatedBy>
      <BlobName>string</BlobName>
      <Customer>
        <CustomerID>1</CustomerID>
        <Title>string</Title>
        <FirstName>string</FirstName>
        <MiddleName>string</MiddleName>
        <LastName>string</LastName>
        <CompanyName>string</CompanyName>
        <TypeCompany>string</TypeCompany>
        <CellPhone>string</CellPhone>
        <Phone>string</Phone>
        <Fax>string</Fax>
        <Address1>string</Address1>
        <Address2>string</Address2>
        <Apartment>string</Apartment>
        <City>string</City>
        <State>string</State>
        <Zipcode>string</Zipcode>
        <Country>string</Country>
        <CustomerKey>string</CustomerKey>
        <PacketCompletionNotificationType>1</PacketCompletionNotificationType>
        <PacketCompletionNotificationEmail>string</PacketCompletionNotificationEmail>
      </Customer>
    </CustomerAgreement>
    <CarrierCustomerAgreementImages>
      <BlobName>string</BlobName>
      <CreatedDate>1970-01-01T00:00:00.001Z</CreatedDate>
    </CarrierCustomerAgreementImages>
    <IsActive>true</IsActive>
    <IPAddress>string</IPAddress>
    <GeoLocLat>1.1</GeoLocLat>
    <GeoLocLng>1.1</GeoLocLng>
    <GeoLocMethod>string</GeoLocMethod>
  </CarrierCustomerAgreements>
  <CarrierCustomerPacketStatuses>
    <Customer>
      <CustomerID>1</CustomerID>
      <Title>string</Title>
      <FirstName>string</FirstName>
      <MiddleName>string</MiddleName>
      <LastName>string</LastName>
      <CompanyName>string</CompanyName>
      <TypeCompany>string</TypeCompany>
      <CellPhone>string</CellPhone>
      <Phone>string</Phone>
      <Fax>string</Fax>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Apartment>string</Apartment>
      <City>string</City>
      <State>string</State>
      <Zipcode>string</Zipcode>
      <Country>string</Country>
      <CustomerKey>string</CustomerKey>
      <PacketCompletionNotificationType>1</PacketCompletionNotificationType>
      <PacketCompletionNotificationEmail>string</PacketCompletionNotificationEmail>
    </Customer>
    <CarrierPacketStatus>string</CarrierPacketStatus>
    <CustomerID>1</CustomerID>
  </CarrierCustomerPacketStatuses>
  <CarrierCargoHauled>
    <GeneralFreight>true</GeneralFreight>
    <LiquidsGas>true</LiquidsGas>
    <Chemicals>true</Chemicals>
    <HouseholdGoods>true</HouseholdGoods>
    <IntermodalContainers>true</IntermodalContainers>
    <CommoditiesDryBulk>true</CommoditiesDryBulk>
    <MetalSheetsCoilsRolls>true</MetalSheetsCoilsRolls>
    <Passengers>true</Passengers>
    <RefrigeratedFood>true</RefrigeratedFood>
    <MotorVehicles>true</MotorVehicles>
    <OilfieldEquipment>true</OilfieldEquipment>
    <Beverages>true</Beverages>
    <DrivewayTowaway>true</DrivewayTowaway>
    <LivestockContainers>true</LivestockContainers>
    <PaperProducts>true</PaperProducts>
    <LogsPolesBeamsLumber>true</LogsPolesBeamsLumber>
    <GrainFeedHay>true</GrainFeedHay>
    <Utility>true</Utility>
    <BuildingMaterials>true</BuildingMaterials>
    <CoalCoke>true</CoalCoke>
    <FarmSupplies>true</FarmSupplies>
    <MobileHomes>true</MobileHomes>
    <Meat>true</Meat>
    <Construction>true</Construction>
    <MachineryLargeObjects>true</MachineryLargeObjects>
    <GarbageRefuseTrash>true</GarbageRefuseTrash>
    <WaterWell>true</WaterWell>
    <FreshProduce>true</FreshProduce>
    <USMail>true</USMail>
    <Other>string</Other>
  </CarrierCargoHauled>
  <CarrierCompanyClassification>
    <AuthForHire>true</AuthForHire>
    <Migrant>true</Migrant>
    <IndianNation>true</IndianNation>
    <ExemptForHire>true</ExemptForHire>
    <USMail>true</USMail>
    <PrivateProperty>true</PrivateProperty>
    <FederalGovernment>true</FederalGovernment>
    <PrivPassBusiness>true</PrivPassBusiness>
    <StateGovernment>true</StateGovernment>
    <PrivPassNonBusiness>true</PrivPassNonBusiness>
    <LocalGovernment>true</LocalGovernment>
    <WOSB>true</WOSB>
    <VOSB>true</VOSB>
    <MBE>true</MBE>
    <AsianPacificAmerican>true</AsianPacificAmerican>
    <SubcontinentAmerican>true</SubcontinentAmerican>
    <NOB>true</NOB>
    <HispanicAmerican>true</HispanicAmerican>
    <AfricanAmerican>true</AfricanAmerican>
    <WBE>true</WBE>
    <DBE>true</DBE>
    <SBA8a>true</SBA8a>
    <EDWOSB>true</EDWOSB>
    <SDVOSB>true</SDVOSB>
    <HUBZone>true</HUBZone>
    <LGBTQIA>true</LGBTQIA>
    <Other>string</Other>
  </CarrierCompanyClassification>
  <CarrierDrivers>
    <DriverName>string</DriverName>
    <CellPhone>string</CellPhone>
    <ComCheck>true</ComCheck>
    <FuelAdvance>true</FuelAdvance>
  </CarrierDrivers>
  <CarrierDispatchers>
    <DispatcherName>string</DispatcherName>
    <PhoneNumber>string</PhoneNumber>
    <Email>string</Email>
  </CarrierDispatchers>
  <CarrierLane>
    <UnitedStates>true</UnitedStates>
    <Mexico>true</Mexico>
    <Canada>true</Canada>
    <NortheastRegion>true</NortheastRegion>
    <MidwestRegion>true</MidwestRegion>
    <SouthRegion>true</SouthRegion>
    <WestRegion>true</WestRegion>
    <Alabama>true</Alabama>
    <Alaska>true</Alaska>
    <Arizona>true</Arizona>
    <Arkansas>true</Arkansas>
    <California>true</California>
    <Colorado>true</Colorado>
    <Delaware>true</Delaware>
    <Florida>true</Florida>
    <Georgia>true</Georgia>
    <Hawaii>true</Hawaii>
    <Idaho>true</Idaho>
    <Illinois>true</Illinois>
    <Indiana>true</Indiana>
    <Iowa>true</Iowa>
    <Kansas>true</Kansas>
    <Kentucky>true</Kentucky>
    <Louisiana>true</Louisiana>
    <Maine>true</Maine>
    <Maryland>true</Maryland>
    <Massachusetts>true</Massachusetts>
    <Michigan>true</Michigan>
    <Minnesota>true</Minnesota>
    <Mississippi>true</Mississippi>
    <Missouri>true</Missouri>
    <Montana>true</Montana>
    <Nebraska>true</Nebraska>
    <Nevada>true</Nevada>
    <NewHampshire>true</NewHampshire>
    <NewJersey>true</NewJersey>
    <NewMexico>true</NewMexico>
    <NewYork>true</NewYork>
    <NorthCarolina>true</NorthCarolina>
    <NorthDakota>true</NorthDakota>
    <Ohio>true</Ohio>
    <Oklahoma>true</Oklahoma>
    <Oregon>true</Oregon>
    <Pennsylvania>true</Pennsylvania>
    <RhodeIsland>true</RhodeIsland>
    <SouthCarolina>true</SouthCarolina>
    <SouthDakota>true</SouthDakota>
    <Tennessee>true</Tennessee>
    <Utah>true</Utah>
    <Vermont>true</Vermont>
    <Virginia>true</Virginia>
    <Washington>true</Washington>
    <WashingtonDC>true</WashingtonDC>
    <WestVirginia>true</WestVirginia>
    <Wisconsin>true</Wisconsin>
    <Wyoming>true</Wyoming>
    <Connecticut>true</Connecticut>
    <Texas>true</Texas>
    <Alberta>true</Alberta>
    <BritishColumbia>true</BritishColumbia>
    <Manitoba>true</Manitoba>
    <NewBrunswick>true</NewBrunswick>
    <NewfoundlandAndLabrador>true</NewfoundlandAndLabrador>
    <NorthwestTerritories>true</NorthwestTerritories>
    <NovaScotia>true</NovaScotia>
    <Nunavut>true</Nunavut>
    <Ontario>true</Ontario>
    <PrinceEdwardIsland>true</PrinceEdwardIsland>
    <Quebec>true</Quebec>
    <Saskatchewan>true</Saskatchewan>
    <YukonTerritory>true</YukonTerritory>
    <Aguascalientes>true</Aguascalientes>
    <BajaCalifornia>true</BajaCalifornia>
    <BajaCaliforniaNorte>true</BajaCaliforniaNorte>
    <BajaCaliforniaSur>true</BajaCaliforniaSur>
    <Chihuahua>true</Chihuahua>
    <Colima>true</Colima>
    <Campeche>true</Campeche>
    <Coahuila>true</Coahuila>
    <Chiapas>true</Chiapas>
    <Durango>true</Durango>
    <Guerrero>true</Guerrero>
    <Guanajuato>true</Guanajuato>
    <Hidalgo>true</Hidalgo>
    <Jalisco>true</Jalisco>
    <MexicoCity>true</MexicoCity>
    <MexicoState>true</MexicoState>
    <Michoacan>true</Michoacan>
    <Morelos>true</Morelos>
    <Nayarit>true</Nayarit>
    <NuevoLeon>true</NuevoLeon>
    <Oaxaca>true</Oaxaca>
    <Puebla>true</Puebla>
    <QuintanaRoo>true</QuintanaRoo>
    <Queretaro>true</Queretaro>
    <Sinaloa>true</Sinaloa>
    <SanLuisPotosi>true</SanLuisPotosi>
    <Sonora>true</Sonora>
    <Tabasco>true</Tabasco>
    <Tlaxcala>true</Tlaxcala>
    <Tamaulipas>true</Tamaulipas>
    <Veracruz>true</Veracruz>
    <Yucatan>true</Yucatan>
    <Zacatecas>true</Zacatecas>
  </CarrierLane>
  <CarrierOperationalDetail>
    <FleetSize>1</FleetSize>
    <TotalPowerUnits>1</TotalPowerUnits>
    <NumberOfVehicles>1</NumberOfVehicles>
    <ReeferEquipment>true</ReeferEquipment>
    <VanEquipment>true</VanEquipment>
    <FlatbedStepDeckEquipment>true</FlatbedStepDeckEquipment>
    <OwnedTractors>1</OwnedTractors>
    <OwnedTrucks>1</OwnedTrucks>
    <OwnedTrailers>1</OwnedTrailers>
    <TermLeasedTractors>1</TermLeasedTractors>
    <TermLeasedTrucks>1</TermLeasedTrucks>
    <TermLeasedTrailers>1</TermLeasedTrailers>
    <TripLeasedTractors>1</TripLeasedTractors>
    <TripLeasedTrucks>1</TripLeasedTrucks>
    <TripLeasedTrailers>1</TripLeasedTrailers>
    <InterstateAndIntrastateDrivers>1</InterstateAndIntrastateDrivers>
    <CDLEmployedDrivers>1</CDLEmployedDrivers>
    <MonthlyAverageLeasedDrivers>1</MonthlyAverageLeasedDrivers>
    <InterstateDriversTotal>1</InterstateDriversTotal>
    <InterstateDriversGT100Miles>1</InterstateDriversGT100Miles>
    <InterstateDriversLT100Miles>1</InterstateDriversLT100Miles>
    <IntrastateDriversTotal>1</IntrastateDriversTotal>
    <IntrastateDriversGT100Miles>1</IntrastateDriversGT100Miles>
    <IntrastateDriversLT100Miles>1</IntrastateDriversLT100Miles>
    <PowerOnly>true</PowerOnly>
    <SatelliteEquipment>true</SatelliteEquipment>
    <TeamDrivers>true</TeamDrivers>
    <DropTrailer>true</DropTrailer>
    <ELDCompliant>true</ELDCompliant>
    <ELDCompliantBy>string</ELDCompliantBy>
    <ELDIdentifier>string</ELDIdentifier>
    <NumberOfTractors>1</NumberOfTractors>
    <NumberOfVans>1</NumberOfVans>
    <NumberOfReefers>1</NumberOfReefers>
    <NumberOfFlats>1</NumberOfFlats>
    <NumberOfStepDecks>1</NumberOfStepDecks>
    <NumberOfTanks>1</NumberOfTanks>
  </CarrierOperationalDetail>
  <CarrierPaymentInfo>
    <BankRoutingNumber>string</BankRoutingNumber>
    <BankAccountNumber>string</BankAccountNumber>
    <BankAccountName>string</BankAccountName>
    <BankName>string</BankName>
    <BankAddress>string</BankAddress>
    <BankPhone>string</BankPhone>
    <BankFax>string</BankFax>
    <FactoringCompanyName>string</FactoringCompanyName>
    <RemitAddress1>string</RemitAddress1>
    <RemitAddress2>string</RemitAddress2>
    <RemitCity>string</RemitCity>
    <RemitZipCode>string</RemitZipCode>
    <BankAccountType>string</BankAccountType>
    <RemitState>string</RemitState>
    <RemitCountry>string</RemitCountry>
    <RemitEmail>string</RemitEmail>
    <Require1099>true</Require1099>
    <EpayManagerID>1</EpayManagerID>
    <RemitCurrency>string</RemitCurrency>
    <PayAdvanceOptionID>1</PayAdvanceOptionID>
    <PayAdvanceOptionType>string</PayAdvanceOptionType>
  </CarrierPaymentInfo>
  <CarrierRemit>
    <CarrierRemitEmail>string</CarrierRemitEmail>
    <CarrierRemitAddress1>string</CarrierRemitAddress1>
    <CarrierRemitAddress2>string</CarrierRemitAddress2>
    <CarrierRemitCity>string</CarrierRemitCity>
    <CarrierRemitCountry>string</CarrierRemitCountry>
    <CarrierRemitStateProvince>string</CarrierRemitStateProvince>
    <CarrierRemitZipCode>string</CarrierRemitZipCode>
  </CarrierRemit>
  <FactoringRemit>
    <FactoringCompanyID>1</FactoringCompanyID>
    <FactoringCompanyName>string</FactoringCompanyName>
    <FactoringRemitEmail>string</FactoringRemitEmail>
    <FactoringRemitAddress>string</FactoringRemitAddress>
    <FactoringRemitAddress2>string</FactoringRemitAddress2>
    <FactoringRemitCity>string</FactoringRemitCity>
    <FactoringRemitCountry>string</FactoringRemitCountry>
    <FactoringRemitStateProvince>string</FactoringRemitStateProvince>
    <FactoringRemitZipcode>string</FactoringRemitZipcode>
    <FactoringPhone>string</FactoringPhone>
    <BankRoutingNumber>string</BankRoutingNumber>
    <BankAccountNumber>string</BankAccountNumber>
  </FactoringRemit>
  <CarrierBank>
    <CarrierBankRoutingNumber>string</CarrierBankRoutingNumber>
    <CarrierBankAccountNumber>string</CarrierBankAccountNumber>
    <CarrierBankAccountName>string</CarrierBankAccountName>
    <CarrierBankName>string</CarrierBankName>
    <CarrierBankAddress>string</CarrierBankAddress>
    <CarrierBankPhone>string</CarrierBankPhone>
    <CarrierBankFax>string</CarrierBankFax>
    <CarrierBankAccountType>string</CarrierBankAccountType>
  </CarrierBank>
  <CarrierPaymentTerms>
    <PaymentTerm>
      <PaymentTermID>1</PaymentTermID>
      <Days>1</Days>
      <Term>string</Term>
      <QuickPay>true</QuickPay>
      <PaymentFeeType>string</PaymentFeeType>
      <PaymentFeeAmount>1.1</PaymentFeeAmount>
      <CustomerID>1</CustomerID>
    </PaymentTerm>
  </CarrierPaymentTerms>
  <CarrierPaymentTypes>
    <PaymentType>
      <PaymentTypeID>1</PaymentTypeID>
      <Type>string</Type>
      <CustomerID>1</CustomerID>
      <PaymentType>
        <Name>string</Name>
      </PaymentType>
    </PaymentType>
  </CarrierPaymentTypes>
  <CarrierPayerType>
    <PayerTypeID>1</PayerTypeID>
    <Name>string</Name>
  </CarrierPayerType>
  <CarrierTruckClass>
    <Conestoga>true</Conestoga>
    <Containers>true</Containers>
    <DecksSpecialized>true</DecksSpecialized>
    <DecksStandard>true</DecksStandard>
    <DryBulk>true</DryBulk>
    <Flatbeds>true</Flatbeds>
    <HazardousMaterials>true</HazardousMaterials>
    <Reefers>true</Reefers>
    <Tankers>true</Tankers>
    <VansSpecialized>true</VansSpecialized>
    <VansStandard>true</VansStandard>
    <Other>string</Other>
  </CarrierTruckClass>
  <CarrierTruckType>
    <AFrameTrailer>true</AFrameTrailer>
    <AFrameTrailerCount>1</AFrameTrailerCount>
    <AcidTanker>true</AcidTanker>
    <AcidTankerCount>1</AcidTankerCount>
    <AugerTrailer>true</AugerTrailer>
    <AugerTrailerCount>1</AugerTrailerCount>
    <AutoCarrier>true</AutoCarrier>
    <AutoCarrierCount>1</AutoCarrierCount>
    <BeamTrailer>true</BeamTrailer>
    <BeamTrailerCount>1</BeamTrailerCount>
    <BellyDumpTrailer>true</BellyDumpTrailer>
    <BellyDumpTrailerCount>1</BellyDumpTrailerCount>
    <BTrain>true</BTrain>
    <BTrainCount>1</BTrainCount>
    <BoatTrailer>true</BoatTrailer>
    <BoatTrailerCount>1</BoatTrailerCount>
    <Chassis>true</Chassis>
    <ChassisCount>1</ChassisCount>
    <ChemicalTankTrailer>true</ChemicalTankTrailer>
    <ChemicalTankTrailerCount>1</ChemicalTankTrailerCount>
    <CompressedGasTanker>true</CompressedGasTanker>
    <CompressedGasTankerCount>1</CompressedGasTankerCount>
    <Conestoga>true</Conestoga>
    <ConestogaCount>1</ConestogaCount>
    <Container>true</Container>
    <ContainerCount>1</ContainerCount>
    <ContainerChassisTrailer20Foot>true</ContainerChassisTrailer20Foot>
    <ContainerChassisTrailer20FootCount>1</ContainerChassisTrailer20FootCount>
    <ContainerChassisTrailer40Foot>true</ContainerChassisTrailer40Foot>
    <ContainerChassisTrailer40FootCount>1</ContainerChassisTrailer40FootCount>
    <ContainerChassisTrailerComboChassis>true</ContainerChassisTrailerComboChassis>
    <ContainerChassisTrailerComboChassisCount>1</ContainerChassisTrailerComboChassisCount>
    <ContainerInsulated>true</ContainerInsulated>
    <ContainerInsulatedCount>1</ContainerInsulatedCount>
    <ContainerRefrigerated>true</ContainerRefrigerated>
    <ContainerRefrigeratedCount>1</ContainerRefrigeratedCount>
    <ContainerStandard>true</ContainerStandard>
    <ContainerStandardCount>1</ContainerStandardCount>
    <ConvertibleTrailer>true</ConvertibleTrailer>
    <ConvertibleTrailerCount>1</ConvertibleTrailerCount>
    <Conveyor>true</Conveyor>
    <ConveyorCount>1</ConveyorCount>
    <CryogenicLiquidTanker>true</CryogenicLiquidTanker>
    <CryogenicLiquidTankerCount>1</CryogenicLiquidTankerCount>
    <Dolly>true</Dolly>
    <DollyCount>1</DollyCount>
    <DoubleDrop>true</DoubleDrop>
    <DoubleDropCount>1</DoubleDropCount>
    <DropDeckLandoll>true</DropDeckLandoll>
    <DropDeckLandollCount>1</DropDeckLandollCount>
    <DryBulkTanker>true</DryBulkTanker>
    <DryBulkTankerCount>1</DryBulkTankerCount>
    <DualLaneTrailer>true</DualLaneTrailer>
    <DualLaneTrailerCount>1</DualLaneTrailerCount>
    <DumpTrailer>true</DumpTrailer>
    <DumpTrailerCount>1</DumpTrailerCount>
    <EightToTenCarHauler>true</EightToTenCarHauler>
    <EightToTenCarHaulerCount>1</EightToTenCarHaulerCount>
    <EndDumpTrailer>true</EndDumpTrailer>
    <EndDumpTrailerCount>1</EndDumpTrailerCount>
    <ExtendableFlatbedTrailer>true</ExtendableFlatbedTrailer>
    <ExtendableFlatbedTrailerCount>1</ExtendableFlatbedTrailerCount>
    <FertilizerHopperTrailer>true</FertilizerHopperTrailer>
    <FertilizerHopperTrailerCount>1</FertilizerHopperTrailerCount>
    <Flatbed>true</Flatbed>
    <FlatbedCount>1</FlatbedCount>
    <FlatbedAirRide>true</FlatbedAirRide>
    <FlatbedAirRideCount>1</FlatbedAirRideCount>
    <FlatbedConestoga>true</FlatbedConestoga>
    <FlatbedConestogaCount>1</FlatbedConestogaCount>
    <FlatbedDouble>true</FlatbedDouble>
    <FlatbedDoubleCount>1</FlatbedDoubleCount>
    <FlatbedHazMat>true</FlatbedHazMat>
    <FlatbedHazMatCount>1</FlatbedHazMatCount>
    <FlatbedHotshot>true</FlatbedHotshot>
    <FlatbedHotshotCount>1</FlatbedHotshotCount>
    <FlatbedMaxi>true</FlatbedMaxi>
    <FlatbedMaxiCount>1</FlatbedMaxiCount>
    <FlatbedOrStepDeck>true</FlatbedOrStepDeck>
    <FlatbedOrStepDeckCount>1</FlatbedOrStepDeckCount>
    <FlatbedOverdimension>true</FlatbedOverdimension>
    <FlatbedOverdimensionCount>1</FlatbedOverdimensionCount>
    <FlatbedSpecialized>true</FlatbedSpecialized>
    <FlatbedSpecializedCount>1</FlatbedSpecializedCount>
    <FlatbedWithchains>true</FlatbedWithchains>
    <FlatbedWithchainsCount>1</FlatbedWithchainsCount>
    <FlatbedWithSides>true</FlatbedWithSides>
    <FlatbedWithSidesCount>1</FlatbedWithSidesCount>
    <FlatbedWithTarps>true</FlatbedWithTarps>
    <FlatbedWithTarpsCount>1</FlatbedWithTarpsCount>
    <FlatbedWithTeam>true</FlatbedWithTeam>
    <FlatbedWithTeamCount>1</FlatbedWithTeamCount>
    <FlatbedVanReefer>true</FlatbedVanReefer>
    <FlatbedVanReeferCount>1</FlatbedVanReeferCount>
    <FoodGradeTankTrailer>true</FoodGradeTankTrailer>
    <FoodGradeTankTrailerCount>1</FoodGradeTankTrailerCount>
    <FourToFiveCarHauler>true</FourToFiveCarHauler>
    <FourToFiveCarHaulerCount>1</FourToFiveCarHaulerCount>
    <FuelTankTrailer>true</FuelTankTrailer>
    <FuelTankTrailerCount>1</FuelTankTrailerCount>
    <GasCylinderTrailer>true</GasCylinderTrailer>
    <GasCylinderTrailerCount>1</GasCylinderTrailerCount>
    <GrainHopperTrailer>true</GrainHopperTrailer>
    <GrainHopperTrailerCount>1</GrainHopperTrailerCount>
    <HazmatTanker>true</HazmatTanker>
    <HazmatTankerCount>1</HazmatTankerCount>
    <HopperBottom>true</HopperBottom>
    <HopperBottomCount>1</HopperBottomCount>
    <HopperHighSide>true</HopperHighSide>
    <HopperHighSideCount>1</HopperHighSideCount>
    <HopperLowSide>true</HopperLowSide>
    <HopperLowSideCount>1</HopperLowSideCount>
    <HopperTrailer>true</HopperTrailer>
    <HopperTrailerCount>1</HopperTrailerCount>
    <HorseTrailer>true</HorseTrailer>
    <HorseTrailerCount>1</HorseTrailerCount>
    <HotshotTrailer>true</HotshotTrailer>
    <HotshotTrailerCount>1</HotshotTrailerCount>
    <InsulatedVanOrReefer>true</InsulatedVanOrReefer>
    <InsulatedVanOrReeferCount>1</InsulatedVanOrReeferCount>
    <Landoll>true</Landoll>
    <LandollCount>1</LandollCount>
    <LivestockTrailer>true</LivestockTrailer>
    <LivestockTrailerCount>1</LivestockTrailerCount>
    <LiveBottomTrailer>true</LiveBottomTrailer>
    <LiveBottomTrailerCount>1</LiveBottomTrailerCount>
    <LoggingTrailer>true</LoggingTrailer>
    <LoggingTrailerCount>1</LoggingTrailerCount>
    <Lowboy>true</Lowboy>
    <LowboyCount>1</LowboyCount>
    <LowboyOrRemGooseneck>true</LowboyOrRemGooseneck>
    <LowboyOrRemGooseneckCount>1</LowboyOrRemGooseneckCount>
    <LowboyOverdimension>true</LowboyOverdimension>
    <LowboyOverdimensionCount>1</LowboyOverdimensionCount>
    <MiniDeckTrailer>true</MiniDeckTrailer>
    <MiniDeckTrailerCount>1</MiniDeckTrailerCount>
    <MilkTankTrailer>true</MilkTankTrailer>
    <MilkTankTrailerCount>1</MilkTankTrailerCount>
    <MovingVan>true</MovingVan>
    <MovingVanCount>1</MovingVanCount>
    <MultiAxleHeavyHaulTrailer>true</MultiAxleHeavyHaulTrailer>
    <MultiAxleHeavyHaulTrailerCount>1</MultiAxleHeavyHaulTrailerCount>
    <MultiLevelCarHauler>true</MultiLevelCarHauler>
    <MultiLevelCarHaulerCount>1</MultiLevelCarHaulerCount>
    <OneToTwoCarHauler>true</OneToTwoCarHauler>
    <OneToTwoCarHaulerCount>1</OneToTwoCarHaulerCount>
    <PerimeterTrailer>true</PerimeterTrailer>
    <PerimeterTrailerCount>1</PerimeterTrailerCount>
    <PintleHitch>true</PintleHitch>
    <PintleHitchCount>1</PintleHitchCount>
    <PintleHitchTrailer>true</PintleHitchTrailer>
    <PintleHitchTrailerCount>1</PintleHitchTrailerCount>
    <PoleTrailer>true</PoleTrailer>
    <PoleTrailerCount>1</PoleTrailerCount>
    <Pneumatic>true</Pneumatic>
    <PneumaticCount>1</PneumaticCount>
    <PowerOnly>true</PowerOnly>
    <PowerOnlyCount>1</PowerOnlyCount>
    <Reefer>true</Reefer>
    <ReeferCount>1</ReeferCount>
    <ReeferAirRide>true</ReeferAirRide>
    <ReeferAirRideCount>1</ReeferAirRideCount>
    <ReeferDouble>true</ReeferDouble>
    <ReeferDoubleCount>1</ReeferDoubleCount>
    <ReeferHazMat>true</ReeferHazMat>
    <ReeferHazMatCount>1</ReeferHazMatCount>
    <ReeferIntermodal>true</ReeferIntermodal>
    <ReeferIntermodalCount>1</ReeferIntermodalCount>
    <ReeferLogistics>true</ReeferLogistics>
    <ReeferLogisticsCount>1</ReeferLogisticsCount>
    <ReeferOrVentedVan>true</ReeferOrVentedVan>
    <ReeferOrVentedVanCount>1</ReeferOrVentedVanCount>
    <ReeferPalletExchange>true</ReeferPalletExchange>
    <ReeferPalletExchangeCount>1</ReeferPalletExchangeCount>
    <ReeferSpecialized>true</ReeferSpecialized>
    <ReeferSpecializedCount>1</ReeferSpecializedCount>
    <ReeferStandard48Foot>true</ReeferStandard48Foot>
    <ReeferStandard48FootCount>1</ReeferStandard48FootCount>
    <ReeferStandard53Foot>true</ReeferStandard53Foot>
    <ReeferStandard53FootCount>1</ReeferStandard53FootCount>
    <ReeferWithTeam>true</ReeferWithTeam>
    <ReeferWithTeamCount>1</ReeferWithTeamCount>
    <RemovableGooseneck>true</RemovableGooseneck>
    <RemovableGooseneckCount>1</RemovableGooseneckCount>
    <SideDumpTrailer>true</SideDumpTrailer>
    <SideDumpTrailerCount>1</SideDumpTrailerCount>
    <SingleLevelCarHauler>true</SingleLevelCarHauler>
    <SingleLevelCarHaulerCount>1</SingleLevelCarHaulerCount>
    <SixToSevenCarHauler>true</SixToSevenCarHauler>
    <SixToSevenCarHaulerCount>1</SixToSevenCarHaulerCount>
    <StandardFlatbed48Foot>true</StandardFlatbed48Foot>
    <StandardFlatbed48FootCount>1</StandardFlatbed48FootCount>
    <StandardFlatbed53Foot>true</StandardFlatbed53Foot>
    <StandardFlatbed53FootCount>1</StandardFlatbed53FootCount>
    <SteerableStepDeckStretch>true</SteerableStepDeckStretch>
    <SteerableStepDeckStretchCount>1</SteerableStepDeckStretchCount>
    <StepDeck>true</StepDeck>
    <StepDeckCount>1</StepDeckCount>
    <StepDeckOrRemGooseneck>true</StepDeckOrRemGooseneck>
    <StepDeckOrRemGooseneckCount>1</StepDeckOrRemGooseneckCount>
    <StepDeckSpecialized>true</StepDeckSpecialized>
    <StepDeckSpecializedCount>1</StepDeckSpecializedCount>
    <StepDeckStandard48Foot>true</StepDeckStandard48Foot>
    <StepDeckStandard48FootCount>1</StepDeckStandard48FootCount>
    <StepDeckStandard53Foot>true</StepDeckStandard53Foot>
    <StepDeckStandard53FootCount>1</StepDeckStandard53FootCount>
    <StepdeckConestoga>true</StepdeckConestoga>
    <StepdeckConestogaCount>1</StepdeckConestogaCount>
    <StraightBoxTruck>true</StraightBoxTruck>
    <StraightBoxTruckCount>1</StraightBoxTruckCount>
    <StretchFlatbed>true</StretchFlatbed>
    <StretchFlatbedCount>1</StretchFlatbedCount>
    <StretchRGN>true</StretchRGN>
    <StretchRGNCount>1</StretchRGNCount>
    <StretchStepDeck>true</StretchStepDeck>
    <StretchStepDeckCount>1</StretchStepDeckCount>
    <StretchTrailer>true</StretchTrailer>
    <StretchTrailerCount>1</StretchTrailerCount>
    <TankerAluminum>true</TankerAluminum>
    <TankerAluminumCount>1</TankerAluminumCount>
    <TankerIntermodal>true</TankerIntermodal>
    <TankerIntermodalCount>1</TankerIntermodalCount>
    <TankerSteel>true</TankerSteel>
    <TankerSteelCount>1</TankerSteelCount>
    <ThreeCarHauler>true</ThreeCarHauler>
    <ThreeCarHaulerCount>1</ThreeCarHaulerCount>
    <TinWideTrailer>true</TinWideTrailer>
    <TinWideTrailerCount>1</TinWideTrailerCount>
    <Toter>true</Toter>
    <ToterCount>1</ToterCount>
    <TruckAndTrailer>true</TruckAndTrailer>
    <TruckAndTrailerCount>1</TruckAndTrailerCount>
    <Van>true</Van>
    <VanCount>1</VanCount>
    <VanAirRide>true</VanAirRide>
    <VanAirRideCount>1</VanAirRideCount>
    <VanBlanketWrap>true</VanBlanketWrap>
    <VanBlanketWrapCount>1</VanBlanketWrapCount>
    <VanConestoga>true</VanConestoga>
    <VanConestogaCount>1</VanConestogaCount>
    <VanDouble>true</VanDouble>
    <VanDoubleCount>1</VanDoubleCount>
    <VanHazMat>true</VanHazMat>
    <VanHazMatCount>1</VanHazMatCount>
    <VanHeated>true</VanHeated>
    <VanHeatedCount>1</VanHeatedCount>
    <VanHotshot>true</VanHotshot>
    <VanHotshotCount>1</VanHotshotCount>
    <VanInsulated>true</VanInsulated>
    <VanInsulatedCount>1</VanInsulatedCount>
    <VanIntermodal>true</VanIntermodal>
    <VanIntermodalCount>1</VanIntermodalCount>
    <VanLiftGate>true</VanLiftGate>
    <VanLiftGateCount>1</VanLiftGateCount>
    <VanLogistics>true</VanLogistics>
    <VanLogisticsCount>1</VanLogisticsCount>
    <VanOpenTop>true</VanOpenTop>
    <VanOpenTopCount>1</VanOpenTopCount>
    <VanOrFlatbed>true</VanOrFlatbed>
    <VanOrFlatbedCount>1</VanOrFlatbedCount>
    <VanOrFlatbedwTarps>true</VanOrFlatbedwTarps>
    <VanOrFlatbedwTarpsCount>1</VanOrFlatbedwTarpsCount>
    <VanOrReefer>true</VanOrReefer>
    <VanOrReeferCount>1</VanOrReeferCount>
    <VanPalletExchange>true</VanPalletExchange>
    <VanPalletExchangeCount>1</VanPalletExchangeCount>
    <VanRollerBed>true</VanRollerBed>
    <VanRollerBedCount>1</VanRollerBedCount>
    <VanSpecialized>true</VanSpecialized>
    <VanSpecializedCount>1</VanSpecializedCount>
    <VanSprinter>true</VanSprinter>
    <VanSprinterCount>1</VanSprinterCount>
    <VanStandard>true</VanStandard>
    <VanStandardCount>1</VanStandardCount>
    <VanTriple>true</VanTriple>
    <VanTripleCount>1</VanTripleCount>
    <VanVented>true</VanVented>
    <VanVentedCount>1</VanVentedCount>
    <VanWithCurtains>true</VanWithCurtains>
    <VanWithCurtainsCount>1</VanWithCurtainsCount>
    <VanWithTeam>true</VanWithTeam>
    <VanWithTeamCount>1</VanWithTeamCount>
    <WalkingFloorTrailer>true</WalkingFloorTrailer>
    <WalkingFloorTrailerCount>1</WalkingFloorTrailerCount>
  </CarrierTruckType>
  <CarrierW9Forms>
    <FullName>string</FullName>
    <BusinessName>string</BusinessName>
    <IndividualOrSingleMemberLLC>true</IndividualOrSingleMemberLLC>
    <CCorporation>true</CCorporation>
    <SCorporation>true</SCorporation>
    <Partnership>true</Partnership>
    <RequesterNameAddress>string</RequesterNameAddress>
    <TrustOrEstate>true</TrustOrEstate>
    <LimitedLiabilityCompany>true</LimitedLiabilityCompany>
    <TaxClassification>string</TaxClassification>
    <Other>true</Other>
    <OtherDetail>string</OtherDetail>
    <ExemptPayeeCode>string</ExemptPayeeCode>
    <ExemptionFATCACode>string</ExemptionFATCACode>
    <Address>string</Address>
    <CityStateZipCode>string</CityStateZipCode>
    <ListAccountNumber>string</ListAccountNumber>
    <SSN>string</SSN>
    <EIN>string</EIN>
    <SignatureDate>1970-01-01T00:00:00.001Z</SignatureDate>
    <SignaturePerson>string</SignaturePerson>
    <IsActive>true</IsActive>
    <City>string</City>
    <State>string</State>
    <ZipCode>string</ZipCode>
    <CarrierW9FormImages>
      <BlobName>string</BlobName>
      <CreatedDate>1970-01-01T00:00:00.001Z</CreatedDate>
      <FileName>string</FileName>
      <CreatedBy>string</CreatedBy>
    </CarrierW9FormImages>
  </CarrierW9Forms>
  <CarrierCertification>
    <Hazmat>true</Hazmat>
    <HazmatNumber>string</HazmatNumber>
    <SmartWay>true</SmartWay>
    <CARB>true</CARB>
    <TWIC>true</TWIC>
    <CTPATCertified>true</CTPATCertified>
    <CTPATSVINumber>string</CTPATSVINumber>
    <TankerEndorsed>true</TankerEndorsed>
    <TankerEndorsedNumOfDrivers>1</TankerEndorsedNumOfDrivers>
    <CBP>true</CBP>
    <CBSA>true</CBSA>
    <ANAM>true</ANAM>
    <ACE>true</ACE>
    <ACI>true</ACI>
    <CSA>true</CSA>
    <FAST>true</FAST>
    <PIP>true</PIP>
  </CarrierCertification>
  <AssureAdvantage>
    <CarrierDetails>
      <docketNumber>string</docketNumber>
      <dotNumber>
        <status>string</status>
        <Value>string</Value>
      </dotNumber>
      <carrierType>string</carrierType>
      <isMonitored>true</isMonitored>
      <isBlocked>true</isBlocked>
      <Identity>
        <legalName>string</legalName>
        <dbaName>string</dbaName>
        <businessStreet>string</businessStreet>
        <businessCity>string</businessCity>
        <businessState>string</businessState>
        <businessZipCode>string</businessZipCode>
        <businessColonia>string</businessColonia>
        <businessCountry>string</businessCountry>
        <businessPhone>string</businessPhone>
        <businessFax>string</businessFax>
        <mailingStreet>string</mailingStreet>
        <mailingCity>string</mailingCity>
        <mailingState>string</mailingState>
        <mailingZipCode>string</mailingZipCode>
        <mailingColonia>string</mailingColonia>
        <mailingCountry>string</mailingCountry>
        <mailingPhone>string</mailingPhone>
        <mailingFax>string</mailingFax>
        <undeliverableMail>string</undeliverableMail>
        <companyRep1>string</companyRep1>
        <companyRep2>string</companyRep2>
        <cellPhone>string</cellPhone>
        <emailAddress>string</emailAddress>
        <dunBradstreetNum>string</dunBradstreetNum>
        <organization>string</organization>
      </Identity>
      <Authority>
        <authGrantDate>string</authGrantDate>
        <commonAuthority>string</commonAuthority>
        <commonAuthorityPending>string</commonAuthorityPending>
        <commonAuthorityRevocation>string</commonAuthorityRevocation>
        <contractAuthority>string</contractAuthority>
        <contractAuthorityPending>string</contractAuthorityPending>
        <contractAuthorityRevocation>string</contractAuthorityRevocation>
        <brokerAuthority>string</brokerAuthority>
        <brokerAuthorityPending>string</brokerAuthorityPending>
        <brokerAuthorityRevocation>string</brokerAuthorityRevocation>
        <freight>string</freight>
        <passenger>string</passenger>
        <householdGoods>string</householdGoods>
        <private>string</private>
        <enterprise>string</enterprise>
      </Authority>
      <FMCSAInsurance>
        <bipdRequired>string</bipdRequired>
        <bipdOnFile>string</bipdOnFile>
        <cargoRequired>string</cargoRequired>
        <cargoOnFile>string</cargoOnFile>
        <bondSuretyRequired>string</bondSuretyRequired>
        <bondSuretyOnFile>string</bondSuretyOnFile>
        <PolicyList>
          <companyName>string</companyName>
          <attnToName>string</attnToName>
          <address>string</address>
          <city>string</city>
          <stateCode>string</stateCode>
          <postalCode>string</postalCode>
          <countryCode>string</countryCode>
          <phone>string</phone>
          <fax>string</fax>
          <insuranceType>string</insuranceType>
          <policyNumber>string</policyNumber>
          <postedDate>string</postedDate>
          <effectiveDate>string</effectiveDate>
          <cancelationDate>string</cancelationDate>
          <coverageFrom>string</coverageFrom>
          <coverageTo>string</coverageTo>
          <amBestRating>string</amBestRating>
        </PolicyList>
      </FMCSAInsurance>
      <CertData>
        <status>string</status>
        <noncoop>true</noncoop>
        <Certificate>
          <certificateID>string</certificateID>
          <producerName>string</producerName>
          <producerAddress>string</producerAddress>
          <producerCity>string</producerCity>
          <producerState>string</producerState>
          <producerZip>string</producerZip>
          <producerPhone>string</producerPhone>
          <producerFax>string</producerFax>
          <producerEmail>string</producerEmail>
          <paidFor>string</paidFor>
          <BlobName>string</BlobName>
          <Coverage>
            <insurerName>string</insurerName>
            <insurerAMBestRating>string</insurerAMBestRating>
            <type>string</type>
            <policyNumber>string</policyNumber>
            <expirationDate>string</expirationDate>
            <coverageLimit>string</coverageLimit>
            <deductable>string</deductable>
            <referBreakdown>string</referBreakdown>
            <referBreakDeduct>string</referBreakDeduct>
            <cancellationDate>string</cancellationDate>
          </Coverage>
        </Certificate>
      </CertData>
      <Safety>
        <rating>string</rating>
        <ratingDate>string</ratingDate>
        <unsafeDrvPCT>string</unsafeDrvPCT>
        <unsafeDrvOT>string</unsafeDrvOT>
        <unsafeDrvSV>string</unsafeDrvSV>
        <unsafeDrvAlert>string</unsafeDrvAlert>
        <unsafeDrvTrend>string</unsafeDrvTrend>
        <unsafeDrvCNT>1</unsafeDrvCNT>
        <hosPCT>string</hosPCT>
        <hosOT>string</hosOT>
        <hosSV>string</hosSV>
        <hosAlert>string</hosAlert>
        <hosTrend>string</hosTrend>
        <hosCNT>1</hosCNT>
        <drvFitPCT>string</drvFitPCT>
        <drvFitOT>string</drvFitOT>
        <drvFitSV>string</drvFitSV>
        <drvFitAlert>string</drvFitAlert>
        <drvFitTrend>string</drvFitTrend>
        <drvFitCNT>1</drvFitCNT>
        <controlSubPCT>string</controlSubPCT>
        <controlSubOT>string</controlSubOT>
        <controlSubSV>string</controlSubSV>
        <controlSubAlert>string</controlSubAlert>
        <controlSubTrend>string</controlSubTrend>
        <controlSubCNT>1</controlSubCNT>
        <vehMaintPCT>string</vehMaintPCT>
        <vehMaintOT>string</vehMaintOT>
        <vehMaintSV>string</vehMaintSV>
        <vehMaintAlert>string</vehMaintAlert>
        <vehMaintTrend>string</vehMaintTrend>
        <vehMaintCNT>1</vehMaintCNT>
        <hazMatPCT>string</hazMatPCT>
        <hazMatOT>string</hazMatOT>
        <hazMatSV>string</hazMatSV>
        <hazMatAlert>string</hazMatAlert>
        <hazMatTrend>string</hazMatTrend>
        <hazMatCNT>1</hazMatCNT>
      </Safety>
      <Inspection>
        <inspectVehUS>string</inspectVehUS>
        <inspectVehOOSUS>string</inspectVehOOSUS>
        <inspectVehOOSPctUS>string</inspectVehOOSPctUS>
        <inspectDrvUS>string</inspectDrvUS>
        <inspectDrvOOSUS>string</inspectDrvOOSUS>
        <inspectDrvOOSPctUS>string</inspectDrvOOSPctUS>
        <inspectHazUS>string</inspectHazUS>
        <inspectHazOOSUS>string</inspectHazOOSUS>
        <inspectHazOOSPctUS>string</inspectHazOOSPctUS>
        <inspectIEPUS>string</inspectIEPUS>
        <inspectIEPOOSUS>string</inspectIEPOOSUS>
        <inspectIEPOOSPctUS>string</inspectIEPOOSPctUS>
        <inspectTotalIEPUS>string</inspectTotalIEPUS>
        <inspectTotalUS>string</inspectTotalUS>
        <inspectVehCAN>string</inspectVehCAN>
        <inspectVehOOSCAN>string</inspectVehOOSCAN>
        <inspectVehOOSPctCAN>string</inspectVehOOSPctCAN>
        <inspectDrvCAN>string</inspectDrvCAN>
        <inspectDrvOOSCAN>string</inspectDrvOOSCAN>
        <inspectDrvOOSPctCAN>string</inspectDrvOOSPctCAN>
        <inspectTotalCAN>string</inspectTotalCAN>
      </Inspection>
      <Crash>
        <crashFatalUS>string</crashFatalUS>
        <crashInjuryUS>string</crashInjuryUS>
        <crashTowUS>string</crashTowUS>
        <crashTotalUS>string</crashTotalUS>
        <crashFatalCAN>string</crashFatalCAN>
        <crashInjuryCAN>string</crashInjuryCAN>
        <crashTowCAN>string</crashTowCAN>
        <crashTotalCAN>string</crashTotalCAN>
      </Crash>
      <Review>
        <reviewType>string</reviewType>
        <reviewDate>string</reviewDate>
        <reviewDocNum>string</reviewDocNum>
        <reviewMiles>string</reviewMiles>
        <mcs150Date>string</mcs150Date>
        <mcs150MileYear>string</mcs150MileYear>
        <mcs150Miles>string</mcs150Miles>
        <accidentRate>string</accidentRate>
        <accidentRatePrevent>string</accidentRatePrevent>
      </Review>
      <Operation>
        <dotAddDate>string</dotAddDate>
        <carrierOperation>string</carrierOperation>
        <shipperOperation>string</shipperOperation>
        <mxOperationType>string</mxOperationType>
        <mxRFCNumber>string</mxRFCNumber>
        <outOfService>string</outOfService>
        <outOfServiceDate>string</outOfServiceDate>
        <outOfServiceReason>string</outOfServiceReason>
        <entityCarrier>string</entityCarrier>
        <entityShipper>string</entityShipper>
        <entityBroker>string</entityBroker>
        <entityFreightFowarder>string</entityFreightFowarder>
        <entityCargoTank>string</entityCargoTank>
        <classAuthForHire>string</classAuthForHire>
        <classMigrant>string</classMigrant>
        <classIndianNation>string</classIndianNation>
        <classExemptForHire>string</classExemptForHire>
        <classUSMail>string</classUSMail>
        <classPrivateProperty>string</classPrivateProperty>
        <classFederalGovernment>string</classFederalGovernment>
        <classPrivPassBusiness>string</classPrivPassBusiness>
        <classStateGovernment>string</classStateGovernment>
        <classPrivPassNonBusiness>string</classPrivPassNonBusiness>
        <classLocalGovernment>string</classLocalGovernment>
        <classOther>string</classOther>
        <operatingStatus>string</operatingStatus>
      </Operation>
      <Cargo>
        <hazmatIndicator>string</hazmatIndicator>
        <cargoGenFreight>string</cargoGenFreight>
        <cargoHousehold>string</cargoHousehold>
        <cargoMetal>string</cargoMetal>
        <cargoMotorVeh>string</cargoMotorVeh>
        <cargoDriveTow>string</cargoDriveTow>
        <cargoLogPole>string</cargoLogPole>
        <cargoBldgMaterial>string</cargoBldgMaterial>
        <cargoMobileHome>string</cargoMobileHome>
        <cargoMachLarge>string</cargoMachLarge>
        <cargoProduce>string</cargoProduce>
        <cargoLiqGas>string</cargoLiqGas>
        <cargoIntermodal>string</cargoIntermodal>
        <cargoPassengers>string</cargoPassengers>
        <cargoOilfield>string</cargoOilfield>
        <cargoLivestock>string</cargoLivestock>
        <cargoGrainfeed>string</cargoGrainfeed>
        <cargoCoalcoke>string</cargoCoalcoke>
        <cargoMeat>string</cargoMeat>
        <cargoGarbage>string</cargoGarbage>
        <cargoUSMail>string</cargoUSMail>
        <cargoChemicals>string</cargoChemicals>
        <cargoDryBulk>string</cargoDryBulk>
        <cargoRefrigerated>string</cargoRefrigerated>
        <cargoBeverages>string</cargoBeverages>
        <cargoPaperProd>string</cargoPaperProd>
        <cargoUtilities>string</cargoUtilities>
        <cargoFarmSupplies>string</cargoFarmSupplies>
        <cargoConstruction>string</cargoConstruction>
        <cargoWaterwell>string</cargoWaterwell>
        <cargoOther>string</cargoOther>
        <cargoOtherDesc>string</cargoOtherDesc>
      </Cargo>
      <Drivers>
        <driversTotal>string</driversTotal>
        <driversAvgLeased>string</driversAvgLeased>
        <driversCDL>string</driversCDL>
        <driversInter>string</driversInter>
        <driversInterLT100>string</driversInterLT100>
        <driversInterGT100>string</driversInterGT100>
        <driversIntra>string</driversIntra>
        <driversIntraLT100>string</driversIntraLT100>
        <driversIntraGT100>string</driversIntraGT100>
      </Drivers>
      <Equipment>
        <trucksTotal>string</trucksTotal>
        <totalPower>string</totalPower>
        <fleetsize>string</fleetsize>
        <trucksOwned>string</trucksOwned>
        <trucksTerm>string</trucksTerm>
        <trucksTrip>string</trucksTrip>
        <trailersOwned>string</trailersOwned>
        <trailersTerm>string</trailersTerm>
        <trailersTrip>string</trailersTrip>
        <tractorsOwned>string</tractorsOwned>
        <tractorsTerm>string</tractorsTerm>
        <tractorsTrip>string</tractorsTrip>
      </Equipment>
      <Other>
        <carbTru>string</carbTru>
        <smartway>string</smartway>
        <watchdogReports>string</watchdogReports>
      </Other>
      <RiskAssessment>
        <Overall>string</Overall>
        <Authority>string</Authority>
        <Insurance>string</Insurance>
        <Safety>string</Safety>
        <Operation>string</Operation>
        <Other>string</Other>
      </RiskAssessment>
      <RiskAssessmentDetails>
        <IsIntrastateCarrier>true</IsIntrastateCarrier>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <ReviewState>string</ReviewState>
        <Authority>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Authority>
        <Insurance>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Insurance>
        <Safety>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Safety>
        <Operation>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Operation>
        <Other>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Other>
        <ReviewDetails>
          <ReviewID>1</ReviewID>
          <PreReviewOverall>string</PreReviewOverall>
          <PreReviewAuthority>string</PreReviewAuthority>
          <PreReviewInsurance>string</PreReviewInsurance>
          <PreReviewSafety>string</PreReviewSafety>
          <PreReviewOperation>string</PreReviewOperation>
          <PreReviewOther>string</PreReviewOther>
          <ReviewUser>string</ReviewUser>
          <ReviewDate>1970-01-01T00:00:00.001Z</ReviewDate>
          <ReviewReason>string</ReviewReason>
          <ReviewNote>string</ReviewNote>
          <ReviewExpirationDate>1970-01-01T00:00:00.001Z</ReviewExpirationDate>
        </ReviewDetails>
      </RiskAssessmentDetails>
      <CarrierRatings>
        <myRating>1</myRating>
        <totalRatings>1</totalRatings>
        <lowRatings>1</lowRatings>
        <avgRating>1.1</avgRating>
      </CarrierRatings>
      <LatestInvitation>
        <InvitedByUserName>string</InvitedByUserName>
        <InvitedByEmail>string</InvitedByEmail>
        <InvitedByFirstName>string</InvitedByFirstName>
        <InvitedByLastName>string</InvitedByLastName>
        <InvitationSentDate>1970-01-01T00:00:00.001Z</InvitationSentDate>
        <InvitationRecipient>string</InvitationRecipient>
      </LatestInvitation>
      <IncidentReports>
        <TotalIncidentReports>1</TotalIncidentReports>
        <TotalIncidentReportsWithFraud>1</TotalIncidentReportsWithFraud>
      </IncidentReports>
    </CarrierDetails>
    <ResponseDO>
      <status>string</status>
      <action>string</action>
      <code>string</code>
      <displayMsg>string</displayMsg>
      <techMsg>string</techMsg>
    </ResponseDO>
  </AssureAdvantage>
  <CarrierMode>
    <LessThanTruckLoad>true</LessThanTruckLoad>
    <Partial>true</Partial>
    <Truckload>true</Truckload>
    <Rail>true</Rail>
    <Intermodal>true</Intermodal>
    <Air>true</Air>
    <Expedite>true</Expedite>
    <Ocean>true</Ocean>
    <Drayage>true</Drayage>
  </CarrierMode>
  <CarrierELDProvider>
    <ComplianceStatusID>1</ComplianceStatusID>
    <ComplianceStatus>string</ComplianceStatus>
    <ProviderName>string</ProviderName>
    <ProviderIdentifier>string</ProviderIdentifier>
    <ExemptionID>1</ExemptionID>
    <Exemption>string</Exemption>
    <CompliantBy>string</CompliantBy>
  </CarrierELDProvider>
  <OwnerContactName>string</OwnerContactName>
  <OwnerContactPhone>string</OwnerContactPhone>
  <OwnerContactEmail>string</OwnerContactEmail>
  <CarrierTINMatchings>
    <TINTypeID>1</TINTypeID>
    <TIN>string</TIN>
    <TINName>string</TINName>
    <TINMatchingStatusID>1</TINMatchingStatusID>
    <TINMatchingResultID>1</TINMatchingResultID>
    <CreatedOnUtc>1970-01-01T00:00:00.001Z</CreatedOnUtc>
    <SubmittedOnUtc>1970-01-01T00:00:00.001Z</SubmittedOnUtc>
    <ProcessedOnUtc>1970-01-01T00:00:00.001Z</ProcessedOnUtc>
    <ContactEmail>string</ContactEmail>
    <ContactPhoneNumber>string</ContactPhoneNumber>
    <MatchingResult>string</MatchingResult>
    <MatchingStatus>string</MatchingStatus>
  </CarrierTINMatchings>
  <Message>string</Message>
</MyCarrierPacketsApi.DTOs.CarrierAADTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT number of the carrier. Example: 12345 | query | integer |
| DocketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierContacts)[/api/v1/Carrier/GetCarrierContacts](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierContacts)



    - [Retrieves a list of authorized and verified users for a carrier.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetCarrierContacts)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model \[\
\
Inline Model 1\
\
\]

Inline Model 1 {

Success (boolean, optional),

Message (string, optional),

Carrier (MyCarrierPacketsDomain.CarrierContacts.Carrier, optional)

}

MyCarrierPacketsDomain.CarrierContacts.Carrier {

DOTNumber (integer, optional),

DocketNumber (string, optional),

LegalName (string, optional),

DBAName (string, optional),

Contacts (Array\[MyCarrierPacketsDomain.CarrierContacts.CarrierContact\], optional)

}

MyCarrierPacketsDomain.CarrierContacts.CarrierContact {

FirstName (string, optional),

LastName (string, optional),

Title (string, optional),

Phone (string, optional),

Email (string, optional),

AuthorizedForPackets (boolean, optional),

VerificationStatus (string, optional)

}

```
[\
  {\
    "Success": true,\
    "Message": "string",\
    "Carrier": {\
      "DOTNumber": 0,\
      "DocketNumber": "string",\
      "LegalName": "string",\
      "DBAName": "string",\
      "Contacts": [\
        {\
          "FirstName": "string",\
          "LastName": "string",\
          "Title": "string",\
          "Phone": "string",\
          "Email": "string",\
          "AuthorizedForPackets": true,\
          "VerificationStatus": "string"\
        }\
      ]\
    }\
  }\
]
```

```
<?xml version="1.0"?>
<Inline Model>
  <Success>true</Success>
  <Message>string</Message>
  <Carrier>
    <DOTNumber>1</DOTNumber>
    <DocketNumber>string</DocketNumber>
    <LegalName>string</LegalName>
    <DBAName>string</DBAName>
    <Contacts>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Title>string</Title>
      <Phone>string</Phone>
      <Email>string</Email>
      <AuthorizedForPackets>true</AuthorizedForPackets>
      <VerificationStatus>string</VerificationStatus>
    </Contacts>
  </Carrier>
</Inline Model>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT number of the carrier. For example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_FindAssociatedCarriers)[/api/v1/Carrier/FindAssociatedCarriers](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_FindAssociatedCarriers)



    - [Searches carrier contact sources within MCP/FMCSA for associated carriers.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_FindAssociatedCarriers)

#### Implementation Notes

This method searches for carriers associated with the given phone number or email address.

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.FindAssociatedCarriersDTO {

Success (boolean, optional),

Message (string, optional),

AssociatedCarriersCount (integer, optional),

AssociatedCarriers (Array\[MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.AssociatedCarriersDTO\], optional):
The list of associated carriers.

}

MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.AssociatedCarriersDTO {

DOTNumber (integer, optional),

DocketNumber (string, optional),

CompanyName (string, optional),

DBAName (string, optional),

Street (string, optional),

City (string, optional),

State (string, optional),

ZipCode (string, optional),

Country (string, optional),

Phone (string, optional),

PhoneAssociationTypes (Array\[MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.AssociationTypeDTO\], optional),

EmailAssociationTypes (Array\[MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.AssociationTypeDTO\], optional)

}

MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.AssociationTypeDTO {

AssociationType (integer, optional):
Value/Type List: 1 = Company, 2 = Support, 3 = Claims, 4 = SafetyManager, 5 = DispatchService, 6 = Owner, 7 = AvailableLoads, 8 = AuthorizedUser, 9 = UserAuthorizationPending, 10 = UserAuthorizationDenied, 11 = UserAuthorizationFollowUp, 12 = VerifiedUser, 13 = UserVerificationPending, 14 = UserVerificationDenied, 15 = UserVerificationFollowUp, 16 = Driver, 17 = Dispatcher, 18 = MCRecord, 19 = DOTRecord; Value Only List:
= \['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'\]

| integer |
| --- |
| Enum: | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 |

,

Description (string, optional)

}

```
{
  "Success": true,
  "Message": "string",
  "AssociatedCarriersCount": 0,
  "AssociatedCarriers": [\
    {\
      "DOTNumber": 0,\
      "DocketNumber": "string",\
      "CompanyName": "string",\
      "DBAName": "string",\
      "Street": "string",\
      "City": "string",\
      "State": "string",\
      "ZipCode": "string",\
      "Country": "string",\
      "Phone": "string",\
      "PhoneAssociationTypes": [\
        {\
          "AssociationType": 1,\
          "Description": "string"\
        }\
      ],\
      "EmailAssociationTypes": [\
        {\
          "AssociationType": 1,\
          "Description": "string"\
        }\
      ]\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.FindAssociatedCarriersDTO>
  <Success>true</Success>
  <Message>string</Message>
  <AssociatedCarriersCount>1</AssociatedCarriersCount>
  <AssociatedCarriers>
    <DOTNumber>1</DOTNumber>
    <DocketNumber>string</DocketNumber>
    <CompanyName>string</CompanyName>
    <DBAName>string</DBAName>
    <Street>string</Street>
    <City>string</City>
    <State>string</State>
    <ZipCode>string</ZipCode>
    <Country>string</Country>
    <Phone>string</Phone>
    <PhoneAssociationTypes>
      <AssociationType>1</AssociationType>
      <Description>string</Description>
    </PhoneAssociationTypes>
    <EmailAssociationTypes>
      <AssociationType>1</AssociationType>
      <Description>string</Description>
    </EmailAssociationTypes>
  </AssociatedCarriers>
</MyCarrierPacketsApi.DTOs.FindAssociatedCarriers.FindAssociatedCarriersDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| phone |  | The phone number to search for associated carriers. | query | string |
| email |  | The email address to search for associated carriers. | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierIncidentReports)[/api/v1/Carrier/GetCarrierIncidentReports](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierIncidentReports)



    - [Retrieves incident report details for a given carrier.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetCarrierIncidentReports)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.CarrierIncidentReportDTO {

DOTNumber (integer, optional),

DocketNumber (string, optional),

LegalName (string, optional),

DBAName (string, optional),

IncidentReports (Array\[MyCarrierPacketsApi.DTOs.CarrierIncidentReportDetailDTO\], optional)

}

MyCarrierPacketsApi.DTOs.CarrierIncidentReportDetailDTO {

IncidentDate (string, optional),

OriginCity (string, optional),

OriginStateProvinceName (string, optional),

OriginCountryName (string, optional),

DestinationCity (string, optional),

DestinationStateProvinceName (string, optional),

DestinationCountryName (string, optional),

ReportedByCompany (string, optional),

CarrierEmails (string, optional),

CreatedBy (string, optional),

CreatedDate (string, optional),

ModifiedBy (string, optional),

ModifiedDate (string, optional),

IncidentTypes (Array\[string\], optional),

Comments (Array\[MyCarrierPacketsApi.DTOs.CarrierIncidentReportCommentDTO\], optional)

}

MyCarrierPacketsApi.DTOs.CarrierIncidentReportCommentDTO {

CommenterType (string, optional),

CommentBy (string, optional),

CommentDate (string, optional),

Comment (string, optional)

}

```
{
  "DOTNumber": 0,
  "DocketNumber": "string",
  "LegalName": "string",
  "DBAName": "string",
  "IncidentReports": [\
    {\
      "IncidentDate": "string",\
      "OriginCity": "string",\
      "OriginStateProvinceName": "string",\
      "OriginCountryName": "string",\
      "DestinationCity": "string",\
      "DestinationStateProvinceName": "string",\
      "DestinationCountryName": "string",\
      "ReportedByCompany": "string",\
      "CarrierEmails": "string",\
      "CreatedBy": "string",\
      "CreatedDate": "2026-05-17T23:54:51.298Z",\
      "ModifiedBy": "string",\
      "ModifiedDate": "2026-05-17T23:54:51.298Z",\
      "IncidentTypes": [\
        "string"\
      ],\
      "Comments": [\
        {\
          "CommenterType": "string",\
          "CommentBy": "string",\
          "CommentDate": "2026-05-17T23:54:51.298Z",\
          "Comment": "string"\
        }\
      ]\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.CarrierIncidentReportDTO>
  <DOTNumber>1</DOTNumber>
  <DocketNumber>string</DocketNumber>
  <LegalName>string</LegalName>
  <DBAName>string</DBAName>
  <IncidentReports>
    <IncidentDate>string</IncidentDate>
    <OriginCity>string</OriginCity>
    <OriginStateProvinceName>string</OriginStateProvinceName>
    <OriginCountryName>string</OriginCountryName>
    <DestinationCity>string</DestinationCity>
    <DestinationStateProvinceName>string</DestinationStateProvinceName>
    <DestinationCountryName>string</DestinationCountryName>
    <ReportedByCompany>string</ReportedByCompany>
    <CarrierEmails>string</CarrierEmails>
    <CreatedBy>string</CreatedBy>
    <CreatedDate>1970-01-01T00:00:00.001Z</CreatedDate>
    <ModifiedBy>string</ModifiedBy>
    <ModifiedDate>1970-01-01T00:00:00.001Z</ModifiedDate>
    <IncidentTypes>string</IncidentTypes>
    <Comments>
      <CommenterType>string</CommenterType>
      <CommentBy>string</CommentBy>
      <CommentDate>1970-01-01T00:00:00.001Z</CommentDate>
      <Comment>string</Comment>
    </Comments>
  </IncidentReports>
</MyCarrierPacketsApi.DTOs.CarrierIncidentReportDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT number of the carrier.For example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierVINVerifications)[/api/v1/Carrier/GetCarrierVINVerifications](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierVINVerifications)



    - [Retrieves Carrier VIN Verification status details.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetCarrierVINVerifications)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.CarrierVINVerificationDTO {

DOTNumber (integer, optional),

DocketNumber (string, optional),

LegalName (string, optional),

DBAName (string, optional),

VINVerifications (Array\[MyCarrierPacketsApi.DTOs.CarrierVINVerificationDetailDTO\], optional)

}

MyCarrierPacketsApi.DTOs.CarrierVINVerificationDetailDTO {

VIN (string, optional),

VINVerificationStatus (MyCarrierPacketsApi.DTOs.VINVerificationStatusDTO, optional),

CreatedOnUtc (string, optional),

ModifiedOnUtc (string, optional),

OtherCarrier (MyCarrierPacketsApi.DTOs.CarrierVINVerificationDetailOtherCarrierDTO, optional),

Requests (Array\[MyCarrierPacketsApi.DTOs.CarrierVINVerificationRequestDTO\], optional)

}

MyCarrierPacketsApi.DTOs.VINVerificationStatusDTO {

StatusID (integer, optional),

Description (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierVINVerificationDetailOtherCarrierDTO {

DOTNumber (integer, optional),

DocketNumber (string, optional),

CompanyName (string, optional),

DBAName (string, optional),

Street (string, optional),

City (string, optional),

StateProvince (string, optional),

Zipcode (string, optional),

Country (string, optional),

Phone (string, optional)

}

MyCarrierPacketsApi.DTOs.CarrierVINVerificationRequestDTO {

RequestSentTo (string, optional),

RequestedByUser (string, optional),

RequestedDateTime (string, optional),

ImageUploadedByFirstName (string, optional),

ImageUploadedByLastName (string, optional),

ImageUploadedFromIPAddress (string, optional),

ImageUploadedDateTime (string, optional),

ImageFileName (string, optional),

ImageBlobName (string, optional),

VIN (string, optional),

VINVerificationStatus (MyCarrierPacketsApi.DTOs.VINVerificationStatusDTO, optional),

OtherCarrier (MyCarrierPacketsApi.DTOs.CarrierVINVerificationDetailOtherCarrierDTO, optional)

}

```
{
  "DOTNumber": 0,
  "DocketNumber": "string",
  "LegalName": "string",
  "DBAName": "string",
  "VINVerifications": [\
    {\
      "VIN": "string",\
      "VINVerificationStatus": {\
        "StatusID": 0,\
        "Description": "string"\
      },\
      "CreatedOnUtc": "2026-05-17T23:54:51.300Z",\
      "ModifiedOnUtc": "2026-05-17T23:54:51.300Z",\
      "OtherCarrier": {\
        "DOTNumber": 0,\
        "DocketNumber": "string",\
        "CompanyName": "string",\
        "DBAName": "string",\
        "Street": "string",\
        "City": "string",\
        "StateProvince": "string",\
        "Zipcode": "string",\
        "Country": "string",\
        "Phone": "string"\
      },\
      "Requests": [\
        {\
          "RequestSentTo": "string",\
          "RequestedByUser": "string",\
          "RequestedDateTime": "2026-05-17T23:54:51.300Z",\
          "ImageUploadedByFirstName": "string",\
          "ImageUploadedByLastName": "string",\
          "ImageUploadedFromIPAddress": "string",\
          "ImageUploadedDateTime": "2026-05-17T23:54:51.300Z",\
          "ImageFileName": "string",\
          "ImageBlobName": "string",\
          "VIN": "string",\
          "VINVerificationStatus": {\
            "StatusID": 0,\
            "Description": "string"\
          },\
          "OtherCarrier": {\
            "DOTNumber": 0,\
            "DocketNumber": "string",\
            "CompanyName": "string",\
            "DBAName": "string",\
            "Street": "string",\
            "City": "string",\
            "StateProvince": "string",\
            "Zipcode": "string",\
            "Country": "string",\
            "Phone": "string"\
          }\
        }\
      ]\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.CarrierVINVerificationDTO>
  <DOTNumber>1</DOTNumber>
  <DocketNumber>string</DocketNumber>
  <LegalName>string</LegalName>
  <DBAName>string</DBAName>
  <VINVerifications>
    <VIN>string</VIN>
    <VINVerificationStatus>
      <StatusID>1</StatusID>
      <Description>string</Description>
    </VINVerificationStatus>
    <CreatedOnUtc>1970-01-01T00:00:00.001Z</CreatedOnUtc>
    <ModifiedOnUtc>1970-01-01T00:00:00.001Z</ModifiedOnUtc>
    <OtherCarrier>
      <DOTNumber>1</DOTNumber>
      <DocketNumber>string</DocketNumber>
      <CompanyName>string</CompanyName>
      <DBAName>string</DBAName>
      <Street>string</Street>
      <City>string</City>
      <StateProvince>string</StateProvince>
      <Zipcode>string</Zipcode>
      <Country>string</Country>
      <Phone>string</Phone>
    </OtherCarrier>
    <Requests>
      <RequestSentTo>string</RequestSentTo>
      <RequestedByUser>string</RequestedByUser>
      <RequestedDateTime>1970-01-01T00:00:00.001Z</RequestedDateTime>
      <ImageUploadedByFirstName>string</ImageUploadedByFirstName>
      <ImageUploadedByLastName>string</ImageUploadedByLastName>
      <ImageUploadedFromIPAddress>string</ImageUploadedFromIPAddress>
      <ImageUploadedDateTime>1970-01-01T00:00:00.001Z</ImageUploadedDateTime>
      <ImageFileName>string</ImageFileName>
      <ImageBlobName>string</ImageBlobName>
      <VIN>string</VIN>
      <VINVerificationStatus>
        <StatusID>1</StatusID>
        <Description>string</Description>
      </VINVerificationStatus>
      <OtherCarrier>
        <DOTNumber>1</DOTNumber>
        <DocketNumber>string</DocketNumber>
        <CompanyName>string</CompanyName>
        <DBAName>string</DBAName>
        <Street>string</Street>
        <City>string</City>
        <StateProvince>string</StateProvince>
        <Zipcode>string</Zipcode>
        <Country>string</Country>
        <Phone>string</Phone>
      </OtherCarrier>
    </Requests>
  </VINVerifications>
</MyCarrierPacketsApi.DTOs.CarrierVINVerificationDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT number of the carrier.For example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetMonitoredCarrierContactsData)[/api/v1/Carrier/GetMonitoredCarrierContactsData](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetMonitoredCarrierContactsData)



    - [Retrieves a list of authorized and verified users for every carrier in the monitored list.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetMonitoredCarrierContactsData)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.MonitoredCarriersContactsDataDTO {

pageNumber (integer, optional),

pageSize (integer, optional),

totalPages (integer, optional),

totalCount (integer, optional),

succeeded (boolean, optional),

message (string, optional),

data (Array\[MyCarrierPacketsApi.DTOs.MonitoredCarriersContacts\], optional)

}

MyCarrierPacketsApi.DTOs.MonitoredCarriersContacts {

DOTNumber (integer, optional),

DocketNumber (string, optional),

LegalName (string, optional),

DBAName (string, optional),

CarriersContacts (Array\[MyCarrierPacketsApi.DTOs.MonitoredCarriersContact\], optional),

Success (boolean, optional),

Messages (Array\[string\], optional)

}

MyCarrierPacketsApi.DTOs.MonitoredCarriersContact {

FirstName (string, optional),

LastName (string, optional),

Title (string, optional),

Phone (string, optional),

Email (string, optional),

AuthorizedForPackets (boolean, optional),

VerificationStatus (string, optional)

}

```
{
  "pageNumber": 0,
  "pageSize": 0,
  "totalPages": 0,
  "totalCount": 0,
  "succeeded": true,
  "message": "string",
  "data": [\
    {\
      "DOTNumber": 0,\
      "DocketNumber": "string",\
      "LegalName": "string",\
      "DBAName": "string",\
      "CarriersContacts": [\
        {\
          "FirstName": "string",\
          "LastName": "string",\
          "Title": "string",\
          "Phone": "string",\
          "Email": "string",\
          "AuthorizedForPackets": true,\
          "VerificationStatus": "string"\
        }\
      ],\
      "Success": true,\
      "Messages": [\
        "string"\
      ]\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.MonitoredCarriersContactsDataDTO>
  <pageNumber>1</pageNumber>
  <pageSize>1</pageSize>
  <totalPages>1</totalPages>
  <totalCount>1</totalCount>
  <succeeded>true</succeeded>
  <message>string</message>
  <data>
    <DOTNumber>1</DOTNumber>
    <DocketNumber>string</DocketNumber>
    <LegalName>string</LegalName>
    <DBAName>string</DBAName>
    <CarriersContacts>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Title>string</Title>
      <Phone>string</Phone>
      <Email>string</Email>
      <AuthorizedForPackets>true</AuthorizedForPackets>
      <VerificationStatus>string</VerificationStatus>
    </CarriersContacts>
    <Success>true</Success>
    <Messages>string</Messages>
  </data>
</MyCarrierPacketsApi.DTOs.MonitoredCarriersContactsDataDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| pageNumber |  | The current page number. | query | integer |
| pageSize |  | The number of carriers returned per page. The recommended and default value is 250. The max is 500. | query | integer |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetDocument)[/api/v1/Carrier/GetDocument](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetDocument)



    - [Pulls PDF documents so the TMS/customer can store them locally for their records.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetDocument)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model {}

```
{}
```

Response Content Typeapplication/jsontext/json

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| name |  | **The name of the document. Example: company-agreement/12/f9f10ed2-799a-4521-a09b-19fb088e16c2** | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_EmailPacketInvitation)[/api/v1/Carrier/EmailPacketInvitation](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_EmailPacketInvitation)



    - [Sends an email with a packet to the carrier based on set parameters.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_EmailPacketInvitation)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model {}

```
{}
```

Response Content Typeapplication/jsontext/json

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| carrierEmail |  | **Email of the carrier. Example: abc@somedomain.com** | query | string |
| dotNumber |  | DOT number of the carrier. Example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| userName |  | Username of the customer. Optional parameter. Example: abc | query | string |
| sendConfirmationEmail | true  false | Indicates whether or not to send a confirmation email that the invitation was sent. Optional Parameter. | query | boolean |
| notificationEmails |  | Comma-separated list of additional emails to notify. Example: notify1@domain.com, notify2@domain.com | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_RequestUserVerification)[/api/v1/Carrier/RequestUserVerification](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_RequestUserVerification)



    - [Requests user verification (non-onboarding Intellivite).](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_RequestUserVerification)

#### Implementation Notes

Remarks

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model {}

```
{}
```

Response Content Typeapplication/jsontext/json

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| userVerificationEmail |  | **Email of the user. Example: abc@somedomain.com** | query | string |
| dotNumber |  | DOT number of the carrier. Example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| userName |  | Username of the customer. Optional parameter. Example: abc | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_RequestVINVerification)[/api/v1/Carrier/RequestVINVerification](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_RequestVINVerification)



    - [Requests Vehicle Identification Number (VIN) verification.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_RequestVINVerification)

#### Implementation Notes

VIN validation requests are sent via text message only. Email VIN validations are no longer supported.

#### Response Class (Status 200)

Returns either a plain text string containing a message when outputVINVerificationRequestID is false, or an object with 'VinVerificationRequestID' and 'Message' when outputVINVerificationRequestID is true.

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.RequestVINVerificationOutput {

VinVerificationRequestID (integer, optional),

Message (string, optional)

}

```
{
  "VinVerificationRequestID": 0,
  "Message": "string"
}
```

Response Content Typeapplication/jsontext/json

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| deliveryOption | 1  2 | **Method for sending the request. Only PhoneNumber (2) is supported.Value/Type List: 1 = Email, 2 = PhoneNumber; Value Only List:** | query | integer |
| vinVerificationEmail |  | Not used. Email VIN validations are no longer supported. | query | string |
| vinVerificationPhoneNumber |  | Phone number to send the request to | query | string |
| dotNumber |  | DOT number of the carrier. Example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC12345 | query | string |
| userName |  | Username of the customer. Optional parameter. Example: abc | query | string |
| outputVINVerificationRequestID | true  false | Output VIN Verification Request ID. Example: false | query | boolean |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_CompletedPackets)[/api/v1/Carrier/CompletedPackets](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_CompletedPackets)



    - [Displays carriers that have completed packets within a specified date range.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_CompletedPackets)

#### Implementation Notes

Common practice is to poll this API every 5-15 minutes.

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model \[\
\
Inline Model 1\
\
\]

Inline Model 1 {

DOTNumber (integer, optional),

DocketNumber (string, optional),

LegalName (string, optional),

CompletedDate (string, optional)

}

```
[\
  {\
    "DOTNumber": 0,\
    "DocketNumber": "string",\
    "LegalName": "string",\
    "CompletedDate": "2026-05-17T23:54:51.314Z"\
  }\
]
```

```
<?xml version="1.0"?>
<Inline Model>
  <DOTNumber>1</DOTNumber>
  <DocketNumber>string</DocketNumber>
  <LegalName>string</LegalName>
  <CompletedDate>1970-01-01T00:00:00.001Z</CompletedDate>
</Inline Model>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| fromDate |  | **From Date. Example: 2021-07-01T01:00:00** | query | date-time |
| toDate |  | **To Date. Required parameter. Example: 2021-07-01T14:00:00** | query | date-time |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_CarriersChanges)[/api/v1/Carrier/CarriersChanges](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_CarriersChanges)



    - [Monitors changes to carrier insurance, risk assessment, and other important details.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_CarriersChanges)

#### Implementation Notes

Common practice is to poll this API every 5-15 minutes.

If pagination parameters are not supplied, all carrier changes are returned. Otherwise, the number of carrier changes returned is limited to the pageSize.
If paging is requested, the response header will contain an "X-Pagination" item containing the details of the paged response.

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.CarrierChangesResultDTO {

FromDate (string, optional),

ToDate (string, optional),

RequestDateTimeUtc (string, optional),

InsuranceChangeCount (integer, optional),

FMCSAChangeCount (integer, optional),

RiskAssessmentChangeCount (integer, optional),

CarrierCount (integer, optional),

CarrierList (Array\[MyCarrierPacketsApi.FMCSA.FMCSACarrierChanged\], optional)

}

MyCarrierPacketsApi.FMCSA.FMCSACarrierChanged {

ChangeDateTime (string, optional),

ChangeCategories (Array\[string\], optional),

CarrierDetails (MyCarrierPacketsApi.FMCSA.CarrierDetails, optional),

ResponseDO (MyCarrierPacketsApi.DTOs.ResponseDO, optional)

}

MyCarrierPacketsApi.FMCSA.CarrierDetails {

docketNumber (string, optional),

dotNumber (MyCarrierPacketsApi.FMCSA.DotNumber, optional),

carrierType (string, optional),

isMonitored (boolean, optional),

isBlocked (boolean, optional),

Identity (MyCarrierPacketsApi.FMCSA.Identity, optional),

Authority (MyCarrierPacketsApi.FMCSA.Authority, optional),

FMCSAInsurance (MyCarrierPacketsApi.FMCSA.FMCSAInsurance, optional),

CertData (MyCarrierPacketsApi.FMCSA.CertData, optional),

Safety (MyCarrierPacketsApi.FMCSA.Safety, optional),

Inspection (MyCarrierPacketsApi.FMCSA.Inspection, optional),

Crash (MyCarrierPacketsApi.FMCSA.Crash, optional),

Review (MyCarrierPacketsApi.FMCSA.Review, optional),

Operation (MyCarrierPacketsApi.FMCSA.Operation, optional),

Cargo (MyCarrierPacketsApi.FMCSA.Cargo, optional),

Drivers (MyCarrierPacketsApi.FMCSA.Drivers, optional),

Equipment (MyCarrierPacketsApi.FMCSA.Equipment, optional),

Other (MyCarrierPacketsApi.FMCSA.Other, optional),

RiskAssessment (MyCarrierPacketsApi.FMCSA.RiskAssessment, optional),

RiskAssessmentDetails (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails, optional),

CarrierRatings (MyCarrierPacketsApi.FMCSA.CarrierRatings, optional),

LatestInvitation (MyCarrierPacketsApi.FMCSA.LatestInvitation, optional),

IncidentReports (MyCarrierPacketsApi.FMCSA.IncidentReports, optional)

}

MyCarrierPacketsApi.DTOs.ResponseDO {

status (string, optional),

action (string, optional),

code (string, optional),

displayMsg (string, optional),

techMsg (string, optional)

}

MyCarrierPacketsApi.FMCSA.DotNumber {

status (string, optional),

Value (string, optional)

}

MyCarrierPacketsApi.FMCSA.Identity {

legalName (string, optional),

dbaName (string, optional),

businessStreet (string, optional),

businessCity (string, optional),

businessState (string, optional),

businessZipCode (string, optional),

businessColonia (string, optional),

businessCountry (string, optional),

businessPhone (string, optional),

businessFax (string, optional),

mailingStreet (string, optional),

mailingCity (string, optional),

mailingState (string, optional),

mailingZipCode (string, optional),

mailingColonia (string, optional),

mailingCountry (string, optional),

mailingPhone (string, optional),

mailingFax (string, optional),

undeliverableMail (string, optional),

companyRep1 (string, optional),

companyRep2 (string, optional),

cellPhone (string, optional),

emailAddress (string, optional),

dunBradstreetNum (string, optional),

organization (string, optional)

}

MyCarrierPacketsApi.FMCSA.Authority {

authGrantDate (string, optional),

commonAuthority (string, optional),

commonAuthorityPending (string, optional),

commonAuthorityRevocation (string, optional),

contractAuthority (string, optional),

contractAuthorityPending (string, optional),

contractAuthorityRevocation (string, optional),

brokerAuthority (string, optional),

brokerAuthorityPending (string, optional),

brokerAuthorityRevocation (string, optional),

freight (string, optional),

passenger (string, optional),

householdGoods (string, optional),

private (string, optional),

enterprise (string, optional)

}

MyCarrierPacketsApi.FMCSA.FMCSAInsurance {

bipdRequired (string, optional),

bipdOnFile (string, optional),

cargoRequired (string, optional),

cargoOnFile (string, optional),

bondSuretyRequired (string, optional),

bondSuretyOnFile (string, optional),

PolicyList (Array\[MyCarrierPacketsApi.DTOs.PolicyOutput\], optional)

}

MyCarrierPacketsApi.FMCSA.CertData {

status (string, optional),

noncoop (boolean, optional),

Certificate (Array\[MyCarrierPacketsApi.DTOs.CertificateDTO\], optional)

}

MyCarrierPacketsApi.FMCSA.Safety {

rating (string, optional),

ratingDate (string, optional),

unsafeDrvPCT (string, optional),

unsafeDrvOT (string, optional),

unsafeDrvSV (string, optional),

unsafeDrvAlert (string, optional),

unsafeDrvTrend (string, optional),

unsafeDrvCNT (integer, optional),

hosPCT (string, optional),

hosOT (string, optional),

hosSV (string, optional),

hosAlert (string, optional),

hosTrend (string, optional),

hosCNT (integer, optional),

drvFitPCT (string, optional),

drvFitOT (string, optional),

drvFitSV (string, optional),

drvFitAlert (string, optional),

drvFitTrend (string, optional),

drvFitCNT (integer, optional),

controlSubPCT (string, optional),

controlSubOT (string, optional),

controlSubSV (string, optional),

controlSubAlert (string, optional),

controlSubTrend (string, optional),

controlSubCNT (integer, optional),

vehMaintPCT (string, optional),

vehMaintOT (string, optional),

vehMaintSV (string, optional),

vehMaintAlert (string, optional),

vehMaintTrend (string, optional),

vehMaintCNT (integer, optional),

hazMatPCT (string, optional),

hazMatOT (string, optional),

hazMatSV (string, optional),

hazMatAlert (string, optional),

hazMatTrend (string, optional),

hazMatCNT (integer, optional)

}

MyCarrierPacketsApi.FMCSA.Inspection {

inspectVehUS (string, optional),

inspectVehOOSUS (string, optional),

inspectVehOOSPctUS (string, optional),

inspectDrvUS (string, optional),

inspectDrvOOSUS (string, optional),

inspectDrvOOSPctUS (string, optional),

inspectHazUS (string, optional),

inspectHazOOSUS (string, optional),

inspectHazOOSPctUS (string, optional),

inspectIEPUS (string, optional),

inspectIEPOOSUS (string, optional),

inspectIEPOOSPctUS (string, optional),

inspectTotalIEPUS (string, optional),

inspectTotalUS (string, optional),

inspectVehCAN (string, optional),

inspectVehOOSCAN (string, optional),

inspectVehOOSPctCAN (string, optional),

inspectDrvCAN (string, optional),

inspectDrvOOSCAN (string, optional),

inspectDrvOOSPctCAN (string, optional),

inspectTotalCAN (string, optional)

}

MyCarrierPacketsApi.FMCSA.Crash {

crashFatalUS (string, optional),

crashInjuryUS (string, optional),

crashTowUS (string, optional),

crashTotalUS (string, optional),

crashFatalCAN (string, optional),

crashInjuryCAN (string, optional),

crashTowCAN (string, optional),

crashTotalCAN (string, optional)

}

MyCarrierPacketsApi.FMCSA.Review {

reviewType (string, optional),

reviewDate (string, optional),

reviewDocNum (string, optional),

reviewMiles (string, optional),

mcs150Date (string, optional),

mcs150MileYear (string, optional),

mcs150Miles (string, optional),

accidentRate (string, optional),

accidentRatePrevent (string, optional)

}

MyCarrierPacketsApi.FMCSA.Operation {

dotAddDate (string, optional),

carrierOperation (string, optional),

shipperOperation (string, optional),

mxOperationType (string, optional),

mxRFCNumber (string, optional),

outOfService (string, optional),

outOfServiceDate (string, optional),

outOfServiceReason (string, optional),

entityCarrier (string, optional),

entityShipper (string, optional),

entityBroker (string, optional),

entityFreightFowarder (string, optional),

entityCargoTank (string, optional),

classAuthForHire (string, optional),

classMigrant (string, optional),

classIndianNation (string, optional),

classExemptForHire (string, optional),

classUSMail (string, optional),

classPrivateProperty (string, optional),

classFederalGovernment (string, optional),

classPrivPassBusiness (string, optional),

classStateGovernment (string, optional),

classPrivPassNonBusiness (string, optional),

classLocalGovernment (string, optional),

classOther (string, optional),

operatingStatus (string, optional)

}

MyCarrierPacketsApi.FMCSA.Cargo {

hazmatIndicator (string, optional),

cargoGenFreight (string, optional),

cargoHousehold (string, optional),

cargoMetal (string, optional),

cargoMotorVeh (string, optional),

cargoDriveTow (string, optional),

cargoLogPole (string, optional),

cargoBldgMaterial (string, optional),

cargoMobileHome (string, optional),

cargoMachLarge (string, optional),

cargoProduce (string, optional),

cargoLiqGas (string, optional),

cargoIntermodal (string, optional),

cargoPassengers (string, optional),

cargoOilfield (string, optional),

cargoLivestock (string, optional),

cargoGrainfeed (string, optional),

cargoCoalcoke (string, optional),

cargoMeat (string, optional),

cargoGarbage (string, optional),

cargoUSMail (string, optional),

cargoChemicals (string, optional),

cargoDryBulk (string, optional),

cargoRefrigerated (string, optional),

cargoBeverages (string, optional),

cargoPaperProd (string, optional),

cargoUtilities (string, optional),

cargoFarmSupplies (string, optional),

cargoConstruction (string, optional),

cargoWaterwell (string, optional),

cargoOther (string, optional),

cargoOtherDesc (string, optional)

}

MyCarrierPacketsApi.FMCSA.Drivers {

driversTotal (string, optional),

driversAvgLeased (string, optional),

driversCDL (string, optional),

driversInter (string, optional),

driversInterLT100 (string, optional),

driversInterGT100 (string, optional),

driversIntra (string, optional),

driversIntraLT100 (string, optional),

driversIntraGT100 (string, optional)

}

MyCarrierPacketsApi.FMCSA.Equipment {

trucksTotal (string, optional),

totalPower (string, optional),

fleetsize (string, optional),

trucksOwned (string, optional),

trucksTerm (string, optional),

trucksTrip (string, optional),

trailersOwned (string, optional),

trailersTerm (string, optional),

trailersTrip (string, optional),

tractorsOwned (string, optional),

tractorsTerm (string, optional),

tractorsTrip (string, optional)

}

MyCarrierPacketsApi.FMCSA.Other {

carbTru (string, optional),

smartway (string, optional),

watchdogReports (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessment {

Overall (string, optional),

Authority (string, optional),

Insurance (string, optional),

Safety (string, optional),

Operation (string, optional),

Other (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails {

IsIntrastateCarrier (boolean, optional),

TotalPoints (integer, optional),

OverallRating (string, optional),

ReviewState (string, optional),

Authority (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Insurance (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Safety (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Operation (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Other (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

ReviewDetails (MyCarrierPacketsRiskAssessmentModels.ReviewDetails, optional)

}

MyCarrierPacketsApi.FMCSA.CarrierRatings {

myRating (integer, optional),

totalRatings (integer, optional),

lowRatings (integer, optional),

avgRating (number, optional)

}

MyCarrierPacketsApi.FMCSA.LatestInvitation {

InvitedByUserName (string, optional),

InvitedByEmail (string, optional),

InvitedByFirstName (string, optional),

InvitedByLastName (string, optional),

InvitationSentDate (string, optional),

InvitationRecipient (string, optional)

}

MyCarrierPacketsApi.FMCSA.IncidentReports {

TotalIncidentReports (integer, optional),

TotalIncidentReportsWithFraud (integer, optional)

}

MyCarrierPacketsApi.DTOs.PolicyOutput {

companyName (string, optional),

attnToName (string, optional),

address (string, optional),

city (string, optional),

stateCode (string, optional),

postalCode (string, optional),

countryCode (string, optional),

phone (string, optional),

fax (string, optional),

insuranceType (string, optional),

policyNumber (string, optional),

postedDate (string, optional),

effectiveDate (string, optional),

cancelationDate (string, optional),

coverageFrom (string, optional),

coverageTo (string, optional),

amBestRating (string, optional)

}

MyCarrierPacketsApi.DTOs.CertificateDTO {

certificateID (string, optional),

producerName (string, optional),

producerAddress (string, optional),

producerCity (string, optional),

producerState (string, optional),

producerZip (string, optional),

producerPhone (string, optional),

producerFax (string, optional),

producerEmail (string, optional),

paidFor (string, optional),

BlobName (string, optional),

Coverage (Array\[MyCarrierPacketsApi.DTOs.CoverageDTO\], optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail {

TotalPoints (integer, optional),

OverallRating (string, optional),

HasRuleOverride (boolean, optional, read only),

Infractions (Array\[MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction\], optional)

}

MyCarrierPacketsRiskAssessmentModels.ReviewDetails {

ReviewID (integer, optional),

PreReviewOverall (string, optional),

PreReviewAuthority (string, optional),

PreReviewInsurance (string, optional),

PreReviewSafety (string, optional),

PreReviewOperation (string, optional),

PreReviewOther (string, optional),

ReviewUser (string, optional),

ReviewDate (string, optional),

ReviewReason (string, optional),

ReviewNote (string, optional),

ReviewExpirationDate (string, optional)

}

MyCarrierPacketsApi.DTOs.CoverageDTO {

insurerName (string, optional),

insurerAMBestRating (string, optional),

type (string, optional),

policyNumber (string, optional),

expirationDate (string, optional),

coverageLimit (string, optional),

deductable (string, optional),

referBreakdown (string, optional),

referBreakDeduct (string, optional),

cancellationDate (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction {

Points (integer, optional),

RuleName (string, optional),

RiskLevel (string, optional),

RuleText (string, optional),

RuleOutput (string, optional),

PreReviewScore (integer, optional),

PreReviewRiskLevel (string, optional),

RuleEnforced (boolean, optional)

}

```
{
  "FromDate": "2026-05-17T23:54:51.316Z",
  "ToDate": "2026-05-17T23:54:51.316Z",
  "RequestDateTimeUtc": "2026-05-17T23:54:51.316Z",
  "InsuranceChangeCount": 0,
  "FMCSAChangeCount": 0,
  "RiskAssessmentChangeCount": 0,
  "CarrierCount": 0,
  "CarrierList": [\
    {\
      "ChangeDateTime": "2026-05-17T23:54:51.316Z",\
      "ChangeCategories": [\
        "string"\
      ],\
      "CarrierDetails": {\
        "docketNumber": "string",\
        "dotNumber": {\
          "status": "string",\
          "Value": "string"\
        },\
        "carrierType": "string",\
        "isMonitored": true,\
        "isBlocked": true,\
        "Identity": {\
          "legalName": "string",\
          "dbaName": "string",\
          "businessStreet": "string",\
          "businessCity": "string",\
          "businessState": "string",\
          "businessZipCode": "string",\
          "businessColonia": "string",\
          "businessCountry": "string",\
          "businessPhone": "string",\
          "businessFax": "string",\
          "mailingStreet": "string",\
          "mailingCity": "string",\
          "mailingState": "string",\
          "mailingZipCode": "string",\
          "mailingColonia": "string",\
          "mailingCountry": "string",\
          "mailingPhone": "string",\
          "mailingFax": "string",\
          "undeliverableMail": "string",\
          "companyRep1": "string",\
          "companyRep2": "string",\
          "cellPhone": "string",\
          "emailAddress": "string",\
          "dunBradstreetNum": "string",\
          "organization": "string"\
        },\
        "Authority": {\
          "authGrantDate": "string",\
          "commonAuthority": "string",\
          "commonAuthorityPending": "string",\
          "commonAuthorityRevocation": "string",\
          "contractAuthority": "string",\
          "contractAuthorityPending": "string",\
          "contractAuthorityRevocation": "string",\
          "brokerAuthority": "string",\
          "brokerAuthorityPending": "string",\
          "brokerAuthorityRevocation": "string",\
          "freight": "string",\
          "passenger": "string",\
          "householdGoods": "string",\
          "private": "string",\
          "enterprise": "string"\
        },\
        "FMCSAInsurance": {\
          "bipdRequired": "string",\
          "bipdOnFile": "string",\
          "cargoRequired": "string",\
          "cargoOnFile": "string",\
          "bondSuretyRequired": "string",\
          "bondSuretyOnFile": "string",\
          "PolicyList": [\
            {\
              "companyName": "string",\
              "attnToName": "string",\
              "address": "string",\
              "city": "string",\
              "stateCode": "string",\
              "postalCode": "string",\
              "countryCode": "string",\
              "phone": "string",\
              "fax": "string",\
              "insuranceType": "string",\
              "policyNumber": "string",\
              "postedDate": "string",\
              "effectiveDate": "string",\
              "cancelationDate": "string",\
              "coverageFrom": "string",\
              "coverageTo": "string",\
              "amBestRating": "string"\
            }\
          ]\
        },\
        "CertData": {\
          "status": "string",\
          "noncoop": true,\
          "Certificate": [\
            {\
              "certificateID": "string",\
              "producerName": "string",\
              "producerAddress": "string",\
              "producerCity": "string",\
              "producerState": "string",\
              "producerZip": "string",\
              "producerPhone": "string",\
              "producerFax": "string",\
              "producerEmail": "string",\
              "paidFor": "string",\
              "BlobName": "string",\
              "Coverage": [\
                {\
                  "insurerName": "string",\
                  "insurerAMBestRating": "string",\
                  "type": "string",\
                  "policyNumber": "string",\
                  "expirationDate": "string",\
                  "coverageLimit": "string",\
                  "deductable": "string",\
                  "referBreakdown": "string",\
                  "referBreakDeduct": "string",\
                  "cancellationDate": "string"\
                }\
              ]\
            }\
          ]\
        },\
        "Safety": {\
          "rating": "string",\
          "ratingDate": "string",\
          "unsafeDrvPCT": "string",\
          "unsafeDrvOT": "string",\
          "unsafeDrvSV": "string",\
          "unsafeDrvAlert": "string",\
          "unsafeDrvTrend": "string",\
          "unsafeDrvCNT": 0,\
          "hosPCT": "string",\
          "hosOT": "string",\
          "hosSV": "string",\
          "hosAlert": "string",\
          "hosTrend": "string",\
          "hosCNT": 0,\
          "drvFitPCT": "string",\
          "drvFitOT": "string",\
          "drvFitSV": "string",\
          "drvFitAlert": "string",\
          "drvFitTrend": "string",\
          "drvFitCNT": 0,\
          "controlSubPCT": "string",\
          "controlSubOT": "string",\
          "controlSubSV": "string",\
          "controlSubAlert": "string",\
          "controlSubTrend": "string",\
          "controlSubCNT": 0,\
          "vehMaintPCT": "string",\
          "vehMaintOT": "string",\
          "vehMaintSV": "string",\
          "vehMaintAlert": "string",\
          "vehMaintTrend": "string",\
          "vehMaintCNT": 0,\
          "hazMatPCT": "string",\
          "hazMatOT": "string",\
          "hazMatSV": "string",\
          "hazMatAlert": "string",\
          "hazMatTrend": "string",\
          "hazMatCNT": 0\
        },\
        "Inspection": {\
          "inspectVehUS": "string",\
          "inspectVehOOSUS": "string",\
          "inspectVehOOSPctUS": "string",\
          "inspectDrvUS": "string",\
          "inspectDrvOOSUS": "string",\
          "inspectDrvOOSPctUS": "string",\
          "inspectHazUS": "string",\
          "inspectHazOOSUS": "string",\
          "inspectHazOOSPctUS": "string",\
          "inspectIEPUS": "string",\
          "inspectIEPOOSUS": "string",\
          "inspectIEPOOSPctUS": "string",\
          "inspectTotalIEPUS": "string",\
          "inspectTotalUS": "string",\
          "inspectVehCAN": "string",\
          "inspectVehOOSCAN": "string",\
          "inspectVehOOSPctCAN": "string",\
          "inspectDrvCAN": "string",\
          "inspectDrvOOSCAN": "string",\
          "inspectDrvOOSPctCAN": "string",\
          "inspectTotalCAN": "string"\
        },\
        "Crash": {\
          "crashFatalUS": "string",\
          "crashInjuryUS": "string",\
          "crashTowUS": "string",\
          "crashTotalUS": "string",\
          "crashFatalCAN": "string",\
          "crashInjuryCAN": "string",\
          "crashTowCAN": "string",\
          "crashTotalCAN": "string"\
        },\
        "Review": {\
          "reviewType": "string",\
          "reviewDate": "string",\
          "reviewDocNum": "string",\
          "reviewMiles": "string",\
          "mcs150Date": "string",\
          "mcs150MileYear": "string",\
          "mcs150Miles": "string",\
          "accidentRate": "string",\
          "accidentRatePrevent": "string"\
        },\
        "Operation": {\
          "dotAddDate": "string",\
          "carrierOperation": "string",\
          "shipperOperation": "string",\
          "mxOperationType": "string",\
          "mxRFCNumber": "string",\
          "outOfService": "string",\
          "outOfServiceDate": "string",\
          "outOfServiceReason": "string",\
          "entityCarrier": "string",\
          "entityShipper": "string",\
          "entityBroker": "string",\
          "entityFreightFowarder": "string",\
          "entityCargoTank": "string",\
          "classAuthForHire": "string",\
          "classMigrant": "string",\
          "classIndianNation": "string",\
          "classExemptForHire": "string",\
          "classUSMail": "string",\
          "classPrivateProperty": "string",\
          "classFederalGovernment": "string",\
          "classPrivPassBusiness": "string",\
          "classStateGovernment": "string",\
          "classPrivPassNonBusiness": "string",\
          "classLocalGovernment": "string",\
          "classOther": "string",\
          "operatingStatus": "string"\
        },\
        "Cargo": {\
          "hazmatIndicator": "string",\
          "cargoGenFreight": "string",\
          "cargoHousehold": "string",\
          "cargoMetal": "string",\
          "cargoMotorVeh": "string",\
          "cargoDriveTow": "string",\
          "cargoLogPole": "string",\
          "cargoBldgMaterial": "string",\
          "cargoMobileHome": "string",\
          "cargoMachLarge": "string",\
          "cargoProduce": "string",\
          "cargoLiqGas": "string",\
          "cargoIntermodal": "string",\
          "cargoPassengers": "string",\
          "cargoOilfield": "string",\
          "cargoLivestock": "string",\
          "cargoGrainfeed": "string",\
          "cargoCoalcoke": "string",\
          "cargoMeat": "string",\
          "cargoGarbage": "string",\
          "cargoUSMail": "string",\
          "cargoChemicals": "string",\
          "cargoDryBulk": "string",\
          "cargoRefrigerated": "string",\
          "cargoBeverages": "string",\
          "cargoPaperProd": "string",\
          "cargoUtilities": "string",\
          "cargoFarmSupplies": "string",\
          "cargoConstruction": "string",\
          "cargoWaterwell": "string",\
          "cargoOther": "string",\
          "cargoOtherDesc": "string"\
        },\
        "Drivers": {\
          "driversTotal": "string",\
          "driversAvgLeased": "string",\
          "driversCDL": "string",\
          "driversInter": "string",\
          "driversInterLT100": "string",\
          "driversInterGT100": "string",\
          "driversIntra": "string",\
          "driversIntraLT100": "string",\
          "driversIntraGT100": "string"\
        },\
        "Equipment": {\
          "trucksTotal": "string",\
          "totalPower": "string",\
          "fleetsize": "string",\
          "trucksOwned": "string",\
          "trucksTerm": "string",\
          "trucksTrip": "string",\
          "trailersOwned": "string",\
          "trailersTerm": "string",\
          "trailersTrip": "string",\
          "tractorsOwned": "string",\
          "tractorsTerm": "string",\
          "tractorsTrip": "string"\
        },\
        "Other": {\
          "carbTru": "string",\
          "smartway": "string",\
          "watchdogReports": "string"\
        },\
        "RiskAssessment": {\
          "Overall": "string",\
          "Authority": "string",\
          "Insurance": "string",\
          "Safety": "string",\
          "Operation": "string",\
          "Other": "string"\
        },\
        "RiskAssessmentDetails": {\
          "IsIntrastateCarrier": true,\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "ReviewState": "string",\
          "Authority": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Insurance": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Safety": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Operation": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "Other": {\
            "TotalPoints": 0,\
            "OverallRating": "string",\
            "HasRuleOverride": true,\
            "Infractions": [\
              {\
                "Points": 0,\
                "RuleName": "string",\
                "RiskLevel": "string",\
                "RuleText": "string",\
                "RuleOutput": "string",\
                "PreReviewScore": 0,\
                "PreReviewRiskLevel": "string",\
                "RuleEnforced": true\
              }\
            ]\
          },\
          "ReviewDetails": {\
            "ReviewID": 0,\
            "PreReviewOverall": "string",\
            "PreReviewAuthority": "string",\
            "PreReviewInsurance": "string",\
            "PreReviewSafety": "string",\
            "PreReviewOperation": "string",\
            "PreReviewOther": "string",\
            "ReviewUser": "string",\
            "ReviewDate": "2026-05-17T23:54:51.316Z",\
            "ReviewReason": "string",\
            "ReviewNote": "string",\
            "ReviewExpirationDate": "2026-05-17T23:54:51.316Z"\
          }\
        },\
        "CarrierRatings": {\
          "myRating": 0,\
          "totalRatings": 0,\
          "lowRatings": 0,\
          "avgRating": 0\
        },\
        "LatestInvitation": {\
          "InvitedByUserName": "string",\
          "InvitedByEmail": "string",\
          "InvitedByFirstName": "string",\
          "InvitedByLastName": "string",\
          "InvitationSentDate": "2026-05-17T23:54:51.316Z",\
          "InvitationRecipient": "string"\
        },\
        "IncidentReports": {\
          "TotalIncidentReports": 0,\
          "TotalIncidentReportsWithFraud": 0\
        }\
      },\
      "ResponseDO": {\
        "status": "string",\
        "action": "string",\
        "code": "string",\
        "displayMsg": "string",\
        "techMsg": "string"\
      }\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.CarrierChangesResultDTO>
  <FromDate>1970-01-01T00:00:00.001Z</FromDate>
  <ToDate>1970-01-01T00:00:00.001Z</ToDate>
  <RequestDateTimeUtc>1970-01-01T00:00:00.001Z</RequestDateTimeUtc>
  <InsuranceChangeCount>1</InsuranceChangeCount>
  <FMCSAChangeCount>1</FMCSAChangeCount>
  <RiskAssessmentChangeCount>1</RiskAssessmentChangeCount>
  <CarrierCount>1</CarrierCount>
  <CarrierList>
    <ChangeDateTime>1970-01-01T00:00:00.001Z</ChangeDateTime>
    <ChangeCategories>string</ChangeCategories>
    <CarrierDetails>
      <docketNumber>string</docketNumber>
      <dotNumber>
        <status>string</status>
        <Value>string</Value>
      </dotNumber>
      <carrierType>string</carrierType>
      <isMonitored>true</isMonitored>
      <isBlocked>true</isBlocked>
      <Identity>
        <legalName>string</legalName>
        <dbaName>string</dbaName>
        <businessStreet>string</businessStreet>
        <businessCity>string</businessCity>
        <businessState>string</businessState>
        <businessZipCode>string</businessZipCode>
        <businessColonia>string</businessColonia>
        <businessCountry>string</businessCountry>
        <businessPhone>string</businessPhone>
        <businessFax>string</businessFax>
        <mailingStreet>string</mailingStreet>
        <mailingCity>string</mailingCity>
        <mailingState>string</mailingState>
        <mailingZipCode>string</mailingZipCode>
        <mailingColonia>string</mailingColonia>
        <mailingCountry>string</mailingCountry>
        <mailingPhone>string</mailingPhone>
        <mailingFax>string</mailingFax>
        <undeliverableMail>string</undeliverableMail>
        <companyRep1>string</companyRep1>
        <companyRep2>string</companyRep2>
        <cellPhone>string</cellPhone>
        <emailAddress>string</emailAddress>
        <dunBradstreetNum>string</dunBradstreetNum>
        <organization>string</organization>
      </Identity>
      <Authority>
        <authGrantDate>string</authGrantDate>
        <commonAuthority>string</commonAuthority>
        <commonAuthorityPending>string</commonAuthorityPending>
        <commonAuthorityRevocation>string</commonAuthorityRevocation>
        <contractAuthority>string</contractAuthority>
        <contractAuthorityPending>string</contractAuthorityPending>
        <contractAuthorityRevocation>string</contractAuthorityRevocation>
        <brokerAuthority>string</brokerAuthority>
        <brokerAuthorityPending>string</brokerAuthorityPending>
        <brokerAuthorityRevocation>string</brokerAuthorityRevocation>
        <freight>string</freight>
        <passenger>string</passenger>
        <householdGoods>string</householdGoods>
        <private>string</private>
        <enterprise>string</enterprise>
      </Authority>
      <FMCSAInsurance>
        <bipdRequired>string</bipdRequired>
        <bipdOnFile>string</bipdOnFile>
        <cargoRequired>string</cargoRequired>
        <cargoOnFile>string</cargoOnFile>
        <bondSuretyRequired>string</bondSuretyRequired>
        <bondSuretyOnFile>string</bondSuretyOnFile>
        <PolicyList>
          <companyName>string</companyName>
          <attnToName>string</attnToName>
          <address>string</address>
          <city>string</city>
          <stateCode>string</stateCode>
          <postalCode>string</postalCode>
          <countryCode>string</countryCode>
          <phone>string</phone>
          <fax>string</fax>
          <insuranceType>string</insuranceType>
          <policyNumber>string</policyNumber>
          <postedDate>string</postedDate>
          <effectiveDate>string</effectiveDate>
          <cancelationDate>string</cancelationDate>
          <coverageFrom>string</coverageFrom>
          <coverageTo>string</coverageTo>
          <amBestRating>string</amBestRating>
        </PolicyList>
      </FMCSAInsurance>
      <CertData>
        <status>string</status>
        <noncoop>true</noncoop>
        <Certificate>
          <certificateID>string</certificateID>
          <producerName>string</producerName>
          <producerAddress>string</producerAddress>
          <producerCity>string</producerCity>
          <producerState>string</producerState>
          <producerZip>string</producerZip>
          <producerPhone>string</producerPhone>
          <producerFax>string</producerFax>
          <producerEmail>string</producerEmail>
          <paidFor>string</paidFor>
          <BlobName>string</BlobName>
          <Coverage>
            <insurerName>string</insurerName>
            <insurerAMBestRating>string</insurerAMBestRating>
            <type>string</type>
            <policyNumber>string</policyNumber>
            <expirationDate>string</expirationDate>
            <coverageLimit>string</coverageLimit>
            <deductable>string</deductable>
            <referBreakdown>string</referBreakdown>
            <referBreakDeduct>string</referBreakDeduct>
            <cancellationDate>string</cancellationDate>
          </Coverage>
        </Certificate>
      </CertData>
      <Safety>
        <rating>string</rating>
        <ratingDate>string</ratingDate>
        <unsafeDrvPCT>string</unsafeDrvPCT>
        <unsafeDrvOT>string</unsafeDrvOT>
        <unsafeDrvSV>string</unsafeDrvSV>
        <unsafeDrvAlert>string</unsafeDrvAlert>
        <unsafeDrvTrend>string</unsafeDrvTrend>
        <unsafeDrvCNT>1</unsafeDrvCNT>
        <hosPCT>string</hosPCT>
        <hosOT>string</hosOT>
        <hosSV>string</hosSV>
        <hosAlert>string</hosAlert>
        <hosTrend>string</hosTrend>
        <hosCNT>1</hosCNT>
        <drvFitPCT>string</drvFitPCT>
        <drvFitOT>string</drvFitOT>
        <drvFitSV>string</drvFitSV>
        <drvFitAlert>string</drvFitAlert>
        <drvFitTrend>string</drvFitTrend>
        <drvFitCNT>1</drvFitCNT>
        <controlSubPCT>string</controlSubPCT>
        <controlSubOT>string</controlSubOT>
        <controlSubSV>string</controlSubSV>
        <controlSubAlert>string</controlSubAlert>
        <controlSubTrend>string</controlSubTrend>
        <controlSubCNT>1</controlSubCNT>
        <vehMaintPCT>string</vehMaintPCT>
        <vehMaintOT>string</vehMaintOT>
        <vehMaintSV>string</vehMaintSV>
        <vehMaintAlert>string</vehMaintAlert>
        <vehMaintTrend>string</vehMaintTrend>
        <vehMaintCNT>1</vehMaintCNT>
        <hazMatPCT>string</hazMatPCT>
        <hazMatOT>string</hazMatOT>
        <hazMatSV>string</hazMatSV>
        <hazMatAlert>string</hazMatAlert>
        <hazMatTrend>string</hazMatTrend>
        <hazMatCNT>1</hazMatCNT>
      </Safety>
      <Inspection>
        <inspectVehUS>string</inspectVehUS>
        <inspectVehOOSUS>string</inspectVehOOSUS>
        <inspectVehOOSPctUS>string</inspectVehOOSPctUS>
        <inspectDrvUS>string</inspectDrvUS>
        <inspectDrvOOSUS>string</inspectDrvOOSUS>
        <inspectDrvOOSPctUS>string</inspectDrvOOSPctUS>
        <inspectHazUS>string</inspectHazUS>
        <inspectHazOOSUS>string</inspectHazOOSUS>
        <inspectHazOOSPctUS>string</inspectHazOOSPctUS>
        <inspectIEPUS>string</inspectIEPUS>
        <inspectIEPOOSUS>string</inspectIEPOOSUS>
        <inspectIEPOOSPctUS>string</inspectIEPOOSPctUS>
        <inspectTotalIEPUS>string</inspectTotalIEPUS>
        <inspectTotalUS>string</inspectTotalUS>
        <inspectVehCAN>string</inspectVehCAN>
        <inspectVehOOSCAN>string</inspectVehOOSCAN>
        <inspectVehOOSPctCAN>string</inspectVehOOSPctCAN>
        <inspectDrvCAN>string</inspectDrvCAN>
        <inspectDrvOOSCAN>string</inspectDrvOOSCAN>
        <inspectDrvOOSPctCAN>string</inspectDrvOOSPctCAN>
        <inspectTotalCAN>string</inspectTotalCAN>
      </Inspection>
      <Crash>
        <crashFatalUS>string</crashFatalUS>
        <crashInjuryUS>string</crashInjuryUS>
        <crashTowUS>string</crashTowUS>
        <crashTotalUS>string</crashTotalUS>
        <crashFatalCAN>string</crashFatalCAN>
        <crashInjuryCAN>string</crashInjuryCAN>
        <crashTowCAN>string</crashTowCAN>
        <crashTotalCAN>string</crashTotalCAN>
      </Crash>
      <Review>
        <reviewType>string</reviewType>
        <reviewDate>string</reviewDate>
        <reviewDocNum>string</reviewDocNum>
        <reviewMiles>string</reviewMiles>
        <mcs150Date>string</mcs150Date>
        <mcs150MileYear>string</mcs150MileYear>
        <mcs150Miles>string</mcs150Miles>
        <accidentRate>string</accidentRate>
        <accidentRatePrevent>string</accidentRatePrevent>
      </Review>
      <Operation>
        <dotAddDate>string</dotAddDate>
        <carrierOperation>string</carrierOperation>
        <shipperOperation>string</shipperOperation>
        <mxOperationType>string</mxOperationType>
        <mxRFCNumber>string</mxRFCNumber>
        <outOfService>string</outOfService>
        <outOfServiceDate>string</outOfServiceDate>
        <outOfServiceReason>string</outOfServiceReason>
        <entityCarrier>string</entityCarrier>
        <entityShipper>string</entityShipper>
        <entityBroker>string</entityBroker>
        <entityFreightFowarder>string</entityFreightFowarder>
        <entityCargoTank>string</entityCargoTank>
        <classAuthForHire>string</classAuthForHire>
        <classMigrant>string</classMigrant>
        <classIndianNation>string</classIndianNation>
        <classExemptForHire>string</classExemptForHire>
        <classUSMail>string</classUSMail>
        <classPrivateProperty>string</classPrivateProperty>
        <classFederalGovernment>string</classFederalGovernment>
        <classPrivPassBusiness>string</classPrivPassBusiness>
        <classStateGovernment>string</classStateGovernment>
        <classPrivPassNonBusiness>string</classPrivPassNonBusiness>
        <classLocalGovernment>string</classLocalGovernment>
        <classOther>string</classOther>
        <operatingStatus>string</operatingStatus>
      </Operation>
      <Cargo>
        <hazmatIndicator>string</hazmatIndicator>
        <cargoGenFreight>string</cargoGenFreight>
        <cargoHousehold>string</cargoHousehold>
        <cargoMetal>string</cargoMetal>
        <cargoMotorVeh>string</cargoMotorVeh>
        <cargoDriveTow>string</cargoDriveTow>
        <cargoLogPole>string</cargoLogPole>
        <cargoBldgMaterial>string</cargoBldgMaterial>
        <cargoMobileHome>string</cargoMobileHome>
        <cargoMachLarge>string</cargoMachLarge>
        <cargoProduce>string</cargoProduce>
        <cargoLiqGas>string</cargoLiqGas>
        <cargoIntermodal>string</cargoIntermodal>
        <cargoPassengers>string</cargoPassengers>
        <cargoOilfield>string</cargoOilfield>
        <cargoLivestock>string</cargoLivestock>
        <cargoGrainfeed>string</cargoGrainfeed>
        <cargoCoalcoke>string</cargoCoalcoke>
        <cargoMeat>string</cargoMeat>
        <cargoGarbage>string</cargoGarbage>
        <cargoUSMail>string</cargoUSMail>
        <cargoChemicals>string</cargoChemicals>
        <cargoDryBulk>string</cargoDryBulk>
        <cargoRefrigerated>string</cargoRefrigerated>
        <cargoBeverages>string</cargoBeverages>
        <cargoPaperProd>string</cargoPaperProd>
        <cargoUtilities>string</cargoUtilities>
        <cargoFarmSupplies>string</cargoFarmSupplies>
        <cargoConstruction>string</cargoConstruction>
        <cargoWaterwell>string</cargoWaterwell>
        <cargoOther>string</cargoOther>
        <cargoOtherDesc>string</cargoOtherDesc>
      </Cargo>
      <Drivers>
        <driversTotal>string</driversTotal>
        <driversAvgLeased>string</driversAvgLeased>
        <driversCDL>string</driversCDL>
        <driversInter>string</driversInter>
        <driversInterLT100>string</driversInterLT100>
        <driversInterGT100>string</driversInterGT100>
        <driversIntra>string</driversIntra>
        <driversIntraLT100>string</driversIntraLT100>
        <driversIntraGT100>string</driversIntraGT100>
      </Drivers>
      <Equipment>
        <trucksTotal>string</trucksTotal>
        <totalPower>string</totalPower>
        <fleetsize>string</fleetsize>
        <trucksOwned>string</trucksOwned>
        <trucksTerm>string</trucksTerm>
        <trucksTrip>string</trucksTrip>
        <trailersOwned>string</trailersOwned>
        <trailersTerm>string</trailersTerm>
        <trailersTrip>string</trailersTrip>
        <tractorsOwned>string</tractorsOwned>
        <tractorsTerm>string</tractorsTerm>
        <tractorsTrip>string</tractorsTrip>
      </Equipment>
      <Other>
        <carbTru>string</carbTru>
        <smartway>string</smartway>
        <watchdogReports>string</watchdogReports>
      </Other>
      <RiskAssessment>
        <Overall>string</Overall>
        <Authority>string</Authority>
        <Insurance>string</Insurance>
        <Safety>string</Safety>
        <Operation>string</Operation>
        <Other>string</Other>
      </RiskAssessment>
      <RiskAssessmentDetails>
        <IsIntrastateCarrier>true</IsIntrastateCarrier>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <ReviewState>string</ReviewState>
        <Authority>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Authority>
        <Insurance>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Insurance>
        <Safety>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Safety>
        <Operation>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Operation>
        <Other>
          <TotalPoints>1</TotalPoints>
          <OverallRating>string</OverallRating>
          <HasRuleOverride>true</HasRuleOverride>
          <Infractions>
            <Points>1</Points>
            <RuleName>string</RuleName>
            <RiskLevel>string</RiskLevel>
            <RuleText>string</RuleText>
            <RuleOutput>string</RuleOutput>
            <PreReviewScore>1</PreReviewScore>
            <PreReviewRiskLevel>string</PreReviewRiskLevel>
            <RuleEnforced>true</RuleEnforced>
          </Infractions>
        </Other>
        <ReviewDetails>
          <ReviewID>1</ReviewID>
          <PreReviewOverall>string</PreReviewOverall>
          <PreReviewAuthority>string</PreReviewAuthority>
          <PreReviewInsurance>string</PreReviewInsurance>
          <PreReviewSafety>string</PreReviewSafety>
          <PreReviewOperation>string</PreReviewOperation>
          <PreReviewOther>string</PreReviewOther>
          <ReviewUser>string</ReviewUser>
          <ReviewDate>1970-01-01T00:00:00.001Z</ReviewDate>
          <ReviewReason>string</ReviewReason>
          <ReviewNote>string</ReviewNote>
          <ReviewExpirationDate>1970-01-01T00:00:00.001Z</ReviewExpirationDate>
        </ReviewDetails>
      </RiskAssessmentDetails>
      <CarrierRatings>
        <myRating>1</myRating>
        <totalRatings>1</totalRatings>
        <lowRatings>1</lowRatings>
        <avgRating>1.1</avgRating>
      </CarrierRatings>
      <LatestInvitation>
        <InvitedByUserName>string</InvitedByUserName>
        <InvitedByEmail>string</InvitedByEmail>
        <InvitedByFirstName>string</InvitedByFirstName>
        <InvitedByLastName>string</InvitedByLastName>
        <InvitationSentDate>1970-01-01T00:00:00.001Z</InvitationSentDate>
        <InvitationRecipient>string</InvitationRecipient>
      </LatestInvitation>
      <IncidentReports>
        <TotalIncidentReports>1</TotalIncidentReports>
        <TotalIncidentReportsWithFraud>1</TotalIncidentReportsWithFraud>
      </IncidentReports>
    </CarrierDetails>
    <ResponseDO>
      <status>string</status>
      <action>string</action>
      <code>string</code>
      <displayMsg>string</displayMsg>
      <techMsg>string</techMsg>
    </ResponseDO>
  </CarrierList>
</MyCarrierPacketsApi.DTOs.CarrierChangesResultDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Headers

| Header | Description | Type | Other |
| --- | --- | --- | --- |
| X-Pagination | Pagination data formatted as {"pageNumber":1,"pageSize":250,"totalPages":10,"totalCount":2500} | string |  |

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| fromDate |  | **From Date. Required parameter. Example: 2021-07-01T01:00:00** | query | date-time |
| toDate |  | **To Date. Required parameter. Example: 2021-07-01T23:00:00** | query | date-time |
| pageNumber |  | The current page number. | query | integer |
| pageSize |  | The number of carriers returned per page. The recommended and default value is 250. The max is 500. | query | integer |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_RequestMonitoring)[/api/v1/Carrier/RequestMonitoring](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_RequestMonitoring)



    - [Adds a carrier to the monitoring list.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_RequestMonitoring)

#### Implementation Notes

Remarks

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.RequestMonitoringOutput {

MonitoringID (integer, optional),

RequestDate (string, optional)

}

```
{
  "MonitoringID": 0,
  "RequestDate": "2026-05-17T23:54:51.330Z"
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.RequestMonitoringOutput>
  <MonitoringID>1</MonitoringID>
  <RequestDate>1970-01-01T00:00:00.001Z</RequestDate>
</MyCarrierPacketsApi.DTOs.RequestMonitoringOutput>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT Number | query | integer |
| DocketNumber |  | Docket number or MC Number | query | string |
| IntrastateNumber |  | Intrastate Number | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_CancelMonitoring)[/api/v1/Carrier/CancelMonitoring](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_CancelMonitoring)



    - [Removes a carrier from the monitoring list.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_CancelMonitoring)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.CancelMonitoringOutput {

MonitoringID (integer, optional),

CancelDate (string, optional)

}

```
{
  "MonitoringID": 0,
  "CancelDate": "2026-05-17T23:54:51.332Z"
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.CancelMonitoringOutput>
  <MonitoringID>1</MonitoringID>
  <CancelDate>1970-01-01T00:00:00.001Z</CancelDate>
</MyCarrierPacketsApi.DTOs.CancelMonitoringOutput>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT Number | query | integer |
| DocketNumber |  | Docket number or MC Number | query | string |
| IntrastateNumber |  | Intrastate Number | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_BlockCarrier)[/api/v1/Carrier/BlockCarrier](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_BlockCarrier)



    - [Blocks a carrier.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_BlockCarrier)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.BlockCarrierOutput {

Result (boolean, optional),

Message (string, optional)

}

```
{
  "Result": true,
  "Message": "string"
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.BlockCarrierOutput>
  <Result>true</Result>
  <Message>string</Message>
</MyCarrierPacketsApi.DTOs.BlockCarrierOutput>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT Number | query | integer |
| DocketNumber |  | Docket number or MC Number | query | string |
| IntrastateNumber |  | Intrastate Number | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_UnblockCarrier)[/api/v1/Carrier/UnblockCarrier](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_UnblockCarrier)



    - [Unblocks a carrier.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_UnblockCarrier)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.UnblockCarrierOutput {

Result (boolean, optional),

Message (string, optional)

}

```
{
  "Result": true,
  "Message": "string"
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.UnblockCarrierOutput>
  <Result>true</Result>
  <Message>string</Message>
</MyCarrierPacketsApi.DTOs.UnblockCarrierOutput>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| DOTNumber |  | DOT Number | query | integer |
| DocketNumber |  | Docket number or MC Number | query | string |
| IntrastateNumber |  | Intrastate Number | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetUpdatedFactoringCompanies)[/api/v1/Carrier/GetUpdatedFactoringCompanies](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetUpdatedFactoringCompanies)



    - [Returns list of MyCarrierPortal Factoring Companies with their unique identifiers.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetUpdatedFactoringCompanies)

#### Implementation Notes

Retrieves updated factoring companies for a given date range.

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.UpdatedFactoringCompaniesDTO {

FromDate (string, optional),

ToDate (string, optional),

RequestDateTimeUtc (string, optional),

FactoringCompaniesCount (integer, optional),

FactoringCompanies (Array\[MyCarrierPacketsApi.UpdatedFactoring\], optional)

}

MyCarrierPacketsApi.UpdatedFactoring {

FactoringCompanyID (integer, optional),

FactoringCompanyName (string, optional),

FactoringRemitEmail (string, optional),

FactoringRemitAddress (string, optional),

FactoringRemitAddress2 (string, optional),

FactoringRemitCity (string, optional),

FactoringRemitCountry (string, optional),

FactoringRemitStateProvince (string, optional),

FactoringRemitZipcode (string, optional),

FactoringPhone (string, optional),

CreatedDateTime (string, optional),

UpdatedDateTime (string, optional)

}

```
{
  "FromDate": "2026-05-17T23:54:51.337Z",
  "ToDate": "2026-05-17T23:54:51.337Z",
  "RequestDateTimeUtc": "2026-05-17T23:54:51.337Z",
  "FactoringCompaniesCount": 0,
  "FactoringCompanies": [\
    {\
      "FactoringCompanyID": 0,\
      "FactoringCompanyName": "string",\
      "FactoringRemitEmail": "string",\
      "FactoringRemitAddress": "string",\
      "FactoringRemitAddress2": "string",\
      "FactoringRemitCity": "string",\
      "FactoringRemitCountry": "string",\
      "FactoringRemitStateProvince": "string",\
      "FactoringRemitZipcode": "string",\
      "FactoringPhone": "string",\
      "CreatedDateTime": "2026-05-17T23:54:51.337Z",\
      "UpdatedDateTime": "2026-05-17T23:54:51.337Z"\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.UpdatedFactoringCompaniesDTO>
  <FromDate>1970-01-01T00:00:00.001Z</FromDate>
  <ToDate>1970-01-01T00:00:00.001Z</ToDate>
  <RequestDateTimeUtc>1970-01-01T00:00:00.001Z</RequestDateTimeUtc>
  <FactoringCompaniesCount>1</FactoringCompaniesCount>
  <FactoringCompanies>
    <FactoringCompanyID>1</FactoringCompanyID>
    <FactoringCompanyName>string</FactoringCompanyName>
    <FactoringRemitEmail>string</FactoringRemitEmail>
    <FactoringRemitAddress>string</FactoringRemitAddress>
    <FactoringRemitAddress2>string</FactoringRemitAddress2>
    <FactoringRemitCity>string</FactoringRemitCity>
    <FactoringRemitCountry>string</FactoringRemitCountry>
    <FactoringRemitStateProvince>string</FactoringRemitStateProvince>
    <FactoringRemitZipcode>string</FactoringRemitZipcode>
    <FactoringPhone>string</FactoringPhone>
    <CreatedDateTime>1970-01-01T00:00:00.001Z</CreatedDateTime>
    <UpdatedDateTime>1970-01-01T00:00:00.001Z</UpdatedDateTime>
  </FactoringCompanies>
</MyCarrierPacketsApi.DTOs.UpdatedFactoringCompaniesDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| fromDate |  | **Start date for the update period. For example: 2024-01-01T00:00:00Z** | query | date-time |
| toDate |  | End date for the update period. For example: 2024-01-01T23:59:59Z | query | date-time |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierRiskAssessment)[/api/v1/Carrier/GetCarrierRiskAssessment](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetCarrierRiskAssessment)



    - [Returns carrier's risk assessment with provided DOT number and Docket number.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetCarrierRiskAssessment)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model \[\
\
Inline Model 1\
\
\]

Inline Model 1 {

DOTNumber (integer, optional),

DocketNumber (string, optional),

RiskAssessmentDetails (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails {

IsIntrastateCarrier (boolean, optional),

TotalPoints (integer, optional),

OverallRating (string, optional),

ReviewState (string, optional),

Authority (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Insurance (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Safety (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Operation (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Other (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

ReviewDetails (MyCarrierPacketsRiskAssessmentModels.ReviewDetails, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail {

TotalPoints (integer, optional),

OverallRating (string, optional),

HasRuleOverride (boolean, optional, read only),

Infractions (Array\[MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction\], optional)

}

MyCarrierPacketsRiskAssessmentModels.ReviewDetails {

ReviewID (integer, optional),

PreReviewOverall (string, optional),

PreReviewAuthority (string, optional),

PreReviewInsurance (string, optional),

PreReviewSafety (string, optional),

PreReviewOperation (string, optional),

PreReviewOther (string, optional),

ReviewUser (string, optional),

ReviewDate (string, optional),

ReviewReason (string, optional),

ReviewNote (string, optional),

ReviewExpirationDate (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction {

Points (integer, optional),

RuleName (string, optional),

RiskLevel (string, optional),

RuleText (string, optional),

RuleOutput (string, optional),

PreReviewScore (integer, optional),

PreReviewRiskLevel (string, optional),

RuleEnforced (boolean, optional)

}

```
[\
  {\
    "DOTNumber": 0,\
    "DocketNumber": "string",\
    "RiskAssessmentDetails": {\
      "IsIntrastateCarrier": true,\
      "TotalPoints": 0,\
      "OverallRating": "string",\
      "ReviewState": "string",\
      "Authority": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Insurance": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Safety": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Operation": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "Other": {\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "HasRuleOverride": true,\
        "Infractions": [\
          {\
            "Points": 0,\
            "RuleName": "string",\
            "RiskLevel": "string",\
            "RuleText": "string",\
            "RuleOutput": "string",\
            "PreReviewScore": 0,\
            "PreReviewRiskLevel": "string",\
            "RuleEnforced": true\
          }\
        ]\
      },\
      "ReviewDetails": {\
        "ReviewID": 0,\
        "PreReviewOverall": "string",\
        "PreReviewAuthority": "string",\
        "PreReviewInsurance": "string",\
        "PreReviewSafety": "string",\
        "PreReviewOperation": "string",\
        "PreReviewOther": "string",\
        "ReviewUser": "string",\
        "ReviewDate": "2026-05-17T23:54:51.339Z",\
        "ReviewReason": "string",\
        "ReviewNote": "string",\
        "ReviewExpirationDate": "2026-05-17T23:54:51.339Z"\
      }\
    }\
  }\
]
```

```
<?xml version="1.0"?>
<Inline Model>
  <DOTNumber>1</DOTNumber>
  <DocketNumber>string</DocketNumber>
  <RiskAssessmentDetails>
    <IsIntrastateCarrier>true</IsIntrastateCarrier>
    <TotalPoints>1</TotalPoints>
    <OverallRating>string</OverallRating>
    <ReviewState>string</ReviewState>
    <Authority>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Authority>
    <Insurance>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Insurance>
    <Safety>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Safety>
    <Operation>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Operation>
    <Other>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <HasRuleOverride>true</HasRuleOverride>
      <Infractions>
        <Points>1</Points>
        <RuleName>string</RuleName>
        <RiskLevel>string</RiskLevel>
        <RuleText>string</RuleText>
        <RuleOutput>string</RuleOutput>
        <PreReviewScore>1</PreReviewScore>
        <PreReviewRiskLevel>string</PreReviewRiskLevel>
        <RuleEnforced>true</RuleEnforced>
      </Infractions>
    </Other>
    <ReviewDetails>
      <ReviewID>1</ReviewID>
      <PreReviewOverall>string</PreReviewOverall>
      <PreReviewAuthority>string</PreReviewAuthority>
      <PreReviewInsurance>string</PreReviewInsurance>
      <PreReviewSafety>string</PreReviewSafety>
      <PreReviewOperation>string</PreReviewOperation>
      <PreReviewOther>string</PreReviewOther>
      <ReviewUser>string</ReviewUser>
      <ReviewDate>1970-01-01T00:00:00.001Z</ReviewDate>
      <ReviewReason>string</ReviewReason>
      <ReviewNote>string</ReviewNote>
      <ReviewExpirationDate>1970-01-01T00:00:00.001Z</ReviewExpirationDate>
    </ReviewDetails>
  </RiskAssessmentDetails>
</Inline Model>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| dotNumber |  | DOT number of the carrier. Example: 12345 | query | integer |
| docketNumber |  | Docket number of the carrier. Example: MC010203. Optional | query | string |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetMonitoredCarriersRiskAssessment)[/api/v1/Carrier/GetMonitoredCarriersRiskAssessment](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_GetMonitoredCarriersRiskAssessment)



    - [Returns all monitored carrier risk assessments in bulk. Includes paging.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_GetMonitoredCarriersRiskAssessment)

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.MonitoredCarriersRiskAssessmentDTO {

pageNumber (integer, optional),

pageSize (integer, optional),

totalPages (integer, optional),

totalCount (integer, optional),

succeeded (boolean, optional),

message (string, optional),

data (Array\[MyCarrierPacketsApi.DTOs.CarrierRiskAssessmentDTO\], optional)

}

MyCarrierPacketsApi.DTOs.CarrierRiskAssessmentDTO {

DOTNumber (integer, optional),

DocketNumber (string, optional),

RiskAssessmentDetails (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails {

IsIntrastateCarrier (boolean, optional),

TotalPoints (integer, optional),

OverallRating (string, optional),

ReviewState (string, optional),

Authority (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Insurance (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Safety (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Operation (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Other (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

ReviewDetails (MyCarrierPacketsRiskAssessmentModels.ReviewDetails, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail {

TotalPoints (integer, optional),

OverallRating (string, optional),

HasRuleOverride (boolean, optional, read only),

Infractions (Array\[MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction\], optional)

}

MyCarrierPacketsRiskAssessmentModels.ReviewDetails {

ReviewID (integer, optional),

PreReviewOverall (string, optional),

PreReviewAuthority (string, optional),

PreReviewInsurance (string, optional),

PreReviewSafety (string, optional),

PreReviewOperation (string, optional),

PreReviewOther (string, optional),

ReviewUser (string, optional),

ReviewDate (string, optional),

ReviewReason (string, optional),

ReviewNote (string, optional),

ReviewExpirationDate (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction {

Points (integer, optional),

RuleName (string, optional),

RiskLevel (string, optional),

RuleText (string, optional),

RuleOutput (string, optional),

PreReviewScore (integer, optional),

PreReviewRiskLevel (string, optional),

RuleEnforced (boolean, optional)

}

```
{
  "pageNumber": 0,
  "pageSize": 0,
  "totalPages": 0,
  "totalCount": 0,
  "succeeded": true,
  "message": "string",
  "data": [\
    {\
      "DOTNumber": 0,\
      "DocketNumber": "string",\
      "RiskAssessmentDetails": {\
        "IsIntrastateCarrier": true,\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "ReviewState": "string",\
        "Authority": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Insurance": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Safety": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Operation": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Other": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "ReviewDetails": {\
          "ReviewID": 0,\
          "PreReviewOverall": "string",\
          "PreReviewAuthority": "string",\
          "PreReviewInsurance": "string",\
          "PreReviewSafety": "string",\
          "PreReviewOperation": "string",\
          "PreReviewOther": "string",\
          "ReviewUser": "string",\
          "ReviewDate": "2026-05-17T23:54:51.341Z",\
          "ReviewReason": "string",\
          "ReviewNote": "string",\
          "ReviewExpirationDate": "2026-05-17T23:54:51.341Z"\
        }\
      }\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.MonitoredCarriersRiskAssessmentDTO>
  <pageNumber>1</pageNumber>
  <pageSize>1</pageSize>
  <totalPages>1</totalPages>
  <totalCount>1</totalCount>
  <succeeded>true</succeeded>
  <message>string</message>
  <data>
    <DOTNumber>1</DOTNumber>
    <DocketNumber>string</DocketNumber>
    <RiskAssessmentDetails>
      <IsIntrastateCarrier>true</IsIntrastateCarrier>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <ReviewState>string</ReviewState>
      <Authority>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Authority>
      <Insurance>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Insurance>
      <Safety>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Safety>
      <Operation>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Operation>
      <Other>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Other>
      <ReviewDetails>
        <ReviewID>1</ReviewID>
        <PreReviewOverall>string</PreReviewOverall>
        <PreReviewAuthority>string</PreReviewAuthority>
        <PreReviewInsurance>string</PreReviewInsurance>
        <PreReviewSafety>string</PreReviewSafety>
        <PreReviewOperation>string</PreReviewOperation>
        <PreReviewOther>string</PreReviewOther>
        <ReviewUser>string</ReviewUser>
        <ReviewDate>1970-01-01T00:00:00.001Z</ReviewDate>
        <ReviewReason>string</ReviewReason>
        <ReviewNote>string</ReviewNote>
        <ReviewExpirationDate>1970-01-01T00:00:00.001Z</ReviewExpirationDate>
      </ReviewDetails>
    </RiskAssessmentDetails>
  </data>
</MyCarrierPacketsApi.DTOs.MonitoredCarriersRiskAssessmentDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| pageNumber |  | Default: 1 | query | integer |
| pageSize |  | Default: 250. If set to more than 500, or less than 1, the default value will be used. | query | integer |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_MonitoredCarriers)[/api/v1/Carrier/MonitoredCarriers](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_MonitoredCarriers)



    - [Provides a list of monitored carriers.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_MonitoredCarriers)

#### Implementation Notes

If pagination parameters are not supplied, all monitored carriers are returned. Otherwise, the number of monitored carriers returned is limited to the pageSize.
If paging is requested, the response header will contain an "X-Pagination" item containing the details of the paged response.

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model \[\
\
Inline Model 1\
\
\]

Inline Model 1 {

DOTNumber (integer, optional),

DocketNumber (string, optional),

IntrastateNumber (string, optional),

CreatedDate (string, optional),

CreatedBy (string, optional),

LastModifiedDate (string, optional),

LastModifiedBy (string, optional)

}

```
[\
  {\
    "DOTNumber": 0,\
    "DocketNumber": "string",\
    "IntrastateNumber": "string",\
    "CreatedDate": "2026-05-17T23:54:51.348Z",\
    "CreatedBy": "string",\
    "LastModifiedDate": "2026-05-17T23:54:51.348Z",\
    "LastModifiedBy": "string"\
  }\
]
```

```
<?xml version="1.0"?>
<Inline Model>
  <DOTNumber>1</DOTNumber>
  <DocketNumber>string</DocketNumber>
  <IntrastateNumber>string</IntrastateNumber>
  <CreatedDate>1970-01-01T00:00:00.001Z</CreatedDate>
  <CreatedBy>string</CreatedBy>
  <LastModifiedDate>1970-01-01T00:00:00.001Z</LastModifiedDate>
  <LastModifiedBy>string</LastModifiedBy>
</Inline Model>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Headers

| Header | Description | Type | Other |
| --- | --- | --- | --- |
| X-Pagination | Pagination data formatted as {"pageNumber":1,"pageSize":2500,"totalPages":10,"totalCount":25000} | string |  |

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| pageNumber |  | The current page number. | query | integer |
| pageSize |  | The number of carriers returned per page. The recommended and default value is 2500. The max is 5000. | query | integer |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_MonitoredCarrierData)[/api/v1/Carrier/MonitoredCarrierData](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_MonitoredCarrierData)



    - [Calls GetCarrierData for all carriers on the monitored list.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_MonitoredCarrierData)

#### Implementation Notes

This is a paginated API call to be used for bulk sync.

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

MyCarrierPacketsApi.DTOs.MonitoredCarrierDataDTO {

pageNumber (integer, optional),

pageSize (integer, optional),

totalPages (integer, optional),

totalCount (integer, optional),

succeeded (boolean, optional),

message (string, optional),

data (Array\[MyCarrierPacketsApi.FMCSA.CarrierDetails\], optional)

}

MyCarrierPacketsApi.FMCSA.CarrierDetails {

docketNumber (string, optional),

dotNumber (MyCarrierPacketsApi.FMCSA.DotNumber, optional),

carrierType (string, optional),

isMonitored (boolean, optional),

isBlocked (boolean, optional),

Identity (MyCarrierPacketsApi.FMCSA.Identity, optional),

Authority (MyCarrierPacketsApi.FMCSA.Authority, optional),

FMCSAInsurance (MyCarrierPacketsApi.FMCSA.FMCSAInsurance, optional),

CertData (MyCarrierPacketsApi.FMCSA.CertData, optional),

Safety (MyCarrierPacketsApi.FMCSA.Safety, optional),

Inspection (MyCarrierPacketsApi.FMCSA.Inspection, optional),

Crash (MyCarrierPacketsApi.FMCSA.Crash, optional),

Review (MyCarrierPacketsApi.FMCSA.Review, optional),

Operation (MyCarrierPacketsApi.FMCSA.Operation, optional),

Cargo (MyCarrierPacketsApi.FMCSA.Cargo, optional),

Drivers (MyCarrierPacketsApi.FMCSA.Drivers, optional),

Equipment (MyCarrierPacketsApi.FMCSA.Equipment, optional),

Other (MyCarrierPacketsApi.FMCSA.Other, optional),

RiskAssessment (MyCarrierPacketsApi.FMCSA.RiskAssessment, optional),

RiskAssessmentDetails (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails, optional),

CarrierRatings (MyCarrierPacketsApi.FMCSA.CarrierRatings, optional),

LatestInvitation (MyCarrierPacketsApi.FMCSA.LatestInvitation, optional),

IncidentReports (MyCarrierPacketsApi.FMCSA.IncidentReports, optional)

}

MyCarrierPacketsApi.FMCSA.DotNumber {

status (string, optional),

Value (string, optional)

}

MyCarrierPacketsApi.FMCSA.Identity {

legalName (string, optional),

dbaName (string, optional),

businessStreet (string, optional),

businessCity (string, optional),

businessState (string, optional),

businessZipCode (string, optional),

businessColonia (string, optional),

businessCountry (string, optional),

businessPhone (string, optional),

businessFax (string, optional),

mailingStreet (string, optional),

mailingCity (string, optional),

mailingState (string, optional),

mailingZipCode (string, optional),

mailingColonia (string, optional),

mailingCountry (string, optional),

mailingPhone (string, optional),

mailingFax (string, optional),

undeliverableMail (string, optional),

companyRep1 (string, optional),

companyRep2 (string, optional),

cellPhone (string, optional),

emailAddress (string, optional),

dunBradstreetNum (string, optional),

organization (string, optional)

}

MyCarrierPacketsApi.FMCSA.Authority {

authGrantDate (string, optional),

commonAuthority (string, optional),

commonAuthorityPending (string, optional),

commonAuthorityRevocation (string, optional),

contractAuthority (string, optional),

contractAuthorityPending (string, optional),

contractAuthorityRevocation (string, optional),

brokerAuthority (string, optional),

brokerAuthorityPending (string, optional),

brokerAuthorityRevocation (string, optional),

freight (string, optional),

passenger (string, optional),

householdGoods (string, optional),

private (string, optional),

enterprise (string, optional)

}

MyCarrierPacketsApi.FMCSA.FMCSAInsurance {

bipdRequired (string, optional),

bipdOnFile (string, optional),

cargoRequired (string, optional),

cargoOnFile (string, optional),

bondSuretyRequired (string, optional),

bondSuretyOnFile (string, optional),

PolicyList (Array\[MyCarrierPacketsApi.DTOs.PolicyOutput\], optional)

}

MyCarrierPacketsApi.FMCSA.CertData {

status (string, optional),

noncoop (boolean, optional),

Certificate (Array\[MyCarrierPacketsApi.DTOs.CertificateDTO\], optional)

}

MyCarrierPacketsApi.FMCSA.Safety {

rating (string, optional),

ratingDate (string, optional),

unsafeDrvPCT (string, optional),

unsafeDrvOT (string, optional),

unsafeDrvSV (string, optional),

unsafeDrvAlert (string, optional),

unsafeDrvTrend (string, optional),

unsafeDrvCNT (integer, optional),

hosPCT (string, optional),

hosOT (string, optional),

hosSV (string, optional),

hosAlert (string, optional),

hosTrend (string, optional),

hosCNT (integer, optional),

drvFitPCT (string, optional),

drvFitOT (string, optional),

drvFitSV (string, optional),

drvFitAlert (string, optional),

drvFitTrend (string, optional),

drvFitCNT (integer, optional),

controlSubPCT (string, optional),

controlSubOT (string, optional),

controlSubSV (string, optional),

controlSubAlert (string, optional),

controlSubTrend (string, optional),

controlSubCNT (integer, optional),

vehMaintPCT (string, optional),

vehMaintOT (string, optional),

vehMaintSV (string, optional),

vehMaintAlert (string, optional),

vehMaintTrend (string, optional),

vehMaintCNT (integer, optional),

hazMatPCT (string, optional),

hazMatOT (string, optional),

hazMatSV (string, optional),

hazMatAlert (string, optional),

hazMatTrend (string, optional),

hazMatCNT (integer, optional)

}

MyCarrierPacketsApi.FMCSA.Inspection {

inspectVehUS (string, optional),

inspectVehOOSUS (string, optional),

inspectVehOOSPctUS (string, optional),

inspectDrvUS (string, optional),

inspectDrvOOSUS (string, optional),

inspectDrvOOSPctUS (string, optional),

inspectHazUS (string, optional),

inspectHazOOSUS (string, optional),

inspectHazOOSPctUS (string, optional),

inspectIEPUS (string, optional),

inspectIEPOOSUS (string, optional),

inspectIEPOOSPctUS (string, optional),

inspectTotalIEPUS (string, optional),

inspectTotalUS (string, optional),

inspectVehCAN (string, optional),

inspectVehOOSCAN (string, optional),

inspectVehOOSPctCAN (string, optional),

inspectDrvCAN (string, optional),

inspectDrvOOSCAN (string, optional),

inspectDrvOOSPctCAN (string, optional),

inspectTotalCAN (string, optional)

}

MyCarrierPacketsApi.FMCSA.Crash {

crashFatalUS (string, optional),

crashInjuryUS (string, optional),

crashTowUS (string, optional),

crashTotalUS (string, optional),

crashFatalCAN (string, optional),

crashInjuryCAN (string, optional),

crashTowCAN (string, optional),

crashTotalCAN (string, optional)

}

MyCarrierPacketsApi.FMCSA.Review {

reviewType (string, optional),

reviewDate (string, optional),

reviewDocNum (string, optional),

reviewMiles (string, optional),

mcs150Date (string, optional),

mcs150MileYear (string, optional),

mcs150Miles (string, optional),

accidentRate (string, optional),

accidentRatePrevent (string, optional)

}

MyCarrierPacketsApi.FMCSA.Operation {

dotAddDate (string, optional),

carrierOperation (string, optional),

shipperOperation (string, optional),

mxOperationType (string, optional),

mxRFCNumber (string, optional),

outOfService (string, optional),

outOfServiceDate (string, optional),

outOfServiceReason (string, optional),

entityCarrier (string, optional),

entityShipper (string, optional),

entityBroker (string, optional),

entityFreightFowarder (string, optional),

entityCargoTank (string, optional),

classAuthForHire (string, optional),

classMigrant (string, optional),

classIndianNation (string, optional),

classExemptForHire (string, optional),

classUSMail (string, optional),

classPrivateProperty (string, optional),

classFederalGovernment (string, optional),

classPrivPassBusiness (string, optional),

classStateGovernment (string, optional),

classPrivPassNonBusiness (string, optional),

classLocalGovernment (string, optional),

classOther (string, optional),

operatingStatus (string, optional)

}

MyCarrierPacketsApi.FMCSA.Cargo {

hazmatIndicator (string, optional),

cargoGenFreight (string, optional),

cargoHousehold (string, optional),

cargoMetal (string, optional),

cargoMotorVeh (string, optional),

cargoDriveTow (string, optional),

cargoLogPole (string, optional),

cargoBldgMaterial (string, optional),

cargoMobileHome (string, optional),

cargoMachLarge (string, optional),

cargoProduce (string, optional),

cargoLiqGas (string, optional),

cargoIntermodal (string, optional),

cargoPassengers (string, optional),

cargoOilfield (string, optional),

cargoLivestock (string, optional),

cargoGrainfeed (string, optional),

cargoCoalcoke (string, optional),

cargoMeat (string, optional),

cargoGarbage (string, optional),

cargoUSMail (string, optional),

cargoChemicals (string, optional),

cargoDryBulk (string, optional),

cargoRefrigerated (string, optional),

cargoBeverages (string, optional),

cargoPaperProd (string, optional),

cargoUtilities (string, optional),

cargoFarmSupplies (string, optional),

cargoConstruction (string, optional),

cargoWaterwell (string, optional),

cargoOther (string, optional),

cargoOtherDesc (string, optional)

}

MyCarrierPacketsApi.FMCSA.Drivers {

driversTotal (string, optional),

driversAvgLeased (string, optional),

driversCDL (string, optional),

driversInter (string, optional),

driversInterLT100 (string, optional),

driversInterGT100 (string, optional),

driversIntra (string, optional),

driversIntraLT100 (string, optional),

driversIntraGT100 (string, optional)

}

MyCarrierPacketsApi.FMCSA.Equipment {

trucksTotal (string, optional),

totalPower (string, optional),

fleetsize (string, optional),

trucksOwned (string, optional),

trucksTerm (string, optional),

trucksTrip (string, optional),

trailersOwned (string, optional),

trailersTerm (string, optional),

trailersTrip (string, optional),

tractorsOwned (string, optional),

tractorsTerm (string, optional),

tractorsTrip (string, optional)

}

MyCarrierPacketsApi.FMCSA.Other {

carbTru (string, optional),

smartway (string, optional),

watchdogReports (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessment {

Overall (string, optional),

Authority (string, optional),

Insurance (string, optional),

Safety (string, optional),

Operation (string, optional),

Other (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetails {

IsIntrastateCarrier (boolean, optional),

TotalPoints (integer, optional),

OverallRating (string, optional),

ReviewState (string, optional),

Authority (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Insurance (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Safety (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Operation (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

Other (MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail, optional),

ReviewDetails (MyCarrierPacketsRiskAssessmentModels.ReviewDetails, optional)

}

MyCarrierPacketsApi.FMCSA.CarrierRatings {

myRating (integer, optional),

totalRatings (integer, optional),

lowRatings (integer, optional),

avgRating (number, optional)

}

MyCarrierPacketsApi.FMCSA.LatestInvitation {

InvitedByUserName (string, optional),

InvitedByEmail (string, optional),

InvitedByFirstName (string, optional),

InvitedByLastName (string, optional),

InvitationSentDate (string, optional),

InvitationRecipient (string, optional)

}

MyCarrierPacketsApi.FMCSA.IncidentReports {

TotalIncidentReports (integer, optional),

TotalIncidentReportsWithFraud (integer, optional)

}

MyCarrierPacketsApi.DTOs.PolicyOutput {

companyName (string, optional),

attnToName (string, optional),

address (string, optional),

city (string, optional),

stateCode (string, optional),

postalCode (string, optional),

countryCode (string, optional),

phone (string, optional),

fax (string, optional),

insuranceType (string, optional),

policyNumber (string, optional),

postedDate (string, optional),

effectiveDate (string, optional),

cancelationDate (string, optional),

coverageFrom (string, optional),

coverageTo (string, optional),

amBestRating (string, optional)

}

MyCarrierPacketsApi.DTOs.CertificateDTO {

certificateID (string, optional),

producerName (string, optional),

producerAddress (string, optional),

producerCity (string, optional),

producerState (string, optional),

producerZip (string, optional),

producerPhone (string, optional),

producerFax (string, optional),

producerEmail (string, optional),

paidFor (string, optional),

BlobName (string, optional),

Coverage (Array\[MyCarrierPacketsApi.DTOs.CoverageDTO\], optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentDetail {

TotalPoints (integer, optional),

OverallRating (string, optional),

HasRuleOverride (boolean, optional, read only),

Infractions (Array\[MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction\], optional)

}

MyCarrierPacketsRiskAssessmentModels.ReviewDetails {

ReviewID (integer, optional),

PreReviewOverall (string, optional),

PreReviewAuthority (string, optional),

PreReviewInsurance (string, optional),

PreReviewSafety (string, optional),

PreReviewOperation (string, optional),

PreReviewOther (string, optional),

ReviewUser (string, optional),

ReviewDate (string, optional),

ReviewReason (string, optional),

ReviewNote (string, optional),

ReviewExpirationDate (string, optional)

}

MyCarrierPacketsApi.DTOs.CoverageDTO {

insurerName (string, optional),

insurerAMBestRating (string, optional),

type (string, optional),

policyNumber (string, optional),

expirationDate (string, optional),

coverageLimit (string, optional),

deductable (string, optional),

referBreakdown (string, optional),

referBreakDeduct (string, optional),

cancellationDate (string, optional)

}

MyCarrierPacketsApi.FMCSA.RiskAssessmentInfraction {

Points (integer, optional),

RuleName (string, optional),

RiskLevel (string, optional),

RuleText (string, optional),

RuleOutput (string, optional),

PreReviewScore (integer, optional),

PreReviewRiskLevel (string, optional),

RuleEnforced (boolean, optional)

}

```
{
  "pageNumber": 0,
  "pageSize": 0,
  "totalPages": 0,
  "totalCount": 0,
  "succeeded": true,
  "message": "string",
  "data": [\
    {\
      "docketNumber": "string",\
      "dotNumber": {\
        "status": "string",\
        "Value": "string"\
      },\
      "carrierType": "string",\
      "isMonitored": true,\
      "isBlocked": true,\
      "Identity": {\
        "legalName": "string",\
        "dbaName": "string",\
        "businessStreet": "string",\
        "businessCity": "string",\
        "businessState": "string",\
        "businessZipCode": "string",\
        "businessColonia": "string",\
        "businessCountry": "string",\
        "businessPhone": "string",\
        "businessFax": "string",\
        "mailingStreet": "string",\
        "mailingCity": "string",\
        "mailingState": "string",\
        "mailingZipCode": "string",\
        "mailingColonia": "string",\
        "mailingCountry": "string",\
        "mailingPhone": "string",\
        "mailingFax": "string",\
        "undeliverableMail": "string",\
        "companyRep1": "string",\
        "companyRep2": "string",\
        "cellPhone": "string",\
        "emailAddress": "string",\
        "dunBradstreetNum": "string",\
        "organization": "string"\
      },\
      "Authority": {\
        "authGrantDate": "string",\
        "commonAuthority": "string",\
        "commonAuthorityPending": "string",\
        "commonAuthorityRevocation": "string",\
        "contractAuthority": "string",\
        "contractAuthorityPending": "string",\
        "contractAuthorityRevocation": "string",\
        "brokerAuthority": "string",\
        "brokerAuthorityPending": "string",\
        "brokerAuthorityRevocation": "string",\
        "freight": "string",\
        "passenger": "string",\
        "householdGoods": "string",\
        "private": "string",\
        "enterprise": "string"\
      },\
      "FMCSAInsurance": {\
        "bipdRequired": "string",\
        "bipdOnFile": "string",\
        "cargoRequired": "string",\
        "cargoOnFile": "string",\
        "bondSuretyRequired": "string",\
        "bondSuretyOnFile": "string",\
        "PolicyList": [\
          {\
            "companyName": "string",\
            "attnToName": "string",\
            "address": "string",\
            "city": "string",\
            "stateCode": "string",\
            "postalCode": "string",\
            "countryCode": "string",\
            "phone": "string",\
            "fax": "string",\
            "insuranceType": "string",\
            "policyNumber": "string",\
            "postedDate": "string",\
            "effectiveDate": "string",\
            "cancelationDate": "string",\
            "coverageFrom": "string",\
            "coverageTo": "string",\
            "amBestRating": "string"\
          }\
        ]\
      },\
      "CertData": {\
        "status": "string",\
        "noncoop": true,\
        "Certificate": [\
          {\
            "certificateID": "string",\
            "producerName": "string",\
            "producerAddress": "string",\
            "producerCity": "string",\
            "producerState": "string",\
            "producerZip": "string",\
            "producerPhone": "string",\
            "producerFax": "string",\
            "producerEmail": "string",\
            "paidFor": "string",\
            "BlobName": "string",\
            "Coverage": [\
              {\
                "insurerName": "string",\
                "insurerAMBestRating": "string",\
                "type": "string",\
                "policyNumber": "string",\
                "expirationDate": "string",\
                "coverageLimit": "string",\
                "deductable": "string",\
                "referBreakdown": "string",\
                "referBreakDeduct": "string",\
                "cancellationDate": "string"\
              }\
            ]\
          }\
        ]\
      },\
      "Safety": {\
        "rating": "string",\
        "ratingDate": "string",\
        "unsafeDrvPCT": "string",\
        "unsafeDrvOT": "string",\
        "unsafeDrvSV": "string",\
        "unsafeDrvAlert": "string",\
        "unsafeDrvTrend": "string",\
        "unsafeDrvCNT": 0,\
        "hosPCT": "string",\
        "hosOT": "string",\
        "hosSV": "string",\
        "hosAlert": "string",\
        "hosTrend": "string",\
        "hosCNT": 0,\
        "drvFitPCT": "string",\
        "drvFitOT": "string",\
        "drvFitSV": "string",\
        "drvFitAlert": "string",\
        "drvFitTrend": "string",\
        "drvFitCNT": 0,\
        "controlSubPCT": "string",\
        "controlSubOT": "string",\
        "controlSubSV": "string",\
        "controlSubAlert": "string",\
        "controlSubTrend": "string",\
        "controlSubCNT": 0,\
        "vehMaintPCT": "string",\
        "vehMaintOT": "string",\
        "vehMaintSV": "string",\
        "vehMaintAlert": "string",\
        "vehMaintTrend": "string",\
        "vehMaintCNT": 0,\
        "hazMatPCT": "string",\
        "hazMatOT": "string",\
        "hazMatSV": "string",\
        "hazMatAlert": "string",\
        "hazMatTrend": "string",\
        "hazMatCNT": 0\
      },\
      "Inspection": {\
        "inspectVehUS": "string",\
        "inspectVehOOSUS": "string",\
        "inspectVehOOSPctUS": "string",\
        "inspectDrvUS": "string",\
        "inspectDrvOOSUS": "string",\
        "inspectDrvOOSPctUS": "string",\
        "inspectHazUS": "string",\
        "inspectHazOOSUS": "string",\
        "inspectHazOOSPctUS": "string",\
        "inspectIEPUS": "string",\
        "inspectIEPOOSUS": "string",\
        "inspectIEPOOSPctUS": "string",\
        "inspectTotalIEPUS": "string",\
        "inspectTotalUS": "string",\
        "inspectVehCAN": "string",\
        "inspectVehOOSCAN": "string",\
        "inspectVehOOSPctCAN": "string",\
        "inspectDrvCAN": "string",\
        "inspectDrvOOSCAN": "string",\
        "inspectDrvOOSPctCAN": "string",\
        "inspectTotalCAN": "string"\
      },\
      "Crash": {\
        "crashFatalUS": "string",\
        "crashInjuryUS": "string",\
        "crashTowUS": "string",\
        "crashTotalUS": "string",\
        "crashFatalCAN": "string",\
        "crashInjuryCAN": "string",\
        "crashTowCAN": "string",\
        "crashTotalCAN": "string"\
      },\
      "Review": {\
        "reviewType": "string",\
        "reviewDate": "string",\
        "reviewDocNum": "string",\
        "reviewMiles": "string",\
        "mcs150Date": "string",\
        "mcs150MileYear": "string",\
        "mcs150Miles": "string",\
        "accidentRate": "string",\
        "accidentRatePrevent": "string"\
      },\
      "Operation": {\
        "dotAddDate": "string",\
        "carrierOperation": "string",\
        "shipperOperation": "string",\
        "mxOperationType": "string",\
        "mxRFCNumber": "string",\
        "outOfService": "string",\
        "outOfServiceDate": "string",\
        "outOfServiceReason": "string",\
        "entityCarrier": "string",\
        "entityShipper": "string",\
        "entityBroker": "string",\
        "entityFreightFowarder": "string",\
        "entityCargoTank": "string",\
        "classAuthForHire": "string",\
        "classMigrant": "string",\
        "classIndianNation": "string",\
        "classExemptForHire": "string",\
        "classUSMail": "string",\
        "classPrivateProperty": "string",\
        "classFederalGovernment": "string",\
        "classPrivPassBusiness": "string",\
        "classStateGovernment": "string",\
        "classPrivPassNonBusiness": "string",\
        "classLocalGovernment": "string",\
        "classOther": "string",\
        "operatingStatus": "string"\
      },\
      "Cargo": {\
        "hazmatIndicator": "string",\
        "cargoGenFreight": "string",\
        "cargoHousehold": "string",\
        "cargoMetal": "string",\
        "cargoMotorVeh": "string",\
        "cargoDriveTow": "string",\
        "cargoLogPole": "string",\
        "cargoBldgMaterial": "string",\
        "cargoMobileHome": "string",\
        "cargoMachLarge": "string",\
        "cargoProduce": "string",\
        "cargoLiqGas": "string",\
        "cargoIntermodal": "string",\
        "cargoPassengers": "string",\
        "cargoOilfield": "string",\
        "cargoLivestock": "string",\
        "cargoGrainfeed": "string",\
        "cargoCoalcoke": "string",\
        "cargoMeat": "string",\
        "cargoGarbage": "string",\
        "cargoUSMail": "string",\
        "cargoChemicals": "string",\
        "cargoDryBulk": "string",\
        "cargoRefrigerated": "string",\
        "cargoBeverages": "string",\
        "cargoPaperProd": "string",\
        "cargoUtilities": "string",\
        "cargoFarmSupplies": "string",\
        "cargoConstruction": "string",\
        "cargoWaterwell": "string",\
        "cargoOther": "string",\
        "cargoOtherDesc": "string"\
      },\
      "Drivers": {\
        "driversTotal": "string",\
        "driversAvgLeased": "string",\
        "driversCDL": "string",\
        "driversInter": "string",\
        "driversInterLT100": "string",\
        "driversInterGT100": "string",\
        "driversIntra": "string",\
        "driversIntraLT100": "string",\
        "driversIntraGT100": "string"\
      },\
      "Equipment": {\
        "trucksTotal": "string",\
        "totalPower": "string",\
        "fleetsize": "string",\
        "trucksOwned": "string",\
        "trucksTerm": "string",\
        "trucksTrip": "string",\
        "trailersOwned": "string",\
        "trailersTerm": "string",\
        "trailersTrip": "string",\
        "tractorsOwned": "string",\
        "tractorsTerm": "string",\
        "tractorsTrip": "string"\
      },\
      "Other": {\
        "carbTru": "string",\
        "smartway": "string",\
        "watchdogReports": "string"\
      },\
      "RiskAssessment": {\
        "Overall": "string",\
        "Authority": "string",\
        "Insurance": "string",\
        "Safety": "string",\
        "Operation": "string",\
        "Other": "string"\
      },\
      "RiskAssessmentDetails": {\
        "IsIntrastateCarrier": true,\
        "TotalPoints": 0,\
        "OverallRating": "string",\
        "ReviewState": "string",\
        "Authority": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Insurance": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Safety": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Operation": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "Other": {\
          "TotalPoints": 0,\
          "OverallRating": "string",\
          "HasRuleOverride": true,\
          "Infractions": [\
            {\
              "Points": 0,\
              "RuleName": "string",\
              "RiskLevel": "string",\
              "RuleText": "string",\
              "RuleOutput": "string",\
              "PreReviewScore": 0,\
              "PreReviewRiskLevel": "string",\
              "RuleEnforced": true\
            }\
          ]\
        },\
        "ReviewDetails": {\
          "ReviewID": 0,\
          "PreReviewOverall": "string",\
          "PreReviewAuthority": "string",\
          "PreReviewInsurance": "string",\
          "PreReviewSafety": "string",\
          "PreReviewOperation": "string",\
          "PreReviewOther": "string",\
          "ReviewUser": "string",\
          "ReviewDate": "2026-05-17T23:54:51.351Z",\
          "ReviewReason": "string",\
          "ReviewNote": "string",\
          "ReviewExpirationDate": "2026-05-17T23:54:51.351Z"\
        }\
      },\
      "CarrierRatings": {\
        "myRating": 0,\
        "totalRatings": 0,\
        "lowRatings": 0,\
        "avgRating": 0\
      },\
      "LatestInvitation": {\
        "InvitedByUserName": "string",\
        "InvitedByEmail": "string",\
        "InvitedByFirstName": "string",\
        "InvitedByLastName": "string",\
        "InvitationSentDate": "2026-05-17T23:54:51.351Z",\
        "InvitationRecipient": "string"\
      },\
      "IncidentReports": {\
        "TotalIncidentReports": 0,\
        "TotalIncidentReportsWithFraud": 0\
      }\
    }\
  ]
}
```

```
<?xml version="1.0"?>
<MyCarrierPacketsApi.DTOs.MonitoredCarrierDataDTO>
  <pageNumber>1</pageNumber>
  <pageSize>1</pageSize>
  <totalPages>1</totalPages>
  <totalCount>1</totalCount>
  <succeeded>true</succeeded>
  <message>string</message>
  <data>
    <docketNumber>string</docketNumber>
    <dotNumber>
      <status>string</status>
      <Value>string</Value>
    </dotNumber>
    <carrierType>string</carrierType>
    <isMonitored>true</isMonitored>
    <isBlocked>true</isBlocked>
    <Identity>
      <legalName>string</legalName>
      <dbaName>string</dbaName>
      <businessStreet>string</businessStreet>
      <businessCity>string</businessCity>
      <businessState>string</businessState>
      <businessZipCode>string</businessZipCode>
      <businessColonia>string</businessColonia>
      <businessCountry>string</businessCountry>
      <businessPhone>string</businessPhone>
      <businessFax>string</businessFax>
      <mailingStreet>string</mailingStreet>
      <mailingCity>string</mailingCity>
      <mailingState>string</mailingState>
      <mailingZipCode>string</mailingZipCode>
      <mailingColonia>string</mailingColonia>
      <mailingCountry>string</mailingCountry>
      <mailingPhone>string</mailingPhone>
      <mailingFax>string</mailingFax>
      <undeliverableMail>string</undeliverableMail>
      <companyRep1>string</companyRep1>
      <companyRep2>string</companyRep2>
      <cellPhone>string</cellPhone>
      <emailAddress>string</emailAddress>
      <dunBradstreetNum>string</dunBradstreetNum>
      <organization>string</organization>
    </Identity>
    <Authority>
      <authGrantDate>string</authGrantDate>
      <commonAuthority>string</commonAuthority>
      <commonAuthorityPending>string</commonAuthorityPending>
      <commonAuthorityRevocation>string</commonAuthorityRevocation>
      <contractAuthority>string</contractAuthority>
      <contractAuthorityPending>string</contractAuthorityPending>
      <contractAuthorityRevocation>string</contractAuthorityRevocation>
      <brokerAuthority>string</brokerAuthority>
      <brokerAuthorityPending>string</brokerAuthorityPending>
      <brokerAuthorityRevocation>string</brokerAuthorityRevocation>
      <freight>string</freight>
      <passenger>string</passenger>
      <householdGoods>string</householdGoods>
      <private>string</private>
      <enterprise>string</enterprise>
    </Authority>
    <FMCSAInsurance>
      <bipdRequired>string</bipdRequired>
      <bipdOnFile>string</bipdOnFile>
      <cargoRequired>string</cargoRequired>
      <cargoOnFile>string</cargoOnFile>
      <bondSuretyRequired>string</bondSuretyRequired>
      <bondSuretyOnFile>string</bondSuretyOnFile>
      <PolicyList>
        <companyName>string</companyName>
        <attnToName>string</attnToName>
        <address>string</address>
        <city>string</city>
        <stateCode>string</stateCode>
        <postalCode>string</postalCode>
        <countryCode>string</countryCode>
        <phone>string</phone>
        <fax>string</fax>
        <insuranceType>string</insuranceType>
        <policyNumber>string</policyNumber>
        <postedDate>string</postedDate>
        <effectiveDate>string</effectiveDate>
        <cancelationDate>string</cancelationDate>
        <coverageFrom>string</coverageFrom>
        <coverageTo>string</coverageTo>
        <amBestRating>string</amBestRating>
      </PolicyList>
    </FMCSAInsurance>
    <CertData>
      <status>string</status>
      <noncoop>true</noncoop>
      <Certificate>
        <certificateID>string</certificateID>
        <producerName>string</producerName>
        <producerAddress>string</producerAddress>
        <producerCity>string</producerCity>
        <producerState>string</producerState>
        <producerZip>string</producerZip>
        <producerPhone>string</producerPhone>
        <producerFax>string</producerFax>
        <producerEmail>string</producerEmail>
        <paidFor>string</paidFor>
        <BlobName>string</BlobName>
        <Coverage>
          <insurerName>string</insurerName>
          <insurerAMBestRating>string</insurerAMBestRating>
          <type>string</type>
          <policyNumber>string</policyNumber>
          <expirationDate>string</expirationDate>
          <coverageLimit>string</coverageLimit>
          <deductable>string</deductable>
          <referBreakdown>string</referBreakdown>
          <referBreakDeduct>string</referBreakDeduct>
          <cancellationDate>string</cancellationDate>
        </Coverage>
      </Certificate>
    </CertData>
    <Safety>
      <rating>string</rating>
      <ratingDate>string</ratingDate>
      <unsafeDrvPCT>string</unsafeDrvPCT>
      <unsafeDrvOT>string</unsafeDrvOT>
      <unsafeDrvSV>string</unsafeDrvSV>
      <unsafeDrvAlert>string</unsafeDrvAlert>
      <unsafeDrvTrend>string</unsafeDrvTrend>
      <unsafeDrvCNT>1</unsafeDrvCNT>
      <hosPCT>string</hosPCT>
      <hosOT>string</hosOT>
      <hosSV>string</hosSV>
      <hosAlert>string</hosAlert>
      <hosTrend>string</hosTrend>
      <hosCNT>1</hosCNT>
      <drvFitPCT>string</drvFitPCT>
      <drvFitOT>string</drvFitOT>
      <drvFitSV>string</drvFitSV>
      <drvFitAlert>string</drvFitAlert>
      <drvFitTrend>string</drvFitTrend>
      <drvFitCNT>1</drvFitCNT>
      <controlSubPCT>string</controlSubPCT>
      <controlSubOT>string</controlSubOT>
      <controlSubSV>string</controlSubSV>
      <controlSubAlert>string</controlSubAlert>
      <controlSubTrend>string</controlSubTrend>
      <controlSubCNT>1</controlSubCNT>
      <vehMaintPCT>string</vehMaintPCT>
      <vehMaintOT>string</vehMaintOT>
      <vehMaintSV>string</vehMaintSV>
      <vehMaintAlert>string</vehMaintAlert>
      <vehMaintTrend>string</vehMaintTrend>
      <vehMaintCNT>1</vehMaintCNT>
      <hazMatPCT>string</hazMatPCT>
      <hazMatOT>string</hazMatOT>
      <hazMatSV>string</hazMatSV>
      <hazMatAlert>string</hazMatAlert>
      <hazMatTrend>string</hazMatTrend>
      <hazMatCNT>1</hazMatCNT>
    </Safety>
    <Inspection>
      <inspectVehUS>string</inspectVehUS>
      <inspectVehOOSUS>string</inspectVehOOSUS>
      <inspectVehOOSPctUS>string</inspectVehOOSPctUS>
      <inspectDrvUS>string</inspectDrvUS>
      <inspectDrvOOSUS>string</inspectDrvOOSUS>
      <inspectDrvOOSPctUS>string</inspectDrvOOSPctUS>
      <inspectHazUS>string</inspectHazUS>
      <inspectHazOOSUS>string</inspectHazOOSUS>
      <inspectHazOOSPctUS>string</inspectHazOOSPctUS>
      <inspectIEPUS>string</inspectIEPUS>
      <inspectIEPOOSUS>string</inspectIEPOOSUS>
      <inspectIEPOOSPctUS>string</inspectIEPOOSPctUS>
      <inspectTotalIEPUS>string</inspectTotalIEPUS>
      <inspectTotalUS>string</inspectTotalUS>
      <inspectVehCAN>string</inspectVehCAN>
      <inspectVehOOSCAN>string</inspectVehOOSCAN>
      <inspectVehOOSPctCAN>string</inspectVehOOSPctCAN>
      <inspectDrvCAN>string</inspectDrvCAN>
      <inspectDrvOOSCAN>string</inspectDrvOOSCAN>
      <inspectDrvOOSPctCAN>string</inspectDrvOOSPctCAN>
      <inspectTotalCAN>string</inspectTotalCAN>
    </Inspection>
    <Crash>
      <crashFatalUS>string</crashFatalUS>
      <crashInjuryUS>string</crashInjuryUS>
      <crashTowUS>string</crashTowUS>
      <crashTotalUS>string</crashTotalUS>
      <crashFatalCAN>string</crashFatalCAN>
      <crashInjuryCAN>string</crashInjuryCAN>
      <crashTowCAN>string</crashTowCAN>
      <crashTotalCAN>string</crashTotalCAN>
    </Crash>
    <Review>
      <reviewType>string</reviewType>
      <reviewDate>string</reviewDate>
      <reviewDocNum>string</reviewDocNum>
      <reviewMiles>string</reviewMiles>
      <mcs150Date>string</mcs150Date>
      <mcs150MileYear>string</mcs150MileYear>
      <mcs150Miles>string</mcs150Miles>
      <accidentRate>string</accidentRate>
      <accidentRatePrevent>string</accidentRatePrevent>
    </Review>
    <Operation>
      <dotAddDate>string</dotAddDate>
      <carrierOperation>string</carrierOperation>
      <shipperOperation>string</shipperOperation>
      <mxOperationType>string</mxOperationType>
      <mxRFCNumber>string</mxRFCNumber>
      <outOfService>string</outOfService>
      <outOfServiceDate>string</outOfServiceDate>
      <outOfServiceReason>string</outOfServiceReason>
      <entityCarrier>string</entityCarrier>
      <entityShipper>string</entityShipper>
      <entityBroker>string</entityBroker>
      <entityFreightFowarder>string</entityFreightFowarder>
      <entityCargoTank>string</entityCargoTank>
      <classAuthForHire>string</classAuthForHire>
      <classMigrant>string</classMigrant>
      <classIndianNation>string</classIndianNation>
      <classExemptForHire>string</classExemptForHire>
      <classUSMail>string</classUSMail>
      <classPrivateProperty>string</classPrivateProperty>
      <classFederalGovernment>string</classFederalGovernment>
      <classPrivPassBusiness>string</classPrivPassBusiness>
      <classStateGovernment>string</classStateGovernment>
      <classPrivPassNonBusiness>string</classPrivPassNonBusiness>
      <classLocalGovernment>string</classLocalGovernment>
      <classOther>string</classOther>
      <operatingStatus>string</operatingStatus>
    </Operation>
    <Cargo>
      <hazmatIndicator>string</hazmatIndicator>
      <cargoGenFreight>string</cargoGenFreight>
      <cargoHousehold>string</cargoHousehold>
      <cargoMetal>string</cargoMetal>
      <cargoMotorVeh>string</cargoMotorVeh>
      <cargoDriveTow>string</cargoDriveTow>
      <cargoLogPole>string</cargoLogPole>
      <cargoBldgMaterial>string</cargoBldgMaterial>
      <cargoMobileHome>string</cargoMobileHome>
      <cargoMachLarge>string</cargoMachLarge>
      <cargoProduce>string</cargoProduce>
      <cargoLiqGas>string</cargoLiqGas>
      <cargoIntermodal>string</cargoIntermodal>
      <cargoPassengers>string</cargoPassengers>
      <cargoOilfield>string</cargoOilfield>
      <cargoLivestock>string</cargoLivestock>
      <cargoGrainfeed>string</cargoGrainfeed>
      <cargoCoalcoke>string</cargoCoalcoke>
      <cargoMeat>string</cargoMeat>
      <cargoGarbage>string</cargoGarbage>
      <cargoUSMail>string</cargoUSMail>
      <cargoChemicals>string</cargoChemicals>
      <cargoDryBulk>string</cargoDryBulk>
      <cargoRefrigerated>string</cargoRefrigerated>
      <cargoBeverages>string</cargoBeverages>
      <cargoPaperProd>string</cargoPaperProd>
      <cargoUtilities>string</cargoUtilities>
      <cargoFarmSupplies>string</cargoFarmSupplies>
      <cargoConstruction>string</cargoConstruction>
      <cargoWaterwell>string</cargoWaterwell>
      <cargoOther>string</cargoOther>
      <cargoOtherDesc>string</cargoOtherDesc>
    </Cargo>
    <Drivers>
      <driversTotal>string</driversTotal>
      <driversAvgLeased>string</driversAvgLeased>
      <driversCDL>string</driversCDL>
      <driversInter>string</driversInter>
      <driversInterLT100>string</driversInterLT100>
      <driversInterGT100>string</driversInterGT100>
      <driversIntra>string</driversIntra>
      <driversIntraLT100>string</driversIntraLT100>
      <driversIntraGT100>string</driversIntraGT100>
    </Drivers>
    <Equipment>
      <trucksTotal>string</trucksTotal>
      <totalPower>string</totalPower>
      <fleetsize>string</fleetsize>
      <trucksOwned>string</trucksOwned>
      <trucksTerm>string</trucksTerm>
      <trucksTrip>string</trucksTrip>
      <trailersOwned>string</trailersOwned>
      <trailersTerm>string</trailersTerm>
      <trailersTrip>string</trailersTrip>
      <tractorsOwned>string</tractorsOwned>
      <tractorsTerm>string</tractorsTerm>
      <tractorsTrip>string</tractorsTrip>
    </Equipment>
    <Other>
      <carbTru>string</carbTru>
      <smartway>string</smartway>
      <watchdogReports>string</watchdogReports>
    </Other>
    <RiskAssessment>
      <Overall>string</Overall>
      <Authority>string</Authority>
      <Insurance>string</Insurance>
      <Safety>string</Safety>
      <Operation>string</Operation>
      <Other>string</Other>
    </RiskAssessment>
    <RiskAssessmentDetails>
      <IsIntrastateCarrier>true</IsIntrastateCarrier>
      <TotalPoints>1</TotalPoints>
      <OverallRating>string</OverallRating>
      <ReviewState>string</ReviewState>
      <Authority>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Authority>
      <Insurance>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Insurance>
      <Safety>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Safety>
      <Operation>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Operation>
      <Other>
        <TotalPoints>1</TotalPoints>
        <OverallRating>string</OverallRating>
        <HasRuleOverride>true</HasRuleOverride>
        <Infractions>
          <Points>1</Points>
          <RuleName>string</RuleName>
          <RiskLevel>string</RiskLevel>
          <RuleText>string</RuleText>
          <RuleOutput>string</RuleOutput>
          <PreReviewScore>1</PreReviewScore>
          <PreReviewRiskLevel>string</PreReviewRiskLevel>
          <RuleEnforced>true</RuleEnforced>
        </Infractions>
      </Other>
      <ReviewDetails>
        <ReviewID>1</ReviewID>
        <PreReviewOverall>string</PreReviewOverall>
        <PreReviewAuthority>string</PreReviewAuthority>
        <PreReviewInsurance>string</PreReviewInsurance>
        <PreReviewSafety>string</PreReviewSafety>
        <PreReviewOperation>string</PreReviewOperation>
        <PreReviewOther>string</PreReviewOther>
        <ReviewUser>string</ReviewUser>
        <ReviewDate>1970-01-01T00:00:00.001Z</ReviewDate>
        <ReviewReason>string</ReviewReason>
        <ReviewNote>string</ReviewNote>
        <ReviewExpirationDate>1970-01-01T00:00:00.001Z</ReviewExpirationDate>
      </ReviewDetails>
    </RiskAssessmentDetails>
    <CarrierRatings>
      <myRating>1</myRating>
      <totalRatings>1</totalRatings>
      <lowRatings>1</lowRatings>
      <avgRating>1.1</avgRating>
    </CarrierRatings>
    <LatestInvitation>
      <InvitedByUserName>string</InvitedByUserName>
      <InvitedByEmail>string</InvitedByEmail>
      <InvitedByFirstName>string</InvitedByFirstName>
      <InvitedByLastName>string</InvitedByLastName>
      <InvitationSentDate>1970-01-01T00:00:00.001Z</InvitationSentDate>
      <InvitationRecipient>string</InvitationRecipient>
    </LatestInvitation>
    <IncidentReports>
      <TotalIncidentReports>1</TotalIncidentReports>
      <TotalIncidentReportsWithFraud>1</TotalIncidentReportsWithFraud>
    </IncidentReports>
  </data>
</MyCarrierPacketsApi.DTOs.MonitoredCarrierDataDTO>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| pageNumber |  | The current page number. | query | integer |
| pageSize |  | The number of carriers returned per page. The recommended and default value is 250. The max is 500. | query | integer |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers
  - ### [post](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_BlockedCarriers)[/api/v1/Carrier/BlockedCarriers](https://api.mycarrierpackets.com/swagger/ui/index\#!/CarrierController/CarrierController_BlockedCarriers)



    - [Provides a list of blocked carriers.](https://api.mycarrierpackets.com/swagger/ui/index#!/CarrierController/CarrierController_BlockedCarriers)

#### Implementation Notes

If pagination parameters are not supplied, all blocked carriers are returned. Otherwise, the number of blocked carriers returned is limited to the pageSize.
If paging is requested, the response header will contain an "X-Pagination" item containing the details of the paged response.

#### Response Class (Status 200)

OK

    - [Model](https://api.mycarrierpackets.com/swagger/ui/index#)
    - [Example Value](https://api.mycarrierpackets.com/swagger/ui/index#)

Inline Model \[\
\
Inline Model 1\
\
\]

Inline Model 1 {

DOTNumber (integer, optional),

DocketNumber (string, optional),

IntrastateNumber (string, optional),

CreatedDate (string, optional),

CreatedBy (string, optional),

LastModifiedDate (string, optional),

LastModifiedBy (string, optional)

}

```
[\
  {\
    "DOTNumber": 0,\
    "DocketNumber": "string",\
    "IntrastateNumber": "string",\
    "CreatedDate": "2026-05-17T23:54:51.362Z",\
    "CreatedBy": "string",\
    "LastModifiedDate": "2026-05-17T23:54:51.362Z",\
    "LastModifiedBy": "string"\
  }\
]
```

```
<?xml version="1.0"?>
<Inline Model>
  <DOTNumber>1</DOTNumber>
  <DocketNumber>string</DocketNumber>
  <IntrastateNumber>string</IntrastateNumber>
  <CreatedDate>1970-01-01T00:00:00.001Z</CreatedDate>
  <CreatedBy>string</CreatedBy>
  <LastModifiedDate>1970-01-01T00:00:00.001Z</LastModifiedDate>
  <LastModifiedBy>string</LastModifiedBy>
</Inline Model>
```

Response Content Typeapplication/jsontext/jsonapplication/xmltext/xml

#### Headers

| Header | Description | Type | Other |
| --- | --- | --- | --- |
| X-Pagination | Pagination data formatted as {"pageNumber":1,"pageSize":2500,"totalPages":10,"totalCount":25000} | string |  |

#### Parameters

| Parameter | Value | Description | Parameter Type | Data Type |
| --- | --- | --- | --- | --- |
| pageNumber |  | The current page number. | query | integer |
| pageSize |  | The number of carriers returned per page. The recommended and default value is 2500. The max is 5000. | query | integer |
| Authorization |  | bearer access\_token | header | string |

[Hide Response](https://api.mycarrierpackets.com/swagger/ui/index#)

#### Curl

#### Request URL

#### Response Body

#### Response Code

#### Response Headers

#### \[ base url:   , api version: v1  \]  [![](https://online.swagger.io/validator?url=https://api.mycarrierpackets.com/swagger/docs/v1)](https://online.swagger.io/validator/debug?url=https://api.mycarrierpackets.com/swagger/docs/v1)