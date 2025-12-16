# Add git-worktree Plugin to Marketplace Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add the git-worktree plugin to the linehaulai-claude-marketplace registry so it can be installed and used

**Architecture:** The git-worktree plugin is a skill-only plugin (no plugin.json manifest needed) that provides Git worktree management guidance via a SKILL.MD file and helper scripts. It follows the "Skill with Bundled Resources" pattern with a scripts directory containing a bash helper (worktree-manager.sh). We need to add it to marketplace.json, create the SKILL.MD content, document it in CLAUDE.md, and create a README.

**Tech Stack:** Markdown, JSON, Bash

---

## Task 1: Create SKILL.MD Content

**Files:**
- Modify: `.claude-plugin/git-worktree/SKILL.MD` (currently empty)

**Step 1: Write skill content with proper frontmatter**

Create comprehensive skill following Claude Code best practices:

```markdown
---
name: git-worktree
description: Use when starting feature work that needs isolation from current workspace - creates isolated git worktrees with smart directory selection and safety verification
---

# Git Worktree Management

## Overview

Manage isolated Git worktrees for parallel feature development. Creates isolated working directories from your repository, allowing you to work on multiple branches simultaneously without stashing or switching contexts.

## When to Use

Use this skill when:
- Starting new feature development that needs isolation
- Working on multiple features simultaneously
- Need to preserve current workspace while testing another branch
- Before executing implementation plans that require clean workspace
- Creating hotfix branches without disrupting current work
- Setting up separate environments for experimentation

## When NOT to Use

Don't use this skill for:
- Simple branch switches (use `git checkout` instead)
- One-off commits or quick fixes
- Working with submodules (requires different approach)
- Repositories without Git (obviously)

## Core Concepts

**What is a Git Worktree?**

A Git worktree is a linked working directory from your repository. Instead of switching branches in one directory, you have multiple directories, each with their own branch checked out.

**Benefits:**
- No context switching - keep current work untouched
- Parallel development - work on multiple features simultaneously
- Environment isolation - each worktree has independent node_modules, .env files, etc.
- Fast switching - just `cd` between directories

**Directory Structure:**
```
your-repo/
├── .git/                    # Main Git directory
├── main branch files...     # Main working directory
└── .worktrees/             # Worktree container (gitignored)
    ├── feature-login/      # Isolated worktree
    ├── feature-auth/       # Another worktree
    └── hotfix-bug-123/     # Emergency fix worktree
```

## Helper Script

This plugin includes `scripts/worktree-manager.sh` for common operations.

**Make it executable first:**
```bash
chmod +x ${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh
```

**Usage:**

```bash
# Create new worktree
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create feature-login

# Create from specific branch
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create feature-auth develop

# List all worktrees
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh list

# Switch to worktree
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh switch feature-login

# Copy .env files to worktree
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh copy-env feature-login

# Clean up finished worktrees
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh cleanup
```

## Workflow

### Creating a Worktree

**Step 1: Identify the branch to work on**

Determine:
- Feature/branch name (e.g., `feature-user-auth`)
- Base branch (usually `main` or `develop`)

**Step 2: Create the worktree**

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create feature-user-auth main
```

This will:
- Update the base branch (`main`)
- Create new branch `feature-user-auth`
- Create worktree at `.worktrees/feature-user-auth/`
- Copy `.env` files automatically
- Add `.worktrees/` to `.gitignore`

**Step 3: Switch to the worktree**

```bash
cd .worktrees/feature-user-auth
```

**Step 4: Verify environment**

Check that:
- Correct branch is checked out: `git branch`
- Environment files present: `ls -la | grep .env`
- Dependencies installed (run `npm install`, `pip install`, etc. if needed)

### Working in a Worktree

**Normal Git operations work as expected:**
```bash
git status
git add .
git commit -m "feat: add user authentication"
git push origin feature-user-auth
```

**Each worktree is independent:**
- Has its own `node_modules/`, `venv/`, build artifacts
- Has its own `.env` files (copied from main repo)
- Doesn't affect other worktrees or main working directory

### Switching Between Worktrees

**Quick switch:**
```bash
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh switch feature-login
```

**Manual navigation:**
```bash
cd /path/to/repo/.worktrees/feature-login
```

**List available worktrees:**
```bash
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh list
```

### Cleaning Up Finished Work

**After merging/completing feature:**

```bash
# Switch back to main repo first
cd /path/to/main/repo

# Clean up all inactive worktrees
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh cleanup
```

This removes worktree directories and Git metadata safely.

## Common Patterns

### Pattern 1: Parallel Feature Development

```bash
# Create two features simultaneously
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create feature-frontend
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create feature-backend

# Work on frontend
cd .worktrees/feature-frontend
npm run dev

# In another terminal, work on backend
cd .worktrees/feature-backend
npm run dev:api
```

### Pattern 2: Urgent Hotfix

```bash
# Create hotfix without disrupting current work
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create hotfix-critical-bug main

# Fix, commit, push
cd .worktrees/hotfix-critical-bug
# make fixes...
git commit -am "fix: critical bug"
git push origin hotfix-critical-bug

# Return to original work
cd ../../  # back to main repo
# Your in-progress work is untouched
```

### Pattern 3: Environment Testing

```bash
# Create worktree for testing with different env
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create test-new-api-keys

cd .worktrees/test-new-api-keys
# Edit .env with new credentials
# Run tests
npm test
```

### Pattern 4: Integration with Implementation Plans

When using with `superpowers:writing-plans` or `superpowers:executing-plans`:

```bash
# 1. Create isolated worktree for feature
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh create feature-user-dashboard main

# 2. Switch to worktree
cd .worktrees/feature-user-dashboard

# 3. Execute implementation plan in isolation
# Your main workspace remains clean
```

## Troubleshooting

### Worktree creation fails

**Symptom:** Error creating worktree branch
**Cause:** Branch already exists
**Fix:**
```bash
# Delete existing branch first
git branch -D feature-name
# Or use different branch name
```

### Environment files missing in worktree

**Symptom:** Application fails due to missing .env
**Fix:**
```bash
# Copy env files to worktree
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh copy-env feature-name

# Or manually copy
cp .env* .worktrees/feature-name/
```

### Can't remove worktree

**Symptom:** `git worktree remove` fails
**Cause:** Uncommitted changes or locked files
**Fix:**
```bash
# Force remove
git worktree remove .worktrees/feature-name --force

# Or manually delete
rm -rf .worktrees/feature-name
git worktree prune
```

### Disk space concerns

**Symptom:** Worktrees consuming too much space
**Cause:** Each worktree has its own dependencies (node_modules, etc.)
**Fix:**
```bash
# Clean up unused worktrees regularly
${CLAUDE_PLUGIN_ROOT}/scripts/worktree-manager.sh cleanup

# Remove dependencies in unused worktrees
cd .worktrees/old-feature
rm -rf node_modules
```

## Best Practices

1. **Use descriptive branch names:** `feature-user-auth` not `feature1`
2. **Clean up regularly:** Don't accumulate unused worktrees
3. **One feature per worktree:** Keep worktrees focused
4. **Copy env files:** Always ensure `.env` files are current
5. **Commit often:** Each worktree is independent, commit freely
6. **Update .gitignore:** Ensure `.worktrees/` is ignored (script does this automatically)

## Integration with Other Skills

- **superpowers:brainstorming** → git-worktree → **superpowers:writing-plans**
  - Brainstorm design → Create isolated worktree → Write implementation plan

- **superpowers:executing-plans** works best in isolated worktree
  - Clean workspace, no interference from other work

- **superpowers:finishing-a-development-branch** after completing work
  - Guides merge/PR creation, then cleanup worktree

## Direct Git Commands (Alternative)

If not using the helper script:

```bash
# Create worktree manually
git worktree add -b feature-name .worktrees/feature-name main

# List worktrees
git worktree list

# Remove worktree
git worktree remove .worktrees/feature-name

# Prune deleted worktrees
git worktree prune
```

## Summary

Git worktrees enable parallel development without context switching:
1. **Create** isolated worktree for feature
2. **Work** independently in that directory
3. **Switch** between worktrees as needed
4. **Cleanup** when done

Use the provided `worktree-manager.sh` script for convenience and safety.
```

**Step 2: Verify SKILL.MD exists and has content**

Run: `cat .claude-plugin/git-worktree/SKILL.MD | head -20`
Expected: Shows frontmatter and beginning of skill content

**Step 3: Commit**

```bash
git add .claude-plugin/git-worktree/SKILL.MD
git commit -m "feat: add git-worktree skill documentation"
```

---

## Task 2: Add Plugin to marketplace.json

**Files:**
- Modify: `.claude-plugin/marketplace.json:80-88`

**Step 1: Add git-worktree entry to plugins array**

Insert after the `svelte5-runes` entry (before closing bracket):

```json
    {
      "name": "svelte5-runes",
      "source": "./.claude-plugin/svelte5-runes",
      "version": "1.0.0",
      "author": {
        "name": "fakebizprez"
      }
    },
    {
      "name": "git-worktree",
      "source": "./.claude-plugin/git-worktree",
      "version": "1.0.0",
      "author": {
        "name": "fakebizprez"
      }
    }
  ]
}
```

**Step 2: Verify JSON is valid**

Run: `python3 -m json.tool .claude-plugin/marketplace.json > /dev/null`
Expected: No output (silent success means valid JSON)

**Step 3: Commit**

```bash
git add .claude-plugin/marketplace.json
git commit -m "feat: add git-worktree to marketplace registry"
```

---

## Task 3: Create Plugin README

**Files:**
- Create: `.claude-plugin/git-worktree/README.md`

**Step 1: Write README content**

```markdown
# Git Worktree Plugin

Isolated Git worktree management for parallel feature development.

## What This Plugin Provides

**Skill:** `git-worktree` - Comprehensive guidance for using Git worktrees
**Script:** `worktree-manager.sh` - Helper tool for common worktree operations

## Installation

```bash
/plugin marketplace add /path/to/linehaulai-claude-marketplace
/plugin install git-worktree
```

## Quick Start

### Make script executable

```bash
chmod +x ~/.claude/plugins/installed/git-worktree/scripts/worktree-manager.sh
```

### Create your first worktree

```bash
~/.claude/plugins/installed/git-worktree/scripts/worktree-manager.sh create feature-my-feature
```

### List worktrees

```bash
~/.claude/plugins/installed/git-worktree/scripts/worktree-manager.sh list
```

## What Are Git Worktrees?

Git worktrees let you have multiple working directories from one repository. Instead of switching branches in place, each worktree is a separate directory with its own checked-out branch.

**Use cases:**
- Work on multiple features simultaneously
- Create hotfix without disrupting current work
- Test different approaches in parallel
- Isolate implementation plan execution

## Skill Triggering

The `git-worktree` skill automatically activates when Claude detects:
- "create worktree"
- "isolate feature work"
- "parallel development"
- Starting implementation plans that need clean workspace

## Helper Script Commands

```bash
# Create worktree
worktree-manager.sh create <branch-name> [from-branch]

# List all worktrees
worktree-manager.sh list

# Switch to worktree
worktree-manager.sh switch <name>

# Copy .env files
worktree-manager.sh copy-env [name]

# Clean up finished worktrees
worktree-manager.sh cleanup
```

## Integration with Other Plugins

Works seamlessly with:
- **superpowers:brainstorming** - Design in main repo, implement in worktree
- **superpowers:writing-plans** - Plans assume isolated workspace
- **superpowers:executing-plans** - Execute plans in clean worktree
- **superpowers:finishing-a-development-branch** - Merge and cleanup

## Directory Structure

```
.claude-plugin/git-worktree/
├── README.md                      # This file
├── SKILL.MD                       # Skill definition and documentation
└── scripts/
    └── worktree-manager.sh        # Helper script
```

## Plugin Type

**Pattern:** Skill with Bundled Resources
- Provides knowledge and guidance (SKILL.MD)
- Includes executable helper (worktree-manager.sh)
- No plugin.json needed (skill-only plugin)

## Documentation

See `SKILL.MD` for:
- Complete usage guide
- Common patterns
- Troubleshooting
- Best practices
- Integration examples

## License

MIT
```

**Step 2: Verify README exists**

Run: `ls -lh .claude-plugin/git-worktree/README.md`
Expected: Shows file with size > 0 bytes

**Step 3: Commit**

```bash
git add .claude-plugin/git-worktree/README.md
git commit -m "docs: add git-worktree plugin README"
```

---

## Task 4: Update CLAUDE.md Documentation

**Files:**
- Modify: `CLAUDE.md` (two sections to update)

**Step 1: Add to Key Plugins list**

Add after `svelte5-runes` line (around line 17):

```markdown
- `svelte5-runes`: Svelte 5 runes system guidance for reactivity, props, effects, and Svelte 4→5 migration
- `git-worktree`: Isolated Git worktree management for parallel feature development with helper scripts
<!-- END AUTO-MANAGED -->
```

**Step 2: Add to Architecture section**

Add after the `svelte5-runes` plugin documentation (after line 106):

```markdown
├── svelte5-runes/
│   ├── commands/            # Slash commands
│   │   └── runes.md         # Runes assistant for reactivity and migration
│   ├── agents/              # Specialized subagents
│   │   └── runes-expert.md  # Svelte 5 runes implementation expert
│   ├── references/          # Reference documentation
│   │   ├── common-mistakes.md     # Anti-patterns with fixes
│   │   ├── component-api.md       # $props, $bindable patterns
│   │   ├── migration-gotchas.md   # Svelte 4 → 5 translation
│   │   ├── reactivity-patterns.md # When to use each rune
│   │   └── snippets-vs-slots.md   # New snippet syntax
│   ├── examples/            # Code examples
│   │   ├── bindable-props.svelte
│   │   └── effect-vs-derived.svelte
│   ├── SKILL.md             # Main skill definition
│   └── README.md
└── git-worktree/
    ├── scripts/             # Helper scripts
    │   └── worktree-manager.sh  # Worktree management CLI
    ├── SKILL.md             # Git worktree guidance
    └── README.md
```

**Step 3: Add to Plugin Types documentation**

Add to the Plugin Types list (around line 142):

```markdown
**Plugin Types**:
1. **Full Plugins** (quickbooks-api-integration, golang-orchestrator, svelte-flow, layerchart, layercake, svelte5-runes, supabase): Commands + Skills + Agents
2. **Skill Plugins** (sequential-thinking, git-worktree): Standalone skills with reference docs, no manifest needed
3. **Hybrid Plugins** (sveltekit-spa, shadcn-svelte-skill): Skills + Commands, minimal structure
```

**Step 4: Add git-worktree pattern documentation**

Add new section after svelte5-runes pattern (around line 202):

```markdown
**svelte5-runes Pattern**:
[existing content...]

**git-worktree Pattern**:
- Skill-only plugin with bundled helper scripts
- Provides Git worktree management guidance
- Includes bash script for common operations (create, list, switch, cleanup)
- Follows "Skill with Bundled Resources" pattern
- No plugin.json needed (pure skill plugin)
<!-- END AUTO-MANAGED -->
```

**Step 5: Verify CLAUDE.md changes**

Run: `grep -n "git-worktree" CLAUDE.md`
Expected: Shows 3-4 matches in different sections

**Step 6: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: document git-worktree plugin in CLAUDE.md"
```

---

## Task 5: Update Usage Instructions

**Files:**
- Modify: `CLAUDE.md` (Usage section, around line 210)

**Step 1: Add installation example**

Add `git-worktree` to the installation examples:

```markdown
# Install a specific plugin
/plugin install quickbooks-api-integration
/plugin install golang-orchestrator
/plugin install sveltekit-spa
/plugin install shadcn-svelte-skill
/plugin install svelte-flow
/plugin install layerchart
/plugin install layercake
/plugin install sequential-thinking
/plugin install supabase
/plugin install svelte5-runes
/plugin install git-worktree
```

**Step 2: Verify addition**

Run: `grep -A 12 "Install a specific plugin" CLAUDE.md`
Expected: Shows all plugins including git-worktree

**Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add git-worktree to installation instructions"
```

---

## Task 6: Verify Plugin Structure

**Files:**
- Verify: `.claude-plugin/git-worktree/` directory structure

**Step 1: Check directory structure**

Run: `tree .claude-plugin/git-worktree/ -L 2`
Expected output:
```
.claude-plugin/git-worktree/
├── README.md
├── SKILL.MD
└── scripts
    └── worktree-manager.sh

1 directory, 3 files
```

**Step 2: Verify script is executable**

Run: `ls -l .claude-plugin/git-worktree/scripts/worktree-manager.sh`
Expected: Shows `-rwxr-xr-x` (executable permissions)

**Step 3: Verify files are non-empty**

Run: `wc -l .claude-plugin/git-worktree/SKILL.MD .claude-plugin/git-worktree/README.md`
Expected: Both files show > 100 lines each

**Step 4: No commit needed** (verification only)

---

## Task 7: Test Marketplace Registration

**Files:**
- Test: Marketplace JSON structure and plugin availability

**Step 1: Validate marketplace.json structure**

Run: `jq '.plugins[] | select(.name == "git-worktree")' .claude-plugin/marketplace.json`
Expected output:
```json
{
  "name": "git-worktree",
  "source": "./.claude-plugin/git-worktree",
  "version": "1.0.0",
  "author": {
    "name": "fakebizprez"
  }
}
```

**Step 2: Count total plugins**

Run: `jq '.plugins | length' .claude-plugin/marketplace.json`
Expected: `11` (was 10, now 11 with git-worktree)

**Step 3: Verify plugin source path**

Run: `ls -ld .claude-plugin/git-worktree`
Expected: Shows directory exists with proper permissions

**Step 4: No commit needed** (verification only)

---

## Task 8: Create Git Tag for Release

**Files:**
- Git repository tags

**Step 1: Verify all changes are committed**

Run: `git status`
Expected: `nothing to commit, working tree clean`

**Step 2: Review commit history**

Run: `git log --oneline -5`
Expected: Shows all 5 commits from previous tasks

**Step 3: Create annotated tag**

Run:
```bash
git tag -a git-worktree-v1.0.0 -m "Release git-worktree plugin v1.0.0

- Add git-worktree skill with comprehensive documentation
- Include worktree-manager.sh helper script
- Register plugin in marketplace
- Document in CLAUDE.md architecture section"
```

**Step 4: Verify tag creation**

Run: `git tag -l | grep git-worktree`
Expected: `git-worktree-v1.0.0`

**Step 5: Push commits and tags**

Run:
```bash
git push origin main
git push origin git-worktree-v1.0.0
```

Expected: Both commands succeed

---

## Verification Checklist

After completing all tasks, verify:

- [ ] `.claude-plugin/git-worktree/SKILL.MD` exists with proper frontmatter and comprehensive content
- [ ] `.claude-plugin/git-worktree/README.md` exists with installation and usage instructions
- [ ] `.claude-plugin/marketplace.json` includes git-worktree entry
- [ ] `CLAUDE.md` documents git-worktree in Key Plugins list
- [ ] `CLAUDE.md` documents git-worktree in Architecture section
- [ ] `CLAUDE.md` includes git-worktree in Plugin Types documentation
- [ ] `CLAUDE.md` includes git-worktree in installation examples
- [ ] `scripts/worktree-manager.sh` has executable permissions
- [ ] All changes committed with meaningful messages
- [ ] Git tag created: `git-worktree-v1.0.0`
- [ ] Changes pushed to remote (commits + tag)

## Testing the Plugin

After installation in a test repository:

```bash
# Install from marketplace
/plugin marketplace add /path/to/linehaulai-claude-marketplace
/plugin install git-worktree

# Test skill triggers
# Ask Claude: "Help me create an isolated worktree for a new feature"

# Test helper script
~/.claude/plugins/installed/git-worktree/scripts/worktree-manager.sh list
```

## Notes

- This is a skill-only plugin (no `.claude-plugin/plugin.json` required)
- Helper script uses `${CLAUDE_PLUGIN_ROOT}` for portability
- Follows "Skill with Bundled Resources" pattern
- Script permissions must be set by user after installation (`chmod +x`)
