---
description: Conduct multi-turn deep research on a specific topic — traces actual code paths with zero tolerance for shallow analysis
---

# Deep Wiki: Deep Research

Conduct a comprehensive, multi-turn investigation of a specific topic within this codebase. You are a **researcher and analyst** — your outputs are understanding, maps, explanations, and actionable insights.

## Source Repository Resolution (MUST DO FIRST)

Before any research, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, use linked citations: `[file:line](REPO_URL/blob/BRANCH/file#Lline)`
   - Local → use `(file_path:line_number)`
3. **Determine default branch**: Run `git rev-parse --abbrev-ref HEAD`
4. **Do NOT proceed** until resolved

## Research Topic

$ARGUMENTS

## Core Invariants (NON-NEGOTIABLE)

1. **TRACE ACTUAL CODE PATHS** — Do not guess from file names. Read the implementation. If A calls B calls C, follow it all the way.
2. **EVERY CLAIM NEEDS A SOURCE** — File path + function/class name. No exceptions.
3. **DISTINGUISH FACT FROM INFERENCE** — "I read this code" vs "I'm inferring from structure."
4. **NO HAND-WAVING** — Don't say "this likely handles..." Read the code and state what it ACTUALLY does.
5. **FLAG UNKNOWNS** — If you haven't traced something, say "I haven't traced this yet" instead of guessing.

## Process: 5-Iteration Research Cycle

You will perform 5 progressive research iterations. Each builds on all previous ones. NEVER repeat prior findings. ALWAYS provide substantive analysis.

### Iteration 1: Research Plan & Structural Survey

- State the specific topic under investigation
- Map the landscape: components, boundaries, entry points
- Identify relevant files and components to examine
- Provide initial findings with file citations
- Rate confidence: HIGH/MEDIUM/LOW for each finding
- End with "Next Steps" for iteration 2

### Iterations 2–4: Progressive Deep Dives

Each iteration takes a different analytical lens:
- **Iteration 2**: Data flow and state management — trace inputs → transformations → outputs → storage. Include `sequenceDiagram` and/or `stateDiagram-v2`.
- **Iteration 3**: Integration, dependency, and API contract perspective — external connections, coupling. Include dependency graph and integration table.
- **Iteration 4**: Pattern analysis — design patterns, anti-patterns, trade-offs, risks, technical debt. Use tables to catalogue patterns and rank risks.

For each:
- Build upon ALL previous iterations
- Focus on one specific unexplored aspect
- Provide new insights with linked citations
- **Include at least 1 Mermaid diagram per iteration** (dark-mode colors) — use the diagram type that best fits the analytical lens
- **Include at least 1 structured table per iteration** — organize findings so they're scannable at a glance
- Rate confidence for every finding
- End with remaining areas to investigate

### Iteration 5: Final Synthesis

- Synthesize ALL findings from iterations 1–4
- Provide a clear mental model: "Here's how to think about this" (2-3 sentences)
- Then: "Here's what that mental model hides" (nuances, edge cases, gotchas)
- Highlight surprising or unusual findings
- Provide actionable insights and recommendations
- List key findings as numbered items with citations and confidence ratings

### Running Knowledge Map

Maintain this throughout all iterations:

```
## Explored ✅
- [component/area]: [1-line summary] — confidence: HIGH/MED/LOW

## Partially Explored 🔶
- [component/area]: [what we know, what's still unknown]

## Unexplored ❓
- [component/area]: [why it might matter]

## Key Findings 🔍
- [finding]: [1-line summary] — [risk/importance]

## Open Questions ❔
- [question]: [what we'd need to trace to answer it]
```

## Rules

- NEVER respond with just "Continue the research" — always provide substantive findings
- ALWAYS cite specific files using the resolved citation format: `[file_path:line_number](REPO_URL/blob/BRANCH/file_path#Lline_number)` (remote) or `(file_path:line_number)` (local)
- ALWAYS build on previous iterations — do not repeat
- Stay focused on the specific topic — do not drift
- Call out the weird stuff — surprising patterns are the most valuable findings
- Include Mermaid diagrams (dark-mode colors) with `<!-- Sources: ... -->` comment blocks after each
