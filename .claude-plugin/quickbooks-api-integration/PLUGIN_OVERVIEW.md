# QuickBooks API Integration Plugin - Overview

## Executive Summary

The QuickBooks API Integration plugin is a comprehensive toolkit for developers building integrations between business applications and QuickBooks Online. It provides expert guidance, production-ready code examples, and complete workflows for OAuth2 authentication, invoicing, payments, customer management, batch operations, and real-time data synchronization. Designed specifically for ERP, CRM, TMS, and custom business system integrations.

## Quick Facts

- **Plugin Name**: quickbooks-api-integration
- **Version**: 1.0.0
- **Author**: CloudMachines
- **Command**: `/quickbooks [topic]`
- **Skill**: quickbooks-online-api (92KB comprehensive reference)
- **Languages**: Node.js, Python examples throughout
- **Keywords**: quickbooks, api, integration, oauth2, accounting, erp, crm, invoicing, payments, bookkeeping

## Key Capabilities

### 1. OAuth2 Authentication Management
- Complete OAuth 2.0 setup and configuration
- Automatic token refresh patterns with code examples
- Token lifecycle management (access tokens expire in 1 hour, refresh tokens in 100 days)
- Secure storage best practices
- Error recovery for expired or invalid tokens

### 2. Invoice Automation
- Create invoices with line items, taxes, and custom fields
- Customer lookup and creation workflows
- Item reference management
- Automatic calculation handling
- Email delivery configuration
- Invoice update patterns with SyncToken handling

### 3. Payment Processing
- Record payments against invoices
- Multi-invoice payment application
- Partial payment handling
- Overpayment and unapplied amount management
- Payment method reference setup
- Balance verification workflows

### 4. Data Synchronization
- **Change Data Capture (CDC)**: Poll for changes in last 30 days
- **Webhooks**: Real-time notifications for entity changes
- Decision matrix for CDC vs webhooks
- Combined approach patterns (webhooks + CDC backup)
- Batch sync operations
- Delta update handling

### 5. Batch Operations
- Process up to 30 operations in a single API call
- Mixed operation types (create, update, delete, query)
- Batch ID tracking for result correlation
- Error handling for partial batch failures
- Performance optimization patterns
- Rate limit management

### 6. Error Handling & Troubleshooting
- Common error code resolution (3200, 3100, 6000, 401, 429, 500/503)
- SyncToken mismatch patterns
- Invalid reference troubleshooting
- Missing required field validation
- Rate limiting and exponential backoff
- Retry patterns with automatic recovery

### 7. Entity Management
- **Customers**: Create, read, update, delete (soft delete)
- **Invoices**: Complete invoice lifecycle management
- **Payments**: Payment recording and application
- **Items**: Product and service item management
- **Accounts**: Chart of accounts operations
- **Vendors**: Vendor management workflows
- **Estimates**: Quote and estimate creation

### 8. Query Language & Filtering
- SQL-like query syntax
- Operators: =, <, >, <=, >=, IN, LIKE
- Pattern matching with wildcards
- Date range filtering
- Sorting and pagination
- Max 1000 results per query with pagination patterns

### 9. Production-Ready Code Examples
- **Example 1**: OAuth2 Token Refresh (Node.js)
- **Example 2**: Create Invoice (Python)
- **Example 3**: Sparse Update Customer (Node.js)
- **Example 4**: Query with Filters (Python)
- **Example 5**: Batch Operations (Node.js)
- **Example 6**: Payment Application (Python)

### 10. Best Practices
- Security: Token encryption, no version control commits
- Performance: Batch operations, query optimization, caching
- Data Integrity: SyncToken handling, validation, error recovery
- Rate Limiting: Exponential backoff, request throttling
- Multi-currency: Currency handling and exchange rates
- Testing: Sandbox environment patterns

## Integration Scenarios

### ERP to QuickBooks
- Synchronize orders → invoices
- Sync customers between systems
- Update inventory from ERP to QuickBooks items
- Post payments from ERP to QuickBooks
- Batch sync nightly or real-time webhooks

### CRM to QuickBooks
- Create QuickBooks customers from CRM contacts
- Generate invoices from closed deals
- Sync payment status back to CRM
- Update customer information bidirectionally
- Track invoice status in CRM pipeline

### TMS to QuickBooks
- Create invoices from completed shipments
- Apply freight charges and accessorials
- Record payments from shippers
- Manage customer accounts for carriers
- Batch process daily shipments

### E-Commerce to QuickBooks
- Automatic invoice generation from orders
- Inventory sync between systems
- Payment gateway to QuickBooks posting
- Customer account creation
- Tax calculation integration

### Payment Gateway Integration
- Post Stripe/Square payments to QuickBooks
- Reconcile payment batches
- Handle refunds and chargebacks
- Multi-invoice payment allocation
- Automatic bookkeeping entries

### Custom Business Applications
- Financial reporting dashboards
- Custom invoice templates
- Automated collections workflows
- Revenue recognition automation
- Multi-company consolidation

## Technical Architecture

### Command Structure
Single slash command with argument-based routing:
- Entry point: `/quickbooks [topic]`
- Topics: auth, invoice, payment, sync, debug, batch, customer, item, account, query
- Guided workflows with step-by-step instructions
- Context-aware help and examples

### Skill Structure
Comprehensive 92KB reference document with:
- 40+ major sections covering all API aspects
- OAuth2 authentication and token management
- Core entities reference (Customer, Invoice, Payment, Item, Account)
- CRUD operation patterns
- Query language specification
- Batch operations guide
- Error handling and troubleshooting
- CDC and webhooks documentation
- Best practices and common pitfalls
- 6 production-ready code examples
- Context7 integration for latest API updates

### Knowledge Base
- **API Version**: QuickBooks Online API v3
- **Authentication**: OAuth 2.0 with token refresh
- **Data Format**: JSON (XML also supported)
- **SDKs**: Java, Python, PHP, Node.js, C#
- **Environments**: Sandbox and Production
- **Rate Limits**: Handled with exponential backoff
- **API Endpoint**: https://quickbooks.api.intuit.com/v3/company/{realmId}

## Use Cases by Role

### Backend Developer
- Implement OAuth2 authentication flows
- Build REST API integrations
- Handle asynchronous webhook processing
- Implement retry logic and error recovery

### Integration Engineer
- Design synchronization architectures
- Build CDC polling systems
- Configure webhook endpoints
- Implement data transformation pipelines

### System Architect
- Design multi-system integration patterns
- Plan data flow and consistency strategies
- Architect real-time vs batch processing
- Design error handling and monitoring

### DevOps Engineer
- Deploy webhook endpoints
- Configure rate limiting and throttling
- Monitor API usage and errors
- Implement logging and alerting

## Common Workflows

1. **Initial Setup**: OAuth2 → Test Connection → Sandbox Testing
2. **Invoice Automation**: Customer Lookup → Create Invoice → Send Email
3. **Payment Recording**: Query Invoices → Record Payment → Verify Balance
4. **Data Sync**: Setup CDC/Webhooks → Process Changes → Update Local System
5. **Batch Import**: Prepare Data → Batch Create → Handle Errors → Verify
6. **Error Recovery**: Detect Error → Identify Type → Apply Pattern → Retry

## Success Metrics

After using this plugin, developers should be able to:

- ✅ Set up OAuth2 authentication in under 30 minutes
- ✅ Create first invoice with production-ready code in under 1 hour
- ✅ Implement payment recording workflow in under 2 hours
- ✅ Set up CDC or webhook synchronization in under 4 hours
- ✅ Handle all common API errors with specific resolution patterns
- ✅ Optimize API usage with batch operations
- ✅ Deploy production-ready integrations with confidence

## Next Steps

1. **Install the Plugin**: See [INSTALL.md](INSTALL.md)
2. **Quick Start**: See [QUICK_START.md](QUICK_START.md)
3. **Run First Command**: `/quickbooks` to see capabilities
4. **Start with Auth**: `/quickbooks auth` for OAuth2 setup
5. **Build Integration**: Follow guided workflows for your use case

---

**Ready to integrate?** Start with `/quickbooks` to explore all available workflows and code examples.
