# PostgreSQL / Supabase Best Practices Reference

## Migration Conventions

### Naming Pattern

```
YYYYMMDDHHMMSS_descriptive_name.sql
```

Examples:
- `20241230120000_create_users_table.sql`
- `20241230120100_add_email_index_to_users.sql`
- `20241230120200_create_orders_table.sql`

### Migration Structure

```sql
-- Migration: create_users_table
-- Description: Creates the users table with audit columns

-- Up migration
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create updated_at trigger
CREATE TRIGGER set_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Create index for common queries
CREATE INDEX idx_users_email ON users(email);
```

## Table Design Patterns

### Standard Table Template

```sql
CREATE TABLE table_name (
    -- Primary key (prefer UUID)
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    -- Business columns
    -- ...

    -- Foreign keys
    parent_id UUID REFERENCES parent_table(id) ON DELETE CASCADE,

    -- Audit columns (always include)
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID REFERENCES users(id),
    updated_by UUID REFERENCES users(id)
);
```

### Enum Types

```sql
-- Create enum type
CREATE TYPE order_status AS ENUM (
    'pending',
    'confirmed',
    'in_transit',
    'delivered',
    'cancelled'
);

-- Use in table
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    status order_status NOT NULL DEFAULT 'pending'
);
```

## Row Level Security (RLS)

### Enable RLS

```sql
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
```

### Common RLS Policies

```sql
-- Users can only see their own data
CREATE POLICY users_select_own ON users
    FOR SELECT
    USING (auth.uid() = id);

-- Users can only update their own data
CREATE POLICY users_update_own ON users
    FOR UPDATE
    USING (auth.uid() = id);

-- Organization-based access
CREATE POLICY org_access ON documents
    FOR ALL
    USING (
        organization_id IN (
            SELECT organization_id
            FROM user_organizations
            WHERE user_id = auth.uid()
        )
    );
```

## Index Strategies

### When to Create Indexes

```sql
-- Foreign keys (always index)
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Frequently filtered columns
CREATE INDEX idx_orders_status ON orders(status);

-- Composite index for common query patterns
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Partial index for specific conditions
CREATE INDEX idx_active_orders ON orders(user_id)
    WHERE status NOT IN ('delivered', 'cancelled');
```

### Text Search

```sql
-- GIN index for full-text search
CREATE INDEX idx_products_search ON products
    USING GIN(to_tsvector('english', name || ' ' || description));
```

## Function Patterns

### Updated At Trigger Function

```sql
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### Audit Trail Function

```sql
CREATE OR REPLACE FUNCTION audit_changes()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (
        table_name,
        record_id,
        action,
        old_data,
        new_data,
        changed_by,
        changed_at
    ) VALUES (
        TG_TABLE_NAME,
        COALESCE(NEW.id, OLD.id),
        TG_OP,
        CASE WHEN TG_OP = 'DELETE' THEN row_to_json(OLD) ELSE NULL END,
        CASE WHEN TG_OP != 'DELETE' THEN row_to_json(NEW) ELSE NULL END,
        auth.uid(),
        NOW()
    );
    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;
```

## Query Patterns

### Pagination

```sql
-- Offset-based (simple but slow for large offsets)
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;

-- Cursor-based (recommended for large datasets)
SELECT * FROM orders
WHERE created_at < $1  -- cursor value
ORDER BY created_at DESC
LIMIT 20;
```

### Upsert (Insert or Update)

```sql
INSERT INTO user_settings (user_id, theme, notifications)
VALUES ($1, $2, $3)
ON CONFLICT (user_id)
DO UPDATE SET
    theme = EXCLUDED.theme,
    notifications = EXCLUDED.notifications,
    updated_at = NOW();
```

### Soft Delete Pattern

```sql
-- Add deleted_at column
ALTER TABLE orders ADD COLUMN deleted_at TIMESTAMPTZ;

-- Create index for active records
CREATE INDEX idx_orders_active ON orders(id) WHERE deleted_at IS NULL;

-- Soft delete
UPDATE orders SET deleted_at = NOW() WHERE id = $1;

-- Query active records
SELECT * FROM orders WHERE deleted_at IS NULL;
```

## Supabase-Specific

### Auth Integration

```sql
-- Reference auth.users
CREATE TABLE profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    display_name TEXT,
    avatar_url TEXT
);

-- Get current user
SELECT auth.uid();
SELECT auth.jwt();
```

### Real-time Subscriptions

```sql
-- Enable real-time for a table
ALTER PUBLICATION supabase_realtime ADD TABLE orders;
```

### Storage Integration

```sql
-- Reference storage objects
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    storage_path TEXT NOT NULL, -- path in storage bucket
    bucket_id TEXT NOT NULL DEFAULT 'documents'
);
```

## SQL Style Guide

1. **Keywords** - Use UPPERCASE for SQL keywords
2. **Identifiers** - Use snake_case for tables and columns
3. **Indentation** - 4 spaces, align related clauses
4. **Line breaks** - One clause per line for complex queries
5. **Comments** - Use `--` for inline comments

```sql
-- Good
SELECT
    u.id,
    u.name,
    COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.status = 'active'
    AND u.created_at > NOW() - INTERVAL '30 days'
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC;
```
