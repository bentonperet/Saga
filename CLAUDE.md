# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault - a personal knowledge management system containing markdown files with interconnected notes, not a software codebase.

**Primary Project: Saga Pryor Data Center**
- A data center design and development project
- Includes Basis of Design (BOD) documents organized by CSI divisions
- BIM/architecture coordination at LOD200 level
- Power systems design (utility, solar, BESS, generators)
- Project management tracking via action items and meeting notes
- Collaboration with Camelot (architect) and other consultants

**Document Organization:**
- Uses modified PARA method (Projects, Archive, Resources)
- Living documents that evolve throughout project lifecycle
- Cross-linked notes form a knowledge graph

## Structure

The vault is organized around active projects and their supporting documentation:

```
Saga1/
├── Saga Pryor DC/              # Primary project: Data center design & development
│   ├── _Project Management/    # Project coordination & tracking
│   │   ├── Actions/           # Action items, task lists, tracking scripts
│   │   ├── Design Notes/      # Technical decisions & considerations
│   │   ├── Future Phases/     # Forward-looking planning
│   │   └── Meetings/          # Meeting notes & transcripts
│   ├── Archive/               # Superseded documents & old versions
│   ├── Basis of Design/       # BOD documents organized by CSI division
│   ├── BIM-Architect/         # Architecture & BIM requirements
│   ├── Power/                 # Power systems, BESS, solar, generators
│   └── Reference Materials/   # Standards, specs, external documentation
└── .obsidian/                 # Obsidian configuration (plugins, workspace)
```

**Key Navigation:**
- Project root: `Saga Pryor DC/` contains all active work
- BOD files: Numbered by CSI division (e.g., `7BOD - Electrical (CSI Div 26).md`)
- Management: `_Project Management/` for coordination docs
- Historical: `Archive/` for outdated content

## Working with This Vault

**No build commands** - This is a documentation repository with no compilation, testing, or deployment steps.

**Prompting:**
- Many prompts are dictated via speech-to-text, which can result in:
  - Homophone errors (e.g., "there" vs "their", "sight" vs "site")
  - Technical terms transcribed phonetically
  - Missing punctuation or run-on sentences
- **Always infer the intended meaning** based on context rather than taking text literally
- When uncertain about speech-to-text errors, ask for clarification

**File Operations:**
- All files are markdown (.md) unless otherwise specified
- Files may contain Obsidian-specific syntax:
  - `[[wikilinks]]` for internal linking between notes
  - `[[note#heading]]` for linking to specific sections
  - `![[image.png]]` for embedding images
  - Tags using `#tag` format (e.g., `#data-center`, `#electrical`)
- HTML comments are used for inline instructions:
  - `<!-- This is a comment -->` provides context for readers
  - `<!-- @claude -->` flags content specifically for AI attention
  - **Always pay attention to `@claude` mentions** - they contain important instructions

**Common Tasks:**
- **Creating new notes:** Place in the appropriate project folder or subfolder
- **Linking notes:** Use `[[Note Title]]` format for internal links
- **Organizing:** Move superseded/outdated content to Archive folders
- **Updating project docs:** BOD files and project management documents are living documents
- **Cross-referencing:** Always search for related notes to link and build the knowledge graph

**When Creating or Editing Notes:**

1. **Add metadata header:**
   ```markdown
   **Created:** YYYY-MM-DD HH:MM
   **Tags:** #tag1 #tag2 #tag3
   **Related:** [[Related Note 1]], [[Related Note 2]]
   ```

2. **Use appropriate tags:**
   - Project-specific: `#data-center`, `#pryor-dc`, `#bim`, `#electrical`
   - Domain: `#architecture`, `#power-systems`, `#mechanical`, `#procurement`
   - Document type: `#bod`, `#meeting-notes`, `#action-items`, `#reference`

3. **Build connections:**
   - Search for existing notes on similar topics before creating new ones
   - Link to related notes using `[[Note Title]]` format
   - Reference specific sections with `[[Note#Section]]`
   - This strengthens the knowledge graph and prevents duplicate content

4. **Formatting guidelines:**
   - Use horizontal rules (`---`) sparingly - only between major sections
   - Don't over-break content - keep related paragraphs together
   - Example: In a 5-part document, use breaks between parts, not between every subsection
   - Use headings (`##`, `###`) to structure content instead of excessive line breaks

**Obsidian Configuration:**
- Workspace state is stored in `.obsidian/workspace.json`
- Plugins and settings in `.obsidian/` directory
- Graph view configuration in `.obsidian/graph.json`

## Git Syncing

**Obsidian Git Plugin:**
- The vault uses the Obsidian Git community plugin for automatic syncing
- Configuration: `.obsidian/plugins/obsidian-git/data.json`
- Auto-commit: Every 60 minutes
- Auto-pull: Every 30 minutes
- Auto-pull on startup: Enabled

**Manual Git Operations:**
When the user asks to "commit my obsidian updates" or similar:

1. **Check status:**
   ```bash
   cd "Saga1" && git status
   ```

2. **Review changes:**
   ```bash
   git diff
   ```

3. **Commit and push:**
   ```bash
   git add . && git commit -m "vault backup: YYYY-MM-DD HH:mm:ss

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>" && git push
   ```

**Repository Details:**
- Remote: `https://github.com/bentonperet/Saga.git`
- Branch: `main`
- Authentication: Configured via GitHub CLI/credentials