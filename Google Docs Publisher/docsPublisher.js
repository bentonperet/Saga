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
    this.bookmarkNames = {}; // Track bookmark names for headings
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
   * Set document margins
   */
  async setDocumentMargins() {
    await this.docs.documents.batchUpdate({
      documentId: this.docId,
      requestBody: {
        requests: [{
          updateDocumentStyle: {
            documentStyle: {
              marginTop: this.makeDimension(BRAND.PAGE.marginTop),
              marginBottom: this.makeDimension(BRAND.PAGE.marginBottom),
              marginLeft: this.makeDimension(BRAND.PAGE.marginLeft),
              marginRight: this.makeDimension(BRAND.PAGE.marginRight),
              marginHeader: this.makeDimension(BRAND.PAGE.marginHeader),
              marginFooter: this.makeDimension(BRAND.PAGE.marginFooter)
            },
            fields: 'marginTop,marginBottom,marginLeft,marginRight,marginHeader,marginFooter'
          }
        }]
      }
    });
  }

  /**
   * Generate a URL-friendly bookmark name from heading text
   */
  generateBookmarkName(text) {
    // Convert to lowercase, replace spaces with hyphens, remove special chars
    let name = text
      .toLowerCase()
      .trim()
      .replace(/[^\w\s-]/g, '') // Remove special characters
      .replace(/\s+/g, '-')     // Replace spaces with hyphens
      .replace(/-+/g, '-')      // Replace multiple hyphens with single hyphen
      .replace(/^-|-$/g, '');   // Remove leading/trailing hyphens

    // If name is empty after cleaning, generate a default name
    if (!name || name.length === 0) {
      name = `heading-${Object.keys(this.bookmarkNames).length + 1}`;
    }

    // Ensure uniqueness
    let uniqueName = name;
    let counter = 1;
    while (this.bookmarkNames[uniqueName]) {
      uniqueName = `${name}-${counter}`;
      counter++;
    }

    this.bookmarkNames[uniqueName] = true;
    return uniqueName;
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

    // Set document margins first
    await this.setDocumentMargins();

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

        try {
          await this.insertAndPopulateTable(block, insertIndex);

          // Read back document to find where cursor should be after table
          const doc = await this.docs.documents.get({ documentId: this.docId });
          const table = this.findTableNearIndex(doc.data.body.content, insertIndex, 50);
          if (table) {
            this.cursorIndex = table.endIndex;
          } else {
            console.warn(`⚠️  Could not find table near index ${insertIndex}`);
            const rows = block.rows.length;
            const cols = block.rows[0]?.length || 1;
            this.cursorIndex = insertIndex + 3 + (rows * (cols * 2 + 1));
          }
        } catch (error) {
          console.error(`❌ Failed to insert table:`, error.message);
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

    // Find the table
    let table = this.findTableAtIndex(doc.data.body.content, insertIndex);

    if (!table) {
      table = this.findTableNearIndex(doc.data.body.content, insertIndex, 50);
    }

    if (!table) {
      throw new Error(`Could not find table near index ${insertIndex}`);
    }

    const tableRequests = this.buildTableContentRequests(block, table, rows, cols);

    if (tableRequests.length > 0) {
      await this.docs.documents.batchUpdate({
        documentId: this.docId,
        requestBody: { requests: tableRequests }
      });
    }

    // Pin header row if configured
    if (BRAND.TABLE.pinHeaderRow && rows > 0) {
      await this.docs.documents.batchUpdate({
        documentId: this.docId,
        requestBody: {
          requests: [{
            pinTableHeaderRows: {
              tableStartLocation: { index: table.startIndex },
              pinnedHeaderRowsCount: 1
            }
          }]
        }
      });
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
          continue;
        }

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
              const fields = [];

              if (run.bold) {
                // Check if this is medium weight text (colon labels)
                if (run.medium) {
                  // Use Medium (500) for colon-prefixed labels
                  textStyle.weightedFontFamily = { fontFamily: 'Poppins', weight: 500 };
                } else {
                  // Use Semi-Bold (600) for regular bold text
                  textStyle.weightedFontFamily = { fontFamily: 'Poppins', weight: 600 };
                }
                fields.push('weightedFontFamily');
              }
              if (run.italic) {
                textStyle.italic = true;
                fields.push('italic');
              }
              if (run.strikethrough) {
                textStyle.strikethrough = true;
                fields.push('strikethrough');
              }
              if (run.code) {
                textStyle.weightedFontFamily = { fontFamily: BRAND.CODE.fontFamily, weight: BRAND.CODE.fontWeight };
                textStyle.fontSize = this.makeDimension(BRAND.CODE.fontSizePt);
                textStyle.backgroundColor = {
                  color: { rgbColor: hexToRgb(BRAND.CODE.backgroundColor) }
                };
                fields.push('weightedFontFamily', 'fontSize', 'backgroundColor');
              }

              if (fields.length > 0) {
                tableRequests.push({
                  updateTextStyle: {
                    range: { startIndex: runStart, endIndex: runEnd },
                    textStyle,
                    fields: fields.join(',')
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

          // Apply cell-level styling
          const cellEndIndex = cellStartIndex + cellText.length;

          // Set font, size, and spacing for all cells
          tableRequests.push({
            updateTextStyle: {
              range: { startIndex: cellStartIndex, endIndex: cellEndIndex },
              textStyle: {
                weightedFontFamily: {
                  fontFamily: BRAND.TABLE.cellFontFamily,
                  weight: BRAND.TABLE.cellFontWeight
                },
                fontSize: this.makeDimension(BRAND.TABLE.cellFontSizePt),
                foregroundColor: {
                  color: { rgbColor: hexToRgb(BRAND.TABLE.cellTextColor) }
                }
              },
              fields: 'weightedFontFamily,fontSize,foregroundColor'
            }
          });

          tableRequests.push({
            updateParagraphStyle: {
              range: { startIndex: cellStartIndex, endIndex: cellEndIndex },
              paragraphStyle: {
                lineSpacing: BRAND.TABLE.cellLineSpacing * 100,
                spaceAbove: this.makeDimension(BRAND.TABLE.cellBeforeSpacingPt),
                spaceBelow: this.makeDimension(BRAND.TABLE.cellAfterSpacingPt)
              },
              fields: 'lineSpacing,spaceAbove,spaceBelow'
            }
          });

          // Apply header row styling (white text on dark blue background)
          if (rowIdx === 0) {
            tableRequests.push({
              updateTextStyle: {
                range: { startIndex: cellStartIndex, endIndex: cellEndIndex },
                textStyle: {
                  weightedFontFamily: {
                    fontFamily: BRAND.TABLE.headerFontFamily,
                    weight: BRAND.TABLE.headerFontWeight
                  },
                  fontSize: this.makeDimension(BRAND.TABLE.headerFontSizePt),
                  foregroundColor: {
                    color: { rgbColor: hexToRgb(BRAND.TABLE.headerTextColor) }
                  }
                },
                fields: 'weightedFontFamily,fontSize,foregroundColor'
              }
            });
          }
        }
      }
    }

    // Apply borders to all cells
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
      case 'hr':
        this.insertHorizontalRule();
        break;
      default:
        console.warn(`Unknown block type: ${block.type}`);
    }
  }

  /**
   * Insert a heading with brand styling and create a bookmark
   */
  insertHeading(block) {
    const brandStyle = getBrandStyleForHeading(block.level);
    const namedStyle = getNamedStyleForHeading(block.level);

    const startIndex = this.cursorIndex;
    const headingText = block.runs.map(r => r.text).join('').trim();

    this.insertStyledParagraph(
      block.runs,
      namedStyle,
      brandStyle
    );

    // Create bookmark for this heading only if it has text
    if (headingText && headingText.length > 0) {
      const bookmarkName = this.generateBookmarkName(headingText);
      const endIndex = this.cursorIndex - 1; // Exclude trailing newline

      // Only create bookmark if we have a valid name (max 256 chars for Google Docs API)
      if (bookmarkName && bookmarkName.length > 0 && bookmarkName.length <= 256) {
        this.requests.push({
          createNamedRange: {
            name: bookmarkName,
            range: {
              startIndex,
              endIndex
            }
          }
        });
      }
    }
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

    // Check if this is a heading (named style starts with HEADING_)
    const isHeading = namedStyle && namedStyle.startsWith('HEADING_');

    // 1. Insert text
    this.requests.push({
      insertText: {
        location: { index: startIndex },
        text: fullText
      }
    });

    // 2. Apply paragraph-level named style and spacing
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

    // 3. For headings: apply brand styling (font, size, color, weight) to override named style
    //    For body text: apply brand styling normally
    let offset = 0;
    runs.forEach(run => {
      const runStart = startIndex + offset;
      const runEnd = runStart + run.text.length;

      const textStyle = {
        weightedFontFamily: {
          fontFamily: brandStyle.fontFamily,
          weight: brandStyle.fontWeight
        },
        fontSize: this.makeDimension(brandStyle.fontSizePt),
        foregroundColor: {
          color: { rgbColor: hexToRgb(brandStyle.color) }
        }
      };

      const fields = ['weightedFontFamily', 'fontSize', 'foregroundColor'];

      // Handle underline (explicit true or false)
      if (brandStyle.underline === true) {
        textStyle.underline = true;
        fields.push('underline');
      } else if (brandStyle.underline === false) {
        textStyle.underline = false;
        fields.push('underline');
      }

      this.requests.push({
        updateTextStyle: {
          range: { startIndex: runStart, endIndex: runEnd },
          textStyle,
          fields: fields.join(',')
        }
      });

      offset += run.text.length;
    });

    // 4. Apply inline formatting to each run (bold, italic, links, etc.)
    offset = 0;
    runs.forEach(run => {
      const runStart = startIndex + offset;
      const runEnd = runStart + run.text.length;

      const textStyle = {};
      const fields = [];

      // Inline formatting
      if (run.bold) {
        // Check if this is medium weight text (colon labels)
        if (run.medium) {
          // Use Medium (500) for colon-prefixed labels
          textStyle.weightedFontFamily = {
            fontFamily: brandStyle.fontFamily,
            weight: 500
          };
        } else {
          // Use Semi-Bold (600) for regular bold text
          textStyle.weightedFontFamily = {
            fontFamily: brandStyle.fontFamily,
            weight: 600
          };
        }
        fields.push('weightedFontFamily');
      }

      if (run.italic) {
        textStyle.italic = true;
        fields.push('italic');
      }

      if (run.strikethrough) {
        textStyle.strikethrough = true;
        fields.push('strikethrough');
      }

      // Code styling
      if (run.code) {
        textStyle.weightedFontFamily = { fontFamily: BRAND.CODE.fontFamily, weight: BRAND.CODE.fontWeight };
        textStyle.fontSize = this.makeDimension(BRAND.CODE.fontSizePt);
        textStyle.backgroundColor = {
          color: { rgbColor: hexToRgb(BRAND.CODE.backgroundColor) }
        };
        fields.push('weightedFontFamily', 'fontSize', 'backgroundColor');
      }

      // Links
      if (run.link) {
        // Check if it's an internal anchor link
        if (run.link.startsWith('#')) {
          const anchor = run.link.substring(1);
          const bookmarkName = this.generateBookmarkName(anchor);
          textStyle.link = { bookmarkId: bookmarkName };
        } else {
          textStyle.link = { url: run.link };
        }
        textStyle.underline = true;
        textStyle.foregroundColor = {
          color: { rgbColor: hexToRgb('#0066CC') }
        };
        fields.push('link', 'underline', 'foregroundColor');
      }

      if (fields.length > 0) {
        this.requests.push({
          updateTextStyle: {
            range: { startIndex: runStart, endIndex: runEnd },
            textStyle,
            fields: fields.join(',')
          }
        });
      }

      offset += run.text.length;
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
        const fields = [];

        if (run.bold) {
          // Check if this is medium weight text (colon labels)
          if (run.medium) {
            // Use Medium (500) for colon-prefixed labels
            textStyle.weightedFontFamily = { fontFamily: 'Poppins', weight: 500 };
          } else {
            // Use Semi-Bold (600) for regular bold text
            textStyle.weightedFontFamily = { fontFamily: 'Poppins', weight: 600 };
          }
          fields.push('weightedFontFamily');
        }
        if (run.italic) {
          textStyle.italic = true;
          fields.push('italic');
        }
        if (run.link) {
          textStyle.link = { url: run.link };
          textStyle.underline = true;
          fields.push('link', 'underline');
        }

        if (fields.length > 0) {
          this.requests.push({
            updateTextStyle: {
              range: { startIndex: runStart, endIndex: runEnd },
              textStyle,
              fields: fields.join(',')
            }
          });
        }

        offset += run.text.length;
      });

      // Apply list styling (font, size, color, weight)
      this.requests.push({
        updateTextStyle: {
          range: { startIndex: itemStartIndex, endIndex: itemEndIndex - 1 },
          textStyle: {
            weightedFontFamily: {
              fontFamily: BRAND.LIST.fontFamily,
              weight: BRAND.LIST.fontWeight
            },
            fontSize: this.makeDimension(BRAND.LIST.fontSizePt),
            foregroundColor: {
              color: { rgbColor: hexToRgb(BRAND.LIST.color) }
            }
          },
          fields: 'weightedFontFamily,fontSize,foregroundColor'
        }
      });

      listItems.push({
        startIndex: itemStartIndex,
        endIndex: itemEndIndex
      });

      this.cursorIndex = itemEndIndex;
    });

    // Apply formatting to all items
    listItems.forEach(item => {
      // Apply spacing
      this.requests.push({
        updateParagraphStyle: {
          range: {
            startIndex: item.startIndex,
            endIndex: item.endIndex
          },
          paragraphStyle: {
            lineSpacing: BRAND.LIST.lineSpacing * 100,
            spaceAbove: this.makeDimension(BRAND.LIST.beforeSpacingPt),
            spaceBelow: this.makeDimension(BRAND.LIST.afterSpacingPt)
          },
          fields: 'lineSpacing,spaceAbove,spaceBelow'
        }
      });

      // Create bullets - each list gets its own auto-generated ID
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

    // Apply code styling with monospace font
    this.requests.push({
      updateTextStyle: {
        range: { startIndex, endIndex: endIndex - 1 },
        textStyle: {
          weightedFontFamily: {
            fontFamily: BRAND.CODE.fontFamily,
            weight: BRAND.CODE.fontWeight
          },
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

        // 2. Apply inline formatting
        let offset = 0;
        innerBlock.runs.forEach(run => {
          const runStart = startIndex + offset;
          const runEnd = runStart + run.text.length;

          const textStyle = {};
          const fields = [];

          if (run.bold) {
            // Check if this is medium weight text (colon labels)
            if (run.medium) {
              // Use Medium (500) for colon-prefixed labels
              textStyle.weightedFontFamily = { fontFamily: 'Poppins', weight: 500 };
            } else {
              // Use Semi-Bold (600) for regular bold text
              textStyle.weightedFontFamily = { fontFamily: 'Poppins', weight: 600 };
            }
            fields.push('weightedFontFamily');
          }
          if (run.italic) {
            textStyle.italic = true;
            fields.push('italic');
          }
          if (run.link) {
            textStyle.link = { url: run.link };
            textStyle.underline = true;
            fields.push('link', 'underline');
          }

          if (fields.length > 0) {
            this.requests.push({
              updateTextStyle: {
                range: { startIndex: runStart, endIndex: runEnd },
                textStyle,
                fields: fields.join(',')
              }
            });
          }

          offset += run.text.length;
        });

        // 3. Apply blockquote paragraph style
        this.requests.push({
          updateParagraphStyle: {
            range: { startIndex, endIndex },
            paragraphStyle: {
              lineSpacing: (BRAND.BLOCKQUOTE.lineSpacing || 1.15) * 100,
              spaceAbove: this.makeDimension(BRAND.BLOCKQUOTE.beforeSpacingPt),
              spaceBelow: this.makeDimension(BRAND.BLOCKQUOTE.afterSpacingPt),
              indentStart: this.makeDimension(BRAND.BLOCKQUOTE.indentStart)
            },
            fields: 'lineSpacing,spaceAbove,spaceBelow,indentStart'
          }
        });

        // 4. Apply blockquote text style
        this.requests.push({
          updateTextStyle: {
            range: { startIndex, endIndex: endIndex - 1 },
            textStyle: {
              weightedFontFamily: {
                fontFamily: BRAND.BLOCKQUOTE.fontFamily,
                weight: BRAND.BLOCKQUOTE.fontWeight
              },
              fontSize: this.makeDimension(BRAND.BLOCKQUOTE.fontSizePt),
              italic: true,
              foregroundColor: {
                color: { rgbColor: hexToRgb(BRAND.BLOCKQUOTE.color) }
              }
            },
            fields: 'weightedFontFamily,fontSize,italic,foregroundColor'
          }
        });

        this.cursorIndex = endIndex;
      } else {
        this.processBlock(innerBlock);
      }
    });
  }

  /**
   * Insert a horizontal rule
   */
  insertHorizontalRule() {
    const startIndex = this.cursorIndex;
    const lineChar = '_';
    const text = lineChar.repeat(80) + '\n';
    const endIndex = startIndex + text.length;

    this.requests.push({
      insertText: {
        location: { index: startIndex },
        text
      }
    });

    // Style the line
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
   * Find a table near a specific index (within ±tolerance positions)
   */
  findTableNearIndex(content, targetIndex, tolerance = 50) {
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
}

export default DocsPublisher;
