#!/bin/bash
# shadcn-component-reminder.sh
# Hook for shadcn-svelte component development
# Triggers when editing files in $lib/components/ui/

# Get the file path from Claude hook environment
FILE_PATH="${CLAUDE_FILE_PATH:-$1}"

# Exit silently if no file path
[ -z "$FILE_PATH" ] && exit 0

# Check if path contains shadcn component directories
if [[ "$FILE_PATH" == *"components/ui/"* ]] || [[ "$FILE_PATH" == *"lib/components/ui/"* ]]; then
  cat << 'EOF'
shadcn-svelte component detected

Patterns:
- Use cn() for class merging
- Props: Use $props() not export let
- Events: onclick not on:click (Svelte 5)
- Variants: Define in component with cva()

Commands:
- /shadcn add     - Install components
- /shadcn form    - Form patterns
- /shadcn table   - DataTable setup
- /shadcn theme   - CSS customization

Skill: shadcn-svelte-skill
EOF
fi
