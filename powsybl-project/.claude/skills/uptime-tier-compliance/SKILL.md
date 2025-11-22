---
name: uptime-tier-compliance
description: Validate data center designs against Uptime Institute Tier Standards (Tier I-IV) for topology, redundancy, concurrent maintainability, and fault tolerance. Use when reviewing BOD documents, design specifications, or assessing tier certification readiness.
allowed-tools: Read, Grep, Glob, WebSearch
---

# Uptime Institute Tier Compliance Validator

## Purpose

This skill helps validate data center infrastructure designs against Uptime Institute Tier Standards for certification readiness. It analyzes design documents, BOD files, and specifications to identify compliance gaps and provide recommendations.

## Instructions

When activated, perform the following validation workflow:

### 1. Identify Target Tier Level

First, determine which tier level is being targeted:
- **Tier I**: Basic Capacity (99.671% availability)
- **Tier II**: Redundant Capacity Components (99.741% availability)
- **Tier III**: Concurrently Maintainable (99.982% availability)
- **Tier IV**: Fault Tolerant (99.995% availability)

### 2. Analyze Key Infrastructure Categories

Review each critical system area:

#### A. ELECTRICAL POWER DISTRIBUTION
- **Tier I**: Single path, no redundancy (N)
- **Tier II**: Single path with redundant components (N+1)
- **Tier III**: Dual power paths, one active (N+1, dual path)
- **Tier IV**: Dual active power paths, fault tolerant (2(N+1))

**Check for:**
- Utility service entrance configuration
- Generator capacity and redundancy
- UPS topology and redundancy level
- Switchgear and distribution paths
- PDU distribution strategy
- Automatic transfer switches (ATS) configuration

#### B. COOLING SYSTEMS
- **Tier I**: Single path, no redundancy (N)
- **Tier II**: Single path with redundant components (N+1)
- **Tier III**: Dual distribution paths, concurrently maintainable (N+1)
- **Tier IV**: Dual active paths, fault tolerant (2(N+1))

**Check for:**
- Chiller redundancy and capacity
- Cooling tower configuration
- Pump redundancy
- CRAH/CRAC unit distribution
- Piping and distribution topology
- Control systems and fail-over mechanisms

#### C. CONCURRENT MAINTAINABILITY (Tier III+)

**Requirements:**
- Any single component can be removed from service without impacting operations
- Dual distribution paths for power and cooling
- Isolation valves and disconnects for all equipment
- Bypass capabilities for maintenance
- No single points of failure in distribution

**Validation checklist:**
- Can chillers be serviced without shutdown?
- Can UPS modules be bypassed for maintenance?
- Are there isolation valves on all cooling loops?
- Can generators be taken offline for service?
- Are distribution paths truly independent?

#### D. FAULT TOLERANCE (Tier IV)

**Requirements:**
- Withstand any single worst-case unplanned failure
- Dual active power and cooling distribution
- Automatic fault detection and response
- No impact to critical load during failure
- 2(N+1) redundancy for all systems

**Validation checklist:**
- Automatic transfer within IT equipment ride-through
- Dual-corded equipment with automatic failover
- Continuous cooling during any single failure
- Independent compartmentalization
- No shared single points of failure

### 3. Document Compliance Gaps

For each non-compliant item, document:
- **System/Component**: What is affected
- **Current Design**: What is currently specified
- **Tier Requirement**: What the tier standard requires
- **Gap**: Specific deficiency
- **Recommendation**: How to achieve compliance
- **Cost Impact**: ROM estimate if available

### 4. Generate Compliance Report

Produce a structured report:

```markdown
# Uptime Institute Tier [X] Compliance Assessment

**Project**: [Project Name]
**Target Tier**: Tier [X]
**Assessment Date**: [Date]
**Documents Reviewed**: [List BOD files, drawings, specs]

## Executive Summary
- Overall compliance status (percentage or qualitative)
- Major gaps identified
- Critical path items for certification

## Detailed Findings

### Electrical Systems
[Compliance analysis with specific gaps]

### Cooling Systems
[Compliance analysis with specific gaps]

### Concurrent Maintainability
[Analysis of maintenance capabilities]

### Fault Tolerance (if Tier IV)
[Analysis of fault tolerance provisions]

## Recommendations
1. [Priority 1 items - certification blockers]
2. [Priority 2 items - significant gaps]
3. [Priority 3 items - minor improvements]

## Next Steps
- [Action items for design team]
- [Recommended consultations with Uptime Institute]
```

## Key Validation Points by Tier

### Tier I Validation
- Single non-redundant distribution path
- No concurrent maintainability required
- Planned shutdowns allowed
- 99.671% availability (28.8 hrs/year downtime)

### Tier II Validation
- N+1 redundancy for critical components
- Single distribution path acceptable
- Planned shutdowns still required
- 99.741% availability (22.0 hrs/year downtime)

### Tier III Validation
- **Critical**: Dual distribution paths
- **Critical**: All equipment concurrently maintainable
- No planned shutdowns of IT load
- 99.982% availability (1.6 hrs/year downtime)
- Must demonstrate maintenance scenarios

### Tier IV Validation
- **Critical**: Fault tolerant topology (2N or 2(N+1))
- **Critical**: Withstand any single worst-case failure
- **Critical**: Dual-corded equipment throughout
- **Critical**: Compartmentalization and isolation
- 99.995% availability (0.4 hrs/year downtime)
- Must demonstrate failure scenarios

## Common Compliance Issues

**Electrical:**
- Insufficient generator capacity for N+1 or 2(N+1)
- Single utility service (not diverse)
- UPS topology doesn't support maintenance bypass
- Shared neutral or ground creating single point of failure
- ATS strategy doesn't support concurrent maintainability

**Cooling:**
- Insufficient chiller redundancy
- Single chilled water loop (no dual path)
- No isolation valves for maintenance
- Cooling tower cells not independently serviceable
- Control system single point of failure

**Architecture/Layout:**
- Inadequate compartmentalization (Tier IV)
- Fire suppression zones create maintenance conflicts
- Cable tray routing creates single points of failure
- Insufficient physical separation of A/B paths

## Submittal Readiness Assessment

When preparing for Uptime Institute certification submittal, also verify document completeness against the official submittal requirements.

**Reference**: See `../GGE Provided Documentation/Uptime Design Certification/Uptime Certification.md` for the complete list of required submittal documents.

### Pre-Submittal Checklist

Before recommending submittal, verify the following documents are complete:

**Core Documents:**
- [ ] Basis of Design document (with redundancy levels, capacities)
- [ ] Electrical single-line diagrams (MV and LV)
- [ ] Mechanical schematics (chilled water, condenser water, fuel)
- [ ] Architectural floor plans (with equipment locations)
- [ ] Equipment schedules (electrical and mechanical)
- [ ] Load calculations (electrical and cooling)

**Tier III/IV Additional Requirements:**
- [ ] Distribution path layout drawings
- [ ] Compartmentalization plans (Tier IV only)
- [ ] Fire compartment drawings (Tier IV only)
- [ ] Sequence of operations (Tier IV only)
- [ ] Maintenance and fault scenario load calculations

**Supporting Documents:**
- [ ] Telecommunications path site plan
- [ ] Fuel system schematics
- [ ] Fire system electrical riser diagram
- [ ] Water treatment system (if applicable)
- [ ] EPO system (if required)

When generating compliance reports, include a submittal readiness section that indicates which documents are complete and which still need development.

## Reference Documents

See [tier-requirements.md](tier-requirements.md) for detailed tier requirement matrices.

See `../GGE Provided Documentation/Uptime Design Certification/Uptime Certification.md` for official submittal document requirements.

## Search Strategy

When analyzing BOD documents, search for keywords:
- "redundancy", "N+1", "2N", "fault tolerant"
- "concurrent maintainability", "bypass", "isolation"
- "single point of failure", "SPOF"
- "UPS", "generator", "chiller", "cooling tower"
- "dual feed", "dual path", "A-side", "B-side"
- "automatic transfer", "failover"

## Output Format

Always provide:
1. **Summary**: Compliant / Non-compliant with key reasons
2. **Gap Analysis**: Specific deficiencies by system
3. **Recommendations**: Prioritized action items
4. **Cost Impact**: ROM estimates where possible
5. **Timeline**: Critical path to certification readiness

## Notes

- This skill provides design validation guidance only
- Official Uptime Institute certification requires formal submittal and review
- Recommend engaging Uptime Institute early in design phase
- Tier certification applies to both design and operational phases
- Some requirements may vary by jurisdiction or specific site conditions
