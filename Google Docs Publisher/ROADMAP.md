# Google Docs Publisher - Roadmap

## Current Status: ✅ WORKING

**Version:** 1.0 (ES Modules conversion in progress)

### ✅ Completed Features
- Headings (H1-H6) with Pachyderm Global brand styling
- Paragraphs with inline formatting (bold, italic, strikethrough)
- Inline code with monospace font
- Clickable links
- Bulleted lists
- Numbered lists
- Code blocks with background color
- Blockquotes with indentation and italic styling
- Horizontal rules
- OAuth authentication (one-time setup)
- Obsidian hotkey integration (via `publish-active.sh`)
- Auto-clipboard copy of Google Docs URL (macOS)

### 🚧 In Progress: Table Support

**Goal:** Convert markdown tables to formatted Google Docs tables

**Current Issue:** Tables require `remark-gfm` which is an ES module. Converting project from CommonJS to ES modules.

**Status:**
- ✅ Added `"type": "module"` to package.json
- ✅ Converted `markdownParser.js` to ES imports
- ✅ Converted `brandConfig.js` to ES exports
- ✅ Converted `googleAuth.js` to ES imports
- ✅ Converted `index.js` to ES imports
- 🚧 Fixing `docsPublisher.js` import syntax error (line 7)
- ⏸️ Test table parsing and rendering

**Next Steps:**
1. Fix remaining syntax errors in docsPublisher.js
2. Test markdown table parsing with remark-gfm
3. Verify table insertion via Google Docs API
4. Test with real documents containing tables
5. Update documentation

**Known Limitations:**
- Blockquote left border not supported (Google Docs API limitation)
- Complex nested tables may not work
- Table cell merging not supported

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
