# Advanced Routing Patterns for SvelteKit SPA

## Complex Nested Layouts

### Multi-Level Dashboard Layout

```
src/routes/
├── +layout.svelte              # Root layout (header, global styles)
├── +layout.ts                  # Auth check, global data
├── dashboard/
│   ├── +layout.svelte          # Dashboard shell (sidebar)
│   ├── +layout.ts              # Dashboard-specific data
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

```ts
// src/routes/+layout.ts (Root)
import type { LayoutLoad } from './$types';

export const ssr = false;
export const prerender = false;

export const load: LayoutLoad = async () => {
	const token = localStorage.getItem('auth_token');
	return { token };
};
```

```ts
// src/routes/dashboard/+layout.ts (Dashboard)
import { redirect } from '@sveltejs/kit';
import type { LayoutLoad } from './$types';

interface DashboardMeta {
	title: string;
	permissions: string[];
}

export const load: LayoutLoad = async ({ parent, fetch }) => {
	const { token } = await parent(); // Get data from parent layout

	if (!token) {
		throw redirect(303, '/login');
	}

	// Fetch dashboard-specific data
	const response = await fetch('/api/dashboard/metadata', {
		headers: { 'Authorization': `Bearer ${token}` }
	});

	const dashboardMeta: DashboardMeta = await response.json();

	return {
		...(await parent()), // Include parent data
		dashboardMeta
	};
};
```

## Optional Parameters

### Pattern: `/blog/[[page]]`

```
src/routes/blog/[[page]]/+page.ts
```

Matches:
- `/blog` (page is undefined)
- `/blog/1` (page is "1")
- `/blog/latest` (page is "latest")

```ts
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params, fetch }) => {
	const page = params.page || '1';
	const pageNum = parseInt(page);

	const response = await fetch(`/api/blog?page=${pageNum}`);
	return await response.json();
};
```

## Rest Parameters

### Pattern: `/docs/[...path]`

```
src/routes/docs/[...path]/+page.ts
```

Matches:
- `/docs/intro` (path is "intro")
- `/docs/guide/getting-started` (path is "guide/getting-started")
- `/docs/api/v2/users/create` (path is "api/v2/users/create")

```ts
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params, fetch }) => {
	const docPath = params.path;

	const response = await fetch(`/api/docs/${docPath}`);
	if (!response.ok) {
		throw error(404, 'Documentation not found');
	}

	return await response.json();
};
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
<script lang="ts">
	import { page } from '$app/state';
	import { cn } from '$lib/utils';
	import type { Snippet } from 'svelte';

	interface Props {
		children: Snippet;
	}

	const tabs = [
		{ path: '/profile', label: 'Overview' },
		{ path: '/profile/posts', label: 'Posts' },
		{ path: '/profile/settings', label: 'Settings' }
	];

	let { children }: Props = $props();
</script>

<div class="tabs">
	{#each tabs as tab}
		<a href={tab.path} class={cn('tab', page.url.pathname === tab.path && 'active')}>
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
<script lang="ts">
	import { page } from '$app/state';
	import Modal from '$lib/Modal.svelte';
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

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

```ts
// src/routes/dashboard/+page.ts
import type { PageLoad } from './$types';

interface Stats {
	total: number;
	active: number;
}

interface Activity {
	id: string;
	action: string;
	timestamp: string;
}

interface Alert {
	id: string;
	message: string;
	severity: 'info' | 'warning' | 'error';
}

export const load: PageLoad = async ({ fetch }) => {
	// Fetch in parallel
	const [stats, activity, alerts] = await Promise.all([
		fetch('/api/stats').then((r) => r.json()) as Promise<Stats>,
		fetch('/api/activity').then((r) => r.json()) as Promise<Activity[]>,
		fetch('/api/alerts').then((r) => r.json()) as Promise<Alert[]>
	]);

	return { stats, activity, alerts };
};
```

## Search Results with Filters

```ts
// src/routes/search/+page.ts
import type { PageLoad } from './$types';

interface SearchResult {
	id: string;
	title: string;
	description: string;
}

interface Filters {
	query: string;
	category: string;
	sort: string;
	page: number;
}

export const load: PageLoad = async ({ url, fetch }) => {
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
	const results: SearchResult[] = await response.json();

	return {
		results,
		filters: { query, category, sort, page } satisfies Filters
	};
};
```

```svelte
<!-- src/routes/search/+page.svelte -->
<script lang="ts">
	import { goto } from '$app/navigation';
	import { cn } from '$lib/utils';
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	function updateFilter(key: string, value: string) {
		const url = new URL(window.location.href);
		url.searchParams.set(key, value);
		url.searchParams.set('page', '1'); // Reset to page 1
		goto(url.pathname + url.search);
	}

	function handleCategoryChange(e: Event) {
		const target = e.target as HTMLSelectElement;
		updateFilter('category', target.value);
	}

	function handleSortChange(e: Event) {
		const target = e.target as HTMLSelectElement;
		updateFilter('sort', target.value);
	}
</script>

<select onchange={handleCategoryChange}>
	<option value="all">All</option>
	<option value="posts">Posts</option>
	<option value="users">Users</option>
</select>

<select onchange={handleSortChange}>
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
<script lang="ts">
	import { onMount } from 'svelte';
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	interface Item {
		id: string;
		title: string;
	}

	let { data }: Props = $props();
	let items = $state<Item[]>([...data.items]);
	let page = $state(1);
	let loading = $state(false);
	let hasMore = $state(true);

	async function loadMore() {
		if (loading || !hasMore) return;

		loading = true;
		page += 1;

		try {
			const response = await fetch(`/api/items?page=${page}`);
			const newItems: Item[] = await response.json();

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
<script lang="ts">
	import { page } from '$app/state';
	import { setContext } from 'svelte';
	import { cn } from '$lib/utils';
	import type { Snippet } from 'svelte';

	interface Props {
		children: Snippet;
	}

	interface FormData {
		step1: { name?: string; email?: string };
		step2: { preferences?: string[] };
		step3: { confirmed?: boolean };
	}

	let { children }: Props = $props();

	// Shared form state using $state rune
	const formData = $state<FormData>({
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

	const currentStepIndex = $derived(steps.findIndex((s) => s.path === page.url.pathname));
</script>

<div class="progress-bar">
	{#each steps as step, i}
		<div
			class={cn(
				'step',
				i === currentStepIndex && 'active',
				i < currentStepIndex && 'completed'
			)}
		>
			{step.label}
		</div>
	{/each}
</div>

{@render children()}
```

```svelte
<!-- src/routes/onboarding/step1/+page.svelte -->
<script lang="ts">
	import { getContext } from 'svelte';
	import { goto } from '$app/navigation';

	interface FormData {
		step1: { name?: string; email?: string };
		step2: { preferences?: string[] };
		step3: { confirmed?: boolean };
	}

	const formData = getContext<FormData>('onboarding');

	let data = $state({ name: formData.step1.name ?? '', email: formData.step1.email ?? '' });

	function next() {
		formData.step1 = { ...data };
		goto('/onboarding/step2');
	}
</script>

<form onsubmit={(e) => { e.preventDefault(); next(); }}>
	<input bind:value={data.name} placeholder="Name" />
	<input bind:value={data.email} placeholder="Email" />
	<button type="submit">Next</button>
</form>
```
