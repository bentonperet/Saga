**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md + Erik_BOD references

# BASIS OF DESIGN - GENERAL REQUIREMENTS
## CSI Division 01
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

## 01 10 00 – SUMMARY

- Scope includes design, procurement, construction, commissioning, and turnover of a 50,000 GSF Tier III data center with 3 MW Phase 1 IT and 12 MW Phase 2.
- All critical systems shall be concurrently maintainable: N+1 IT UPS with 13.8 kV dual-ring MV path redundancy, N+1 mechanical, N+1 generators and transformers.

---

## 01 14 00 – WORK RESTRICTIONS

- Normal work hours: M–F, 7:00–17:00; after-hours for outages or noisy work.
- Security badging required; background checks for all personnel.
- No photography without Owner approval; NDA required.

---

## 01 30 00 – ADMINISTRATIVE REQUIREMENTS

- Kickoff meeting; weekly OAC meetings; monthly risk reviews.
- RFI process via Procore (or Owner’s platform); 3 business-day response goal.
- Document control: Use drawing/revision indices; cloud-based repository.

---

## 01 33 00 – SUBMITTALS

- Product data, shop drawings, samples, calculations, test reports.
- Critical submittals: Generators, MV gear, transformers, UPS, chillers, RMUs, fire alarm, DOAS, CDUs, BESS (if included), solar inverters.
- Provide factory witness test plans for generators, UPS, switchgear, chillers.

---

## 01 35 00 – SPECIAL PROCEDURES

- Hot work permits; lockout/tagout (LOTO); confined space.
- Outage coordination: 10 business days’ notice; method of procedure (MOP) required.
- Vibration/noise controls for nearby stakeholders.

---

## 01 40 00 – QUALITY REQUIREMENTS

- Manufacturers: Tier-1 with 10+ year support and parts availability.
- Factory testing: FAT for UPS, switchgear, generators, BMS head-end.
- Field testing: Acceptance testing per NETA ATS (electrical), TAB (mechanical).

---

## 01 42 00 – IDENTIFICATION AND NAMING STANDARDS

### Asset Naming Hierarchy

**Campus Code:** `TUL` (Tulsa International Airport - nearest major airport to Pryor, OK)

**Building Numbering:** `TUL-##`
- First building: `TUL-01`
- Future expansion: `TUL-02`, `TUL-03`, etc.

**Floor Designation:** `TUL-##-F#`
- Ground floor: `F1`
- Mezzanine: `F2`
- Upper level: `F3`

**Zone Codes:** `TUL-##-F#-ZZZ`
- Data halls: `DH1`, `DH2`
- Equipment yards: `EYN` (North/Mechanical), `EYS` (South/Electrical)
- Substation: `SUB`
- Network Operations Center: `NOC`
- Meet-Me Rooms: `MMR1`, `MMR2`
- Main Distribution Area: `MDA`

### Equipment Asset Tagging Format

**Full Asset ID:** `XXX-##-F#-ZZZ-EEEEE-###`

**Components:**
- Location: `XXX-##-F#-ZZZ` (Campus-Building-Floor-Zone)
- Equipment Type: `EEEEE` (5-character code)
- Unit Number: `###` (3-digit sequential)

**Key Equipment Type Codes:**
- Generators: `GEN` (e.g., `TUL-01-F1-EYS-GEN-001`)
- Transformers: `XFMR` (e.g., `TUL-01-F1-EYS-XFMR-001`)
- UPS Modules: `UPS-IT`, `UPS-MC`
- Chillers: `CHLR` (e.g., `TUL-01-F1-EYN-CHLR-L1-001`)
- Pumps: `PUMP`
- CDUs: `CDU`
- Switchboards: `SWBD`
- Racks/Cabinets: Format `TUL-01-F1-DH1-R001` (R001 through R030)

### Path and Loop Designation

**Electrical Paths (Dual Switchboards on Different MV Ring Segments):**
- Add suffix `-A` or `-B` for switchboard designation (SWBD-A on Ring A, SWBD-B on Ring B)
- Example: `TUL-01-F1-EYS-SWBD-A`, `TUL-01-F1-EYS-SWBD-B`
- Cabinet PDUs: `TUL-01-F1-DH1-PDU-R001-A`, `PDU-R001-B` (fed from different panels/switchboards)

**Mechanical Loops:**
- Add suffix `-L#` for Loop number
- Loop 1+2: Air cooling (shared plant)
- Loop 3: Direct-to-chip cooling
- Example: `TUL-01-F1-EYN-CHLR-L1-001`, `CHLR-L3-001`

### Physical Asset Labels

**Label Content:**
- QR code (machine-readable, links to DCIM asset record)
- Human-readable asset ID
- Equipment description and capacity
- Vendor serial number
- Commissioning date

**Label Material:**
- Outdoor equipment: Anodized aluminum (weather/UV resistant)
- Indoor equipment: Laminated polyester
- Engraving: Laser-engraved (permanent, no fade)

**Label Placement:**
- Primary: Front panel at eye level
- Backup: Rear/side panel (for large equipment)
- Cable entry points: Cable identification labels

### Cable and Conduit Marking

**Cable ID Format:** `[SOURCE]-[DEST]-[TYPE]-###`

Examples:
- Power cable: `SWBD-A-PANEL-DH1-PWR-001`
- MV cable: `RMU-001-XFMR-001-MV-001`
- Fiber: `MMR1-DH1-R001-FIBER-001`

**Labeling Frequency:**
- Every 10 ft along cable route
- At both termination points
- At all junction boxes and pull points

### DCIM/Asset Management Integration

**Required Asset Registry Fields:**
- Asset ID (per naming standard)
- Asset type and capacity
- Location (Campus-Building-Floor-Zone)
- Vendor, model, serial number
- Commissioning date, warranty expiration
- Path/Loop assignment
- BMS/EPMS point address
- Maintenance schedule links

**Database Population:**
- All assets registered in DCIM before commissioning
- QR codes link directly to DCIM asset record
- Changes tracked with revision history

### Documentation Requirements

**Contractor Deliverables:**
- Asset tag schedule (Excel/CSV with all equipment IDs)
- As-built cable schedule (source-destination-ID for all cables)
- Physical labels installed and photographed
- DCIM database populated and verified

**Detailed Naming Standard:**
See [[Appendix A - Asset Naming and Tagging Standard]] for complete rubric, equipment type codes, and examples.

---

## 01 43 00 – CODE COMPLIANCE

- Comply with NEC 2023, IBC/IFC 2021, NFPA, IEEE, ASHRAE, TIA-942.
- Local AHJ approvals; utility interconnect agreements.

---

## 01 50 00 – TEMPORARY FACILITIES

- Temporary power, lighting, water, sanitary per OSHA.
- Temporary security fence/gates; badging trailer if needed.
- Temporary network for coordination (separate from customer IT).

---

## 01 60 00 – PRODUCT REQUIREMENTS

- Standardize on: 13.8 kV MV equipment, 3,500 kVA transformers, 4.0 MW MV gens, 1,500 kW chillers, 1,250 kVA IT UPS modules (N+1), 250 kW mech UPS.
- Spares: Filters, UPS modules (one spare module per 5 deployed), sensors, controller cards.

---

## 01 70 00 – EXECUTION AND CLOSEOUT

- Closeout submittals: O&M manuals, as-builts (PDF + CAD/BIM), warranty certificates.
- Training: 40 hours per discipline (electrical, mechanical, BMS, security).
- Warranties: 1 year minimum; extended warranties for UPS batteries (5–10 years), generators (5 years), roof (20 years).

---

## 01 78 00 – CLOSEOUT SUBMITTALS

- Turnover: Asset registry, maintenance schedules, vendor contacts.
- As-builts: Redline drawings transferred to CAD/BIM; point lists for BMS/EPMS/DCIM.

---

## 01 79 00 – DEMONSTRATION AND TRAINING

- Vendor-led training sessions with recordings; quick-reference guides.
- Emergency drills: Generator failover, fire alarm, security breach.

---

## 01 90 00 – COMMISSIONING

- Commissioning Agent (CxA): Independent 3rd party.
- Levels 1–5: Factory tests, delivery inspection, start-up, functional testing, IST.
- IST scenarios: Utility loss, chiller failure, UPS module failure, RMU switching, fire alarm.
- Performance targets: PUE ≤1.35 (Phase 1), ≤1.25 (Phase 2).

---

## 01 91 00 – MONITORING & REPORTING

- Monthly reports: PUE, WUE, uptime, incident summaries, maintenance performed.
- Quarterly reviews: Energy optimization, capacity planning, reliability improvements.

---

**Tags:** #general-requirements #commissioning #submittals #quality #codes #cx

**Next Steps:**
1. Approve standardized equipment list and preferred vendors
2. Appoint CxA and finalize commissioning plan
3. Establish Procore (or equivalent) for RFI/submittal workflows

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md, Erik_BOD references
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** Standardized equipment list, commissioning scope, training