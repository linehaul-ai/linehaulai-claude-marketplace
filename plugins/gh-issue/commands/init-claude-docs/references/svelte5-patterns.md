# Svelte 5 Best Practices Reference

## Runes Syntax (Svelte 5)

Svelte 5 introduces runes - a new reactivity system replacing the old `$:` syntax.

### Core Runes

```svelte
<script>
  // $state - reactive state
  let count = $state(0);
  let user = $state({ name: '', email: '' });

  // $derived - computed values (replaces $:)
  let doubled = $derived(count * 2);
  let isValid = $derived(user.name.length > 0 && user.email.includes('@'));

  // $effect - side effects (replaces $: with side effects)
  $effect(() => {
    console.log('Count changed:', count);
    // Cleanup function (optional)
    return () => console.log('Cleanup');
  });

  // $props - component props
  let { title, onSubmit } = $props();

  // $bindable - two-way bindable props
  let { value = $bindable() } = $props();
</script>
```

### State Management Patterns

```svelte
<!-- Avoid: Direct mutation tracking issues -->
<script>
  let items = $state([]);
  items.push(newItem); // Works in Svelte 5!
</script>

<!-- Object state -->
<script>
  let form = $state({
    name: '',
    email: '',
    errors: {}
  });

  function updateField(field, value) {
    form[field] = value;
  }
</script>
```

## Component Patterns

### Props with Defaults

```svelte
<script>
  let {
    variant = 'primary',
    size = 'md',
    disabled = false,
    onclick
  } = $props();
</script>
```

### Snippet Pattern (Replaces Slots)

```svelte
<!-- Parent.svelte -->
<Card>
  {#snippet header()}
    <h2>Title</h2>
  {/snippet}

  {#snippet footer()}
    <Button>Action</Button>
  {/snippet}

  <p>Main content</p>
</Card>

<!-- Card.svelte -->
<script>
  let { header, footer, children } = $props();
</script>

<div class="card">
  {#if header}
    <header>{@render header()}</header>
  {/if}

  <main>{@render children()}</main>

  {#if footer}
    <footer>{@render footer()}</footer>
  {/if}
</div>
```

### Event Handling

```svelte
<script>
  let { onclick, onsubmit } = $props();

  function handleClick(event) {
    // Process then delegate
    onclick?.(event);
  }
</script>

<button {onclick}>Click me</button>
<!-- Or with handler -->
<button onclick={handleClick}>Click me</button>
```

## SvelteKit Patterns

### Load Functions

```typescript
// +page.ts (universal load)
export async function load({ fetch, params }) {
  const response = await fetch(`/api/items/${params.id}`);
  return { item: await response.json() };
}

// +page.server.ts (server-only load)
export async function load({ locals, params }) {
  // Access server-only resources
  const item = await db.items.findUnique({ where: { id: params.id } });
  return { item };
}
```

### Form Actions

```typescript
// +page.server.ts
export const actions = {
  default: async ({ request, locals }) => {
    const data = await request.formData();
    // Process form
    return { success: true };
  },

  delete: async ({ params }) => {
    await db.items.delete({ where: { id: params.id } });
    throw redirect(303, '/items');
  }
};
```

### Error Handling

```typescript
// +error.svelte
<script>
  import { page } from '$app/stores';
</script>

<h1>{$page.status}: {$page.error?.message}</h1>
```

## Styling Patterns

### Scoped Styles

```svelte
<style>
  /* Scoped to this component */
  .button { }

  /* Global escape hatch */
  :global(.external-class) { }
</style>
```

### CSS Variables for Theming

```svelte
<div class="themed" style:--primary={primaryColor}>
  <button class="btn">Themed button</button>
</div>

<style>
  .btn {
    background: var(--primary, #007bff);
  }
</style>
```

## File Organization

```
src/
├── lib/
│   ├── components/     # Reusable components
│   │   ├── ui/         # Base UI components
│   │   └── features/   # Feature-specific components
│   ├── stores/         # Svelte stores
│   ├── utils/          # Utility functions
│   └── types/          # TypeScript types
├── routes/
│   ├── +layout.svelte  # Root layout
│   ├── +page.svelte    # Home page
│   └── [slug]/         # Dynamic routes
└── app.html            # HTML template
```

## Common Gotchas

1. **$state arrays** - Mutations now work: `arr.push(item)` is reactive
2. **$derived vs $effect** - Use $derived for values, $effect only for side effects
3. **Prop destructuring** - Must use $props() in Svelte 5
4. **Snippet vs slot** - Snippets replace slots, use {@render}
