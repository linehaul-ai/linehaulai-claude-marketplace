# Layer Cake Plugin Overview

Comprehensive architecture and advanced patterns for custom data visualization with Layer Cake.

## Plugin Structure

```
.claude-plugin/layercake/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── agents/
│   └── layercake-expert.md      # Expert subagent for implementation guidance
├── skills/
│   └── layercake/
│       └── SKILL.md             # Comprehensive skill documentation
├── README.md                     # Plugin overview
├── QUICK_START.md                # 5-minute getting started
└── PLUGIN_OVERVIEW.md            # This file (architecture & patterns)
```

## Layer Cake Philosophy

Layer Cake operates on a simple principle:

**You provide the components. We handle the math.**

### What Layer Cake Does
- ✅ Scale calculations (map data dimensions to visual dimensions)
- ✅ Coordinate transforms (data → pixel → screen)
- ✅ Responsive sizing and layout
- ✅ Reactive data binding
- ✅ SVG/Canvas/WebGL helpers

### What You Provide
- ✅ Component structure (your SVG/Canvas)
- ✅ Visual design (colors, shapes, styles)
- ✅ Interaction logic (click, hover, drag)
- ✅ Application features (filtering, sorting, grouping)

## Core Architecture

### 1. Scales

D3 scales are functions that map data values to visual values.

```typescript
import { scaleLinear, scaleTime, scaleBand } from 'd3-scale';

// Linear scale: data 0-100 → pixels 0-800
const xScale = scaleLinear()
  .domain([0, 100])
  .range([0, 800]);

// Time scale: dates → pixels
const timeScale = scaleTime()
  .domain([new Date('2024-01-01'), new Date('2024-12-31')])
  .range([0, 800]);

// Band scale: categories with spacing
const categoryScale = scaleBand()
  .domain(['A', 'B', 'C'])
  .range([0, 300])
  .padding(0.1);

// Usage
console.log(xScale(50));           // 400
console.log(categoryScale('A'));   // 0
console.log(categoryScale.bandwidth()); // ~90 (width of each bar)
```

### 2. Dimensions

Define the visual space for your chart.

```typescript
interface ChartDimensions {
  width: number;
  height: number;
  marginTop: number;
  marginRight: number;
  marginBottom: number;
  marginLeft: number;
}

const dimensions: ChartDimensions = {
  width: 800,
  height: 400,
  marginTop: 20,
  marginRight: 30,
  marginBottom: 30,
  marginLeft: 60
};

// Calculate inner dimensions (plotting area)
const innerWidth = dimensions.width - dimensions.marginLeft - dimensions.marginRight;
const innerHeight = dimensions.height - dimensions.marginTop - dimensions.marginBottom;
```

### 3. Data Transformation

Transform raw data into visualization-ready format.

```typescript
interface RawData {
  timestamp: string;
  value: number;
  category: string;
}

interface VisualizationData {
  date: Date;
  x: number;
  y: number;
  category: string;
  color: string;
}

function transformData(raw: RawData[]): VisualizationData[] {
  return raw.map((item, index) => ({
    date: new Date(item.timestamp),
    x: index,
    y: item.value,
    category: item.category,
    color: getColor(item.category)
  }));
}
```

### 4. Reactive Computation

Use Svelte's reactivity to automatically recalculate when data changes.

```svelte
<script lang="ts">
  import { scaleLinear } from 'd3-scale';

  let data = $state([...]);
  let selectedCategory = $state('all');

  // Filter data based on selection
  $: filtered = selectedCategory === 'all'
    ? data
    : data.filter(d => d.category === selectedCategory);

  // Recalculate scales when filtered data changes
  $: yDomain = [0, Math.max(...filtered.map(d => d.y)) || 100];
  $: yScale = scaleLinear()
    .domain(yDomain)
    .range([height - padding, padding]);

  // SVG updates automatically
</script>

<select bind:value={selectedCategory}>
  <option value="all">All Categories</option>
  <option value="A">Category A</option>
</select>

<svg>
  {#each filtered as d}
    <circle cx={xScale(d.x)} cy={yScale(d.y)} r="4" />
  {/each}
</svg>
```

## Common Patterns

### Pattern 1: Basic XY Chart

```svelte
<script lang="ts">
  import { scaleLinear } from 'd3-scale';

  interface Point {
    x: number;
    y: number;
  }

  let data: Point[] = [
    { x: 0, y: 10 },
    { x: 1, y: 20 },
    { x: 2, y: 15 }
  ];

  const width = 400, height = 300, padding = 40;

  $: xScale = scaleLinear()
    .domain([0, Math.max(...data.map(d => d.x))])
    .range([padding, width - padding]);

  $: yScale = scaleLinear()
    .domain([0, Math.max(...data.map(d => d.y))])
    .range([height - padding, padding]);
</script>

<svg {width} {height}>
  {#each data as point}
    <circle
      cx={xScale(point.x)}
      cy={yScale(point.y)}
      r="3"
      fill="blue"
    />
  {/each}
</svg>
```

### Pattern 2: Time Series

```svelte
<script lang="ts">
  import { scaleTime, scaleLinear } from 'd3-scale';
  import { timeParse } from 'd3-time-format';

  interface TimePoint {
    date: string;
    value: number;
  }

  let data: TimePoint[] = [
    { date: '2024-01-01', value: 100 },
    { date: '2024-01-02', value: 120 },
    // ...
  ];

  const parseDate = timeParse('%Y-%m-%d');

  $: xScale = scaleTime()
    .domain(d3.extent(data, d => parseDate(d.date)))
    .range([40, 760]);

  $: yScale = scaleLinear()
    .domain([0, Math.max(...data.map(d => d.value))])
    .range([260, 40]);

  $: line = d3.line()
    .x((d: TimePoint) => xScale(parseDate(d.date)))
    .y((d: TimePoint) => yScale(d.value));
</script>

<svg width="800" height="300">
  <path d={line(data)} stroke="blue" fill="none" stroke-width="2" />
</svg>
```

### Pattern 3: Categorical Bar Chart

```svelte
<script lang="ts">
  import { scaleBand, scaleLinear } from 'd3-scale';

  interface Category {
    name: string;
    value: number;
  }

  let data: Category[] = [
    { name: 'A', value: 30 },
    { name: 'B', value: 45 },
    { name: 'C', value: 20 }
  ];

  $: xScale = scaleBand()
    .domain(data.map(d => d.name))
    .range([40, 360])
    .padding(0.1);

  $: yScale = scaleLinear()
    .domain([0, Math.max(...data.map(d => d.value))])
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
    <text
      x={xScale(d.name) + xScale.bandwidth() / 2}
      y={280}
      text-anchor="middle"
    >
      {d.name}
    </text>
  {/each}
</svg>
```

### Pattern 4: Interactive Scatter Plot

```svelte
<script lang="ts">
  import { scaleLinear } from 'd3-scale';

  interface Point {
    id: string;
    x: number;
    y: number;
    category: string;
  }

  let data: Point[] = [...];
  let selected = $state<string | null>(null);
  let hovered = $state<string | null>(null);

  $: xScale = scaleLinear()
    .domain([0, 100])
    .range([40, 360]);

  $: yScale = scaleLinear()
    .domain([0, 100])
    .range([260, 40]);

  const handleClick = (id: string) => {
    selected = selected === id ? null : id;
  };

  const handleHover = (id: string | null) => {
    hovered = id;
  };

  const getColor = (point: Point) => {
    if (selected === point.id) return '#ff0000';
    if (hovered === point.id) return '#ff8800';
    return '#0066ff';
  };
</script>

<svg
  width="400"
  height="300"
  on:mouseleave={() => handleHover(null)}
>
  {#each data as point}
    <circle
      cx={xScale(point.x)}
      cy={yScale(point.y)}
      r={selected === point.id ? 6 : 4}
      fill={getColor(point)}
      on:click={() => handleClick(point.id)}
      on:mouseenter={() => handleHover(point.id)}
      style="cursor: pointer"
    />
  {/each}

  {#if selected}
    {@const p = data.find(d => d.id === selected)}
    <text x="200" y="20" text-anchor="middle">
      Selected: ({p?.x}, {p?.y})
    </text>
  {/if}
</svg>
```

### Pattern 5: Multi-Series Visualization

```svelte
<script lang="ts">
  import { scaleLinear } from 'd3-scale';

  interface Series {
    name: string;
    color: string;
    data: Array<{ x: number; y: number }>;
  }

  let series: Series[] = [
    {
      name: 'Product A',
      color: '#0066ff',
      data: [{ x: 0, y: 10 }, ...]
    },
    {
      name: 'Product B',
      color: '#ff6600',
      data: [{ x: 0, y: 15 }, ...]
    }
  ];

  $: allData = series.flatMap(s => s.data);

  $: xScale = scaleLinear()
    .domain([0, Math.max(...allData.map(d => d.x))])
    .range([40, 360]);

  $: yScale = scaleLinear()
    .domain([0, Math.max(...allData.map(d => d.y))])
    .range([260, 40]);
</script>

<svg width="400" height="300">
  {#each series as s}
    <g>
      {#each s.data as d, i}
        <circle
          cx={xScale(d.x)}
          cy={yScale(d.y)}
          r="3"
          fill={s.color}
        />
        {#if i < s.data.length - 1}
          <line
            x1={xScale(d.x)}
            y1={yScale(d.y)}
            x2={xScale(s.data[i + 1].x)}
            y2={yScale(s.data[i + 1].y)}
            stroke={s.color}
            stroke-width="2"
          />
        {/if}
      {/each}
    </g>
  {/each}

  <!-- Legend -->
  {#each series as s, i}
    <rect x="10" y={10 + i * 20} width="10" height="10" fill={s.color} />
    <text x="25" y="20" font-size="12">
      {s.name}
    </text>
  {/each}
</svg>
```

## D3 Utilities

### Scale Types

```typescript
import {
  scaleLinear,      // Maps numbers to numbers
  scaleLog,         // Logarithmic mapping
  scaleSqrt,        // Square root mapping
  scaleTime,        // Maps dates to numbers
  scaleBand,        // Maps categories to positions
  scaleOrdinal,     // Maps categories to discrete values
  scaleSequential   // Maps to color ranges
} from 'd3-scale';

// Linear
const x = scaleLinear().domain([0, 100]).range([0, 800]);

// Logarithmic (for data with wide range)
const log = scaleLog().domain([1, 1000]).range([0, 800]);

// Time (for dates)
const time = scaleTime()
  .domain([new Date(2024, 0, 1), new Date(2024, 11, 31)])
  .range([0, 800]);

// Band (for categories)
const band = scaleBand()
  .domain(['Q1', 'Q2', 'Q3', 'Q4'])
  .range([0, 400])
  .padding(0.1);

// Color mapping
const color = scaleOrdinal()
  .domain(['A', 'B', 'C'])
  .range(['#ff0000', '#00ff00', '#0000ff']);
```

### Shape Generators

```typescript
import {
  line,
  area,
  curve
} from 'd3-shape';

// Line generator
const line = d3.line()
  .x(d => xScale(d.x))
  .y(d => yScale(d.y));

// Area generator
const area = d3.area()
  .x(d => xScale(d.x))
  .y0(height - padding)
  .y1(d => yScale(d.y));

// With custom curve
const curvedLine = d3.line()
  .curve(d3.curveMonotoneX)
  .x(d => xScale(d.x))
  .y(d => yScale(d.y));
```

## Performance Optimization

### Pattern 1: Data Aggregation

For large datasets, aggregate before visualization:

```typescript
function aggregateData(
  data: DataPoint[],
  bucketSize: number
): AggregatedData[] {
  const buckets: Record<number, DataPoint[]> = {};

  data.forEach(point => {
    const bucket = Math.floor(point.x / bucketSize);
    if (!buckets[bucket]) buckets[bucket] = [];
    buckets[bucket].push(point);
  });

  return Object.entries(buckets).map(([bucket, points]) => ({
    x: Number(bucket) * bucketSize,
    y: points.reduce((sum, p) => sum + p.y, 0) / points.length,
    count: points.length
  }));
}

// Use aggregated data for visualization
let displayData = $derived(
  data.length > 10000 ? aggregateData(data, 100) : data
);
```

### Pattern 2: Viewport Filtering

Render only visible data points:

```svelte
<script>
  let scrollPosition = $state(0);
  const viewportSize = 50; // Show 50 points

  $: startIndex = Math.max(0, scrollPosition);
  $: endIndex = Math.min(data.length, scrollPosition + viewportSize);
  $: visibleData = data.slice(startIndex, endIndex);

  const handleScroll = (event: WheelEvent) => {
    scrollPosition += event.deltaY > 0 ? 1 : -1;
  };
</script>

<svg on:wheel={handleScroll}>
  {#each visibleData as d, i}
    <circle
      cx={xScale(startIndex + i)}
      cy={yScale(d.y)}
      r="3"
    />
  {/each}
</svg>
```

### Pattern 3: Canvas Rendering

For extreme performance, use Canvas instead of SVG:

```svelte
<script>
  let canvas: HTMLCanvasElement;

  $: if (canvas) {
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Clear canvas
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw data points
    data.forEach(d => {
      ctx.fillStyle = 'blue';
      ctx.beginPath();
      ctx.arc(xScale(d.x), yScale(d.y), 3, 0, Math.PI * 2);
      ctx.fill();
    });
  }
</script>

<canvas bind:this={canvas} width="400" height="300" />
```

## Best Practices

1. **Separate Concerns**
   - Keep data transformation separate from rendering
   - Use computed values for scales and dimensions
   - Store interaction state separately

2. **Responsive Design**
   - Use relative positioning and percentages
   - Calculate dimensions from container
   - Test on different viewport sizes

3. **Accessibility**
   - Include descriptive titles and labels
   - Provide data in alternative formats
   - Support keyboard navigation

4. **Performance**
   - Use Canvas for large datasets (1000+)
   - Aggregate data when appropriate
   - Memoize expensive calculations

5. **Code Organization**
   - Extract complex calculations into functions
   - Create reusable component patterns
   - Document scale domains and ranges

## Resources

- **Full documentation**: See `layercake-skills` skill
- **Expert guidance**: Ask `layercake-expert` agent
- **D3.js**: https://d3js.org
- **SVG Reference**: https://developer.mozilla.org/en-US/docs/Web/SVG

---

**Ready to build custom visualizations?** Explore the skill for comprehensive documentation and patterns!
