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
