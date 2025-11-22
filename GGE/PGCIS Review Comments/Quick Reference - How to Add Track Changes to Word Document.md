**Created:** 2025-11-14
**Tags:** #instructions #microsoft-word #track-changes
**Related:** [[GGE - Information Security Architecture - DETAILED REVIEW COMMENTS]]

---

# Quick Reference: Adding Track Changes to Word Document

## Overview

You now have a detailed review document with recommended text. Here's how to incorporate these into the Word document with Track Changes so the client can see your suggestions.

---

## Step-by-Step Process

### Step 1: Open the Original Word Document

```
File: GE01-DES-PM08-GG-BOD-0002 - Information Security Architecture.docx
Location: C:\Users\eriks\Documents\Obsidian\GGE\PGCIS Review Comments\
```

### Step 2: Enable Track Changes

**Method A - Ribbon:**
1. Go to **Review** tab in Word ribbon
2. Click **Track Changes** button (make sure it's highlighted/active)
3. Optionally: Click dropdown arrow → **Track Changes Options** to set your name/initials

**Method B - Keyboard Shortcut:**
- Press `Ctrl + Shift + E` (Windows)

**Verify it's on:** You should see "Track Changes: On" in the status bar at bottom of Word

---

### Step 3: Add Comments Using the Review Document

For each comment in the review document, you'll either:
- **Add text** (insertions shown in color with underline)
- **Delete text** (deletions shown in color with strikethrough)
- **Add comment bubble** (for questions or explanations)

---

## Example: Adding HIGH Priority Comment 1.1

### From Review Document:

**COMMENT 1.1 - OT/IT Network Segregation**
**Location:** Page 7, "Requirements" section, Item 1
**Recommended Change:** Add new requirement after item 1

### How to Add in Word:

1. Navigate to **Page 7, Section 3.1 Network Security, Requirements**
2. Find existing text: "1. Define and document network zoning architecture..."
3. Press **Enter** after that line to create new paragraph
4. Type the new requirement:

```
1a. Define OT/IT Network Boundary Architecture:
• BMS, EPMS, and DCIM systems shall operate on dedicated OT network segments physically or logically separated from IT networks
• HPP SCADA systems shall be air-gapped with unidirectional data diodes for monitoring data export to IT SIEM
• Critical alarm integration between OT and IT systems shall use secure protocol gateways (e.g., OPC-UA with TLS 1.3)
• OT patch management shall follow separate approval process considering 24/7 uptime requirements
• Vendor remote access to OT systems shall require jump host architecture with session recording
```

5. **Word will automatically show this as tracked insertion** (colored text, underlined)

---

### Adding a Comment Bubble (Optional but Recommended)

If you want to add explanation for WHY you're suggesting this:

1. **Select the text** you just added (the new 1a. requirement)
2. Go to **Review** tab → **New Comment** (or press `Ctrl + Alt + M`)
3. Type your explanation:

```
GGE Comment 1.1 (HIGH Priority): Data center with integrated HPP requires explicit OT/IT network boundary definition. This addresses critical infrastructure protection for BMS, EPMS, DCIM, and HPP SCADA systems. Reference: IEC 62443-3-3, ISO/IEC 27019.
```

---

## Example: Modifying Existing Text (Comment 4.2)

### From Review Document:

**COMMENT 4.2 - Log Retention**
**Location:** Page 16, Requirements section, Item 2
**Current Text:** "Log retention: ≥1 year for security systems, ≥3 months for OS logs."
**Recommended Change:** Replace with enhanced retention policy

### How to Modify in Word:

1. Navigate to **Page 16, Section 3.6, Requirements, Item 2**
2. Find: "Log retention: ≥1 year for security systems, ≥3 months for OS logs."
3. **Select and delete** that text (it will show as strikethrough)
4. **Type replacement text:**

```
2. Log retention aligned with investigation and compliance requirements:
• Security system logs (firewall, IDS/IPS, EDR, SIEM): ≥ 2 years (online 1 year, cold storage 1 year)
• OS and application logs: ≥ 1 year (online 6 months, cold storage 6 months)
• Critical infrastructure logs (BMS, EPMS, access control): ≥ 3 years (regulatory compliance for facility operations)
• Audit logs (PAM, configuration changes): ≥ 7 years (compliance with SOX, financial regulations if applicable)
```

5. Add comment bubble explaining the change:

```
GGE Comment 4.2 (MED-HIGH Priority): Extended log retention to support forensic investigations (typically 6-12 months) and align with regulatory compliance requirements for critical infrastructure operations.
```

---

## Time-Saving Tips

### Tip 1: Use "Insert" Instead of "Replace" for Non-Controversial Additions

For comments that **add** new content without changing existing text:
- Just place cursor where new content should go
- Type the new content
- No need to delete anything

**Example:** Adding new implementation items (like Comment 3.1 - Emergency Break-Glass Access)

### Tip 2: Copy-Paste from Review Document

You can copy text directly from the review markdown document and paste into Word:
1. Copy recommended text from review document
2. Paste into Word (with Track Changes enabled)
3. Word will show it as inserted text
4. Clean up any formatting issues

### Tip 3: Work Section by Section

Follow the order in the review document:
1. Start with HIGH priority comments (Section 3.1)
2. Complete all comments for that section
3. Move to next section
4. This prevents jumping around and missing items

### Tip 4: Use Comment Bubbles Strategically

**Add comment bubbles when:**
- The change is significant and needs explanation
- You're proposing something that might be debated
- You want to reference a specific standard or best practice
- The client might not understand the reason for the change

**Skip comment bubbles when:**
- The change is obvious (fixing typo, adding missing word)
- Your review document already has full explanation
- You're adding standard industry practice content

---

## Checklist for Each Comment

For each of the 19 comments in the review document:

- [ ] Navigate to correct location in Word document
- [ ] Verify Track Changes is ON
- [ ] Make the change (add, delete, or modify text)
- [ ] Add comment bubble if needed for explanation
- [ ] Cross-reference with review document to ensure complete
- [ ] Check formatting (bullets, numbering, bold/italic)
- [ ] Move to next comment

---

## Priority Order for Adding Comments

### Phase 1: HIGH Priority (Must Do - ~2-3 hours)
1. Comment 1.1 - OT/IT Network Segregation
2. Comment 1.2 - Zero Trust Implementation
3. Comment 2.1 - Hypervisor Patch Management
4. Comment 3.1 - Emergency Break-Glass Access
5. Comment 4.1 - SIEM Integration with Facility Systems
6. Comment 5.1 - Cyber-Physical Incident Response
7. Comment 5.2 - Ransomware Response Playbook
8. Comment 6.1 - Cyber-Physical Security Integration
9. General-D - Georgian Regulatory Compliance

### Phase 2: MEDIUM Priority (Should Do - ~1-2 hours)
10. Comment 4.2 - Log Retention
11. Comment 7.1 - OT Vendor VPN Access
12. Comment 8.1 - OT Endpoint Protection
13. Comment 9.1 - Operational Readiness Metrics
14. Comment 10.1 - DCIM Integration
15. General A-C - BCP/DR, Procedures, Uptime Tier

### Phase 3: LOW Priority (Nice to Have - ~30 min)
16. Comment 11.1 - Quantum-Safe Crypto
17. Comment 12.1 - Role-Specific Training

---

## Final Steps Before Sending

### 1. Review All Changes
- Use **Review** tab → **Next Change** to step through all tracked changes
- Verify each change matches your intent
- Check for any accidental edits

### 2. Add Document Summary
At the beginning of document, consider adding a page with:
- Review summary
- List of major changes
- Reviewer information
- Date of review

### 3. Save With Descriptive Filename
```
GE01-DES-PM08-GG-BOD-0002 - Information Security Architecture - R00 - GGE Comments - 2025-11-14.docx
```

### 4. Export Clean Version for Reference (Optional)
- **File** → **Save As**
- Choose "PDF" format
- This creates snapshot of your tracked changes for your records

### 5. Double-Check Before Sending
- [ ] Track Changes is visible (not hidden)
- [ ] All HIGH priority comments incorporated
- [ ] Comment bubbles added for significant changes
- [ ] Document saved with appropriate filename
- [ ] Email draft reviewed and customized

---

## Troubleshooting

### Problem: Track Changes Not Showing
**Solution:**
- Go to **Review** tab → **Display for Review** dropdown
- Select "All Markup" (not "Simple Markup" or "No Markup")

### Problem: Changes Showing in Wrong Name
**Solution:**
- **File** → **Options** → **General**
- Update "User name" and "Initials"
- Close and reopen document

### Problem: Can't Edit Document
**Solution:**
- Check if document is in "Read-Only" mode
- **Review** tab → Check if "Protect Document" is enabled
- If protected, click "Restrict Editing" and enter password (if known) or contact document author

### Problem: Lost Track of Which Comments You've Added
**Solution:**
- Print the review document as checklist
- Check off each comment as you add it to Word
- Or use the review document in split screen while editing Word

---

## Estimated Time

| Task | Time Estimate |
|------|---------------|
| Enable Track Changes & Setup | 5 minutes |
| Add 9 HIGH priority comments | 2-3 hours |
| Add 7 MEDIUM priority comments | 1-2 hours |
| Add 3 LOW priority comments | 30 minutes |
| Review all changes | 30 minutes |
| Format and finalize | 15 minutes |
| **Total** | **4-6 hours** |

**Recommendation:** Block out half a day to complete HIGH priority comments. You can return to MEDIUM/LOW later if time is tight.

---

## Ready to Start?

1. Open: `GE01-DES-PM08-GG-BOD-0002 - Information Security Architecture.docx`
2. Open: `GGE - Information Security Architecture - DETAILED REVIEW COMMENTS.md` (in second window/screen)
3. Enable Track Changes in Word
4. Start with Comment 1.1 (Page 7)
5. Work through systematically

**You've got this!** The review document has all the text ready - you're just copying it into Word with Track Changes enabled.

