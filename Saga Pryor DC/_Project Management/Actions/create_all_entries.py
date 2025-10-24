#!/usr/bin/env python3
"""
Generate all the mcp__Notion__API-post-page calls needed
This will output the commands that Claude Code can execute
"""

import csv
import json
from datetime import datetime

DATABASE_ID = "28d776f6-a4e0-8014-8f3f-fdde8020d043"
CSV_FILE = "/Users/bentonperet/Documents/Benton's Brain/1 Projects/Saga Pryor DC/_Project Management/Actions/Consolidated Action Items - FINAL-FIXED.csv"

def parse_date(date_str):
    """Convert date string like '18-Oct-25' to ISO format '2025-10-18'"""
    if not date_str or date_str == 'TBD' or date_str == 'ASAP':
        return None
    try:
        dt = datetime.strptime(date_str, "%d-%b-%y")
        return dt.strftime("%Y-%m-%d")
    except:
        return None

def read_csv_actions():
    """Read and parse CSV file"""
    actions = []
    encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(CSV_FILE, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    actions.append(row)
            return actions
        except UnicodeDecodeError:
            continue
    raise Exception("Could not read CSV with any known encoding")

def escape_json_string(s):
    """Escape string for JSON"""
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def create_properties_json(row):
    """Create properties JSON for a row"""
    props = {}

    props["Name"] = {"title": [{"type": "text", "text": {"content": row['Name']}}]}
    props["Action Description"] = {"rich_text": [{"type": "text", "text": {"content": row['Action Description']}}]}
    props["Notes_Comments"] = {"rich_text": [{"type": "text", "text": {"content": row['Notes_Comments'][:2000]}}]}
    props["Priority"] = {"select": {"name": row['Priority']}}
    props["Assigned To"] = {"rich_text": [{"type": "text", "text": {"content": row['Assigned To']}}]}
    props["Status"] = {"select": {"name": row['Status']}}
    props["Organization"] = {"select": {"name": row['Organization']}}
    props["Category"] = {"rich_text": [{"type": "text", "text": {"content": row['Category']}}]}
    props["Cost Impact"] = {"rich_text": [{"type": "text", "text": {"content": row['Cost Impact']}}]}
    props["Dependencies"] = {"rich_text": [{"type": "text", "text": {"content": row['Dependencies']}}]}
    props["Related Decision IDs"] = {"rich_text": [{"type": "text", "text": {"content": row['Related Decision IDs']}}]}
    props["Timeline Impact"] = {"rich_text": [{"type": "text", "text": {"content": row['Timeline Impact']}}]}

    due_date = parse_date(row['Due Date'])
    if due_date:
        props["Due Date"] = {"date": {"start": due_date}}

    return props

if __name__ == "__main__":
    actions = read_csv_actions()
    print(f"Generating commands for {len(actions)} actions...\n")

    for i, action in enumerate(actions, 1):
        props = create_properties_json(action)
        parent = {"database_id": DATABASE_ID}

        print(f"# Action {i}/{len(actions)}: {action['Name']}")
        print(f"Parent: {json.dumps(parent)}")
        print(f"Properties: {json.dumps(props)}")
        print()
