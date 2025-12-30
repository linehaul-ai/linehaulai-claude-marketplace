---
name: backend-service-patterns
description: Use when implementing API endpoints, business logic, database operations, or adding new entities to laneweaverTMS Go/Echo backend.
---

# Backend Service Patterns - Go/Echo/pgx for laneweaverTMS

## When to Use This Skill

- Implementing new API endpoints (handlers)
- Adding business logic (services)
- Writing database queries (repositories)
- Creating models and DTOs
- Handling transactions
- Building complex filters with QueryBuilder
- Adding validation logic

## Layered Architecture

```
HTTP Request → Handler → Service → Repository → PostgreSQL
                 ↓           ↓           ↓
             Bind/JSON   Business    SQL/pgx
             Validate     Logic    Transaction
                 ↓           ↓           ↓
HTTP Response ← Handler ← Service ← Repository
```

**Layer Responsibilities:**
- **Handler** (`/internal/handlers/`): HTTP request/response, Echo context, bind JSON, return APIResponse
- **Service** (`/internal/services/`): Business logic, validation, orchestration, coordinate repos
- **Repository** (`/internal/repository/`): SQL queries, transactions, pgx operations
- **Models** (`/internal/models/`): Structs with db/json tags, enums, request/response DTOs

## Handler Patterns

### Handler Struct with Dependency Injection

```go
type LoadHandler struct {
    service *services.LoadService
}

func NewLoadHandler(service *services.LoadService) *LoadHandler {
    return &LoadHandler{service: service}
}
```

### Create Handler (POST)

```go
func (h *LoadHandler) Create(c echo.Context) error {
    var req models.CreateLoadRequest
    if err := c.Bind(&req); err != nil {
        return c.JSON(http.StatusBadRequest, models.APIResponse{
            Success: false,
            Message: "Invalid request body",
            Errors:  map[string][]string{"body": {"Failed to parse JSON"}},
        })
    }

    result, err := h.service.CreateLoad(c.Request().Context(), &req)
    if err != nil {
        // Validation errors → 400
        if validationErrors, ok := err.(models.ValidationErrors); ok {
            return c.JSON(http.StatusBadRequest, models.APIResponse{
                Success: false,
                Message: "Validation failed",
                Errors:  validationErrors.ToMap(),
            })
        }
        // Operational errors → 500
        c.Logger().Error("CreateLoad error:", err)
        return c.JSON(http.StatusInternalServerError, models.APIResponse{
            Success: false,
            Message: "Failed to create load",
        })
    }

    return c.JSON(http.StatusCreated, models.APIResponse{
        Success: true,
        Message: "Load created successfully",
        Data:    result,
    })
}
```

### List Handler with Filters (GET)

```go
func (h *LoadHandler) List(c echo.Context) error {
    filters := parseLoadFilters(c)

    items, total, err := h.service.ListLoads(c.Request().Context(), filters)
    if err != nil {
        return c.JSON(http.StatusInternalServerError, models.APIResponse{
            Success: false,
            Message: "Failed to fetch loads",
        })
    }

    response := models.NewPaginatedResponse(items, total, filters.Page, filters.PageSize)
    return c.JSON(http.StatusOK, models.APIResponse{
        Success: true,
        Data:    response,
    })
}
```

### Query Parameter Parsing (Nil Pointer Helpers)

```go
func parseLoadFilters(c echo.Context) models.LoadFilters {
    var filters models.LoadFilters

    // Multi-select (comma-separated)
    if loadStatus := c.QueryParam("load_status"); loadStatus != "" {
        filters.LoadStatus = strings.Split(loadStatus, ",")
    }

    // Optional string
    filters.AccountID = parseStringPtr(c.QueryParam("account_id"))

    // Date range
    filters.PickupDateFrom = parseDatePtr(c.QueryParam("pickup_date_from"))
    filters.PickupDateTo = parseDatePtr(c.QueryParam("pickup_date_to"))

    // Pagination with defaults
    filters.Page = 1
    if page := c.QueryParam("page"); page != "" {
        if p, err := strconv.Atoi(page); err == nil && p > 0 {
            filters.Page = p
        }
    }
    filters.PageSize = 50
    if pageSize := c.QueryParam("page_size"); pageSize != "" {
        if ps, err := strconv.Atoi(pageSize); err == nil && ps > 0 && ps <= 100 {
            filters.PageSize = ps
        }
    }

    return filters
}

// Helper functions for safe type conversion
func parseStringPtr(s string) *string {
    if s == "" {
        return nil
    }
    return &s
}

func parseDatePtr(s string) *time.Time {
    if s == "" {
        return nil
    }
    t, err := time.Parse("2006-01-02", s)
    if err != nil {
        return nil
    }
    return &t
}

func parseFloatPtr(s string) *float64 {
    if s == "" {
        return nil
    }
    f, err := strconv.ParseFloat(s, 64)
    if err != nil {
        return nil
    }
    return &f
}

func parseBoolPtr(s string) *bool {
    if s == "" {
        return nil
    }
    b, err := strconv.ParseBool(s)
    if err != nil {
        return nil
    }
    return &b
}
```

### GetByID Handler

```go
func (h *LoadHandler) GetByID(c echo.Context) error {
    id := c.Param("id")

    load, err := h.service.GetLoadByID(c.Request().Context(), id)
    if err != nil {
        return c.JSON(http.StatusInternalServerError, models.APIResponse{
            Success: false,
            Message: "Failed to fetch load",
        })
    }
    if load == nil {
        return c.JSON(http.StatusNotFound, models.APIResponse{
            Success: false,
            Message: "Load not found",
        })
    }

    return c.JSON(http.StatusOK, models.APIResponse{
        Success: true,
        Data:    load,
    })
}
```

## Service Patterns

### Service Struct with Multiple Repositories

```go
type LoadService struct {
    loadRepo     *repository.LoadRepository
    facilityRepo *repository.FacilityRepository
    accountRepo  *repository.AccountRepository
}

func NewLoadService(
    loadRepo *repository.LoadRepository,
    facilityRepo *repository.FacilityRepository,
    accountRepo *repository.AccountRepository,
) *LoadService {
    return &LoadService{
        loadRepo:     loadRepo,
        facilityRepo: facilityRepo,
        accountRepo:  accountRepo,
    }
}
```

### Create Method with Validation

```go
func (s *LoadService) CreateLoad(ctx context.Context, req *models.CreateLoadRequest) (*models.CreateLoadResponse, error) {
    // 1. Validate request (delegated to models)
    if errors := models.ValidateCreateLoadRequest(req); len(errors) > 0 {
        return nil, errors
    }

    // 2. Business logic (find-or-create facilities, generate IDs, etc.)
    stopParams, err := s.resolveStopFacilities(ctx, req.Stops)
    if err != nil {
        return nil, err
    }

    // 3. Build entity
    load := &models.Load{
        ID:           uuid.New().String(),
        LoadNumber:   s.generateLoadNumber(ctx),
        TenderID:     req.TenderID,
        LoadStatus:   models.LoadStatusUncovered,
        Mode:         &req.Mode,
        CustomerRate: &req.CustomerRate,
    }

    // 4. Call repository
    createParams := repository.CreateLoadParams{Load: load, Stops: stopParams}
    if err := s.loadRepo.CreateWithStops(ctx, createParams); err != nil {
        return nil, fmt.Errorf("failed to create load: %w", err)
    }

    // 5. Build response
    return &models.CreateLoadResponse{
        ID:         load.ID,
        LoadNumber: load.LoadNumber,
        LoadStatus: load.LoadStatus,
    }, nil
}
```

### Retry Logic for Race Conditions

```go
const maxRetries = 3

func (s *LoadService) CreateLoadWithRetry(ctx context.Context, req *models.CreateLoadRequest) (*models.Load, error) {
    var lastErr error
    for attempt := 0; attempt < maxRetries; attempt++ {
        loadNumber, err := s.generateLoadNumber(ctx)
        if err != nil {
            return nil, err
        }

        load := &models.Load{
            ID:         uuid.New().String(),
            LoadNumber: loadNumber,
            // ...
        }

        err = s.loadRepo.Create(ctx, load)
        if err != nil {
            // Retry on unique constraint violation
            if strings.Contains(err.Error(), "duplicate key") ||
                strings.Contains(err.Error(), "loads_load_number_key") {
                lastErr = err
                continue
            }
            return nil, err
        }
        return load, nil
    }
    return nil, fmt.Errorf("failed after %d retries: %w", maxRetries, lastErr)
}
```

## Repository Patterns

### Repository Struct

```go
type LoadRepository struct {
    db *database.Client
}

func NewLoadRepository(db *database.Client) *LoadRepository {
    return &LoadRepository{db: db}
}
```

### Transaction Pattern

```go
func (r *LoadRepository) CreateWithStops(ctx context.Context, params CreateLoadParams) error {
    tx, err := r.db.Begin(ctx)
    if err != nil {
        return fmt.Errorf("failed to begin transaction: %w", err)
    }
    defer tx.Rollback(ctx)

    // Insert load
    loadQuery := `
        INSERT INTO loads (id, load_number, tender_id, load_status, mode, customer_rate, created_at, updated_at)
        VALUES ($1, $2, $3, $4, $5, $6, NOW(), NOW())
    `
    _, err = tx.Exec(ctx, loadQuery,
        params.Load.ID,
        params.Load.LoadNumber,
        params.Load.TenderID,
        params.Load.LoadStatus,
        params.Load.Mode,
        params.Load.CustomerRate,
    )
    if err != nil {
        return fmt.Errorf("failed to insert load: %w", err)
    }

    // Insert stops
    stopQuery := `
        INSERT INTO stops (id, load_id, facility_id, stop_sequence, stop_type, scheduled_date, created_at, updated_at)
        VALUES ($1, $2, $3, $4, $5, $6, NOW(), NOW())
    `
    for _, stop := range params.Stops {
        _, err = tx.Exec(ctx, stopQuery,
            stop.ID, params.Load.ID, stop.FacilityID, stop.StopSequence, stop.StopType, stop.ScheduledDate,
        )
        if err != nil {
            return fmt.Errorf("failed to insert stop %d: %w", stop.StopSequence, err)
        }
    }

    if err = tx.Commit(ctx); err != nil {
        return fmt.Errorf("failed to commit: %w", err)
    }
    return nil
}
```

### GetByID with Not Found Handling

```go
func (r *LoadRepository) GetByID(ctx context.Context, id string) (*models.Load, error) {
    query := `
        SELECT id, load_number, tender_id, load_status, mode, customer_rate, created_at, updated_at
        FROM loads
        WHERE id = $1 AND deleted_at IS NULL
    `
    var load models.Load
    err := r.db.QueryRow(ctx, query, id).Scan(
        &load.ID, &load.LoadNumber, &load.TenderID, &load.LoadStatus,
        &load.Mode, &load.CustomerRate, &load.CreatedAt, &load.UpdatedAt,
    )
    if err != nil {
        if errors.Is(err, pgx.ErrNoRows) {
            return nil, nil // Not found
        }
        return nil, err
    }
    return &load, nil
}
```

### QueryBuilder for Complex Filters

```go
func buildLoadListQuery(filters models.LoadFilters) (string, []interface{}) {
    qb := NewQueryBuilder()

    // Multi-select IN conditions
    qb.AddInCondition("l.load_status", filters.LoadStatus)
    qb.AddInCondition("l.mode", filters.Mode)

    // Single value conditions
    if filters.AccountID != nil {
        qb.AddCondition("t.account_id = $%d", *filters.AccountID)
    }
    if filters.CarrierID != nil {
        qb.AddCondition("l.carrier_id = $%d", *filters.CarrierID)
    }

    // Date ranges
    if filters.PickupDateFrom != nil {
        qb.AddCondition("t.pickup_date >= $%d", *filters.PickupDateFrom)
    }
    if filters.PickupDateTo != nil {
        qb.AddCondition("t.pickup_date <= $%d", *filters.PickupDateTo)
    }

    // Boolean filters
    if filters.IsCancelled != nil {
        qb.AddCondition("l.is_cancelled = $%d", *filters.IsCancelled)
    }

    // Text search
    if filters.Search != nil && *filters.Search != "" {
        qb.AddOrCondition([]string{"l.load_number", "a.name"}, "%"+*filters.Search+"%")
    }

    whereClause, args := qb.Build()

    // Sort column whitelist
    sortColumn := "l.created_at"
    sortColumnMap := map[string]string{
        "load_number": "l.load_number",
        "created_at":  "l.created_at",
        "pickup_date": "t.pickup_date",
    }
    if col, ok := sortColumnMap[filters.SortBy]; ok {
        sortColumn = col
    }

    sortDir := "DESC"
    if filters.SortDir == "asc" {
        sortDir = "ASC"
    }

    offset := (filters.Page - 1) * filters.PageSize
    argIdx := qb.ArgCount()

    baseQuery := `
        SELECT l.id, l.load_number, l.load_status, l.customer_rate, a.name as account_name
        FROM loads l
        JOIN tenders t ON l.tender_id = t.id
        LEFT JOIN accounts a ON t.account_id = a.id
        WHERE l.deleted_at IS NULL
    ` + whereClause

    query := fmt.Sprintf("%s ORDER BY %s %s LIMIT $%d OFFSET $%d",
        baseQuery, sortColumn, sortDir, argIdx+1, argIdx+2)
    args = append(args, filters.PageSize, offset)

    return query, args
}
```

### Find-or-Create Pattern

```go
func (r *FacilityRepository) FindOrCreate(ctx context.Context, addr *models.FacilityAddress) (*models.Facility, error) {
    // Try to find existing
    existing, err := r.FindByAddress(ctx, addr.Address, addr.City, addr.State, addr.Zip)
    if err != nil {
        return nil, err
    }
    if existing != nil {
        return existing, nil
    }

    // Create new
    facility := &models.Facility{
        ID:      uuid.New().String(),
        Name:    fmt.Sprintf("%s, %s", addr.City, addr.State),
        Address: addr.Address,
        City:    addr.City,
        State:   strings.ToUpper(addr.State),
        Zip:     addr.Zip,
        Country: "USA",
    }
    if err := r.Create(ctx, facility); err != nil {
        return nil, err
    }
    return facility, nil
}
```

## Model Patterns

### Entity Struct with Tags

```go
type Load struct {
    ID           string          `db:"id" json:"id"`
    LoadNumber   string          `db:"load_number" json:"loadNumber"`
    TenderID     string          `db:"tender_id" json:"tenderId"`
    CarrierID    *string         `db:"carrier_id" json:"carrierId,omitempty"`
    LoadStatus   LoadStatus      `db:"load_status" json:"loadStatus"`
    Mode         *ModeOfTransport `db:"mode" json:"mode,omitempty"`
    CustomerRate *float64        `db:"customer_rate" json:"customerRate,omitempty"`
    CarrierRate  *float64        `db:"carrier_rate" json:"carrierRate,omitempty"`
    IsCancelled  bool            `db:"is_cancelled" json:"isCancelled"`

    // Audit fields
    CreatedAt time.Time  `db:"created_at" json:"createdAt"`
    UpdatedAt time.Time  `db:"updated_at" json:"updatedAt"`
    CreatedBy *int32     `db:"created_by" json:"createdBy,omitempty"`
    UpdatedBy *int32     `db:"updated_by" json:"updatedBy,omitempty"`
    DeletedAt *time.Time `db:"deleted_at" json:"deletedAt,omitempty"`
}
```

**Tag Conventions:**
- `db:"column_name"` - Maps to PostgreSQL column (snake_case)
- `json:"fieldName"` - Maps to JSON field (camelCase for API)
- `json:"...,omitempty"` - Omits null/zero values from response
- Required fields: `string`, `float64`, `time.Time`
- Optional fields: `*string`, `*float64`, `*time.Time`

### Enum Definition with Validation

```go
type LoadStatus string

const (
    LoadStatusUncovered     LoadStatus = "uncovered"
    LoadStatusAssigned      LoadStatus = "assigned"
    LoadStatusDispatched    LoadStatus = "dispatched"
    LoadStatusAtOrigin      LoadStatus = "at_origin"
    LoadStatusInTransit     LoadStatus = "in_transit"
    LoadStatusAtDestination LoadStatus = "at_destination"
    LoadStatusDelivered     LoadStatus = "delivered"
)

func (s LoadStatus) IsValid() bool {
    switch s {
    case LoadStatusUncovered, LoadStatusAssigned, LoadStatusDispatched,
         LoadStatusAtOrigin, LoadStatusInTransit, LoadStatusAtDestination, LoadStatusDelivered:
        return true
    }
    return false
}

type ModeOfTransport string

const (
    ModeDryVan          ModeOfTransport = "Dry Van"
    ModeRefrigeratedVan ModeOfTransport = "Refrigerated Van"
    ModeFlatbed         ModeOfTransport = "Flatbed"
)

func (m ModeOfTransport) IsTempControlled() bool {
    return m == ModeRefrigeratedVan
}
```

### Request DTO

```go
type CreateLoadRequest struct {
    TenderID     string          `json:"tender_id" validate:"required"`
    Mode         ModeOfTransport `json:"mode" validate:"required"`
    CustomerRate float64         `json:"customer_rate" validate:"required,gt=0"`
    CarrierRate  *float64        `json:"carrier_rate,omitempty" validate:"omitempty,gt=0"`
    Temperature  *float64        `json:"temperature,omitempty"`
    Stops        []CreateStopRequest `json:"stops" validate:"required,min=2"`
}
```

### Validation Function

```go
func ValidateCreateLoadRequest(req *CreateLoadRequest) ValidationErrors {
    var errors ValidationErrors

    if req.TenderID == "" {
        errors = append(errors, ValidationError{
            Field:   "tender_id",
            Message: "Tender ID is required",
        })
    }

    if !req.Mode.IsValid() {
        errors = append(errors, ValidationError{
            Field:   "mode",
            Message: "Invalid mode of transport",
        })
    }

    // Conditional validation
    if req.Mode.IsTempControlled() && req.Temperature == nil {
        errors = append(errors, ValidationError{
            Field:   "temperature",
            Message: fmt.Sprintf("Temperature is required for %s mode", req.Mode),
        })
    }

    if len(req.Stops) < 2 {
        errors = append(errors, ValidationError{
            Field:   "stops",
            Message: "At least 2 stops are required (pickup and delivery)",
        })
    }

    return errors
}
```

## Response & Error Patterns

### APIResponse Wrapper

```go
type APIResponse struct {
    Success bool                `json:"success"`
    Message string              `json:"message,omitempty"`
    Data    interface{}         `json:"data,omitempty"`
    Errors  map[string][]string `json:"errors,omitempty"`
}
```

### PaginatedResponse Generic

```go
type PaginatedResponse[T any] struct {
    Data       []T `json:"data"`
    Total      int `json:"total"`
    Page       int `json:"page"`
    PageSize   int `json:"page_size"`
    TotalPages int `json:"total_pages"`
}

func NewPaginatedResponse[T any](items []T, total, page, pageSize int) PaginatedResponse[T] {
    totalPages := 0
    if total > 0 && pageSize > 0 {
        totalPages = (total + pageSize - 1) / pageSize
    }
    return PaginatedResponse[T]{
        Data:       items,
        Total:      total,
        Page:       page,
        PageSize:   pageSize,
        TotalPages: totalPages,
    }
}
```

### ValidationErrors Type

```go
type ValidationError struct {
    Field   string `json:"field"`
    Message string `json:"message"`
}

type ValidationErrors []ValidationError

func (v ValidationErrors) Error() string {
    if len(v) == 0 {
        return ""
    }
    return fmt.Sprintf("%d validation error(s)", len(v))
}

func (v ValidationErrors) ToMap() map[string][]string {
    result := make(map[string][]string)
    for _, err := range v {
        result[err.Field] = append(result[err.Field], err.Message)
    }
    return result
}
```

## Router Setup

```go
func Setup(e *echo.Echo, loadHandler *handlers.LoadHandler, accountHandler *handlers.AccountHandler) {
    // Global middleware
    e.Use(middleware.SetupLogger())
    e.Use(middleware.SetupRecover())
    e.Use(middleware.SetupCORS())

    // Health check
    e.GET("/health", func(c echo.Context) error {
        return c.JSON(200, map[string]string{"status": "ok"})
    })

    // API v1 routes
    api := e.Group("/api/v1")

    // Loads
    loads := api.Group("/loads")
    loads.GET("", loadHandler.List)
    loads.POST("", loadHandler.Create)
    loads.GET("/:id", loadHandler.GetByID)
    loads.PUT("/:id", loadHandler.Update)
    loads.DELETE("/:id", loadHandler.Delete)

    // Accounts
    accounts := api.Group("/accounts")
    accounts.GET("", accountHandler.List)
    accounts.GET("/:id", accountHandler.GetByID)
}
```

## Checklist for New Endpoints

```
Handler:
[ ] Create handler struct with service dependency
[ ] Implement New*Handler constructor
[ ] Bind request body with c.Bind()
[ ] Use type assertion for ValidationErrors
[ ] Return APIResponse wrapper for all responses
[ ] Log errors only on 500s

Service:
[ ] Create service struct with repository dependencies
[ ] Implement New*Service constructor
[ ] Call validation function at start of create/update methods
[ ] Use context.Context throughout
[ ] Return ValidationErrors for business rule failures

Repository:
[ ] Create repository struct with database client
[ ] Use parameterized queries ($1, $2)
[ ] Check pgx.ErrNoRows for "not found"
[ ] Include deleted_at IS NULL in queries
[ ] Use transactions for multi-table operations

Models:
[ ] Add db and json tags to all fields
[ ] Use pointers for nullable fields
[ ] Include audit fields (CreatedAt, UpdatedAt, etc.)
[ ] Create request/response DTOs separate from entity

Router:
[ ] Register routes in Setup function
[ ] Use route groups for resource prefixes
[ ] Follow RESTful conventions (GET/POST/PUT/DELETE)
```

## Code References

- **Handlers**: `/internal/handlers/load.go`, `/internal/handlers/account.go`
- **Services**: `/internal/services/load.go`
- **Repositories**: `/internal/repository/load.go`, `/internal/repository/query_builder.go`
- **Models**: `/internal/models/load.go`, `/internal/models/validation.go`, `/internal/models/responses.go`
- **Router**: `/internal/router/router.go`
