**Created:** 2025-10-23 12:00

# Action ID Renumbering Guide
## Transition from A-XXX to CSI MasterFormat Division Format

**Purpose:** Document the renumbering of all project actions from sequential A-XXX/F-XXX format to CSI MasterFormat division-based numbering for better organization and alignment with Basis of Design structure.

---

## Renumbering Mapping: Old → New

### Priority 1 - Critical Path

| Old ID | New ID | Action Description | Division |
|--------|--------|-------------------|----------|
| A-008 | 26-099 | BESS-as-UPS analysis (REJECTED) | Electrical |
| A-041 | 48-001 | Generator/turbine configuration modeling | Power Generation |
| A-002 | 33-002 | Natural gas service confirmation | Utilities |
| A-005 | 00-001 | Send Camelot Scope to PGCIS | Project Management |
| A-049 | 99-001 | Environmental consultant emissions/permitting | Environmental/Permitting |
| A-039 | **33-001** | **Utility interconnection (ENHANCED)** | Utilities |

### Priority 2 - Critical

| Old ID | New ID | Action Description | Division |
|--------|--------|-------------------|----------|
| A-038 | 00-002 | Schedule follow-up meeting | Project Management |
| A-011 | 99-002 | Research turbine lead times | Procurement |
| A-009 | 26-100 | BESS-as-UPS CapEx savings (REJECTED) | Electrical |
| A-004 | 33-003 | ALTA survey natural gas info | Utilities |
| A-020 | 27-001 | Camelot fiber + Aaron Google coordination | Communications |

### Priority 3 - High

| Old ID | New ID | Action Description | Division |
|--------|--------|-------------------|----------|
| A-040 | 27-002 | Receive/review Camelot studies | Communications |
| A-036 | 27-003 | Research GCP Cloud Interconnect | Communications |
| A-032 | 23-001 | Finalize chiller plant sizing | Mechanical |
| A-034 | 23-002 | CapEx comparison closed-loop cooling | Mechanical |
| A-047 | 23-003 | RDHx incremental deployment | Mechanical |
| F-002 | 27-004 | Diverse fiber routes to Google | Communications |
| A-030 | 99-003 | Power pass-through model review | Financial |
| A-059 | 99-004 | Validate power pricing assumptions | Financial |
| A-058 | 99-005 | Model both power pricing strategies | Financial |
| A-001 | 33-005 | Demand response programs research | Utilities |

### Priority 4 - Medium

| Old ID | New ID | Action Description | Division |
|--------|--------|-------------------|----------|
| A-043 | 02-002 | Validate slab-on-grade foundation | Building & Site |
| A-018 | 02-003 | Review geotech analysis | Building & Site |
| A-012 | 02-004 | FM I-135 tornado roof standards | Building & Site |
| A-044 | 02-005 | Tornado shelter specifications | Building & Site |
| A-046 | 02-006 | Roof upgrade for wind resistance | Building & Site |
| A-013 | 02-007 | Document storm mitigation features | Building & Site |
| A-029 | (merged with 02-004) | FM I-135 vs ASCE comparison | Building & Site |
| A-019 | 23-004 | RDHx vs fan walls CapEx analysis | Mechanical |
| A-024 | 33-006 | Validate substation transformer sizing | Utilities |
| A-021 | 99-006 | Generac diesel generator lead times | Procurement |
| A-022 | 99-007 | Clarify OCP compliance | Procurement |
| A-018 (dup) | 02-008 | Put geotech in Dropbox | Building & Site |
| A-016 | 99-008 | Notify consultant - raised floor | Financial |
| A-017 | 99-009 | Notify consultant - RDHx change | Financial |
| F-012 | **33-004** | **Water/wastewater study (ENHANCED)** | Utilities |

---

## New Actions Added (from BOD Review)

| New ID | Action Description | Division | Source |
|--------|-------------------|----------|--------|
| **33-001** | **Comprehensive utility interconnection & grid power validation** | Utilities | Enhanced A-039 with grid power + solar monetization questions |
| 33-007 | Determine POI configuration (single vs dual) | Utilities | BOD Priority 1 |
| 33-008 | Confirm diesel fuel storage strategy | Utilities | BOD Priority 3 |
| 26-001 | Confirm UPS equipment specifications and pricing | Electrical | BOD Priority 2 |
| 48-002 | Confirm final generator configuration | Power Generation | BOD Priority 2 |
| 26-002 | Confirm electrical room configuration (indoor vs outdoor) | Electrical | BOD Priority 2 |
| 23-005 | Validate CDU sizing for AI racks | Mechanical | BOD Priority 2 |
| 23-006 | Confirm rooftop AHU configuration | Mechanical | BOD Priority 2 |
| 02-001 | Confirm building test fit and equipment yards | Building & Site | BOD Priority 2 |
| 00-003 | Update total project CAPEX range | General Requirements | BOD Priority 4 |
| 01-001 | Finalize BOD for MEP handoff | General Requirements | BOD Priority 5 |

---

## CSI MasterFormat Division Numbering Scheme

**Format:** `[Division]-[Sequential Number]`

### Division Assignments:

- **00-XXX**: Project Management, Procurement, Contracting
- **01-XXX**: General Requirements (commissioning, QA/QC, handoff)
- **02-14-XXX**: Building & Site (earthwork, concrete, structure, envelope, openings)
- **23-XXX**: HVAC / Mechanical Systems
- **26-XXX**: Electrical Systems
- **27-XXX**: Communications / Connectivity
- **28-XXX**: Electronic Safety & Security
- **33-XXX**: Utilities (electrical, gas, water, sewer)
- **48-XXX**: Power Generation (generators, turbines, solar)
- **99-XXX**: Cross-Cutting (financial, procurement, environmental when not specific to other divisions)

### Numbering Convention:
- **X01-X49**: Standard actions within division
- **X50-X79**: Design validation actions
- **X80-X98**: Cost/financial actions related to division
- **X99-X100**: Rejected/archived actions (for historical reference)

---

## Key Changes & Mergers

### Enhanced Actions:

**33-001 (was A-039): Comprehensive Utility Interconnection Study**
- **Enhanced with:** Grid power validation (foundational question: is power available?)
- **Enhanced with:** Solar monetization questions (12MW export for Option A, 6-8MW additional load for Option B)
- **Enhanced with:** Camelot Task 1 coordination (substation hosting capacity, transmission analysis)
- **Enhanced with:** POI configuration determination (single BTM vs dual)
- **Impact:** Now THE most critical foundational action - without grid power, project cannot proceed

**33-004 (was F-012): Water & Wastewater Availability Study**
- **Enhanced with:** Zero water cooling strategy context (domestic use only)
- **Enhanced with:** Oklahoma DEQ requirements for on-site well/septic if municipal unavailable
- **Enhanced with:** BOD cost estimates ($50-200K municipal, $100-300K on-site)

**27-001 (was A-020): Fiber & GCP Coordination**
- **Enhanced with:** Clarification that Camelot Task 3 provides fiber drawings
- **Enhanced with:** Separation of Aaron's Google GCP outreach from Camelot scope
- **Enhanced with:** Questions for Camelot on T&M fiber design work

### Rejected Actions (Status Changed):

**26-099 (was A-008): BESS-as-UPS Analysis**
- **Status:** Changed to "Rejected"
- **Rationale:** Violates Tier III concurrent maintainability (non-maintainable SPOF)
- **Decision:** Traditional 2N modular UPS confirmed (Phase 1: $4.5M, ultimate: $26.3M phased)
- **Reference:** [[Why BESS Should Not Be UPS]] document

**26-100 (was A-009): BESS-as-UPS CapEx Savings**
- **Status:** Changed to "Rejected"
- **Rationale:** Savings do NOT justify Tier III violation and lender risk. Economic BESS also rejected (negative NPV: -$5.3M to -$6.2M)
- **Decision:** Traditional UPS required for project finance viability
- **Reference:** [[Excess Solar Monetization Strategy]] document

---

## Total Action Count: 47

**By Priority:**
- Priority 1 (Critical Path): 6 actions
- Priority 2 (Critical): 5 actions
- Priority 3 (High): 15 actions
- Priority 4 (Medium): 21 actions

**By Division:**
- **Utilities (33-XXX)**: 8 actions
- **Mechanical (23-XXX)**: 6 actions
- **Electrical (26-XXX)**: 4 actions (includes 2 rejected BESS actions)
- **Building & Site (02-XXX)**: 8 actions
- **Power Generation (48-XXX)**: 2 actions
- **Communications (27-XXX)**: 4 actions
- **Financial/Procurement (99-XXX)**: 9 actions
- **Project Management (00-XXX)**: 3 actions
- **General Requirements (01-XXX)**: 1 action
- **Environmental (99-XXX)**: 1 action (cross-cutting)

---

## Migration Path

1. **Immediate:** Use new Consolidated Action Items.csv for all future tracking
2. **Transition:** Old Action Items.csv archived as "Action Items - Legacy (A-XXX format).csv"
3. **Communication:** Notify team of new numbering scheme via email/meeting
4. **Documentation:** Update all BOD references to use new action IDs
5. **Tools:** Update any project management tools/trackers with new IDs

---

## Benefits of CSI Division Numbering

✅ **Alignment with BOD:** Action IDs now match CSI MasterFormat divisions used in Basis of Design documents
✅ **Clarity:** Instant recognition of which discipline owns the action (33-XXX = Utilities, 26-XXX = Electrical)
✅ **Scalability:** Easy to add new actions within existing divisions without numbering conflicts
✅ **Integration:** BOD pages can directly reference action IDs (e.g., "See Action 33-001 for utility interconnection")
✅ **Organization:** Actions naturally grouped by discipline for filtering and reporting

---

**Tags:** #saga-project #action-items #renumbering #csi-masterformat #project-management

**Related Documents:**
- [[Consolidated Action Items.csv]] - New action tracking file
- [[Action Items.csv]] - Legacy file (A-XXX format, archived)
- [[BOD Confirmation Actions - Draft]] - Source of new BOD actions
- [[Saga Pryor DC/Basis of Design/Benton_BOD/_BOD - Exec Summary and TOC]] - Basis of Design overview
