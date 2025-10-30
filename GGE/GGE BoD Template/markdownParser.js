import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import { visit } from 'unist-util-visit';
import { toString } from 'mdast-util-to-string';

/**
 * Parse markdown text into structured blocks for Google Docs
 * @param {string} markdownText - The markdown content to parse
 * @returns {Array} Array of block objects ready for Docs API
 */
function parseMarkdownToBlocks(markdownText) {
  const tree = unified()
    .use(remarkParse)
    .use(remarkGfm) // Enable GitHub Flavored Markdown (tables, strikethrough, etc.)
    .parse(markdownText);

  const blocks = [];

  // Process top-level children
  tree.children.forEach(node => {
    const block = processNode(node);
    if (block) {
      blocks.push(block);
    }
  });

  return blocks;
}

/**
 * Process a single markdown AST node into a block
 */
function processNode(node) {
  switch (node.type) {
    case 'heading':
      return {
        type: 'heading',
        level: node.depth,
        runs: processInlineContent(node.children)
      };

    case 'paragraph':
      return {
        type: 'paragraph',
        runs: processInlineContent(node.children)
      };

    case 'list':
      return {
        type: 'list',
        ordered: node.ordered,
        start: node.start || 1,
        items: node.children.map(item => ({
          runs: processInlineContent(item.children.length > 0 && item.children[0].type === 'paragraph'
            ? item.children[0].children
            : item.children),
          // Handle nested lists (simplified for now - can expand)
          nested: item.children.slice(1).filter(child => child.type === 'list')
        }))
      };

    case 'code':
      return {
        type: 'codeblock',
        lang: node.lang || '',
        value: node.value
      };

    case 'blockquote':
      // Process blockquote children and flatten to paragraphs
      const quoteBlocks = node.children.map(child => processNode(child)).filter(Boolean);
      return {
        type: 'blockquote',
        blocks: quoteBlocks
      };

    case 'table':
      return {
        type: 'table',
        align: node.align || [],
        rows: node.children.map(row =>
          row.children.map(cell => ({
            runs: processInlineContent(cell.children)
          }))
        )
      };

    case 'thematicBreak':
      return {
        type: 'hr'
      };

    case 'html':
      // Skip raw HTML for now (could optionally preserve as code)
      return null;

    default:
      console.warn(`Unhandled block type: ${node.type}`);
      return null;
  }
}

/**
 * Process inline content (text, bold, italic, links, etc.) into runs
 * @param {Array} children - Array of inline nodes
 * @returns {Array} Array of run objects with text and formatting
 */
function processInlineContent(children) {
  const runs = [];

  children.forEach(node => {
    const nodeRuns = processInlineNode(node);
    runs.push(...nodeRuns);
  });

  return runs;
}

/**
 * Process a single inline node into one or more runs
 */
function processInlineNode(node, inheritedStyle = {}) {
  switch (node.type) {
    case 'text':
      return [{
        text: node.value,
        ...inheritedStyle
      }];

    case 'strong':
      return processInlineContent(node.children).map(run => ({
        ...run,
        bold: true
      }));

    case 'emphasis':
      return processInlineContent(node.children).map(run => ({
        ...run,
        italic: true
      }));

    case 'delete':
      return processInlineContent(node.children).map(run => ({
        ...run,
        strikethrough: true
      }));

    case 'inlineCode':
      return [{
        text: node.value,
        code: true,
        ...inheritedStyle
      }];

    case 'link':
      return processInlineContent(node.children).map(run => ({
        ...run,
        link: node.url
      }));

    case 'break':
      return [{
        text: '\n',
        ...inheritedStyle
      }];

    case 'image':
      // Google Docs API can insert images, but it's complex
      // For now, we'll insert the alt text as a placeholder
      return [{
        text: `[Image: ${node.alt || node.url}]`,
        italic: true,
        ...inheritedStyle
      }];

    default:
      // Fallback: try to extract text content
      const text = toString(node);
      if (text) {
        return [{
          text: text,
          ...inheritedStyle
        }];
      }
      return [];
  }
}

/**
 * Merge consecutive runs with identical formatting
 * This reduces API request count
 */
function optimizeRuns(runs) {
  if (runs.length <= 1) return runs;

  const optimized = [runs[0]];

  for (let i = 1; i < runs.length; i++) {
    const prev = optimized[optimized.length - 1];
    const curr = runs[i];

    // Check if formatting is identical
    if (
      prev.bold === curr.bold &&
      prev.italic === curr.italic &&
      prev.strikethrough === curr.strikethrough &&
      prev.code === curr.code &&
      prev.link === curr.link
    ) {
      // Merge text
      prev.text += curr.text;
    } else {
      optimized.push(curr);
    }
  }

  return optimized;
}

export {
  parseMarkdownToBlocks,
  optimizeRuns
};
