# Google Docs Publisher Setup Guide

This guide will walk you through setting up the Obsidian → Google Docs publisher.

## Prerequisites

- Node.js installed (v16 or higher)
- Google account
- Obsidian with your vault

## Part 1: Google Cloud Setup (One-time)

### Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" (top bar) → "New Project"
3. Project name: `Obsidian Publisher` (or your choice)
4. Click "Create"
5. Wait for project creation, then select it

### Step 2: Enable Required APIs

1. In your project, go to **APIs & Services** → **Enable APIs and Services**
2. Search for and enable:
   - **Google Docs API**
   - **Google Drive API**

### Step 3: Create OAuth Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click **+ CREATE CREDENTIALS** → **OAuth client ID**

   **First-time setup?** You'll need to configure the OAuth consent screen:
   - Click "Configure Consent Screen"
   - Choose **External** (unless you have Google Workspace)
   - Fill in required fields:
     - App name: `Obsidian Publisher`
     - User support email: your email
     - Developer contact: your email
   - Click **Save and Continue**
   - Skip "Scopes" (click Save and Continue)
   - Add yourself as a test user
   - Click **Save and Continue**, then **Back to Dashboard**

3. Now create the OAuth client:
   - Click **+ CREATE CREDENTIALS** → **OAuth client ID** again
   - Application type: **Desktop app**
   - Name: `Obsidian Publisher Desktop`
   - Click **Create**

4. **Download the credentials:**
   - Click the Download icon (⬇️) next to your new OAuth client
   - Save as `client_secret.json`
   - Move this file to: `Google Docs Publisher/client_secret.json`

### Step 4: First-Time Authentication

1. Open Terminal and navigate to the publisher directory:
   ```bash
   cd "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher"
   ```

2. Run a test publish on any markdown file:
   ```bash
   node index.js "../path/to/test.md"
   ```

3. You'll see:
   ```
   === FIRST TIME SETUP ===
   Authorize this app by visiting this URL:

   https://accounts.google.com/o/oauth2/v2/auth?...
   ```

4. **Copy the URL** and paste into your browser

5. You may see "Google hasn't verified this app":
   - Click "Advanced"
   - Click "Go to Obsidian Publisher (unsafe)"
   - This is safe because you created the app

6. Grant permissions (allow access to Google Docs and Drive)

7. Copy the **authorization code** from the browser

8. Paste it back into the Terminal

9. You'll see:
   ```
   ✓ Token stored successfully to token.json
   ✓ Future runs will use this token automatically
   ```

**Done!** You're now authenticated. The `token.json` file will be used for all future publishes.

---

## Part 2: Obsidian Integration

### Option A: Using Shell Commands Plugin (Recommended)

1. **Install the plugin:**
   - In Obsidian: Settings → Community plugins → Browse
   - Search for "Shell commands"
   - Install and enable

2. **Add a new shell command:**
   - Settings → Shell commands → New shell command
   - Command:
     ```bash
     node "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher/index.js" "{{file_path:absolute}}"
     ```
   - Alias: `Publish to Google Docs`

3. **Add a hotkey:**
   - Settings → Hotkeys
   - Search for "Shell commands: Publish to Google Docs"
   - Set your preferred hotkey (e.g., `Cmd+Shift+P`)

4. **Test it:**
   - Open any markdown file
   - Press your hotkey
   - Check the output in Obsidian's console (Cmd+Option+I)
   - The Google Docs URL will be in the output

### Option B: Using Templater Plugin

1. **Install Templater:**
   - Settings → Community plugins → Browse
   - Search for "Templater"
   - Install and enable

2. **Create a script:**
   - Settings → Templater → Script files folder
   - Create a new file: `publishToGoogleDocs.js`
   - Add:
     ```javascript
     async function publishToGoogleDocs(tp) {
       const filePath = tp.file.path(true);
       const command = `node "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher/index.js" "${filePath}"`;

       const result = await tp.user.system(command);
       return result;
     }

     module.exports = publishToGoogleDocs;
     ```

3. **Add a hotkey** in Templater settings to run this script

---

## Part 3: Usage

### Command Line

```bash
# Basic usage
node index.js "/path/to/file.md"

# Append Google Docs URL to markdown file
node index.js "/path/to/file.md" --append-url

# Disable clipboard copy (URL won't auto-copy)
node index.js "/path/to/file.md" --no-clipboard

# Debug mode (show full error stack traces)
node index.js "/path/to/file.md" --debug
```

### From Obsidian

1. Open the markdown file you want to publish
2. Press your hotkey (or run the command from Command Palette)
3. Wait for the process to complete
4. The Google Docs URL will be:
   - Printed in the console
   - Copied to clipboard (macOS)
   - Optionally appended to your markdown file

---

## Supported Markdown Features

✅ **Fully Supported:**
- Headings (H1-H6) with brand styling
- Paragraphs with inline formatting:
  - **Bold**
  - *Italic*
  - ~~Strikethrough~~
  - `Inline code`
  - [Links](https://example.com)
- Bulleted lists
- Numbered lists
- Code blocks with syntax highlighting
- Tables with headers
- Blockquotes
- Horizontal rules

⚠️ **Partial Support:**
- Images (converted to `[Image: alt text]` placeholders)
- Nested lists (single level works best)

❌ **Not Supported:**
- Footnotes
- Task lists (converted to regular bullets)
- Mermaid diagrams
- Embedded notes

---

## Customizing Brand Styles

Edit `brandConfig.js` to customize:
- Font families
- Font sizes
- Colors (hex format)
- Line spacing
- Spacing before/after paragraphs

Example:
```javascript
H1: {
  fontFamily: 'Rubik',
  color: '#044A74',
  fontSizePt: 20,
  bold: true,
  lineSpacing: 1.10,
  beforeSpacingPt: 12,
  afterSpacingPt: 6
}
```

---

## Troubleshooting

### "client_secret.json not found"
- Make sure you downloaded the OAuth credentials
- Place the file in `Google Docs Publisher/client_secret.json`

### "Error retrieving access token"
- Delete `token.json` and re-authenticate
- Make sure you're using the correct Google account

### "Permission denied" errors
- Check that you enabled both Google Docs API and Drive API
- Re-run the OAuth flow

### "File not found" from Obsidian
- Verify the file path in your shell command
- Try using absolute paths instead of relative
- Check that `{{file_path:absolute}}` is supported by your plugin

### Tables not formatting correctly
- Make sure your markdown tables have proper syntax
- Tables with merged cells aren't supported
- Try simplifying complex tables

---

## Security Notes

- **`client_secret.json`**: Contains your OAuth client credentials (not sensitive, but keep private)
- **`token.json`**: Contains your personal access token (keep this private!)
- Both files are in `.gitignore` and won't be committed to version control

---

## Next Steps

- Test with a simple markdown file first
- Gradually test more complex features (tables, code blocks, etc.)
- Customize brand styles in `brandConfig.js`
- Set up your preferred Obsidian hotkey

**Need help?** Check the error messages or run with `--debug` flag for detailed output.
