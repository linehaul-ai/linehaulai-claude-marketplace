---
description: Create structured GitHub issues with sub-tasks from conversation context
model: sonnet
---

# Command Instructions

Invoke the `gh-issue` skill and delegate to the `gh-issue-creator` subagent to create GitHub issues.

## Parameters

- `$ARGUMENTS` - Optional description of what issues to create (e.g., feature name, bug description, or work item). If omitted, analyzes conversation context to determine what issues to create.

## Expected Behavior

1. Invoke the `gh-issue` skill
2. Delegate to the `gh-issue-creator` subagent with `$ARGUMENTS` (if provided)

## Examples

- `/gh-issue`
- `/gh-issue carrier onboarding feature`
