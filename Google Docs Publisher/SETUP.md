# Google Docs Publisher - Complete Setup Guide

This is the **detailed version** of the setup guide. For a quicker start, see [QUICKSTART.md](QUICKSTART.md).

## What You'll Need

- **A Google account** (Gmail, Google Workspace, etc.)
- **Obsidian** installed with your vault
- **Node.js** installed (the tool needs this to run)
  - Check if you have it: Ask Claude Code "Do I have Node.js installed?"
  - If not, Claude can help you install it
- **10-15 minutes** for first-time setup

💡 **Throughout this guide, when you see technical steps, you can ask Claude Code to help!**

---

## Part 1: Google Cloud Setup (One-time)

**Why do this?** This gives the tool permission to create Google Docs on your behalf. You only do this once ever.

### Step 1: Create a Google Cloud Project

**What is this?** A "project" in Google Cloud is like a container that holds your app's permissions and settings.

1. **Visit the console:**
   - Go to: [https://console.cloud.google.com/](https://console.cloud.google.com/)
   - Sign in with your Google account

2. **Create new project:**
   - At the very top of the page, click the project dropdown (it says "Select a project")
   - Click **"NEW PROJECT"** button
   - Give it a name: `Obsidian Publisher` (or anything you prefer)
   - Leave "Organization" as "No organization" (unless you know you need something else)
   - Click **"CREATE"**

3. **Select your project:**
   - Wait a few seconds for it to create
   - Click the project dropdown again and select your new project
   - The project name should now appear at the top of the page

### Step 2: Enable Required APIs

**What are APIs?** These are the "switches" that allow the tool to create Docs and save them to your Drive.

1. **Open the API Library:**
   - On the left sidebar, find and click **"APIs & Services"**
   - Click **"Library"** (or "Enable APIs and Services")

2. **Enable Google Docs API:**
   - In the search bar, type: `Google Docs API`
   - Click on the **Google Docs API** result
   - Click the blue **"ENABLE"** button
   - Wait for it to enable (takes a few seconds)

3. **Enable Google Drive API:**
   - Click the back arrow to go back to the API Library
   - Search for: `Google Drive API`
   - Click on it
   - Click **"ENABLE"**

✅ You now have both APIs enabled!

### Step 3: Create OAuth Credentials

**What is OAuth?** It's a secure way for the tool to access your Google account without ever knowing your password.

1. **Go to Credentials page:**
   - In the left sidebar, click **"Credentials"** (under "APIs & Services")

2. **Create OAuth client ID:**
   - At the top, click the blue **"+ CREATE CREDENTIALS"** button
   - Select **"OAuth client ID"**

3. **First time only - Configure consent screen:**

   If this is your first time, Google will ask you to configure a "consent screen" (the page that asks for your permission). Here's how:

   - Click **"CONFIGURE CONSENT SCREEN"**
   - Choose **"External"** (this just means people outside Google can use it - even if that's only you!)
   - Click **"CREATE"**
   - Fill out the form:
     - **App name:** `Obsidian Publisher`
     - **User support email:** Select your email from dropdown
     - **Developer contact information:** Type your email
     - Leave everything else blank
   - Click **"SAVE AND CONTINUE"** at the bottom
   - On the "Scopes" screen, just click **"SAVE AND CONTINUE"** (don't add anything)
   - On the "Test users" screen, click **"+ ADD USERS"** and add your own email address
   - Click **"SAVE AND CONTINUE"**
   - Review the summary and click **"BACK TO DASHBOARD"**

4. **Now create the OAuth client ID:**
   - Click **"Credentials"** in the left sidebar again
   - Click **"+ CREATE CREDENTIALS"** → **"OAuth client ID"** again
   - Application type: Select **"Desktop app"** from the dropdown
   - Name: `Obsidian Publisher Desktop` (or any name you like)
   - Click **"CREATE"**

5. **Download your credentials file:**
   - A popup appears showing your Client ID and Client Secret
   - Click the **"DOWNLOAD JSON"** button (looks like a download arrow ⬇️)
   - The file downloads to your Downloads folder

### Step 4: Move the Credentials File

**This is important!** The tool needs this file in a specific location.

1. **Find the downloaded file:**
   - Open your Downloads folder
   - Look for a file named something like: `client_secret_1234567890.apps.googleusercontent.com.json`

2. **Rename it:**
   - Rename it to exactly: `client_secret.json` (just that, no numbers or extra stuff)

3. **Move it to the right folder:**

   💡 **Not sure where to put it? Ask Claude Code:**
   ```
   Where should I place the client_secret.json file? What's the full path?
   ```

   Or find it yourself:
   - Open Obsidian
   - Right-click on your vault name in the left sidebar
   - Select "Show in system explorer" (Windows) or "Reveal in Finder" (Mac)
   - Find the `Google Docs Publisher` folder
   - Drag `client_secret.json` into that folder

### Step 5: First-Time Authentication

**Now we connect the tool to your Google account.** This is where Claude Code is really helpful!

💡 **Recommended approach - Ask Claude Code:**
```
Please authenticate the Google Docs Publisher by running: node index.js TEST-MINIMAL.md
```

Claude will:
1. Run the authentication command
2. Give you a URL to click
3. Help you through the OAuth flow
4. Handle the authorization code

**If you prefer to do it manually:**

1. Open Terminal (Mac) or Command Prompt (Windows)

2. Navigate to the publisher folder:
   ```bash
   cd "path/to/Google Docs Publisher"
   ```
   (Ask Claude Code for the exact path if you're not sure)

3. Run the authentication:
   ```bash
   node index.js TEST-MINIMAL.md
   ```

4. Copy the long URL that appears and paste it into your browser

5. **Authorize the app:**
   - Choose your Google account
   - You'll see **"Google hasn't verified this app"** - this is normal!
   - Click **"Advanced"**
   - Click **"Go to Obsidian Publisher (unsafe)"** (it's YOUR app, completely safe)
   - Click **"Allow"** when asked for permissions

6. Copy the authorization code from the browser

7. Paste it back into Terminal/Command Prompt and press Enter

8. ✅ **Success!** You'll see a Google Docs URL. A `token.json` file has been created - this means you're authenticated and won't need to do this again!

---

## Part 2: Obsidian Integration

**Now let's add the "Publish" button to Obsidian!**

See [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md) for the complete step-by-step guide.

**Quick summary:**
1. **Install "Shell commands" plugin** in Obsidian (Settings → Community plugins → Browse)
2. **Add the publish command** (ask Claude Code: "What path should I use for the Shell Commands plugin?")
3. **Set a hotkey** like `Alt+Shift+P` (Settings → Hotkeys)
4. **Test it** - Press your hotkey and get a Google Docs link!

💡 The detailed guide walks through every click and setting. It takes about 5 minutes.

---

## Supported Markdown Features

**✅ Fully Supported:**
- Headings (H1-H6) with brand styling
- **Bold**, *italic*, ~~strikethrough~~, `code`
- [Links](https://example.com)
- Bulleted lists
- Numbered lists
- Code blocks
- Blockquotes
- Horizontal rules
- Tables (formatted text with borders)

**❌ Not Supported:**
- Images (placeholder text only)
- Footnotes
- Task lists
- Mermaid diagrams

**📊 Note:** Tables are rendered as formatted text rather than native Google Docs tables, which keeps them readable and reliable.

---

## Customizing Brand Styles

Edit `brandConfig.js`:

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

All Google Fonts supported.

---

## Troubleshooting

### Setup Issues

#### "I can't find the Google Docs Publisher folder"
💡 **Ask Claude Code:** "Where is the Google Docs Publisher folder located?"

Or in Obsidian:
- Right-click your vault name in the left sidebar
- Choose "Show in system explorer" (Windows) or "Reveal in Finder" (Mac)
- Navigate to find the `Google Docs Publisher` folder

#### "client_secret.json not found"
This means the tool can't find your OAuth credentials file. Make sure you:
1. Downloaded the JSON file from Google Cloud Console (Step 3, part 5 above)
2. Renamed it to exactly `client_secret.json`
3. Placed it in the `Google Docs Publisher` folder

💡 **Ask Claude Code:** "Where should I put client_secret.json?" and Claude will give you the exact path.

#### "Error retrieving access token" or "Invalid grant"
Your authentication token might be expired or corrupted. Fix it:
1. Find the `token.json` file in the `Google Docs Publisher` folder
2. Delete it
3. Re-run authentication (see Step 5 above, or ask Claude Code to help)
4. Make sure you're using the same Google account that you added as a "test user" in the consent screen

#### "Permission denied" errors
Your APIs might not be enabled correctly:
1. Go back to Google Cloud Console
2. Check that both **Google Docs API** and **Google Drive API** show as "Enabled"
3. If not, enable them (see Step 2 above)
4. Try authenticating again

#### "Google hasn't verified this app"
**This is completely normal!** You created a personal app for yourself. Google shows this warning for all apps that haven't gone through their public review process (which you don't need).

Just click **"Advanced"** → **"Go to Obsidian Publisher (unsafe)"** - it's YOUR app, it's safe.

#### "Do I have Node.js installed?"
💡 **Ask Claude Code:** "Do I have Node.js installed? If not, can you help me install it?"

Or check yourself:
- Open Terminal (Mac) or Command Prompt (Windows)
- Type: `node --version`
- If you see a version number (like `v18.0.0`), you have it!
- If you see "command not found", you need to install it

### Usage Issues

#### Hotkey doesn't work
Try these steps in order:

1. **Test with Command Palette first:**
   - Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
   - Type: "Publish to Google Docs"
   - Press Enter
   - Does it work? If yes, your hotkey is just not set up correctly

2. **Check Shell Commands plugin:**
   - Settings → Community plugins
   - Is "Shell commands" showing as enabled?
   - If not, toggle it on

3. **Check the command:**
   - Settings → Shell commands
   - Do you see your "Publish to Google Docs" command?
   - Click on it and verify the path is correct
   - Check that "Output channel for stdout" is set to "Modal"

4. **Check your hotkey:**
   - Settings → Hotkeys
   - Search for "Publish to Google Docs"
   - Is there a hotkey assigned?
   - Try changing it to something else (like `Alt+Shift+G`)

5. **Still not working?**
   💡 **Ask Claude Code:** "Help me debug the Shell Commands setup for Obsidian"

#### Wrong file gets published
The tool publishes whichever markdown file in your vault was edited most recently. To ensure the right file publishes:

1. Click into the file you want to publish
2. Make a tiny edit (add a space, then delete it)
3. Save the file (`Cmd+S` or `Ctrl+S`)
4. Now press your publish hotkey - it will publish that file

**Alternative:** Use Terminal/Command Prompt to publish a specific file:
```bash
node index.js "path/to/specific-file.md"
```
(Ask Claude Code to do this for you!)

#### "Command not found: node"
The publish script can't find Node.js on your system.

💡 **Ask Claude Code:** "Please help me fix the node command path in publish-active.sh"

Or fix it yourself:
1. Find where Node.js is installed: Type `which node` in Terminal/Command Prompt
2. Open `publish-active.sh` in a text editor
3. On the last line, replace `/usr/local/bin/node` with the path from step 1
4. Save the file

#### Document looks wrong in Google Docs
**Check your markdown syntax:**
- Test with the included `TEST-MINIMAL.md` file first
- This will show you if the tool is working correctly

**Customize the styling:**
- Edit `brandConfig.js` to change colors, fonts, sizes, spacing
- See the "Customizing Brand Styles" section below

**Unsupported features:**
- Remember that images, tables, footnotes, and task lists aren't fully supported yet
- See "Supported Markdown Features" section above for the complete list

---

## Security & Privacy

**Is my data safe?**

Yes! Here's what you should know:

- **`client_secret.json`** - Your OAuth credentials
  - This allows the tool to request access to your Google account
  - Keep this file private (don't share it or commit to public repos)
  - If compromised, you can delete it in Google Cloud Console and create a new one

- **`token.json`** - Your personal access token
  - This is created after you authorize the app
  - It grants the tool access to create Docs/Drive files on your behalf
  - Keep this private!
  - If compromised, just delete it and re-authenticate

- **Your files**
  - The tool runs locally on your computer
  - Your markdown files never leave your machine except to go directly to Google Docs
  - No third-party servers involved
  - The tool only has permission to create new Google Docs, not read or modify existing ones

- **Git safety**
  - Both sensitive files are in `.gitignore`
  - They won't accidentally get committed to version control

---

## Next Steps

**You're all set up!** Here's what to do next:

1. **Test it out:**
   - Try publishing a simple note first
   - The included `TEST-MINIMAL.md` is perfect for this
   - Verify the formatting looks good in Google Docs

2. **Customize your styling:**
   - Edit `brandConfig.js` to match your brand colors and fonts
   - See the "Customizing Brand Styles" section above
   - You can change colors, fonts, sizes, and spacing

3. **Learn the features:**
   - See what markdown elements are supported
   - Test with different types of content
   - Read [ROADMAP.md](ROADMAP.md) to see what's coming

4. **Get help if needed:**
   - Check the troubleshooting section above
   - Read [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md) for Obsidian-specific tips
   - Ask Claude Code: "Help me with [specific issue]"

**Advanced debugging:**
If you need to see detailed logs, run with `--debug`:
```bash
node index.js file.md --debug
```
(Or ask Claude Code to do this for you!)

**Happy publishing!** 🚀
