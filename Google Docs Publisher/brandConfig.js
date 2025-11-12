/**
 * Brand styling configuration for PACHYDERM GLOBAL documents
 *
 * Font: Poppins (Google Fonts)
 * Available weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
 */

const BRAND = {
  TITLE: {
    fontFamily: 'Poppins',
    fontWeight: 700,           // Bold
    color: '#2e4387',
    fontSizePt: 18,
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  H1: {
    fontFamily: 'Poppins',
    fontWeight: 500,           // Medium
    color: '#2e4387',
    fontSizePt: 16,
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  H2: {
    fontFamily: 'Poppins',
    fontWeight: 500,           // Medium
    color: '#2e4387',
    fontSizePt: 14,
    underline: false,          // No underline
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  H3: {
    fontFamily: 'Poppins',
    fontWeight: 500,           // Medium
    color: '#2e4387',
    fontSizePt: 13,
    underline: false,          // No underline
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  H4: {
    fontFamily: 'Poppins',
    fontWeight: 500,           // Medium
    color: '#2e4387',
    fontSizePt: 11,
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  H5: {
    fontFamily: 'Poppins',
    fontWeight: 400,           // Normal/Regular
    color: '#2e4387',
    fontSizePt: 10,
    underline: true,           // Underlined
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  H6: {
    fontFamily: 'Poppins',
    fontWeight: 400,           // Normal/Regular (fallback if H6 is used)
    color: '#2e4387',
    fontSizePt: 10,
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  BODY: {
    fontFamily: 'Poppins',
    fontWeight: 300,           // Light
    color: '#222222',
    fontSizePt: 10,
    lineSpacing: 1.15,
    beforeSpacingPt: 0,
    afterSpacingPt: 0
  },
  LIST: {
    fontFamily: 'Poppins',
    fontWeight: 300,           // Light
    color: '#222222',
    fontSizePt: 10,
    lineSpacing: 1.0,          // Single spacing for lists
    beforeSpacingPt: 0,
    afterSpacingPt: 0          // No spacing between list items
  },
  CODE: {
    fontFamily: 'Source Code Pro',
    fontWeight: 400,           // Regular
    color: '#222222',
    fontSizePt: 10,
    lineSpacing: 1.15,
    beforeSpacingPt: 4,
    afterSpacingPt: 4,
    backgroundColor: '#F5F5F5'
  },
  BLOCKQUOTE: {
    fontFamily: 'Poppins',
    fontWeight: 400,           // Regular (italic will be applied separately)
    color: '#222222',
    fontSizePt: 10,
    italic: true,
    lineSpacing: 1.15,
    beforeSpacingPt: 6,
    afterSpacingPt: 3,
    indentStart: 36,
    borderLeft: true,
    borderColor: '#CCCCCC'
  },
  TABLE: {
    borderColor: '#000000',
    borderWidth: 0.5,
    headerBackgroundColor: '#2e4387',  // Match heading color
    headerTextColor: '#FFFFFF',        // White text
    headerFontFamily: 'Poppins',
    headerFontWeight: 600,             // Semi-Bold for table headers
    headerFontSizePt: 10,
    cellPaddingPt: 6,
    cellFontFamily: 'Poppins',
    cellFontWeight: 400,               // Regular for table cells
    cellFontSizePt: 10,
    cellTextColor: '#222222',
    cellLineSpacing: 1.0,              // Single spacing
    cellBeforeSpacingPt: 0,
    cellAfterSpacingPt: 0,
    pinHeaderRow: true                 // Pin top row
  },
  PAGE: {
    // Page margins (in points: 1 inch = 72 points)
    marginTop: 72,        // 1 inch
    marginBottom: 36,     // 0.5 inch
    marginLeft: 54,       // 0.75 inch
    marginRight: 54,      // 0.75 inch
    // Header and footer margins (distance from edge of page)
    marginHeader: 18,     // 0.25 inch from top edge
    marginFooter: 18      // 0.25 inch from bottom edge
  },
  FOOTER_TEXT: '© PACHYDERM GLOBAL 2025 — Confidential'
};

/**
 * Convert hex color to RGB object for Google Docs API
 * @param {string} hex - Hex color string (e.g., "#044A74")
 * @returns {Object} RGB object with values 0-1
 */
function hexToRgb(hex) {
  const r = parseInt(hex.slice(1, 3), 16) / 255;
  const g = parseInt(hex.slice(3, 5), 16) / 255;
  const b = parseInt(hex.slice(5, 7), 16) / 255;
  return { red: r, green: g, blue: b };
}

/**
 * Map heading level to brand style configuration
 * @param {number} level - Heading level (1-6)
 * @returns {Object} Brand style object
 */
function getBrandStyleForHeading(level) {
  switch (level) {
    case 1: return BRAND.H1;
    case 2: return BRAND.H2;
    case 3: return BRAND.H3;
    case 4: return BRAND.H4;
    case 5: return BRAND.H5;
    case 6: return BRAND.H6;
    default: return BRAND.BODY;
  }
}

/**
 * Map heading level to Google Docs named style type
 * @param {number} level - Heading level (1-6)
 * @returns {string} Named style type
 */
function getNamedStyleForHeading(level) {
  switch (level) {
    case 1: return 'HEADING_1';
    case 2: return 'HEADING_2';
    case 3: return 'HEADING_3';
    case 4: return 'HEADING_4';
    case 5: return 'HEADING_5';
    case 6: return 'HEADING_6';
    default: return 'NORMAL_TEXT';
  }
}

export {
  BRAND,
  hexToRgb,
  getBrandStyleForHeading,
  getNamedStyleForHeading
};
