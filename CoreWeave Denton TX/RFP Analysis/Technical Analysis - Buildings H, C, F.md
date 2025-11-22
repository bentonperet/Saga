**Created:** 2025-11-19 14:15
**Tags:** #coreweave #technical-analysis #equipment #commissioning #building-h #building-c #building-f
**Related:** [[Building Selection - REVISED Priority Analysis]], [[powsybl-project/README]]

---

# Technical Analysis - CoreWeave Denton Campus
## Buildings H, C, & F - Equipment & Commissioning Assessment

**NOTE:** Main drawings PDF (2.8GB) could not be accessed due to file size. Analysis based on OFE (Owner Furnished Equipment) Tracker. **Request smaller drawing set or specific sheets for complete analysis.**

---

## CAMPUS OVERVIEW - All Buildings Summary

### Building Designations & Scale

| Building | IT Modules | Mech Modules | UPS Capacity | IT Load Estimate | Complexity Tier |
|----------|-----------|--------------|--------------|------------------|-----------------|
| **A** | 5 | 3 | 12.5 MW UPS | ~10 MW IT | Small |
| **B** | 21 | 10 | 52.5 MW UPS | **~42 MW IT** | **LARGEST** |
| **C** | 21 | 10 | 52.5 MW UPS | **~42 MW IT** | **LARGEST** |
| **D** | 21 | 10 | 52.5 MW UPS | **~42 MW IT** | **LARGEST** |
| **E** | 5 | 3 | 12.5 MW UPS | ~10 MW IT | Small |
| **F** | 21 | 10 | 52.5 MW UPS | **~42 MW IT** | **LARGEST** |
| **G** | 21 | 10 | 52.5 MW UPS | **~42 MW IT** | **LARGEST** |
| **H** | 21 | 10 | 52.5 MW UPS | **~42 MW IT** | **LARGEST** |

**Campus Total: ~306 MW IT Load** (assuming 80% UPS efficiency)

**Large Buildings (B, C, D, F, G, H): Identical 42 MW configuration**
**Small Buildings (A, E): Identical 10 MW configuration**

---

## BUILDING H - DETAILED ANALYSIS

### IT Load Capacity

**UPS Configuration:**
- **42x Delta 1250kVA UPS units** = 52.5 MVA total UPS capacity
- **30x Delta 250kVA UPS units** = 7.5 MVA total UPS capacity
- **Total UPS: 60 MVA / ~48 MW** (at 0.8 PF)
- **Estimated IT Load: ~42 MW** (assuming 85-90% loading)

**Power Distribution:**
- 54x Delta 800A STS (Static Transfer Switches)
- 54x Delta 800A Busway
- 58x Delta 600A Busway
- 2x Delta 400A Busway
- 54x 63A PIU (Power Interface Units) - **INCLUDED IN BUSWAY**
- 1,114 LF (339 m) EAE 4000A Reserve Busduct

### Mechanical Systems

**Chiller Plant:**
- **30x JCI 500-ton chillers** (1,758 kW each) (JCI-500T-115-CHILLER)
- **Total Cooling: 15,000 tons (52,750 kW)** = ~18 MW cooling capacity
- **4x Wendland 30,000 gal (114 m³) horizontal thermal storage tanks** = 120,000 gal (454 m³) total
- **30x Fisen chilled water pump skids** (YVFA0459)
- **1,200x Danfoss 2" (50mm) FD83 quick-connect couplers**

**Air Distribution:**
- **48x JCI 72K CFM (122,400 m³/h) fan walls** (MOST of all buildings)
- 2x AAON RQA-011 DOAS (Dedicated Outdoor Air System)
- 4x Condair RS-030 humidifiers
- 2x Dadex 60kW CRAH (data hall)
- 4x Dadex 60kW CRAH (MMR - Machine Room)

**IT/Mechanical Modules:**
- **21x MCFI IT Modules** ($29.5M - largest modular investment)
- **10x MCFI Mechanical Modules** ($14.1M)

### Electrical Infrastructure

**Transformers:**
- **21x JCL Energy 2550kVA 34.5kV KNAN transformers** (natural air cooled)
- **10x JCL Energy 2550kVA 34.5kV KNAF transformers** (forced air cooled)
- **Total: 31 transformers = 79 MVA capacity**

**Generators:**
- **18x CAT 1.25MW generators** (T5 Data Solutions)
- **Total Generator Capacity: 22.5 MW**
- 9x Point Eight Power 1.25MW CAT switchboards

**Key Observation:** Generator capacity (22.5 MW) is ~50% of IT load (42 MW). This suggests:
1. Utility is primary power source
2. Generators provide N+1 or 2N backup for critical loads only
3. NOT a behind-the-meter generation facility

### Equipment Counts - Building H

| Category | Equipment Type | Quantity | Cx Complexity |
|----------|----------------|----------|---------------|
| **UPS Systems** | 1250kVA UPS | 42 | HIGH |
| | 250kVA UPS | 30 | MEDIUM |
| **Static Transfer** | 800A STS | 54 | HIGH |
| **Power Distribution** | 800A Busway | 54 | MEDIUM |
| | 600A Busway | 58 | MEDIUM |
| | 400A Busway | 2 | LOW |
| | 4000A Reserve Busduct | 1,114 LF (339 m) | MEDIUM |
| **Transformers** | 2550kVA 34.5kV (KNAN) | 21 | MEDIUM |
| | 2550kVA 34.5kV (KNAF) | 10 | MEDIUM |
| **Generators** | 1.25MW CAT Gen | 18 | HIGH |
| | Switchboards | 9 | MEDIUM |
| **Chillers** | 500-ton (1,758 kW) chillers | 30 | HIGH |
| **Thermal Storage** | 30K gal (114 m³) tanks | 4 | MEDIUM |
| **Pumps** | CW Pump Skids | 30 | MEDIUM |
| **Quick Connects** | 2" (50mm) Couplers | 1,200 | LOW (count) |
| **Fan Walls** | 72K CFM (122,400 m³/h) | **48** | HIGH |
| **DOAS** | AAON units | 2 | MEDIUM |
| **Modular** | IT Modules | 21 | VERY HIGH |
| | Mech Modules | 10 | VERY HIGH |
| **TOTAL MAJOR EQUIPMENT** | | **~440 units** | |

### Building H - Commissioning Implications

**Advantages:**
1. **Standalone infrastructure** - No shared courtyards, equipment yards, or MV distribution
2. **Latest lessons learned** - 5 buildings commissioned before H starts
3. **48 fan walls** = Most of any building (10 more than B/C/D/F/G) - likely larger data hall
4. **Modular equipment** - IT/Mech modules should have factory testing pre-complete

**Challenges:**
1. **18 generators** = Most of any building (vs 4-8 for others) - extensive generator testing
2. **Complexity:** 440+ major equipment items requiring integrated testing
3. **54 STS units** - Each requires dual-source transfer testing
4. **30 chillers** - Full chiller plant sequencing and optimization
5. **Long flush/fill** - 15 days indicates complex piping/large volume

**Estimated Cx Duration:**
- **L4 Functional Testing:** 20-25 days (vs 14 planned)
- **L5 Integrated Testing:** 7-10 days (vs 5 planned)
- **Contingency needed:** 10+ days beyond plan

---

## BUILDING C - DETAILED ANALYSIS

### IT Load Capacity

**UPS Configuration:**
- **42x Delta 1250kVA UPS units** = 52.5 MVA total
- **30x Delta 250kVA UPS units** = 7.5 MVA total
- **Total UPS: 60 MVA / ~48 MW**
- **Estimated IT Load: ~42 MW**

**Power Distribution:**
- 72x Delta 800A STS (**18 MORE than Building H**)
- 72x Delta 800A Busway
- 16x Delta 600A Busway (**42 FEWER than H**)
- 2x Delta 400A Busway
- 72x 63A PIU
- 1,108 LF (338 m) EAE 4000A Reserve Busduct
- 72x EAE 800A Reserve Busduct Tap Boxes

### Mechanical Systems

**Chiller Plant:**
- **30x JCI 500-ton chillers** (1,758 kW each) (IDENTICAL to H)
- **Total Cooling: 15,000 tons (52,750 kW)** = ~18 MW
- **4x Wendland 30,000 gal (114 m³) VERTICAL thermal storage tanks** (vs HORIZONTAL in H)
- **30x Fisen chilled water pump skids**
- **1,200x Danfoss 2" (50mm) quick-connect couplers**

**Air Distribution:**
- **38x JCI 72K CFM (122,400 m³/h) fan walls** (10 fewer than H)
- 2x AAON RQA-011 DOAS
- 4x Condair RS-030 humidifiers
- 2x Dadex 60kW CRAH (data hall)
- 4x Dadex 60kW CRAH (MMR)

**IT/Mechanical Modules:**
- **21x MCFI IT Modules** (IDENTICAL to H)
- **10x MCFI Mechanical Modules** (IDENTICAL to H)

### Electrical Infrastructure

**Transformers:**
- **21x JCL Energy 2550kVA 34.5kV KNAN** (IDENTICAL to H)
- **10x JCL Energy 2550kVA 34.5kV KNAF** (IDENTICAL to H)
- **Total: 31 transformers = 79 MVA**

**Generators:**
- **4x Kohler 3MW generators** (vs 18x 1.25MW in H)
- **Total Generator Capacity: 12 MW** (vs 22.5 MW in H)
- **CRITICAL DIFFERENCE: 50% less generator capacity than H**

### Equipment Counts - Building C

| Category | Equipment Type | Quantity | Difference from H |
|----------|----------------|----------|-------------------|
| **UPS Systems** | 1250kVA UPS | 42 | SAME |
| | 250kVA UPS | 30 | SAME |
| **Static Transfer** | 800A STS | 72 | **+18 more STS** |
| **Power Distribution** | 800A Busway | 72 | +18 |
| | 600A Busway | 16 | **-42 fewer** |
| | 400A Busway | 2 | SAME |
| **Transformers** | 2550kVA (total) | 31 | SAME |
| **Generators** | 3MW Kohler Gen | 4 | **-14 fewer units** |
| | | | **-10.5 MW less capacity** |
| **Chillers** | 500-ton (1,758 kW) chillers | 30 | SAME |
| **Thermal Storage** | 30K gal (114 m³) VERTICAL | 4 | **Different orientation** |
| **Pumps** | CW Pump Skids | 30 | SAME |
| **Quick Connects** | 2" (50mm) Couplers | 1,200 | SAME |
| **Fan Walls** | 72K CFM (122,400 m³/h) | 38 | **-10 fewer** |
| **DOAS** | AAON units | 2 | SAME |
| **Modular** | IT Modules | 21 | SAME |
| | Mech Modules | 10 | SAME |
| **TOTAL MAJOR EQUIPMENT** | | **~395 units** | **-45 fewer than H** |

### Building C - Commissioning Implications

**Advantages:**
1. **Fewer generators** - Only 4 vs 18 in H (simpler generator Cx)
2. **Fewer fan walls** - 38 vs 48 (less airside testing)
3. **Proven design** - Buildings F, G, D will be complete before C Cx starts
4. **Smaller equipment count** - 395 vs 440 major items

**Challenges:**
1. **D-C Courtyard sharing** - Equipment setting through 1/8/26 during Cx prep
2. **B-C Courtyard sharing** - Mezz equipment coordination
3. **More STS units** - 72 vs 54 (18 more dual-source transfer tests)
4. **Chiller piping on C mezz** - Critical path 1/9-1/31/26
5. **Vertical thermal tanks** - Different configuration than H (different test approach)

**Interdependencies:**
- **D-C Courtyard:** Shared equipment yards between Buildings D & C
- **B-C Courtyard:** Shared courtyard space and crane operations
- **C Mezz chiller piping:** Pred on mezz equipment setting (1/9-1/31/26)

**Estimated Cx Duration:**
- **L4 Functional Testing:** 18-20 days (vs 14 planned)
- **L5 Integrated Testing:** 5-7 days (vs 5 planned)
- **Contingency needed:** 6-8 days beyond plan

---

## BUILDING F - DETAILED ANALYSIS

### IT Load Capacity

**UPS Configuration:**
- **42x Delta 1250kVA UPS units** = 52.5 MVA total
- **30x Delta 250kVA UPS units** = 7.5 MVA total
- **Total UPS: 60 MVA / ~48 MW**
- **Estimated IT Load: ~42 MW**

**Power Distribution:**
- **72x Delta 800A STS** (IDENTICAL to C)
- 72x Delta 800A Busway
- 16x Delta 600A Busway
- 2x Delta 400A Busway
- 72x 63A PIU
- 1,095 LF (334 m) EAE 4000A Reserve Busduct
- 72x EAE 800A Reserve Busduct Tap Boxes

### Mechanical Systems

**Chiller Plant:**
- **30x JCI 500-ton chillers** (1,758 kW each) (IDENTICAL to C & H)
- **Total Cooling: 15,000 tons (52,750 kW)**
- **4x Wendland 30,000 gal (114 m³) VERTICAL thermal storage tanks**
- **30x Fisen chilled water pump skids**
- **1,200x Danfoss 2" (50mm) quick-connect couplers**

**Air Distribution:**
- **38x JCI 72K CFM (122,400 m³/h) fan walls** (IDENTICAL to C)
- 2x AAON RQA-011 DOAS
- 8x Condair RS-030 humidifiers (**DOUBLE C & H**)
- 2x Dadex 60kW CRAH (data hall)
- 4x Dadex 60kW CRAH (MMR)

**IT/Mechanical Modules:**
- **21x MCFI IT Modules**
- **10x MCFI Mechanical Modules**

### Electrical Infrastructure

**Transformers:**
- **21x Giga Energy 2550kVA 18kV KNAN** (**DIFFERENT VOLTAGE vs C/H 34.5kV**)
- **10x Giga Energy 2550kVA 18kV KNAF** (**DIFFERENT VOLTAGE**)
- **Total: 31 transformers = 79 MVA**
- **CRITICAL: 18kV vs 34.5kV - DIFFERENT UTILITY VOLTAGE**

**Generators:**
- **8x CAT 1.25MW generators** (vs 18 in H, 4 in C)
- **Total Generator Capacity: 10 MW**
- 4x Point Eight Power 1.25MW CAT switchboards

### Equipment Counts - Building F

| Category | Equipment Type | Quantity | Difference from H | Difference from C |
|----------|----------------|----------|-------------------|-------------------|
| **UPS Systems** | 1250kVA UPS | 42 | SAME | SAME |
| | 250kVA UPS | 30 | SAME | SAME |
| **Static Transfer** | 800A STS | 72 | +18 | SAME as C |
| **Power Distribution** | 800A Busway | 72 | +18 | SAME |
| | 600A Busway | 16 | -42 | SAME as C |
| **Transformers** | 2550kVA **18kV** | 31 | **DIFF VOLTAGE** | **DIFF VOLTAGE** |
| **Generators** | 1.25MW CAT Gen | 8 | **-10 fewer** | **+4 more than C** |
| | | | **-12.5 MW less** | **-2 MW less than C** |
| **Chillers** | 500-ton (1,758 kW) | 30 | SAME | SAME |
| **Thermal Storage** | 30K gal (114 m³) VERT | 4 | DIFFERENT | SAME as C |
| **Pumps** | CW Pump Skids | 30 | SAME | SAME |
| **Quick Connects** | 2" (50mm) Couplers | 1,200 | SAME | SAME |
| **Fan Walls** | 72K CFM (122,400 m³/h) | 38 | -10 | SAME as C |
| **Humidifiers** | RS-030 units | 8 | **+4 more (DOUBLE)** | **+4 more** |
| **DOAS** | AAON units | 2 | SAME | SAME |
| **Modular** | IT Modules | 21 | SAME | SAME |
| | Mech Modules | 10 | SAME | SAME |
| **TOTAL MAJOR EQUIPMENT** | | **~403 units** | **-37 fewer than H** | **+8 more than C** |

### Building F - Commissioning Implications

**Advantages:**
1. **North Campus** - Completely isolated from south campus (D, C, B, H)
2. **No shared courtyards** - Independent equipment yards
3. **First large building** - Sets baseline for B, C, D, H (but also inherits unknowns)
4. **Early completion** - 1/22/26 handoff = earliest revenue
5. **Standalone infrastructure** - Minimal interdependencies

**Challenges:**
1. **18kV utility voltage** - Different from 34.5kV used in C, D, H (different test procedures)
2. **Giga Energy transformers** - Different OEM than JCL Energy (C, D, H) or VTC (D)
3. **8 humidifiers** - Double the count of C/H (more BMS integration points)
4. **8 generators** - More than C (4) but fewer than H (18)
5. **First to prove modular integration** - IT/Mech modules untested on this campus

**Unique Characteristics:**
- **North Campus MV voltage:** 18kV (vs 34.5kV South Campus)
- **Building G nearby:** Also 18kV, smaller (10 MW) - will commission first
- **Isolation advantage:** No crane conflicts, courtyard sharing, or south campus construction noise

**Estimated Cx Duration:**
- **L4 Functional Testing:** 18-22 days (vs 14 planned)
- **L5 Integrated Testing:** 5-7 days (vs 3 planned)
- **Contingency needed:** 8-12 days beyond plan

---

## COMPARATIVE ANALYSIS: H vs C vs F

### Equipment Complexity Matrix

| System | Building H | Building C | Building F | Cx Priority |
|--------|-----------|-----------|-----------|-------------|
| **UPS/STS** | 42+30 UPS, 54 STS | 42+30 UPS, 72 STS | 42+30 UPS, 72 STS | CRITICAL |
| **Generators** | 18x 1.25MW (22.5MW) | 4x 3MW (12MW) | 8x 1.25MW (10MW) | CRITICAL |
| **MV Transformers** | 31x 34.5kV | 31x 34.5kV | 31x **18kV** | CRITICAL |
| **Chillers** | 30x 500T | 30x 500T | 30x 500T | CRITICAL |
| **Fan Walls** | **48 units** | 38 units | 38 units | HIGH |
| **Thermal Storage** | 4x 30K gal HORIZ | 4x 30K gal VERT | 4x 30K gal VERT | MEDIUM |
| **Humidifiers** | 4 units | 4 units | **8 units** | MEDIUM |
| **Modular Units** | 21 IT + 10 Mech | 21 IT + 10 Mech | 21 IT + 10 Mech | VERY HIGH |
| **Quick Connects** | 1,200 | 1,200 | 1,200 | LOW |

### Interdependency Assessment

| Building | Shared Infrastructure | Conflict Risk | Independence Score |
|----------|----------------------|---------------|-------------------|
| **H** | NONE - Standalone | NONE | **10/10** ✅✅✅ |
| **F** | Shared with G (18kV MV loop only) | MINIMAL - G complete before F Cx | **9/10** ✅✅ |
| **C** | D-C courtyard, B-C courtyard, C mezz | MODERATE - crane ops, equipment setting | **5/10** ⚠️ |

### Generator Commissioning Comparison

**Building H: 18 Generators = Most Complex**
- 18x individual generator startup tests
- 18x load bank tests (if available)
- Load sharing/paralleling tests (multiple combinations)
- Transfer testing with 9 switchboards
- **Estimated: 8-10 days generator Cx**

**Building C: 4 Generators = Simplest**
- 4x individual generator startup tests
- 4x load bank tests
- Basic paralleling (if required)
- **Estimated: 3-4 days generator Cx**

**Building F: 8 Generators = Middle Ground**
- 8x individual startup tests
- 8x load bank tests
- Paralleling tests with 4 switchboards
- **Estimated: 5-6 days generator Cx**

---

## COMMISSIONING SCOPE RECOMMENDATIONS

### Critical Cx Systems (All Buildings)

**1. UPS & Power Distribution (HIGHEST PRIORITY)**
- 72 UPS units per building (42x 1250kVA + 30x 250kVA)
- 54-72 STS units (dual-source transfer testing)
- Busway/busduct distribution verification
- Reserve power distribution tap-box verification
- **Est. Duration: 8-10 days**

**2. Generator & Emergency Power**
- H: 18 generators (8-10 days Cx)
- C: 4 generators (3-4 days Cx)
- F: 8 generators (5-6 days Cx)
- **Includes:** Load testing, paralleling, ATS operation, load shedding

**3. Chiller Plant & Thermal Distribution**
- 30 chillers per building
- Chiller sequencing and optimization
- Thermal storage integration
- 30 pump skids per building
- 1,200 quick-connect couplers (leak testing, flow verification)
- **Est. Duration: 7-9 days**

**4. Air Distribution & HVAC Controls**
- H: 48 fan walls (most complex)
- C/F: 38 fan walls each
- DOAS integration and controls
- Humidifier operation (F has 8 vs 4 in C/H)
- Data hall environmental monitoring
- **Est. Duration: 5-7 days**

**5. Modular Equipment Integration**
- 21 IT modules per building
- 10 Mechanical modules per building
- **Factory testing completion verification**
- **Field integration and controls handshake**
- **Est. Duration: 5-7 days**

**6. Integrated Systems Testing (L5)**
- Full load simulation (if possible)
- Failover scenarios (utility loss, chiller loss, etc.)
- Cascade failure testing
- Load shedding verification
- **Est. Duration: 7-10 days**

---

## INFRASTRUCTURE INTERDEPENDENCIES

### Medium Voltage (MV) Distribution

**North Campus (18kV):**
- Building F
- Building G
- **Shared 18kV loop** - but separate feeders to each building
- **Risk:** Minimal - G completes before F commissioning

**South Campus (34.5kV):**
- Building B
- Building C
- Building D
- Building H
- **Shared 34.5kV loop** - multiple buildings on same distribution
- **Risk:** MODERATE - C shares courtyard MV infrastructure with D

### Shared Chiller/Thermal Infrastructure

**Per OFE Tracker: Each building has INDEPENDENT chiller plants**
- No shared chiller central plant
- No inter-building chilled water distribution
- Each building: 30 chillers + 4 thermal tanks + 30 pump skids

**VERDICT: NO SHARED MECHANICAL INFRASTRUCTURE** ✅

### Shared Electrical Yards/Courtyards

**Building H:**
- **INDEPENDENT** - No shared yards
- Equipment yards: North, South, East, West (all H-only)

**Building F:**
- **INDEPENDENT** - North Campus isolation
- Potential crane conflicts with G (minor - G complete before F Cx)

**Building C:**
- **D-C Courtyard** - Shared equipment setting area
- **B-C Courtyard** - Shared mezz and crane operations
- **C East Yard** - Independent (good)
- **C Mezz** - Chiller piping conflicts with D (1/9-1/31/26)

---

## KEY COMMISSIONING RISKS & RECOMMENDATIONS

### Building H Risks

**HIGH RISK:**
1. **18 generators** = Most complex generator Cx of any building
2. **48 fan walls** = Most airside testing points
3. **Compressed timeline** - DATA hall energized 3/6/26, handoff 4/30/26 (55 days total)
4. **15-day flush/fill** - Longest chiller plant fill (complexity indicator)

**MITIGATION:**
- Allocate 8-10 days solely for generator Cx
- Pre-functional checklists for all 18 generators before L4 starts
- Parallel testing where possible (fan walls in zones)
- Extend L4/L5 from 19 to 27 days (use full 55-day buffer)

### Building C Risks

**MEDIUM-HIGH RISK:**
1. **D-C Courtyard conflicts** - Equipment setting through 1/8/26
2. **B-C Courtyard conflicts** - Crane operations, mezz coordination
3. **C Mezz chiller piping** - Critical path 1/9-1/31/26 (overlaps early Cx prep)
4. **72 STS units** - 18 more than H (more dual-source transfer tests)

**MITIGATION:**
- Early coordination with D and B construction teams
- Pre-Cx access to independent systems (C East Yard ready 2/5/26)
- Phased Cx approach: East Yard → South Wall → Courtyard → Mezz
- Add 6-8 days contingency for coordination delays

### Building F Risks

**MEDIUM RISK:**
1. **18kV voltage different from other buildings** - unique test procedures
2. **Giga Energy transformers** - different OEM, need vendor support
3. **First large building Cx** - no prior campus lessons learned yet
4. **8 humidifiers** - double other buildings (more BMS integration)

**MITIGATION:**
- Observe Building G Cx first (also 18kV, completes 12/27/25)
- Pre-qualified test procedures for 18kV equipment
- QA/QC review of Giga Energy factory test reports (factory witness testing NOT in our scope)
- Early BMS programming review for humidifier integration

---

## UNKNOWN FACTORS (REQUIRE DRAWING REVIEW)

**Cannot determine from OFE Tracker alone:**

1. **IT rack configuration** - kW/rack density, hot aisle/cold aisle layout
2. **Data hall architecture** - modular vs monolithic, zone divisions
3. **BMS/EPMS architecture** - extent of building automation integration
4. **Fire protection systems** - VESDA, preaction, FM-200 scope
5. **Physical security systems** - access control, CCTV integration with Cx
6. **Backup power hierarchy** - which loads on UPS vs generator vs utility only
7. **Electrical one-line diagrams** - fault coordination, protective relay settings
8. **Chilled water flow diagrams** - primary/secondary pumping, bypass strategy
9. **Roof/building envelope** - impact on mechanical equipment placement
10. **Site/civil constraints** - access limitations, crane paths, staging areas

**REQUEST:** Provide electrical one-lines, mechanical flow diagrams, and site plans for complete assessment.

---

## COMMISSIONING DURATION ESTIMATES (REVISED)

### Building H (Most Complex)

| Phase | Planned | Recommended | Buffer |
|-------|---------|-------------|--------|
| **Pre-Cx (observation)** | - | 60 days | Dec 1 → Mar 6 |
| **L4 Functional Testing** | 14 days | 22 days | +8 days |
| **L5 Integrated Testing** | 5 days | 10 days | +5 days |
| **Post-Cx buffer** | 36 days | 23 days | -13 days used |
| **TOTAL to Handoff** | 55 days | 55 days | ✅ Fits in buffer |

**Recommendation:** Use full 55-day buffer. Schedule L4/L5 as 32 days total (vs 19 planned).

### Building C (Medium-High Complexity)

| Phase | Planned | Recommended | Buffer |
|-------|---------|-------------|--------|
| **L4 Functional Testing** | 14 days | 20 days | +6 days |
| **L5 Integrated Testing** | 5 days | 7 days | +2 days |
| **Post-Cx buffer** | 20 days | 12 days | -8 days used |
| **TOTAL to Handoff** | 39 days | 39 days | ✅ Fits in buffer |

**Recommendation:** Extend L4/L5 to 27 days total (vs 19 planned). Coordinate D-C courtyard access early.

### Building F (Medium Complexity)

| Phase | Planned | Recommended | Buffer |
|-------|---------|-------------|--------|
| **L4 Functional Testing** | 14 days | 20 days | +6 days |
| **L5 Integrated Testing** | 3 days | 7 days | +4 days |
| **Post-Cx buffer** | 28 days | 18 days | -10 days used |
| **TOTAL to Handoff** | 45 days | 45 days | ✅ Fits in buffer |

**Recommendation:** Extend L4/L5 to 27 days total (vs 17 planned). Leverage G lessons learned.

---

## FINAL RECOMMENDATION FOR CxA

### Based on Equipment Analysis:

**Primary: Building H**
- Most buffer time (55 days)
- Complete independence (no courtyard conflicts)
- Largest equipment count = highest Cx fee potential
- 18 generators = substantial scope
- Can observe 5 buildings before starting

**Secondary: Building F**
- North Campus independence
- Early completion = faster revenue
- Different voltage (18kV) = unique technical challenge
- Can observe G immediately (completes 12/27/25)
- Smallest generator scope (8 units) = lower complexity

**Tertiary: Building C**
- Middle timeline (adequate buffer)
- Courtyard conflicts reduce independence score
- Same configuration as B, D = proven approach
- 4 generators only = simplest generator Cx

### Equipment Complexity Ranking:

1. **H: Most Complex** (440 major items, 18 generators, 48 fan walls)
2. **F: Medium-High** (403 items, 8 generators, 8 humidifiers, unique 18kV)
3. **C: Medium** (395 items, 4 generators, courtyard conflicts)

### Recommendation Aligns with Priority Analysis:

**Building H remains the top choice** based on:
1. ✅ Maximum buffer (55 days)
2. ✅ Complete independence (10/10)
3. ✅ Largest scope = highest Cx value
4. ✅ December 1 mobilization feasible (3 months observation)

---

## NEXT STEPS

1. **Request additional documents:**
   - Electrical one-line diagrams (all buildings)
   - Mechanical flow diagrams (chilled water, condenser water)
   - BMS/EPMS architecture drawings
   - Site plan with equipment yard layouts
   - Data hall layout drawings (IT rack densities)

2. **Clarify with client:**
   - Is multi-building Cx bid acceptable?
   - What is exact Cx scope (IST, FPT, or both)?
   - Are there owner Cx procedures or shall we develop?
   - Load bank availability for generator testing?
   - Client expectations for modular equipment Cx (factory vs field)

3. **Vendor coordination:**
   - MCFI (modular) - what testing completed at factory?
   - Delta (UPS/STS) - vendor support availability?
   - JCI (chillers) - startup services included?
   - CAT/Kohler (generators) - commissioning support?

4. **Develop detailed Cx plan:**
   - Building H: 32-day L4/L5 schedule
   - Test procedure outline (UPS, STS, generators, chillers)
   - Resource loading (staff requirements)
   - Pricing with equipment-based scope
