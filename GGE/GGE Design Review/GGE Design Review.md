# Biliki Data Center Design Review

**Project**: Data Center "Biliki" - GGE  
**Review Date**: October 28, 2025  
**Documents Reviewed**:
- GE01-CAS-0003-AR5-C02 (Master Plan)
- GE01-CAS-0003-FL5-B1-C02 (Basement Level -1 Floor Plan)
- GE01-CAS-0003-FL6-L1-C02 (Ground Floor Plan)

---
## Executive Summary

This review identified 15 critical concerns, multiple omissions, and documentation quality issues that require resolution before proceeding to construction documentation. The designs appear to be at schematic level and require substantial development in coordination with MEP, structural, and IT infrastructure specialists.

---
## Critical Concerns

### 1. Fire Suppression System Misspelling (All Documents)
**Severity**: Medium  
**Issue**: Consistent misspelling of "suppression" as "supperstion" throughout all documents

**Locations**:
- Room labels: "Fr - Fire supperstion systems"
- "Tch - Technical room (Fire supperstion systems)"

**Impact**: 
- Professional credibility issue
- Could cause confusion in construction documents
- May lead to specification errors

**Standard Reference**: Basic technical documentation quality standards

**Recommendation**: Global find-and-replace correction in all project documents

---

### 2. Area Calculation Discrepancies (FL5-B1)
**Severity**: High  
**Issue**: Floor area summary shows mathematical inconsistency

**Data**:
- Floor gross area: 4,142 sq m
- Floor usable area: 3,863 sq m
- Sum of individual zones: 3,764.52 sq m
- **Discrepancy**: ~98.5 sq m unaccounted for (2.5% of usable area)

**Impact**: 
- Budget and material estimation errors
- HVAC load calculations may be incorrect
- Construction cost discrepancies

**Standard Reference**: BOMA (Building Owners and Managers Association) measurement standards

**Recommendation**: 
- Reconcile all area calculations
- Provide circulation factor documentation
- Add wall thickness and shaft area accounting

---

### 3. Transformer Capacity Labeling Inconsistency (FL5-B1)
**Severity**: High  
**Issue**: Transformer rooms labeled as "Dry Tr (3000 kVA)" but relationship to load unclear

**Concerns**:
- Generator sets rated at 2500 kVA
- Need verification that 3000 kVA transformers are adequate
- No diversity factor or load calculation documentation
- Transformer type (dry-type) may have derating factors

**Standard Reference**: 
- IEEE C57.12.01 (Transformer Standards)
- NEC Article 450 (Transformers)

**Recommendation**: 
- Provide electrical load calculations
- Show transformer sizing methodology
- Consider future expansion capacity

---

### 4. UPS/Battery Room Sizing Concerns (FL5-B1 & FL6-L1)
**Severity**: High  
**Issue**: Battery and UPS rooms lack specification details

**Data**:
- Battery rooms (BT): 68.97-72.13 m� per room (Phase 1)
- UPS rooms: 32.61-35.65 m� per room
- Multiple rooms shown but no redundancy notation

**Missing Information**:
- Battery backup duration (typically 15-30 minutes for data centers)
- Battery type (VRLA, Li-ion, etc.)
- UPS topology (online double-conversion, rotary, etc.)
- Redundancy configuration (N, N+1, 2N)
- Maintenance bypass provisions

**Standard Reference**: 
- ANSI/TIA-942 Tier classification requirements
- IEEE 946 (Recommended Practice for the Design of DC Power Systems)
- Uptime Institute Tier Standards

**Recommendation**: 
- Specify battery runtime at full load
- Document redundancy configuration
- Add single-line diagrams showing UPS topology
- Consider thermal management requirements

---

### 5. Missing Generator Set Specifications (FL5-B1)
**Severity**: High  
**Issue**: Generator rooms labeled "GS (2500 kVA)" without critical specifications

**Missing Information**:
- Fuel type (diesel, natural gas, dual-fuel)
- Runtime at full load (typically 48-72 hours for Tier III)
- Exhaust routing and silencer locations
- Sound attenuation requirements (dBA at property line)
- Cooling requirements (radiator vs. remote cooling)
- Day tank capacity and fuel distribution

**Site Plan Notes**:
- "Fuel Plant Underground tanks & distribution" shown but not detailed
- Fuel plant area: 256 sq m (from site plan)
- No connection shown between fuel plant and generator rooms

**Standard Reference**: 
- NFPA 110 (Emergency and Standby Power Systems)
- ISO 8528 (Reciprocating Internal Combustion Engine Driven Alternating Current Generating Sets)

**Recommendation**: 
- Provide generator specifications
- Show fuel distribution piping
- Document day tank and bulk storage capacity
- Show exhaust routing and silencer locations
- Add acoustic analysis for noise compliance

---

### 6. Cooling System Undefined (FL6-L1)
**Severity**: Critical  
**Issue**: No visible cooling equipment rooms on ground floor despite substantial IT load

**Data**:
- Total IT room area: ~2,786 sq m
- Quantum room: 465.89 sq m (80 racks)
- Enterprise rooms: 242.47 sq m + 158.81 sq m + 93.26 sq m (132 racks total)
- VIP rooms: 5 rooms totaling ~379 m (80 racks total)
- HUB room: 388.08 sq m (rack count not specified)

**Concerns**:
- No CRAC/CRAH unit locations shown
- No chiller locations (may be on roof or external)
- Cooling capacity calculations not provided
- Heat rejection method unclear
- Water source from "Cooling Reservoir and pump room" noted on site plan but connection not shown

**Typical Requirements**:
- Data center cooling: 1:1 or higher IT:cooling space ratio
- Hot aisle/cold aisle containment not indicated
- Raised floor plenum depth not specified
- Design temperatures typically 18-27C, 40-60% RH

**Standard Reference**: 
- ASHRAE TC 9.9 (Thermal Guidelines for Data Processing Environments)
- ASHRAE 90.4 (Energy Standard for Data Centers)

**Recommendation**: 
- Provide mechanical plans showing HVAC distribution
- Document cooling capacity calculations
- Show redundancy configuration (N+1, N+2)
- Specify hot aisle/cold aisle containment strategy
- Show water distribution from cooling reservoir

---

### 7. "Quantum" IT Room Classification (FL6-L1)
**Severity**: High  
**Issue**: Room labeled "IT Room (QUANTUM)" appears to be misclassified

**Data**:
- Area: 465.89 sq m (largest single IT room)
- Capacity: 80 racks
- Height: 3.5m
- Label: "CR AI" (Computer Room AI/Quantum)

**Technical Concerns**:
True quantum computing requires:
- Extreme temperature control (near absolute zero, 10-15 millikelvin)
- Dilution refrigerators or cryogenic systems
- Vibration isolation platforms
- Electromagnetic shielding (Faraday cage)
- Specialized power conditioning
- Completely different infrastructure from standard racks

**Likely Interpretation**:
- This is probably High Performance Computing (HPC) or AI/ML computing
- May involve GPU-dense servers for quantum simulation
- Higher power density than standard enterprise computing

**Standard Reference**: 
- No standard exists for quantum computing facilities
- If HPC: DOE Best Practices for HPC Data Centers

**Recommendation**: 
- Clarify room purpose (Quantum Computing vs. Quantum Simulation/HPC)
- If true quantum: Complete redesign required
- If HPC/AI: Specify power density (kW/rack), typically 10-30 kW/rack
- Document cooling requirements
- Show power distribution topology

---

### 8. Electrical Redundancy Path Unclear (FL5-B1)
**Severity**: Critical  
**Issue**: Phase 1 and Phase 2 electrical equipment shown but redundancy topology not documented

**Observations**:
- Phase 1: 4 generator sets, transformers, UPS systems, battery rooms
- Phase 2: Duplicate infrastructure shown
- No indication of:
  - Automatic Transfer Switch (ATS) locations
  - Bus tie breaker positions
  - Distribution redundancy (A/B feeds)
  - Failure mode operation

**Missing Documentation**:
- Single-line electrical diagram
- N, N+1, or 2N redundancy configuration
- Concurrent maintainability provisions
- Fault isolation strategy

**Standard Reference**: 
- Uptime Institute Tier Standards
  - Tier I: N (no redundancy)
  - Tier II: N+1 (single path, redundant components)
  - Tier III: N+1 (dual path, concurrently maintainable)
  - Tier IV: 2N (fault tolerant)
- TIA-942 Data Center Standards

**Recommendation**: 
- Provide electrical single-line diagrams
- Document target Tier level
- Show all ATS locations and switching logic
- Demonstrate concurrent maintainability
- Show failure mode analysis

---

### 9. Meet Me Room (MMR) Access Path (FL6-L1)
**Severity**: Medium  
**Issue**: MMR locations shown but carrier entry pathway not clearly marked

**Data**:
- MMR-1: 72.12 sq m (4 racks)
- MMR-2: 27.12 sq m (4 racks)
- Both on ground floor

**Missing Information**:
- Telecommunications carrier entry point
- Fiber entrance facility (manhole to building entry)
- Cable tray routing from entrance to MMRs
- Provider diversity paths (separate conduits)
- Number of conduits and size

**Typical Requirements**:
- Minimum 2 diverse carrier entry points (geographic diversity)
- 4-6" conduits per carrier
- Separate secure access for carrier technicians
- Cross-connect documentation

**Standard Reference**: 
- TIA-942 Section 5.5 (Entrance Room/Space requirements)
- TIA-569 (Telecommunications Pathways and Spaces)

**Recommendation**: 
- Show carrier entry points on site plan
- Document conduit routing to property line
- Provide diverse path analysis
- Show separation from power systems (avoiding EMI)
- Add carrier access security provisions

---

### 10. Security Zoning Unclear (FL6-L1)
**Severity**: Medium  
**Issue**: Multiple security spaces shown but security perimeter not delineated

**Security Spaces Identified**:
- Security Hall: 65.33 sq m
- Security office: 17.00 sq m
- Security office: 33.81 sq m
- Security schluss: 33.50 sq m
- VIP Hall: 39.10 sq m
- VIP Entrance Hall: 256.14 sq m

**Missing Information**:
- Security zones (public, semi-secure, secure, critical)
- Mantrap locations
- CCTV coverage zones
- Access control points between zones
- Biometric authentication locations
- Security monitoring center (NOC/SOC)

**Typical Requirements**:
- Minimum 3 security zones
- Mantraps at critical boundaries
- Two-factor authentication for IT spaces
- Separate customer access paths

**Standard Reference**: 
- ISO 27001 Annex A.11 (Physical and Environmental Security)
- PCI DSS Physical Security Requirements
- TIA-942 Section 5.3 (Security)

**Recommendation**: 
- Provide security zoning diagram
- Show all access control points
- Document authentication requirements per zone
- Show CCTV camera coverage
- Add security desk location and sight lines

---

### 11. Georgian Text on Site Plan (AR5)
**Severity**: Low  
**Issue**: Site survey data includes Georgian language labels

**Examples**:
- "nayari betoni" (appears multiple times)
- "??. ???" (Georgian script)
- "????" (Georgian script)
- Mixed with English labels

**Concerns**:
- International contractors may not understand labels
- Potential for misinterpretation during construction
- BIM/CAD standards typically require single language

**Standard Reference**: 
- ISO 128 (Technical Drawings - General Principles)
- Construction document clarity standards

**Recommendation**: 
- Provide bilingual legend
- Create English-only construction set
- Or fully translate all labels to English
- Maintain Georgian version for local approvals

---

### 12. Hydropower Integration (AR5)
**Severity**: High  
**Issue**: 3.7 MW HPP (Hydropower Plant) shown but integration unclear

**Site Plan Notes**:
- Item 9: "Hydropower Dam  3.7 MW HPP (Mtkvari)"
- "HPPT - Utility tunnel between HPP and DC" shown (259.59 sq m)

**Missing Information**:
- Electrical integration with data center
- Power quality characteristics (voltage, frequency stability)
- Reliability data (seasonal flow variations)
- Switchover logic between HPP and grid power
- Whether HPP is primary or supplemental power
- Dam failure risk assessment

**Technical Concerns**:
- Data centers require 99.99%+ uptime
- Hydropower varies with seasonal water flow
- Power quality may not meet IT equipment standards
- Need UPS to buffer HPP variability

**Standard Reference**: 
- IEEE 1547 (Interconnection and Interoperability Standards)
- IEC 61850 (Communication Networks for Power Systems)

**Recommendation**: 
- Provide electrical one-line showing HPP integration
- Document power quality analysis
- Show UPS protection from HPP transients
- Provide hydrological study (minimum flow rates)
- Document grid vs. HPP prioritization logic
- Consider HPP as supplemental/renewable credit only

---

### 13. Stair Riser/Tread Specifications Vary
**Severity**: Medium  
**Issue**: Inconsistent stair dimensions across building

**Stair Specifications Found**:
1. 32R  0.163m / 31G  0.325m (riser 163mm, tread 325mm)
2. 32R  0.172m / 31G  0.306m (riser 172mm, tread 306mm)
3. 30R  0.183m / 29G  0.283m (riser 183mm, tread 283mm)
4. 34R  0.159m / 33G  0.317m (riser 159mm, tread 317mm)

**Concerns**:
- Varying riser heights create trip hazard
- 183mm riser exceeds some code maximums
- Inconsistency indicates design coordination issue

**Code Requirements (Typical)**:
- IBC 1011.5.2: Max riser 7" (178mm), Min 4" (102mm)
- IBC 1011.5.2: Min tread 11" (279mm)
- Riser/tread relationship: 2R + T = 24"-25" (610-635mm)

**Analysis**:
- Stair #3 (183mm riser) **exceeds IBC maximum**
- Tread depths below IBC minimum in some cases
- Inconsistency suggests copy/paste errors or multiple designers

**Standard Reference**: 
- IBC (International Building Code) 1011.5
- Georgian National Building Codes
- EN 12464 (European Standard)

**Recommendation**: 
- Standardize all stairs to single riser/tread dimension
- Verify compliance with Georgian building codes
- Check 2R + T formula for comfortable stairs
- Review accessibility requirements

---

### 14. Elevator Capacities (FL5-B1 & FL6-L1)
**Severity**: Medium  
**Issue**: Limited elevator capacity and redundancy

**Elevator Inventory**:
- 1 3-ton freight elevator
- 2 10-ton freight elevators
- 1 10-passenger elevator

**Concerns**:
- Single passenger elevator for entire facility
- No passenger elevator redundancy (facility access during maintenance)
- 10-ton elevators adequate for server racks (typical 42U rack  1-2 tons loaded)
- But may be undersized for large infrastructure (transformers, chillers)

**Typical Requirements**:
- Mission-critical facilities: N+1 passenger elevators
- Freight elevator capacity for heaviest single component
- Consider transformer/generator maintenance (may require crane)

**Standard Reference**: 
- ASHRAE recommendations for equipment access
- IBC accessibility requirements

**Recommendation**: 
- Consider second passenger elevator or document operational procedure during maintenance
- Verify 10-ton capacity adequate for all equipment moves
- Show rigging paths for oversized equipment
- Consider outdoor crane pad for major equipment

---

### 15. Missing Fire Detection/Suppression Details
**Severity**: High  
**Issue**: Fire suppression system rooms shown but system design undefined

**Fire System Rooms**:
- 2 Fire suppression system rooms: 37.96 sq m and 45.57 sq m
- Labeled "Fr - Fire supperstion systems" [sic]

**Missing Information**:
- Suppression agent type:
  - FM-200 (HFC-227ea)
  - Novec 1230
  - Inergen (IG-541)
  - Water-based pre-action
- VESDA (Very Early Smoke Detection Apparatus) coverage
- Pre-action system staging and zones
- Agent storage requirements
- Discharge time requirements
- Personnel egress considerations

**Typical Requirements**:
- Data centers: Gaseous suppression in IT spaces
- VESDA for earliest possible detection
- Pre-action dry pipe to prevent accidental water discharge
- Zone-based suppression (individual rooms)
- Emergency power off (EPO) integration

**Standard Reference**: 
- NFPA 75 (Fire Protection of Information Technology Equipment)
- NFPA 76 (Fire Protection of Telecommunications Facilities)
- NFPA 2001 (Clean Agent Fire Extinguishing Systems)

**Recommendation**: 
- Specify suppression agent and justify selection
- Provide fire detection/suppression riser diagram
- Show VESDA aspirator locations
- Document discharge time and agent quantity
- Show integration with HVAC shutdown
- Provide egress analysis with suppression discharge

---

## Omissions

### Critical Omissions

1. **No Legend for Colored Zones** - Floor plans show color-coded zones (orange, blue, pink, yellow, green) with no legend
2. **No Voltage Specifications** - Electrical distribution voltages not specified (110/208V, 415/240V, 480/277V)
3. **No Structural Grid Load Ratings** - Floor load capacity not specified (critical for equipment placement)
4. **No Cable Tray/Raceway Paths** - Fiber and copper distribution routing not shown
5. **No Emergency Egress Calculations** - Occupancy load factors and exit capacity not calculated
6. **No HVAC Ductwork or Piping Routing** - Mechanical systems not coordinated with floor plan
7. **No Seismic Design Information** - Critical for Georgia (moderate seismic activity)
8. **No Grounding/Lightning Protection System** - Critical for data center uptime
9. **No Water Detection System** - Despite water-based cooling systems
10. **Fuel Plant Details Missing** - Site plan shows 256 sq m but no detail drawings

### Design Development Omissions

11. **No IT Load Density Specifications** - kW per rack not specified
12. **No Redundancy Topology Diagrams** - Electrical single-line and cooling redundancy missing
13. **No Room Data Sheets** - Detailed room requirements not documented
14. **No Equipment Schedules** - Specifications for all major equipment missing
15. **No Phasing Plan Detail** - Phase boundaries and operational impacts unclear
16. **No BMS/DCIM Integration** - Building Management System strategy undefined
17. **No Commissioning Plan Reference** - Critical systems testing not documented
18. **No Maintenance Access** - Equipment clearances not verified
19. **No Renewable Energy Integration Detail** - Solar canopy integration not shown
20. **No Water Usage/Efficiency Strategy** - Consumption and treatment not documented

---

## Standards Compliance Checklist

### Primary Standards Referenced

- ? **TIA-942**: Data Center Standards (needs full compliance review)
- ?? **Uptime Institute Tier Standards**: Tier level not declared
- ?? **ISO 27001**: Physical security needs development
- ?? **ASHRAE TC 9.9**: Cooling design undefined
- ?? **NFPA 75/76**: Fire protection needs detail
- ?? **IBC**: Building code compliance needs verification
- ?? **IEEE Standards**: Electrical design needs documentation
- ? **LEED/Green Building**: Not referenced

### Additional Standards to Consider

- **ISO 50001**: Energy management
- **ISO 22301**: Business continuity
- **EN 50600**: European data center standards
- **Georgian National Building Codes**: Local compliance
- **PCI DSS**: If payment card data processed
- **GDPR/Data Protection**: If EU data stored

---

## Risk Assessment Summary

### High-Priority Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Cooling system undersized | Facility shutdown | High | Develop mechanical design immediately |
| Electrical redundancy inadequate | Downtime during maintenance | Medium | Document redundancy topology |
| Area calculations incorrect | Cost overruns | Medium | Reconcile all calculations |
| Fire suppression inadequate | Equipment damage, liability | Low | Complete fire protection engineering |
| Seismic vulnerability | Structural failure | Medium | Conduct seismic analysis |
| Hydropower unreliability | Power interruptions | Medium | Document UPS protection strategy |

### Medium-Priority Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Security zones unclear | Unauthorized access | Medium | Develop security master plan |
| Stair code non-compliance | Construction delays | Medium | Verify and standardize stair design |
| Elevator capacity insufficient | Operational constraints | Low | Verify equipment move procedures |
| MMR access unclear | Carrier installation issues | Medium | Document carrier entrance facility |

---

## Recommendations by Phase

### Immediate Actions (Before Design Development)

1. ? **Correct all spelling errors** ("supperstion" ? "suppression")
2. ? **Reconcile area calculations** and provide documentation
3. ? **Declare target Uptime Institute Tier** level (or equivalent)
4. ? **Clarify "Quantum" room** purpose and requirements
5. ? **Develop mechanical cooling design** (critical path item)
6. ? **Create electrical single-line diagrams** showing redundancy

### Design Development Phase

7. ? **Coordinate with MEP engineers** for systems integration
8. ? **Develop structural design** with seismic analysis
9. ? **Complete fire protection engineering** with system selection
10. ? **Develop security master plan** with zoning and access control
11. ? **Create equipment schedules** with full specifications
12. ? **Develop phasing plan** with temporary services
13. ? **Document hydropower integration** with power quality analysis
14. ? **Show all cable routing** (fiber, copper, power)
15. ? **Add room data sheets** for all critical spaces

### Construction Documentation Phase

16. ? **Develop detailed MEP drawings** (not just floor plans)
17. ? **Create equipment cut sheets** and submittal packages
18. ? **Develop commissioning plan** with test procedures
19. ? **Create operations/maintenance manuals** framework
20. ? **Prepare BIM model** (if not already in use)

### Pre-Construction

21. ? **Third-party design review** (recommend independent data center consultant)
22. ? **Code compliance review** with local authorities
23. ? **Value engineering** study
24. ? **Constructability review** with contractor input

---

## Questions for Design Team

### Operational Questions

1. What is the target Uptime Institute Tier level (I, II, III, or IV)?
2. What is the target total IT load capacity (MW)?
3. What is the average and peak power density per rack (kW)?
4. What is the expected occupancy (staff count)?
5. What are the planned operating hours (24/7 or scheduled)?

### Technical Questions

6. What is the source of the 3000 kVA transformer rating?
7. What is the battery backup duration requirement?
8. What cooling technology is planned (air-cooled chillers, cooling towers, etc.)?
9. What is the role of the hydropower plant (primary, supplemental, renewable credit)?
10. What is the "Quantum" room actually for (true quantum, HPC, AI/ML)?

### Site-Specific Questions

11. What is the seismic design category for this site?
12. What are the local soil conditions and bearing capacity?
13. What is the reliability of the utility grid connection?
14. What telecommunications carriers will serve this facility?
15. Are there any environmental restrictions (water usage, noise, etc.)?

### Standards and Compliance

16. Which standards govern this project (Georgian codes, international standards)?
17. Are there any sustainability certifications targeted (LEED, BREEAM, etc.)?
18. What security certifications are required (ISO 27001, SOC 2, etc.)?
19. What is the construction schedule and phasing strategy?
20. What is the budget and cost per square meter target?

---

## Conclusion

The Biliki Data Center design documents represent a substantial project with interesting features including hydropower integration and multi-phase expansion. However, the documents are at a schematic level and require significant development before construction can begin.

**Key Takeaways**:
- ?? **Critical Systems Undefined**: Cooling, redundancy topology, and power quality need immediate attention
- ?? **Documentation Quality**: Spelling errors and calculation discrepancies need resolution
- ?? **Standards Compliance**: Tier level and compliance framework need declaration
- ?? **Coordination Required**: MEP systems need full integration with architectural plans
- ? **Good Foundation**: Site layout and space allocation appear reasonable
- ? **Phased Approach**: Two-phase design allows for expansion

**Recommended Next Steps**:
1. Engage data center design consultant for third-party review
2. Develop complete MEP design with redundancy documentation
3. Conduct standards compliance review (TIA-942, Uptime Institute)
4. Create detailed equipment specifications and schedules
5. Develop commissioning and testing procedures

**Estimated Design Completion**: These issues represent approximately 40-60% additional design effort before construction documentation is complete.

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-28 | Design Review | Initial comprehensive review |

---

*This review is based on three PDF documents and represents findings from document review only. Site inspection, utility coordination review, and stakeholder interviews may reveal additional concerns.*
