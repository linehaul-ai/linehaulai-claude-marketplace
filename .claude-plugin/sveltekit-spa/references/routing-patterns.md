# Advanced Routing Patterns for SvelteKit SPA

## Complex Nested Layouts

### Multi-Level Dashboard Layout

```
src/routes/
├── +layout.svelte              # Root layout (header, global styles)
├── +layout.js                  # Auth check, global data
├── dashboard/
│   ├── +layout.svelte          # Dashboard shell (sidebar)
│   ├── +layout.js              # Dashboard-specific data
│   ├── +page.svelte            # Dashboard home
│   ├── analytics/
│   │   ├── +layout.svelte      # Analytics section layout
│   │   ├── +page.svelte        # Analytics overview
│   │   ├── reports/
│   │   │   └── +page.svelte    # /dashboard/analytics/reports
│   │   └── charts/
│   │       └── +page.svelte    # /dashboard/analytics/charts
│   └── settings/
│       ├── +page.svelte        # Settings home
│       ├── profile/
│       │   └── +page.svelte    # /dashboard/settings/profile
│       └── billing/
│           └── +page.svelte    # /dashboard/settings/billing
```

### Layout Inheritance Pattern

```js
// src/routes/+layout.js (Root)
export const ssr = false;

export async function load() {
	const token = localStorage.getItem('auth_token');
	return { token };
}
```

```js
// src/routes/dashboard/+layout.js (Dashboard)
import { redirect } from '@sveltejs/kit';

export async function load({ parent }) {
	const { token } = await parent(); // Get data from parent layout
	
	if (!token) {
		throw redirect(303, '/login');
	}
	
	// Fetch dashboard-specific data
	const response = await fetch('/api/dashboard/metadata', {
		headers: { 'Authorization': `Bearer ${token}` }
	});
	
	return {
		...(await parent()), // Include parent data
		dashboardMeta: await response.json()
	};
}
```

## Optional Parameters

### Pattern: `/blog/[[page]]`

```
src/routes/blog/[[page]]/+page.js
```

Matches:
- `/blog` (page is undefined)
- `/blog/1` (page is "1")
- `/blog/latest` (page is "latest")

```js
export async function load({ params }) {
	const page = params.page || '1';
	const pageNum = parseInt(page);
	
	const response = await fetch(`/api/blog?page=${pageNum}`);
	return await response.json();
}
```

## Rest Parameters

### Pattern: `/docs/[...path]`

```
src/routes/docs/[...path]/+page.js
```

Matches:
- `/docs/intro` (path is "intro")
- `/docs/guide/getting-started` (path is "guide/getting-started")
- `/docs/api/v2/users/create` (path is "api/v2/users/create")

```js
export async function load({ params }) {
	const docPath = params.path;
	
	const response = await fetch(`/api/docs/${docPath}`);
	if (!response.ok) {
		throw error(404, 'Documentation not found');
	}
	
	return await response.json();
}
```

## Route Groups

Use parentheses to organize routes without affecting URLs:

```
src/routes/
├── (auth)/
│   ├── +layout.svelte          # Auth layout (no sidebar)
│   ├── login/
│   │   └── +page.svelte        # /login
│   ├── register/
│   │   └── +page.svelte        # /register
│   └── forgot-password/
│       └── +page.svelte        # /forgot-password
└── (app)/
    ├── +layout.svelte          # App layout (with sidebar)
    ├── dashboard/
    │   └── +page.svelte        # /dashboard
    └── settings/
        └── +page.svelte        # /settings
```

The `(auth)` and `(app)` folders don't appear in URLs but allow different layouts.

## Breaking Layout Inheritance

Use `@` to reset layout inheritance:

```
src/routes/
├── +layout.svelte              # Root layout
├── dashboard/
│   ├── +layout.svelte          # Dashboard layout
│   └── report/
│       └── @auth/              # Reset to auth layout
│           ├── +layout.svelte  # Different layout
│           └── +page.svelte
```

This makes `/dashboard/report` use the `@auth` layout instead of the dashboard layout.

## Tab Navigation Pattern

```svelte
<!-- src/routes/profile/+layout.svelte -->
<script>
	import { page } from '$app/state';
	
	const tabs = [
		{ path: '/profile', label: 'Overview' },
		{ path: '/profile/posts', label: 'Posts' },
		{ path: '/profile/settings', label: 'Settings' }
	];
	
	let { children } = $props();
</script>

<div class="tabs">
	{#each tabs as tab}
		<a 
			href={tab.path}
			class:active={page.url.pathname === tab.path}
		>
			{tab.label}
		</a>
	{/each}
</div>

<div class="tab-content">
	{@render children()}
</div>
```

## Modal Routing Pattern

```svelte
<!-- src/routes/items/+page.svelte -->
<script>
	import { page } from '$app/state';
	import Modal from '$lib/Modal.svelte';
	
	let { data } = $props();
	
	const showModal = page.url.searchParams.has('modal');
</script>

{#each data.items as item}
	<a href="/items?modal={item.id}">
		{item.title}
	</a>
{/each}

{#if showModal}
	<Modal itemId={page.url.searchParams.get('modal')} />
{/if}
```

## Parallel Routes

Load data for multiple sections simultaneously:

```js
// src/routes/dashboard/+page.js
export async function load({ fetch }) {
	// Fetch in parallel
	const [stats, activity, alerts] = await Promise.all([
		fetch('/api/stats').then(r => r.json()),
		fetch('/api/activity').then(r => r.json()),
		fetch('/api/alerts').then(r => r.json())
	]);
	
	return { stats, activity, alerts };
}
```

## Search Results with Filters

```js
// src/routes/search/+page.js
export async function load({ url, fetch }) {
	const query = url.searchParams.get('q') || '';
	const category = url.searchParams.get('category') || 'all';
	const sort = url.searchParams.get('sort') || 'relevance';
	const page = parseInt(url.searchParams.get('page') || '1');
	
	const params = new URLSearchParams({
		q: query,
		category,
		sort,
		page: page.toString()
	});
	
	const response = await fetch(`/api/search?${params}`);
	return {
		results: await response.json(),
		filters: { query, category, sort, page }
	};
}
```

```svelte
<!-- src/routes/search/+page.svelte -->
<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
	
	let { data } = $props();
	
	function updateFilter(key, value) {
		const url = new URL(window.location.href);
		url.searchParams.set(key, value);
		url.searchParams.set('page', '1'); // Reset to page 1
		goto(url.pathname + url.search);
	}
</script>

<select onchange={(e) => updateFilter('category', e.target.value)}>
	<option value="all">All</option>
	<option value="posts">Posts</option>
	<option value="users">Users</option>
</select>

<select onchange={(e) => updateFilter('sort', e.target.value)}>
	<option value="relevance">Relevance</option>
	<option value="date">Date</option>
	<option value="popular">Popular</option>
</select>

<div class="results">
	{#each data.results as result}
		<div>{result.title}</div>
	{/each}
</div>
```

## Infinite Scroll Pattern

```svelte
<script>
	import { onMount } from 'svelte';
	
	let { data } = $props();
	let items = $state([...data.items]);
	let page = $state(1);
	let loading = $state(false);
	let hasMore = $state(true);
	
	async function loadMore() {
		if (loading || !hasMore) return;
		
		loading = true;
		page += 1;
		
		try {
			const response = await fetch(`/api/items?page=${page}`);
			const newItems = await response.json();
			
			if (newItems.length === 0) {
				hasMore = false;
			} else {
				items = [...items, ...newItems];
			}
		} finally {
			loading = false;
		}
	}
	
	onMount(() => {
		const observer = new IntersectionObserver((entries) => {
			if (entries[0].isIntersecting) {
				loadMore();
			}
		});
		
		const sentinel = document.querySelector('.load-more-sentinel');
		if (sentinel) observer.observe(sentinel);
		
		return () => observer.disconnect();
	});
</script>

<div class="items">
	{#each items as item}
		<div>{item.title}</div>
	{/each}
</div>

{#if hasMore}
	<div class="load-more-sentinel">
		{#if loading}
			<p>Loading...</p>
		{/if}
	</div>
{/if}
```

## Route Matching Priority

SvelteKit prioritizes routes in this order:

1. Static routes: `/about`
2. Dynamic routes: `/blog/[slug]`
3. Rest parameters: `/docs/[...path]`

Example priority:

```
src/routes/
├── blog/
│   ├── latest/
│   │   └── +page.svelte    # Priority 1: /blog/latest
│   └── [slug]/
│       └── +page.svelte    # Priority 2: /blog/anything-else
└── docs/
    ├── api/
    │   └── +page.svelte    # Priority 1: /docs/api
    └── [...path]/
        └── +page.svelte    # Priority 2: /docs/anything/else
```

## Multi-Step Form Pattern

```svelte
<!-- src/routes/onboarding/+layout.svelte -->
<script>
	import { page } from '$app/state';
	import { writable } from 'svelte/store';
	import { setContext } from 'svelte';
	
	let { children } = $props();
	
	// Shared form state
	const formData = writable({
		step1: {},
		step2: {},
		step3: {}
	});
	
	setContext('onboarding', formData);
	
	const steps = [
		{ path: '/onboarding/step1', label: 'Personal Info' },
		{ path: '/onboarding/step2', label: 'Preferences' },
		{ path: '/onboarding/step3', label: 'Confirmation' }
	];
	
	const currentStepIndex = steps.findIndex(s => s.path === page.url.pathname);
</script>

<div class="progress-bar">
	{#each steps as step, i}
		<div class:active={i === currentStepIndex} class:completed={i < currentStepIndex}>
			{step.label}
		</div>
	{/each}
</div>

{@render children()}
```

```svelte
<!-- src/routes/onboarding/step1/+page.svelte -->
<script>
	import { getContext } from 'svelte';
	import { goto } from '$app/navigation';
	
	const formData = getContext('onboarding');
	
	let data = $state($formData.step1);
	
	function next() {
		formData.update(d => ({ ...d, step1: data }));
		goto('/onboarding/step2');
	}
</script>

<form onsubmit={(e) => { e.preventDefault(); next(); }}>
	<input bind:value={data.name} placeholder="Name" />
	<input bind:value={data.email} placeholder="Email" />
	<button type="submit">Next</button>
</form>
```
