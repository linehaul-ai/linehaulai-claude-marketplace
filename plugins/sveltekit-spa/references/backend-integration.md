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

```ts
// SvelteKit Frontend (src/lib/auth.ts)
interface User {
	id: string;
	email: string;
	name?: string;
}

interface LoginResponse {
	token: string;
	user: User;
}

export async function login(email: string, password: string): Promise<LoginResponse> {
	const response = await fetch('http://localhost:8080/api/auth/login', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ email, password })
	});

	if (!response.ok) {
		const errorData = await response.json();
		throw new Error(errorData.error || 'Login failed');
	}

	const data: LoginResponse = await response.json();
	localStorage.setItem('auth_token', data.token);
	localStorage.setItem('user', JSON.stringify(data.user));

	return data;
}

export function logout(): void {
	localStorage.removeItem('auth_token');
	localStorage.removeItem('user');
}

export function getToken(): string | null {
	return localStorage.getItem('auth_token');
}

export function getUser(): User | null {
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

```ts
// SvelteKit Frontend (src/routes/+layout.ts)
import { getToken } from '$lib/auth';
import type { LayoutLoad } from './$types';

export const ssr = false;
export const prerender = false;

interface User {
	id: string;
	email: string;
	name?: string;
}

export const load: LayoutLoad = async ({ fetch }) => {
	const token = getToken();

	if (!token) {
		return { user: null, token: null };
	}

	// Validate token with backend
	try {
		const response = await fetch('http://localhost:8080/api/auth/me', {
			headers: { 'Authorization': `Bearer ${token}` }
		});

		if (!response.ok) {
			throw new Error('Token invalid');
		}

		const user: User = await response.json();
		return { user, token };
	} catch {
		// Token invalid, clear storage
		localStorage.removeItem('auth_token');
		localStorage.removeItem('user');
		return { user: null, token: null };
	}
};
```

## API Request Utilities

### Centralized API Client

```ts
// src/lib/api.ts
const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8080';

export class APIError extends Error {
	constructor(
		public status: number,
		message: string,
		public details?: unknown
	) {
		super(message);
		this.name = 'APIError';
	}
}

export async function apiRequest<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
	const token = localStorage.getItem('auth_token');

	const config: RequestInit = {
		...options,
		headers: {
			'Content-Type': 'application/json',
			...(token && { 'Authorization': `Bearer ${token}` }),
			...options.headers
		}
	};

	if (options.body && typeof options.body === 'object' && !(options.body instanceof FormData)) {
		config.body = JSON.stringify(options.body);
	}

	const response = await fetch(`${API_BASE}${endpoint}`, config);

	if (!response.ok) {
		let errorData: { error?: string; message?: string };
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
		return response.json() as Promise<T>;
	}

	return response.text() as unknown as T;
}

// Convenience methods with type inference
export const api = {
	get: <T>(endpoint: string) => apiRequest<T>(endpoint),
	post: <T>(endpoint: string, data: unknown) => apiRequest<T>(endpoint, { method: 'POST', body: data as BodyInit }),
	put: <T>(endpoint: string, data: unknown) => apiRequest<T>(endpoint, { method: 'PUT', body: data as BodyInit }),
	patch: <T>(endpoint: string, data: unknown) => apiRequest<T>(endpoint, { method: 'PATCH', body: data as BodyInit }),
	delete: <T>(endpoint: string) => apiRequest<T>(endpoint, { method: 'DELETE' })
};
```

### Usage in Components

```svelte
<script lang="ts">
	import { api } from '$lib/api';
	import { onMount } from 'svelte';

	interface Item {
		id: string;
		name: string;
	}

	let items = $state<Item[]>([]);
	let loading = $state(true);
	let error = $state<string | null>(null);

	onMount(async () => {
		try {
			items = await api.get<Item[]>('/api/items');
		} catch (e) {
			error = e instanceof Error ? e.message : 'Failed to load items';
		} finally {
			loading = false;
		}
	});

	async function deleteItem(id: string) {
		try {
			await api.delete(`/api/items/${id}`);
			items = items.filter((item) => item.id !== id);
		} catch (e) {
			alert('Delete failed: ' + (e instanceof Error ? e.message : 'Unknown error'));
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
<script lang="ts">
	import { getToken } from '$lib/auth';

	let file = $state<File | null>(null);
	let uploading = $state(false);
	let progress = $state(0);
	let uploadedURL = $state<string | null>(null);

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
					const response = JSON.parse(xhr.responseText) as { url: string };
					uploadedURL = response.url;
				} else {
					alert('Upload failed');
				}
				uploading = false;
			});

			xhr.open('POST', 'http://localhost:8080/api/upload');
			xhr.setRequestHeader('Authorization', `Bearer ${getToken()}`);
			xhr.send(formData);
		} catch (err) {
			console.error('Upload error:', err);
			uploading = false;
		}
	}

	function handleFileChange(e: Event) {
		const target = e.target as HTMLInputElement;
		file = target.files?.[0] ?? null;
	}
</script>

<input type="file" onchange={handleFileChange} disabled={uploading} />

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
<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { getToken } from '$lib/auth';

	interface Message {
		text: string;
	}

	let messages = $state<Message[]>([]);
	let connected = $state(false);
	let ws: WebSocket | null = null;

	onMount(() => {
		const token = getToken();
		ws = new WebSocket(`ws://localhost:8080/ws?token=${token}`);

		ws.onopen = () => {
			connected = true;
		};

		ws.onmessage = (event: MessageEvent) => {
			const data = JSON.parse(event.data) as Message;
			messages = [...messages, data];
		};

		ws.onclose = () => {
			connected = false;
		};

		ws.onerror = (err) => {
			console.error('WebSocket error:', err);
		};
	});

	onDestroy(() => {
		if (ws) ws.close();
	});

	function sendMessage(text: string) {
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

```bash
# .env.development
VITE_API_URL=http://localhost:8080
VITE_WS_URL=ws://localhost:8080

# .env.production
VITE_API_URL=https://api.yourdomain.com
VITE_WS_URL=wss://api.yourdomain.com
```

```ts
// src/lib/config.ts
interface AppConfig {
	apiUrl: string;
	wsUrl: string;
	environment: string;
	isDevelopment: boolean;
	isProduction: boolean;
}

export const config: AppConfig = {
	apiUrl: import.meta.env.VITE_API_URL,
	wsUrl: import.meta.env.VITE_WS_URL,
	environment: import.meta.env.MODE,
	isDevelopment: import.meta.env.DEV,
	isProduction: import.meta.env.PROD
};
```

