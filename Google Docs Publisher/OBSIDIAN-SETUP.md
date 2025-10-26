# Obsidian Integration Guide

## Step-by-Step: Shell Commands Plugin Setup

### 1. Install Shell Commands Plugin

1. Open Obsidian
2. Go to **Settings** (gear icon) → **Community plugins**
3. If you haven't already, click **Turn on community plugins**
4. Click **Browse**
5. Search for **"Shell commands"**
6. Click **Install**, then **Enable**

### 2. Configure the Publish Command

1. Go to **Settings** → **Shell commands**
2. Click **New shell command** (+ icon)
3. In the command field, paste:

   ```bash
   node "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher/index.js" "{{file_path:absolute}}"
   ```

4. **Alias**: Enter `Publish to Google Docs`
5. **Output channel**: Choose `Notification balloon` or `Modal` (so you can see the result)
6. Click the **checkmark** to save

### 3. Add a Hotkey (Optional but Recommended)

1. Go to **Settings** → **Hotkeys**
2. In the search box, type: `Publish to Google Docs`
3. You should see: **Shell commands: Publish to Google Docs**
4. Click the **+** icon next to it
5. Press your desired key combination (e.g., **⌘⇧P** on Mac or **Ctrl+Shift+P** on Windows)
6. The hotkey is now saved

### 4. Test It!

1. Open this file (`TEST.md`) or any markdown file
2. Press your hotkey (or open Command Palette with `Cmd+P` and type "Publish to Google Docs")
3. You should see:
   - A notification that the command is running
   - After a few seconds, the Google Docs URL
   - The URL is automatically copied to your clipboard (macOS)

### 5. Troubleshooting

**"Command not found: node"**
- The Shell Commands plugin might not have Node.js in its PATH
- Fix: In Shell Commands settings, add to "Environment variables":
  ```
  PATH=/usr/local/bin:/opt/homebrew/bin:$PATH
  ```

**"File not found"**
- Make sure you're using `{{file_path:absolute}}`
- Check that the path to `index.js` is correct

**No output visible**
- Change "Output channel" to `Modal` to see full output
- Or enable "Show in status bar" to see status updates

**Authentication errors**
- Make sure you've completed the Google Cloud setup in SETUP.md
- Check that `client_secret.json` exists
- Try running the command from Terminal first to authenticate

---

## Alternative: Command Palette Only (No Hotkey)

If you prefer not to set a hotkey:

1. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows) to open Command Palette
2. Type "Publish to Google Docs"
3. Press Enter

---

## Advanced: Custom Output Handling

If you want more control over what happens after publishing:

### Option 1: Append URL to Note

Add `--append-url` flag to the command:
```bash
node "/path/to/index.js" "{{file_path:absolute}}" --append-url
```

This will add the Google Docs URL at the bottom of your markdown file.

### Option 2: Create a Template

If you use the Templater plugin, you can create a template that:
1. Publishes to Google Docs
2. Inserts the URL in a specific format
3. Updates a "Published" field in frontmatter

Example template:
```javascript
<%*
const filePath = tp.file.path(true);
const cmd = `node "/path/to/index.js" "${filePath}"`;
const result = await tp.user.system(cmd);

// Extract URL from result
const urlMatch = result.match(/https:\/\/docs\.google\.com[^\s]+/);
if (urlMatch) {
  const url = urlMatch[0];
  await tp.file.cursor_append(`\n**Published:** [Google Doc](${url})\n`);
}
%>
```

---

## Workflow Recommendations

### Workflow 1: Quick Publish
1. Write in Obsidian
2. Press hotkey when ready
3. Send Google Docs link to client

### Workflow 2: Review Before Sending
1. Write in Obsidian
2. Press hotkey to publish
3. Open Google Docs link
4. Quick review/tweaks in Google Docs
5. Share with client

### Workflow 3: Version Control
1. Write in Obsidian
2. Press hotkey with `--append-url` flag
3. URL is saved in markdown for future reference
4. Can re-publish anytime (creates new doc)

---

## Tips & Tricks

**Multiple hotkeys for different options:**
- Create multiple shell commands with different flags
- Example:
  - `Cmd+Shift+P`: Basic publish
  - `Cmd+Shift+Option+P`: Publish + append URL

**Batch publishing:**
- Select multiple files in file explorer
- (This requires a custom script - not built-in yet)

**Auto-publish on save:**
- Not recommended (would create many docs)
- But possible with Templater + event handlers

---

**Need help?** Check SETUP.md or run the command with `--debug` flag from Terminal to see detailed error messages.
