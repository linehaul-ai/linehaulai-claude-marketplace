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
