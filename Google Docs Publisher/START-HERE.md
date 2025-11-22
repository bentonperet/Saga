# 🎉 Obsidian → Google Docs Publisher

## ✅ Installation Complete!

Your publisher is ready to go. Here's what happens next:

### 📋 What You Have

```
Google Docs Publisher/
├── index.js              ⚙️  Main script
├── googleAuth.js         🔐 OAuth handler
├── markdownParser.js     📝 Markdown parser
├── docsPublisher.js      📄 Google Docs API
├── brandConfig.js        🎨 Your brand styles
├── package.json          📦 Dependencies (installed)
│
├── QUICKSTART.md         ⚡ Start here! (10-minute setup)
├── SETUP.md              📖 Detailed setup guide
├── OBSIDIAN-SETUP.md     🔧 Obsidian integration
├── README.md             ℹ️  Overview
└── TEST.md               🧪 Test document
```

---

## 🚀 Next Steps (Choose Your Path)

### Path A: Quick Setup (10 minutes)

👉 **Follow [QUICKSTART.md](QUICKSTART.md)**

Perfect if you just want it working ASAP.

### Path B: Detailed Setup (20 minutes)

👉 **Follow [SETUP.md](SETUP.md)**

Best if you want to understand each step.

---

## 📚 What Each Guide Covers

### [QUICKSTART.md](QUICKSTART.md)
- ⚡ 3-phase setup (Google → Obsidian → Test)
- 🎯 Minimal steps to get working
- 🆘 Common first-time issues

### [SETUP.md](SETUP.md)
- 🔧 Google Cloud Console setup
- 🔐 OAuth authentication flow
- 🔌 Obsidian integration options
- 🛠️ Troubleshooting guide
- 🎨 Customization tips

### [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md)
- 🔌 Shell Commands plugin config
- ⌨️  Hotkey setup
- 🎛️ Advanced workflows
- 💡 Tips & tricks

### [README.md](Google%20Docs%20Publisher/README.md)
- 📊 Feature overview
- 🗂️ File structure
- 🛠️ Tech stack
- 📝 Usage examples

---

## ⚡ TL;DR - Super Quick Start

If you already have:
- ✅ Node.js installed
- ✅ Google account
- ✅ 10 minutes

**Do this:**

1. **Get Google credentials** (5 min)
   - https://console.cloud.google.com/
   - Create project → Enable APIs → Create OAuth client
   - Download `client_secret.json` → put in this folder

2. **Authenticate** (2 min)
   ```bash
   cd "/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Google Docs Publisher"
   node index.js TEST.md
   ```
   - Open URL in browser → Allow → Copy code → Paste

3. **Setup Obsidian** (3 min)
   - Install "Shell commands" plugin
   - Add command (see QUICKSTART.md)
   - Set hotkey

4. **Test** (30 sec)
   - Open any `.md` file
   - Press hotkey
   - Get Google Docs link! 🎉

---

## 🎨 Features

### Markdown → Google Docs Conversion

✅ **Headings** (H1-H6) with Rubik font + brand colors
✅ **Text formatting** (bold, italic, strikethrough, code)
✅ **Links** (clickable, styled)
✅ **Lists** (bullets + numbered)
✅ **Tables** with headers
✅ **Code blocks** with monospace
✅ **Blockquotes** with indent + border
✅ **Horizontal rules**

### Brand Styling (PACHYDERM GLOBAL)

- **Headings**: Rubik, #044A74 (H1), #4F81BD (H2)
- **Body**: Source Sans 3, 11.5pt, 1.28 line spacing
- **Code**: Source Code Pro, gray background
- **Tables**: Professional borders, header styling
- **Footer**: "© PACHYDERM GLOBAL 2025 — Confidential"

All customizable in `brandConfig.js`!

---

## 🆘 Quick Help

**Problem?** Check these in order:

1. [QUICKSTART.md](QUICKSTART.md#-common-first-time-issues) - Common issues
2. [SETUP.md](SETUP.md#troubleshooting) - Detailed troubleshooting
3. Run with debug: `node index.js yourfile.md --debug`

**Most common issues:**

- Missing `client_secret.json` → Download from Google Cloud Console
- "Command not found: node" → Add PATH to Shell Commands plugin
- "Permission denied" → Enable both APIs (Docs + Drive)
- Tables not working → Check markdown table syntax

---

## 🎯 What to Do Right Now

1. Open [QUICKSTART.md](QUICKSTART.md)
2. Follow the 3 phases
3. Test with `TEST.md`
4. Start publishing! 🚀

---

## 💡 Pro Tips

- **Test first** with `TEST.md` to verify all features work
- **Customize** fonts/colors in `brandConfig.js`
- **Use `--append-url`** flag to save Google Docs links in your notes
- **Set a hotkey** for one-press publishing
- **Clipboard auto-copy** (macOS only) - URL is ready to paste!

---

**Questions?** Read the guides or check the inline code comments.

**Ready to go?** → [QUICKSTART.md](QUICKSTART.md) ⚡

---

Made with ❤️ for PACHYDERM GLOBAL
