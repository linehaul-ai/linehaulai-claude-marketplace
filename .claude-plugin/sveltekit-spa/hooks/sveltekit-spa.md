# SvelteKit SPA Hook

## Purpose

This hook automatically provides contextual reminders about SvelteKit SPA best practices when you're working on Svelte frontend files.

## How It Works

**Trigger**: Fires before `Read`, `Edit`, or `Write` operations on files matching:
- File extensions: `.svelte`, `.ts`, `.js`
- Paths containing: `src/routes`, `src/lib`, `svelte.config`, or `vite.config`

**Action**: Injects a reminder message with key SPA conventions into the context, including:
- SSR configuration reminders
- Environment variable usage
- Backend separation patterns
- TypeScript conventions
- Testing reminders
- Security considerations
- Reference to the `sveltekit-spa` skill

## Files

- **Hook Script**: `~/.claude/hooks/sveltekit-spa-reminder.sh`
- **Configuration**: `~/.claude/settings.json` (hooks.PreToolUse section)

## Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read|Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/sveltekit-spa-reminder.sh",
            "timeout": 5,
            "suppressOutput": false
          }
        ]
      }
    ]
  }
}
```

## Testing

Test the hook manually:

```bash
# Test with a SvelteKit file (should show reminder)
echo '{"tool_name": "Read", "tool_input": {"file_path": "/path/to/src/routes/+page.svelte"}}' | \
  ~/.claude/hooks/sveltekit-spa-reminder.sh

# Test with a non-SvelteKit file (should silently allow)
echo '{"tool_name": "Read", "tool_input": {"file_path": "/path/to/README.md"}}' | \
  ~/.claude/hooks/sveltekit-spa-reminder.sh
```

## Customization

To modify the reminder message, edit the `context` field in the hook script at:
`~/.claude/hooks/sveltekit-spa-reminder.sh`

To change which files trigger the hook, modify the regex patterns in the conditional:
```bash
if [[ -n "$file_path" ]] && [[ "$file_path" =~ \.(svelte|ts|js)$ ]] && [[ "$file_path" =~ (src/routes|src/lib|svelte\.config|vite\.config) ]]; then
```

## Disabling the Hook

To temporarily disable without deleting:

1. Open `~/.claude/settings.json`
2. Remove or comment out the `hooks` section
3. Restart Claude Code or reload settings

## Related

This hook complements the `sveltekit-spa` skill located at:
`~/.claude/skills/sveltekit-spa/SKILL.md`

## Version

- Created: 2025-12-08
- Compatible with: Claude Code hooks system
- Requires: bash, jq (JSON processor)
