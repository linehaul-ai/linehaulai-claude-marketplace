#!/bin/bash
# SvelteKit SPA Hook - Reminds about SPA conventions when working on Svelte frontend files
# Triggers on Read, Edit, Write operations for .svelte, .ts, .js files in SvelteKit directories

# Read JSON input from stdin
input=$(cat)

# Extract file path from tool input
file_path=$(echo "$input" | jq -r '.tool_input.file_path // .tool_input.path // empty')

# Check if we're working with SvelteKit SPA project files
if [[ -n "$file_path" ]] && [[ "$file_path" =~ \.(svelte|ts|tsx|js)$ ]] && [[ "$file_path" =~ (src/routes|src/lib|svelte\.config|vite\.config) ]]; then

  # Return context injection with SPA reminders
  cat << 'HOOK_END'
{
  "decision": "allow",
  "reason": "Working on SvelteKit SPA frontend file",
  "context": "📘 **SvelteKit SPA Context Active**\n\nYou're working on a SvelteKit Single Page Application (CSR only).\n\n**Critical Configuration:**\n- ✅ Use BOTH `export const ssr = false` AND `export const prerender = false` in all load functions\n- ✅ Root layout (`src/routes/+layout.ts`) must have both exports\n- ✅ Use TypeScript: `+page.ts` and `+layout.ts` (not `.js`)\n\n**Best Practices:**\n- ✅ Use `import.meta.env.VITE_API_URL` for backend API URLs (never hardcode)\n- ✅ Backend is separate (Golang + Echo) - avoid `+server.ts` files\n- ✅ Test with `bun run preview` before deploying\n- ⚠️ localStorage for auth tokens: See Security Considerations in skill\n\n💡 **Need detailed help?** Invoke the `sveltekit-spa` skill for:\n- Complete routing patterns and dynamic routes\n- Data loading patterns with load functions\n- Authentication flows and security\n- Performance optimization strategies"
}
HOOK_END
else
  # Not a SvelteKit file, allow silently
  echo '{"decision": "allow"}'
fi
