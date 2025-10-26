/**
 * Brand styling configuration for Pachyderm Global documents
 */

const BRAND = {
  TITLE: {
    fontFamily: 'Rubik',
    color: '#044A74',
    fontSizePt: 26,
    bold: true,
    lineSpacing: 1.08,
    beforeSpacingPt: 0,
    afterSpacingPt: 8
  },
  H1: {
    fontFamily: 'Rubik',
    color: '#044A74',
    fontSizePt: 20,
    bold: true,
    lineSpacing: 1.10,
    beforeSpacingPt: 12,
    afterSpacingPt: 6
  },
  H2: {
    fontFamily: 'Rubik',
    color: '#4F81BD',
    fontSizePt: 16,
    bold: true,
    lineSpacing: 1.10,
    beforeSpacingPt: 10,
    afterSpacingPt: 5
  },
  H3: {
    fontFamily: 'Rubik',
    color: '#4F81BD',
    fontSizePt: 14,
    bold: true,
    lineSpacing: 1.10,
    beforeSpacingPt: 8,
    afterSpacingPt: 4
  },
  H4: {
    fontFamily: 'Rubik',
    color: '#4F81BD',
    fontSizePt: 12,
    bold: true,
    lineSpacing: 1.10,
    beforeSpacingPt: 6,
    afterSpacingPt: 3
  },
  H5: {
    fontFamily: 'Rubik',
    color: '#222222',
    fontSizePt: 11.5,
    bold: true,
    lineSpacing: 1.10,
    beforeSpacingPt: 4,
    afterSpacingPt: 2
  },
  H6: {
    fontFamily: 'Rubik',
    color: '#222222',
    fontSizePt: 11,
    bold: true,
    lineSpacing: 1.10,
    beforeSpacingPt: 4,
    afterSpacingPt: 2
  },
  BODY: {
    fontFamily: 'Source Sans 3',
    color: '#222222',
    fontSizePt: 11.5,
    bold: false,
    lineSpacing: 1.28,
    beforeSpacingPt: 0,
    afterSpacingPt: 4
  },
  CODE: {
    fontFamily: 'Source Code Pro',
    color: '#222222',
    fontSizePt: 10,
    bold: false,
    lineSpacing: 1.15,
    beforeSpacingPt: 4,
    afterSpacingPt: 4,
    backgroundColor: '#F5F5F5'
  },
  BLOCKQUOTE: {
    fontFamily: 'Source Sans 3',
    color: '#555555',
    fontSizePt: 11,
    bold: false,
    italic: true,
    lineSpacing: 1.28,
    beforeSpacingPt: 4,
    afterSpacingPt: 4,
    indentStart: 36,
    borderLeft: true,
    borderColor: '#CCCCCC'
  },
  TABLE: {
    borderColor: '#CCCCCC',
    headerBackgroundColor: '#F0F0F0',
    headerFontFamily: 'Source Sans 3',
    headerBold: true,
    cellPaddingPt: 6
  },
  FOOTER_TEXT: '© Pachyderm Global 2025 — Confidential'
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

module.exports = {
  BRAND,
  hexToRgb,
  getBrandStyleForHeading,
  getNamedStyleForHeading
};
