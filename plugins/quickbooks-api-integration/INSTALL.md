# QuickBooks API Integration Plugin - Installation Guide

Complete installation instructions for the QuickBooks API Integration plugin for Claude Code.

## Prerequisites

Before installing this plugin, ensure you have:

- ✅ **Claude Code** installed and working (latest version recommended)
- ✅ **QuickBooks Online Account** (sandbox or production)
- ✅ **Intuit Developer Account** (register at https://developer.intuit.com)
- ✅ **Terminal access** for running installation commands

## Installation Methods

### Method 1: Install from CloudMachines Marketplace (Recommended)

This method installs the plugin from the CloudMachines marketplace repository.

#### Step 1: Add the Marketplace

```bash
/plugin marketplace add /Users/fakebizprez/Developer/repositories/dotfiles cloudmachines-marketplace
```

**Expected Output:**
```
✓ Marketplace 'cloudmachines-marketplace' added successfully
✓ Found 2 plugins: golang-orchestrator, quickbooks-api-integration
```

#### Step 2: Install the Plugin

```bash
/plugin install quickbooks-api-integration@cloudmachines-marketplace
```

**Expected Output:**
```
✓ Installing quickbooks-api-integration v1.0.0
✓ Plugin installed successfully
✓ Commands available: /quickbooks
✓ Skills available: quickbooks-online-api
```

#### Step 3: Verify Installation

```bash
/quickbooks
```

**Expected Output:**
You should see the QuickBooks API Assistant overview with available topics including auth, invoice, payment, sync, debug, and more.

---

### Method 2: Install from Local Development Directory

This method is useful for plugin development or testing local modifications.

#### Step 1: Clone or Navigate to Plugin Directory

```bash
cd /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration
```

#### Step 2: Add as Local Marketplace

```bash
/plugin marketplace add /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration local-quickbooks
```

#### Step 3: Install the Plugin

```bash
/plugin install quickbooks-api-integration@local-quickbooks
```

#### Step 4: Verify Installation

```bash
/quickbooks
```

---

## Verification Steps

After installation, verify the plugin is working correctly:

### 1. Check Plugin List

```bash
/plugin list
```

You should see `quickbooks-api-integration` in the installed plugins list.

### 2. Test the Main Command

```bash
/quickbooks
```

Should display the overview menu with all available topics.

### 3. Test a Specific Topic

```bash
/quickbooks auth
```

Should display OAuth2 authentication setup guide with code examples.

### 4. Verify Skill Access

The skill `quickbooks-online-api` should be automatically available to Claude for answering QuickBooks API questions.

---

## Troubleshooting

### Issue: Marketplace not found

**Error:**
```
✗ Marketplace 'cloudmachines-marketplace' not found
```

**Solution:**
Verify the path is correct and the marketplace.json file exists:
```bash
ls -la /Users/fakebizprez/Developer/repositories/dotfiles/.claude-plugin/marketplace.json
```

If the file doesn't exist, you may need to set up the marketplace first.

---

### Issue: Plugin not found in marketplace

**Error:**
```
✗ Plugin 'quickbooks-api-integration' not found in marketplace 'cloudmachines-marketplace'
```

**Solution:**
Check that the plugin is listed in the marketplace.json:
```bash
cat /Users/fakebizprez/Developer/repositories/dotfiles/.claude-plugin/marketplace.json
```

The plugins array should include:
```json
{
  "name": "quickbooks-api-integration",
  "source": "./quickbooks-api-integration"
}
```

---

### Issue: Command not recognized

**Error:**
```
✗ Command '/quickbooks' not found
```

**Solution:**

1. **Reinstall the plugin:**
   ```bash
   /plugin uninstall quickbooks-api-integration
   /plugin install quickbooks-api-integration@cloudmachines-marketplace
   ```

2. **Verify command file exists:**
   ```bash
   ls -la /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration/commands/quickbooks.md
   ```

3. **Check frontmatter in command file:**
   ```bash
   head -10 /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration/commands/quickbooks.md
   ```

   Should show:
   ```yaml
   ---
   name: quickbooks
   description: QuickBooks Online API integration assistant with guided workflows
   argument-hint: [auth | invoice | payment | sync | debug | entity-name]
   ---
   ```

---

### Issue: Skill not available

**Error:**
Skill doesn't appear when asking QuickBooks API questions.

**Solution:**

1. **Verify skill file exists:**
   ```bash
   ls -la /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration/skills/quickbooks-online-api.md
   ```

2. **Check skill frontmatter:**
   ```bash
   head -10 /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration/skills/quickbooks-online-api.md
   ```

   Should show:
   ```yaml
   ---
   name: quickbooks-online-api
   description: Expert guide for QuickBooks Online API integration covering authentication, CRUD operations, batch processing, and best practices for invoicing, payments, and customer management.
   ---
   ```

3. **Restart Claude Code** (if necessary)

---

### Issue: Permission denied

**Error:**
```
✗ Permission denied: /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration
```

**Solution:**
Check directory permissions:
```bash
ls -la /Users/fakebizprez/Developer/repositories/dotfiles/
```

Ensure you have read access to the plugin directory. If needed:
```bash
chmod -R 755 /Users/fakebizprez/Developer/repositories/dotfiles/quickbooks-api-integration
```

---

## Updating the Plugin

To update to a newer version:

### Step 1: Pull Latest Changes

```bash
cd /Users/fakebizprez/Developer/repositories/dotfiles
git pull origin main
```

### Step 2: Reinstall the Plugin

```bash
/plugin uninstall quickbooks-api-integration
/plugin install quickbooks-api-integration@cloudmachines-marketplace
```

### Step 3: Verify New Version

Check that the new version is installed:
```bash
/plugin list
```

---

## Uninstalling the Plugin

If you need to remove the plugin:

```bash
/plugin uninstall quickbooks-api-integration
```

**Expected Output:**
```
✓ Plugin 'quickbooks-api-integration' uninstalled successfully
```

To also remove the marketplace:
```bash
/plugin marketplace remove cloudmachines-marketplace
```

---

## Next Steps

After successful installation:

1. ✅ **Read the Overview**: See [PLUGIN_OVERVIEW.md](PLUGIN_OVERVIEW.md) for capabilities
2. ✅ **Quick Start**: See [QUICK_START.md](QUICK_START.md) for fastest path to integration
3. ✅ **Start with Auth**: Run `/quickbooks auth` to set up OAuth2
4. ✅ **Explore Topics**: Run `/quickbooks` to see all available workflows

---

## Support

If you encounter issues not covered in this guide:

1. Check the [README.md](README.md) for general information
2. Verify all prerequisites are met
3. Review the troubleshooting section above
4. Check Claude Code documentation for plugin system details

---

**Installation complete?** Run `/quickbooks` to start building your QuickBooks integration!
