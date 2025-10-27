#!/bin/bash

# Wrapper script for Obsidian Shell Commands
# This handles file path variables more reliably

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
FILE_PATH="$1"

# If no file path provided, show error
if [ -z "$FILE_PATH" ]; then
    echo "Error: No file path provided"
    echo "Usage: publish.sh <path-to-markdown-file>"
    exit 1
fi

# Clean up escaped characters from Obsidian
# Use tr to delete all backslashes
FILE_PATH=$(echo "$FILE_PATH" | tr -d '\\')

# Run the publisher
/usr/local/bin/node "$SCRIPT_DIR/index.js" "$FILE_PATH"
