# GitHub Issue Creation Examples

## Example 1: Feature Implementation

**User Request:**
```
"We need to add carrier onboarding with compliance verification through MyCarrierPortal.
Create issues for this."
```

**What Gets Created:**
- **Parent Issue**: "Implement carrier onboarding with MyCarrierPortal integration"
  - Description includes integration requirements, API details, compliance verification flow
  - **Sub-task 1**: "Set up MyCarrierPortal OAuth provider"
  - **Sub-task 2**: "Implement compliance verification endpoints"
  - **Sub-task 3**: "Add carrier onboarding UI flow"
  - **Sub-task 4**: "Create database migrations for onboarding data"

---

## Example 2: Bug Fixes

**User Request:**
```
"I found several issues with the load billing workflow - POD receipt isn't updating
correctly and the invoice_ready flag logic is wrong. Create issues."
```

**What Gets Created:**
- **Parent Issue**: "Fix load billing workflow bugs"
  - Description summarizes the billing workflow issues
  - **Sub-task 1**: "Fix POD receipt not updating correctly"
    - Detailed description of the bug
    - Steps to reproduce
    - Expected vs actual behavior
  - **Sub-task 2**: "Fix invoice_ready flag logic"
    - Description of the incorrect logic
    - Expected behavior
    - Impact analysis

---

## Example 3: After Implementation Discussion

**User Request:**
```
"Can you create issues for the remaining work we discussed?"
```

**Context:** User and Claude just discussed implementing a new GPS tracking feature

**What Gets Created:**
- Issues based on the conversation context:
  - **Issue 1**: "Integrate Samsara GPS webhook endpoint"
  - **Issue 2**: "Add load_cognition table tracking"
  - **Issue 3**: "Create frontend map view for real-time tracking"
  - **Issue 4**: "Add GPS coordinate validation and error handling"

---

## Example 4: Breaking Down Complex Work

**User Request:**
```
"Create a parent issue for implementing the virtual yard feature with sub-tasks for:
- Trailer tracking
- Dock position management
- Dwell time alerts"
```

**What Gets Created:**
- **Parent Issue**: "Implement DROP-IT Virtual Yard Management System"
  - Comprehensive description of the virtual yard feature
  - **Sub-task 1**: "Implement trailer tracking in virtual_yard table"
  - **Sub-task 2**: "Add dock position management UI and API"
  - **Sub-task 3**: "Create dwell time alert system"

---

## Example 5: Proactive Issue Creation

**Context:** After implementing a new feature

**Claude:**
```
"I've completed the carrier endpoints implementation. Would you like me to create
GitHub issues for the follow-up work we identified (tests, documentation, error handling)?"
```

**User:** "Yes, create those issues"

**What Gets Created:**
- **Issue 1**: "Add unit tests for carrier service layer"
- **Issue 2**: "Document carrier API endpoints"
- **Issue 3**: "Enhance carrier error handling and validation"

---

## Example 6: From Todo List

**User Request:**
```
"Create GitHub issues from our current todo list"
```

**Context:** Active todo list with completed items

**What Gets Created:**
Issues matching the todo structure:
- Completed todos → Documented as done in issue description
- Pending todos → Individual issues or sub-tasks
- Blocked todos → Issues with blocker dependencies noted

---

## Tips for Effective Issue Creation

### Be Specific
✅ **Good**: "Create issues for the carrier onboarding feature with OAuth and compliance verification"
❌ **Bad**: "Create some issues"

### Provide Context
✅ **Good**: "Based on our discussion about the billing workflow, create tracking issues"
❌ **Bad**: "Make issues" (without prior discussion)

### Break Down Complex Work
✅ **Good**: "Create a parent issue with sub-tasks for: API, database, frontend, tests"
❌ **Bad**: "Create one issue for everything"

### Reference Earlier Discussion
✅ **Good**: "Create issues for the GPS tracking work we just planned"
❌ **Bad**: "Create GPS issues" (without context)

---

## Issue Formatting

All created issues follow consistent formatting:

### Title Format
- Clear, action-oriented (starts with verb)
- Specific scope
- Example: "Implement carrier onboarding with MyCarrierPortal integration"

### Description Format
```markdown
## Summary
[Brief overview of what needs to be done]

## Requirements
- [Requirement 1]
- [Requirement 2]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Technical Notes
[Implementation details, API references, dependencies]

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

### Sub-task Format
- Linked to parent issue
- Focused on single responsibility
- Includes implementation details
- Clear acceptance criteria

---

## Integration Points

### Works Well With:
- **Todo lists** - Convert todos into tracked issues
- **Planning mode** - Create issues from implementation plans
- **Feature discussions** - Track features discussed in conversation
- **Bug reports** - Organize related bugs under parent issues

### Best Used After:
- Completing feature planning
- Identifying multiple related bugs
- Discussing implementation approaches
- Finishing initial implementation (for follow-up work)
