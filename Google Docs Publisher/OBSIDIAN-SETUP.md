# Obsidian Integration Guide

**Complete step-by-step guide to adding a "Publish to Google Docs" button in Obsidian.**

## How It Works

When you press your hotkey (like `Alt+Shift+P`), the tool:
1. Finds whichever markdown file you edited most recently
2. Converts it to a beautifully formatted Google Doc
3. Shows you the link in a popup
4. Copies the link to your clipboard (on Mac)

**Takes about 5 minutes to set up, then works forever!**

---

## Setup: Install Shell Commands Plugin

**What's the Shell Commands plugin?** It lets you run scripts (like our publisher) from inside Obsidian using a hotkey or command.

### Step 1: Enable Community Plugins

1. **Open Obsidian Settings**
   - Click the gear icon ⚙️ in the bottom-left corner
   - Or press `Cmd+,` (Mac) / `Ctrl+,` (Windows)

2. **Turn on Community Plugins**
   - In the left sidebar, click **"Community plugins"**
   - If you see "Safe mode is enabled", click **"Turn on community plugins"**
   - (This is safe - community plugins are reviewed by Obsidian)

### Step 2: Install Shell Commands

1. **Browse plugins**
   - Still in the Community plugins section, click the **"Browse"** button

2. **Find Shell Commands**
   - In the search box at the top, type: `Shell commands`
   - Look for the plugin by **Jare Satkalahti** (it has a terminal icon 🖥️)

3. **Install and enable**
   - Click on the plugin
   - Click **"Install"**
   - After it installs, click **"Enable"**
   - Close the plugin browser

---

## Add the Publish Command

Now we'll tell the plugin what command to run when you press your hotkey.

### Step 3: Configure Shell Commands

1. **Open Shell Commands settings**
   - Still in Settings, scroll down in the left sidebar to find **"Shell commands"** (under "Community plugins")
   - Click it

2. **Create a new command**
   - At the top, click the **"+ New shell command"** button
   - You'll see a text box for entering a command

3. **Get the command path**

   💡 **Ask Claude Code for help!** This is the easiest way:
   ```
   What's the full path to publish-active.sh that I should paste into Obsidian Shell Commands?
   ```

   Claude will give you something like:
   ```
   "/Users/YourName/.../Google Docs Publisher/publish-active.sh"
   ```

   **Why is this needed?** The path tells Obsidian exactly where to find the publisher script on your computer.

4. **Enter the command**
   - Paste the full path (with quotes) into the command box
   - Make sure it includes quotes around the whole path!

5. **Add an alias (friendly name)**
   - In the **"Alias"** field below the command, type: `Publish to Google Docs`
   - This is what you'll see in Obsidian's command palette

6. **Configure the output**
   - At the top of this command's settings, click the **"Output"** tab
   - Find the dropdown for **"Output channel for stdout"**
   - Change it from "Ignore" to: **"Modal"**
   - (This makes the Google Docs link appear in a popup window)

7. **Save it**
   - Click the checkmark ✓ icon to save your command

---

## Add a Hotkey

Let's make it easy to publish with just a keyboard shortcut!

### Step 4: Set Up Your Hotkey

1. **Open Hotkeys settings**
   - Still in Settings, find **"Hotkeys"** in the left sidebar (near the bottom)
   - Click it

2. **Find your command**
   - In the search box at the top, type: `Publish to Google Docs`
   - You should see: **"Shell commands: Publish to Google Docs"**

3. **Assign a hotkey**
   - Click the **"+"** icon next to the command
   - Press your desired key combination
   - Suggestions:
     - **Mac:** `Option+Shift+P` or `Cmd+Shift+G`
     - **Windows:** `Alt+Shift+P` or `Ctrl+Shift+G`
   - The hotkey will appear next to the command

4. **Close Settings**
   - Your hotkey is now active!

---

## Test It!

### Step 5: Publish Your First Doc

1. **Open any markdown file** in Obsidian

2. **Press your hotkey** (e.g., `Alt+Shift+P`)

3. **Wait a moment** (usually 2-5 seconds)

4. **See the popup!**
   - A modal window appears with the Google Docs URL
   - The URL is automatically copied to your clipboard (on Mac)

5. **Open the doc**
   - Click the link or paste it (`Cmd+V` / `Ctrl+V`) into your browser
   - Check that the formatting looks good!

🎉 **Success!** You can now publish any note with a single hotkey.

---

## Behind the Scenes: How It Works

**Technical details** (you don't need to know this to use it, but it's interesting!)

The tool uses a script called `publish-active.sh` that:
1. Searches your entire vault for `.md` files
2. Finds the one that was modified most recently
3. Sends it to the publisher
4. Returns the Google Docs URL

**Why does it find the most recent file?** The file you're currently working on is always the most recently edited one. This approach is more reliable than trying to detect which file is "active" in Obsidian.

**Why not use the Shell Commands plugin's `{{file_path}}` variable?** We tried that first! But it had issues with special characters in file paths getting escaped incorrectly. The "find most recent file" approach works perfectly every time.

---

## Troubleshooting

### Nothing happens when I press the hotkey

**Step 1: Test with Command Palette**
- Press `Cmd+P` (Mac) or `Ctrl+P` (Windows) to open Command Palette
- Type: "Publish to Google Docs"
- Press Enter

Does it appear in the list?
- **Yes, and it works:** Your hotkey just isn't set up correctly. Go back to Settings → Hotkeys and try a different key combination.
- **Yes, but nothing happens:** See "Modal shows but nothing happens" below
- **No, it doesn't appear:** The Shell Commands plugin isn't recognizing your command. Go back to Settings → Shell commands and check that your command is there and enabled.

### Modal shows but no URL (or shows an error)

1. **Check authentication:**
   - Have you completed the Google Cloud setup? See [QUICKSTART.md](QUICKSTART.md)
   - Do you have both `client_secret.json` and `token.json` files?

2. **Test in terminal:**
   - 💡 Ask Claude Code: "Please test the publisher by running: node index.js TEST-MINIMAL.md"
   - If that works, the hotkey should work too
   - If that fails, you need to complete the Google setup first

### "Command not found: node"

This means the script can't find Node.js on your computer.

💡 **Ask Claude Code:** "Help me fix the node command path in publish-active.sh"

Or fix it yourself:
1. Open Terminal/Command Prompt
2. Type: `which node` (Mac/Linux) or `where node` (Windows)
3. Copy the path it shows
4. Open `publish-active.sh` in a text editor
5. On the last line, replace `/usr/local/bin/node` with your path
6. Save and try again

### Wrong file gets published

The tool publishes whichever markdown file was edited most recently. To make sure the right file publishes:

**Method 1: Make it the most recent**
1. Click into the file you want to publish
2. Make a tiny edit (add a space, then delete it)
3. Save (`Cmd+S` or `Ctrl+S`)
4. Press your hotkey - it will publish that file

**Method 2: Use Command Palette for specific files**
If you have multiple files open and haven't edited the one you want recently, repeat Method 1.

**Method 3: Use Terminal for precise control**
💡 Ask Claude Code: "Please publish this specific file: path/to/my-note.md"

### Hotkey conflicts with another plugin

If your hotkey doesn't work, it might conflict with another plugin or Obsidian command.

**Fix:**
1. Settings → Hotkeys
2. Search for your key combination (e.g., "Alt+Shift+P")
3. See if something else is using it
4. Either remove the other hotkey or choose a different one for publishing

---

## Alternative: Command Palette Only

**Don't want to use a hotkey?** You can publish through the Command Palette:

1. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
2. Type: "Publish to Google Docs"
3. Press Enter
4. Wait for the popup with your Google Docs URL

This works great if you only publish occasionally!

---

## Tips & Best Practices

### Which file gets published?

**Remember:** The most recently edited/saved file is what gets published.

**Good workflow:**
1. Write your note
2. Save it (`Cmd+S` or `Ctrl+S`)
3. Immediately press your publish hotkey
4. The doc you just saved will be published

**Multiple notes open?**
- Just edit and save the one you want to publish before pressing the hotkey
- Or close all other notes to avoid confusion

### Publishing vs. Updating

**Important:** Each time you press the hotkey, you create a **NEW** Google Doc.

- If you need to make changes, either:
  - Edit directly in Google Docs (doesn't update your markdown)
  - Edit your markdown and publish again (creates a new doc)

**Future feature:** Document versioning/updating is planned for v2.0 (see [ROADMAP.md](ROADMAP.md))

### Testing & Experimenting

**Use TEST-MINIMAL.md first!**
- Before publishing important notes, test with the included `TEST-MINIMAL.md` file
- This helps you understand the formatting and make sure everything works
- You can delete test docs from Google Drive afterward

### Batch Publishing

**Not yet supported,** but here's a workaround:

💡 Ask Claude Code to help: "Can you publish all markdown files in my Notes folder?"

Claude can write a quick script to loop through files and publish them one by one.

---

## Getting Help

**Something not covered here?**
- Check [SETUP.md](SETUP.md) for detailed troubleshooting
- Read [QUICKSTART.md](QUICKSTART.md) for the condensed version
- See [ROADMAP.md](ROADMAP.md) for upcoming features
- Ask Claude Code: "Help me with [specific issue]"

**Happy publishing!** 🚀
