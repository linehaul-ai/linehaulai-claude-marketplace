# LayerChart Quick Start (5 Minutes)

Create your first data visualization in 5 minutes.

## Step 1: Install Dependencies

```bash
npm install layer-cake d3
# or with bun:
bun add layer-cake d3
```

## Step 2: Create a Line Chart

Create `src/lib/SalesChart.svelte`:

```svelte
<script lang="ts">
  import { LineChart } from 'layerchart';

  // Sample data
  let data = [
    { month: 'Jan', sales: 4000 },
    { month: 'Feb', sales: 3000 },
    { month: 'Mar', sales: 2000 },
    { month: 'Apr', sales: 2780 },
    { month: 'May', sales: 1890 },
    { month: 'Jun', sales: 2390 }
  ];
</script>

<div class="chart-container">
  <LineChart
    {data}
    xKey="month"
    yKey="sales"
    width={800}
    height={400}
    title="Monthly Sales"
  />
</div>

<style>
  .chart-container {
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 20px;
  }
</style>
```

## Step 3: Use in Your App

Import and use the component:

```svelte
<!-- src/routes/+page.svelte -->
<script>
  import SalesChart from '$lib/SalesChart.svelte';
</script>

<main>
  <h1>Sales Dashboard</h1>
  <SalesChart />
</main>
```

## Step 4: Add a Bar Chart

```svelte
<script>
  import { BarChart, LineChart } from 'layerchart';

  let salesData = [...];
  let categoryData = [
    { category: 'Product A', revenue: 12000 },
    { category: 'Product B', revenue: 8500 },
    { category: 'Product C', revenue: 15200 }
  ];
</script>

<div class="dashboard">
  <LineChart data={salesData} xKey="month" yKey="sales" />
  <BarChart data={categoryData} xKey="category" yKey="revenue" />
</div>
```

## Step 5: Make It Interactive

```svelte
<script>
  import { LineChart } from 'layerchart';

  let data = $state([...]);
  let selectedPoint = $state<any>(null);

  const handlePointClick = (point: any) => {
    selectedPoint = point;
  };
</script>

<LineChart
  {data}
  xKey="month"
  yKey="sales"
  on:pointSelect={e => handlePointClick(e.detail)}
/>

{#if selectedPoint}
  <p>Selected: {selectedPoint.month} - ${selectedPoint.sales}</p>
{/if}
```

## Done! 🎉

You now have:
- ✅ Line chart showing trends
- ✅ Bar chart for comparisons
- ✅ Responsive, auto-sizing charts
- ✅ Interactive tooltips
- ✅ Professional styling

## Chart Types

### Quick Reference

| Chart Type | Use Case | Example |
|-----------|----------|---------|
| **LineChart** | Trends over time | Stock prices, temperature |
| **BarChart** | Comparisons | Sales by region, survey results |
| **AreaChart** | Cumulative trends | Stacked metrics, resource usage |
| **ScatterPlot** | Correlations | X/Y relationships, clusters |
| **PieChart** | Composition | Market share, budget breakdown |
| **SunburstChart** | Hierarchies | File system, org structure |

### Next: Try Different Charts

```svelte
<!-- Area Chart -->
<AreaChart
  {data}
  xKey="month"
  yKey="sales"
  fill="rgba(76, 175, 80, 0.3)"
/>

<!-- Pie Chart -->
<PieChart
  data={[
    { name: 'A', value: 35 },
    { name: 'B', value: 25 },
    { name: 'C', value: 40 }
  ]}
  nameKey="name"
  valueKey="value"
/>

<!-- Scatter Plot -->
<ScatterPlot
  data={pointData}
  xKey="x"
  yKey="y"
  sizeKey="size"
/>
```

## Common Customizations

### Add Axis Labels

```svelte
<LineChart
  {data}
  xKey="month"
  yKey="sales"
  xAxisLabel="Month"
  yAxisLabel="Sales ($)"
/>
```

### Change Colors

```svelte
<BarChart
  {data}
  xKey="category"
  yKey="value"
  color="#ff6b6b"
  secondaryColor="#4ecdc4"
/>
```

### Add Legends

```svelte
<LineChart
  {data}
  xKey="month"
  yKey="sales"
  showLegend={true}
  legendPosition="bottom"
/>
```

### Responsive Sizing

```svelte
<script>
  let containerWidth = $state(0);
  let containerHeight = $state(400);
</script>

<div bind:clientWidth={containerWidth}>
  <LineChart
    {data}
    xKey="month"
    yKey="sales"
    width={containerWidth}
    height={containerHeight}
  />
</div>
```

## Troubleshooting

**Q: Chart not showing**
A: Verify data structure matches xKey/yKey props and has at least 2 data points.

**Q: Axes labels overlapping**
A: Increase width/height or rotate labels with `xAxisRotate={45}` prop.

**Q: Performance slow with large datasets**
A: Use data aggregation (see PLUGIN_OVERVIEW.md) or consider Layer Cake for custom rendering.

**Q: Colors don't match design**
A: Use the `color` and `secondaryColor` props to match your theme.

## Real-World Examples

### Sales Dashboard
```svelte
<script>
  import { BarChart, LineChart } from 'layerchart';

  let monthly = fetch('/api/monthly-sales').then(r => r.json());
  let categories = fetch('/api/category-totals').then(r => r.json());
</script>

<h1>Sales Dashboard</h1>
<LineChart data={monthly} xKey="month" yKey="sales" />
<BarChart data={categories} xKey="category" yKey="total" />
```

### Real-time Metrics
```svelte
<script>
  let metrics = $state([]);

  setInterval(async () => {
    metrics = await fetch('/api/metrics').then(r => r.json());
  }, 5000);
</script>

<LineChart
  data={metrics}
  xKey="timestamp"
  yKey="cpu_usage"
  title="CPU Usage (%)"
/>
```

### Data Exploration
```svelte
<script>
  let data = $state([]);
  let selectedCategory = $state('all');

  const filtered = selectedCategory === 'all'
    ? data
    : data.filter(d => d.category === selectedCategory);
</script>

<select bind:value={selectedCategory}>
  <option value="all">All Categories</option>
  <option value="A">Category A</option>
  <option value="B">Category B</option>
</select>

<ScatterPlot {data: filtered} xKey="x" yKey="y" sizeKey="size" />
```

## Next Steps

1. **Explore More Charts** - See the `layerchart-skills` skill for all chart types
2. **Get Expert Help** - Ask `layerchart-expert` for specific use cases
3. **Optimize Performance** - Read PLUGIN_OVERVIEW.md for large dataset handling
4. **Customize Further** - Check Layer Cake docs for advanced customization
5. **Build Dashboards** - Combine multiple charts in a single page

## Resources

- Full documentation: See the `layerchart-skills` skill
- Expert guidance: Ask the `layerchart-expert` agent
- Detailed patterns: See PLUGIN_OVERVIEW.md
- Official docs: https://layercake.graphics
