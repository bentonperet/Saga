# Obsidian → Google Docs Publisher

Publish your Obsidian markdown notes to beautifully formatted Google Docs with one hotkey.

## ✅ Status: WORKING

Tables support in progress (see [ROADMAP.md](ROADMAP.md))

## Quick Start

**[→ See QUICKSTART.md for 10-minute setup](QUICKSTART.md)**

1. Create Google Cloud project + OAuth credentials
2. Install Obsidian Shell Commands plugin
3. Add publish command + hotkey
4. Press hotkey → Get Google Doc link!

## Features

**✅ Full Support:**
- Headings (H1-H6) with Pachyderm Global brand styling (Rubik font, custom colors)
- Inline formatting: **bold**, *italic*, ~~strikethrough~~, `code`
- [Clickable links](https://example.com)
- Bulleted & numbered lists
- Code blocks with monospace font + background
- Blockquotes with indentation
- Horizontal rules
- Auto-copy URL to clipboard (macOS)

**⏸️ In Progress:**
- Tables (converting to ES modules - see ROADMAP.md)

**❌ Not Supported:**
- Images (shows `[Image: alt text]` placeholder)
- Footnotes
- Task lists (converted to bullets)
- Mermaid diagrams

## Usage

### From Obsidian
Press your hotkey (`Alt+Shift+P`) → Get Google Docs URL!

### From Command Line
```bash
cd "Google Docs Publisher"
node index.js "../path/to/file.md"
```

## File Structure

```
Google Docs Publisher/
├── index.js              # Main CLI script
├── googleAuth.js         # OAuth authentication
├── markdownParser.js     # Markdown → blocks
├── docsPublisher.js      # Google Docs API integration
├── brandConfig.js        # Brand styles (Rubik, Source Sans 3, colors)
├── publish-active.sh     # Wrapper for Obsidian
├── client_secret.json    # Your OAuth credentials (add this)
├── token.json            # Auto-generated after first auth
└── *.md                  # Documentation
```

## Customization

Edit `brandConfig.js` to change:
- Colors (hex codes)
- Fonts (Google Fonts)
- Font sizes
- Line spacing
- Paragraph spacing

## Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - 10-minute setup
- **[SETUP.md](SETUP.md)** - Detailed guide + troubleshooting
- **[OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md)** - Obsidian integration
- **[ROADMAP.md](ROADMAP.md)** - Status + future plans

## Tech Stack

- Node.js
- `googleapis` - Google Docs/Drive API
- `remark` + `remark-parse` - Markdown parsing
- `remark-gfm` - Tables (in progress)

## License

MIT

---

**Made for Pachyderm Global** 🐘
