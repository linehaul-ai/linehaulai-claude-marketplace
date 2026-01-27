# Snippets: Content Composition in Svelte 5

## Quick Reference

| Feature              | Syntax                                         |
| -------------------- | ---------------------------------------------- |
| Default content      | `{@render children()}`                         |
| Named content        | `{@render header()}`                           |
| Provide named        | `{#snippet header()}...{/snippet}`             |
| With parameters      | `{@render item(data)}`                         |
| Optional with fallback | `{@render children?.() ?? 'Fallback'}`       |

## Children (Default Content)

### Component Definition

```svelte
<!-- Card.svelte -->
<script>
	let { children } = $props();
</script>

<div class="card">
	{@render children()}
</div>
```

### Usage

```svelte
<Card>
	<p>This is card content</p>
</Card>
```

**Key points:**

- Must declare `children` in `$props()`
- Use `{@render children()}` to render
- Content between component tags becomes `children`

## Named Snippets

### Component Definition

```svelte
<!-- Layout.svelte -->
<script>
	let { header, footer, children } = $props();
</script>

<div class="layout">
	<header>{@render header()}</header>
	<main>{@render children()}</main>
	<footer>{@render footer()}</footer>
</div>
```

### Usage

```svelte
<Layout>
	{#snippet header()}
		Header content
	{/snippet}

	{#snippet footer()}
		Footer content
	{/snippet}

	Main content
</Layout>
```

**Key points:**

- Snippets are props declared in `$props()`
- Named snippets use `{#snippet name()}...{/snippet}` syntax
- Content outside snippets becomes `children`

## Snippet Parameters

### Component Definition

```svelte
<!-- List.svelte -->
<script>
	let { items, children } = $props();
</script>

<ul>
	{#each items as item, i}
		<li>
			{@render children(item, i)}
		</li>
	{/each}
</ul>
```

### Usage

```svelte
<List items={users}>
	{#snippet children(item, index)}
		{index}: {item.name}
	{/snippet}
</List>
```

**Key points:**

- Parameters are explicit function arguments
- Better TypeScript support with typed parameters
- Can pass any data to the snippet

## Optional Snippets

### With Conditional Rendering

```svelte
<!-- Card.svelte -->
<script>
	let { header, children } = $props();
</script>

<div class="card">
	{#if header}
		<h2>{@render header()}</h2>
	{:else}
		<h2>Default Title</h2>
	{/if}

	{@render children()}
</div>
```

### Shorthand with Optional Chaining

```svelte
<script>
  let { header, children } = $props();
</script>

<div class="card">
  <h2>{@render header?.() ?? 'Default Title'}</h2>
  {@render children()}
</div>
```

## Reusable Snippets

Snippets can be defined and reused within a component:

```svelte
<script>
	let items = $state(['Apple', 'Banana', 'Cherry']);
</script>

{#snippet listItem(text)}
	<li class="item">{text}</li>
{/snippet}

<ul>
	{#each items as item}
		{@render listItem(item)}
	{/each}
</ul>

<ul>
	{#each items.slice(0, 2) as item}
		{@render listItem(item)}
	{/each}
</ul>
```

**Benefits:**

- DRY (Don't Repeat Yourself)
- Keeps markup organized
- Can be passed to child components

## Passing Snippets as Props

```svelte
<!-- Table.svelte -->
<script>
  let { data, renderCell } = $props();
</script>

<table>
  {#each data as row}
    <tr>
      {#each row as cell}
        <td>{@render renderCell(cell)}</td>
      {/each}
    </tr>
  {/each}
</table>

<!-- Usage -->
<script>
  let data = $state([[1, 2], [3, 4]]);
</script>

{#snippet boldCell(value)}
  <strong>{value}</strong>
{/snippet}

<Table {data} renderCell={boldCell} />
```

## TypeScript with Snippets

```svelte
<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		children: Snippet;
		header?: Snippet;
		item?: Snippet<[{ name: string; age: number }]>; // Snippet with params
	}

	let { children, header, item }: Props = $props();
</script>

{#if header}
	{@render header()}
{/if}

{@render children()}

{#if item}
	{@render item({ name: 'Alex', age: 30 })}
{/if}
```

## Common Patterns

### Conditional Rendering

```svelte
<script>
	let { header, showHeader = true, children } = $props();
</script>

{#if showHeader && header}
	{@render header()}
{/if}

{@render children()}
```

### Multiple Content Sections

```svelte
<script>
	let { sidebar, main } = $props();
</script>

<div class="layout">
	<aside>{@render sidebar()}</aside>
	<main>{@render main()}</main>
</div>

<!-- Usage -->
<Layout>
	{#snippet sidebar()}
		<nav>Navigation</nav>
	{/snippet}

	{#snippet main()}
		<p>Main content</p>
	{/snippet}
</Layout>
```

### Snippet with Complex Logic

```svelte
{#snippet userCard(user)}
	<div class="card">
		<h3>{user.name}</h3>
		{#if user.email}
			<p>{user.email}</p>
		{/if}
		{#if user.premium}
			<span class="badge">Premium</span>
		{/if}
	</div>
{/snippet}

{#each users as user}
	{@render userCard(user)}
{/each}
```

## Common Mistakes

### Forgetting to Declare children

```svelte
<!-- WRONG -->
<div>
	{@render children()}
	<!-- ERROR: children not defined -->
</div>

<!-- RIGHT -->
<script>
	let { children } = $props();
</script>

<div>
	{@render children()}
</div>
```

### Missing Parentheses

```svelte
<!-- WRONG -->
{@render children}  <!-- Missing () -->

<!-- RIGHT -->
{@render children()}
```

### Not Handling Missing Optional Snippets

```svelte
<!-- RISKY -->
<script>
	let { header } = $props();
</script>

{@render header()}
<!-- Error if header not provided! -->

<!-- SAFE -->
{#if header}
	{@render header()}
{/if}

<!-- OR -->
{@render header?.()}
```

## Why Snippets

1. **Explicit** - Props make it clear what content areas exist
2. **TypeScript support** - Can type snippet parameters
3. **Composable** - Snippets can be passed around like functions
4. **Cleaner syntax** - Straightforward function-like semantics
5. **Powerful** - Can define reusable snippets within components
6. **Consistent** - Everything is a prop
