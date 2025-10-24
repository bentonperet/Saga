#!/usr/bin/env python3
"""
Generate commands to update Notion database
This script creates a JSON file with all the necessary Notion API operations
"""

import csv
import json
from datetime import datetime

DATABASE_ID = "28d776f6-a4e0-8014-8f3f-fdde8020d043"
csv_file = "/Users/bentonperet/Documents/Benton's Brain/1 Projects/Saga Pryor DC/_Project Management/Actions/Consolidated Action Items - FINAL-FIXED.csv"

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
            with open(csv_file, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    actions.append(row)
            return actions
        except UnicodeDecodeError:
            continue
    raise Exception("Could not read CSV with any known encoding")

def create_page_payload(row):
    """Create payload for Notion create page API"""
    properties = {
        "Name": {
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Name']
                    }
                }
            ]
        },
        "Action Description": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Action Description']
                    }
                }
            ]
        },
        "Notes_Comments": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Notes_Comments']
                    }
                }
            ]
        },
        "Priority": {
            "select": {
                "name": row['Priority']
            }
        },
        "Assigned To": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Assigned To']
                    }
                }
            ]
        },
        "Status": {
            "select": {
                "name": row['Status']
            }
        },
        "Organization": {
            "select": {
                "name": row['Organization']
            }
        },
        "Category": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Category']
                    }
                }
            ]
        },
        "Cost Impact": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Cost Impact']
                    }
                }
            ]
        },
        "Dependencies": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Dependencies']
                    }
                }
            ]
        },
        "Related Decision IDs": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Related Decision IDs']
                    }
                }
            ]
        },
        "Timeline Impact": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Timeline Impact']
                    }
                }
            ]
        }
    }

    due_date = parse_date(row['Due Date'])
    if due_date:
        properties["Due Date"] = {
            "date": {
                "start": due_date
            }
        }

    return {
        "parent": {"database_id": DATABASE_ID},
        "properties": properties
    }

if __name__ == "__main__":
    actions = read_csv_actions()
    print(f"Read {len(actions)} actions from CSV")

    # Generate create page payloads
    create_commands = []
    for action in actions:
        payload = create_page_payload(action)
        create_commands.append({
            "action": "create_page",
            "payload": payload
        })

    # Save to file
    output_file = "/Users/bentonperet/Documents/Benton's Brain/1 Projects/Saga Pryor DC/_Project Management/Actions/notion_commands.json"
    with open(output_file, 'w') as f:
        json.dump(create_commands, f, indent=2)

    print(f"\nGenerated {len(create_commands)} commands")
    print(f"Saved to: {output_file}")
