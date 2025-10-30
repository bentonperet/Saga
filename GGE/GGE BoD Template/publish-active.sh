#!/bin/bash

# This script publishes the currently active file in Obsidian
# Windows/Git Bash compatible version for GGE BoD Template directory

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if file path was provided as argument
if [ -n "$1" ]; then
    FILE_PATH="$1"
    echo "Using provided file path: $FILE_PATH"
else
    # Fall back to finding the most recently modified .md file in current directory
    echo "No file path provided, finding most recently modified file in current directory..."
    FILE_PATH=$(find "$SCRIPT_DIR" -maxdepth 1 -name "*.md" -type f -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)
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

# Run the publisher (using node from PATH)
node "$SCRIPT_DIR/index.js" "$FILE_PATH"
