#!/bin/bash
# golang-orchestrator-reminder.sh
# Hook for golang-orchestrator plugin
# Triggers when editing Go files

# Get the file path from Claude hook environment
FILE_PATH="${CLAUDE_FILE_PATH:-$1}"

# Exit silently if no file path
[ -z "$FILE_PATH" ] && exit 0

# Check if the file has .go extension
if [[ "$FILE_PATH" == *.go ]]; then
  cat << 'EOF'
golang-orchestrator plugin available

Use this plugin for Go backend development with Echo Router.

Commands:
- /golang-echo-orchestrator:backend-setup                 - Simple backend setup
- /golang-echo-orchestrator:backend-setup-orchestration   - Full orchestrated setup with subagents

Specialized Agents:
- golang-expert         - Go architecture and best practices
- echo-router-expert    - Echo framework and HTTP routing

Core Skills:
- effective-go          - Golang idioms and conventions
- echo-router-skill     - Echo framework patterns

Use Cases:
- Building production REST APIs
- Implementing middleware patterns
- Designing scalable backend architectures
- Following Go best practices (effective-go)

Tip: Use /golang-echo-orchestrator:backend-setup-orchestration for collaborative
two-agent design of your backend system. It spawns both golang-expert and
echo-router-expert agents to work together.
EOF
fi
