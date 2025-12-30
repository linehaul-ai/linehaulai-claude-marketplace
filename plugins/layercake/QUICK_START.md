# Layer Cake Quick Start (5 Minutes)

Build your first custom visualization in 5 minutes.

## Step 1: Understand the Concept

Layer Cake provides three things:
1. **Scales** - Convert data to pixels (e.g., value 50 → pixel 250)
2. **Dimensions** - Define the chart area
3. **Reactivity** - Automatically update when data changes

You provide:
- **SVG/Canvas elements** - What to draw
- **Your components** - How it looks
- **Styling** - Your design

## Step 2: Install Dependencies

```bash
npm install d3-scale
# or with bun:
bun add d3-scale
```

## Step 3: Create a Basic Line Chart

Create `src/lib/LineChart.svelte`:

```svelte
<script lang="ts">
  import { scaleLinear } from 'd3-scale';

  // Data
  let data = [
    { x: 0, y: 10 },
    { x: 1, y: 25 },
    { x: 2, y: 15 },
    { x: 3, y: 30 },
    { x: 4, y: 20 }
  ];

  const width = 400;
  const height = 300;
  const padding = 40;

  // Create scales
  $: xScale = scaleLinear()
    .domain([0, data.length - 1])
    .range([padding, width - padding]);

  $: yScale = scaleLinear()
    .domain([0, Math.max(...data.map(d => d.y))])
    .range([height - padding, padding]);

  // Create path string for line
  $: pathData = data
    .map((d, i) => `${xScale(i)},${yScale(d.y)}`)
    .join(' L ');
</script>

<svg {width} {height} style="border: 1px solid #ccc">
  <!-- Y-axis -->
  <line x1={padding} y1={padding} x2={padding} y2={height - padding} stroke="black" />

  <!-- X-axis -->
  <line x1={padding} y1={height - padding} x2={width - padding} y2={height - padding} stroke="black" />

  <!-- Line -->
  <polyline points={pathData} fill="none" stroke="blue" stroke-width="2" />

  <!-- Data points -->
  {#each data as d, i}
    <circle cx={xScale(i)} cy={yScale(d.y)} r="3" fill="blue" />
  {/each}

  <!-- X-axis labels -->
  {#each data as d, i}
    <text x={xScale(i)} y={height - 20} text-anchor="middle" font-size="12">
      {i}
    </text>
  {/each}

  <!-- Y-axis labels -->
  {#each [0, 10, 20, 30, 40] as tick}
    <text x={padding - 5} y={yScale(tick) + 5} text-anchor="end" font-size="12">
      {tick}
    </text>
  {/each}
</svg>

<style>
  svg {
    background: #f9f9f9;
  }
</style>
```

## Step 4: Use in Your App

```svelte
<!-- src/routes/+page.svelte -->
<script>
  import LineChart from '$lib/LineChart.svelte';
</script>

<main>
  <h1>My First Layer Cake Chart</h1>
  <LineChart />
</main>
```

## Step 5: Make It Reactive

```svelte
<script lang="ts">
  import { scaleLinear } from 'd3-scale';

  let data = $state([
    { x: 0, y: 10 },
    { x: 1, y: 25 },
    { x: 2, y: 15 },
    { x: 3, y: 30 },
    { x: 4, y: 20 }
  ]);

  let newValue = $state(0);

  const addPoint = () => {
    data = [
      ...data,
      {
        x: data.length,
        y: newValue
      }
    ];
    newValue = 0;
  };

  // ... scales and rendering ...
</script>

<input type="number" bind:value={newValue} />
<button on:click={addPoint}>Add Point</button>

<svg>
  <!-- ... -->
</svg>
```

## Done! 🎉

You've created a custom line chart with:
- ✅ Data to pixel conversion (scales)
- ✅ SVG rendering
- ✅ Axes and labels
- ✅ Reactive data updates
- ✅ Interactive features

## Key Concepts

### Scales

```typescript
const xScale = scaleLinear()
  .domain([0, 100])      // Input data range
  .range([0, 800]);      // Output pixel range

// Convert: value 50 → pixel 400
const pixel = xScale(50);
```

### Dimensions

```typescript
const width = 800;
const height = 400;
const padding = 40;

const innerWidth = width - padding * 2;
const innerHeight = height - padding * 2;
```

### Data Binding

```svelte
<script>
  let data = $state([...]);

  // Automatically recalculate when data changes
  $: max = Math.max(...data.map(d => d.y));
  $: yScale = scaleLinear().domain([0, max]).range([...]);
</script>

<!-- SVG updates automatically -->
<svg>
  {#each data as point}
    <circle cy={yScale(point.y)} />
  {/each}
</svg>
```

## Common Patterns

### Scatter Plot

```svelte
<script>
  import { scaleLinear } from 'd3-scale';

  let data = [
    { x: 10, y: 20 },
    { x: 30, y: 40 },
    // ...
  ];

  $: xScale = scaleLinear()
    .domain([0, 50])
    .range([40, 360]);

  $: yScale = scaleLinear()
    .domain([0, 50])
    .range([260, 40]);
</script>

<svg width="400" height="300">
  {#each data as d}
    <circle
      cx={xScale(d.x)}
      cy={yScale(d.y)}
      r="4"
      fill="blue"
    />
  {/each}
</svg>
```

### Bar Chart

```svelte
<script>
  import { scaleBand, scaleLinear } from 'd3-scale';

  let data = [
    { name: 'A', value: 30 },
    { name: 'B', value: 45 },
    { name: 'C', value: 20 }
  ];

  $: xScale = scaleBand()
    .domain(data.map(d => d.name))
    .range([40, 360])
    .padding(0.1);

  $: yScale = scaleLinear()
    .domain([0, 50])
    .range([260, 40]);
</script>

<svg width="400" height="300">
  {#each data as d}
    <rect
      x={xScale(d.name)}
      y={yScale(d.value)}
      width={xScale.bandwidth()}
      height={260 - yScale(d.value)}
      fill="steelblue"
    />
  {/each}
</svg>
```

### Interactive Selection

```svelte
<script>
  let data = [...];
  let selected = $state<DataPoint | null>(null);

  const handleClick = (point: DataPoint) => {
    selected = point;
  };
</script>

<svg>
  {#each data as point}
    <circle
      cx={xScale(point.x)}
      cy={yScale(point.y)}
      r={selected === point ? 8 : 4}
      fill={selected === point ? 'red' : 'blue'}
      on:click={() => handleClick(point)}
      style="cursor: pointer"
    />
  {/each}
</svg>
```

## D3 Scales Quick Reference

```typescript
import {
  scaleLinear,    // Numeric to numeric
  scaleLog,       // Logarithmic scale
  scaleSqrt,      // Square root scale
  scaleTime,      // Date to numeric
  scaleBand,      // Categorical positioning
  scaleOrdinal,   // Discrete color mapping
  scaleSequential // Continuous color mapping
} from 'd3-scale';

// Linear: 0-100 → 0-800px
const x = scaleLinear().domain([0, 100]).range([0, 800]);

// Time: dates → 0-800px
const time = scaleTime()
  .domain([new Date('2024-01-01'), new Date('2024-12-31')])
  .range([0, 800]);

// Band: categories → positions with padding
const band = scaleBand()
  .domain(['A', 'B', 'C'])
  .range([0, 300])
  .padding(0.1);
```

## Troubleshooting

**Q: Values are off or inverted**
A: Remember y-axis is inverted in SVG (0 at top). Use `range([height - padding, padding])` for y-scale.

**Q: Chart not updating when data changes**
A: Make sure data is reactive with `$state` and scales use `$:` for reactivity.

**Q: Points/bars overlap**
A: Use `scaleBand` for categorical x-axis, adjust padding.

**Q: Text labels are hard to read**
A: Add `text-anchor` and positioning attributes to align labels.

## Next Steps

1. **Explore Scale Types** - Try `scaleTime`, `scaleBand`, `scaleLog`
2. **Add Axes** - Learn about D3 axis generators
3. **Add Tooltips** - Show values on hover
4. **Animations** - Use Svelte transitions for smooth updates
5. **Complex Charts** - Combine multiple visualizations

## Resources

- **Full guide**: See the `layercake-skills` skill for all concepts
- **Expert help**: Ask `layercake-expert` agent for specific patterns
- **D3 docs**: https://d3js.org
- **Advanced patterns**: See PLUGIN_OVERVIEW.md

---

**Ready to build advanced visualizations?** Check out the skill for comprehensive documentation!
