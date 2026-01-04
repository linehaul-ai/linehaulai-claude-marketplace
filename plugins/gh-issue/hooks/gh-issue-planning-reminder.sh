#!/bin/bash
#
# gh-issue-planning-reminder.sh
# UserPromptSubmit hook that reminds Claude to suggest creating GitHub issues
# after discussing features, completing implementation plans, or identifying work items
#
# This hook detects keywords related to planning/feature discussions and injects
# context reminding Claude about the gh-issue skill for creating tracked issues.

# Read JSON from stdin
input=$(cat)

# Extract the user prompt from the JSON
prompt=$(echo "$input" | jq -r '.prompt // ""')

# Convert to lowercase for pattern matching
prompt_lower=$(echo "$prompt" | tr '[:upper:]' '[:lower:]')

# Define patterns that suggest planning/feature discussion is happening
# These indicate moments where issue creation might be valuable
planning_patterns=(
    "implement"
    "add feature"
    "new feature"
    "build"
    "create.*api"
    "create.*endpoint"
    "refactor"
    "integrate"
    "set up"
    "setup"
    "add.*support"
    "design"
    "plan"
    "roadmap"
    "breaking down"
    "break down"
    "todo"
    "tasks for"
    "work items"
    "remaining work"
    "follow.?up"
    "next steps"
)

# Patterns that indicate issue creation is already being requested (skip reminder)
already_requesting_issues=(
    "create.*issue"
    "make.*issue"
    "github.*issue"
    "gh.?issue"
    "/gh-issue"
)

# Check if user is already requesting issues (skip reminder)
for pattern in "${already_requesting_issues[@]}"; do
    if echo "$prompt_lower" | grep -qE "$pattern"; then
        # User is already asking for issues, no need for reminder
        echo '{"continue": true, "suppressOutput": true}'
        exit 0
    fi
done

# Check if prompt matches planning patterns
matched=false
for pattern in "${planning_patterns[@]}"; do
    if echo "$prompt_lower" | grep -qE "$pattern"; then
        matched=true
        break
    fi
done

if [ "$matched" = true ]; then
    # Inject context about gh-issue skill
    cat << 'EOF'
{
  "continue": true,
  "additionalContext": "REMINDER: After completing this planning/feature discussion, consider using the /gh-issue skill to create GitHub issues for tracking. The gh-issue-creator agent can create well-structured parent issues with sub-tasks, ensuring work doesn't get lost. Use it when: discussing new features, identifying bugs, completing implementation plans, or when the user asks about 'remaining work' or 'next steps'."
}
EOF
else
    # No planning patterns detected, continue silently
    echo '{"continue": true, "suppressOutput": true}'
fi

exit 0
