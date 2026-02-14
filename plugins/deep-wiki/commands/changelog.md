---
description: Generate a structured changelog from recent git commits, categorized by change type
---

# Deep Wiki: Changelog Generation

Analyze the git commit history of this repository and generate a structured changelog.

## Source Repository Resolution (MUST DO FIRST)

Before generating any changelog, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, link commit hashes: `[abc1234](REPO_URL/commit/abc1234)`
   - Local → use plain commit hashes
3. **Do NOT proceed** until resolved

## Process

1. Examine recent git commits (messages, dates, authors)
2. Group by date: daily for last 7 days, aggregated weekly for older
3. Classify each commit into categories
4. Generate concise, user-facing descriptions using project terminology from README

## Categories

| Emoji | Category | Signal Keywords |
|-------|----------|----------------|
| 🆕 | New Features | `feat`, `add`, `new`, `implement`, `introduce` |
| 🐛 | Bug Fixes | `fix`, `bug`, `patch`, `resolve`, `hotfix` |
| 🔄 | Refactoring | `refactor`, `restructure`, `reorganize`, `clean` |
| 📝 | Documentation | `docs`, `readme`, `comment`, `jsdoc`, `docstring` |
| 🔧 | Configuration | `config`, `env`, `setting`, `ci`, `build` |
| 📦 | Dependencies | `deps`, `upgrade`, `bump`, `package`, `lock` |
| ⚠️ | Breaking Changes | `breaking`, `BREAKING`, `migrate`, `deprecate` |

## Output

For each time period, output:

```markdown
## [Date or Date Range]

**[Summary Title]**

[1-2 sentence overview]

### 🆕 New Features
- [Change description]

### 🐛 Bug Fixes
- [Change description]

### ⚠️ Breaking Changes
- [Change description with migration notes]
```

Focus on **user-facing changes**. Merge related commits. Highlight breaking changes prominently.

$ARGUMENTS
