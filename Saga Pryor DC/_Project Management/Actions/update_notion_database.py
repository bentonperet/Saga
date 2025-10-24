#!/usr/bin/env python3
"""
Update PGCIS Action List in Notion
- Archives all existing entries
- Creates new entries from CSV file

Requires: pip install requests

Usage:
  1. Set your Notion API token as environment variable:
     export NOTION_API_TOKEN="your_token_here"

  2. Run the script:
     python3 update_notion_database.py
"""

import csv
import json
import os
import requests
from datetime import datetime
from time import sleep

# Configuration
DATABASE_ID = "28d776f6-a4e0-8014-8f3f-fdde8020d043"
CSV_FILE = "/Users/bentonperet/Documents/Benton's Brain/1 Projects/Saga Pryor DC/_Project Management/Actions/Consolidated Action Items - FINAL-FIXED.csv"
NOTION_API_VERSION = "2022-06-28"

def get_headers():
    """Get headers for Notion API requests"""
    token = os.environ.get("NOTION_API_TOKEN")
    if not token:
        raise Exception("NOTION_API_TOKEN environment variable not set")

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_API_VERSION
    }

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
            print(f"✓ Read CSV with {encoding} encoding")
            return actions
        except UnicodeDecodeError:
            continue
    raise Exception("Could not read CSV with any known encoding")

def query_database_pages(database_id, start_cursor=None):
    """Query all pages in a database"""
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    payload = {"page_size": 100}
    if start_cursor:
        payload["start_cursor"] = start_cursor

    response = requests.post(url, headers=get_headers(), json=payload)
    response.raise_for_status()
    return response.json()

def archive_page(page_id):
    """Archive (delete) a page"""
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {"archived": True}
    response = requests.patch(url, headers=get_headers(), json=payload)
    response.raise_for_status()
    return response.json()

def create_database_entry(row):
    """Create a new database entry from CSV row"""
    url = "https://api.notion.com/v1/pages"

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
                        "content": row['Action Description'][:2000]  # Notion limit
                    }
                }
            ]
        },
        "Notes_Comments": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": row['Notes_Comments'][:2000]  # Notion limit
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

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": properties
    }

    response = requests.post(url, headers=get_headers(), json=payload)
    response.raise_for_status()
    return response.json()

def main():
    print("=" * 60)
    print("PGCIS Action List Notion Update")
    print("=" * 60)

    # Step 1: Read CSV
    print("\n[1/3] Reading CSV file...")
    actions = read_csv_actions()
    print(f"✓ Found {len(actions)} actions in CSV")

    # Step 2: Archive existing pages
    print("\n[2/3] Archiving existing database entries...")
    all_pages = []
    has_more = True
    start_cursor = None

    while has_more:
        result = query_database_pages(DATABASE_ID, start_cursor)
        all_pages.extend(result["results"])
        has_more = result["has_more"]
        start_cursor = result.get("next_cursor")
        sleep(0.3)  # Rate limiting

    print(f"  Found {len(all_pages)} existing entries to archive")

    for i, page in enumerate(all_pages, 1):
        try:
            archive_page(page["id"])
            print(f"  ✓ Archived {i}/{len(all_pages)}")
            sleep(0.3)  # Rate limiting
        except Exception as e:
            print(f"  ✗ Error archiving page {page['id']}: {e}")

    # Step 3: Create new entries
    print(f"\n[3/3] Creating {len(actions)} new entries...")
    for i, action in enumerate(actions, 1):
        try:
            create_database_entry(action)
            print(f"  ✓ Created {action['Name']} ({i}/{len(actions)})")
            sleep(0.3)  # Rate limiting
        except Exception as e:
            print(f"  ✗ Error creating {action['Name']}: {e}")

    print("\n" + "=" * 60)
    print("✓ Update complete!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
