---
name: freight-domain-glossary
description: Freight brokerage industry terminology and domain concepts. Use when working with laneweaverTMS to understand loads, tenders, carriers, accounts, facilities, stops, financial terms, status workflows, equipment types, and common abbreviations.
---

# Freight Brokerage Domain Glossary

Quick reference for freight brokerage terminology used throughout laneweaverTMS.

## Core Entities

| Entity | Description | ID Format |
|--------|-------------|-----------|
| **Load** | A shipment transaction between shipper and carrier | `L-XXXXXX` |
| **Tender** | Customer request for freight capacity (often from EDI 204) | `T-XXXXXX` |
| **Carrier** | Motor carrier transporting freight (has MC#, DOT#, SCAC) | UUID |
| **Account** | Customer organization (not individual contacts) | UUID |
| **Facility** | Physical location: warehouse, shipper, consignee, or distribution center | UUID |
| **Stop** | Pickup or delivery point on a load; loads have 2+ stops | UUID |

### Entity Relationships

```
Account (customer) -> Tender (request) -> Load (shipment) -> Carrier (transporter)
                                              |
                                              v
                                    Stops (pickup/delivery at Facilities)
```

## Carrier Identifiers

| Identifier | Issuing Authority | Format | Example |
|------------|-------------------|--------|---------|
| **MC Number** | FMCSA | MC-XXXXXX | MC-123456 |
| **DOT Number** | USDOT | Numeric | 1234567 |
| **SCAC Code** | NMFTA | 2-4 alpha chars | ABCD |

## Financial Terms

| Term | Definition |
|------|------------|
| **Customer Rate** | What the customer pays the broker for the shipment |
| **Carrier Rate** | What the broker pays the carrier |
| **Gross Profit** | `customer_rate - carrier_rate` |
| **Net Profit** | Gross profit adjusted for accessorials and fees |
| **Accessorials** | Additional charges beyond base linehaul rate |
| **Factoring** | Third-party purchase of carrier invoices for immediate payment |

### Common Accessorials

| Accessorial | Description |
|-------------|-------------|
| **Detention** | Charge for driver wait time exceeding free time |
| **Lumper** | Fee for third-party loading/unloading services |
| **TONU** | Truck Ordered Not Used - cancellation fee when carrier arrives but load cancelled |
| **Layover** | Compensation for overnight wait between pickup and delivery |
| **Fuel Surcharge** | Variable charge tied to diesel fuel prices |
| **Deadhead** | Miles driven empty to reach pickup location |

## Status Workflows

### Load Status Lifecycle

```
uncovered -> assigned -> dispatched -> at_origin -> in_transit -> at_destination -> delivered
```

| Status | Description |
|--------|-------------|
| `uncovered` | No carrier assigned |
| `assigned` | Carrier committed, not yet dispatched |
| `dispatched` | Driver confirmed and en route to pickup |
| `at_origin` | Driver arrived at pickup facility |
| `in_transit` | Loaded and moving to destination |
| `at_destination` | Driver arrived at delivery facility |
| `delivered` | Freight delivered, awaiting POD |

### Tender Status

| Status | Description |
|--------|-------------|
| `pending` | Awaiting broker acceptance |
| `accepted` | Broker accepted, capacity search in progress |
| `planned` | Load created from tender |
| `cancelled` | Customer cancelled request |

### Invoice Status

| Status | Description |
|--------|-------------|
| `draft` | Invoice created, not sent |
| `sent` | Invoice sent to customer |
| `partial_payment` | Partial payment received |
| `paid` | Fully paid |
| `void` | Invoice cancelled/voided |

## Equipment Types

| Type | Description | Common Cargo |
|------|-------------|--------------|
| **Dry Van** | Enclosed trailer, no temp control | General freight, palletized goods |
| **Reefer** | Refrigerated trailer | Produce, meat, pharmaceuticals |
| **Flatbed** | Open platform, no sides | Steel, lumber, machinery |
| **Step Deck** | Lower deck height, easier loading | Tall equipment, vehicles |
| **Conestoga** | Flatbed with retractable tarp system | Weather-sensitive flatbed freight |

## Operational Terms

| Term | Definition |
|------|------------|
| **POD** | Proof of Delivery - signed document confirming receipt |
| **BOL** | Bill of Lading - shipping document with freight details |
| **Drop and Hook** | Driver drops loaded trailer, hooks to pre-loaded trailer |
| **Live Load/Unload** | Driver waits while freight is loaded/unloaded |
| **Deadhead** | Miles driven with empty trailer |
| **Bounce** | Carrier backing out of a committed load |
| **Hot Load** | Urgent shipment requiring immediate capacity |

## Regulatory Terms

| Term | Definition |
|------|------------|
| **FMCSA** | Federal Motor Carrier Safety Administration |
| **USDOT** | United States Department of Transportation |
| **CSA Score** | Carrier Safety Administration score (safety rating) |
| **HOS** | Hours of Service - driver work time regulations |
| **ELD** | Electronic Logging Device - tracks driver hours |

## Common Abbreviations

| Abbreviation | Full Term |
|--------------|-----------|
| **TMS** | Transportation Management System |
| **EDI** | Electronic Data Interchange |
| **TONU** | Truck Ordered Not Used |
| **POD** | Proof of Delivery |
| **BOL** | Bill of Lading |
| **A/R** | Accounts Receivable (customer invoices) |
| **A/P** | Accounts Payable (carrier bills) |
| **LTL** | Less Than Truckload |
| **FTL** | Full Truckload |
| **OTR** | Over The Road (long-haul) |
| **P&D** | Pickup and Delivery |
| **RPM** | Revenue Per Mile |
| **CPM** | Cost Per Mile |

## Database Conventions in laneweaverTMS

- Load numbers: `L-XXXXXX` format (generated via trigger)
- Tender numbers: `T-XXXXXX` format (generated via trigger)
- All monetary values: `NUMERIC(10,2)` type
- All status fields: PostgreSQL ENUM types
- Carrier identifiers stored as `TEXT` (MC#, DOT#, SCAC)
