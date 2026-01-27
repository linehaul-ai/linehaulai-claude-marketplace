---
name: gh-issue
description: Create structured GitHub issues with sub-tasks and proper formatting. Use when organizing development work into trackable issues, breaking down features into parent/child issues, converting discussions into tracked work, or creating issues from conversation context.
keywords: [github, github-issues, automation, task-management, issue-tracking]
---

# GitHub Issue Creator

## Overview

This Skill helps you create well-structured GitHub issues directly from conversation context. It automatically organizes complex work into parent issues with sub-tasks, ensuring nothing gets lost in discussion.

## When to Use This Skill

Use this when you want to:

- **Convert discussions into tracked work** - Turn feature discussions into properly structured GitHub issues
- **Break down complex features** - Create parent issues with sub-tasks for multi-step work
- **Organize related bugs** - Group related issues under a parent for better tracking
- **Track implementation work** - Create issues aligned with the to-do tree structure
- **Ensure work isn't forgotten** - Proactively create issues after discussing features or improvements

## How It Works

When you ask to create GitHub issues, I'll:

1. **Analyze the conversation context** to understand what needs to be tracked
2. **Use the gh-issue-creator agent** to create properly structured issues with:
   - Clear, descriptive titles
   - Detailed descriptions with acceptance criteria
   - Parent/child relationships for complex work
   - Sub-tasks that align with the implementation plan
3. **Provide GitHub links** so you can review and manage the issues

## Example Usage

### After Feature Discussion
```
"Create GitHub issues for the carrier onboarding feature we just discussed"
```

### Breaking Down Work
```
"Create a parent issue for the new billing workflow with sub-tasks for:
- POD receipt handling
- Invoice ready flag logic
- Payment tracking"
```

### Organizing Related Bugs
```
"Create a parent issue for the load status bugs with individual sub-tasks for each problem"
```

### From Existing Plan
```
"Create GitHub issues for the remaining work we discussed"
```

## Agent Delegation

When you request issue creation, I'll delegate to the **gh-issue-creator** agent, which has access to:

- Current conversation context
- Your repository structure
- GitHub CLI (`gh`) for issue creation
- Understanding of parent/child issue relationships

The agent will create issues that match your discussion and provide you with direct links to review them in GitHub.

## Tips for Best Results

- **Be specific** about what features or bugs need tracking
- **Mention sub-tasks** if you want them broken down
- **Reference earlier discussion** - the agent has full conversation context
- **Review the created issues** using the GitHub links provided

## Integration with Workflow

This Skill works seamlessly with:

- **Todo lists** - Convert completed todos into documented issues
- **Planning discussions** - Create issues from implementation plans
- **Bug reports** - Track bugs with proper sub-task breakdown
- **Feature requests** - Organize feature work into manageable pieces
