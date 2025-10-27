# Google Docs Publisher - Roadmap

## Current Status: ✅ FULLY WORKING

**Version:** 1.1 (Tables supported!)

### ✅ Completed Features

**Core Functionality:**
- Headings (H1-H6) with Pachyderm Global brand styling
- Paragraphs with inline formatting (bold, italic, strikethrough)
- Inline code with monospace font
- Clickable links
- Bulleted lists
- Numbered lists
- Code blocks with background color
- Blockquotes with indentation and italic styling
- Horizontal rules
- **Tables** (formatted as text with borders)

**Integration:**
- OAuth authentication (one-time setup)
- Obsidian hotkey integration (via `publish-active.sh`)
- Auto-clipboard copy of Google Docs URL (macOS)
- ES modules support (full CommonJS to ES module conversion)

### ✅ Table Support Status

**Implementation:** Tables are now supported! They render as formatted text with borders (markdown-style).

**What we did:**
- ✅ Added `"type": "module"` to package.json
- ✅ Converted all files to ES modules (markdownParser.js, brandConfig.js, googleAuth.js, docsPublisher.js, index.js)
- ✅ Fixed `__dirname` usage in ES modules (using `import.meta.url`)
- ✅ Integrated `remark-gfm` for GitHub Flavored Markdown
- ✅ Implemented table parsing in markdownParser.js
- ✅ Implemented table rendering as formatted text in docsPublisher.js
- ✅ Tested with complex tables (formatting, links, etc.)

**Current Approach:**
Tables are rendered as monospace formatted text with borders:
```
| Name | Role | Department |
|------|------|-------------|
| Alice | Manager | Engineering |
```

This approach:
- ✅ Works reliably
- ✅ Preserves table structure
- ✅ Shows all content clearly
- ✅ Supports inline formatting (bold, italic, links)
- ⚠️ Does not use native Google Docs table elements

**Why formatted text instead of native tables?**
The Google Docs API for tables requires:
1. Inserting the table structure
2. Reading back the document to get cell locations
3. Inserting content into each cell with precise indices
4. The index calculations are complex and error-prone

Our formatted text approach is more reliable and still presents tables clearly.

### Known Limitations

**API Limitations:**
- Blockquote left border not supported (Google Docs API limitation)
- Font family cannot be set via API (weightedFontFamily requires complex structure)
- Tables use formatted text instead of native table elements

**Feature Limitations:**
- Table cell merging not supported
- Table alignment (left/center/right) not visually applied
- Complex nested tables may not format perfectly

---

## Future Enhancements (v2.0)

- Image support (currently shows `[Image: alt text]` placeholder)
- Nested lists (currently single-level)
- Custom font families via API (currently removed due to API complexity)
- Batch publishing (multiple files at once)
- Template support (apply different brand configs)
- Table of contents generation
- Document versioning/update existing docs

---

## Technical Debt

- Shell Commands plugin variable issue (worked around with `publish-active.sh`)
- ES module conversion incomplete (syntax errors remaining)
- Limited error handling for API rate limits
- No retry logic for failed API calls

---

**Last Updated:** 2025-10-27
