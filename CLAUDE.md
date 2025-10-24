# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault - a personal knowledge management system organized using the PARA method (Projects, Areas, Resources, Archive). It contains markdown files with interconnected notes, not a software codebase.

## Structure

<!-- claude - please update here -->

## Working with This Vault

**No build commands** - This is a documentation repository with no compilation, testing, or deployment steps.

**Prompting:**
- Many prompts given are "typed" in using a speech-to-text app. This often results in strange spellings of words or sentences that are slightly off-meaning but sound similar. Please infer what I actually mean vs. taking all text literally.

**File Operations:**
- All files are markdown (.md) unless otherwise specified
- Files may contain Obsidian-specific syntax like `[[wikilinks]]` for internal linking
- Images and attachments may be referenced inline or stored as separate files
- Comments such as <!-- This is a comment --> are often used to provide commentary to both claude and to other users of the documents.
- Please pay special attention when @claude is highlighted anywhere in a document as it means this information is intended for you.

**Common Tasks:**
- Creating new notes: Add markdown files in the appropriate PARA category
- Linking notes: Use `[[Note Title]]` format for internal links
- Organizing: Move completed projects to Archive, active items to Projects

**When Creating or Editing Notes:**
- **Always add a timestamp** at the top of new files in the format: `**Created:** YYYY-MM-DD HH:MM` (use 24-hour format)
- Add relevant tags using `#tag` format to categorize content (e.g., `#sales`, `#ai`, `#health`, `#recipe`, `#finance`)
- Include links to related notes using `[[Note Title]]` format to build connections across the vault
- Search for and link to existing notes on similar topics to strengthen the knowledge graph
- Don't use too many line breaks. Ideally line breaks are between larger sections of the content. Example: If there's a 5 part paper, and within each part there are multiple sections, only put lines between parts not every section.

**Obsidian Configuration:**
- Workspace state is stored in `.obsidian/workspace.json`
- Plugins and settings in `.obsidian/` directory
- Graph view configuration in `.obsidian/graph.json`

## Git Syncing

**To sync vault changes to GitHub:**
When the user asks to "commit my obsidian updates" or similar:
1. Run `git status` to check for changes
2. Run `git diff` to view what changed
3. Run `git add . && git commit -m "descriptive message" && git push`
4. Use the standard commit message format with Claude Code attribution

The repository is configured with GitHub CLI authentication, so pushes should work automatically.