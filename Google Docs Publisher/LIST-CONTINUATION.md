# Numbered List Continuation Feature

**Feature:** Automatically continues numbered list numbering when lists are interrupted by headings or other content.

---

## The Problem

In markdown, when you have a numbered list that's interrupted by a heading, paragraph, or other content, the list numbering resets:

```markdown
1. First item
2. Second item

## A Heading

3. Third item (wants to be #3 but becomes #1)
4. Fourth item (wants to be #4 but becomes #2)
```

**Without this feature:** Each list segment starts counting from 1.
**With this feature:** All numbered lists in the document continue counting.

---

## How It Works

### Implementation Strategy

1. **Track List IDs:** The first numbered list gets an auto-generated `listId` from Google Docs
2. **Capture the ID:** After creating the first list, we read back the document and capture that `listId`
3. **Reuse the ID:** All subsequent numbered lists use the same `listId`
4. **Auto-continuation:** Google Docs automatically continues numbering for items with the same `listId`

### Code Flow

```javascript
// Constructor - initialize tracking
this.listIds = {}; // Track list IDs for continuing numbered lists

// When first numbered list is encountered
if (!this.listIds.numbered) {
  this.listIds.numbered = 'pending'; // Placeholder
}

// When creating list items
if (block.ordered && this.listIds.numbered && this.listIds.numbered !== 'pending') {
  bulletRequest.createParagraphBullets.listId = this.listIds.numbered;
}

// After batch update, capture the list ID
await this.captureListIds();
```

---

## Example

### Markdown Input

```markdown
1. Step one
2. Step two

### Important Note

This is some explanatory text between list items.

3. Step three (continues as #3)
4. Step four (continues as #4)

## Another Section

5. Step five (continues as #5)
6. Step six (continues as #6)
```

### Result in Google Docs

```
1. Step one
2. Step two

Important Note (heading)

This is some explanatory text between list items.

3. Step three ← Correctly continues!
4. Step four

Another Section (heading)

5. Step five ← Still continuing!
6. Step six
```

---

## Technical Details

### Google Docs API Concept

**listId:** A unique identifier for a list in Google Docs
- List items with the same `listId` belong to the same list
- They're numbered sequentially regardless of location in document
- Items don't need to be adjacent or have the same parent

### API Request Structure

**Without continuation (old behavior):**
```javascript
{
  createParagraphBullets: {
    range: { startIndex, endIndex },
    bulletPreset: 'NUMBERED_DECIMAL_ALPHA_ROMAN'
    // No listId - gets new auto-generated ID
  }
}
```

**With continuation (new behavior):**
```javascript
{
  createParagraphBullets: {
    range: { startIndex, endIndex },
    bulletPreset: 'NUMBERED_DECIMAL_ALPHA_ROMAN',
    listId: 'kix.abc123xyz' // Reuse existing list ID
  }
}
```

### List ID Capture Process

```javascript
async captureListIds() {
  if (this.listIds.numbered === 'pending') {
    // Read document
    const doc = await this.docs.documents.get({ documentId: this.docId });

    // Find numbered lists
    const lists = doc.data.lists || {};
    for (const listId in lists) {
      const list = lists[listId];
      const firstLevel = list.listProperties.nestingLevels[0];

      // Check if it's a numbered list (DECIMAL glyph type)
      if (firstLevel.glyphType.includes('DECIMAL')) {
        this.listIds.numbered = listId; // Store for reuse
        break;
      }
    }
  }
}
```

---

## Behavior

### ✅ What Gets Continued

**All numbered lists in the document:**
- Sequential numbering maintained
- Works across headings
- Works across paragraphs
- Works across tables
- Works across blockquotes

### ❌ What Doesn't Continue

**Bulleted lists:** Each bulleted list is independent (by design)

**Different document:** List IDs are document-specific, not cross-document

**Manual intervention:** If user manually restarts numbering in Google Docs, it breaks the chain

---

## Use Cases

### Technical Documentation
```markdown
1. Install dependencies
2. Configure settings

### Prerequisites

Before proceeding, ensure you have admin access.

3. Run the installer
4. Verify installation
```

### Step-by-Step Procedures
```markdown
1. Open the application
2. Navigate to settings

#### Note About Security

Make sure you're connected to a secure network.

3. Enter credentials
4. Click submit
```

### Complex Instructions with Sections
```markdown
# Setup Instructions

1. Download the software
2. Extract files

## Configuration

3. Edit config.yml
4. Set your API key

## Running the Application

5. Execute start.sh
6. Verify output
```

---

## Implementation in docsPublisher.js

### Constructor Change
```javascript
constructor(auth) {
  // ... existing code ...
  this.listIds = {}; // Track list IDs for continuing numbered lists
}
```

### insertList Method Updates
```javascript
// Determine list ID for numbered lists
if (block.ordered) {
  if (!this.listIds.numbered) {
    this.listIds.numbered = 'pending';
  }
}

// When creating bullets
const bulletRequest = {
  createParagraphBullets: {
    range: { startIndex, endIndex },
    bulletPreset: block.ordered ? 'NUMBERED_DECIMAL_ALPHA_ROMAN' : 'BULLET_DISC_CIRCLE_SQUARE'
  }
};

// Add listId if we have one
if (block.ordered && this.listIds.numbered && this.listIds.numbered !== 'pending') {
  bulletRequest.createParagraphBullets.listId = this.listIds.numbered;
}
```

### publish Method Updates
```javascript
// After batch updates
await this.docs.documents.batchUpdate({
  documentId: this.docId,
  requestBody: { requests: this.requests }
});

// Capture list IDs
await this.captureListIds();
```

---

## Limitations

### Current Implementation

**Single numbered list sequence:**
- All numbered lists in document share one sequence
- No support for multiple independent numbered sequences
- No support for restarting numbering

**No nested list continuation:**
- Nested lists (indented) may not continue correctly
- Only top-level numbered lists are tracked

**Performance:**
- Requires document read-back after each batch
- Slight overhead for list ID capture
- Minimal impact on typical documents

---

## Future Enhancements

Possible improvements:
- **Multiple sequences:** Support different numbered list streams (e.g., main steps vs. substeps)
- **Explicit restart:** Markdown syntax to force restart numbering
- **Nested lists:** Better handling of nested/indented numbered lists
- **List types:** Different numbering styles (A, B, C or i, ii, iii)

---

## Testing

To test list continuation:

```bash
cd "Google Docs Publisher"
node index.js test-lists.md
```

**Sample test file:**
```markdown
1. First item
2. Second item

## Interruption

3. Should be number 3
4. Should be number 4

Some paragraph text here.

5. Should be number 5
6. Should be number 6
```

**Expected result:** Numbers 1-6 sequential throughout the document.

---

## Benefits

✅ **Professional appearance** - No confusing restarts
✅ **Accurate numbering** - Reflects intended sequence
✅ **Automatic** - No manual intervention needed
✅ **Flexible** - Works with complex document structures
✅ **Reliable** - Uses Google Docs native list management

**Your numbered lists now continue correctly across interruptions!**
