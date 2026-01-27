# Backend Integration Patterns for SvelteKit SPA with Golang/Echo

## Golang Echo CORS Configuration

### Basic CORS Setup

```go
package main

import (
	"net/http"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()
	
	// CORS configuration for development
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: []string{
			"http://localhost:5173",  // Vite dev server
			"http://localhost:4173",  // Vite preview server
		},
		AllowMethods: []string{
			http.MethodGet,
			http.MethodPost,
			http.MethodPut,
			http.MethodPatch,
			http.MethodDelete,
			http.MethodOptions,
		},
		AllowHeaders: []string{
			"Authorization",
			"Content-Type",
			"X-Requested-With",
		},
		AllowCredentials: true,
		MaxAge: 3600,
	}))
	
	e.Logger.Fatal(e.Start(":8080"))
}
```

### Production CORS with Environment Variables

```go
import (
	"os"
	"strings"
)

func getCORSOrigins() []string {
	origins := os.Getenv("CORS_ORIGINS")
	if origins == "" {
		return []string{"http://localhost:5173"}
	}
	return strings.Split(origins, ",")
}

func main() {
	e := echo.New()
	
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins:     getCORSOrigins(),
		AllowMethods:     []string{"GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"},
		AllowHeaders:     []string{"Authorization", "Content-Type"},
		AllowCredentials: true,
	}))
}
```

## Authentication Patterns

### JWT Token Authentication

```go
// Golang Echo Backend
import (
	"github.com/golang-jwt/jwt/v5"
	"time"
)

type JWTClaims struct {
	UserID string `json:"user_id"`
	Email  string `json:"email"`
	jwt.RegisteredClaims
}

func generateToken(userID, email string) (string, error) {
	claims := &JWTClaims{
		UserID: userID,
		Email:  email,
		RegisteredClaims: jwt.RegisteredClaims{
			ExpiresAt: jwt.NewNumericDate(time.Now().Add(24 * time.Hour)),
			IssuedAt:  jwt.NewNumericDate(time.Now()),
		},
	}
	
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString([]byte(os.Getenv("JWT_SECRET")))
}

// Login endpoint
func login(c echo.Context) error {
	var req LoginRequest
	if err := c.Bind(&req); err != nil {
		return c.JSON(http.StatusBadRequest, map[string]string{"error": "Invalid request"})
	}
	
	// Validate credentials (implement your logic)
	user, err := validateCredentials(req.Email, req.Password)
	if err != nil {
		return c.JSON(http.StatusUnauthorized, map[string]string{"error": "Invalid credentials"})
	}
	
	token, err := generateToken(user.ID, user.Email)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "Token generation failed"})
	}
	
	return c.JSON(http.StatusOK, map[string]interface{}{
		"token": token,
		"user":  user,
	})
}
```

```js
// SvelteKit Frontend (src/lib/auth.js)
export async function login(email, password) {
	const response = await fetch('http://localhost:8080/api/auth/login', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ email, password })
	});
	
	if (!response.ok) {
		const error = await response.json();
		throw new Error(error.error || 'Login failed');
	}
	
	const data = await response.json();
	localStorage.setItem('auth_token', data.token);
	localStorage.setItem('user', JSON.stringify(data.user));
	
	return data;
}

export function logout() {
	localStorage.removeItem('auth_token');
	localStorage.removeItem('user');
}

export function getToken() {
	return localStorage.getItem('auth_token');
}

export function getUser() {
	const userStr = localStorage.getItem('user');
	return userStr ? JSON.parse(userStr) : null;
}
```

### Protected Route Middleware

```go
// Golang Echo Backend
func authMiddleware(next echo.HandlerFunc) echo.HandlerFunc {
	return func(c echo.Context) error {
		authHeader := c.Request().Header.Get("Authorization")
		if authHeader == "" {
			return c.JSON(http.StatusUnauthorized, map[string]string{"error": "Missing authorization header"})
		}
		
		tokenString := strings.TrimPrefix(authHeader, "Bearer ")
		
		token, err := jwt.ParseWithClaims(tokenString, &JWTClaims{}, func(token *jwt.Token) (interface{}, error) {
			return []byte(os.Getenv("JWT_SECRET")), nil
		})
		
		if err != nil || !token.Valid {
			return c.JSON(http.StatusUnauthorized, map[string]string{"error": "Invalid token"})
		}
		
		claims, ok := token.Claims.(*JWTClaims)
		if !ok {
			return c.JSON(http.StatusUnauthorized, map[string]string{"error": "Invalid token claims"})
		}
		
		// Store user info in context
		c.Set("user_id", claims.UserID)
		c.Set("user_email", claims.Email)
		
		return next(c)
	}
}

// Apply to protected routes
func setupRoutes(e *echo.Echo) {
	api := e.Group("/api")
	
	// Public routes
	api.POST("/auth/login", login)
	api.POST("/auth/register", register)
	
	// Protected routes
	protected := api.Group("")
	protected.Use(authMiddleware)
	protected.GET("/dashboard", getDashboard)
	protected.GET("/profile", getProfile)
	protected.PUT("/profile", updateProfile)
}
```

```js
// SvelteKit Frontend (src/routes/+layout.js)
import { getToken, getUser } from '$lib/auth';

export const ssr = false;

export async function load({ fetch }) {
	const token = getToken();
	
	if (!token) {
		return { user: null };
	}
		// Validate token with backend
	try {
		const response = await fetch('http://localhost:8080/api/auth/me', {
			headers: { 'Authorization': `Bearer ${token}` }
		});
		
		if (!response.ok) {
			throw new Error('Token invalid');
		}
		
		const user = await response.json();
		return { user, token };
	} catch (error) {
		// Token invalid, clear storage
		localStorage.removeItem('auth_token');
		localStorage.removeItem('user');
		return { user: null };
	}
}
```

## API Request Utilities

### Centralized API Client

```js
// src/lib/api.js
const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8080';

class APIError extends Error {
	constructor(status, message, details) {
		super(message);
		this.status = status;
		this.details = details;
	}
}

export async function apiRequest(endpoint, options = {}) {
	const token = localStorage.getItem('auth_token');
	
	const config = {
		...options,
		headers: {
			'Content-Type': 'application/json',
			...(token && { 'Authorization': `Bearer ${token}` }),
			...options.headers,
		},
	};
	
	if (options.body && typeof options.body === 'object') {
		config.body = JSON.stringify(options.body);
	}
	
	const response = await fetch(`${API_BASE}${endpoint}`, config);
	
	if (!response.ok) {
		let errorData;
		try {
			errorData = await response.json();
		} catch {
			errorData = { message: 'Request failed' };
		}
		
		throw new APIError(
			response.status,
			errorData.error || errorData.message || 'Request failed',
			errorData
		);
	}
	
	// Handle empty responses
	const contentType = response.headers.get('content-type');
	if (contentType && contentType.includes('application/json')) {
		return response.json();
	}
	
	return response.text();
}

// Convenience methods
export const api = {
	get: (endpoint) => apiRequest(endpoint),
	post: (endpoint, data) => apiRequest(endpoint, { method: 'POST', body: data }),
	put: (endpoint, data) => apiRequest(endpoint, { method: 'PUT', body: data }),
	patch: (endpoint, data) => apiRequest(endpoint, { method: 'PATCH', body: data }),
	delete: (endpoint) => apiRequest(endpoint, { method: 'DELETE' }),
};
```

### Usage in Components

```svelte
<script>
	import { api } from '$lib/api';
	import { onMount } from 'svelte';
	
	let items = $state([]);
	let loading = $state(true);
	let error = $state(null);
	
	onMount(async () => {
		try {
			items = await api.get('/api/items');
		} catch (e) {
			error = e.message;
		} finally {
			loading = false;
		}
	});
	
	async function deleteItem(id) {
		try {
			await api.delete(`/api/items/${id}`);
			items = items.filter(item => item.id !== id);
		} catch (e) {
			alert('Delete failed: ' + e.message);
		}
	}
</script>

{#if loading}
	<p>Loading...</p>
{:else if error}
	<p class="error">{error}</p>
{:else}
	{#each items as item}
		<div>
			{item.name}
			<button onclick={() => deleteItem(item.id)}>Delete</button>
		</div>
	{/each}
{/if}
```

## File Upload Patterns

### Backend File Upload Handler

```go
// Golang Echo Backend
func uploadFile(c echo.Context) error {
	// Get user from auth middleware
	userID := c.Get("user_id").(string)
	
	// Read file from form
	file, err := c.FormFile("file")
	if err != nil {
		return c.JSON(http.StatusBadRequest, map[string]string{"error": "File is required"})
	}
	
	// Validate file size (10MB limit)
	if file.Size > 10*1024*1024 {
		return c.JSON(http.StatusBadRequest, map[string]string{"error": "File too large (max 10MB)"})
	}
	
	// Open file
	src, err := file.Open()
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "Failed to open file"})
	}
	defer src.Close()
	
	// Save file (implement your storage logic)
	fileURL, err := saveFile(userID, file.Filename, src)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "Failed to save file"})
	}
	
	return c.JSON(http.StatusOK, map[string]interface{}{
		"url":      fileURL,
		"filename": file.Filename,
		"size":     file.Size,
	})
}
```

### Frontend File Upload

```svelte
<script>
	import { getToken } from '$lib/auth';
	
	let file = $state(null);
	let uploading = $state(false);
	let progress = $state(0);
	let uploadedURL = $state(null);
	
	async function handleUpload() {
		if (!file) return;
		
		uploading = true;
		progress = 0;
		
		const formData = new FormData();
		formData.append('file', file);
		
		try {
			const xhr = new XMLHttpRequest();
			
			// Track upload progress
			xhr.upload.addEventListener('progress', (e) => {
				if (e.lengthComputable) {
					progress = Math.round((e.loaded / e.total) * 100);
				}
			});
			
			// Handle completion
			xhr.addEventListener('load', () => {
				if (xhr.status === 200) {
					const response = JSON.parse(xhr.responseText);
					uploadedURL = response.url;
				} else {
					alert('Upload failed');
				}
				uploading = false;
			});
			
			xhr.open('POST', 'http://localhost:8080/api/upload');
			xhr.setRequestHeader('Authorization', `Bearer ${getToken()}`);
			xhr.send(formData);
		} catch (error) {
			console.error('Upload error:', error);
			uploading = false;
		}
	}
</script>

<input
	type="file"
	onchange={(e) => file = e.target.files[0]}
	disabled={uploading}
/>

<button onclick={handleUpload} disabled={!file || uploading}>
	{uploading ? `Uploading... ${progress}%` : 'Upload'}
</button>

{#if uploadedURL}
	<p>File uploaded: <a href={uploadedURL}>{uploadedURL}</a></p>
{/if}
```

## WebSocket Integration

### Backend WebSocket Handler

```go
import (
	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		// In production, validate origin properly
		return true
	},
}

func websocketHandler(c echo.Context) error {
	ws, err := upgrader.Upgrade(c.Response(), c.Request(), nil)
	if err != nil {
		return err
	}
	defer ws.Close()
	
	// Handle WebSocket messages
	for {
		var msg Message
		err := ws.ReadJSON(&msg)
		if err != nil {
			break
		}
		
		// Process message and send response
		response := processMessage(msg)
		if err := ws.WriteJSON(response); err != nil {
			break
		}
	}
	
	return nil
}
```

### Frontend WebSocket Client

```svelte
<script>
	import { onMount, onDestroy } from 'svelte';
	import { getToken } from '$lib/auth';
	
	let messages = $state([]);
	let connected = $state(false);
	let ws = null;
	
	onMount(() => {
		const token = getToken();
		ws = new WebSocket(`ws://localhost:8080/ws?token=${token}`);
		
		ws.onopen = () => {
			connected = true;
		};
		
		ws.onmessage = (event) => {
			const data = JSON.parse(event.data);
			messages = [...messages, data];
		};
		
		ws.onclose = () => {
			connected = false;
		};
		
		ws.onerror = (error) => {
			console.error('WebSocket error:', error);
		};
	});
	
	onDestroy(() => {
		if (ws) ws.close();
	});
	
	function sendMessage(text) {
		if (ws && connected) {
			ws.send(JSON.stringify({ text }));
		}
	}
</script>

<div class="connection-status">
	Status: {connected ? 'Connected' : 'Disconnected'}
</div>

<div class="messages">
	{#each messages as msg}
		<div>{msg.text}</div>
	{/each}
</div>
```

## Environment-Specific Configuration

### Backend Configuration

```go
// config/config.go
type Config struct {
	Port        string
	DatabaseURL string
	JWTSecret   string
	CORSOrigins []string
	Environment string
}

func LoadConfig() *Config {
	return &Config{
		Port:        getEnv("PORT", "8080"),
		DatabaseURL: getEnv("DATABASE_URL", ""),
		JWTSecret:   getEnv("JWT_SECRET", ""),
		CORSOrigins: strings.Split(getEnv("CORS_ORIGINS", "http://localhost:5173"), ","),
		Environment: getEnv("ENVIRONMENT", "development"),
	}
}

func getEnv(key, defaultValue string) string {
	if value := os.Getenv(key); value != "" {
		return value
	}
	return defaultValue
}
```

### Frontend Configuration

```js
// .env.development
VITE_API_URL=http://localhost:8080
VITE_WS_URL=ws://localhost:8080

// .env.production
VITE_API_URL=https://api.yourdomain.com
VITE_WS_URL=wss://api.yourdomain.com
```

```js
// src/lib/config.js
export const config = {
	apiUrl: import.meta.env.VITE_API_URL,
	wsUrl: import.meta.env.VITE_WS_URL,
	environment: import.meta.env.MODE,
	isDevelopment: import.meta.env.DEV,
	isProduction: import.meta.env.PROD,
};
```

