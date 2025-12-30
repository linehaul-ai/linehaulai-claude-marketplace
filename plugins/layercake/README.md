# Layer Cake Plugin

**Headless visualization framework for unlimited custom data visualizations.**

This plugin provides comprehensive guidance for building advanced, custom data visualizations using Layer Cake - a lightweight, unopinionated visualization framework. Perfect for unique chart types, complex interactions, and data-driven graphics.

## What You Get

### Skills
- **layercake-skills** - Expert guide covering core concepts, scales, dimensions, data transforms, custom rendering, and performance

### Agents
- **layercake-expert** - Specialized consultant for framework architecture, scale design, custom components, and optimization

## Philosophy

Layer Cake operates on a simple philosophy:

> **You bring the components. We handle the math.**

Layer Cake provides:
- ✅ Scale calculations (map data to visual dimensions)
- ✅ Coordinate transformations (data → canvas → screen)
- ✅ Responsive sizing and layout
- ✅ Reactive data binding

You provide:
- ✅ Custom SVG/Canvas/HTML/WebGL components
- ✅ Visual design (colors, shapes, interactions)
- ✅ Application logic (filtering, sorting, grouping)

## Use Cases

- **Unique Chart Types** - Visualizations that don't fit pre-built libraries
- **Complex Interactions** - Sophisticated user interactions and animations
- **Data Art** - Creative data visualization and storytelling
- **Scientific Visualization** - Custom plots for research and analysis
- **Real-time Dashboards** - Live updating custom visualizations
- **Specialized Domains** - Domain-specific chart types (financial, medical, etc.)

## Why Layer Cake vs LayerChart?

| Aspect | Layer Cake | LayerChart |
|--------|-----------|-----------|
| **Purpose** | Framework | Component Library |
| **Customization** | Unlimited | Limited to pre-built components |
| **Development Speed** | Slower (custom code) | Faster (use components) |
| **Learning Curve** | Steeper | Shallow |
| **Best For** | Unique visualizations | Standard charts |
| **Code Volume** | 100-500 lines | 10-50 lines |
| **Flexibility** | Maximum | Medium |

## Core Concepts

### 1. Scales
Convert data values to visual dimensions (pixels, angles, colors).

```typescript
import { scaleLinear } from 'd3-scale';

const xScale = scaleLinear()
  .domain([0, 100])
  .range([0, width]);

// Convert data value 50 → pixel position 250
const xPos = xScale(50);
```

### 2. Dimensions
Define visual space (width, height, margins).

```typescript
const dimensions = {
  width: 800,
  height: 400,
  marginTop: 20,
  marginRight: 30,
  marginBottom: 30,
  marginLeft: 60
};

// Inner chart area
const innerWidth = dimensions.width - dimensions.marginLeft - dimensions.marginRight;
const innerHeight = dimensions.height - dimensions.marginTop - dimensions.marginBottom;
```

### 3. Transforms
Convert between coordinate systems (data → pixel → SVG).

```typescript
// Data point
const dataPoint = { x: 50, y: 75 };

// Transform to pixel coordinates
const pixelX = xScale(dataPoint.x);
const pixelY = yScale(dataPoint.y);

// Rendered position
<circle cx={pixelX} cy={pixelY} r="4" />
```

### 4. Reactivity
Data changes automatically update the visualization.

```svelte
<script>
  let data = $state([...]);

  // Charts update automatically when data changes
  $effect(() => {
    console.log('Data changed:', data);
  });
</script>
```

## Quick Start Examples

### Line Chart from Scratch

```svelte
<script>
  import { scaleLinear, scaleTime } from 'd3-scale';

  let data = [
    { date: new Date('2024-01-01'), value: 100 },
    { date: new Date('2024-01-02'), value: 120 },
    // ...
  ];

  let width = 800, height = 400;

  $: xScale = scaleTime()
    .domain(d3.extent(data, d => d.date))
    .range([50, width - 20]);

  $: yScale = scaleLinear()
    .domain([0, d3.max(data, d => d.value)])
    .range([height - 20, 20]);

  $: line = d3.line()
    .x(d => xScale(d.date))
    .y(d => yScale(d.value));
</script>

<svg {width} {height}>
  <path d={line(data)} stroke="blue" fill="none" stroke-width="2" />

  {#each data as d}
    <circle
      cx={xScale(d.date)}
      cy={yScale(d.value)}
      r="3"
      fill="blue"
    />
  {/each}
</svg>
```

### Interactive Scatter Plot

```svelte
<script>
  import { scaleLinear } from 'd3-scale';

  let data = $state([...]);
  let selectedPoint = $state<DataPoint | null>(null);

  $: xScale = scaleLinear()
    .domain([...])
    .range([...]);

  $: yScale = scaleLinear()
    .domain([...])
    .range([...]);

  const handleClick = (point: DataPoint) => {
    selectedPoint = point;
  };
</script>

<svg>
  {#each data as point (point.id)}
    <circle
      cx={xScale(point.x)}
      cy={yScale(point.y)}
      r={selectedPoint?.id === point.id ? 8 : 4}
      fill={selectedPoint?.id === point.id ? 'red' : 'blue'}
      on:click={() => handleClick(point)}
      style="cursor: pointer"
    />
  {/each}
</svg>
```

## Integration

This plugin works with:
- **Svelte/SvelteKit** - Full framework integration
- **D3.js** - Scale and utilities
- **SVG** - Vector graphics rendering
- **Canvas** - Raster rendering
- **WebGL** - High-performance rendering
- **HTML/CSS** - DOM-based visualization

## Dependencies

- `svelte` v5+
- `d3` v7+ (optional but recommended)

## When to Use Layer Cake

Use Layer Cake when you need:
1. **Custom chart type** - Not available in pre-built libraries
2. **Complex interaction** - Beyond standard hover/selection
3. **Performance optimization** - Control over rendering
4. **Integration** - Part of larger application
5. **Unique design** - Specific visual requirements

## Examples

See [QUICK_START.md](./QUICK_START.md) for working examples.

## Architecture & Patterns

See [PLUGIN_OVERVIEW.md](./PLUGIN_OVERVIEW.md) for detailed architecture, patterns, and best practices.

## Learning Path

1. **Start Here** - Read [QUICK_START.md](./QUICK_START.md) for basic concepts
2. **Explore Skills** - Use `layercake-skills` skill for comprehensive documentation
3. **Get Expert Help** - Consult `layercake-expert` agent for specific patterns
4. **Study Patterns** - Reference [PLUGIN_OVERVIEW.md](./PLUGIN_OVERVIEW.md) for advanced techniques
5. **Build Projects** - Create custom visualizations using the patterns you've learned

## Support

- **Skill**: Use the `layercake-skills` skill for framework documentation
- **Expert**: Ask the `layercake-expert` agent for implementation guidance
- **Community**: Check Layer Cake docs at https://layercake.graphics
- **D3.js**: https://d3js.org for scale and utility functions

## Comparison with Related Libraries

| Library | Type | Use Case |
|---------|------|----------|
| **Layer Cake** | Framework | Custom visualizations |
| **LayerChart** | Components | Standard charts |
| **D3.js** | Library | Low-level DOM manipulation |
| **Plotly** | Components | Interactive web plots |
| **Observable Plot** | Components | Quick exploratory charts |

## Next Steps

1. Read [QUICK_START.md](./QUICK_START.md) for basic line chart
2. Explore the `layercake-skills` skill for all concepts
3. Build a simple custom visualization
4. Consult `layercake-expert` for optimization
5. Reference [PLUGIN_OVERVIEW.md](./PLUGIN_OVERVIEW.md) for patterns

---

**Ready to build custom visualizations?** Start with [QUICK_START.md](./QUICK_START.md) or explore the skill!
