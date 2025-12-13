# Svelte Flow Plugin Overview

Comprehensive architecture and advanced patterns for building interactive node-based editors.

## Plugin Structure

```
.claude-plugin/svelte-flow/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── agents/
│   └── svelte-flow-expert.md    # Expert subagent for implementation guidance
├── commands/
│   └── create-editor.md         # Command for editor orchestration
├── skills/
│   └── svelte-flow/
│       └── SKILL.md             # Comprehensive skill documentation
├── README.md                     # Plugin overview
├── QUICK_START.md                # 5-minute getting started
└── PLUGIN_OVERVIEW.md            # This file (architecture & patterns)
```

## Architecture Patterns

### 1. Basic Editor Pattern

**When to use:** Simple flow editors with standard nodes

```svelte
<script lang="ts">
  import { SvelteFlow, Background, useStore } from '@xyflow/svelte';
  import type { Node, Edge } from '@xyflow/svelte';

  let nodes: Node[] = $state.raw([...]);
  let edges: Edge[] = $state.raw([...]);

  const store = useStore();

  // Nodes are draggable by default
  // Zoom/pan enabled by default
</script>

<SvelteFlow {nodes} {edges} fitView>
  <Background />
</SvelteFlow>
```

### 2. Custom Node Pattern

**When to use:** Specialized node appearances (workflow steps, data sources, etc.)

```svelte
<!-- CustomNode.svelte -->
<script lang="ts" module>
  import type { NodeProps } from '@xyflow/svelte';

  export interface CustomNodeData {
    label: string;
    status: 'pending' | 'active' | 'completed';
    icon: string;
  }
</script>

<script lang="ts">
  type $$Props = NodeProps<CustomNodeData>;

  let { data, isConnecting, selected } = $$props;
</script>

<div class={`node ${data.status} ${selected ? 'selected' : ''}`}>
  <div class="icon">{data.icon}</div>
  <div class="label">{data.label}</div>
</div>

<style>
  .node {
    padding: 12px;
    border-radius: 8px;
    background: white;
    border: 2px solid #ccc;
    min-width: 150px;
  }

  .node.pending { border-color: #ffb74d; }
  .node.active { border-color: #4caf50; }
  .node.completed { border-color: #2196f3; }
  .node.selected { box-shadow: 0 0 0 2px #2196f3; }
</style>
```

### 3. Layout Algorithm Pattern

**When to use:** Auto-arranging nodes instead of manual positioning

```typescript
import { getLayoutedElements } from 'elkjs';
import type { Node, Edge } from '@xyflow/svelte';

export async function layoutNodes(
  nodes: Node[],
  edges: Edge[],
  algorithm: 'dagre' | 'hierarchical' = 'dagre'
): Promise<Node[]> {
  // Use algorithm to calculate positions
  // Return nodes with updated positions
  const layouted = await elkjs.layout({
    nodes: nodes.map(n => ({ id: n.id, width: 150, height: 50 })),
    edges: edges.map(e => ({ id: e.id, sources: [e.source], targets: [e.target] }))
  });

  return nodes.map(node => ({
    ...node,
    position: {
      x: layouted.children?.find(n => n.id === node.id)?.x || 0,
      y: layouted.children?.find(n => n.id === node.id)?.y || 0
    }
  }));
}
```

### 4. Validation Pattern

**When to use:** Restricting connections based on business logic

```typescript
interface ValidationRules {
  canConnect: (source: Node, target: Node) => boolean;
  canDelete: (node: Node) => boolean;
  isValidConnection: (edge: Edge) => boolean;
}

const rules: ValidationRules = {
  canConnect: (source, target) => {
    // Example: Prevent loops
    return source.id !== target.id;
  },
  canDelete: (node) => {
    // Example: Don't delete special nodes
    return node.type !== 'start' && node.type !== 'end';
  },
  isValidConnection: (edge) => {
    // Example: Validate edge data
    return edge.source !== edge.target;
  }
};
```

### 5. State Management Pattern

**When to use:** Managing editor state (undo/redo, persistence)

```typescript
interface EditorState {
  nodes: Node[];
  edges: Edge[];
  history: {
    past: EditorState[];
    future: EditorState[];
  };
}

function createEditorStore() {
  let state = $state<EditorState>({
    nodes: [],
    edges: [],
    history: { past: [], future: [] }
  });

  return {
    get nodes() { return state.nodes; },
    get edges() { return state.edges; },

    addNode(node: Node) {
      state.nodes.push(node);
      state.history.future = [];
    },

    undo() {
      if (state.history.past.length === 0) return;
      state.history.future.unshift(state);
      state = state.history.past.pop()!;
    },

    redo() {
      if (state.history.future.length === 0) return;
      state.history.past.push(state);
      state = state.history.future.shift()!;
    },

    save() {
      localStorage.setItem('editor-state', JSON.stringify(state));
    },

    load() {
      const saved = localStorage.getItem('editor-state');
      if (saved) state = JSON.parse(saved);
    }
  };
}
```

## Use Case Examples

### 1. Workflow Builder

**Features:**
- Step nodes with conditional branching
- DAG validation (no cycles)
- Execution visualization
- Export to workflow format

**Key components:**
- Step, Decision, Merge, End nodes
- Animated edges during execution
- Dagre layout for automatic arrangement

```typescript
type WorkflowNodeType = 'step' | 'decision' | 'merge' | 'start' | 'end';

interface WorkflowNode extends Node {
  type: WorkflowNodeType;
  data: {
    label: string;
    description?: string;
    config?: Record<string, unknown>;
  };
}
```

### 2. Data Pipeline

**Features:**
- Source, transform, sink nodes
- Data type validation
- Lineage tracking
- Performance metrics

**Key components:**
- Database, Transform, API nodes
- Type-labeled edges
- Hierarchical layout

```typescript
type PipelineNodeType = 'source' | 'transform' | 'sink' | 'join';

interface PipelineNode extends Node {
  type: PipelineNodeType;
  data: {
    operation: string;
    schema?: Schema;
    performance?: PerformanceMetrics;
  };
}
```

### 3. Org Chart

**Features:**
- Employee hierarchy
- Department visualization
- Expandable/collapsible groups
- Search and filtering

**Key components:**
- Person cards with photos
- Department containers
- Hierarchical layout

```typescript
interface OrgNode extends Node {
  type: 'person' | 'department';
  data: {
    name: string;
    title?: string;
    department?: string;
    photo?: string;
    team?: OrgNode[];
  };
}
```

## Performance Considerations

### For Large Graphs (100+ nodes)

1. **Viewport Rendering**
   ```typescript
   // Only render visible nodes
   const visibleNodes = nodes.filter(node => isInViewport(node, viewport));
   ```

2. **Memoization**
   ```svelte
   <!-- Use Svelte Component library memoization -->
   <SvelteFlow {nodes} {edges}>
     <!-- Only re-render if nodes/edges change -->
   </SvelteFlow>
   ```

3. **Batch Updates**
   ```typescript
   // Update multiple nodes efficiently
   nodes = nodes.map(n => ({...n, ...updates[n.id]}));
   ```

4. **Edge Simplification**
   - Reduce edge curve complexity
   - Use straight lines instead of bezier for many edges
   - Consider edge pruning in large graphs

## Integration Points

### With TypeScript
- Full type safety for nodes, edges, handles
- Custom node data types
- Event handler typing

### With Tailwind CSS
- Style nodes with utility classes
- Custom edge styling
- Responsive containers

### With shadcn-svelte
- Use Button, Dialog, Input components in custom nodes
- Card component for complex node layouts
- Form validation in node config dialogs

### With SvelteKit
- Page-based editors
- API endpoints for persistence
- Server-side layout calculation

## Best Practices

1. **Node Design**
   - Keep nodes reasonably sized (min 100x50px)
   - Use clear labels and icons
   - Minimize nested components

2. **Edge Management**
   - Limit edge complexity in large graphs
   - Use animated edges sparingly
   - Color-code edges by type/status

3. **Layout**
   - Choose algorithm based on data structure
   - Cache layout calculations
   - Update incrementally on changes

4. **Performance**
   - Use `$state.raw` for nodes/edges arrays
   - Debounce frequent updates
   - Monitor render cycles

5. **UX**
   - Provide visual feedback for interactions
   - Support keyboard shortcuts
   - Enable undo/redo for critical operations
   - Show clear error messages

## Advanced Topics

### Custom Handles
Position connection points anywhere on node:

```svelte
<Handle type="target" position={Position.Top} />
<Handle type="source" position={Position.Bottom} />
```

### Animated Edges
Visualize data flow:

```typescript
let edges = $state.raw([
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    animated: true,
    style: { stroke: '#f6ad55' }
  }
]);
```

### Selection Events
Handle node/edge selection:

```typescript
onSelectionChange(({ nodes, edges }) => {
  console.log('Selected:', nodes, edges);
});
```

### Minimap
Show overview of large graphs:

```svelte
<MiniMap nodeColor="#f6ad55" nodeStrokeColor="#f97316" />
```

## Resources

- **Skill**: Read `svelte-flow` for complete API reference
- **Expert**: Consult `svelte-flow-expert` for implementation decisions
- **Command**: Use `/create-editor` for scaffolding
- **Official**: https://svelteflow.dev

---

**Ready to build advanced visualizations?** Explore the skill or ask the expert for specific patterns!
