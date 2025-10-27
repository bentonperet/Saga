# Obsidian Integration Guide

## Current Solution: Publish Active File

We use `publish-active.sh` which automatically finds the most recently edited markdown file (the one you're working on).

## Setup: Shell Commands Plugin

### 1. Install Shell Commands Plugin

1. Open **Settings** → **Community plugins**
2. Click **Browse**
3. Search **"Shell commands"**
4. Click **Install**, then **Enable**

### 2. Add the Publish Command

1. Go to **Settings** → **Shell commands**
2. Click **New shell command** (+ icon)
3. In the command field, paste:

   ```bash
   "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher/publish-active.sh"
   ```

4. **Alias**: `Publish to Google Docs`
5. Click the **Output** tab
6. Set **"Output channel for stdout"** to: `Modal`
7. Click checkmark to save

### 3. Add a Hotkey

1. Go to **Settings** → **Hotkeys**
2. Search: `Publish to Google Docs`
3. Find: **Shell commands: Publish to Google Docs**
4. Click **+** icon
5. Press your desired keys (e.g., `Alt+Shift+P`)
6. Done!

### 4. Test It

1. Open any markdown file in Obsidian
2. Press your hotkey (`Alt+Shift+P`)
3. Modal appears with Google Docs URL
4. URL auto-copied to clipboard (macOS)

---

## How It Works

**`publish-active.sh`** finds the most recently modified `.md` file in your vault (excluding the publisher folder and `.obsidian`). This works reliably because the file you're editing is always the most recent.

**Why not use `{{file_path:absolute}}`?**
The Shell Commands plugin's file path variable had issues with escaped characters. The wrapper script avoids this.

---

## Troubleshooting

**Nothing happens when I press hotkey**
- Open Command Palette (`Cmd+P`)
- Type "Publish to Google Docs"
- Does it appear? If not, Shell Commands plugin isn't recognizing the command

**"Command not found: node"**
- Script uses full path `/usr/local/bin/node`
- Should work automatically

**Modal shows but no URL**
- Check that you completed Google OAuth setup (see QUICKSTART.md)
- Try running from terminal first: `node index.js TEST-MINIMAL.md`

**Wrong file gets published**
- The script publishes the most recently modified file
- Save your current file first (makes it the most recent)
- Or use terminal: `node index.js "path/to/specific-file.md"`

---

## Alternative: Command Palette Only

If you prefer not to set a hotkey:

1. Press `Cmd+P` (Command Palette)
2. Type "Publish to Google Docs"
3. Press Enter

---

## Advanced: Optional Flags

Edit the shell command to add flags:

**Append URL to markdown file:**
```bash
"/path/to/publish-active.sh" --append-url
```
(Note: This requires modifying the script to pass flags to index.js)

**Currently supported in terminal only:**
```bash
node index.js "file.md" --append-url --debug
```

---

## Tips

**Multiple files open?**
- Save the file you want to publish (makes it most recent)
- Or close other files

**Publishing frequency:**
- Each publish creates a NEW Google Doc
- To update existing doc, manually edit in Google Docs
- (Doc versioning planned for v2.0)

**Batch publishing:**
- Not yet supported
- Workaround: Use terminal with a loop

---

**Questions?** Check [SETUP.md](SETUP.md) for troubleshooting.
