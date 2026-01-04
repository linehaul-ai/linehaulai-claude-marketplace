#!/bin/bash
#
# gh-issue-commit-reminder.sh
# PostToolUse hook that suggests creating GitHub issues for follow-up work after git commits
#
# This hook monitors Bash tool calls for git commit operations and injects
# context reminding Claude about the gh-issue skill for tracking follow-up work.

# Read JSON from stdin
input=$(cat)

# Extract tool name
tool_name=$(echo "$input" | jq -r '.tool_name // ""')

# Only process Bash tool calls
if [ "$tool_name" != "Bash" ]; then
    echo '{"continue": true, "suppressOutput": true}'
    exit 0
fi

# Extract command from tool_input
# tool_input is a JSON object containing the bash command
# Handle both cases: tool_input as object directly or as stringified JSON
command=$(echo "$input" | jq -r '.tool_input.command // ""')

# If command is empty, try parsing tool_input as a string containing JSON
if [ -z "$command" ]; then
    tool_input_str=$(echo "$input" | jq -r '.tool_input // ""')
    command=$(echo "$tool_input_str" | jq -r '.command // ""' 2>/dev/null || echo "")
fi

command_lower=$(echo "$command" | tr '[:upper:]' '[:lower:]')

# Check if this is a git commit operation
if echo "$command_lower" | grep -qE "git commit"; then
    # This is a commit! Suggest follow-up issue creation
    cat << 'EOF'
{
  "continue": true,
  "additionalContext": "COMMIT COMPLETED: Consider asking the user if they'd like to create GitHub issues for any follow-up work identified during this implementation. Use the /gh-issue skill or gh-issue-creator agent to create structured issues for: remaining tasks, documentation needs, test coverage, or related improvements discovered during development."
}
EOF
    exit 0
fi

# Not a commit operation, continue silently
echo '{"continue": true, "suppressOutput": true}'
exit 0
