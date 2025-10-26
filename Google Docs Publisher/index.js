#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { getAuth } = require('./googleAuth');
const { parseMarkdownToBlocks } = require('./markdownParser');
const DocsPublisher = require('./docsPublisher');

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
        const { execSync } = require('child_process');
        execSync(`echo "${result.url}" | pbcopy`);
        console.log('📋 URL copied to clipboard!\n');
      } catch (err) {
        // Clipboard copy failed, not critical
      }
    }

  } catch (error) {
    console.error('\n❌ Error:', error.message);

    if (error.stack && process.argv.includes('--debug')) {
      console.error('\nStack trace:');
      console.error(error.stack);
    }

    process.exit(1);
  }
}

// Run main function
if (require.main === module) {
  main();
}

module.exports = { main };
