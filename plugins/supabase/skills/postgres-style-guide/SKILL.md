---
name: postgres-style-guide
description: PostgreSQL SQL style guide for consistent, readable database code. Use when writing SQL queries, creating tables, defining constraints, or reviewing PostgreSQL code for style compliance.
---

# Postgres SQL Style Guide

## General Principles

- Use **lowercase** for SQL reserved words to maintain consistency and readability
- Employ **consistent, descriptive identifiers** for tables, columns, and other database objects
- Use **white space and indentation** to enhance code readability
- Store **dates in ISO 8601 format** (`yyyy-mm-ddThh:mm:ss.sssz`)
- Include **comments for complex logic** using `/* ... */` for blocks and `--` for line comments
- Always specify **schema prefix** (`public.`) in queries for clarity
- Prefer **explicit over implicit**—always name joins, FK relationships, and computed columns

---

## Naming Conventions

### General Rules

- **Avoid SQL reserved words** and ensure names are unique and under 63 characters
- **Use snake_case** for tables, columns, functions, and identifiers
- **Use lowercase snake_case for custom enum types** (e.g., `public.load_status`, `public.invoice_status`)
- **Use plurals for table names** (e.g., `loads`, `carriers`, `accounts`)
- **Use singular names for columns** (e.g., `load_id`, not `load_ids`)
- **Prefix foreign key columns** with the referenced table name (e.g., `load_id` for a `loads` reference)

### Examples

```sql
-- ✓ Good
table: public.loads
column: load_id (references loads.id)
column: carrier_id (references carriers.id)
column: created_at, updated_at
column: is_cancelled, pod_received

-- ✗ Avoid
table: tbl_loads, Load, LOADs
column: id (ambiguous), load (too short), loadId (camelCase)
column: CreatedOn, created_date (inconsistent patterns)
```

---

## Tables

### Primary Keys & Identifiers

- **Always add an `id` column as primary key** (unless explicitly specified otherwise)
- **Use `uuid` type for primary keys** with `default gen_random_uuid()`
- **Use `bigint` for user IDs and system references** (references to `users.id`)
- **Use `uuid` for cross-entity relationships** (loads, carriers, accounts, etc.)

### Timestamps & Audit Columns

- **Always include audit columns**: `created_at`, `updated_at`, `created_by`, `updated_by`
- **Use `timestamp with time zone`** for all temporal data
- **Default `created_at` and `updated_at`** to `CURRENT_TIMESTAMP`
- **For soft deletes**: add `deleted_at`, `deleted_by` columns
- **Use triggers** to auto-update `updated_at` on every modification

### Table-Level Patterns

- **Always specify the schema**: `create table public.table_name (...)`
- **Always add a descriptive comment** (up to 1024 characters) explaining table purpose
- **Create constraints for data integrity**:
  - `not null` for required columns
  - `unique` for business unique keys (e.g., `mc_number` on carriers)
  - `check` for valid value ranges (e.g., temperature units, payment methods)

### Example Table Definition

```sql
create table public.loads (
  id uuid default gen_random_uuid() primary key,
  load_number text not null,
  owner_id integer not null,
  account_id uuid not null,
  carrier_id uuid,
  load_status public.load_status,
  customer_rate numeric(12, 2),
  carrier_rate numeric(12, 2),
  is_cancelled boolean default false not null,
  cancelled_at timestamp with time zone,
  created_at timestamp with time zone default current_timestamp not null,
  updated_at timestamp with time zone default current_timestamp not null,
  created_by integer not null,
  updated_by integer,
  deleted_at timestamp with time zone,
  deleted_by integer,
  constraint loads_load_number_key unique (load_number),
  constraint loads_owner_id_fkey foreign key (owner_id) references public.users(id),
  constraint loads_account_id_fkey foreign key (account_id) references public.accounts(id),
  constraint loads_carrier_id_fkey foreign key (carrier_id) references public.carriers(id),
  constraint loads_created_by_fkey foreign key (created_by) references public.users(id),
  constraint loads_updated_by_fkey foreign key (updated_by) references public.users(id)
);

comment on table public.loads is
  'Core load/shipment records tracking full lifecycle from creation through delivery with financial metrics and A/P/A/R workflow.';

comment on column public.loads.is_cancelled is
  'Whether this load has been cancelled. See load_cancellations for detailed reasons and TONU charges.';
```

---

## Columns

### Data Types

- **Text fields**: Use `text` (not `varchar(n)`) unless you need to enforce a maximum length
- **Numeric fields**: Use `numeric(precision, scale)` for money values (e.g., `numeric(12, 2)`)
- **Boolean fields**: Use `boolean` with `default false` where applicable
- **Timestamps**: Use `timestamp with time zone` for all temporal data
- **Enums**: Use custom `type` enums for constrained domains (e.g., `public.load_status`)
- **IDs**: Use `uuid` for entity IDs, `bigint` for user/system references

### Column Naming

- **Foreign key columns**: `{singular_table_name}_id` (e.g., `carrier_id`, `load_id`)
- **Boolean columns**: Prefix with `is_` or `has_` when semantically appropriate (e.g., `is_cancelled`, `is_active`), or use descriptive past participles (e.g., `pod_received`, `carrier_bill_received`, `invoice_ready`)
- **Date/time columns**: Use `_at` suffix (e.g., `created_at`, `approved_at`, `cancelled_at`)
- **Generated columns**: Use `generated always as` for computed values

### Example Column Patterns

```sql
-- ✓ Good patterns from LaneWeaver
id uuid default gen_random_uuid() primary key
load_id uuid not null references public.loads(id) on delete cascade
created_by integer not null references public.users(id)
updated_by integer references public.users(id)
is_cancelled boolean default false not null
pod_received boolean default false not null
approved_at timestamp with time zone
carrier_rate numeric(12, 2)
status public.invoice_status default 'Draft'::public.invoice_status

-- Audit trail columns (standard pattern)
created_at timestamp with time zone default current_timestamp not null
updated_at timestamp with time zone default current_timestamp not null
created_by integer not null
updated_by integer

-- Soft delete columns
deleted_at timestamp with time zone
deleted_by integer

-- Generated columns (read-only computed values)
invoice_ready boolean generated always as
  ((pod_received and carrier_bill_received)) stored
```

---

## Type Enums

### Defining Enums

- Create **custom type enums** for constrained domains
- Use **lowercase snake_case** for enum type names (e.g., `load_status`, `invoice_status`, `payment_method`)
- Use **lowercase snake_case** for enum values when representing system states or technical values (e.g., `'uncovered'`, `'in_transit'`, `'electronic_check'`)
- Use **PascalCase** for enum values when representing user-facing labels or business terms (e.g., `'Draft'`, `'Sent'`, `'Dispatcher'`)
- Prefix related enums with a common term (e.g., `load_status`, `carrier_payment_status`, `customer_payment_status`)

### Enum Examples

```sql
-- System state enum (lowercase snake_case values)
create type public.load_status as enum (
  'uncovered',
  'assigned',
  'dispatched',
  'at_origin',
  'in_transit',
  'at_destination',
  'delivered'
);

comment on type public.load_status is
  'Load lifecycle status: uncovered → assigned → dispatched → at_origin → in_transit → at_destination → delivered';

-- Business term enum (PascalCase values)
create type public.invoice_status as enum (
  'Draft',
  'Sent',
  'Pending',
  'Paid',
  'Overdue',
  'Cancelled',
  'Disputed'
);

-- Technical value enum (lowercase snake_case values)
create type public.payment_method as enum (
  'ach',
  'electronic_check',
  'zelle',
  'wire'
);

-- User-facing role enum (PascalCase values)
create type public.carrier_contact_title as enum (
  'Dispatcher',
  'Driver',
  'Accounts Receivable',
  'Manager',
  'Owner'
);
```

---

## Queries

### Query Formatting

**Small queries** (fit on 3-5 lines): Keep compact

```sql
select id, name, status
from public.accounts
where status = 'Active' and deleted_at is null;

update public.carriers
set updated_at = now()
where id = $1;
```

**Medium queries** (6-10 lines): Add newlines around major clauses

```sql
select
  load_id,
  count(*) as num_stops
from public.stops
where load_id = $1
group by load_id
order by load_id;
```

**Large queries** (10+ lines): Use CTEs, format for readability

```sql
with load_summary as (
  -- Get financial metrics per load
  select
    id,
    load_number,
    customer_rate - carrier_rate as gross_profit,
    round(((customer_rate - carrier_rate) / customer_rate * 100), 2) as margin_pct
  from public.loads
  where deleted_at is null
),
top_loads as (
  -- Filter to highest margin loads
  select * from load_summary
  where margin_pct > 30
  order by margin_pct desc
  limit 10
)
select * from top_loads;
```

### Style Rules

- **Use lowercase** for SQL keywords (`select`, `where`, `join`, `group by`)
- **Use full table names** in queries (prefer `public.loads` over `l`)
- **Explicit joins over implicit**: Use `join ... on` instead of `where` conditions for relationships
- **Spaces for readability**: `a = b`, not `a=b`; `value, count`, not `value,count`
- **Line continuity**: Indent sub-clauses consistently

---

## Joins and Subqueries

### Join Formatting

```sql
select
  loads.load_number,
  loads.customer_rate,
  loads.carrier_rate,
  carriers.name as carrier_name,
  accounts.name as account_name
from public.loads
join public.carriers on loads.carrier_id = carriers.id
join public.accounts on loads.account_id = accounts.id
where
  loads.load_status = 'delivered'
  and loads.deleted_at is null
  and carriers.status = 'Active'
order by loads.created_at desc;
```

### Subquery Formatting

**Avoid subqueries in select list** (use joins or views instead)

```sql
-- ✓ Better: Use join
select
  l.id,
  l.load_number,
  count(s.id) as stop_count
from public.loads l
left join public.stops s on l.id = s.load_id
where l.deleted_at is null
group by l.id
order by l.id;

-- ✗ Avoid: Subquery in select
select
  id,
  load_number,
  (select count(*) from stops where load_id = l.id) as stop_count
from loads l;
```

---

## Aliases

### Alias Rules

- **Use meaningful aliases** that reflect the data or transformation
- **Always include the `as` keyword** for clarity
- **Short aliases are OK for temporary CTEs**, but be explicit in final select

### Example

```sql
select
  count(*) as total_shipments,
  sum(customer_rate) as total_revenue,
  avg(customer_rate - carrier_rate) as avg_profit
from public.loads
where load_status = 'delivered' and deleted_at is null;

-- CTE with meaningful names
with carrier_loads as (
  select
    carrier_id,
    count(*) as total_loads,
    sum(customer_rate) as revenue
  from public.loads
  where deleted_at is null
  group by carrier_id
)
select
  carriers.name,
  cl.total_loads,
  cl.revenue
from public.carriers carriers
join carrier_loads cl on carriers.id = cl.carrier_id
order by cl.revenue desc;
```

---

## Complex Queries and CTEs

### CTE Patterns

- **Use CTEs for complex logic** to improve readability
- **Maintain linear flow**: top-level CTE first, then refine downward
- **Comment each CTE block** to explain its purpose
- **Prefer readability over performance** (within reason)

### Comprehensive Example

```sql
with load_financials as (
  -- Calculate financial metrics for each completed load
  select
    id,
    load_number,
    account_id,
    carrier_id,
    customer_rate,
    carrier_rate,
    customer_rate - carrier_rate as gross_profit,
    case
      when customer_rate > 0 then
        round(((customer_rate - carrier_rate) / customer_rate * 100), 2)
      else 0
    end as profit_margin_pct
  from public.loads
  where load_status = 'delivered' and deleted_at is null
),
carrier_performance as (
  -- Aggregate performance by carrier
  select
    carrier_id,
    count(*) as num_loads,
    sum(gross_profit) as total_profit,
    round(avg(profit_margin_pct), 2) as avg_margin_pct
  from load_financials
  group by carrier_id
),
account_performance as (
  -- Aggregate performance by account
  select
    account_id,
    count(*) as num_loads,
    sum(gross_profit) as total_profit,
    round(avg(profit_margin_pct), 2) as avg_margin_pct
  from load_financials
  group by account_id
)
select
  cp.carrier_id,
  carriers.name as carrier_name,
  cp.num_loads,
  cp.total_profit,
  cp.avg_margin_pct
from carrier_performance cp
join public.carriers carriers on cp.carrier_id = carriers.id
order by cp.total_profit desc;
```

---

## Indexes

### Indexing Strategy

- **Create indexes on frequently filtered columns** (where, join conditions)
- **Create indexes on sort columns** (order by)
- **Create composite indexes** for multi-column filters
- **Use partial indexes** where queries filter to a subset (e.g., `where deleted_at is null`)
- **Avoid indexing low-cardinality boolean columns** unless they're primary filters

### Example Index Patterns

```sql
-- Single column indexes
create index idx_loads_account_id on public.loads using btree (account_id);
create index idx_loads_carrier_id on public.loads using btree (carrier_id);
create index idx_loads_created_at on public.loads using btree (created_at);
create index idx_loads_load_status on public.loads using btree (load_status);

-- Partial index (only non-deleted records)
create index idx_loads_deleted_at on public.loads using btree (deleted_at)
where deleted_at is null;

-- Composite index for common joins
create index idx_carrier_bills_load_carrier on public.carrier_bills using btree (load_id, carrier_id);

-- Composite index for filtering + sorting
create index idx_loads_status_created on public.loads using btree (load_status, created_at desc);

-- GIN index for JSON/JSONB columns
create index idx_documents_metadata on public.documents using gin (metadata);

-- BRIN for time-series data (better for large tables)
create index idx_load_cognition_recorded_at on public.load_cognition using brin (recorded_at);
```

---

## Constraints & Data Integrity

### Primary Keys

```sql
-- Always explicit, typically UUID
id uuid default gen_random_uuid() primary key
```

### Unique Constraints

```sql
-- Business unique keys
constraint loads_load_number_key unique (load_number),
constraint carriers_mc_number_key unique (mc_number),
constraint accounts_account_number_key unique (account_number),

-- Compound uniqueness (e.g., one record per load per reference type)
constraint load_references_unique_type_per_load
  unique (load_id, reference_type_id)
```

### Check Constraints

```sql
-- Value range validation
constraint invoices_amount_positive check (amount > 0),
constraint invoices_amount_paid_positive check (amount_paid >= 0),
constraint invoices_amount_paid_not_exceed check (amount_paid <= amount),

-- Enum-like validation
constraint load_cognition_heading_degrees_check
  check (heading >= 0 and heading < 360),
constraint load_cognition_latitude_check
  check (latitude >= -90 and latitude <= 90),
constraint load_cognition_longitude_check
  check (longitude >= -180 and longitude <= 180),

-- Business logic
constraint factoring_company_required_check
  check ((uses_factoring_company = false) or
         (uses_factoring_company = true and factoring_company_id is not null))
```

### Foreign Keys with Actions

```sql
-- Cascade deletes for dependent records
load_id uuid not null references public.loads(id) on delete cascade,

-- Prevent deletion if referenced
reference_type_id uuid not null references public.reference_types(id) on delete restrict,

-- Set null on deletion (allows orphaning)
carrier_id uuid references public.carriers(id) on delete set null
```

### Foreign Key Constraint Naming

Foreign key constraints follow these naming patterns:

```sql
-- Standard pattern: {table}_{column}_fkey
constraint loads_account_id_fkey foreign key (account_id) references public.accounts(id)
constraint loads_carrier_id_fkey foreign key (carrier_id) references public.carriers(id)
constraint carrier_contacts_carrier_id_fkey foreign key (carrier_id) references public.carriers(id)

-- Alternative pattern: fk_{table}_{column} (used for newer tables)
constraint fk_carrier_tractors_created_by foreign key (created_by) references public.users(id)
constraint fk_virtual_yard_created_by foreign key (created_by) references public.users(id)

-- Prefer the standard {table}_{column}_fkey pattern for consistency
```

---

## Views

### View Patterns

- **Use `security_invoker='on'`** for views with RLS compliance
- **Include detail in view names** (e.g., `_with_details`, `_with_financials`)
- **Document view purpose** with comments
- **Include calculated columns** (gross profit %, aging buckets, etc.)

### Example View

```sql
create view public.loads_with_financials with (security_invoker='on') as
select
  id,
  load_number,
  owner_id,
  account_id,
  carrier_id,
  load_status,
  customer_rate,
  carrier_rate,
  (coalesce(revenue, 0) - coalesce(carrier_spend, 0)) as gross_profit,
  case
    when coalesce(revenue, 0) > 0 then
      round(((coalesce(revenue, 0) - coalesce(carrier_spend, 0)) / revenue * 100), 2)
    else 0
  end as gross_profit_percentage,
  case
    when coalesce(total_miles, 0) > 0 then
      round(coalesce(carrier_rate, 0) / total_miles, 2)
    else 0
  end as carrier_rpm,
  case
    when coalesce(total_miles, 0) > 0 then
      round(coalesce(customer_rate, 0) / total_miles, 2)
    else 0
  end as customer_rpm
from public.loads l;

comment on view public.loads_with_financials is
  'Loads with calculated financial metrics. Uses security_invoker for RLS compliance.';
```

---

## Triggers & Functions

### Common Trigger Patterns

```sql
-- Auto-update timestamp
create function public.update_timestamp() returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

create trigger update_loads_timestamp
before update on public.loads
for each row
execute function public.update_timestamp();

-- Sync related table state
create function public.sync_load_billing_flags() returns trigger as $$
begin
  update public.loads
  set
    pod_received = new.pod_received,
    carrier_bill_received = new.carrier_bill_received,
    updated_at = now()
  where id = new.load_id;
  return new;
end;
$$ language plpgsql;

comment on function public.sync_load_billing_flags() is
  'Keeps loads.pod_received and loads.carrier_bill_received in sync with load_billing table';
```

---

## Row Level Security (RLS)

### RLS Policy Patterns

```sql
-- Enable RLS on table
alter table public.loads enable row level security;

-- Authenticated users can select all
create policy "Authenticated users can select loads"
on public.loads
for select
to authenticated
using (true);

-- Authenticated users can insert
create policy "Authenticated users can insert loads"
on public.loads
for insert
to authenticated
with check (true);

-- Authenticated users can update their own records
create policy "Authenticated users can update loads"
on public.loads
for update
to authenticated
using (true)
with check (true);

-- Authenticated users can delete
create policy "Authenticated users can delete loads"
on public.loads
for delete
to authenticated
using (true);
```

---

## Soft Deletes

### Pattern

- Add `deleted_at timestamp with time zone` column
- Add `deleted_by integer` column for audit trail
- **Always filter `where deleted_at is null`** in application queries
- Create **partial indexes** on soft-deleted tables
- Use **triggers** to maintain referential integrity

### Example

```sql
create table public.loads (
  -- ... other columns ...
  deleted_at timestamp with time zone,
  deleted_by integer references public.users(id)
);

-- Partial index for active records
create index idx_loads_deleted_at on public.loads
where deleted_at is null;

-- Standard query pattern (always filter)
select * from public.loads
where deleted_at is null
order by created_at desc;
```

---

## Comments & Documentation

### Table Comments

```sql
comment on table public.loads is
  'Core load/shipment records. See loads_with_financials view for calculated metrics.';
```

### Column Comments

```sql
comment on column public.loads.is_cancelled is
  'Whether this load has been cancelled. See load_cancellations for detailed reasons.';

comment on column public.load_cognition.heading is
  'Direction of travel expressed in degrees from true north (0-359).';
```

### Function Comments

```sql
comment on function public.log_load_event(...) is
  'Records state changes and events for load tracking and audit compliance.';
```

---

## Common Anti-Patterns to Avoid

```sql
-- ✗ Don't use generic "id" in joins
select l.*, c.id from loads l join carriers c on l.carrier_id = c.id;

-- ✓ Use table-qualified columns
select
  loads.id, loads.load_number,
  carriers.id as carrier_id, carriers.name
from public.loads
join public.carriers on loads.carrier_id = carriers.id;

-- ✗ Don't omit schema prefix
select * from loads where deleted_at is null;

-- ✓ Always specify schema
select * from public.loads where deleted_at is null;

-- ✗ Don't use implicit joins
select * from loads, carriers where loads.carrier_id = carriers.id;

-- ✓ Use explicit joins
select * from public.loads
join public.carriers on loads.carrier_id = carriers.id;

-- ✗ Don't filter soft-deleted in application
select * from public.loads order by created_at desc;

-- ✓ Always filter deleted records at database level
select * from public.loads
where deleted_at is null
order by created_at desc;

-- ✗ Don't mix case conventions
select LoadNumber, Carrier_ID, customer_RATE from public.loads;

-- ✓ Use consistent snake_case
select load_number, carrier_id, customer_rate from public.loads;
```

---

## Summary Checklist

- [ ] Table names are **plural** and **snake_case**
- [ ] Primary key is **`id uuid default gen_random_uuid()`**
- [ ] All tables have **`created_at`, `updated_at`, `created_by`, `updated_by`**
- [ ] Foreign keys use **`{table_singular}_id`** naming
- [ ] Foreign key constraints use **`{table}_{column}_fkey`** naming
- [ ] Boolean columns use **`is_` or `has_` prefixes** or descriptive past participles
- [ ] Soft deletes include **`deleted_at` and `deleted_by`**
- [ ] Every table has a **descriptive comment**
- [ ] Enum types use **lowercase snake_case** naming
- [ ] Enum values use **lowercase snake_case** for system states or **PascalCase** for business terms
- [ ] Queries specify the **`public.` schema**
- [ ] Large queries use **CTEs** with meaningful names
- [ ] Frequently filtered columns have **indexes**
- [ ] Soft-deleted tables use **partial indexes**
- [ ] All constraints are **explicit and named**
- [ ] RLS policies are defined for **all tables** (if using Supabase)
