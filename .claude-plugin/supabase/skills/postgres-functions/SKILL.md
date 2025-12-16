---
name: supabase-functions
description: Use when creating or modifying PostgreSQL functions, triggers, or stored procedures for Supabase databases - ensures secure function design with SECURITY INVOKER, proper search_path configuration, and production-ready patterns
---

# Supabase PostgreSQL Functions

Generate high-quality PostgreSQL functions following Supabase best practices.

## When to Use

Use this skill when:
- Creating new PostgreSQL functions or stored procedures
- Writing trigger functions for automated table operations
- Implementing database-side business logic
- Updating existing functions with security best practices
- Designing functions that will be called from Supabase client libraries
- Setting up helper functions for Row-Level Security (RLS) policies

## When NOT to Use

Don't use this skill for:
- Client-side TypeScript/JavaScript functions (use application code instead)
- Supabase Edge Functions (Deno-based serverless functions)
- PostgreSQL schema design (use postgres-table-design skill instead)
- RLS policy creation (use supabase-rls-policy skill instead)

## Core Security Principles

**Security context:** PostgreSQL functions without proper configuration are vulnerable to:
- **Schema search path attacks** - Malicious objects inserted in search path can hijack function calls
- **Privilege escalation** - SECURITY DEFINER functions run with elevated privileges
- **SQL injection** - Dynamic SQL and unqualified references create injection vectors

These patterns prevent real-world exploits observed in production Supabase databases. Following these rules is **mandatory** for security.

### 1. Default to SECURITY INVOKER

Functions run with the permissions of the invoking user by default, ensuring safer access control.

```sql
create or replace function my_schema.example()
returns text
language plpgsql
security invoker  -- Default to this
set search_path = ''
as $$
begin
  return 'hello world';
end;
$$;
```

Only use `SECURITY DEFINER` when explicitly required and document the rationale.

### 2. Always Set search_path

Set `search_path` to empty string to prevent security risks from untrusted schema resolution:

```sql
set search_path = '';
```

Use fully qualified names for all database objects:

```sql
select sum(price * quantity)
from public.order_items  -- Fully qualified
where order_id = calculate_total.order_id;
```

## Function Design Patterns

### Basic Function Template

```sql
create or replace function public.function_name(param_name type)
returns return_type
language plpgsql
security invoker
set search_path = ''
as $$
declare
  variable_name type;
begin
  -- Function logic here
  return variable_name;
end;
$$;
```

### Function with Parameters

```sql
create or replace function public.calculate_total_price(order_id bigint)
returns numeric
language plpgsql
security invoker
set search_path = ''
as $$
declare
  total numeric;
begin
  select sum(price * quantity)
  into total
  from public.order_items
  where order_id = calculate_total_price.order_id;
  return total;
end;
$$;
```

### Trigger Function

```sql
create or replace function my_schema.update_updated_at()
returns trigger
language plpgsql
security invoker
set search_path = ''
as $$
begin
  new.updated_at := now();
  return new;
end;
$$;

create trigger update_updated_at_trigger
before update on my_schema.my_table
for each row
execute function my_schema.update_updated_at();
```

### Error Handling

```sql
create or replace function my_schema.safe_divide(numerator numeric, denominator numeric)
returns numeric
language plpgsql
security invoker
set search_path = ''
as $$
begin
  if denominator = 0 then
    raise exception 'Division by zero is not allowed';
  end if;
  return numerator / denominator;
end;
$$;
```

### Immutable Function (Optimized)

```sql
create or replace function my_schema.full_name(first_name text, last_name text)
returns text
language sql
security invoker
set search_path = ''
immutable  -- Enables better PostgreSQL optimization
as $$
  select first_name || ' ' || last_name;
$$;
```

## Function Volatility

Choose the appropriate volatility level:

- **IMMUTABLE**: Function always returns the same result for the same inputs. No database modifications or external dependencies.
- **STABLE**: Function returns consistent results within a single query execution. Suitable for functions that read data but don't modify it.
- **VOLATILE** (default): Function can modify database state or has side effects. Use for INSERT/UPDATE/DELETE operations.

## Common Mistakes (Anti-Patterns)

### ❌ WRONG: Missing search_path

```sql
create or replace function public.calculate_total(order_id bigint)
returns numeric
language plpgsql
as $$
begin
  -- SECURITY RISK: Unqualified table reference + no search_path
  select sum(price * quantity) into total
  from order_items  -- Which schema? Attacker can create malicious table
  where order_id = order_id;  -- Also: ambiguous column reference
  return total;
end;
$$;
```

**Problems:**
- No `search_path = ''` allows schema hijacking
- Unqualified `order_items` can resolve to attacker's table
- Parameter name collision (`order_id = order_id` always true)

### ✅ CORRECT: Set search_path and qualify all references

```sql
create or replace function public.calculate_total(order_id bigint)
returns numeric
language plpgsql
security invoker
set search_path = ''
as $$
declare
  total numeric;
begin
  select sum(price * quantity)
  into total
  from public.order_items  -- Fully qualified
  where order_id = calculate_total.order_id;  -- Qualified parameter
  return total;
end;
$$;
```

### ❌ WRONG: SECURITY DEFINER without justification

```sql
create or replace function public.admin_delete_user(user_id uuid)
returns void
language plpgsql
security definer  -- Dangerous: runs as function owner
set search_path = ''
as $$
begin
  delete from public.users where id = user_id;  -- Anyone can call this!
end;
$$;
```

**Problems:**
- Runs with elevated privileges (function owner)
- No access control checks
- Any user can delete any user

### ✅ CORRECT: Use SECURITY INVOKER or add access checks

```sql
create or replace function public.delete_own_account()
returns void
language plpgsql
security invoker  -- Runs as caller
set search_path = ''
as $$
begin
  delete from public.users
  where id = auth.uid();  -- Caller can only delete their own account
end;
$$;
```

Or with SECURITY DEFINER (if truly needed):

```sql
create or replace function public.admin_delete_user(user_id uuid)
returns void
language plpgsql
security definer  -- Justified: needs elevated privileges
set search_path = ''
as $$
begin
  -- REQUIRED: Access control check
  if not exists (
    select 1 from public.user_roles
    where user_id = auth.uid() and role = 'admin'
  ) then
    raise exception 'Access denied: admin role required';
  end if;

  delete from public.users where id = admin_delete_user.user_id;
end;
$$;
```

### ❌ WRONG: Dynamic SQL without validation

```sql
create or replace function public.get_table_data(table_name text)
returns json
language plpgsql
security invoker
set search_path = ''
as $$
begin
  -- SQL INJECTION: Unsanitized input
  return query execute 'select * from ' || table_name;
end;
$$;
```

### ✅ CORRECT: Whitelist valid inputs or use parameters

```sql
create or replace function public.get_table_data(table_name text)
returns json
language plpgsql
security invoker
set search_path = ''
as $$
begin
  -- Whitelist approach: only allow specific tables
  if table_name not in ('orders', 'products', 'customers') then
    raise exception 'Invalid table name';
  end if;

  return query execute format('select * from public.%I', table_name);
  -- %I properly quotes identifiers
end;
$$;
```

## Best Practices

1. **Minimize Side Effects**: Prefer functions that return results over those that modify data unless modification is the purpose
2. **Use Explicit Typing**: Specify input and output types clearly
3. **Test Thoroughly**: Validate all SQL queries are valid PostgreSQL compatible with Supabase
4. **Include Triggers When Needed**: Provide complete `CREATE TRIGGER` statements when functions are designed as triggers
5. **Document Rationale**: Comment why `SECURITY DEFINER` is used if required