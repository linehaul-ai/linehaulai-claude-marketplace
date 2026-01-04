---
name: handoff
description: Write a HANDOFF.md file for another agent to continue the conversation. Use when switching to a new session and need to pass context to the next agent.
metadata:
  short-description: Write handoff document for agent continuation
---

# Handoff

Write a `/docs/handoffs/{YYYY-MM-DD_HH-MM-SS_description}/HANDOFF.md` file in the current working directory for another agent to continue this conversation.

## Workflow

### 1. Gather Context

Before writing, collect:
- Current git branch and commit hash
- Repository name
- Summary of tasks worked on and their statuses
- Key files modified
- Important learnings and patterns discovered

### 2. Write Handoff Document

Create the file using this template structure:

```markdown
---
date: [Current date and time with timezone in ISO format]
researcher: Claude
git_commit: [Current commit hash]
branch: [Current branch name]
repository: [Repository name]
topic: "[Feature/Task Name] Implementation Strategy"
tags: [implementation, strategy, relevant-component-names]
status: in_progress
last_updated: [Current date in YYYY-MM-DD format]
last_updated_by: Claude
type: implementation_strategy
---

# Handoff: {very concise description}

## Task(s)
{description of the task(s) worked on, with status: completed, in-progress, or planned}

## Critical References
{2-3 most important file paths for specs, architecture docs, or design decisions. Leave blank if none.}

## Recent Changes
{files modified in file:line syntax}

## Learnings
{important patterns, root causes, or insights the next agent should know}

## Artifacts
{exhaustive list of files produced or updated}

## Action Items & Next Steps
{list of next steps for the next agent}

## Other Notes
{additional context, file locations, or useful information}
```

### 3. Confirm Handoff

After writing, confirm the file location and summarize what was captured.

## Guidelines

- Extract only what matters for continuing the work
- Write from the user's perspective (first person: "I did...", "I told you...")
- Focus on capabilities and behavior, not excessive implementation details
- Choose appropriate length based on complexity
- If the user's goal is unclear, ask for clarification
