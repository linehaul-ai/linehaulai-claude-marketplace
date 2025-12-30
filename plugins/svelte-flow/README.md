# Svelte Flow Plugin

**Build interactive node-based editors, flow diagrams, and flow visualizations with Svelte Flow.**

This plugin provides comprehensive guidance for creating interactive node-based UIs using Svelte Flow (@xyflow/svelte). Perfect for workflow editors, data flow diagrams, organizational charts, mindmaps, process visualizations, and DAG editors.

## What You Get

### Skills
- **svelte-flow** - Expert guide covering installation, core setup, nodes/edges, handles, custom components, layouts, events, and performance

### Agents
- **svelte-flow-expert** - Specialized consultant for node/edge architecture, layout algorithms, custom components, and performance optimization

### Commands
- **`/create-editor`** - Orchestrate interactive editor setup with requirement analysis and code generation

## Use Cases

- **Workflow Editors** - Visual workflow builder with step-by-step processes
- **Data Flow Diagrams** - Visualize data transformations and pipelines
- **Organizational Charts** - Display hierarchical structures and relationships
- **Mindmaps** - Create expandable mind maps and concept visualizations
- **DAG Editors** - Build and validate Directed Acyclic Graphs
- **Process Visualizations** - Diagram complex processes and procedures

## Quick Start

To create a simple node-based editor:

```bash
/create-editor Create a simple workflow editor with:
- Step nodes for workflow actions
- Conditional decision nodes
- Edge connections with labels
- Drag-and-drop interactions
```

Or use the skill directly to understand Svelte Flow concepts:

```
I want to build a node-based editor for my app. What are the key components I need?
```

The svelte-flow skill and svelte-flow-expert agent will provide detailed guidance.

## Key Features

### Node Management
- Create, position, and manage nodes in the canvas
- Built-in node types: default, input, output
- Custom node components with any design
- Handle-based connection points
- Automatic sizing and styling

### Edge Management
- Connect nodes with multiple edge types: default, smoothstep, step, straight, bezier
- Animated edges for visual feedback
- Custom edge labels and styling
- Marker ends for directional flow
- Edge validation and constraints

### Layout Algorithms
- **Dagre** - Best for Directed Acyclic Graphs (DAGs)
- **Hierarchical** - Organize nodes in levels
- **Manual** - Explicit positioning
- Auto-layout on node addition/removal

### Interaction Patterns
- Drag nodes to reposition
- Zoom and pan the canvas
- Select single or multiple nodes
- Keyboard shortcuts for productivity
- Touch support for mobile

### Performance
- Handles 1000+ nodes efficiently
- Viewport-based rendering optimization
- Memoized node/edge components
- Configurable re-render cycles

## Installation & Setup

See the [QUICK_START.md](./QUICK_START.md) for a 5-minute setup guide.

## Architecture

See [PLUGIN_OVERVIEW.md](./PLUGIN_OVERVIEW.md) for detailed architecture, patterns, and best practices.

## Integration

This plugin works with:
- **Svelte/SvelteKit** - Full SPA or SSR environments
- **Tailwind CSS** - For styling custom nodes/edges
- **TypeScript** - Type-safe node/edge definitions
- **Bun/Vite** - Build tool integration
- **shadcn-svelte** - UI component library (for custom nodes)

## Dependencies

- `@xyflow/svelte` v11+
- `svelte` v5+
- `typescript` (recommended)

## Example Applications

### Workflow Engine
```typescript
interface WorkflowNode {
  id: string;
  type: 'step' | 'condition' | 'merge';
  title: string;
  position: { x: number; y: number };
}
```

### Data Pipeline
```typescript
interface PipelineNode {
  id: string;
  type: 'source' | 'transform' | 'sink';
  operation: string;
  position: { x: number; y: number };
}
```

### Organization Chart
```typescript
interface OrgNode {
  id: string;
  name: string;
  title: string;
  department: string;
  position: { x: number; y: number };
}
```

## Support

- **Skill**: Use the `svelte-flow` skill for comprehensive documentation
- **Expert**: Ask the `svelte-flow-expert` agent for implementation guidance
- **Command**: Use `/create-editor` to orchestrate new editor setups
- **Community**: Check Svelte Flow docs at https://svelteflow.dev

## Next Steps

1. Read [QUICK_START.md](./QUICK_START.md) for basic setup
2. Explore the `svelte-flow` skill for detailed concepts
3. Use `/create-editor` command for scaffolding new editors
4. Consult `svelte-flow-expert` agent for complex implementations
5. Reference [PLUGIN_OVERVIEW.md](./PLUGIN_OVERVIEW.md) for patterns

---

**Ready to build interactive flow editors?** Start with `/create-editor` or explore the svelte-flow skill!
