#!/usr/bin/env python3
"""
Script to update PGCIS Action list in Notion
Clears existing entries and populates from CSV file
"""

import csv
import json
from datetime import datetime

# Database ID
DATABASE_ID = "28d776f6-a4e0-8014-8f3f-fdde8020d043"

# Read CSV file
csv_file = "/Users/bentonperet/Documents/Benton's Brain/1 Projects/Saga Pryor DC/_Project Management/Actions/Consolidated Action Items - FINAL-FIXED.csv"

def parse_date(date_str):
    """Convert date string like '18-Oct-25' to ISO format '2025-10-18'"""
    if not date_str or date_str == 'TBD' or date_str == 'ASAP':
        return None
    try:
        # Parse dates like "18-Oct-25"
        dt = datetime.strptime(date_str, "%d-%b-%y")
        return dt.strftime("%Y-%m-%d")
    except:
        return None

def read_csv_actions():
    """Read and parse CSV file"""
    actions = []
    # Try different encodings
    encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(csv_file, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    actions.append(row)
            print(f"Successfully read CSV with {encoding} encoding")
            return actions
        except UnicodeDecodeError:
            continue
    raise Exception("Could not read CSV with any known encoding")
    return actions

def create_notion_properties(row):
    """Convert CSV row to Notion properties format"""
    due_date = parse_date(row['Due Date'])

    properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": row['Name']
                    }
                }
            ]
        },
        "Action Description": {
            "rich_text": [
                {
                    "text": {
                        "content": row['Action Description']
                    }
                }
            ]
        },
        "Notes_Comments": {
            "rich_text": [
                {
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
                    "text": {
                        "content": row['Category']
                    }
                }
            ]
        },
        "Cost Impact": {
            "rich_text": [
                {
                    "text": {
                        "content": row['Cost Impact']
                    }
                }
            ]
        },
        "Dependencies": {
            "rich_text": [
                {
                    "text": {
                        "content": row['Dependencies']
                    }
                }
            ]
        },
        "Related Decision IDs": {
            "rich_text": [
                {
                    "text": {
                        "content": row['Related Decision IDs']
                    }
                }
            ]
        },
        "Timeline Impact": {
            "rich_text": [
                {
                    "text": {
                        "content": row['Timeline Impact']
                    }
                }
            ]
        }
    }

    # Add due date if present
    if due_date:
        properties["Due Date"] = {
            "date": {
                "start": due_date
            }
        }

    return properties

if __name__ == "__main__":
    actions = read_csv_actions()
    print(f"Read {len(actions)} actions from CSV")

    # Print first action as example
    if actions:
        print("\nExample action:")
        print(json.dumps(create_notion_properties(actions[0]), indent=2))
