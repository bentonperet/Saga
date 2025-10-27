#!/bin/bash

# This script publishes the currently active file in Obsidian
# It works by looking at the most recently modified markdown file

VAULT_DIR="/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Find the most recently modified .md file (excluding this directory)
FILE_PATH=$(find "$VAULT_DIR" -name "*.md" -not -path "*/Google Docs Publisher/*" -not -path "*/.obsidian/*" -type f -exec stat -f "%m %N" {} \; | sort -rn | head -1 | cut -d' ' -f2-)

if [ -z "$FILE_PATH" ]; then
    echo "Error: Could not find any markdown file"
    exit 1
fi

echo "Publishing: $FILE_PATH"

# Run the publisher
/usr/local/bin/node "$SCRIPT_DIR/index.js" "$FILE_PATH"
