# Google Docs Publisher Setup Guide

Complete setup guide with troubleshooting.

## Prerequisites

- Node.js installed (v16+)
- Google account
- Obsidian with your vault

---

## Part 1: Google Cloud Setup (One-time)

### Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Name: `Obsidian Publisher`
4. Click "Create"
5. Select the project

### Step 2: Enable Required APIs

1. Go to **APIs & Services** → **Enable APIs and Services**
2. Search and enable:
   - **Google Docs API**
   - **Google Drive API**

### Step 3: Create OAuth Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click **+ CREATE CREDENTIALS** → **OAuth client ID**

**First-time?** Configure consent screen:
   - Click "Configure Consent Screen"
   - Choose **External**
   - App name: `Obsidian Publisher`
   - User support email: your email
   - Developer contact: your email
   - Click **Save and Continue** through all screens
   - Add yourself as test user

3. Create OAuth client:
   - Application type: **Desktop app**
   - Name: `Obsidian Publisher Desktop`
   - Click **Create**

4. **Download credentials:**
   - Click Download icon (⬇️)
   - Rename to `client_secret.json`
   - Move to: `Google Docs Publisher/client_secret.json`

### Step 4: First-Time Authentication

1. Open Terminal:
   ```bash
   cd "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher"
   node index.js TEST-MINIMAL.md
   ```

2. Copy the URL and open in browser

3. If you see "Google hasn't verified this app":
   - Click **"Advanced"**
   - Click **"Go to Obsidian Publisher (unsafe)"** (it's safe!)

4. Grant permissions

5. Copy authorization code from browser

6. Paste into terminal

7. Success! `token.json` created.

---

## Part 2: Obsidian Integration

See [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md) for full details.

**Quick version:**
1. Install "Shell commands" plugin
2. Add command: `/path/to/publish-active.sh`
3. Set hotkey: `Alt+Shift+P`
4. Press hotkey → Done!

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

**⏸️ In Progress:**
- Tables (see ROADMAP.md)

**❌ Not Supported:**
- Images (placeholder text only)
- Footnotes
- Task lists
- Mermaid diagrams

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

### "client_secret.json not found"
- Download OAuth credentials from Google Cloud
- Place in `Google Docs Publisher/client_secret.json`

### "Error retrieving access token"
- Delete `token.json`
- Re-run authentication
- Check you're using correct Google account

### "Permission denied" errors
- Verify both APIs enabled (Docs + Drive)
- Re-run OAuth flow

### Hotkey doesn't work
- Try Command Palette: `Cmd+P` → "Publish to Google Docs"
- Check Shell Commands plugin is enabled
- Verify command path is correct

### Wrong file gets published
- Script publishes most recently edited file
- Save your current file first
- Or use terminal with specific path

### "Command not found: node"
- Script uses `/usr/local/bin/node`
- If Node is elsewhere, update `publish-active.sh`

### Document looks wrong
- Check `brandConfig.js` for styling
- Verify markdown syntax is correct
- Test with `TEST-MINIMAL.md` first

---

## Security Notes

- `client_secret.json`: OAuth client credentials (keep private)
- `token.json`: Your personal access token (keep private!)
- Both in `.gitignore` (won't commit to git)

---

## Next Steps

- Test with simple files first
- Customize `brandConfig.js`
- Set up your preferred hotkey
- Read [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md) for tips

**Need help?** Run with `--debug`: `node index.js file.md --debug`
