# Go Echo Framework Best Practices Reference

## Project Structure

```
cmd/
└── server/
    └── main.go          # Entry point
internal/
├── config/              # Configuration
├── database/            # Database connection
├── handlers/            # HTTP handlers
├── middleware/          # Custom middleware
├── models/              # Domain models
├── repository/          # Data access layer
├── router/              # Route definitions
├── services/            # Business logic
└── validators/          # Input validation
```

## Handler Patterns

### Standard Handler Structure

```go
type UserHandler struct {
    userService services.UserService
}

func NewUserHandler(us services.UserService) *UserHandler {
    return &UserHandler{userService: us}
}

func (h *UserHandler) GetUser(c echo.Context) error {
    id := c.Param("id")

    user, err := h.userService.GetByID(c.Request().Context(), id)
    if err != nil {
        if errors.Is(err, services.ErrNotFound) {
            return c.JSON(http.StatusNotFound, map[string]string{
                "error": "user not found",
            })
        }
        return c.JSON(http.StatusInternalServerError, map[string]string{
            "error": "internal server error",
        })
    }

    return c.JSON(http.StatusOK, user)
}
```

### Request Binding and Validation

```go
type CreateUserRequest struct {
    Name  string `json:"name" validate:"required,min=2,max=100"`
    Email string `json:"email" validate:"required,email"`
}

func (h *UserHandler) CreateUser(c echo.Context) error {
    var req CreateUserRequest
    if err := c.Bind(&req); err != nil {
        return c.JSON(http.StatusBadRequest, map[string]string{
            "error": "invalid request body",
        })
    }

    if err := c.Validate(&req); err != nil {
        return c.JSON(http.StatusBadRequest, map[string]string{
            "error": err.Error(),
        })
    }

    user, err := h.userService.Create(c.Request().Context(), req)
    if err != nil {
        return handleServiceError(c, err)
    }

    return c.JSON(http.StatusCreated, user)
}
```

## Service Layer Patterns

### Service Interface

```go
type UserService interface {
    GetByID(ctx context.Context, id string) (*models.User, error)
    Create(ctx context.Context, req CreateUserRequest) (*models.User, error)
    Update(ctx context.Context, id string, req UpdateUserRequest) (*models.User, error)
    Delete(ctx context.Context, id string) error
}

type userService struct {
    repo repository.UserRepository
}

func NewUserService(repo repository.UserRepository) UserService {
    return &userService{repo: repo}
}
```

### Error Handling in Services

```go
var (
    ErrNotFound     = errors.New("resource not found")
    ErrUnauthorized = errors.New("unauthorized")
    ErrConflict     = errors.New("resource conflict")
)

func (s *userService) GetByID(ctx context.Context, id string) (*models.User, error) {
    user, err := s.repo.FindByID(ctx, id)
    if err != nil {
        if errors.Is(err, sql.ErrNoRows) {
            return nil, ErrNotFound
        }
        return nil, fmt.Errorf("failed to get user: %w", err)
    }
    return user, nil
}
```

## Repository Patterns

### Repository Interface

```go
type UserRepository interface {
    FindByID(ctx context.Context, id string) (*models.User, error)
    FindByEmail(ctx context.Context, email string) (*models.User, error)
    Create(ctx context.Context, user *models.User) error
    Update(ctx context.Context, user *models.User) error
    Delete(ctx context.Context, id string) error
}
```

### Database Queries

```go
func (r *userRepository) FindByID(ctx context.Context, id string) (*models.User, error) {
    var user models.User
    query := `
        SELECT id, name, email, created_at, updated_at
        FROM users
        WHERE id = $1
    `
    err := r.db.QueryRowContext(ctx, query, id).Scan(
        &user.ID,
        &user.Name,
        &user.Email,
        &user.CreatedAt,
        &user.UpdatedAt,
    )
    if err != nil {
        return nil, err
    }
    return &user, nil
}
```

## Middleware Patterns

### Custom Middleware

```go
func AuthMiddleware(next echo.HandlerFunc) echo.HandlerFunc {
    return func(c echo.Context) error {
        token := c.Request().Header.Get("Authorization")
        if token == "" {
            return c.JSON(http.StatusUnauthorized, map[string]string{
                "error": "missing authorization header",
            })
        }

        // Validate token and set user context
        user, err := validateToken(token)
        if err != nil {
            return c.JSON(http.StatusUnauthorized, map[string]string{
                "error": "invalid token",
            })
        }

        c.Set("user", user)
        return next(c)
    }
}
```

## Router Setup

```go
func SetupRoutes(e *echo.Echo, h *Handlers) {
    // Public routes
    e.POST("/auth/login", h.Auth.Login)
    e.POST("/auth/register", h.Auth.Register)

    // Protected routes
    api := e.Group("/api", middleware.AuthMiddleware)

    // Users
    users := api.Group("/users")
    users.GET("", h.User.List)
    users.GET("/:id", h.User.GetByID)
    users.POST("", h.User.Create)
    users.PUT("/:id", h.User.Update)
    users.DELETE("/:id", h.User.Delete)
}
```

## Testing Patterns

```go
func TestUserHandler_GetUser(t *testing.T) {
    // Setup
    e := echo.New()
    mockService := &mocks.UserService{}
    handler := NewUserHandler(mockService)

    // Test case
    mockService.On("GetByID", mock.Anything, "123").Return(&models.User{
        ID:   "123",
        Name: "Test User",
    }, nil)

    req := httptest.NewRequest(http.MethodGet, "/users/123", nil)
    rec := httptest.NewRecorder()
    c := e.NewContext(req, rec)
    c.SetParamNames("id")
    c.SetParamValues("123")

    // Execute
    err := handler.GetUser(c)

    // Assert
    assert.NoError(t, err)
    assert.Equal(t, http.StatusOK, rec.Code)
}
```

## Common Conventions

1. **Context propagation** - Always pass `context.Context` through the call stack
2. **Error wrapping** - Use `fmt.Errorf("description: %w", err)` for error context
3. **Interface-based design** - Define interfaces in the consuming package
4. **Constructor functions** - Use `NewXxx()` pattern for struct initialization
5. **Pointer receivers** - Use pointer receivers for methods that modify state
