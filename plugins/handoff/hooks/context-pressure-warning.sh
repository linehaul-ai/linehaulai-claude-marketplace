#!/bin/bash
# Context Pressure Warning Hook
# Triggered by PreCompact event when context reaches ~95% capacity
# Warns the user and suggests creating a handoff before context is compacted

# Read input from stdin
input=$(cat)

# Parse the trigger type (manual or auto)
trigger=$(echo "$input" | jq -r '.trigger // "unknown"')

# Only warn on auto-compaction (user-initiated compaction is intentional)
if [ "$trigger" = "auto" ]; then
    # Output JSON response with warning and options
    cat << 'EOF'
{
  "continue": true,
  "systemMessage": "CONTEXT PRESSURE WARNING: The conversation has reached ~95% of context capacity and auto-compaction is about to occur. Consider creating a handoff document to preserve important context before it's summarized.\n\nOptions:\n1. Run /handoff - Create a handoff document to preserve full context\n2. Continue - Allow compaction to proceed (some context will be summarized)\n3. Run /compact with instructions - Guide what to preserve\n\nRecommendation: If you're in the middle of complex work, create a handoff first.",
  "suppressOutput": false
}
EOF
else
    # Manual compaction - user knows what they're doing
    cat << 'EOF'
{
  "continue": true,
  "suppressOutput": true
}
EOF
fi

exit 0
