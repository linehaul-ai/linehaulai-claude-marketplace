---
name: load-lifecycle-patterns
description: Document the critical business logic for load lifecycle and billing workflows in laneweaverTMS. Use when implementing load status transitions, billing workflows, financial calculations, TONU handling, or quick pay features.
keywords: [freight-tms, load-management, billing, workflow, business-logic]
---

# Load Lifecycle Patterns - Business Logic for laneweaverTMS

## When to Use This Skill

Use when:
- Implementing load status transitions
- Building billing workflow logic (POD, carrier bills, invoicing)
- Calculating financial metrics (gross profit, margin, net profit)
- Handling load cancellations and TONU scenarios
- Implementing quick pay features for carriers
- Understanding the "life of load" flow from tender to payment

## Load Status Transitions

### Status Lifecycle

```
uncovered → assigned → dispatched → at_origin → in_transit → at_destination → delivered
```

### Valid Transitions Table

| Current Status   | Valid Next Status                      | Trigger                                |
|------------------|----------------------------------------|----------------------------------------|
| `uncovered`      | `assigned`, `cancelled`                | Carrier assignment or cancellation     |
| `assigned`       | `dispatched`, `uncovered`, `cancelled` | Dispatch confirmation or carrier bounce |
| `dispatched`     | `at_origin`, `assigned`, `cancelled`   | Carrier arrives or dispatch cancelled  |
| `at_origin`      | `in_transit`, `cancelled`              | Pickup completed, load departs         |
| `in_transit`     | `at_destination`, `cancelled`          | Approaching delivery destination       |
| `at_destination` | `delivered`, `cancelled`               | Delivery completed                     |
| `delivered`      | (terminal state)                       | No further transitions                 |
| `cancelled`      | (terminal state)                       | No further transitions                 |

### Transition Triggers

**uncovered → assigned**
- Carrier is selected and rate is confirmed
- `carrier_id` is set on the load
- `carrier_rate` is established

**assigned → dispatched**
- Carrier confirms pickup commitment
- Driver information may be captured in `load_cognition`
- Dispatch confirmation timestamp recorded

**dispatched → at_origin**
- Carrier/driver arrives at pickup facility
- Check-in time recorded on origin stop

**at_origin → in_transit**
- Loading completed
- Departure time recorded on origin stop
- BOL (Bill of Lading) may be captured

**in_transit → at_destination**
- Carrier approaching delivery facility
- Optional: ETA updates via tracking

**at_destination → delivered**
- Delivery completed
- Delivery time recorded on destination stop
- POD (Proof of Delivery) capture begins

### Cancellation Rules

**Cancellation can happen from ANY non-terminal status**:
- Creates a `load_cancellations` record
- Sets `loads.is_cancelled = true` (synced via trigger)
- Records cancellation reason and timestamp
- If carrier was assigned, may trigger TONU (see below)

```sql
-- Example cancellation logic
INSERT INTO load_cancellations (load_id, reason, cancelled_by)
VALUES ($1, $2, $3);

-- Trigger auto-syncs is_cancelled flag:
UPDATE loads SET is_cancelled = true WHERE id = $1;
```

## Billing Workflow

### Post-Delivery Billing Flow

```
delivered → POD Received → Carrier Bill Received → Invoice Ready → Customer Invoiced → Carrier Paid
```

### Billing Status Tracking

The `load_billing` table tracks billing milestones for each load:

| Field                  | Purpose                                    |
|------------------------|--------------------------------------------|
| `pod_received`         | Proof of Delivery document received        |
| `pod_received_at`      | Timestamp when POD was received            |
| `carrier_bill_received`| Carrier's invoice/rate confirmation received|
| `carrier_bill_received_at`| Timestamp when carrier bill was received |
| `invoice_ready`        | Generated column: `pod_received AND carrier_bill_received` |

### Invoice Ready Logic

A load is ready for customer invoicing when BOTH:
1. POD is received (proof that delivery occurred)
2. Carrier bill is received (final carrier charges confirmed)

```sql
-- Generated column auto-calculates invoice readiness
invoice_ready BOOLEAN GENERATED ALWAYS AS (pod_received AND carrier_bill_received) STORED
```

### Customer Invoice Creation

After `invoice_ready = true`:
1. Create `customer_invoices` record
2. Link to load via `load_id`
3. Include line items for:
   - Base freight rate (`customer_rate`)
   - Customer accessorials
   - Fuel surcharges (if applicable)
4. Set `invoice_status` to initial state

### Carrier Bill Approval and Payment

After carrier bill is received:
1. Review carrier charges against agreed rate
2. Add carrier accessorials if applicable
3. Approve or dispute discrepancies
4. Schedule payment based on payment terms
5. Handle quick pay if requested (see Quick Pay section)

## Financial Calculations

### Core Formulas

```
grossProfit    = customerRate - carrierRate
grossMarginPct = (grossProfit / customerRate) * 100
netProfit      = (customerRate + customerAccessorials) - (carrierRate + carrierAccessorials)
```

### Calculation Examples

**Basic Load**:
```
Customer Rate: $2,500
Carrier Rate:  $2,000

Gross Profit:  $500
Gross Margin:  20%
```

**Load with Accessorials**:
```
Customer Rate:        $2,500
Customer Accessorials: $150 (detention, lumper)
Carrier Rate:         $2,000
Carrier Accessorials:  $100 (detention)

Revenue:      $2,650 ($2,500 + $150)
Cost:         $2,100 ($2,000 + $100)
Net Profit:   $550
Net Margin:   20.75%
```

### Implementation Pattern

```sql
-- View for financial calculations
CREATE OR REPLACE VIEW public.loads_with_financials
WITH (security_invoker = on)
AS
SELECT
    l.id,
    l.load_number,
    l.customer_rate,
    l.carrier_rate,

    -- Gross profit (base rates only)
    (l.customer_rate - COALESCE(l.carrier_rate, 0)) AS gross_profit,

    -- Gross margin percentage
    CASE
        WHEN l.customer_rate > 0
        THEN ((l.customer_rate - COALESCE(l.carrier_rate, 0)) / l.customer_rate * 100)
        ELSE 0
    END AS gross_margin_pct,

    -- Accessorial totals
    (SELECT COALESCE(SUM(amount), 0)
     FROM customer_accessorials
     WHERE load_id = l.id AND deleted_at IS NULL) AS customer_accessorials_total,

    (SELECT COALESCE(SUM(amount), 0)
     FROM carrier_accessorials
     WHERE load_id = l.id AND deleted_at IS NULL) AS carrier_accessorials_total,

    -- Net profit (including accessorials)
    ((l.customer_rate + (SELECT COALESCE(SUM(amount), 0) FROM customer_accessorials WHERE load_id = l.id AND deleted_at IS NULL)) -
     (COALESCE(l.carrier_rate, 0) + (SELECT COALESCE(SUM(amount), 0) FROM carrier_accessorials WHERE load_id = l.id AND deleted_at IS NULL))) AS net_profit

FROM public.loads l
WHERE l.deleted_at IS NULL;
```

## TONU (Truck Ordered Not Used)

### What is TONU?

TONU occurs when a load is cancelled after a carrier has been assigned and has committed resources (dispatched driver, positioned truck, etc.).

### When TONU Applies

TONU may be charged when:
- Load is cancelled after carrier assignment (`assigned` or later status)
- Cancellation is NOT due to carrier fault
- Carrier has incurred costs (deadhead miles, driver time)

### TONU Workflow

1. **Load Cancelled** - User initiates cancellation after carrier assignment
2. **TONU Evaluation** - Determine if TONU is warranted
3. **TONU Amount Set** - Negotiate or apply standard TONU rate
4. **Record Created** - `load_cancellations` record includes TONU details
5. **Customer Billing** - TONU amount billed to customer
6. **Carrier Payment** - TONU amount paid to carrier (minus margin if applicable)

### Data Model

```sql
-- load_cancellations table captures TONU
CREATE TABLE public.load_cancellations (
    id UUID DEFAULT gen_random_uuid() NOT NULL,
    load_id UUID NOT NULL,
    reason TEXT,
    tonu_amount NUMERIC(10,2),  -- Amount charged for TONU
    cancelled_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    cancelled_by INT4,
    -- ... audit columns
);
```

### Business Rules

- TONU is typically a flat fee (e.g., $250-$500)
- May be a percentage of the agreed carrier rate
- Should be documented in carrier agreements
- Customer may dispute TONU charges
- TONU still triggers customer invoice (for the TONU amount)

## Quick Pay

### What is Quick Pay?

Quick Pay is an accelerated payment option where carriers receive payment faster than standard terms (typically net 30) in exchange for a fee.

### Quick Pay Terms

| Standard Terms | Quick Pay Terms | Typical Fee     |
|----------------|-----------------|-----------------|
| Net 30         | 1-2 days        | 1-2% of payment |
| Net 45         | 1-2 days        | 2-3% of payment |

### Data Model

```sql
-- carrier_bills table tracks quick pay requests
CREATE TABLE public.carrier_bills (
    id UUID DEFAULT gen_random_uuid() NOT NULL,
    load_id UUID NOT NULL,
    carrier_id UUID NOT NULL,
    bill_amount NUMERIC(10,2) NOT NULL,
    bill_status public.carrier_bill_status NOT NULL,

    -- Quick pay fields
    quick_pay_requested BOOLEAN DEFAULT false,
    quick_pay_fee_pct NUMERIC(5,2),  -- e.g., 2.00 for 2%
    quick_pay_fee_amount NUMERIC(10,2),

    scheduled_payment_date DATE,
    paid_at TIMESTAMPTZ,
    -- ... audit columns
);
```

### Quick Pay Workflow

1. **Carrier Requests Quick Pay** - Sets `quick_pay_requested = true`
2. **Fee Calculation** - Calculate quick pay fee
3. **Net Payment** - Deduct fee from carrier payment
4. **Expedited Processing** - Move to front of payment queue
5. **Payment Execution** - Pay within quick pay terms

### Fee Calculation

```
Quick Pay Fee = Bill Amount * Quick Pay Fee Percentage
Net Payment   = Bill Amount - Quick Pay Fee
```

Example:
```
Bill Amount:      $2,000
Quick Pay Fee %:  2%
Quick Pay Fee:    $40
Net Payment:      $1,960
```

### Implementation Notes

- Index `quick_pay_requested = true` for efficient filtering
- Track quick pay fee as revenue (margin improvement)
- Quick pay is optional and carrier-initiated
- Consider automated quick pay for preferred carriers

## Related Tables Reference

### Core Load Tables

| Table             | Purpose                                   |
|-------------------|-------------------------------------------|
| `loads`           | Core load record with status, rates       |
| `tenders`         | Customer tender/order source              |
| `stops`           | Pickup and delivery locations             |
| `load_billing`    | POD/carrier bill tracking, invoice ready  |

### Cancellation & TONU

| Table               | Purpose                                 |
|---------------------|-----------------------------------------|
| `load_cancellations`| Cancellation records with TONU amounts  |

### Invoicing & Payment

| Table               | Purpose                                 |
|---------------------|-----------------------------------------|
| `customer_invoices` | Customer invoices for loads             |
| `carrier_bills`     | Carrier bills/invoices to pay           |
| `customer_accessorials` | Additional customer charges         |
| `carrier_accessorials`  | Additional carrier charges          |

## Business Logic Checklist

```
Load Status Management:
[ ] Validate status transitions against allowed transitions table
[ ] Record status change timestamps
[ ] Sync is_cancelled flag via trigger when load_cancellations inserted
[ ] Prevent invalid transitions (e.g., uncovered → delivered)

Billing Workflow:
[ ] Track POD receipt separately from carrier bill receipt
[ ] Use generated column for invoice_ready calculation
[ ] Create customer invoice only when invoice_ready = true
[ ] Link all billing records to load_id

Financial Calculations:
[ ] Always use NUMERIC(10,2) for money fields
[ ] Include accessorials in net profit calculations
[ ] Handle null carrier_rate (uncovered loads)
[ ] Calculate margin percentages safely (avoid division by zero)

TONU Handling:
[ ] Only apply TONU after carrier assignment
[ ] Record TONU amount in load_cancellations
[ ] Bill TONU to customer
[ ] Pay TONU to carrier (if applicable)

Quick Pay:
[ ] Carrier-initiated request only
[ ] Calculate fee based on agreed percentage
[ ] Deduct fee from carrier payment
[ ] Track as revenue/margin improvement
```

---

**Remember**: This skill focuses on business logic patterns. For database schema implementation details (columns, indexes, constraints), refer to the `laneweaver-database-design` skill.
