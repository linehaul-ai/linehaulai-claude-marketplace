# GitHub Issue Creator Skill

A Claude Code skill that creates structured GitHub issues with proper sub-task organization directly from conversation context.

## Quick Start

### Activation

This skill activates automatically when you mention creating GitHub issues. Just say:

```
"Create GitHub issues for [feature/bug/work discussed]"
```

### Common Patterns

```bash
# After discussing a feature
"Create issues for the carrier onboarding feature we discussed"

# Breaking down complex work
"Create a parent issue for the billing workflow with sub-tasks for POD handling and invoice logic"

# From conversation context
"Create GitHub issues for the remaining work"

# After implementation
"Create follow-up issues for tests and documentation"
```

## How It Works

1. **You discuss** features, bugs, or implementation plans with Claude
2. **You request** issue creation when ready to track the work
3. **Claude delegates** to the `gh-issue-creator` agent
4. **Agent creates** properly structured GitHub issues with:
   - Clear titles and descriptions
   - Parent/child relationships
   - Sub-tasks aligned with implementation
   - Acceptance criteria
5. **You receive** direct GitHub links to review the issues

## Features

### Automatic Context Understanding
- Analyzes full conversation history
- Extracts requirements from discussions
- Identifies logical sub-task breakdown
- Creates appropriate parent/child relationships

### Structured Issue Format
- Action-oriented titles
- Detailed descriptions
- Clear acceptance criteria
- Technical notes and dependencies
- Proper markdown formatting

### Smart Sub-task Organization
- Groups related work under parent issues
- Creates focused, single-responsibility sub-tasks
- Links dependencies appropriately
- Aligns with implementation plans

## File Structure

```
.claude/skills/gh-issue/
├── SKILL.md          # Main skill definition (triggers and behavior)
├── examples.md       # Usage examples and patterns
└── README.md         # This file
```

## Skill Metadata

| Property | Value |
|----------|-------|
| **Name** | `gh-issue` |
| **Triggers** | Creating issues, tracking work, organizing development tasks |
| **Agent** | `gh-issue-creator` |
| **Access** | Project-wide (team accessible in git) |

## Requirements

- GitHub CLI (`gh`) installed and authenticated
- Repository must be a GitHub repository
- User must have write access to create issues

## Best Practices

### Do:
- ✅ Discuss features/bugs thoroughly before creating issues
- ✅ Be specific about what needs tracking
- ✅ Mention desired sub-task breakdown
- ✅ Review created issues via GitHub links

### Don't:
- ❌ Create issues without discussion context
- ❌ Request vague "create some issues"
- ❌ Skip reviewing the created issues
- ❌ Forget to mention parent/child organization if needed

## Examples

See [examples.md](./examples.md) for detailed usage patterns and created issue examples.

## Integration

### Works With:
- **Todo lists** - Convert todos into GitHub issues
- **Planning mode** - Create issues from implementation plans
- **Feature discussions** - Track discussed features
- **Bug reports** - Organize related bugs

### Typical Workflow:
1. Discuss feature/bug with Claude
2. Plan implementation approach
3. Request issue creation: "Create GitHub issues for this work"
4. Review issues via provided GitHub links
5. Continue development with tracked work

## Troubleshooting

### Skill Not Triggering
- Ensure you mention "GitHub issues" or "create issues" in your request
- Try explicit phrasing: "Use the gh-issue skill to create issues"
- Restart Claude Code to reload skills

### Issues Not Created
- Check `gh` CLI is authenticated: `gh auth status`
- Verify repository is a GitHub repo: `git remote -v`
- Ensure you have write access to the repository

### Wrong Issue Structure
- Provide more context in your discussion before requesting issues
- Be explicit about parent/child relationships
- Mention specific sub-tasks you want created

## Contributing

This skill is part of the laneweaverTMS project. To modify:

1. Edit `SKILL.md` for behavior changes
2. Update `examples.md` for new usage patterns
3. Test by requesting issue creation
4. Commit changes to share with team

## Related

- **Agent**: `gh-issue-creator` (creates the actual issues)
- **Tool**: `gh` CLI (GitHub command-line interface)
- **Directory**: `.claude/skills/gh-issue/`
