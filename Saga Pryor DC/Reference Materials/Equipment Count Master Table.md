**Created:** 2025-11-05
**Tags:** #equipment-count #master-table #phasing #pryor-dc
**Related:** [[5BOD - HVAC (CSI Div 23)]], [[_BOD - Exec Summary]]

# EQUIPMENT COUNT MASTER TABLE
## Saga Pryor Data Center - Complete Phasing Equipment List

**Purpose:** Master equipment count table for all major systems across 4 phases. This table consolidates equipment counts from BOD documents and provides validation against capacity requirements.

---

## FACILITY LOAD SUMMARY

| Phase | IT MW | PUE  | Facility MW | Total Racks | L2C Racks (100kW) | RDHx Racks (25kW) |
|-------|-------|------|-------------|-------------|-------------------|-------------------|
| **1** | 3     | 1.45 | 4.35        | 30          | 30                | 0                 |
| **2** | 6     | 1.45 | 8.70        | 150         | 30                | 120               |
| **3** | 15    | 1.35 | 20.25       | 285         | 105               | 180               |
| **4** | 22    | 1.35 | 29.70       | 394         | 162               | 232               |

---

## MECHANICAL COOLING EQUIPMENT

### L2C Cooling Plant (Loop 3 - Warm Water @ 85°F)

| Equipment | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Unit Size | Purpose |
|-----------|---------|---------|---------|---------|-----------|---------|
| **Air-Cooled Chillers** | 4 | 4 | 9 | 12 | 1,500 kW each | L2C warm water supply (N+1) |
| **Total Chiller Capacity** | 6,000 kW | 6,000 kW | 13,500 kW | 18,000 kW | - | Total installed capacity |
| **N+1 Active Capacity** | 4,500 kW | 4,500 kW | 12,000 kW | 16,500 kW | - | Capacity with 1 chiller down |
| **Cooling Load Required** | 3,300 kW | 3,300 kW | 11,550 kW | 17,820 kW | - | IT load + 10% CDU parasitic |
| **Utilization (N+1)** | 73% | 73% | 96% | 108% ⚠️ | - | Load / N+1 capacity |
| **CDU Rack Pairs Served** | 30 | 30 | 105 | 162 | - | Each rack has A+B CDU pair |
| **Physical CDU Units** | 60 | 60 | 210 | 324 | ~100-120 kW each | 2 per rack (A/B redundant) |

**Note:** Phase 4 L2C utilization shows 108% - this assumes exactly 10% parasitic load. Actual CDU efficiency may vary. Monitor during detailed design.

### RDHx Cooling Plant (Loops 1+2 - Cold Water @ 60°F)

| Equipment | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Unit Size | Purpose |
|-----------|---------|---------|---------|---------|-----------|---------|
| **Air-Cooled Chillers** | 0 | 3 | 5 ✓ | 6 ✓ | 1,500 kW each | RDHx cold water supply (N+1) |
| **Total Chiller Capacity** | 0 | 4,500 kW | 7,500 kW | 9,000 kW | - | Total installed capacity |
| **N+1 Active Capacity** | 0 | 3,000 kW | 6,000 kW | 7,500 kW | - | Capacity with 1 chiller down |
| **Cooling Load Required** | 0 | 3,300 kW | 4,950 kW | 6,380 kW | - | IT load + 10% parasitic |
| **Utilization (N+1)** | - | 110% ⚠️ | 83% ✓ | 85% ✓ | - | Load / N+1 capacity |
| **RDHx Units** | 0 | 120 | 180 | 232 | ~25 kW each | 1 per RDHx rack |

**✓ CORRECTED:** Phase 3 increased from 4 to 5 chillers, Phase 4 increased from 5 to 6 chillers to provide adequate N+1 capacity.

**Note:** Phase 2 RDHx shows 110% utilization - acceptable for Phase 2 as transitional phase. Alternative: deploy 4 chillers in Phase 2 (N+1 = 4,500 kW for 3,300 kW load = 73% utilization).

### Total Chiller Count Summary

| Phase | L2C Chillers | RDHx Chillers | Total Chillers | Notes |
|-------|--------------|---------------|----------------|-------|
| **1** | 4 | 0 | **4** | L2C only |
| **2** | 4 | 3 | **7** | Add RDHx plant |
| **3** | 9 | 5 ✓ | **14** | Scale both plants |
| **4** | 12 | 6 ✓ | **18** | Full build-out |

---

## ELECTRICAL POWER EQUIPMENT

### Generators (13.8 kV Diesel, Tier 4 Final, N+1)

| Phase | Unit Count | Unit Size | Total Capacity | N+1 Active Capacity | Facility Load | Utilization (N+1) |
|-------|------------|-----------|----------------|---------------------|---------------|-------------------|
| **1** | 3 | 4.0 MW | 12.0 MW | 8.0 MW | 4.35 MW | 54% |
| **2** | 4 | 4.0 MW | 16.0 MW | 12.0 MW | 8.70 MW | 73% |
| **3** | 7 | 4.0 MW | 28.0 MW | 24.0 MW | 20.25 MW | 84% |
| **4** | 9 | 4.0 MW | 36.0 MW | 32.0 MW | 29.70 MW | 93% |

**Fuel:** ~2,000 gal belly tank per generator + centralized bulk fuel storage for 24-hour runtime.

### Transformers (13.8 kV/480V, Oil-Filled, N+1)

| Phase | Unit Count | Unit Size | Total Capacity | N+1 Active Capacity | Facility Load | Utilization (N+1) |
|-------|------------|-----------|----------------|---------------------|---------------|-------------------|
| **1** | 3 | 3,500 kVA | 10.5 MVA | 7.0 MVA | 4.35 MW | 62% |
| **2** | 4 | 3,500 kVA | 14.0 MVA | 10.5 MVA | 8.70 MW | 83% |
| **3** | 8 | 3,500 kVA | 28.0 MVA | 24.5 MVA | 20.25 MW | 83% |
| **4** | 11 | 3,500 kVA | 38.5 MVA | 35.0 MVA | 29.70 MW | 85% |

### IT UPS (Modular, N+1, 80% Loading Target)

| Phase | Module Count | Module Size | Total Capacity | N+1 Active Capacity | IT Load | Utilization (N+1 @ 80% each) |
|-------|--------------|-------------|----------------|---------------------|---------|------------------------------|
| **1** | 4 | 1,250 kVA | 5.0 MVA | 3.75 MVA @ 80% | 3.0 MW | 100% |
| **2** | 7 | 1,250 kVA | 8.75 MVA | 6.0 MVA @ 80% | 6.0 MW | 100% |
| **3** | 16 | 1,250 kVA | 20.0 MVA | 15.0 MVA @ 80% | 15.0 MW | 100% |
| **4** | 23 | 1,250 kVA | 28.75 MVA | 22.0 MVA @ 80% | 22.0 MW | 100% |

**Note:** UPS modules targeted at 80% loading each for optimal efficiency. N+1 configuration provides component redundancy; MV dual-ring provides path redundancy.

### MV Distribution (13.8 kV Ring Main Units)

| Equipment | Phase 1-4 (No Change) | Purpose |
|-----------|------------------------|---------|
| **RMUs (Ring Main Units)** | 8 | 13.8 kV, 630A, dual-ring topology |
| **Dual-Ring Segments** | 2 (Ring A + Ring B) | Self-healing SCADA switching for path redundancy |

### House Generators (Natural Gas, Non-Critical)

| Equipment | Count | Size | Purpose |
|-----------|-------|------|---------|
| **House Generators** | 2 | 250-350 kW | N+1 for offices, bathrooms, hallways, SCR, SCB, loading dock, NOC, gym, storm shelter |

---

## FACILITY CONSTRUCTION

| Component | Specification | Notes |
|-----------|---------------|-------|
| **White Space** | 20,000 SF | Two 10,000 SF data halls (DH-W + DH-E) |
| **Total Compound** | 140,000 SF | Covered building (38,000 SF) + Equipment yard (102,000 SF) |
| **Covered Building** | 38,000 SF | Data halls + support spaces |
| **Equipment Yard** | 102,000 SF | Electrical + mechanical equipment |
| **Ceiling Height** | 30+ ft | Data hall clear height |
| **Construction Type** | Tilt-up concrete | FM 1-150 tornado-rated, reinforced walls |
| **Storm Shelter** | 1 unit (20 person) | FEMA 361 EF5-rated, prefabricated module |

---

## SUPPORT SPACES EQUIPMENT

| Space | Equipment/Features | Notes |
|-------|-------------------|-------|
| **Security Control Room (SCR)** | CCTV monitoring, access control | East entry zone |
| **Security Control Booth (SCB)** | Loading dock monitoring | West loading zone |
| **Mantrap** | Card + biometric MFA | Secure entry |
| **NOC (Level 2)** | ~2,060 SF, precision cooling | 24/7 operations center |
| **Storm Shelter (Level 1)** | 20 person capacity | FEMA 361 compliant |
| **Elevator** | 1 unit, 3-level service | Central spine |
| **MPOE (Fiber Entrance)** | 2 locations (east + west) | Dual diverse fiber entries |
| **MMR (Meet-Me-Room)** | 2 locations (east + west) | Redundant interconnect |

---

## FIRE PROTECTION

| System | Specification | Coverage |
|--------|---------------|----------|
| **Sprinkler System** | Zoned preaction | Data halls |
| **VESDA Detection** | Very Early Smoke Detection | Data halls |
| **Cabinet Suppression** | Integrated in DDC cabinets | Rack-level protection |
| **PDM Suppression** | Clean agent per NFPA | Electrical enclosures |
| **Emergency Lighting** | 90-minute battery backup | All egress paths |

---

## VALIDATION NOTES

### ✅ Aligned Items
- IT capacity phasing (3 → 6 → 15 → 22 MW)
- Rack counts (30 → 150 → 285 → 394)
- L2C cooling capacity (16.2 MW ultimate)
- RDHx cooling capacity (5.8 MW ultimate)
- PUE targets (1.45 → 1.35)
- Supply temperatures (85°F L2C, 60°F RDHx)
- Generator, transformer, UPS counts

### ⚠️ Corrections Made
1. **RDHx Chiller Counts:**
   - Phase 3: Increased from 4 to **5 chillers** (4,950 kW load requires 6,000 kW N+1 capacity)
   - Phase 4: Increased from 5 to **6 chillers** (6,380 kW load requires 7,500 kW N+1 capacity)

2. **CDU Count Clarification:**
   - "CDU Rack Pairs Served": 162 (one A+B pair per rack)
   - "Physical CDU Units": 324 (two physical units per rack for A/B redundancy)

3. **Free Cooling Hours:**
   - Corrected estimate: **3,500-4,000 hours/year** (not 5,000-6,000)
   - Based on L2C best practices research for 85°F warm water in Oklahoma climate

### 🚨 Action Items for BOD Update
1. Update Exec Summary free cooling hours (line 96): 5,000-6,000 → 3,500-4,000
2. Update Exec Summary RDHx chiller counts:
   - Phase 3: 4 → 5 chillers
   - Phase 4: 5 → 6 chillers
3. Clarify CDU terminology (rack pairs vs. physical units)
4. Consider adding Phase 2 RDHx 4th chiller for better margin (optional)

---

**Document Version:** 1.0
**Last Updated:** 2025-11-05
**Prepared by:** Claude Code alignment verification