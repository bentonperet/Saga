# Uptime Institute Tier Requirements Reference

## Overview

This document provides detailed requirement matrices for Uptime Institute Tier I through Tier IV certification.

---

## Tier Comparison Matrix

| Characteristic | Tier I | Tier II | Tier III | Tier IV |
|----------------|--------|---------|----------|---------|
| **Availability** | 99.671% | 99.741% | 99.982% | 99.995% |
| **Annual Downtime** | 28.8 hours | 22.0 hours | 1.6 hours | 0.4 hours |
| **Redundancy** | N | N+1 components | N+1 distribution | 2(N+1) or 2N |
| **Distribution Paths** | Single | Single | Dual (active/passive) | Dual active |
| **Concurrent Maintainability** | No | No | Yes | Yes |
| **Fault Tolerance** | No | No | No | Yes |

---

## TIER I - Basic Capacity

### Philosophy
Single path for power and cooling distribution with no redundant components. Susceptible to disruption from both planned and unplanned events.

### Requirements

**Electrical:**
- Single utility service entrance
- Single generator (if provided)
- Single UPS module (if provided)
- Single power distribution path to loads
- N capacity (no redundancy)

**Cooling:**
- Single chiller (or multiple chillers totaling N capacity)
- Single cooling tower
- Single chilled water distribution path
- N capacity (no redundancy)

**Operations:**
- Planned shutdowns required for maintenance
- Vulnerable to unplanned failures
- Single points of failure acceptable

**Typical Applications:**
- Small server rooms
- Non-critical IT operations
- Budget-constrained facilities

---

## TIER II - Redundant Capacity Components

### Philosophy
Single path for distribution with redundant components (N+1). Some maintenance can be performed without shutdown, but distribution path maintenance requires downtime.

### Requirements

**Electrical:**
- Single utility service (or N+1 if generators sized for full load)
- N+1 generators (can lose one generator without impact)
- N+1 UPS modules (can lose one UPS without impact)
- Single distribution path (but components are redundant)
- Automatic transfer capabilities

**Cooling:**
- N+1 chillers (can lose one chiller without impact)
- N+1 cooling tower cells
- N+1 pumps (chilled water and condenser water)
- N+1 CRAH/CRAC units
- Single distribution path (piping/ductwork)

**Operations:**
- Most component maintenance without shutdown
- Distribution path maintenance requires shutdown
- Planned annual shutdown still required

**Typical Applications:**
- Enterprise data centers
- Medium-criticality operations
- Cost-sensitive projects requiring some redundancy

---

## TIER III - Concurrently Maintainable

### Philosophy
Multiple independent distribution paths with N+1 redundancy. Any single component or distribution element can be removed for maintenance without impacting IT operations.

### Requirements

**Electrical:**
- Dual utility services (geographically diverse, or single utility with N+1 generators)
- N+1 generators minimum
- N+1 UPS modules per distribution path
- **Dual power distribution paths (A-side and B-side)**
- Automatic transfer switches (ATS) at equipment level
- Isolation and bypass capabilities for all equipment

**Cooling:**
- N+1 chillers minimum
- **Dual chilled water distribution loops (A-side and B-side)**
- Isolation valves on all equipment
- N+1 pumps per distribution path
- N+1 CRAH/CRAC units per zone
- Bypass piping for chiller maintenance

**Critical Requirements:**
- **Dual distribution throughout**: Two independent paths from source to load
- **Isolation capabilities**: Every component can be isolated without load impact
- **No planned IT downtime**: All maintenance performed live
- **Active/passive or active/active**: One path can carry full load

**Maintenance Scenarios:**
The design must demonstrate ability to maintain:
1. Any UPS module (via bypass and redundancy)
2. Any generator (remaining generators carry load)
3. Any chiller (isolation valves, backup capacity)
4. Any distribution path (switchover to alternate path)

**Typical Applications:**
- Mission-critical data centers
- Financial services
- Healthcare systems
- Large cloud providers

---

## TIER IV - Fault Tolerant

### Philosophy
Multiple independent and physically isolated distribution paths configured to be fault tolerant. The infrastructure can sustain any single worst-case unplanned failure or event without impacting the critical load.

### Requirements

**Electrical:**
- **Dual diverse utility services** (geographically separated)
- **2(N+1) generators** or dual N+1 systems
- **2(N+1) UPS modules** (distributed across both paths)
- **Dual active distribution paths** (continuously powered)
- **Dual-corded equipment** with automatic failover (sub-second)
- Complete electrical isolation between A and B paths
- Independent compartments for A and B equipment

**Cooling:**
- **2(N+1) chillers** or dual N+1 systems
- **Dual independent chilled water loops** (A and B)
- **2(N+1) pumps** distributed across paths
- **Dual ductwork or piping** (physically separated)
- **Compartmentalized cooling zones** (A and B)
- Each path must independently support 100% load

**Compartmentalization:**
- **Physical separation**: A-side and B-side equipment in separate rooms/zones
- **Fire barriers**: Independent fire suppression zones
- **Access control**: Separate access to A and B infrastructure
- **No shared components**: Including controls, monitoring, grounding

**Critical Requirements:**
- **Continuous operation during any single failure**
- **Automatic fault detection and transfer** (<10ms for power)
- **No single points of failure** anywhere in the infrastructure
- **S+S distribution** (Simultaneous + Simultaneous) for power and cooling
- **Dual-corded IT equipment** throughout

**Failure Scenarios:**
The design must demonstrate survival of:
1. Complete loss of any utility service
2. Failure of any generator
3. Complete UPS path failure
4. Chiller plant failure
5. Fire suppression activation in one zone
6. Complete loss of any compartment

**Typical Applications:**
- Hyperscale cloud providers
- Global financial trading platforms
- Critical government/defense systems
- Tier IV is rare (~1% of data centers globally)

---

## Specific Design Criteria

### Electrical - Detailed Requirements

| Component | Tier I | Tier II | Tier III | Tier IV |
|-----------|--------|---------|----------|---------|
| **Utility Service** | Single | Single* | Dual or single w/ generators | Dual diverse |
| **Generators** | Optional N | N+1 | N+1 | 2(N+1) or 2×(N+1) |
| **Generator Fuel** | 12 hrs min | 24 hrs min | 48 hrs min | 96 hrs min |
| **UPS** | N | N+1 | N+1 per path (dual path) | 2(N+1) or 2×(N+1) |
| **UPS Battery** | 10 min | 15 min | 15 min | 15-20 min |
| **Distribution Paths** | Single (N) | Single (N+1) | Dual (A+B) | Dual active (S+S) |
| **PDU per Rack** | Single | Single or dual | Dual | Dual (mandatory) |
| **ATS** | Not required | Optional | Required | Required (ms transfer) |

\* Tier II allows single utility if generators sized to carry 100% load indefinitely

### Cooling - Detailed Requirements

| Component | Tier I | Tier II | Tier III | Tier IV |
|-----------|--------|---------|----------|---------|
| **Chillers** | N | N+1 | N+1 | 2(N+1) or 2×(N+1) |
| **Chilled Water Loops** | Single | Single | Dual (A+B) | Dual independent (S+S) |
| **Pumps (CHW)** | N | N+1 | N+1 per loop | 2(N+1) distributed |
| **Cooling Towers** | N | N+1 cells | N+1 cells | 2(N+1) or 2 separate systems |
| **CRAH/CRAC Units** | N | N+1 | N+1 distributed | 2×(N+1) in compartments |
| **Isolation Valves** | Not required | Recommended | Required | Required + automated |
| **Control Systems** | Single | Single | Redundant | Fully redundant + isolated |

### Concurrent Maintainability Checklist (Tier III+)

**Power Systems:**
- [ ] UPS modules can be bypassed individually
- [ ] Generators have isolation switches and fuel line valves
- [ ] Switchgear has maintenance bypass or dual bus
- [ ] PDUs can be isolated without load impact
- [ ] All distribution panels have dual feeds

**Cooling Systems:**
- [ ] Chillers have isolation valves on all connections
- [ ] Bypass piping allows chiller removal
- [ ] Pumps have isolation valves and bypass
- [ ] Cooling towers have isolation on each cell
- [ ] CRAH/CRAC units can be removed without impact

**Distribution:**
- [ ] Dual distribution paths from source to load
- [ ] Either path can carry 100% load
- [ ] No single conduit/raceway failure impacts operation
- [ ] Crossover switches allow path-to-path transfer

### Fault Tolerance Checklist (Tier IV Only)

**Topology:**
- [ ] 2(N+1) redundancy or 2×(N+1) dual systems
- [ ] Dual active distribution (S+S configuration)
- [ ] Complete physical separation of A and B paths
- [ ] Independent compartments for A and B equipment

**Single Points of Failure Eliminated:**
- [ ] No shared utility service points
- [ ] No shared generator fuel systems
- [ ] No shared cooling water systems
- [ ] No shared control systems
- [ ] No shared grounding points (isolated grounds)
- [ ] No shared fire suppression agents

**Automatic Failover:**
- [ ] Power transfer <10ms (within IT equipment hold-up)
- [ ] Automatic detection of all failure modes
- [ ] No manual intervention required for any failure
- [ ] Cooling maintains capacity during any failure

**Testing Requirements:**
- [ ] Annual Tier IV certification testing
- [ ] Simulated failures of each path
- [ ] Load bank testing at full capacity
- [ ] Generator run testing under load

---

## Cost and Timeline Implications

### Relative Capital Cost (Tier I = 1.0×)

- **Tier I**: 1.0× baseline
- **Tier II**: 1.15-1.25× (15-25% premium)
- **Tier III**: 1.4-1.6× (40-60% premium)
- **Tier IV**: 1.8-2.5× (80-150% premium)

### Design and Construction Timeline

- **Tier I**: 6-9 months design + construction
- **Tier II**: 9-12 months design + construction
- **Tier III**: 12-18 months design + construction
- **Tier IV**: 18-30 months design + construction + commissioning

---

## Certification Process

### Uptime Institute Certification Steps

1. **Design Review** (TCDD - Tier Certification of Design Documents)
   - Submit design drawings, specifications, BOD
   - Uptime Institute reviews for compliance
   - Iterative feedback and revisions

2. **Constructed Facility Review** (TCCF - Tier Certification of Constructed Facility)
   - Site inspection during construction
   - Verification of as-built conditions
   - Equipment inspections

3. **Operational Sustainability** (TCOS - Tier Certification of Operational Sustainability)
   - Annual recertification
   - Operations and maintenance procedures review
   - Staff training verification

### Certification Timeline

- **TCDD**: 2-6 months (depends on design complexity and revisions)
- **TCCF**: 1-3 site visits during construction
- **TCOS**: Annual renewal required

---

## Common Certification Failures

### Top Reasons Designs Fail Tier Certification

1. **Insufficient redundancy**: Claiming N+1 but actually N
2. **Single points of failure**: Hidden dependencies in distribution
3. **Inadequate isolation**: Cannot maintain equipment without impact
4. **Shared systems**: Control systems, grounding, cooling water
5. **Insufficient fuel storage**: Not meeting minimum runtime requirements
6. **Inadequate compartmentalization** (Tier IV): A and B paths not truly isolated
7. **Transfer time too slow**: ATS or UPS transfer exceeds IT equipment ride-through
8. **Cooling capacity errors**: Not accounting for actual heat loads or future growth

---

## Resources

**Uptime Institute Publications:**
- Tier Standard: Topology (ANSI/TIA-942)
- Tier Standard: Operational Sustainability
- Data Center Site Infrastructure Tier Standard

**Industry Standards:**
- ANSI/TIA-942: Telecommunications Infrastructure Standard for Data Centers
- ASHRAE TC 9.9: Data Center Guidelines
- NFPA 75: Standard for Protection of IT Equipment

---

**Last Updated**: November 2025
**References**: Uptime Institute Tier Standard: Topology (current revision)
