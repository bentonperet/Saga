# Quick Start Guide

## ⚡ Get Publishing in 10 Minutes

### Phase 1: Google Setup (5 minutes)

1. **Create project & enable APIs**
   - Go to https://console.cloud.google.com/
   - Create new project: "Obsidian Publisher"
   - Enable: **Google Docs API** + **Google Drive API**

2. **Get credentials**
   - APIs & Services → Credentials → Create OAuth client ID
   - Choose **"Desktop app"**
   - Download JSON → rename to `client_secret.json`
   - Move to `Google Docs Publisher/client_secret.json`

3. **Authenticate**
   - Open Terminal:
     ```bash
     cd "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher"
     node index.js TEST-MINIMAL.md
     ```
   - Copy the URL → paste in browser
   - Allow permissions (click "Advanced" if you see "Google hasn't verified this app")
   - Copy auth code → paste in terminal
   - ✅ Done! (creates `token.json`)

### Phase 2: Obsidian Setup (5 minutes)

1. **Install plugin**
   - Settings → Community plugins → Browse
   - Search **"Shell commands"** → Install + Enable

2. **Add command**
   - Settings → Shell commands → New command
   - Paste:
     ```bash
     "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher/publish-active.sh"
     ```
   - Alias: `Publish to Google Docs`
   - Click **Output** tab → Set "Output channel for stdout" to: **Modal**

3. **Add hotkey**
   - Settings → Hotkeys
   - Search "Publish to Google Docs"
   - Set: `Alt+Shift+P` (or your choice)

### Phase 3: Test (30 seconds)

1. Open any markdown file in Obsidian
2. Press `Alt+Shift+P`
3. Wait for modal showing Google Docs URL
4. Open URL → verify formatting! ✅

---

## 🎯 That's It!

**What Works:**
- ✅ Headings (H1-H6) with Pachyderm Global brand colors
- ✅ Bold, italic, strikethrough, inline code
- ✅ Links (clickable)
- ✅ Bulleted & numbered lists
- ✅ Code blocks with monospace
- ✅ Blockquotes (indented + italic)
- ✅ Horizontal rules

**Not Yet Working:**
- ⏸️ Tables (in progress - see ROADMAP.md)

---

## 🆘 Common Issues

**"client_secret.json not found"**
→ Download OAuth credentials from Google Cloud Console

**"Google hasn't verified this app"**
→ Click "Advanced" → "Go to Obsidian Publisher (unsafe)" - safe!

**Hotkey doesn't work**
→ Try Command Palette (`Cmd+P` → "Publish to Google Docs")

**Need more help?**
→ Read [SETUP.md](SETUP.md) or [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md)

**Ready to publish!** 🚀
