# Recent Vault Changes

**Purpose:** Track recent file updates across the PGCIS Obsidian vault
**Tags:** #dashboard #tracking #pgcis

---

## Manual Updates (Current)

**2025-11-12:**
- Created new vault folder structure
- Created PGCIS Knowledge Management Strategy document
- Created README files for Service Line Templates and Shared Resources
- Created Project Index Dashboard
- Set up organizational folders: _Client_Projects, _Service_Line_Templates, _Shared_Resources, _Company, _Tools, _Utilities, _Archive

---

## Recent Project Updates

### Saga Pryor DC
- 2025-11-09: Multiple BOD updates
- 2025-11-07: Merged remote changes, resolved BOD v2 conflict
- 2025-11-06: Various design updates

### Hut 8 Riverbend
- 2025-11-11: Proofreading review completed
- 2025-11-10: Final proposal submitted
- 2025-11-09: Equipment lists updated
- 2025-11-08: Multiple proposal sections refined

### GGE Georgia
- 2025-11-06: Design review updates
- Recent: 10kV voltage updates

---

## Dataview Queries (To Be Activated)

> **Note:** The queries below will activate once projects are migrated to the new folder structure with proper metadata headers.

### Files Modified Today
```dataview
TABLE file.mtime as "Modified", file.folder as "Location"
WHERE file.mtime >= date(today)
SORT file.mtime DESC
```

### Files Modified This Week
```dataview
TABLE file.mtime as "Modified", file.folder as "Folder"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 50
```

### Files Modified This Month
```dataview
TABLE file.mtime as "Modified", file.folder as "Folder"
WHERE file.mtime >= date(today) - dur(30 days)
SORT file.mtime DESC
LIMIT 100
```

### Templates Recently Modified
```dataview
TABLE file.mtime as "Updated"
FROM "_Service_Line_Templates"
WHERE file.mtime >= date(today) - dur(30 days)
SORT file.mtime DESC
```

### Shared Resources Updates
```dataview
TABLE file.mtime as "Updated"
FROM "_Shared_Resources"
WHERE file.mtime >= date(today) - dur(30 days)
SORT file.mtime DESC
```

### Active Projects Activity
```dataview
TABLE file.mtime as "Last Modified", file.folder as "Project"
FROM "_Client_Projects"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

---

## Most Frequently Updated Files (Last 30 Days)

[To be populated by Dataview once metadata is in place]

---

**Related:**
- [[Project_Index_Dashboard|Project Index]]
- [[Template_Usage_Guide|Template Usage]]

**Last Manual Update:** 2025-11-12
