# shadcn-svelte-skill Hook Integration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Integrate the shadcn-component-reminder.sh hook with the shadcn-svelte-skill plugin so it triggers contextual reminders when editing shadcn component files.

**Architecture:** The integration follows the established pattern from golang-orchestrator and sveltekit-spa plugins. The hook script will be placed in `.claude-plugin/shadcn-svelte-skill/hooks/` directory and registered in a new `plugin.json` manifest file. The hook triggers on file:edit events for files matching `**/lib/components/ui/**` glob pattern.

**Tech Stack:**
- Bash hook script for contextual reminders
- Claude Plugin manifest (plugin.json) for hook registration
- File-based event system (file:edit)
- Glob pattern matching for component directories

---

## Task 1: Create hooks Directory

**Files:**
- Create: `.claude-plugin/shadcn-svelte-skill/hooks/` (directory)

**Step 1: Create the hooks directory structure**

Run: `mkdir -p /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks`

Expected: Directory created successfully with no output (exit code 0)

---

## Task 2: Move Hook File to Plugin Directory

**Files:**
- Move: `/Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/shadcn-component-reminder.sh` → `.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh`

**Step 1: Move the hook file from repository root to plugin hooks directory**

Run: `mv /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/shadcn-component-reminder.sh /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh`

Expected: File moved successfully with no output (exit code 0)

**Step 2: Verify file exists in new location**

Run: `ls -l /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh`

Expected: Output shows the file with proper permissions (-rw-r--r-- or similar)

**Step 3: Verify hook script is executable**

Run: `chmod +x /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh`

Expected: File permissions updated (exit code 0)

**Step 4: Verify hook script content**

Run: `head -n 5 /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh`

Expected: Output shows:
```
#!/bin/bash
# shadcn-component-reminder.sh
# Hook for shadcn-svelte component development
# Triggers when editing files in $lib/components/ui/
```

---

## Task 3: Create plugin.json Manifest

**Files:**
- Create: `.claude-plugin/shadcn-svelte-skill/.claude-plugin/plugin.json`

**Step 1: Create .claude-plugin subdirectory if it doesn't exist**

Run: `mkdir -p /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/.claude-plugin`

Expected: Directory created successfully with no output (exit code 0)

**Step 2: Write plugin.json with hook configuration**

Create file: `.claude-plugin/shadcn-svelte-skill/.claude-plugin/plugin.json`

```json
{
  "name": "shadcn-svelte-skill",
  "version": "1.0.0",
  "description": "Build accessible, customizable UI components for Svelte/SvelteKit projects using shadcn-svelte CLI, Tailwind CSS v4.1, and TypeScript",
  "author": {
    "name": "fakebizprez",
    "email": "anthony@linehaul.ai"
  },
  "keywords": ["svelte", "sveltekit", "shadcn-svelte", "ui-components", "tailwind", "typescript"],
  "hooks": [
    {
      "event": "file:edit",
      "glob": "**/lib/components/ui/**",
      "script": "./hooks/shadcn-component-reminder.sh"
    }
  ]
}
```

**Step 3: Verify plugin.json is valid JSON**

Run: `cat /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/.claude-plugin/plugin.json | python3 -m json.tool > /dev/null && echo "Valid JSON"`

Expected: Output shows `Valid JSON` (exit code 0)

**Step 4: Verify hook script path is correct**

Run: `test -f /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh && echo "Hook script exists"`

Expected: Output shows `Hook script exists` (exit code 0)

---

## Task 4: Update Marketplace Registry

**Files:**
- Modify: `.claude-plugin/marketplace.json`

**Step 1: Read current marketplace.json to understand structure**

Run: `cat /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/marketplace.json`

Expected: JSON output showing plugin entries (shadcn-svelte-skill entry already exists)

**Step 2: Verify shadcn-svelte-skill is properly registered**

Run: `grep -A 5 '"name": "shadcn-svelte-skill"' /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/marketplace.json`

Expected: Output shows shadcn-svelte-skill entry with correct source path

**Step 3: Commit notice - marketplace.json likely requires no changes**

The marketplace.json already has the shadcn-svelte-skill entry pointing to `./.claude-plugin/shadcn-svelte-skill`, which means the plugin system will automatically discover the hooks from the new `.claude-plugin/plugin.json` manifest.

---

## Task 5: Verify Complete Integration

**Files:**
- Check: All integration points are in place

**Step 1: Verify complete directory structure**

Run: `find /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill -type f | sort`

Expected: Output includes:
- `.claude-plugin/shadcn-svelte-skill/.claude-plugin/plugin.json` (NEW)
- `.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh` (MOVED)
- `.claude-plugin/shadcn-svelte-skill/SKILL.md`
- `.claude-plugin/shadcn-svelte-skill/commands/shadcn.md`
- `.claude-plugin/shadcn-svelte-skill/references/` files

**Step 2: Verify no duplicate hook file exists in repository root**

Run: `ls -la /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/shadcn-component-reminder.sh 2>&1`

Expected: Output shows `No such file or directory` (file successfully moved, not duplicated)

**Step 3: Test hook script execution (dry run)**

Run: `CLAUDE_FILE_PATH="/path/to/lib/components/ui/button/button.svelte" bash /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh`

Expected: Output shows the shadcn-component reminder message:
```
shadcn-svelte component detected

Patterns:
- Use cn() for class merging
- Props: Use $props() not export let
- Events: onclick not on:click (Svelte 5)
- Variants: Define in component with cva()

Commands:
- /shadcn add     - Install components
- /shadcn form    - Form patterns
- /shadcn table   - DataTable setup
- /shadcn theme   - CSS customization

Skill: shadcn-svelte-skill
```

**Step 4: Test hook script with non-matching path**

Run: `CLAUDE_FILE_PATH="/path/to/src/lib/utils.ts" bash /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace/.claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh`

Expected: No output (hook correctly exits silently for non-matching paths)

**Step 5: Verify git status**

Run: `cd /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace && git status --short`

Expected: Output shows:
- `A  .claude-plugin/shadcn-svelte-skill/.claude-plugin/plugin.json` (new file)
- `D  shadcn-component-reminder.sh` (deleted from root)
- `A  .claude-plugin/shadcn-svelte-skill/hooks/shadcn-component-reminder.sh` (added to plugin)

Or similar variation showing the file move and new manifest creation.

---

## Task 6: Commit Integration Changes

**Files:**
- Modified: `.claude-plugin/shadcn-svelte-skill/` (new hook and plugin manifest)
- Git operations: stage, commit

**Step 1: Stage all changes**

Run: `cd /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace && git add .claude-plugin/shadcn-svelte-skill/`

Expected: No output (exit code 0)

**Step 2: Verify staged changes**

Run: `cd /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace && git status --short`

Expected: Output shows staged changes with `A` (added) and `D` (deleted) markers

**Step 3: Commit the integration**

Run: `cd /Users/fakebizprez/Developer/repositories/linehaulai-claude-marketplace && git commit -m "feat: integrate shadcn-component hook with shadcn-svelte-skill plugin"`

Expected: Output shows commit summary with:
- Files changed count
- Insertions count
- Deletions count (the hook file move)

---

## Implementation Notes

### Pattern Consistency
This integration follows the established patterns in the marketplace:
- **golang-orchestrator**: Has hooks directory with `.claude-plugin/plugin.json` manifest
- **sveltekit-spa**: Has hooks directory with `.claude-plugin/plugin.json` manifest
- **shadcn-svelte-skill**: Now has matching structure

### Hook Trigger Details
The hook triggers on:
- **Event**: `file:edit` (when user edits a file)
- **Glob**: `**/lib/components/ui/**` (matches shadcn component directories in any SvelteKit project)
- **Script**: `./hooks/shadcn-component-reminder.sh` (relative to plugin root)

The hook provides Svelte 5-specific patterns and commands relevant to shadcn-svelte component development.

### Testing Recommendations
After integration:
1. Edit a shadcn component file (e.g., `src/lib/components/ui/button/button.svelte`)
2. Verify the reminder message appears in the Claude Code interface
3. Confirm the hook doesn't trigger for non-component files
4. Check that the `/shadcn` command still works alongside the hook

---

## Summary

This plan integrates the shadcn-component-reminder.sh hook into the shadcn-svelte-skill plugin through:
1. Creating the hooks directory structure
2. Moving the hook file from repository root to the proper plugin location
3. Creating plugin.json manifest with hook configuration
4. Verifying the integration works correctly
5. Committing all changes

The integration enables the plugin system to automatically trigger contextual reminders when users edit shadcn component files, improving their development experience with Svelte 5 patterns and available commands.
