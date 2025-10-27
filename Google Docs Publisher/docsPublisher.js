import { google } from "googleapis";
import {
  BRAND,
  hexToRgb,
  getBrandStyleForHeading,
  getNamedStyleForHeading
} from('./brandConfig.js');

/**
 * Publish parsed markdown blocks to Google Docs
 */
class DocsPublisher {
  constructor(auth) {
    this.docs = google.docs({ version: 'v1', auth });
    this.drive = google.drive({ version: 'v3', auth });
    this.requests = [];
    this.cursorIndex = 1; // Docs body starts at index 1
  }

  /**
   * Safely create a dimension object with proper units
   */
  makeDimension(magnitude) {
    return {
      magnitude: magnitude || 0,
      unit: 'PT'
    };
  }

  /**
   * Create a new Google Doc and publish content
   * @param {string} title - Document title
   * @param {Array} blocks - Parsed markdown blocks
   * @returns {Promise<Object>} Document info with ID and URL
   */
  async publish(title, blocks) {
    // Create empty document
    const createRes = await this.docs.documents.create({
      requestBody: { title }
    });

    this.docId = createRes.data.documentId;
    this.requests = [];
    this.cursorIndex = 1;

    // Build all content requests
    blocks.forEach(block => this.processBlock(block));

    // Execute all requests in a single batch update
    if (this.requests.length > 0) {
      await this.docs.documents.batchUpdate({
        documentId: this.docId,
        requestBody: { requests: this.requests }
      });
    }

    return {
      documentId: this.docId,
      url: `https://docs.google.com/document/d/${this.docId}/edit`,
      title
    };
  }

  /**
   * Process a single block and add appropriate requests
   */
  processBlock(block) {
    switch (block.type) {
      case 'heading':
        this.insertHeading(block);
        break;
      case 'paragraph':
        this.insertParagraph(block);
        break;
      case 'list':
        this.insertList(block);
        break;
      case 'codeblock':
        this.insertCodeBlock(block);
        break;
      case 'blockquote':
        this.insertBlockquote(block);
        break;
      case 'table':
        this.insertTable(block);
        break;
      case 'hr':
        this.insertHorizontalRule();
        break;
      default:
        console.warn(`Unknown block type: ${block.type}`);
    }
  }

  /**
   * Insert a heading with brand styling
   */
  insertHeading(block) {
    const brandStyle = getBrandStyleForHeading(block.level);
    const namedStyle = getNamedStyleForHeading(block.level);

    this.insertStyledParagraph(
      block.runs,
      namedStyle,
      brandStyle
    );
  }

  /**
   * Insert a regular paragraph with body styling
   */
  insertParagraph(block) {
    this.insertStyledParagraph(
      block.runs,
      'NORMAL_TEXT',
      BRAND.BODY
    );
  }

  /**
   * Insert a styled paragraph with runs
   */
  insertStyledParagraph(runs, namedStyle, brandStyle) {
    const startIndex = this.cursorIndex;
    const fullText = runs.map(r => r.text).join('') + '\n';
    const endIndex = startIndex + fullText.length;

    // 1. Insert text
    this.requests.push({
      insertText: {
        location: { index: startIndex },
        text: fullText
      }
    });

    // 2. Apply inline formatting to each run
    let offset = 0;
    runs.forEach(run => {
      const runStart = startIndex + offset;
      const runEnd = runStart + run.text.length;

      const textStyle = {};

      // Inline formatting
      if (run.bold) textStyle.bold = true;
      if (run.italic) textStyle.italic = true;
      if (run.strikethrough) textStyle.strikethrough = true;

      // Code styling
      if (run.code) {
        // textStyle.fontFamily = BRAND.CODE.fontFamily; // TODO: Fix API field
        textStyle.fontSize = { magnitude: BRAND.CODE.fontSizePt, unit: 'PT' };
        textStyle.backgroundColor = {
          color: { rgbColor: hexToRgb(BRAND.CODE.backgroundColor) }
        };
      }

      // Links
      if (run.link) {
        textStyle.link = { url: run.link };
        textStyle.underline = true;
        textStyle.foregroundColor = {
          color: { rgbColor: hexToRgb('#0066CC') }
        };
      }

      if (Object.keys(textStyle).length > 0) {
        this.requests.push({
          updateTextStyle: {
            range: { startIndex: runStart, endIndex: runEnd },
            textStyle,
            fields: Object.keys(textStyle).join(',')
          }
        });
      }

      offset += run.text.length;
    });

    // 3. Apply paragraph-level brand styling
    this.requests.push({
      updateParagraphStyle: {
        range: { startIndex, endIndex },
        paragraphStyle: {
          namedStyleType: namedStyle,
          lineSpacing: (brandStyle.lineSpacing || 1.15) * 100,
          spaceAbove: this.makeDimension(brandStyle.beforeSpacingPt),
          spaceBelow: this.makeDimension(brandStyle.afterSpacingPt)
        },
        fields: 'namedStyleType,lineSpacing,spaceAbove,spaceBelow'
      }
    });

    // 4. Apply brand font, size, color
    this.requests.push({
      updateTextStyle: {
        range: { startIndex, endIndex: endIndex - 1 }, // Exclude newline
        textStyle: {
          bold: brandStyle.bold,
          fontSize: this.makeDimension(brandStyle.fontSizePt),
          foregroundColor: {
            color: { rgbColor: hexToRgb(brandStyle.color) }
          }
        },
        fields: 'bold,fontSize,foregroundColor'
      }
    });

    this.cursorIndex = endIndex;
  }

  /**
   * Insert a bulleted or numbered list
   */
  insertList(block) {
    const listStartIndex = this.cursorIndex;
    const listItems = [];

    block.items.forEach(item => {
      const itemStartIndex = this.cursorIndex;
      const text = item.runs.map(r => r.text).join('') + '\n';

      // Insert text
      this.requests.push({
        insertText: {
          location: { index: this.cursorIndex },
          text
        }
      });

      const itemEndIndex = this.cursorIndex + text.length;

      // Apply inline formatting
      let offset = 0;
      item.runs.forEach(run => {
        const runStart = itemStartIndex + offset;
        const runEnd = runStart + run.text.length;

        const textStyle = {};
        if (run.bold) textStyle.bold = true;
        if (run.italic) textStyle.italic = true;
        if (run.link) {
          textStyle.link = { url: run.link };
          textStyle.underline = true;
        }

        if (Object.keys(textStyle).length > 0) {
          this.requests.push({
            updateTextStyle: {
              range: { startIndex: runStart, endIndex: runEnd },
              textStyle,
              fields: Object.keys(textStyle).join(',')
            }
          });
        }

        offset += run.text.length;
      });

      // Apply body styling
      this.requests.push({
        updateTextStyle: {
          range: { startIndex: itemStartIndex, endIndex: itemEndIndex - 1 },
          textStyle: {
            fontSize: this.makeDimension(BRAND.BODY.fontSizePt),
            foregroundColor: {
              color: { rgbColor: hexToRgb(BRAND.BODY.color) }
            }
          },
          fields: 'fontSize,foregroundColor'
        }
      });

      listItems.push({
        startIndex: itemStartIndex,
        endIndex: itemEndIndex
      });

      this.cursorIndex = itemEndIndex;
    });

    // Apply bullet/numbering to all items
    listItems.forEach(item => {
      this.requests.push({
        createParagraphBullets: {
          range: {
            startIndex: item.startIndex,
            endIndex: item.endIndex
          },
          bulletPreset: block.ordered ? 'NUMBERED_DECIMAL_ALPHA_ROMAN' : 'BULLET_DISC_CIRCLE_SQUARE'
        }
      });
    });
  }

  /**
   * Insert a code block with monospace styling
   */
  insertCodeBlock(block) {
    const lines = block.value.split('\n');
    const text = lines.join('\n') + '\n';
    const startIndex = this.cursorIndex;
    const endIndex = startIndex + text.length;

    // Insert code text
    this.requests.push({
      insertText: {
        location: { index: startIndex },
        text
      }
    });

    // Apply code styling
    this.requests.push({
      updateTextStyle: {
        range: { startIndex, endIndex: endIndex - 1 },
        textStyle: {
          fontSize: this.makeDimension(BRAND.CODE.fontSizePt),
          foregroundColor: {
            color: { rgbColor: hexToRgb(BRAND.CODE.color) }
          },
          backgroundColor: {
            color: { rgbColor: hexToRgb(BRAND.CODE.backgroundColor) }
          }
        },
        fields: 'fontSize,foregroundColor,backgroundColor'
      }
    });

    // Set paragraph style
    this.requests.push({
      updateParagraphStyle: {
        range: { startIndex, endIndex },
        paragraphStyle: {
          lineSpacing: BRAND.CODE.lineSpacing * 100,
          spaceAbove: this.makeDimension(BRAND.CODE.beforeSpacingPt),
          spaceBelow: this.makeDimension(BRAND.CODE.afterSpacingPt)
        },
        fields: 'lineSpacing,spaceAbove,spaceBelow'
      }
    });

    this.cursorIndex = endIndex;
  }

  /**
   * Insert a blockquote
   */
  insertBlockquote(block) {
    // Flatten blockquote blocks into simple paragraphs with blockquote styling
    block.blocks.forEach(innerBlock => {
      if (innerBlock.type === 'paragraph') {
        // Insert as styled paragraph with blockquote styling
        const startIndex = this.cursorIndex;
        const fullText = innerBlock.runs.map(r => r.text).join('') + '\n';
        const endIndex = startIndex + fullText.length;

        // 1. Insert text
        this.requests.push({
          insertText: {
            location: { index: startIndex },
            text: fullText
          }
        });

        // 1.5 Apply inline formatting to runs
        let offset = 0;
        innerBlock.runs.forEach(run => {
          const runStart = startIndex + offset;
          const runEnd = runStart + run.text.length;

          const textStyle = {};
          if (run.bold) textStyle.bold = true;
          if (run.italic) textStyle.italic = true;
          if (run.link) {
            textStyle.link = { url: run.link };
            textStyle.underline = true;
          }

          if (Object.keys(textStyle).length > 0) {
            this.requests.push({
              updateTextStyle: {
                range: { startIndex: runStart, endIndex: runEnd },
                textStyle,
                fields: Object.keys(textStyle).join(',')
              }
            });
          }

          offset += run.text.length;
        });

        // 2. Apply blockquote paragraph style
        this.requests.push({
          updateParagraphStyle: {
            range: { startIndex, endIndex },
            paragraphStyle: {
              lineSpacing: (BRAND.BLOCKQUOTE.lineSpacing || 1.15) * 100,
              spaceAbove: this.makeDimension(BRAND.BLOCKQUOTE.beforeSpacingPt),
              spaceBelow: this.makeDimension(BRAND.BLOCKQUOTE.afterSpacingPt),
              indentStart: this.makeDimension(BRAND.BLOCKQUOTE.indentStart)
              // Note: borderLeft is not supported via API - would need manual styling
            },
            fields: 'lineSpacing,spaceAbove,spaceBelow,indentStart'
          }
        });

        // 3. Apply blockquote text style
        this.requests.push({
          updateTextStyle: {
            range: { startIndex, endIndex: endIndex - 1 },
            textStyle: {
              fontSize: this.makeDimension(BRAND.BLOCKQUOTE.fontSizePt),
              italic: true,
              foregroundColor: {
                color: { rgbColor: hexToRgb(BRAND.BLOCKQUOTE.color) }
              }
            },
            fields: 'fontSize,italic,foregroundColor'
          }
        });

        this.cursorIndex = endIndex;
      } else {
        // For other block types (headings, lists), process normally without blockquote styling
        this.processBlock(innerBlock);
      }
    });
  }

  /**
   * Insert a table with proper formatting
   */
  insertTable(block) {
    const rows = block.rows.length;
    const cols = block.rows[0]?.length || 1;
    const tableStartIndex = this.cursorIndex;

    // 1. Insert the table structure
    this.requests.push({
      insertTable: {
        rows,
        columns: cols,
        location: { index: tableStartIndex }
      }
    });

    // Calculate table structure (Google Docs table format)
    // After insertion, the cursor will be at: tableStartIndex + 3 (header) + rows*cols*2 + rows + 1
    // This is complex, so we'll track it carefully

    let cellIndex = tableStartIndex + 3; // Tables start with some overhead

    // 2. Populate and style cells
    block.rows.forEach((row, rowIdx) => {
      row.forEach((cell, colIdx) => {
        const cellText = cell.runs.map(r => r.text).join('');

        if (cellText.trim()) {
          // Insert text into cell
          this.requests.push({
            insertText: {
              location: { index: cellIndex },
              text: cellText
            }
          });

          const cellEndIndex = cellIndex + cellText.length;

          // Style cell text
          const isHeader = rowIdx === 0;
          // const fontFamily = isHeader ? BRAND.TABLE.headerFontFamily : BRAND.BODY.fontFamily; // TODO: Fix API field
          const bold = isHeader ? BRAND.TABLE.headerBold : false;

          this.requests.push({
            updateTextStyle: {
              range: { startIndex: cellIndex, endIndex: cellEndIndex },
              textStyle: {
                weightedFontFamily,
                fontSize: this.makeDimension(BRAND.BODY.fontSizePt),
                bold,
                foregroundColor: {
                  color: { rgbColor: hexToRgb(BRAND.BODY.color) }
                }
              },
              fields: 'fontSize,bold,foregroundColor'
            }
          });

          // Apply inline formatting from runs
          let offset = 0;
          cell.runs.forEach(run => {
            const runStart = cellIndex + offset;
            const runEnd = runStart + run.text.length;

            const textStyle = {};
            if (run.bold) textStyle.bold = true;
            if (run.italic) textStyle.italic = true;
            if (run.link) {
              textStyle.link = { url: run.link };
              textStyle.underline = true;
            }

            if (Object.keys(textStyle).length > 0) {
              this.requests.push({
                updateTextStyle: {
                  range: { startIndex: runStart, endIndex: runEnd },
                  textStyle,
                  fields: Object.keys(textStyle).join(',')
                }
              });
            }

            offset += run.text.length;
          });

          cellIndex = cellEndIndex;
        }

        cellIndex += 2; // Move to next cell (includes cell marker)
      });
      cellIndex += 1; // Move to next row
    });

    // Update cursor to after table
    this.cursorIndex = cellIndex;

    // 3. Apply table styling (borders, header background)
    // Note: Table styling in Google Docs API is limited
    // We can set borders via updateTableCellStyle for each cell
  }

  /**
   * Insert a horizontal rule (represented as a centered line)
   */
  insertHorizontalRule() {
    const text = '—'.repeat(20) + '\n';
    const startIndex = this.cursorIndex;
    const endIndex = startIndex + text.length;

    this.requests.push({
      insertText: {
        location: { index: startIndex },
        text
      }
    });

    this.requests.push({
      updateParagraphStyle: {
        range: { startIndex, endIndex },
        paragraphStyle: {
          alignment: 'CENTER',
          spaceAbove: this.makeDimension(6),
          spaceBelow: this.makeDimension(6)
        },
        fields: 'alignment,spaceAbove,spaceBelow'
      }
    });

    this.requests.push({
      updateTextStyle: {
        range: { startIndex, endIndex: endIndex - 1 },
        textStyle: {
          foregroundColor: {
            color: { rgbColor: hexToRgb('#CCCCCC') }
          }
        },
        fields: 'foregroundColor'
      }
    });

    this.cursorIndex = endIndex;
  }
}

export default DocsPublisher;
