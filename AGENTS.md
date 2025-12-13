# Instructions for Agents

This document provides guidelines for AI agents working on the Linehaul AI Claude Marketplace repository.

## Project Structure

- **Root Directory**: Contains project-level documentation (`README.md`, `CLAUDE.md`, `LICENSE`) and configuration.
- **Plugin Directory**: All plugin code is located in `.claude-plugin/`.
- **Registry**: `marketplace.json` in `.claude-plugin/` is the central registry for all plugins.

## Development Guidelines

### 1. Plugin Structure
When creating or modifying plugins, adhere to the following structure based on the plugin type:

- **Full Plugins** (e.g., `golang-orchestrator`):
  - Must have a `.claude-plugin/plugin.json` manifest.
  - typically contain `commands/`, `skills/`, `agents/`, and `docs/` directories.
  - Should have their own `README.md`, `INSTALL.md`, and `PLUGIN_OVERVIEW.md`.

- **Skill Plugins** (e.g., `sequential-thinking`):
  - Must contain a `SKILL.md` file.
  - May contain a `references/` directory for specialized documentation.
  - Do not strictly require a `plugin.json` if they are pure skill definitions, but it is good practice if they are to be installed independently.

- **Manifest (`plugin.json`)**:
  - Must be valid JSON.
  - Must contain `name`, `version`, `description`, and `author` fields.
  - Ensure version numbers follow semantic versioning.

### 2. Marketplace Registry
- **Registration**: If adding a new plugin, you **must** register it in `.claude-plugin/marketplace.json`.
- **Paths**: The `source` path in `marketplace.json` must be relative to the `.claude-plugin` directory (e.g., `./.claude-plugin/my-new-plugin`).
- **Metadata**: Ensure the name and description in `marketplace.json` match the plugin's purpose.

### 3. Documentation
- **Source of Truth**: Maintain `CLAUDE.md` as the single source of truth for architecture and detailed descriptions.
- **Updates**:
  - Update `README.md` if high-level changes are made (e.g., adding a new key plugin).
  - Update individual plugin documentation when modifying plugin behavior.
  - Use `AUTO-MANAGED` blocks in `CLAUDE.md` if present (or respect existing ones) to keep documentation synchronized.

### 4. Naming Conventions
- **Directories**: Use `kebab-case` for plugin directory names (e.g., `my-plugin-name`).
- **Files**:
  - Skill definitions: `SKILL.md` or `skills/my-skill.md`.
  - Slash commands: `commands/my-command.md`.
  - Agents: `agents/my-expert.md`.

## Verification Steps

Before submitting changes, perform the following verifications:

1.  **JSON Validity**: Ensure `marketplace.json` and any `plugin.json` files are valid JSON.
2.  **Path Validity**: Verify that any paths referenced in `marketplace.json` actually exist in the file system.
3.  **Markdown Formatting**: Ensure all markdown files are well-formatted and links are valid.
4.  **Consistency**: Check that the plugin name in the directory matches the name in `plugin.json` and `marketplace.json`.
