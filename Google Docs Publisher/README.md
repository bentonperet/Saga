# Obsidian → Google Docs Publisher

**One hotkey. Beautiful Google Docs. Every time.**

Transform your Obsidian markdown notes into professionally formatted Google Docs instantly. Press a hotkey, get a shareable link.

## ✅ Status: Fully Working (Including Tables!)

All features working perfectly! **Tables are now supported** and render as formatted text with borders.

## Why Use This?

- **Zero manual formatting** - Your brand styles are applied automatically
- **One hotkey** - Press `Alt+Shift+P` and you're done
- **Share instantly** - Google Docs link auto-copied to clipboard
- **Keep working in Obsidian** - No need to export, import, or reformat
- **Perfect for teams** - Share professional docs without leaving your workflow

## Quick Start

**[→ See QUICKSTART.md for step-by-step setup (10 minutes)](QUICKSTART.md)**

1. **Set up Google Cloud** (one-time) - Create project + OAuth credentials
2. **Install plugin** - Add Shell Commands plugin in Obsidian
3. **Configure hotkey** - Press your keys to publish
4. **Done!** - Press hotkey → Get Google Doc link instantly

💡 **Not technical?** No problem! The guides are written for everyone, and Claude Code can help with any terminal steps.

## What Gets Formatted

**✅ Fully Working:**
- **Headings (H1-H6)** - Styled with your brand colors and fonts (Rubik for headings, Source Sans 3 for body)
- **Text formatting** - **Bold**, *italic*, ~~strikethrough~~, `inline code`
- **Links** - Become clickable blue links in Google Docs
- **Lists** - Both bulleted and numbered, properly indented
- **Code blocks** - Monospace font with gray background
- **Blockquotes** - Indented and italicized
- **Horizontal rules** - Convert to visual separators
- **Tables** - Rendered as formatted text with borders (preserves structure and content)
- **Auto-clipboard** - URL copied automatically on Mac

**❌ Not Supported:**
- Images (shows placeholder: `[Image: filename]`)
- Footnotes
- Task lists (converts to regular bullets)
- Mermaid diagrams

**ℹ️ Note on Tables:**
Tables are rendered as formatted text (like code blocks) rather than native Google Docs tables. This approach is more reliable and still presents the data clearly. Native table support may come in a future version.

## Usage

### From Obsidian (Recommended)
1. Open any markdown note
2. Press your hotkey (e.g., `Alt+Shift+P`)
3. Wait 2-5 seconds
4. Get a popup with the Google Docs URL (auto-copied to clipboard on Mac)
5. Share the link with your team!

### From Command Line (For Specific Files)
Ask Claude Code:
```
Please publish this file to Google Docs: path/to/my-note.md
```

Or run manually:
```bash
cd "Google Docs Publisher"
node index.js "path/to/file.md"
```

## Error Logging

If the export fails, all error details are automatically saved to `export-errors.log` in the same directory. This helps capture errors that disappear quickly when using the hotkey.

**Error log includes:**
- Full error message and stack trace
- Timestamp of when the error occurred
- File path and command-line arguments used
- Google API error details (if applicable)

**To view recent errors:**
```bash
# View last 50 lines of the error log
tail -50 "Google Docs Publisher/export-errors.log"

# View entire error log
cat "Google Docs Publisher/export-errors.log"
```

**Note:** The error log file (`export-errors.log`) is already in `.gitignore` and won't be committed to Git.

## Customizing Your Brand

**Want different colors or fonts?** Edit `brandConfig.js`:

```javascript
H1: {
  fontFamily: 'Rubik',          // Any Google Font
  color: '#044A74',             // Your brand color (hex)
  fontSizePt: 20,               // Size in points
  bold: true,
  lineSpacing: 1.10,            // 110% spacing
  beforeSpacingPt: 12,          // Space before heading
  afterSpacingPt: 6             // Space after heading
}
```

**You can customize:**
- Colors for all heading levels and body text
- Font families (any Google Font works!)
- Font sizes
- Line spacing
- Paragraph spacing
- Bold/italic defaults

**Pro tip:** Ask Claude Code to help! "Please update brandConfig.js to use my brand colors: primary #FF5733, secondary #33C3FF"

## How It Works

1. **You press the hotkey** in Obsidian
2. **Script finds your file** - Identifies the most recently edited markdown file
3. **Parses markdown** - Converts to structured data the Google Docs API understands
4. **Authenticates** - Uses your stored OAuth token
5. **Creates doc** - Builds a new Google Doc with your brand styling applied
6. **Returns URL** - Shows you the link instantly

**No cloud storage involved!** Everything runs locally on your computer. Your files go directly from your machine to Google Docs.

## Documentation

Start here based on your needs:

- **[QUICKSTART.md](QUICKSTART.md)** - First-time setup (10 minutes, beginner-friendly)
- **[SETUP.md](SETUP.md)** - Detailed setup with troubleshooting (technical reference)
- **[OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md)** - Obsidian integration guide (step-by-step with screenshots)
- **[ROADMAP.md](ROADMAP.md)** - Development status and upcoming features

💡 **All guides are written for non-technical users!** If you get stuck, Claude Code can help with any step.

## Project Structure

```
Google Docs Publisher/
├── index.js              # Main script (handles CLI arguments, coordinates publishing)
├── googleAuth.js         # OAuth 2.0 authentication (manages tokens)
├── markdownParser.js     # Converts markdown to structured blocks
├── docsPublisher.js      # Google Docs API integration (creates documents)
├── brandConfig.js        # Your brand styling (CUSTOMIZE THIS!)
├── publish-active.sh     # Obsidian hotkey wrapper (finds most recent file)
├── client_secret.json    # Your OAuth credentials (YOU ADD THIS)
├── token.json            # Access token (auto-generated after first auth)
├── TEST-MINIMAL.md       # Test file for validating setup
└── *.md                  # Documentation files
```

## Tech Stack

Built with:
- **Node.js** - JavaScript runtime
- **googleapis** - Official Google APIs client
- **remark** + **remark-parse** - Markdown parsing (AST-based)
- **remark-gfm** - GitHub Flavored Markdown (for tables, coming soon)
- **unified** - Text processing ecosystem

## Security & Privacy

- ✅ Runs **locally on your computer** - no third-party servers
- ✅ **Direct connection** to Google Docs - your files never pass through anything else
- ✅ **OAuth 2.0** - Industry-standard secure authentication
- ✅ **Limited permissions** - Can only create new docs, not read or modify existing ones
- ✅ **Git-safe** - Credentials in `.gitignore` won't be committed

## Contributing

Found a bug? Want a feature? Have a suggestion?
- Open an issue
- Submit a pull request
- Ask Claude Code to help implement it!

## License

MIT License - Use it, modify it, share it!

---

**Made with ❤️ for PACHYDERM GLOBAL** 🐘

*Turning markdown notes into professional documents, one hotkey at a time.*
