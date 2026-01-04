---
name: handoff-resume
description: Resume work from a HANDOFF.md file. Use when starting a new session to continue where a previous agent left off. Triggers include "resume", "pickup", "continue from handoff", "load handoff", "where did we leave off".
metadata:
  short-description: Resume work from handoff document
---

# Resume from Handoff

Interactively load and process a HANDOFF.md document to continue work from where a previous agent left off.

## Workflow

### 1. Find Available Handoffs

Search for handoff documents in the project:

```
/docs/handoffs/**/HANDOFF.md
```

List available handoffs with their dates, topics, and status. Present them to the user in a clear format:

```
Available Handoffs:
1. [2024-01-15] Feature X Implementation - Status: in_progress
2. [2024-01-14] Bug Fix Y - Status: complete
3. [2024-01-12] Refactoring Z - Status: in_progress
```

If no handoffs are found, inform the user and suggest creating one with `/handoff`.

### 2. Interactive Selection

Ask the user which handoff to load, or if they provide a specific file path, use that directly.

If multiple handoffs exist for similar work, help the user identify the most recent or relevant one.

### 3. Parse Handoff Document

Read the selected handoff and extract:
- **Task(s)**: What was being worked on and their statuses
- **Critical References**: Specification docs, architectural decisions
- **Recent Changes**: Files modified (file:line format)
- **Learnings**: Important patterns, root causes, insights
- **Artifacts**: Documents and files produced
- **Action Items**: Next steps to accomplish
- **Other Notes**: Additional context

### 4. Interactive Context Loading

Present a summary of the handoff and ask the user what they want to focus on:

```
Handoff Summary:
- Topic: [Topic from handoff]
- Status: [Current status]
- Tasks: [Number of completed/in-progress/planned tasks]
- Artifacts: [Number of referenced files]

What would you like me to load?
1. Full context - Load all referenced artifacts and provide complete summary
2. Action items only - Focus on next steps without loading all files
3. Specific section - Choose which parts to load
4. Just the summary - Quick overview without file loading
```

### 5. Load Selected Context

Based on user selection:

**Full context:**
- Read all files listed in Artifacts section
- Read Critical References
- Read files from Recent Changes
- Provide comprehensive summary

**Action items only:**
- Read Action Items section
- Create a todo list from the action items
- Provide brief context on what needs to be done

**Specific section:**
- Ask which sections to load
- Load only those referenced files

**Just the summary:**
- Provide the handoff summary without reading additional files

### 6. Create Working Todo List

Convert the Action Items from the handoff into a proper todo list using TodoWrite:

```
Pending tasks from handoff:
- [ ] Task 1 from action items
- [ ] Task 2 from action items
- [ ] Task 3 from action items
```

### 7. Confirm Ready to Continue

After loading context, confirm with the user:

```
Context loaded from handoff. Ready to continue work on [topic].

Quick summary:
- [Brief summary of where we left off]
- [Current state]
- [Immediate next step]

Shall I proceed with the first action item, or do you have specific questions about the previous work?
```

## Output Format

When presenting the loaded handoff, use this structure:

```markdown
## Resuming: [Topic]

**Previous Session**: [Date] by [Researcher]
**Branch**: [branch name]
**Status**: [status]

### Where We Left Off
[Summary of current state based on handoff]

### Loaded Context
- [List of files/artifacts loaded]

### Next Steps (from handoff)
1. [First action item]
2. [Second action item]
...

### Key Learnings to Remember
- [Important learnings from previous session]
```

## Error Handling

- If handoff references files that no longer exist, note them but continue
- If handoff is from a different branch, warn the user
- If handoff is very old (>7 days), suggest verifying the context is still relevant
- If git commit referenced doesn't match current state, note the divergence
