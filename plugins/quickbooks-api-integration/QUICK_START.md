# QuickBooks API Integration - Quick Start

Get started with QuickBooks API integration in 3 steps.

## TL;DR

```bash
# 1. Install the plugin
/plugin marketplace add /Users/fakebizprez/Developer/repositories/dotfiles cloudmachines-marketplace
/plugin install quickbooks-api-integration@cloudmachines-marketplace

# 2. See what's available
/quickbooks

# 3. Start with authentication
/quickbooks auth
```

---

## Step 1: Install (2 minutes)

### Add Marketplace and Install Plugin

```bash
/plugin marketplace add /Users/fakebizprez/Developer/repositories/dotfiles cloudmachines-marketplace
/plugin install quickbooks-api-integration@cloudmachines-marketplace
```

### Verify Installation

```bash
/quickbooks
```

You should see the overview menu with available topics.

**Done?** ✅ Move to Step 2

---

## Step 2: Set Up Authentication (15 minutes)

### Get OAuth2 Credentials

1. Go to https://developer.intuit.com
2. Create a new app
3. Copy your Client ID and Client Secret
4. Set redirect URI (e.g., `http://localhost:3000/callback`)

### Get Setup Code

```bash
/quickbooks auth
```

This provides:
- Complete OAuth2 flow explanation
- Token refresh code (Node.js and Python)
- Token storage best practices
- Error handling patterns

**Done?** ✅ Move to Step 3

---

## Step 3: Your First Integration (30 minutes)

### Choose Your Starting Point

#### Option A: Create an Invoice

```bash
/quickbooks invoice
```

Follow the guided workflow:
1. Query or create customer
2. Set up line items
3. Create invoice
4. Send via email (optional)

#### Option B: Record a Payment

```bash
/quickbooks payment
```

Follow the guided workflow:
1. Query invoices by customer
2. Create payment record
3. Apply to one or more invoices
4. Handle partial payments

#### Option C: Set Up Sync

```bash
/quickbooks sync
```

Choose your approach:
- **CDC (Polling)**: For batch syncs every hour/day
- **Webhooks**: For real-time updates
- **Both**: Webhooks primary, CDC backup

**Done?** ✅ You're ready to build!

---

## Common Next Steps

### Explore All Topics

```bash
/quickbooks
```

Available topics:
- `auth` - OAuth2 authentication
- `invoice` - Invoice creation and management
- `payment` - Payment recording and application
- `sync` - CDC and webhook configuration
- `debug` - Error troubleshooting
- `batch` - Bulk operations
- `customer`, `item`, `account` - Entity management
- `query` - Query language and filtering

### Get Entity-Specific Help

```bash
/quickbooks customer   # Customer CRUD operations
/quickbooks item       # Product/service items
/quickbooks account    # Chart of accounts
```

### Troubleshoot Issues

```bash
/quickbooks debug
```

Interactive troubleshooting for common API errors with specific resolutions.

### Optimize with Batch Operations

```bash
/quickbooks batch
```

Learn to process up to 30 operations in a single API call.

---

## Typical First Integration Flow

Here's the most common path developers take:

```
1. /quickbooks auth
   ↓
   Set up OAuth2, get tokens working

2. /quickbooks customer
   ↓
   Create or query customers

3. /quickbooks invoice
   ↓
   Create first invoice

4. /quickbooks payment
   ↓
   Record payment against invoice

5. /quickbooks sync
   ↓
   Set up ongoing synchronization

6. /quickbooks debug
   ↓
   Handle any errors encountered
```

**Time to first working integration:** ~1-2 hours

---

## Code Examples Included

Every topic provides production-ready code:

- ✅ **OAuth2 Token Refresh** (Node.js, Python)
- ✅ **Create Invoice** (Python with error handling)
- ✅ **Record Payment** (Python with multi-invoice support)
- ✅ **Batch Operations** (Node.js with 30 operations)
- ✅ **Query with Filters** (Python with pagination)
- ✅ **Update Customer** (Node.js sparse update)

All examples include:
- Complete working code
- Error handling
- Best practices
- Comments explaining key concepts

---

## Integration Scenarios

### ERP Integration
Start with: `/quickbooks invoice` → `/quickbooks payment` → `/quickbooks sync`

### CRM Integration
Start with: `/quickbooks customer` → `/quickbooks invoice` → `/quickbooks sync`

### TMS Integration
Start with: `/quickbooks invoice` → `/quickbooks customer` → `/quickbooks batch`

### E-Commerce Integration
Start with: `/quickbooks auth` → `/quickbooks invoice` → `/quickbooks payment`

### Payment Gateway Integration
Start with: `/quickbooks payment` → `/quickbooks query` → `/quickbooks sync`

---

## Quick Reference

### Most Used Commands

| Command | When to Use |
|---------|-------------|
| `/quickbooks` | See all available topics |
| `/quickbooks auth` | Set up OAuth2 authentication |
| `/quickbooks invoice` | Create invoices |
| `/quickbooks payment` | Record payments |
| `/quickbooks sync` | Set up CDC or webhooks |
| `/quickbooks debug` | Troubleshoot errors |

### Common Errors

| Error Code | Fix Command |
|------------|-------------|
| 401 Unauthorized | `/quickbooks auth` (refresh tokens) |
| 3200 SyncToken | `/quickbooks debug` (re-read entity) |
| 3100 Invalid Ref | `/quickbooks debug` (verify references) |
| 6000 Missing Field | `/quickbooks debug` (check required fields) |
| 429 Rate Limit | `/quickbooks debug` (implement backoff) |

---

## Full Documentation

- **Detailed Overview**: [PLUGIN_OVERVIEW.md](PLUGIN_OVERVIEW.md)
- **Installation Guide**: [INSTALL.md](INSTALL.md)
- **Complete README**: [README.md](README.md)

---

## Need Help?

1. Run `/quickbooks` to see all available topics
2. Run `/quickbooks debug` for error-specific help
3. Check [PLUGIN_OVERVIEW.md](PLUGIN_OVERVIEW.md) for detailed capabilities
4. Visit QuickBooks API docs: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/invoice

---

**Ready to integrate?** Start with `/quickbooks auth` and follow the guided workflow!
