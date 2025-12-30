# LayerChart Plugin

**Pre-built, high-level chart components for rapid data visualization.**

This plugin provides comprehensive guidance for building diverse data visualizations using LayerChart - a component library built on the Layer Cake framework. Rapidly create professional, interactive charts with minimal configuration.

## What You Get

### Skills
- **layerchart-skills** - Expert guide covering component types, composition patterns, data binding, styling, and performance optimization

### Agents
- **layerchart-expert** - Specialized consultant for chart selection, data transformation, and implementation patterns

## Use Cases

- **Business Dashboards** - KPI tracking, metrics visualization, performance monitoring
- **Analytics** - Time-series analysis, distribution charts, cohort comparisons
- **Finance** - Stock charts, portfolio analysis, budget visualization
- **Scientific Data** - Experimental results, multi-dimensional analysis
- **Real-time Monitoring** - Live data streams, performance metrics
- **Reports** - Data-rich documents, automated chart generation

## Chart Types Supported

### Cartesian Charts
- **Bar Charts** - Horizontal and vertical, stacked, grouped
- **Line Charts** - Single/multi-line, area under curves, confidence intervals
- **Area Charts** - Stacked, normalized, streamgraph
- **Scatter Plots** - Bubble charts, regression lines
- **Combo Charts** - Mixed bar/line/area visualizations

### Radial Charts
- **Pie Charts** - Standard, donut, sunburst (hierarchical)
- **Gauges** - Dial gauges, bullet graphs
- **Polar Charts** - Wind rose, radar charts

### Hierarchical Charts
- **Tree Maps** - Nested rectangles for hierarchical data
- **Sunburst** - Radial tree visualization
- **Dendrograms** - Hierarchical clustering visualization

### Geographic Charts
- **Choropleth Maps** - Color-coded regions
- **Bubble Maps** - Geographic bubble scatter plots
- **Flow Maps** - Network flows by geography

## Quick Start

### 1. Choose Your Chart

```typescript
// Time-series line chart
import { LineChart } from 'layerchart';

let data = [
  { date: '2024-01-01', value: 100 },
  { date: '2024-01-02', value: 120 },
  // ...
];
```

### 2. Add to Component

```svelte
<LineChart
  {data}
  xKey="date"
  yKey="value"
  width={800}
  height={400}
/>
```

### 3. Customize

```svelte
<LineChart
  {data}
  xKey="date"
  yKey="value"
  title="Monthly Revenue"
  yAxisLabel="Revenue ($)"
  color="#4CAF50"
/>
```

## Key Features

### Pre-built Components
- **Plug-and-Play** - Components work out of the box with sensible defaults
- **Responsive** - Adapt to container size automatically
- **Accessible** - ARIA labels and keyboard navigation built-in
- **Themeable** - Customize colors, fonts, spacing with simple props

### Data Binding
- **Reactive** - Charts update automatically when data changes
- **Flexible** - Support arrays, reactive stores, live streams
- **Transformable** - Built-in data aggregation and grouping

### Interactivity
- **Hover Details** - Tooltips show detailed information
- **Selection** - Click to select/highlight data points
- **Legends** - Toggle series visibility
- **Zoom/Pan** - Explore detailed regions

### Performance
- **Optimized Rendering** - SVG virtualization for large datasets
- **Smooth Animations** - Transitions between data states
- **Memory Efficient** - Only render visible elements

## Examples

### Sales Dashboard
```svelte
<script>
  import { BarChart, LineChart } from 'layerchart';

  let salesData = [...];
  let trendData = [...];
</script>

<div class="dashboard">
  <BarChart data={salesData} xKey="month" yKey="sales" />
  <LineChart data={trendData} xKey="date" yKey="trend" />
</div>
```

### Real-time Monitoring
```svelte
<script>
  let metrics = $state([]);

  // Update from API
  setInterval(async () => {
    metrics = await fetch('/api/metrics').then(r => r.json());
  }, 1000);
</script>

<LineChart data={metrics} xKey="timestamp" yKey="value" />
```

### Hierarchical Data
```svelte
<SunburstChart
  data={fileSystemData}
  name="size"
  children="files"
/>
```

## Installation

See [QUICK_START.md](./QUICK_START.md) for a 5-minute setup guide.

## Architecture & Patterns

See [PLUGIN_OVERVIEW.md](./PLUGIN_OVERVIEW.md) for detailed patterns, composition strategies, and performance optimization.

## Integration

This plugin works with:
- **Svelte/SvelteKit** - Full SPA or SSR environments
- **Layer Cake** - The underlying visualization framework
- **Tailwind CSS** - For styling and layout
- **TypeScript** - Type-safe component props
- **D3.js** - Compatible with D3 scales and utilities

## Dependencies

- `layer-cake` v2.0+
- `svelte` v5+
- `d3` (optional, for scales and utilities)

## Comparison: LayerChart vs Layer Cake

| Aspect | LayerChart | Layer Cake |
|--------|-----------|-----------|
| **Learning Curve** | Shallow (pre-built) | Steep (framework) |
| **Development Speed** | Fast (components) | Slower (custom) |
| **Customization** | Limited | Unlimited |
| **Best For** | Standard charts, dashboards | Custom, unique visualizations |
| **Code Volume** | 20-30 lines | 100-300 lines |

## Support

- **Skill**: Use the `layerchart-skills` skill for comprehensive documentation
- **Expert**: Ask the `layerchart-expert` agent for implementation guidance
- **Community**: Check Layer Cake docs at https://layercake.graphics
- **Examples**: Explore chart examples in QUICK_START.md

## Next Steps

1. Read [QUICK_START.md](./QUICK_START.md) for basic chart setup
2. Explore the `layerchart-skills` skill for all chart types
3. Consult `layerchart-expert` agent for optimization strategies
4. Reference [PLUGIN_OVERVIEW.md](./PLUGIN_OVERVIEW.md) for patterns
5. Check out Layer Cake documentation for advanced customization

---

**Ready to build data visualizations?** Start with a simple chart in [QUICK_START.md](./QUICK_START.md)!
