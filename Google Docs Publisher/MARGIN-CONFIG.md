# Document Margin Configuration

**Feature:** Automatically sets page margins and header/footer margins when publishing to Google Docs.

---

## Current Default Settings

### Page Margins (from content edge)
- **Top:** 1 inch (72pt)
- **Bottom:** 1 inch (72pt)
- **Left:** 1 inch (72pt)
- **Right:** 1 inch (72pt)

### Header/Footer Margins (from page edge)
- **Header:** 0.5 inch (36pt) from top edge
- **Footer:** 0.5 inch (36pt) from bottom edge

**Note:** 1 inch = 72 points

---

## Visual Layout

```
┌─────────────────────────────────────────────────┐
│ ← 0.5" →  HEADER AREA                          │
│ ─────────────────────────────────────────────── │
│ ← 1" →    CONTENT AREA                          │
│           (Your document content)               │
│           Top margin: 1"                        │
│           Left margin: 1"                       │
│           Right margin: 1" →                    │
│           Bottom margin: 1"                     │
│ ─────────────────────────────────────────────── │
│ ← 0.5" →  FOOTER AREA                          │
└─────────────────────────────────────────────────┘
```

---

## Configuration

Edit `brandConfig.js` to customize margins:

```javascript
PAGE: {
  // Page margins (in points: 1 inch = 72 points)
  marginTop: 72,        // 1 inch
  marginBottom: 72,     // 1 inch
  marginLeft: 72,       // 1 inch
  marginRight: 72,      // 1 inch

  // Header and footer margins (distance from edge of page)
  marginHeader: 36,     // 0.5 inch from top edge
  marginFooter: 36      // 0.5 inch from bottom edge
}
```

---

## Common Margin Presets

### Standard (Current Default)
```javascript
marginTop: 72,     // 1"
marginBottom: 72,  // 1"
marginLeft: 72,    // 1"
marginRight: 72    // 1"
```
**Use for:** General business documents, proposals

### Narrow (More content per page)
```javascript
marginTop: 36,     // 0.5"
marginBottom: 36,  // 0.5"
marginLeft: 36,    // 0.5"
marginRight: 36    // 0.5"
```
**Use for:** Dense technical documents, specifications

### Wide (More whitespace)
```javascript
marginTop: 108,    // 1.5"
marginBottom: 108, // 1.5"
marginLeft: 108,   // 1.5"
marginRight: 108   // 1.5"
```
**Use for:** Executive summaries, presentation materials

### Moderate (Balanced)
```javascript
marginTop: 54,     // 0.75"
marginBottom: 54,  // 0.75"
marginLeft: 54,    // 0.75"
marginRight: 54    // 0.75"
```
**Use for:** Standard reports, general correspondence

---

## Point-to-Inch Conversion

| Inches | Points | Usage |
|--------|--------|-------|
| 0.25"  | 18pt   | Minimal margin |
| 0.5"   | 36pt   | Narrow margin |
| 0.75"  | 54pt   | Moderate margin |
| 1"     | 72pt   | Standard margin (default) |
| 1.25"  | 90pt   | Comfortable margin |
| 1.5"   | 108pt  | Wide margin |
| 2"     | 144pt  | Extra wide margin |

**Formula:** `points = inches × 72`

---

## Header and Footer Margins Explained

### What They Control

**marginHeader:** Distance from **top edge of page** to header content
**marginFooter:** Distance from **bottom edge of page** to footer content

### Relationship to Page Margins

```
Page Edge (top)
    ↓
    [marginHeader: 36pt = 0.5"]
    ↓
Header Content Area
    ↓
    [marginTop: 72pt = 1"]
    ↓
Content Area (your document text)
    ↓
    [marginBottom: 72pt = 1"]
    ↓
Footer Content Area
    ↓
    [marginFooter: 36pt = 0.5"]
    ↓
Page Edge (bottom)
```

### Common Configurations

**Standard (default):**
```javascript
marginHeader: 36,  // 0.5" from top edge
marginFooter: 36   // 0.5" from bottom edge
```

**Compact (headers/footers closer to edge):**
```javascript
marginHeader: 18,  // 0.25" from top edge
marginFooter: 18   // 0.25" from bottom edge
```

**Spacious (headers/footers away from edge):**
```javascript
marginHeader: 54,  // 0.75" from top edge
marginFooter: 54   // 0.75" from bottom edge
```

---

## How It Works

### Implementation in docsPublisher.js

Margins are set immediately after document creation:

```javascript
async publish(title, blocks) {
  // Create empty document
  const createRes = await this.docs.documents.create({
    requestBody: { title }
  });

  this.docId = createRes.data.documentId;

  // Set document margins FIRST (before adding content)
  await this.setDocumentMargins();

  // Then add content...
}
```

### API Request Structure

```javascript
{
  updateDocumentStyle: {
    documentStyle: {
      marginTop: { magnitude: 72, unit: 'PT' },
      marginBottom: { magnitude: 72, unit: 'PT' },
      marginLeft: { magnitude: 72, unit: 'PT' },
      marginRight: { magnitude: 72, unit: 'PT' },
      marginHeader: { magnitude: 36, unit: 'PT' },
      marginFooter: { magnitude: 36, unit: 'PT' }
    },
    fields: 'marginTop,marginBottom,marginLeft,marginRight,marginHeader,marginFooter'
  }
}
```

---

## Use Cases by Document Type

### Business Proposals
```javascript
marginTop: 72,     // 1"
marginBottom: 72,  // 1"
marginLeft: 72,    // 1"
marginRight: 72,   // 1"
marginHeader: 36,  // 0.5"
marginFooter: 36   // 0.5"
```
Professional standard margins with adequate whitespace.

### Technical Specifications
```javascript
marginTop: 54,     // 0.75"
marginBottom: 54,  // 0.75"
marginLeft: 54,    // 0.75"
marginRight: 54,   // 0.75"
marginHeader: 36,  // 0.5"
marginFooter: 36   // 0.5"
```
Moderate margins for more content per page while maintaining readability.

### Executive Summaries
```javascript
marginTop: 108,    // 1.5"
marginBottom: 108, // 1.5"
marginLeft: 108,   // 1.5"
marginRight: 108,  // 1.5"
marginHeader: 54,  // 0.75"
marginFooter: 54   // 0.75"
```
Wide margins create premium feel with lots of whitespace.

### Data Sheets / Specifications
```javascript
marginTop: 36,     // 0.5"
marginBottom: 36,  // 0.5"
marginLeft: 36,    // 0.5"
marginRight: 36,   // 0.5"
marginHeader: 18,  // 0.25"
marginFooter: 18   // 0.25"
```
Narrow margins maximize content space for dense information.

---

## Google Docs Default vs Our Settings

### Google Docs Default
- Top: 1 inch
- Bottom: 1 inch
- Left: 1 inch
- Right: 1 inch
- Header: 0.5 inch
- Footer: 0.5 inch

### Our Settings (Same as Google Default)
- Top: 1 inch ✓
- Bottom: 1 inch ✓
- Left: 1 inch ✓
- Right: 1 inch ✓
- Header: 0.5 inch ✓
- Footer: 0.5 inch ✓

**We match Google Docs defaults** for consistency and familiarity.

---

## Changing Margins

### Step 1: Edit brandConfig.js

```javascript
PAGE: {
  marginTop: 54,        // Change from 72 to 54 (0.75")
  marginBottom: 54,     // Change from 72 to 54 (0.75")
  marginLeft: 54,       // Change from 72 to 54 (0.75")
  marginRight: 54,      // Change from 72 to 54 (0.75")
  marginHeader: 36,     // Keep at 0.5"
  marginFooter: 36      // Keep at 0.5"
}
```

### Step 2: Save and Test

```bash
cd "Google Docs Publisher"
node index.js TEST-MINIMAL.md
```

### Step 3: Verify in Google Docs

Open published document → File → Page Setup → Check margins

---

## Important Notes

### Timing
- Margins are set **immediately after document creation**
- Applied **before any content is added**
- Cannot be changed after content is published (would require manual edit in Google Docs)

### Units
- All values in **points (PT)**
- Google Docs API requires point values
- 1 inch = 72 points (standard conversion)

### Automatic Application
- Margins apply to **entire document**
- No per-section margin control in current implementation
- Consistent across all pages

### Validation
- Google Docs will reject invalid margin values
- Margins must be positive numbers
- Very large margins (> 3 inches) may look odd

---

## Benefits

✅ **Consistent formatting** across all published documents
✅ **Automated** - no manual margin adjustment needed
✅ **Customizable** - easy to change in brandConfig.js
✅ **Professional** - matches business document standards
✅ **Control** - header/footer positioning configurable

---

## Future Enhancements

Possible additions:
- Per-section margin control
- Different first-page margins
- Portrait vs landscape margin presets
- A4 vs Letter size presets
- Command-line margin override

---

**Margins are now automatically configured!** Your published documents will have consistent, professional spacing.
