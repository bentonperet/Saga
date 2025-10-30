import { google } from "googleapis";
import {
  BRAND,
  hexToRgb,
  getBrandStyleForHeading,
  getNamedStyleForHeading
} from './brandConfig.js';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// ES module equivalent of __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Path to the logo file
const LOGO_PATH = path.join(__dirname, '..', 'Saga Pryor DC', 'Elephant Globe No_Inner_Shadow 220x230 no Words 20250128.png');

/**
 * Publish parsed markdown blocks to Google Docs
 */
class DocsPublisher {
  constructor(auth) {
    this.auth = auth;
    this.docs = google.docs({ version: 'v1', auth });
    this.drive = google.drive({ version: 'v3', auth });
    this.requests = [];
    this.cursorIndex = 1; // Docs body starts at index 1
    this.logoImageId = null;
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
   * Upload logo image to Google Drive and return the image ID
   * @returns {Promise<string>} Image ID for use in Google Docs
   */
  async uploadLogo() {
    if (this.logoImageId) {
      return this.logoImageId; // Already uploaded
    }

    if (!fs.existsSync(LOGO_PATH)) {
      console.warn('⚠️  Logo file not found, skipping header');
      return null;
    }

    try {
      const fileMetadata = {
        name: 'Pachyderm Global Logo',
        mimeType: 'image/png'
      };

      const media = {
        mimeType: 'image/png',
        body: fs.createReadStream(LOGO_PATH)
      };

      const file = await this.drive.files.create({
        requestBody: fileMetadata,
        media: media,
        fields: 'id'
      });

      // Make the image accessible to anyone with the link
      await this.drive.permissions.create({
        fileId: file.data.id,
        requestBody: {
          role: 'reader',
          type: 'anyone'
        }
      });

      this.logoImageId = file.data.id;
      return this.logoImageId;
    } catch (error) {
      console.warn('⚠️  Failed to upload logo:', error.message);
      return null;
    }
  }

  /**
   * Insert Pachyderm Global branded header at the top of the document
   */
  async insertHeader() {
    // Upload logo first
    const imageId = await this.uploadLogo();
    if (!imageId) {
      return; // Skip header if logo upload failed
    }

    const startIndex = this.cursorIndex;

    // Get the logo URL for embedding
    const imageUrl = `https://drive.google.com/uc?id=${imageId}`;

    // Insert a table for the header layout (1 row, 2 columns)
    await this.docs.documents.batchUpdate({
      documentId: this.docId,
      requestBody: {
        requests: [{
          insertTable: {
            rows: 1,
            columns: 2,
            location: { index: startIndex }
          }
        }]
      }
    });

    // Read back document to get table structure
    const doc = await this.docs.documents.get({ documentId: this.docId });
    const headerTable = this.findTableNearIndex(doc.data.body.content, startIndex, 5);

    if (!headerTable) {
      console.warn('⚠️  Could not find header table, skipping header');
      return;
    }

    const tableStartIndex = headerTable.startIndex;
    const leftCell = headerTable.table.tableRows[0].tableCells[0];
    const rightCell = headerTable.table.tableRows[0].tableCells[1];

    // Get cell content indexes - need to find the paragraph inside the cell
    const leftParagraph = leftCell.content[0].paragraph;
    const rightParagraph = rightCell.content[0].paragraph;

    const leftCellIndex = leftParagraph.elements[0].startIndex;
    const rightCellIndex = rightParagraph.elements[0].startIndex;

    // Build header content requests
    const textRequests = [];

    // RIGHT CELL: Insert company info text first
    const companyText =
      'PACHYDERM GLOBAL\n' +
      'CRITICAL INFRASTRUCTURE SERVICES\n' +
      'NA Headquarters\n' +
      '6275 W. Plano Parkway, Suite 500, Plano, Texas 75093 USA\n' +
      '+1 469 727 5717  pgcis.com\n\n' +
      'EMEA Headquarters\n' +
      'Rahmannstraße 11, 65760, Eschborn, Hessen, Germany\n' +
      '+49 6196 97-340-97  pgcis.com/de';

    textRequests.push({
      insertText: {
        location: { index: rightCellIndex },
        text: companyText
      }
    });

    // Style the text in right cell - using dynamic position tracking
    const segments = [
      { text: 'PACHYDERM GLOBAL', style: { bold: true, size: 18, color: '#044A74', font: 'Rubik' } },
      { text: 'CRITICAL INFRASTRUCTURE SERVICES', style: { size: 10, color: '#666666', font: 'Source Sans 3' } },
      { text: 'NA Headquarters', style: { bold: true, size: 9, font: 'Source Sans 3' } },
      { text: '6275 W. Plano Parkway, Suite 500, Plano, Texas 75093 USA', style: { size: 9, font: 'Source Sans 3' } },
      { text: '+1 469 727 5717  ', style: { size: 9, font: 'Source Sans 3' } },
      { text: 'pgcis.com', style: { size: 9, font: 'Source Sans 3', link: 'https://pgcis.com', color: '#4F81BD' } },
      { text: '\n\n', style: null }, // Spacer between sections
      { text: 'EMEA Headquarters', style: { bold: true, size: 9, font: 'Source Sans 3' } },
      { text: 'Rahmannstraße 11, 65760, Eschborn, Hessen, Germany', style: { size: 9, font: 'Source Sans 3' } },
      { text: '+49 6196 97-340-97  ', style: { size: 9, font: 'Source Sans 3' } },
      { text: 'pgcis.com/de', style: { size: 9, font: 'Source Sans 3', link: 'https://pgcis.com/de', color: '#4F81BD' } }
    ];

    let currentIndex = rightCellIndex;
    for (const segment of segments) {
      if (segment.style) {
        const textStyle = {
          fontSize: this.makeDimension(segment.style.size),
          weightedFontFamily: { fontFamily: segment.style.font }
        };

        if (segment.style.bold) {
          textStyle.bold = true;
        }

        if (segment.style.color) {
          textStyle.foregroundColor = {
            color: { rgbColor: hexToRgb(segment.style.color) }
          };
        }

        if (segment.style.link) {
          textStyle.link = { url: segment.style.link };
        }

        const fields = ['fontSize', 'weightedFontFamily'];
        if (segment.style.bold) fields.push('bold');
        if (segment.style.color) fields.push('foregroundColor');
        if (segment.style.link) fields.push('link');

        textRequests.push({
          updateTextStyle: {
            range: {
              startIndex: currentIndex,
              endIndex: currentIndex + segment.text.length
            },
            textStyle,
            fields: fields.join(',')
          }
        });
      }

      currentIndex += segment.text.length;

      // Add newline if not the spacer segment
      if (segment.style && segments.indexOf(segment) < segments.length - 1 && segment.text !== '\n\n') {
        currentIndex += 1; // Account for newline in companyText
      }
    }

    // Remove table borders and set padding
    textRequests.push({
      updateTableCellStyle: {
        tableRange: {
          tableCellLocation: {
            tableStartLocation: { index: tableStartIndex },
            rowIndex: 0,
            columnIndex: 0
          },
          rowSpan: 1,
          columnSpan: 2
        },
        tableCellStyle: {
          paddingTop: this.makeDimension(6),
          paddingBottom: this.makeDimension(12),
          paddingLeft: this.makeDimension(0),
          paddingRight: this.makeDimension(0)
        },
        fields: 'paddingTop,paddingBottom,paddingLeft,paddingRight'
      }
    });

    // Apply text formatting first
    await this.docs.documents.batchUpdate({
      documentId: this.docId,
      requestBody: { requests: textRequests }
    });

    // Now insert the logo image in the left cell
    await this.docs.documents.batchUpdate({
      documentId: this.docId,
      requestBody: {
        requests: [{
          insertInlineImage: {
            location: { index: leftCellIndex },
            uri: imageUrl,
            objectSize: {
              height: { magnitude: 120, unit: 'PT' },
              width: { magnitude: 115, unit: 'PT' }
            }
          }
        }]
      }
    });

    // Update cursor position to after the header table
    this.cursorIndex = headerTable.endIndex;
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
    this.pendingTables = [];

    // Process blocks sequentially, handling tables specially
    for (const block of blocks) {
      if (block.type === 'table') {
        // Flush any pending non-table requests first
        if (this.requests.length > 0) {
          await this.docs.documents.batchUpdate({
            documentId: this.docId,
            requestBody: { requests: this.requests }
          });
          this.requests = [];
        }

        // Insert and populate this table immediately
        const insertIndex = this.cursorIndex;
        await this.insertAndPopulateTable(block, insertIndex);

        // Read back document to find where cursor should be after table
        const doc = await this.docs.documents.get({ documentId: this.docId });
        const table = this.findTableNearIndex(doc.data.body.content, insertIndex);
        if (table) {
          this.cursorIndex = table.endIndex;
        } else {
          console.warn(`Could not find table near index ${insertIndex}, cursor position may be incorrect`);
          // Estimate based on table size
          const rows = block.rows.length;
          const cols = block.rows[0]?.length || 1;
          this.cursorIndex = insertIndex + 3 + (rows * (cols * 2 + 1));
        }
      } else {
        // Regular block - process normally
        this.processBlock(block);
      }
    }

    // Flush any remaining requests
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
   * Insert a table and populate it immediately (two-phase process)
   */
  async insertAndPopulateTable(block, insertIndex) {
    const rows = block.rows.length;
    const cols = block.rows[0]?.length || 1;

    // Phase 1: Create empty table structure
    await this.docs.documents.batchUpdate({
      documentId: this.docId,
      requestBody: {
        requests: [{
          insertTable: {
            rows,
            columns: cols,
            location: { index: insertIndex }
          }
        }]
      }
    });

    // Phase 2: Read back document and populate table
    const doc = await this.docs.documents.get({ documentId: this.docId });

    // Find the table - it might be at insertIndex ±1 due to document structure
    let table = this.findTableAtIndex(doc.data.body.content, insertIndex);

    if (!table) {
      // Try nearby indexes (table structure can shift by 1-2 positions)
      table = this.findTableNearIndex(doc.data.body.content, insertIndex, 5);
    }

    if (!table) {
      console.error(`Could not find table near index ${insertIndex}`);
      return;
    }

    const tableRequests = this.buildTableContentRequests(block, table, rows, cols);

    if (tableRequests.length > 0) {
      try {
        await this.docs.documents.batchUpdate({
          documentId: this.docId,
          requestBody: { requests: tableRequests }
        });
      } catch (error) {
        console.error(`Error populating table:`, error.message);
        if (error.errors) {
          error.errors.forEach(err => console.error(`  - ${err.message}`));
        }
        throw error;
      }
    }
  }

  /**
   * Build requests for table content and styling
   */
  buildTableContentRequests(block, table, rows, cols) {
    const tableRequests = [];
    const startIndex = table.startIndex;

    // Process cells in reverse order to avoid index shifting
    for (let rowIdx = rows - 1; rowIdx >= 0; rowIdx--) {
      const row = block.rows[rowIdx];
      const tableRow = table.table.tableRows[rowIdx];

      for (let colIdx = cols - 1; colIdx >= 0; colIdx--) {
        const cell = row[colIdx] || { runs: [{ text: '' }] };
        const tableCell = tableRow.tableCells[colIdx];

        // Get the actual start index of the cell's first paragraph
        const cellContent = tableCell.content[0];
        if (!cellContent || !cellContent.paragraph) {
          console.warn(`Cell at row ${rowIdx}, col ${colIdx} has no paragraph content`);
          continue;
        }

        // Get the paragraph's first element index (where we can insert)
        const paragraph = cellContent.paragraph;
        let cellStartIndex;

        if (paragraph.elements && paragraph.elements.length > 0) {
          cellStartIndex = paragraph.elements[0].startIndex;
        } else {
          cellStartIndex = cellContent.startIndex + 1;
        }

        const cellText = cell.runs.map(r => r.text).join('');

        // Insert cell content
        if (cellText) {
          tableRequests.push({
            insertText: {
              location: { index: cellStartIndex },
              text: cellText
            }
          });

          // Apply inline formatting
          let offset = 0;
          cell.runs.forEach(run => {
            if (run.text) {
              const runStart = cellStartIndex + offset;
              const runEnd = runStart + run.text.length;

              const textStyle = {};
              if (run.bold) textStyle.bold = true;
              if (run.italic) textStyle.italic = true;
              if (run.strikethrough) textStyle.strikethrough = true;
              if (run.code) {
                textStyle.weightedFontFamily = { fontFamily: BRAND.CODE.fontFamily };
                textStyle.fontSize = this.makeDimension(BRAND.CODE.fontSizePt);
                textStyle.backgroundColor = {
                  color: { rgbColor: hexToRgb(BRAND.CODE.backgroundColor) }
                };
              }

              if (Object.keys(textStyle).length > 0) {
                tableRequests.push({
                  updateTextStyle: {
                    range: { startIndex: runStart, endIndex: runEnd },
                    textStyle,
                    fields: Object.keys(textStyle).join(',')
                  }
                });
              }

              if (run.link) {
                tableRequests.push({
                  updateTextStyle: {
                    range: { startIndex: runStart, endIndex: runEnd },
                    textStyle: {
                      link: { url: run.link },
                      foregroundColor: { color: { rgbColor: hexToRgb('#4F81BD') } },
                      underline: true
                    },
                    fields: 'link,foregroundColor,underline'
                  }
                });
              }

              offset += run.text.length;
            }
          });
        }

        // Apply header row styling (white text on dark blue background)
        if (rowIdx === 0 && cellText) {
          const cellEndIndex = cellStartIndex + cellText.length;
          tableRequests.push({
            updateTextStyle: {
              range: { startIndex: cellStartIndex, endIndex: cellEndIndex },
              textStyle: {
                bold: BRAND.TABLE.headerBold,
                weightedFontFamily: { fontFamily: BRAND.TABLE.headerFontFamily },
                fontSize: this.makeDimension(BRAND.BODY.fontSizePt),
                foregroundColor: {
                  color: { rgbColor: hexToRgb(BRAND.TABLE.headerTextColor) }
                }
              },
              fields: 'bold,weightedFontFamily,fontSize,foregroundColor'
            }
          });
        }
      }
    }

    // Apply borders to all cells (0.5pt black grid)
    const borderStyle = {
      color: { color: { rgbColor: hexToRgb(BRAND.TABLE.borderColor) } },
      width: this.makeDimension(BRAND.TABLE.borderWidth),
      dashStyle: 'SOLID'
    };

    tableRequests.push({
      updateTableCellStyle: {
        tableRange: {
          tableCellLocation: {
            tableStartLocation: { index: startIndex },
            rowIndex: 0,
            columnIndex: 0
          },
          rowSpan: rows,
          columnSpan: cols
        },
        tableCellStyle: {
          borderTop: borderStyle,
          borderBottom: borderStyle,
          borderLeft: borderStyle,
          borderRight: borderStyle,
          paddingTop: this.makeDimension(BRAND.TABLE.cellPaddingPt),
          paddingBottom: this.makeDimension(BRAND.TABLE.cellPaddingPt),
          paddingLeft: this.makeDimension(BRAND.TABLE.cellPaddingPt),
          paddingRight: this.makeDimension(BRAND.TABLE.cellPaddingPt)
        },
        fields: 'borderTop,borderBottom,borderLeft,borderRight,paddingTop,paddingBottom,paddingLeft,paddingRight'
      }
    });

    // Style header row with dark blue background
    if (rows > 0) {
      tableRequests.push({
        updateTableCellStyle: {
          tableRange: {
            tableCellLocation: {
              tableStartLocation: { index: startIndex },
              rowIndex: 0,
              columnIndex: 0
            },
            rowSpan: 1,
            columnSpan: cols
          },
          tableCellStyle: {
            backgroundColor: {
              color: { rgbColor: hexToRgb(BRAND.TABLE.headerBackgroundColor) }
            }
          },
          fields: 'backgroundColor'
        }
      });
    }

    return tableRequests;
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
        // Tables are handled separately in publish() method
        // This case should not be reached
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

      // Reduce spacing between list items (30% less than default)
      this.requests.push({
        updateParagraphStyle: {
          range: {
            startIndex: item.startIndex,
            endIndex: item.endIndex
          },
          paragraphStyle: {
            spaceAbove: this.makeDimension(0),
            spaceBelow: this.makeDimension(3),
            lineSpacing: 100 // 1.0 line spacing
          },
          fields: 'spaceAbove,spaceBelow,lineSpacing'
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

    // Apply code styling with monospace font
    this.requests.push({
      updateTextStyle: {
        range: { startIndex, endIndex: endIndex - 1 },
        textStyle: {
          weightedFontFamily: { fontFamily: BRAND.CODE.fontFamily },
          fontSize: this.makeDimension(BRAND.CODE.fontSizePt),
          foregroundColor: {
            color: { rgbColor: hexToRgb(BRAND.CODE.color) }
          },
          backgroundColor: {
            color: { rgbColor: hexToRgb(BRAND.CODE.backgroundColor) }
          }
        },
        fields: 'weightedFontFamily,fontSize,foregroundColor,backgroundColor'
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
   * Insert a table with proper Google Docs table structure and brand styling
   * This is stored for later processing since tables require a two-phase approach
   */
  insertTable(block) {
    const rows = block.rows.length;
    const cols = block.rows[0]?.length || 1;
    const tableStartIndex = this.cursorIndex;

    // Store table data for processing in a separate batch
    if (!this.pendingTables) {
      this.pendingTables = [];
    }

    this.pendingTables.push({
      block,
      startIndex: tableStartIndex,
      rows,
      cols
    });

    // Insert the table structure
    this.requests.push({
      insertTable: {
        rows,
        columns: cols,
        location: { index: tableStartIndex }
      }
    });

    // Calculate end index of table
    // Table structure: start + 1 (table start) + (rows * (1 row start + cols * 2)) + 1 (table end)
    const tableEndIndex = tableStartIndex + 2 + (rows * (1 + cols * 2));
    this.cursorIndex = tableEndIndex;
  }

  /**
   * Process pending tables after initial table structures are created
   * This must be called after the first batchUpdate completes
   */
  async processPendingTables() {
    if (!this.pendingTables || this.pendingTables.length === 0) {
      return;
    }

    // Read back the document to get actual table cell locations
    const doc = await this.docs.documents.get({ documentId: this.docId });

    const tableRequests = [];

    for (const tableData of this.pendingTables) {
      const { block, startIndex, rows, cols } = tableData;

      // Find the table in the document structure
      const table = this.findTableAtIndex(doc.data.body.content, startIndex);

      if (!table) {
        console.warn(`Could not find table at index ${startIndex}`);
        continue;
      }

      // Process cells in reverse order to avoid index shifting
      for (let rowIdx = rows - 1; rowIdx >= 0; rowIdx--) {
        const row = block.rows[rowIdx];
        const tableRow = table.table.tableRows[rowIdx];

        for (let colIdx = cols - 1; colIdx >= 0; colIdx--) {
          const cell = row[colIdx] || { runs: [{ text: '' }] };
          const tableCell = tableRow.tableCells[colIdx];

          // Get the actual start index of the cell's first paragraph
          // Each cell contains at least one paragraph with content
          const cellContent = tableCell.content[0]; // First element is the paragraph
          if (!cellContent || !cellContent.paragraph) {
            console.warn(`Cell at row ${rowIdx}, col ${colIdx} has no paragraph content`);
            continue;
          }

          // The paragraph element has a startIndex, but we need to insert INSIDE it
          // The paragraph's first content element (if it exists) tells us where to insert
          // For an empty paragraph, we insert right after the paragraph start
          const paragraph = cellContent.paragraph;
          let cellStartIndex;

          if (paragraph.elements && paragraph.elements.length > 0) {
            // Use the first element's start index
            cellStartIndex = paragraph.elements[0].startIndex;
          } else {
            // Empty paragraph - insert at start + 1
            cellStartIndex = cellContent.startIndex + 1;
          }

          const cellText = cell.runs.map(r => r.text).join('');
          console.log(`Cell [${rowIdx},${colIdx}]: cellStartIndex=${cellStartIndex}, paragraphStart=${cellContent.startIndex}, text="${cellText}"`);

          // Insert cell content
          if (cellText) {
            tableRequests.push({
              insertText: {
                location: { index: cellStartIndex },
                text: cellText
              }
            });

            // Apply inline formatting to each run within the cell
            let offset = 0;
            cell.runs.forEach(run => {
              if (run.text) {
                const runStart = cellStartIndex + offset;
                const runEnd = runStart + run.text.length;

                const textStyle = {};
                if (run.bold) textStyle.bold = true;
                if (run.italic) textStyle.italic = true;
                if (run.strikethrough) textStyle.strikethrough = true;
                if (run.code) {
                  textStyle.weightedFontFamily = { fontFamily: BRAND.CODE.fontFamily };
                  textStyle.fontSize = this.makeDimension(BRAND.CODE.fontSizePt);
                  textStyle.backgroundColor = {
                    color: { rgbColor: hexToRgb(BRAND.CODE.backgroundColor) }
                  };
                }

                // Apply text style if there's any formatting
                if (Object.keys(textStyle).length > 0) {
                  tableRequests.push({
                    updateTextStyle: {
                      range: { startIndex: runStart, endIndex: runEnd },
                      textStyle,
                      fields: Object.keys(textStyle).join(',')
                    }
                  });
                }

                // Apply links
                if (run.link) {
                  tableRequests.push({
                    updateTextStyle: {
                      range: { startIndex: runStart, endIndex: runEnd },
                      textStyle: {
                        link: { url: run.link },
                        foregroundColor: {
                          color: { rgbColor: hexToRgb('#4F81BD') }
                        },
                        underline: true
                      },
                      fields: 'link,foregroundColor,underline'
                    }
                  });
                }

                offset += run.text.length;
              }
            });
          }

          // Apply header row styling (first row)
          if (rowIdx === 0 && cellText) {
            const cellEndIndex = cellStartIndex + cellText.length;
            tableRequests.push({
              updateTextStyle: {
                range: { startIndex: cellStartIndex, endIndex: cellEndIndex },
                textStyle: {
                  bold: BRAND.TABLE.headerBold,
                  weightedFontFamily: { fontFamily: BRAND.TABLE.headerFontFamily },
                  fontSize: this.makeDimension(BRAND.BODY.fontSizePt)
                },
                fields: 'bold,weightedFontFamily,fontSize'
              }
            });
          }
        }
      }

      // Style header row with background color and borders
      if (rows > 0) {
        tableRequests.push({
          updateTableCellStyle: {
            tableRange: {
              tableCellLocation: {
                tableStartLocation: { index: startIndex },
                rowIndex: 0,
                columnIndex: 0
              },
              rowSpan: 1,
              columnSpan: cols
            },
            tableCellStyle: {
              backgroundColor: {
                color: { rgbColor: hexToRgb(BRAND.TABLE.headerBackgroundColor) }
              },
              borderBottom: {
                color: {
                  color: { rgbColor: hexToRgb(BRAND.TABLE.borderColor) }
                },
                width: this.makeDimension(1),
                dashStyle: 'SOLID'
              },
              paddingTop: this.makeDimension(BRAND.TABLE.cellPaddingPt),
              paddingBottom: this.makeDimension(BRAND.TABLE.cellPaddingPt),
              paddingLeft: this.makeDimension(BRAND.TABLE.cellPaddingPt),
              paddingRight: this.makeDimension(BRAND.TABLE.cellPaddingPt)
            },
            fields: 'backgroundColor,borderBottom,paddingTop,paddingBottom,paddingLeft,paddingRight'
          }
        });
      }
    }

    // Execute all table content requests in a second batch update
    if (tableRequests.length > 0) {
      await this.docs.documents.batchUpdate({
        documentId: this.docId,
        requestBody: { requests: tableRequests }
      });
    }

    // Clear pending tables
    this.pendingTables = [];
  }

  /**
   * Find a table in the document content at a specific index
   */
  findTableAtIndex(content, targetIndex) {
    for (const element of content) {
      if (element.table && element.startIndex === targetIndex) {
        return element;
      }
    }
    return null;
  }

  /**
   * Find a table near a specific index (within ±10 positions)
   * Useful when index might have shifted due to content insertion
   */
  findTableNearIndex(content, targetIndex, tolerance = 10) {
    let closestTable = null;
    let closestDistance = Infinity;

    for (const element of content) {
      if (element.table) {
        const distance = Math.abs(element.startIndex - targetIndex);
        if (distance <= tolerance && distance < closestDistance) {
          closestTable = element;
          closestDistance = distance;
        }
      }
    }

    return closestTable;
  }

  /**
   * Insert a horizontal rule as a visual line
   * (Google Docs API doesn't support insertHorizontalRule or paragraph borders)
   */
  insertHorizontalRule() {
    const startIndex = this.cursorIndex;
    // Use a thin underline character repeated to create a line
    const lineChar = '_';
    const text = lineChar.repeat(80) + '\n';
    const endIndex = startIndex + text.length;

    this.requests.push({
      insertText: {
        location: { index: startIndex },
        text
      }
    });

    // Style the line - light gray, small font, centered
    this.requests.push({
      updateTextStyle: {
        range: { startIndex, endIndex: endIndex - 1 },
        textStyle: {
          foregroundColor: {
            color: { rgbColor: hexToRgb('#D3D3D3') }
          },
          fontSize: this.makeDimension(6)
        },
        fields: 'foregroundColor,fontSize'
      }
    });

    this.requests.push({
      updateParagraphStyle: {
        range: { startIndex, endIndex },
        paragraphStyle: {
          alignment: 'CENTER',
          spaceAbove: this.makeDimension(4),
          spaceBelow: this.makeDimension(4)
        },
        fields: 'alignment,spaceAbove,spaceBelow'
      }
    });

    this.cursorIndex = endIndex;
  }
}

export default DocsPublisher;
