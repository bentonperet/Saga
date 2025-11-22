#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';
import { getAuth } from './googleAuth.js';
import { parseMarkdownToBlocks } from './markdownParser.js';
import DocsPublisher from './docsPublisher.js';

// ES module equivalent of __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Log file path
const LOG_FILE = path.join(__dirname, 'export-errors.log');

/**
 * Write error to log file with timestamp
 */
function logError(error, context = {}) {
  const timestamp = new Date().toISOString();
  const logEntry = {
    timestamp,
    error: {
      message: error.message,
      stack: error.stack,
      code: error.code,
      ...error
    },
    context
  };

  const logLine = `
${'='.repeat(80)}
[${timestamp}] ERROR
${'='.repeat(80)}
Context: ${JSON.stringify(context, null, 2)}

Error Message: ${error.message}

${error.stack || 'No stack trace available'}

${error.errors ? 'API Errors:\n' + JSON.stringify(error.errors, null, 2) : ''}
${'='.repeat(80)}

`;

  try {
    fs.appendFileSync(LOG_FILE, logLine);
    console.log(`\n📝 Error logged to: ${LOG_FILE}`);
  } catch (logErr) {
    console.error('⚠️  Failed to write to error log:', logErr.message);
  }
}

/**
 * Clean up extra newlines/carriage returns from markdown
 * @param {string} markdown - Raw markdown content
 * @returns {string} Cleaned markdown
 */
function cleanExtraNewlines(markdown) {
  return markdown
    // Normalize line endings (CRLF -> LF)
    .replace(/\r\n/g, '\n')
    // Remove standalone carriage returns
    .replace(/\r/g, '\n')
    // Replace 3+ consecutive newlines with 2 newlines (preserve paragraph breaks)
    .replace(/\n{3,}/g, '\n\n')
    // Remove trailing whitespace from lines
    .replace(/[ \t]+$/gm, '')
    // Ensure file ends with single newline
    .replace(/\n*$/, '\n');
}

/**
 * Fix numbered list continuations - restart numbering at 1 when interrupted by non-list text
 * @param {string} markdown - Markdown content
 * @returns {string} Markdown with corrected list numbering
 */
function fixListNumbering(markdown) {
  const lines = markdown.split('\n');
  const result = [];
  let inNumberedList = false;
  let expectedNumber = 1;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmedLine = line.trim();

    // Check if this is a numbered list item (starts with digit(s) followed by period and space)
    const numberedListMatch = trimmedLine.match(/^(\d+)\.\s+(.+)$/);

    if (numberedListMatch) {
      const actualNumber = parseInt(numberedListMatch[1]);
      const content = numberedListMatch[2];

      // If we're starting a new list (not in a list or number jumped), reset to 1
      if (!inNumberedList || actualNumber > expectedNumber + 1) {
        result.push(line.replace(/^\s*\d+\./, line.match(/^\s*/)[0] + '1.'));
        expectedNumber = 2;
        inNumberedList = true;
      } else {
        // Continue the list with expected number
        result.push(line.replace(/^\s*\d+\./, line.match(/^\s*/)[0] + expectedNumber + '.'));
        expectedNumber++;
      }
    } else {
      // Not a numbered list item
      // If line is not empty and not blank, we've left the list
      if (trimmedLine.length > 0) {
        inNumberedList = false;
        expectedNumber = 1;
      }
      result.push(line);
    }
  }

  return result.join('\n');
}

/**
 * Format colon-prefixed text as medium weight
 * Detects patterns like "Label:" at start of lines or list items and wraps them for medium formatting
 * Only affects plain text (not already bold/italic/etc)
 * @param {string} markdown - Markdown content
 * @returns {string} Markdown with colon labels marked for medium weight
 */
function formatColonLabels(markdown) {
  const lines = markdown.split('\n');
  const result = [];

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // Pattern 1: Line starts with text ending in colon (e.g., "Company Structure:")
    // Pattern 2: Bulleted list item with label: (e.g., "- Label: text")
    // Pattern 3: Numbered list item with label: (e.g., "1. Label: text")

    // Match: optional whitespace, optional bullet/number, then text with colon, then more text
    // Don't match if the label is already formatted (contains **, *, __, _, etc.)
    const match = line.match(/^(\s*(?:[-*+]|\d+\.)\s+)?([^*_`[\]]+?):\s+(.+)$/);

    if (match) {
      const prefix = match[1] || ''; // bullet/number or empty
      const label = match[2]; // text before colon
      const rest = match[3]; // text after colon

      // Check if label contains any markdown formatting
      const hasFormatting = /[*_`[\]]/.test(label);

      if (!hasFormatting) {
        // Wrap the label (including colon) with special marker {{MEDIUM}}
        line = `${prefix}{{MEDIUM}}${label}:{{/MEDIUM}} ${rest}`;
      }
    }

    result.push(line);
  }

  return result.join('\n');
}

/**
 * Main function to publish markdown to Google Docs
 */
async function main() {
  try {
    // Get markdown file path from command line
    const mdPath = process.argv[2];

    if (!mdPath) {
      console.error('❌ Error: No file path provided\n');
      console.log('Usage: node index.js <path-to-markdown-file.md>');
      console.log('Example: node index.js "../Client Brief - Saga Pryor.md"');
      process.exit(1);
    }

    // Resolve absolute path
    const absolutePath = path.resolve(mdPath);

    // Check if file exists
    if (!fs.existsSync(absolutePath)) {
      console.error(`❌ Error: File not found: ${absolutePath}`);
      process.exit(1);
    }

    // Read markdown content
    console.log('📄 Reading markdown file...');
    let markdown = fs.readFileSync(absolutePath, 'utf8');

    if (!markdown.trim()) {
      console.error('❌ Error: File is empty');
      process.exit(1);
    }

    // Clean up extra newlines and whitespace
    console.log('🧹 Cleaning extra newlines...');
    markdown = cleanExtraNewlines(markdown);

    // Fix numbered list numbering
    console.log('🔢 Fixing list numbering...');
    markdown = fixListNumbering(markdown);

    // Format colon labels as medium weight
    console.log('🏷️  Formatting colon labels...');
    markdown = formatColonLabels(markdown);

    // Parse markdown into structured blocks
    console.log('🔍 Parsing markdown...');
    const blocks = parseMarkdownToBlocks(markdown);
    console.log(`   Found ${blocks.length} blocks`);

    // Authenticate with Google
    console.log('🔐 Authenticating with Google...');
    const auth = await getAuth();

    // Create publisher and publish
    console.log('📝 Creating Google Doc...');
    const publisher = new DocsPublisher(auth);

    const docTitle = path.basename(absolutePath, '.md');
    const result = await publisher.publish(docTitle, blocks);

    // Success!
    console.log('\n✅ Document published successfully!\n');
    console.log(`   Title: ${result.title}`);
    console.log(`   URL:   ${result.url}\n`);

    // Optional: append URL to markdown file
    const appendUrl = process.argv.includes('--append-url');
    if (appendUrl) {
      const urlLine = `\n\n---\n**Published to Google Docs:** ${result.url}\n`;
      fs.appendFileSync(absolutePath, urlLine);
      console.log('✓ URL appended to markdown file\n');
    }

    // Copy URL to clipboard (macOS only)
    if (process.platform === 'darwin' && !process.argv.includes('--no-clipboard')) {
      try {
        execSync(`echo "${result.url}" | pbcopy`);
        console.log('📋 URL copied to clipboard!\n');
      } catch (err) {
        // Clipboard copy failed, not critical
      }
    }

  } catch (error) {
    console.error('\n❌ Error:', error.message);

    // Log error to file
    logError(error, {
      file: process.argv[2],
      timestamp: new Date().toISOString(),
      args: process.argv.slice(2)
    });

    if (error.stack && process.argv.includes('--debug')) {
      console.error('\nStack trace:');
      console.error(error.stack);
    }

    console.log('\n💡 Tip: Check export-errors.log for full error details');

    process.exit(1);
  }
}

// Run main function
main();

export { main };
