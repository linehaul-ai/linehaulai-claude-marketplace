# Svelte Flow Quick Start (5 Minutes)

Get a basic node-based editor running in 5 minutes.

## Step 1: Install Dependency

```bash
npm install @xyflow/svelte
# or with bun:
bun add @xyflow/svelte
```

## Step 2: Create Basic Component

Create `src/lib/SimpleEditor.svelte`:

```svelte
<script lang="ts">
  import { SvelteFlow, Background } from '@xyflow/svelte';
  import '@xyflow/svelte/dist/style.css';

  // Define nodes
  let nodes = $state.raw([
    {
      id: '1',
      data: { label: 'Start' },
      position: { x: 0, y: 0 }
    },
    {
      id: '2',
      data: { label: 'Process' },
      position: { x: 0, y: 100 }
    },
    {
      id: '3',
      data: { label: 'End' },
      position: { x: 0, y: 200 }
    }
  ]);

  // Define edges (connections)
  let edges = $state.raw([
    { id: 'e1-2', source: '1', target: '2' },
    { id: 'e2-3', source: '2', target: '3' }
  ]);
</script>

<div class="editor-container">
  <SvelteFlow {nodes} {edges} fitView>
    <Background />
  </SvelteFlow>
</div>

<style>
  .editor-container {
    width: 100%;
    height: 100vh;
  }
</style>
```

## Step 3: Use in Your App

Import and use the component:

```svelte
<!-- src/routes/+page.svelte -->
<script>
  import SimpleEditor from '$lib/SimpleEditor.svelte';
</script>

<SimpleEditor />
```

## Step 4: Add Basic Styling

Create a tailwind class or add inline styles:

```svelte
<style>
  .editor-container {
    width: 100%;
    height: 100vh;
    background: #fafafa;
  }
</style>
```

## Step 5: Add Node Drag Support

Update the script section to enable dragging:

```svelte
<script lang="ts">
  import { SvelteFlow, Background, useStore } from '@xyflow/svelte';
  import '@xyflow/svelte/dist/style.css';

  let nodes = $state.raw([...]);
  let edges = $state.raw([...]);

  const store = useStore();

  // Nodes are now draggable by default!
</script>
```

## Done! 🎉

You now have a basic node editor with:
- ✅ Three nodes positioned vertically
- ✅ Two edges connecting them
- ✅ Draggable nodes
- ✅ Zoom and pan controls
- ✅ Background grid

## Next Steps

1. **Custom Nodes** - Create specialized node components (see PLUGIN_OVERVIEW.md)
2. **Handle Validation** - Restrict which nodes can connect to which
3. **Layout Algorithms** - Auto-arrange nodes with dagre or hierarchical
4. **Styling** - Use Tailwind or CSS to customize appearance
5. **Events** - Handle node/edge selection, connection creation, deletion

## Useful Commands

```bash
# Use the create-editor command for more complex setups
/create-editor Create a workflow editor with step nodes and decision branching

# Ask the expert for specific patterns
# "How do I prevent circular connections in my workflow editor?"
```

## Common Customizations

### Add a Toolbar

```svelte
<div class="toolbar">
  <button on:click={() => addNode()}>Add Node</button>
  <button on:click={() => deleteSelected()}>Delete</button>
  <button on:click={() => fitView()}>Fit View</button>
</div>
```

### Style Nodes

```svelte
let nodes = $state.raw([
  {
    id: '1',
    data: { label: 'Start' },
    position: { x: 0, y: 0 },
    style: 'background: #4CAF50; color: white; border-radius: 8px;'
  },
  ...
]);
```

### Add Edge Labels

```svelte
let edges = $state.raw([
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    label: 'Click to continue',
    animated: true
  },
  ...
]);
```

## Troubleshooting

**Q: Nodes aren't draggable**
A: Make sure you're using `$state.raw` for nodes/edges. `$state` causes reactivity issues.

**Q: Nodes are overlapping**
A: Use a layout algorithm or adjust `position` values manually.

**Q: Edges aren't showing**
A: Verify source and target node IDs match exactly.

**Q: Performance is slow**
A: For 100+ nodes, consider viewport-based rendering (see PLUGIN_OVERVIEW.md).

## Resources

- Full documentation: See the `svelte-flow` skill
- Implementation help: Use the `svelte-flow-expert` agent
- Official docs: https://svelteflow.dev
