# /create-editor

Create an interactive node-based editor or diagram using Svelte Flow

## Description

This command orchestrates the creation of interactive flow editors, data diagrams, organizational charts, mindmaps, and process visualizations using Svelte Flow (@xyflow/svelte).

## Usage

```bash
/create-editor [requirements]
```

## Examples

### Example 1: Workflow Editor
```bash
/create-editor Create a workflow editor where users can:
- Add/delete nodes for workflow steps
- Connect nodes with edges to define flow
- Support conditional branching nodes
- Auto-layout when adding new nodes
- Persist workflow state to localStorage
- Validate connections (no circular dependencies)
```

### Example 2: Data Flow Diagram
```bash
/create-editor Build a data flow diagram showing:
- Data source nodes (databases, APIs)
- Processing nodes (transformations)
- Sink nodes (destinations)
- Edges with data type labels
- Color-coded nodes by type
- Auto-layout using dagre algorithm
```

### Example 3: Organizational Chart
```bash
/create-editor Design an org chart visualizer:
- Display employee nodes in hierarchy
- Manager-subordinate relationships as edges
- Expandable/collapsible departments
- Search and filter employees
- Department-based coloring
- Hierarchical layout algorithm
```

## What This Command Does

1. **Analyzes Requirements** - Determines the type of editor (workflow, diagram, chart, etc.)

2. **Recommends Components**
   - Appropriate node types and shapes
   - Edge types for connections
   - Layout algorithms (dagre, hierarchical, manual)
   - Interaction patterns (drag, zoom, selection)

3. **Generates Architecture**
   - Svelte component structure
   - State management approach
   - Event handling setup
   - Performance considerations

4. **Provides Implementation**
   - Custom node component templates
   - Edge styling and animation
   - Connection validation logic
   - Persistence strategies

5. **Offers Next Steps**
   - Advanced features (undo/redo, search)
   - Styling and theming
   - Export/import functionality
   - Performance optimization

## Integration

This command invokes the `svelte-flow-expert` agent to:
- Validate requirements for feasibility
- Design node/edge structures
- Recommend layout algorithms
- Optimize for performance
- Suggest interaction patterns

## Common Patterns

### Workflow Editors
- Suitable node types: step, condition, merge, split, end
- Common edges: default, smoothstep (curved)
- Layout: dagre (Directed Acyclic Graph)
- Validation: cycle detection

### Diagrams
- Suitable node types: custom shapes per domain
- Common edges: bezier, straight
- Layout: hierarchical or manual
- Styling: color-coded by category

### Organizational Charts
- Suitable node types: person cards
- Common edges: clean lines
- Layout: hierarchical (top-down)
- Interaction: expandable groups

## Tips

- Define clear node types before building custom components
- Choose layout algorithm based on data structure (tree, DAG, cyclic)
- Consider performance for graphs with 100+ nodes
- Use handles for connection points on custom nodes
- Validate connections to maintain data integrity

## See Also

- `svelte-flow` skill - Comprehensive Svelte Flow documentation
- `svelte-flow-expert` agent - Implementation guidance
- Svelte Flow docs - https://svelteflow.dev
