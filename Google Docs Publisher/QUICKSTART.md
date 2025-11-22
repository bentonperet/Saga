# Quick Start Guide

## ⚡ Get Publishing in 10 Minutes

### Phase 1: Google Setup (5 minutes)

This is a **one-time setup**. Once complete, you'll never need to do it again.

#### Step 1: Create Google Cloud Project & Enable APIs

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create a new project**
   - Click the project dropdown at the top (says "Select a project")
   - Click **"NEW PROJECT"**
   - Project name: `Obsidian Publisher` (or any name you like)
   - Click **"CREATE"**
   - Wait a few seconds, then select your new project from the dropdown

3. **Enable the APIs** (allows the tool to create Google Docs)
   - In the left sidebar, click **"APIs & Services"** → **"Library"**
   - Search for: `Google Docs API`
   - Click it → Click **"ENABLE"**
   - Click the back arrow, then search for: `Google Drive API`
   - Click it → Click **"ENABLE"**

#### Step 2: Download Your Credentials

**This is the only technical file you need to download!**

1. **Create OAuth credentials**
   - Go to **"APIs & Services"** → **"Credentials"** (in left sidebar)
   - Click the blue **"+ CREATE CREDENTIALS"** button at the top
   - Choose **"OAuth client ID"**

2. **First time? Configure consent screen**
   - If prompted, click **"CONFIGURE CONSENT SCREEN"**
   - Choose **"External"** → Click **"CREATE"**
   - Fill in:
     - App name: `Obsidian Publisher`
     - User support email: (your email)
     - Developer contact: (your email again)
   - Click **"SAVE AND CONTINUE"** through all screens (you can skip optional fields)
   - Under "Test users", click **"+ ADD USERS"** and add your own email
   - Click **"SAVE AND CONTINUE"** until you're back to the credentials page

3. **Create the credentials**
   - Click **"+ CREATE CREDENTIALS"** → **"OAuth client ID"** again
   - Application type: **"Desktop app"**
   - Name: `Obsidian Publisher Desktop` (or any name)
   - Click **"CREATE"**
   - You'll see a popup with your Client ID - click **"DOWNLOAD JSON"** (the download arrow ⬇️)

4. **Rename and move the file**
   - Find the downloaded file (usually in Downloads folder)
   - It's named something like `client_secret_123456.json`
   - **Rename it to:** `client_secret.json` (exactly this name)
   - **Move it to:** `Google Docs Publisher/client_secret.json`

   💡 **Can't find the folder?** In Obsidian, right-click your vault name → "Show in system explorer/Finder"

#### Step 3: First Authentication

**Let Claude Code handle this step!**

1. **In Claude Code, send this message:**
   ```
   Please authenticate the Google Docs Publisher.
   Run: node index.js TEST-MINIMAL.md
   ```

2. **Claude will give you a URL** - click it to open in your browser

3. **Authorize the app:**
   - Choose your Google account
   - If you see **"Google hasn't verified this app"**:
     - This is normal! It's YOUR app, so it's safe.
     - Click **"Advanced"**
     - Click **"Go to Obsidian Publisher (unsafe)"** ← (it's safe, Google just hasn't reviewed your personal app)
   - Click **"Allow"** to grant permissions

4. **Copy the authorization code** from the browser and paste it back to Claude Code

5. ✅ **Done!** A file called `token.json` is created. You're authenticated forever (or until you delete this file).

### Phase 2: Obsidian Setup (5 minutes)

This connects the "Publish" button to your Obsidian hotkey.

#### Step 1: Install the Shell Commands Plugin

1. **Open Obsidian Settings**
   - Click the gear icon ⚙️ in the bottom-left
   - Or press `Cmd+,` (Mac) / `Ctrl+,` (Windows)

2. **Enable Community Plugins**
   - Click **"Community plugins"** in the left sidebar
   - If you see a warning about "Safe mode", click **"Turn on community plugins"**

3. **Install Shell Commands**
   - Click the **"Browse"** button
   - In the search box, type: `Shell commands`
   - Find the plugin by **Jare Satkalahti** (has a terminal icon)
   - Click **"Install"**
   - After it installs, click **"Enable"**

#### Step 2: Add the Publish Command

1. **Go to Shell Commands settings**
   - Still in Settings, find **"Shell commands"** in the left sidebar (under Community plugins)
   - Click it

2. **Create a new command**
   - Click the **"+ New shell command"** button at the top
   - You'll see a text box for the command

3. **Get the path from Claude Code:**

   💡 **Ask Claude to help!** Send this message to Claude Code:
   ```
   What's the full path to publish-active.sh that I should use in Obsidian Shell Commands?
   ```

   Claude will give you the exact path to copy/paste. It will look something like:
   ```
   "/Users/YourName/.../Google Docs Publisher/publish-active.sh"
   ```

4. **Configure the command:**
   - Paste the path in the command box
   - In the **"Alias"** field (below the command), type: `Publish to Google Docs`
   - Click the **"Output"** tab (at the top of this command)
   - Find **"Output channel for stdout"** dropdown
   - Select: **"Modal"** (this shows the Google Docs link in a popup)
   - Click the checkmark ✓ to save

#### Step 3: Add a Hotkey

1. **Open Hotkeys settings**
   - In Settings, find **"Hotkeys"** in the left sidebar (near the bottom)

2. **Find your command**
   - In the search box at the top, type: `Publish to Google Docs`
   - You should see: **"Shell commands: Publish to Google Docs"**

3. **Set your hotkey**
   - Click the **"+"** icon next to it
   - Press your desired key combination (e.g., `Alt+Shift+P` on Windows, `Option+Shift+P` on Mac)
   - The hotkey appears next to the command
   - Close Settings

#### Step 4: Test It! (30 seconds)

1. **Open any markdown file in Obsidian**
2. **Press your hotkey** (e.g., `Alt+Shift+P`)
3. **Wait a moment** - you'll see a modal popup with the Google Docs URL
4. **Click the URL** to open your newly created Google Doc
5. **Verify the formatting** looks good! ✅

🎉 **You're done!** From now on, just press your hotkey to publish any note to Google Docs.

---

## 🎯 What Works Right Now

When you publish a note, these markdown elements will be beautifully formatted in Google Docs:

**✅ Fully Working:**
- **Headings** (H1-H6) - Styled with PACHYDERM GLOBAL brand colors (Rubik font, custom blues)
- **Text formatting** - **Bold**, *italic*, ~~strikethrough~~, `inline code`
- **Links** - Become clickable blue links in Google Docs
- **Lists** - Both bulleted and numbered lists
- **Code blocks** - Monospace font with gray background
- **Blockquotes** - Indented and italicized
- **Horizontal rules** - Convert to lines
- **Tables** - Rendered as formatted text with borders

**❌ Not Supported:**
- Images (shows placeholder text: `[Image: filename]`)
- Footnotes
- Task lists (converts to regular bullets)
- Mermaid diagrams

**📊 About Tables:**
Tables render as formatted text (similar to markdown) rather than native Google Docs tables. This keeps them readable and reliable while we work on native table support for a future version.

---

## 🆘 Troubleshooting

### "I can't find where to move client_secret.json"
💡 **Ask Claude Code:** "Where should I put the client_secret.json file?" and Claude will tell you the exact path.

Or in Obsidian: Right-click your vault name in the left sidebar → "Show in system explorer" (Windows) or "Reveal in Finder" (Mac), then navigate to the `Google Docs Publisher` folder.

### "Google hasn't verified this app"
This is normal! You're using your own personal app. Click **"Advanced"** → **"Go to Obsidian Publisher (unsafe)"** - it's completely safe because YOU created it.

### "Hotkey doesn't work"
- First, try using the Command Palette instead: Press `Cmd+P` (Mac) or `Ctrl+P` (Windows), then type "Publish to Google Docs"
- If that works, check your hotkey in Settings → Hotkeys
- If nothing works, ask Claude Code: "Help me debug the Shell Commands setup"

### "Wrong file gets published"
The tool publishes whichever file you edited most recently. To ensure the right file publishes:
1. Click into the file you want to publish
2. Make any tiny edit (add a space, delete it)
3. Save (`Cmd+S` or `Ctrl+S`)
4. Now press your hotkey - it will publish that file

### "Command not found: node"
💡 **Ask Claude Code:** "Please help me fix the node command path in publish-active.sh"

### Need More Help?
- **Detailed setup guide:** [SETUP.md](SETUP.md)
- **Obsidian integration details:** [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md)
- **What's coming next:** [ROADMAP.md](ROADMAP.md)
- **Ask Claude Code:** Claude can help troubleshoot any step!

**Happy publishing!** 🚀
