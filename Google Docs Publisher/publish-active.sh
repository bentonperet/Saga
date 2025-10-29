#!/bin/bash

# This script publishes the currently active file in Obsidian
# It accepts the file path as the first argument, or falls back to finding
# the most recently modified markdown file if no argument is provided

VAULT_DIR="/Users/bentonperet/benperet@gmail.com - Google Drive/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if file path was provided as argument
if [ -n "$1" ]; then
    FILE_PATH="$1"
    echo "Using provided file path: $FILE_PATH"
else
    # Fall back to finding the most recently modified .md file
    echo "No file path provided, finding most recently modified file..."
    FILE_PATH=$(find "$VAULT_DIR" -name "*.md" -not -path "*/Google Docs Publisher/*" -not -path "*/.obsidian/*" -type f -exec stat -f "%m %N" {} \; | sort -rn | head -1 | cut -d' ' -f2-)
fi

if [ -z "$FILE_PATH" ]; then
    echo "Error: Could not find any markdown file"
    exit 1
fi

# Verify the file exists
if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File does not exist: $FILE_PATH"
    exit 1
fi

echo "Publishing: $FILE_PATH"

# Run the publisher
/usr/local/bin/node "$SCRIPT_DIR/index.js" "$FILE_PATH"
