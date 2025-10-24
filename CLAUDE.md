# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an Obsidian vault named "Saga" - a personal knowledge management system using markdown files. Obsidian is a note-taking application that uses plain markdown files with wiki-style linking between notes.

## Vault Structure

- **Root directory**: Contains markdown notes (`.md` files)
- **`.obsidian/`**: Configuration directory for Obsidian (DO NOT modify unless explicitly requested)
  - `workspace.json`: Workspace layout and open files
  - `core-plugins.json`: Enabled core plugins configuration
  - `community-plugins.json`: List of installed community plugins
  - `plugins/`: Community plugin data and settings

## Installed Plugins

### Core Plugins
- File explorer, search, graph view, backlinks
- Canvas (for visual note organization)
- Daily notes, templates, bookmarks
- Note composer, command palette
- Obsidian Sync and Bases

### Community Plugins
- **obsidian-git**: Git integration for version control and automatic backup
- **dataview**: Query and display note metadata as dynamic tables/lists
  - DataviewJS enabled for JavaScript queries
  - Inline queries enabled with `=` prefix
  - JS inline queries with `$=` prefix

## Working with Notes

### Note Linking
- Use `[[Note Name]]` for wiki-style links between notes
- Links create bidirectional connections viewable in the graph view

### Dataview Queries
When creating or modifying dataview queries:
- Use dataview codeblocks: ` ```dataview `
- Query types: TABLE, LIST, TASK, CALENDAR
- Reference fields with inline metadata: `key:: value`
- DataviewJS blocks use: ` ```dataviewjs `

Example dataview query structure:
```
TABLE field1, field2
FROM "folder"
WHERE condition
SORT field ASC
```

### File Organization
- The vault currently has a flat structure
- When organizing notes, consider creating folders for:
  - Topics/subjects
  - Daily notes (if using daily notes feature)
  - Templates (if using templates feature)

## Git Integration

The obsidian-git plugin is installed. When working with version control:
- The plugin handles automatic commits and syncing
- Standard git operations can be performed via command line
- Be mindful that `.obsidian/workspace.json` changes frequently and may not need to be committed

## Best Practices

### Note Creation
- Use descriptive, human-readable filenames
- Follow consistent naming conventions (if user has established any)
- Add YAML frontmatter for metadata when helpful:
  ```yaml
  ---
  tags: [tag1, tag2]
  created: 2025-10-24
  ---
  ```

### Dataview Metadata
- Inline fields: `key:: value` anywhere in note
- YAML frontmatter for structured metadata
- Implicit fields available: `file.name`, `file.ctime`, `file.mtime`, `file.size`, etc.

### Link Handling
- Prefer relative wiki-links over markdown links for note interconnection
- Update links when renaming files (Obsidian handles this automatically in the UI)

## Important Notes

- This is NOT a code repository - avoid treating it like a software project
- Focus on markdown formatting, note organization, and Obsidian-specific features
- The vault location is on Google Drive (`G:\My Drive\_Obsidian\Saga`)
- Not currently a git repository (though git plugin is installed)
