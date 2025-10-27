#!/bin/bash

# Debug script to see what path we're getting

echo "Received argument: $1" > /tmp/obsidian-debug.log
echo "Working directory: $(pwd)" >> /tmp/obsidian-debug.log
echo "Script location: $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" >> /tmp/obsidian-debug.log

cat /tmp/obsidian-debug.log
