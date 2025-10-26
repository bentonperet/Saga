# Obsidian → Google Docs Publisher

Publish your Obsidian markdown notes to beautifully formatted Google Docs with one click.

## Quick Start

1. **First-time setup** (see [SETUP.md](SETUP.md)):
   - Create Google Cloud project
   - Enable APIs (Docs + Drive)
   - Download OAuth credentials to `client_secret.json`
   - Run first-time authentication

2. **Install Obsidian Shell Commands plugin**

3. **Add command** in Obsidian:
   ```bash
   node "/path/to/Google Docs Publisher/index.js" "{{file_path:absolute}}"
   ```

4. **Set a hotkey** and publish!

## Features

✨ **Full markdown support:**
- Headings with brand styling (Rubik font)
- Bold, italic, strikethrough, code
- Links
- Bulleted & numbered lists
- Tables with headers
- Code blocks
- Blockquotes
- Horizontal rules

🎨 **Brand styling:**
- Pachyderm Global color scheme
- Professional fonts (Rubik + Source Sans 3)
- Consistent spacing & formatting
- Customizable in `brandConfig.js`

🚀 **Smart features:**
- Auto-copy URL to clipboard
- Optional URL append to markdown
- Debug mode for troubleshooting
- Fast batch API requests

## File Structure

```
Google Docs Publisher/
├── index.js              # Main CLI script
├── googleAuth.js         # OAuth authentication
├── markdownParser.js     # Markdown → structured blocks
├── docsPublisher.js      # Google Docs API integration
├── brandConfig.js        # Brand styles (colors, fonts)
├── package.json          # Dependencies
├── SETUP.md             # Detailed setup guide
├── README.md            # This file
├── client_secret.json   # Your OAuth credentials (git-ignored)
└── token.json           # Auth token (auto-generated, git-ignored)
```

## Usage

### From Command Line

```bash
# Basic
node index.js "/path/to/note.md"

# With options
node index.js "/path/to/note.md" --append-url --debug
```

### From Obsidian

Press your hotkey → Get Google Docs link!

## Customization

Edit `brandConfig.js` to change:
- Colors (hex codes)
- Fonts (Google Fonts only)
- Font sizes
- Line spacing
- Paragraph spacing

## Troubleshooting

See [SETUP.md](SETUP.md#troubleshooting) for common issues.

**Quick fixes:**
- Delete `token.json` and re-auth
- Check that both APIs are enabled
- Verify file paths in Obsidian command
- Run with `--debug` flag

## Tech Stack

- **Node.js** - Runtime
- **googleapis** - Google Docs/Drive API
- **remark** - Markdown parsing
- **remark-gfm** - GitHub Flavored Markdown (tables, etc.)

## License

MIT

---

**Made for Pachyderm Global** 🐘
