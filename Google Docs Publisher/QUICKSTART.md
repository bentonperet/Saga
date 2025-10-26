# Quick Start Guide

## ⚡ Get Publishing in 10 Minutes

### Phase 1: Google Setup (5 minutes)

1. **Create project & enable APIs**
   - Go to https://console.cloud.google.com/
   - Create new project: "Obsidian Publisher"
   - Enable: Google Docs API + Google Drive API

1. **Get credentials**
   - APIs & Services → Credentials → Create OAuth client ID
   - Choose "Desktop app"
   - Download JSON → rename to `client_secret.json`
   - Move to `Google Docs Publisher/client_secret.json`

Bentons client ID: 802257196931-rli4hi6sndno44b4jmmrqdtuafstpi08.apps.googleusercontent.com
Secret: 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

1. **Authenticate**
   - Open Terminal:
     ```bash
     cd "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher"
     node index.js TEST.md
     ```
   - Copy the URL → paste in browser
   - Allow permissions
   - Copy auth code → paste in terminal
   - ✅ Done! (creates `token.json`)

### Phase 2: Obsidian Setup (5 minutes)

1. **Install plugin**
   - Settings → Community plugins → Browse
   - Search "Shell commands" → Install + Enable

2. **Add command**
   - Settings → Shell commands → New command
   - Paste:
     ```bash
     node "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher/index.js" "{{file_path:absolute}}"
     ```
   - Alias: `Publish to Google Docs`
   - Output: `Modal`

3. **Add hotkey**
   - Settings → Hotkeys
   - Search "Publish to Google Docs"
   - Set: `Cmd+Shift+P` (or your choice)

### Phase 3: Test (30 seconds)

1. Open `TEST.md` in Obsidian
2. Press `Cmd+Shift+P`
3. Wait for modal showing Google Docs URL
4. Open URL → verify formatting! ✅

---

## 🎯 That's It!

Now you can publish any markdown file with one hotkey press.

**Next steps:**
- Read [SETUP.md](SETUP.md) for troubleshooting
- Customize [brandConfig.js](brandConfig.js) for your styles
- Check [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md) for advanced options

---

## 🆘 Common First-Time Issues

**"client_secret.json not found"**
→ Make sure you downloaded the OAuth credentials and placed them in `Google Docs Publisher/`

**"Command not found: node"**
→ Add to Shell Commands environment variables:
```
PATH=/usr/local/bin:/opt/homebrew/bin:$PATH
```

**"Google hasn't verified this app"**
→ Click "Advanced" → "Go to Obsidian Publisher (unsafe)" - it's safe, you created it!

**"Permission denied"**
→ Make sure you enabled BOTH Google Docs API and Google Drive API

---

**Ready to publish!** 🚀
