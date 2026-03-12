---
name: sveltekit-spa
description: Comprehensive guide for building SvelteKit applications in SPA (Single Page Application) mode with client-side rendering only. Use when working on SvelteKit projects that use adapter-static with CSR, especially those with separate backends like Golang/Echo. Covers routing, page options, data loading, and proper SPA configuration while avoiding SSR features.
---

# SvelteKit SPA Mode

Guide for building SvelteKit applications in pure SPA/CSR mode with `adapter-static`, specifically optimized for projects with separate backends (e.g., Golang + Echo).

## About This Skill

**Type:** Reference guide (flexible pattern)

This skill provides patterns and conventions for SvelteKit SPA development. The core requirements (SSR disabled, adapter-static configuration) are mandatory for SPA mode, but implementation details should be adapted to your project's needs.

> 💡 **Additional Resources:** This skill includes detailed reference documentation:
> - `references/routing-patterns.md` - Complex routing scenarios, nested layouts, route guards
> - `references/backend-integration.md` - Detailed API patterns, authentication flows, error handling

## Core Concept

SvelteKit SPA mode creates a fully client-rendered single-page application. The entire app runs in the browser with a fallback HTML page that bootstraps the application for any route.

**Key characteristics:**
- No server-side rendering (SSR disabled)
- All routing handled client-side
- Backend is separate (API-only)
- Uses `adapter-static` with fallback page
- Full SvelteKit routing capabilities without SSR complexity

## Initial SPA Setup Checklist

When setting up a new SvelteKit project in SPA mode:

- [ ] Install `@sveltejs/adapter-static`
- [ ] Configure adapter in `svelte.config.js` with fallback page
- [ ] Create `src/routes/+layout.ts` with `export const ssr = false` and `export const prerender = false`
- [ ] Set up environment variables for API URL (`.env` file)
- [ ] Configure CORS on backend API
- [ ] Test build process with `bun run build`
- [ ] Test locally with `bun run preview`
- [ ] Verify routing works after page refresh

## Migrating Existing SvelteKit Project to SPA Mode

If converting an existing SvelteKit project:

- [ ] Install `@sveltejs/adapter-static` (remove other adapters)
- [ ] Update `svelte.config.js` adapter configuration
- [ ] Add `ssr = false` and `prerender = false` to root `+layout.ts`
- [ ] Convert all `+page.server.js` files to `+page.ts`
- [ ] Remove all `+server.js` API routes (move to backend)
- [ ] Update load functions to use absolute API URLs with environment variables
- [ ] Test all routes still work client-side
- [ ] Update deployment configuration for static hosting

## Project Configuration

### Adapter Setup

```js
// svelte.config.js
import adapter from '@sveltejs/adapter-static';

export default {
	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: '200.html', // or '404.html', 'index.html' depending on host
			precompress: false,
			strict: false // Set false since we're not prerendering
		})
	}
};
```

**Fallback page selection:**
- `200.html` - For hosts like Surge that support catch-all routes
- `404.html` - For hosts that serve 404.html for missing routes (GitHub Pages)
- `index.html` - Avoid unless necessary (can conflict with prerendered pages)

### Disable SSR Globally

```ts
// src/routes/+layout.ts
export const ssr = false;
export const prerender = false;
```

**Critical**: Both exports are required for SPA mode:
- `ssr = false` - Disables server-side rendering (all rendering happens client-side)
- `prerender = false` - Disables prerendering at build time (unless selectively enabled per route)

This configuration ensures the entire application runs as a pure SPA with client-side rendering only.

## Routing in SPA Mode

SvelteKit's filesystem-based routing works identically in SPA mode. The only difference is that all routes render client-side.

### Basic Route Structure

```
laneweaver-frontend/
├── bun.lock
├── components.json
├── e2e/                    # Playwright end-to-end tests
│   └── demo.test.ts
├── eslint.config.js
├── package.json
├── playwright.config.ts
├── src/
│   ├── app.css             # Global styles
│   ├── app.d.ts            # TypeScript declarations
│   ├── app.html            # HTML template
│   ├── lib/
│   │   ├── assets/
│   │   │   └── favicon.svg
│   │   ├── components/
│   │   │   └── ui/         # Reusable UI components
│   │   ├── index.ts        # Library exports
│   │   └── utils.ts        # Utility functions
│   └── routes/
│       ├── +layout.svelte  # Root layout (nav, etc.)
│       ├── +layout.ts      # SSR disable, shared data
│       ├── +page.svelte    # Home page
│       ├── dashboard/
│       │   ├── +page.svelte        # /dashboard
│       │   ├── +layout.svelte      # Dashboard layout
│       │   └── [id]/
│       │       └── +page.svelte    # /dashboard/:id
│       └── api/
│           └── +server.ts  # ❌ AVOID - Use backend API instead
├── static/                 # Static assets (served as-is)
├── svelte.config.js
├── tsconfig.json
└── vite.config.ts
```

### Route Files

**+page.svelte** - Page component
```svelte
<script lang="ts">
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
</script>

<h1>{data.title}</h1>
```

**+page.ts** - Client-side data loading
```ts
import type { PageLoad } from './$types';

export const ssr = false; // Optional if set in root layout
export const prerender = false; // Optional if set in root layout

export const load: PageLoad = async ({ fetch, params }) => {
	// Fetch from your backend API
	const API_URL = import.meta.env.VITE_API_URL;
	const res = await fetch(`${API_URL}/api/items/${params.id}`);
	return await res.json();
};
```

**+layout.svelte** - Shared layout
```svelte
<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		children: Snippet;
	}

	let { children }: Props = $props();
</script>

<nav>
	<a href="/">Home</a>
	<a href="/dashboard">Dashboard</a>
</nav>

{@render children()}
```

### Dynamic Routes

```
src/routes/
└── blog/
    └── [slug]/
        ├── +page.svelte    # /blog/hello-world
        └── +page.ts        # Load data for slug
```

```ts
// src/routes/blog/[slug]/+page.ts
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const ssr = false;
export const prerender = false;

export const load: PageLoad = async ({ params, fetch }) => {
	const API_URL = import.meta.env.VITE_API_URL;
	const response = await fetch(`${API_URL}/api/blog/${params.slug}`);
	if (!response.ok) {
		throw error(404, 'Post not found');
	}
	return await response.json();
};
```

## Security Considerations

### Authentication Token Storage

⚠️ **IMPORTANT:** Many examples in this guide use `localStorage` for simplicity in demonstrating concepts, but this has significant security implications:

**Risks:**
- Vulnerable to XSS (Cross-Site Scripting) attacks
- Accessible to all JavaScript code on the page, including third-party scripts
- Not automatically cleared on browser close
- No built-in protection against CSRF attacks

**Recommended alternatives for production:**

1. **HttpOnly Cookies** (preferred)
   - Set by backend server
   - Not accessible to JavaScript (immune to XSS token theft)
   - Automatically sent with requests to same domain
   - Can be marked as Secure and SameSite

2. **sessionStorage** (slightly better than localStorage)
   - Cleared when tab/window closes
   - Still vulnerable to XSS
   - Better for temporary sessions

3. **In-memory storage with session timeout**
   - Store in component state or stores
   - Cleared on page refresh
   - Most secure for highly sensitive apps

**Best practice:** Use HttpOnly cookies with your backend API for authentication tokens. Reserve `localStorage` only for non-sensitive application state.

### CORS Configuration

Ensure your backend properly configures CORS to only allow your frontend origin:

```go
// Example: Golang + Echo
e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
    AllowOrigins: []string{"https://yourdomain.com"}, // Never use "*" in production
    AllowMethods: []string{http.MethodGet, http.MethodPost, http.MethodPut, http.MethodDelete},
    AllowHeaders: []string{"Authorization", "Content-Type"},
    AllowCredentials: true, // Required for cookies
}))
```

## Data Loading Patterns

### Client-Side Load Function

Load functions in `+page.ts` run in the browser for SPA mode:

```ts
// src/routes/dashboard/+page.ts
import type { PageLoad } from './$types';

export const ssr = false;
export const prerender = false;

interface DashboardData {
	// Define the shape of your dashboard data
	[key: string]: unknown;
}

export const load: PageLoad = async ({ fetch, parent, url }) => {
	// Access parent layout data
	const parentData = await parent();

	// Fetch from backend API
	const API_URL = import.meta.env.VITE_API_URL;
	const response = await fetch(`${API_URL}/api/dashboard`, {
		headers: {
			'Authorization': `Bearer ${parentData.token}`
		}
	});

	// Access URL search params
	const filter = url.searchParams.get('filter');

	const dashboardData: DashboardData = await response.json();

	return {
		dashboardData,
		filter
	};
};
```

### Authentication Token Flow

```ts
// src/routes/+layout.ts
import type { LayoutLoad } from './$types';

export const ssr = false;
export const prerender = false;

interface User {
	id: string;
	email: string;
	name?: string;
}

export const load: LayoutLoad = async ({ fetch }) => {
	// Get token from localStorage or cookie
	// NOTE: See Security Considerations section for production-ready alternatives
	const token = localStorage.getItem('auth_token');

	if (!token) {
		return { user: null, token: null };
	}

	// Validate token with backend
	const API_URL = import.meta.env.VITE_API_URL;
	const response = await fetch(`${API_URL}/api/auth/me`, {
		headers: { 'Authorization': `Bearer ${token}` }
	});

	if (!response.ok) {
		localStorage.removeItem('auth_token');
		return { user: null, token: null };
	}

	const user: User = await response.json();

	return {
		user,
		token
	};
};
```

### Error Handling

```ts
import { error, redirect } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const ssr = false;
export const prerender = false;

export const load: PageLoad = async ({ fetch, parent }) => {
	const { token } = await parent();

	if (!token) {
		throw redirect(303, '/login');
	}

	const API_URL = import.meta.env.VITE_API_URL;
	const response = await fetch(`${API_URL}/api/protected-resource`);

	if (response.status === 401) {
		throw redirect(303, '/login');
	}

	if (response.status === 404) {
		throw error(404, 'Resource not found');
	}

	if (!response.ok) {
		throw error(response.status, 'Failed to load resource');
	}

	return await response.json();
};
```

## Backend Integration (Golang + Echo)

### API Communication

```ts
// src/lib/api.ts
const API_BASE = import.meta.env.VITE_API_URL;

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
	// NOTE: See Security Considerations section for production-ready alternatives
	const token = localStorage.getItem('auth_token');

	const response = await fetch(`${API_BASE}${endpoint}`, {
		...options,
		headers: {
			'Content-Type': 'application/json',
			...(token && { 'Authorization': `Bearer ${token}` }),
			...options.headers
		}
	});

	if (!response.ok) {
		const errorData = await response.json().catch(() => ({}));
		throw new APIError(response.status, errorData.message || 'API request failed', errorData);
	}

	return response.json() as Promise<T>;
}
```

### Form Submission

```svelte
<script lang="ts">
	import { apiRequest } from '$lib/api';
	import { goto } from '$app/navigation';

	interface LoginResponse {
		token: string;
	}

	let formData = $state({ email: '', password: '' });
	let error = $state<string | null>(null);

	async function handleSubmit() {
		try {
			const result = await apiRequest<LoginResponse>('/api/auth/login', {
				method: 'POST',
				body: JSON.stringify(formData)
			});

			// NOTE: See Security Considerations section for production-ready alternatives
			localStorage.setItem('auth_token', result.token);
			goto('/dashboard');
		} catch (e) {
			error = e instanceof Error ? e.message : 'Login failed';
		}
	}
</script>

<form onsubmit={(e) => { e.preventDefault(); handleSubmit(); }}>
	<input type="email" bind:value={formData.email} />
	<input type="password" bind:value={formData.password} />
	{#if error}
		<p class="error">{error}</p>
	{/if}
	<button type="submit">Login</button>
</form>
```

## Page Options Reference

### Available Options

```ts
// +page.ts or +layout.ts
export const ssr = false;        // Disable server-side rendering
export const prerender = false;  // Don't prerender this page
export const csr = true;         // Enable client-side rendering (default)
```

**Important for SPA mode:**
- Always set `ssr = false` and `prerender = false` in root layout or individual pages
- Keep `csr = true` (it's the default)
- Both exports are required for pure SPA behavior

### When to Prerender in SPA Mode

You can selectively prerender pages even in SPA mode:

```ts
// src/routes/about/+page.ts
export const ssr = true;         // Enable for prerendering
export const prerender = true;   // Prerender this page at build
```

This creates static HTML for `/about` while keeping other routes as SPA. Useful for:
- Marketing pages
- About pages
- Terms of service
- Any static content

## Navigation

### Programmatic Navigation

```js
import { goto } from '$app/navigation';

// Navigate to route
goto('/dashboard');

// Navigate with options
goto('/search', {
	replaceState: true,  // Replace history instead of push
	noScroll: true,      // Don't scroll to top
	keepFocus: true,     // Keep current focus
	state: { from: 'home' }  // Pass state
});

// Navigate with search params
goto('/search?q=sveltekit&page=2');
```

### Link Behavior

```svelte
<!-- Standard navigation -->
<a href="/dashboard">Dashboard</a>

<!-- Disable client-side routing for this link -->
<a href="/external" data-sveltekit-reload>External Site</a>

<!-- Prefetch on hover -->
<a href="/dashboard" data-sveltekit-preload-data="hover">
	Dashboard
</a>

<!-- Prefetch on viewport -->
<a href="/dashboard" data-sveltekit-preload-data="viewport">
	Dashboard
</a>
```

## State Management

### URL State with $page

```svelte
<script lang="ts">
	import { page } from '$app/state';

	// Access current route info
	$effect(() => {
		console.log(page.url.pathname);  // Current path
		console.log(page.params);        // Route parameters
		console.log(page.data);          // Data from load functions
	});
</script>

<div>
	Current path: {page.url.pathname}
	{#if page.params.id}
		Viewing ID: {page.params.id}
	{/if}
</div>
```

### Navigation State

```svelte
<script lang="ts">
	import { navigating } from '$app/state';

	// Show loading indicator during navigation
</script>

{#if navigating}
	<div class="loading-bar">Loading...</div>
{/if}
```

## Error Pages

```svelte
<!-- src/routes/+error.svelte -->
<script lang="ts">
	import { page } from '$app/state';
</script>

<div class="error-page">
	<h1>{page.status}</h1>
	<p>{page.error?.message}</p>
	<a href="/">Go home</a>
</div>
```

## Environment Variables

```js
// .env
VITE_API_URL=http://localhost:8080
VITE_PUBLIC_KEY=pk_test_...
```

```js
// Access in code
const apiUrl = import.meta.env.VITE_API_URL;
const publicKey = import.meta.env.VITE_PUBLIC_KEY;
```

**Important:** All env vars must be prefixed with `VITE_` to be accessible in client-side code.

## Common Patterns

### Protected Routes

```ts
// src/routes/dashboard/+layout.ts
import { redirect } from '@sveltejs/kit';
import type { LayoutLoad } from './$types';

export const ssr = false;
export const prerender = false;

export const load: LayoutLoad = async ({ parent }) => {
	const { user } = await parent();

	if (!user) {
		throw redirect(303, '/login');
	}

	return { user };
};
```

### Data Fetching with Loading States

```svelte
<script lang="ts">
	import { onMount } from 'svelte';

	interface DataResponse {
		content: string;
	}

	let data = $state<DataResponse | null>(null);
	let loading = $state(true);
	let error = $state<string | null>(null);

	onMount(async () => {
		try {
			const response = await fetch('/api/data');
			data = await response.json();
		} catch (e) {
			error = e instanceof Error ? e.message : 'Failed to load data';
		} finally {
			loading = false;
		}
	});
</script>

{#if loading}
	<p>Loading...</p>
{:else if error}
	<p>Error: {error}</p>
{:else if data}
	<div>{data.content}</div>
{/if}
```

### Pagination

```svelte
<script lang="ts">
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import { cn } from '$lib/utils';
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	function goToPage(pageNum: number) {
		const url = new URL(window.location.href);
		url.searchParams.set('page', String(pageNum));
		goto(url.pathname + url.search);
	}

	const currentPage = Number(page.url.searchParams.get('page') || '1');
</script>

<div class="items">
	{#each data.items as item}
		<div>{item.title}</div>
	{/each}
</div>

<div class="pagination">
	{#each Array(data.totalPages) as _, i}
		<button
			class={cn('page-btn', currentPage === i + 1 && 'active')}
			onclick={() => goToPage(i + 1)}
		>
			{i + 1}
		</button>
	{/each}
</div>
```

## Build and Deployment

### Build Command

```bash
bun run build
```

This generates static files in the `build/` directory (or path specified in adapter config).

### Preview Locally

```bash
bun run preview
```

### Directory Structure After Build

```
build/
├── _app/
│   ├── immutable/      # Hashed JS/CSS chunks
│   └── version.json
├── 200.html            # Fallback page (your SPA entry)
└── index.html          # Root page (if prerendered)
```

### Deployment Checklist

1. ✅ `adapter-static` configured with correct fallback
2. ✅ `ssr = false` in root layout
3. ✅ Backend API URLs configured via environment variables
4. ✅ CORS configured on backend for frontend origin
5. ✅ Build successful with no errors
6. ✅ Test locally with `bun run preview`
7. ✅ Deploy `build/` directory to static host

## SvelteKit SPA vs Pure Vite

**Choose SvelteKit SPA when you want:**
- File-based routing
- Load functions for data fetching
- Built-in error pages
- Layouts and nested routes
- Programmatic navigation with goto()
- URL state management

**Choose Pure Vite + Svelte when you want:**
- Manual routing (or no routing)
- Complete control over bundle structure
- Minimal framework overhead
- Custom build configuration

SvelteKit SPA provides routing and data loading conventions while remaining fully client-side.

## Troubleshooting

### Issue: "Cannot access server-side modules"

**Cause:** Trying to use `+page.server.ts` in SPA mode.

**Solution:** Use `+page.ts` instead. All load functions run client-side in SPA mode.

### Issue: "This page will be rendered on the server"

**Cause:** `ssr = false` and `prerender = false` not set.

**Solution:** Add both exports to root `+layout.ts`:
```ts
export const ssr = false;
export const prerender = false;
```

### Issue: 404 errors on refresh

**Cause:** Server doesn't serve fallback page for all routes.

**Solution:** 
- Verify adapter fallback configuration
- Configure your static host to serve the fallback page for all routes
- Test with `bun run preview` locally first

### Issue: API CORS errors

**Cause:** Backend not configured to allow frontend origin.

**Solution:** Configure CORS on your Golang/Echo backend:

```go
// In your Echo server
e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
    AllowOrigins: []string{"http://localhost:5173", "https://yourdomain.com"},
    AllowMethods: []string{http.MethodGet, http.MethodPost, http.MethodPut, http.MethodDelete},
    AllowHeaders: []string{"Authorization", "Content-Type"},
}))
```

### Issue: Environment variables not available

**Cause:** Variables not prefixed with `VITE_`.

**Solution:** Rename all client-side env vars to start with `VITE_`.

## Performance Optimization

### Prefetching Strategies

SvelteKit provides built-in prefetching for faster navigation:

```svelte
<!-- Prefetch on hover (most common) -->
<a href="/dashboard" data-sveltekit-preload-data="hover">
	Dashboard
</a>

<!-- Prefetch when link enters viewport -->
<a href="/reports" data-sveltekit-preload-data="viewport">
	Reports
</a>

<!-- Prefetch immediately on page load -->
<a href="/critical" data-sveltekit-preload-data="tap">
	Critical Page
</a>
```

### Code Splitting

Leverage dynamic imports for large components:

```svelte
<script lang="ts">
	import { onMount } from 'svelte';
	import type { Component } from 'svelte';

	let HeavyComponent = $state<Component | null>(null);

	onMount(async () => {
		// Load component only when needed
		const module = await import('$lib/components/HeavyChart.svelte');
		HeavyComponent = module.default;
	});
</script>

{#if HeavyComponent}
	<svelte:component this={HeavyComponent} />
{/if}
```

### Selective Prerendering

Prerender static pages for instant loading:

```ts
// src/routes/about/+page.ts
export const prerender = true;
export const ssr = true; // Enable for build-time rendering
```

Good candidates for prerendering:
- Marketing pages
- About/Terms/Privacy pages
- Documentation
- Blog posts (if content is static)

### Request Deduplication

Prevent duplicate API calls in load functions:

```ts
// src/lib/cache.ts
const cache = new Map<string, unknown>();
const pending = new Map<string, Promise<unknown>>();

export async function cachedFetch<T>(url: string, options: RequestInit = {}): Promise<T> {
	const key = `${url}:${JSON.stringify(options)}`;

	// Return cached result
	if (cache.has(key)) {
		return cache.get(key) as T;
	}

	// Return pending request
	if (pending.has(key)) {
		return pending.get(key) as Promise<T>;
	}

	// Make new request
	const promise = fetch(url, options).then((r) => r.json());
	pending.set(key, promise);

	try {
		const result = await promise;
		cache.set(key, result);
		return result as T;
	} finally {
		pending.delete(key);
	}
}
```

### Loading State Optimization

Show instant feedback during navigation:

```svelte
<script lang="ts">
	import { navigating } from '$app/state';
</script>

{#if navigating}
	<div class="loading-bar" />
{/if}

<style>
	.loading-bar {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		height: 3px;
		background: linear-gradient(90deg, #4f46e5, #06b6d4);
		animation: slide 1s ease-in-out infinite;
	}

	@keyframes slide {
		0% { transform: translateX(-100%); }
		100% { transform: translateX(100%); }
	}
</style>
```

### Bundle Optimization Tips

1. **Tree-shake unused code** - Import only what you need
2. **Use lightweight alternatives** - Consider bundle size of dependencies
3. **Lazy load routes** - SvelteKit does this automatically
4. **Optimize images** - Use modern formats (WebP, AVIF)
5. **Enable compression** - Configure your hosting for gzip/brotli

## Best Practices

1. **Disable SSR and prerender early** - Set both `ssr = false` and `prerender = false` in root `+layout.ts` immediately
2. **Use load functions** - Centralize data fetching in `+page.ts` load functions with proper TypeScript types
3. **Handle errors gracefully** - Use error boundaries and proper error states
4. **Protect routes** - Implement authentication checks in layout load functions
5. **Use environment variables** - Never hardcode API URLs or keys
6. **Test locally** - Always test with `bun run preview` before deploying
7. **Configure CORS properly** - Ensure backend allows frontend origin
8. **Consider prerendering** - Prerender static pages for better initial load
9. **Use absolute API URLs** - Avoid relative paths when calling backend
10. **Handle loading states** - Show feedback during data fetching

## Related Documentation

For advanced patterns and additional context:
- See `references/routing-patterns.md` for complex routing scenarios
- See `references/backend-integration.md` for detailed backend integration patterns
