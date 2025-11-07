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
    const markdown = fs.readFileSync(absolutePath, 'utf8');

    if (!markdown.trim()) {
      console.error('❌ Error: File is empty');
      process.exit(1);
    }

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
