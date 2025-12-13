# LayerChart Plugin Overview

Comprehensive patterns and advanced techniques for data visualization with LayerChart.

## Plugin Structure

```
.claude-plugin/layerchart/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── agents/
│   └── layerchart-expert.md     # Expert subagent for implementation guidance
├── skills/
│   └── layerchart/
│       └── SKILL.md             # Comprehensive skill documentation
├── README.md                     # Plugin overview
├── QUICK_START.md                # 5-minute getting started
└── PLUGIN_OVERVIEW.md            # This file (architecture & patterns)
```

## LayerChart Architecture

### Component Hierarchy

```
LayerChart (Container)
├── SVG Canvas
│   ├── Background/Grid
│   ├── Axes (X, Y)
│   ├── Plot Area
│   │   ├── Data Elements (lines, bars, etc.)
│   │   └── Interactive Overlays
│   ├── Legend
│   └── Annotations
└── Tooltip Container
```

### Built on Layer Cake

LayerChart is built on **Layer Cake**, a headless visualization framework that handles:
- **Scale Calculations** - Map data dimensions to visual dimensions
- **Coordinate Transforms** - Convert data to canvas coordinates
- **Responsive Sizing** - Adapt to container dimensions
- **Accessibility** - ARIA labels and semantic HTML

## Common Patterns

### 1. Basic Chart Pattern

**When to use:** Standard charts with default styling

```svelte
<script lang="ts">
  import { LineChart } from 'layerchart';

  interface DataPoint {
    x: string | number;
    y: number;
  }

  let data: DataPoint[] = [
    { x: 'Jan', y: 100 },
    { x: 'Feb', y: 120 }
  ];
</script>

<LineChart
  {data}
  xKey="x"
  yKey="y"
  width={800}
  height={400}
/>
```

### 2. Multi-Series Pattern

**When to use:** Comparing multiple data series

```svelte
<script lang="ts">
  interface Series {
    label: string;
    data: Array<{ month: string; value: number }>;
  }

  let series: Series[] = [
    {
      label: 'Product A',
      data: [{ month: 'Jan', value: 100 }, ...]
    },
    {
      label: 'Product B',
      data: [{ month: 'Jan', value: 80 }, ...]
    }
  ];
</script>

<!-- Option 1: Separate charts -->
{#each series as s}
  <LineChart
    data={s.data}
    xKey="month"
    yKey="value"
    title={s.label}
  />
{/each}

<!-- Option 2: Combined chart -->
<LineChart
  data={flattenedData}
  xKey="month"
  yKey="value"
  seriesKey="series"
  showLegend
/>
```

### 3. Data Transformation Pattern

**When to use:** Transform raw data before visualization

```typescript
interface RawData {
  date: string;
  events: Event[];
}

interface VisualizationData {
  date: string;
  count: number;
  unique_users: number;
}

function transformData(raw: RawData[]): VisualizationData[] {
  return raw.map(item => ({
    date: item.date,
    count: item.events.length,
    unique_users: new Set(item.events.map(e => e.user_id)).size
  }));
}

let chartData = transformData(rawData);
```

### 4. Reactive Data Pattern

**When to use:** Charts that update with changing data

```svelte
<script lang="ts">
  import { LineChart } from 'layerchart';

  let data = $state([...]);
  let timeRange = $state({ start: '2024-01-01', end: '2024-12-31' });

  // Reactive filter
  let filteredData = $derived(
    data.filter(d => d.date >= timeRange.start && d.date <= timeRange.end)
  );
</script>

<input type="date" bind:value={timeRange.start} />
<input type="date" bind:value={timeRange.end} />

<LineChart data={filteredData} xKey="date" yKey="value" />
```

### 5. Interactivity Pattern

**When to use:** Charts with user interactions

```svelte
<script lang="ts">
  import { LineChart } from 'layerchart';

  let data = [...];
  let selectedPoint = $state<DataPoint | null>(null);
  let hoveredDate = $state<string | null>(null);

  const handlePointSelect = (point: DataPoint) => {
    selectedPoint = point;
  };

  const handleHover = (date: string) => {
    hoveredDate = date;
  };
</script>

<LineChart
  {data}
  xKey="date"
  yKey="value"
  on:pointSelect={e => handlePointSelect(e.detail)}
  on:hover={e => handleHover(e.detail)}
  highlightDate={hoveredDate}
/>

{#if selectedPoint}
  <div class="details">
    <p>Date: {selectedPoint.date}</p>
    <p>Value: {selectedPoint.value}</p>
  </div>
{/if}
```

### 6. Responsive Container Pattern

**When to use:** Charts that adapt to container size

```svelte
<script>
  import { LineChart } from 'layerchart';
  import { resize } from 'svelte-5-action';

  let containerWidth = $state(800);
  let containerHeight = $state(400);

  let data = [...];
</script>

<div
  use:resize={({ width, height }) => {
    containerWidth = width;
    containerHeight = height;
  }}
  class="chart-container"
>
  <LineChart
    {data}
    xKey="date"
    yKey="value"
    width={containerWidth}
    height={containerHeight}
  />
</div>

<style>
  .chart-container {
    width: 100%;
    height: 100%;
  }
</style>
```

### 7. Dashboard Pattern

**When to use:** Multiple charts in a single dashboard

```svelte
<script lang="ts">
  import {
    LineChart,
    BarChart,
    PieChart
  } from 'layerchart';

  let revenue = [...];
  let categories = [...];
  let composition = [...];

  let dateRange = $state({ start: '2024-01-01', end: '2024-12-31' });

  // Filtered data for all charts
  let filtered = $derived({
    revenue: filterByDate(revenue, dateRange),
    categories: filterByDate(categories, dateRange),
    composition: composition  // Pie doesn't need date filtering
  });
</script>

<div class="dashboard">
  <div class="row">
    <div class="chart">
      <h3>Revenue Trend</h3>
      <LineChart
        data={filtered.revenue}
        xKey="date"
        yKey="amount"
      />
    </div>
    <div class="chart">
      <h3>Sales by Category</h3>
      <BarChart
        data={filtered.categories}
        xKey="category"
        yKey="sales"
      />
    </div>
  </div>
  <div class="row">
    <div class="chart">
      <h3>Market Share</h3>
      <PieChart
        data={filtered.composition}
        nameKey="product"
        valueKey="share"
      />
    </div>
  </div>
</div>

<style>
  .dashboard {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 20px;
  }

  .row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 20px;
  }

  .chart {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
  }
</style>
```

## Performance Patterns

### 1. Data Aggregation

**For large datasets (1000+ points), aggregate before visualization:**

```typescript
interface DailyData {
  date: string;
  value: number;
}

function aggregateByWeek(data: DailyData[]): DailyData[] {
  const weekly: Record<string, number[]> = {};

  data.forEach(point => {
    const week = getWeekStart(point.date);
    if (!weekly[week]) weekly[week] = [];
    weekly[week].push(point.value);
  });

  return Object.entries(weekly).map(([week, values]) => ({
    date: week,
    value: values.reduce((a, b) => a + b) / values.length
  }));
}

let displayData = $derived(
  data.length > 1000 ? aggregateByWeek(data) : data
);
```

### 2. Memoization

**Prevent unnecessary re-renders:**

```svelte
<script lang="ts">
  let data = [...];
  let xKey = 'month';
  let yKey = 'value';

  // Only recalculate when inputs change
  let chartConfig = $derived({
    data,
    xKey,
    yKey,
    width: 800,
    height: 400
  });
</script>

<LineChart {...chartConfig} />
```

### 3. Virtual Scrolling

**For scrollable chart lists:**

```svelte
<script>
  import { VirtualList } from 'svelte-virtual';
  import { LineChart } from 'layerchart';

  let charts = [
    { id: 1, data: [...], title: 'Chart 1' },
    { id: 2, data: [...], title: 'Chart 2' },
    // ... many more
  ];
</script>

<VirtualList items={charts} let:item>
  <div class="chart-item">
    <h3>{item.title}</h3>
    <LineChart data={item.data} xKey="x" yKey="y" />
  </div>
</VirtualList>
```

## Chart Type Selection Guide

| Data Type | Best Chart | Use When |
|-----------|-----------|----------|
| Time-series | LineChart | Trends over time |
| Categorical | BarChart | Compare categories |
| Composition | PieChart | Show proportions |
| Distribution | AreaChart | Cumulative values |
| Correlation | ScatterPlot | X/Y relationships |
| Hierarchy | SunburstChart | Tree structures |
| Geographic | ChoroplethMap | Regional data |
| Network | (Use Layer Cake) | Connection flows |

## Integration Patterns

### With Tailwind CSS

```svelte
<div class="w-full h-screen p-4 bg-gray-50">
  <div class="bg-white rounded-lg shadow-md p-6">
    <h2 class="text-2xl font-bold mb-4">Sales Dashboard</h2>
    <LineChart
      {data}
      xKey="month"
      yKey="sales"
      class="w-full"
    />
  </div>
</div>
```

### With shadcn-svelte Components

```svelte
<script>
  import { Card, Button, Select } from 'shadcn-svelte';
  import { LineChart } from 'layerchart';
</script>

<Card>
  <Card.Header>
    <Card.Title>Revenue Analysis</Card.Title>
    <div class="flex gap-2">
      <Select bind:value={metric}>
        <option value="revenue">Revenue</option>
        <option value="profit">Profit</option>
      </Select>
      <Button on:click={exportChart}>Export</Button>
    </div>
  </Card.Header>
  <Card.Content>
    <LineChart data={filteredData} xKey="date" yKey={metric} />
  </Card.Content>
</Card>
```

### With SvelteKit

```typescript
// src/routes/api/chart-data/+server.ts
import { json } from '@sveltejs/kit';

export async function GET({ url }) {
  const metric = url.searchParams.get('metric');
  const data = await db.query(metric);
  return json(data);
}
```

```svelte
<!-- src/routes/dashboard/+page.svelte -->
<script>
  import { LineChart } from 'layerchart';
  import type { PageData } from './$types';

  export let data: PageData;
</script>

<LineChart data={data.chartData} xKey="date" yKey="value" />
```

## Advanced Customization

### Custom Tooltips

```svelte
<LineChart
  {data}
  xKey="month"
  yKey="value"
  tooltipFormatter={(point) => `${point.month}: $${point.value.toLocaleString()}`}
/>
```

### Axis Formatting

```svelte
<BarChart
  {data}
  xKey="category"
  yKey="amount"
  yAxisFormatter={(value) => `$${(value / 1000).toFixed(1)}k`}
/>
```

### Conditional Styling

```svelte
<script>
  let getColor = (value: number) => {
    if (value > 10000) return '#4caf50';
    if (value > 5000) return '#ff9800';
    return '#f44336';
  };
</script>

<BarChart
  {data}
  xKey="category"
  yKey="value"
  barColor={getColor}
/>
```

## Troubleshooting Guide

### Chart Rendering Issues

**Issue:** Chart not displaying
- Verify data array is not empty
- Check xKey/yKey match data structure
- Ensure width/height are specified

**Issue:** Axes not showing
- Check scale range is valid (not NaN)
- Verify data includes both numbers and strings as needed

**Issue:** Performance degradation with large datasets
- Aggregate data (see Performance Patterns section)
- Reduce animation duration
- Use virtual scrolling for multiple charts

### Data Issues

**Issue:** Wrong data displayed
- Verify data transformation logic
- Check date format consistency
- Ensure numeric values are valid numbers

**Issue:** Tooltips showing wrong values
- Verify data structure in tooltipFormatter
- Check decimal precision settings

## Best Practices

1. **Data Validation**
   - Always validate data before visualization
   - Handle missing/null values explicitly
   - Test with edge cases (empty, single point, outliers)

2. **Accessibility**
   - Always include axis labels
   - Provide data in table format as fallback
   - Use color + pattern for colorblind accessibility

3. **Performance**
   - Aggregate large datasets
   - Use appropriate chart types for data size
   - Lazy load charts below the fold

4. **User Experience**
   - Match data granularity to use case
   - Provide context (titles, labels, units)
   - Enable interactivity for exploration

5. **Responsive Design**
   - Use container queries for sizing
   - Test on mobile and tablet
   - Adjust animation for touch devices

## Resources

- Full documentation: See the `layerchart-skills` skill
- Expert guidance: Ask `layerchart-expert` agent
- Layer Cake framework: https://layercake.graphics
- D3.js utilities: https://d3js.org/

---

**Building data visualizations?** Consult the skill for specific chart types and the expert for optimization strategies!
