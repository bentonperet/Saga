# Data Center Electrical Topology Comparison

This guide compares the four supported topologies in the PACHYDERM electrical SLD generator.

## Overview Table

| Topology | Redundancy | Tie Breaker | Use Case | Tier Level |
|----------|-----------|-------------|----------|------------|
| **Radial** | N+1 | No | Single-feed systems, cost-sensitive | Tier I-II |
| **Dual-Feed** | N+1 per path | Yes | Medium redundancy with flexibility | Tier II-III |
| **Ring Bus** | N+1 | No (closed loop) | High reliability, industrial | Tier III |
| **Distributed Redundant (2N)** | 100% per path | No | Maximum uptime, mission-critical | Tier IV |

---

## 1. Radial Topology

### Architecture
```
Utility/Gen → MV SWGR → TX → LV SWBD → UPS → PDU → Load
```

### Characteristics
- **Single power path** to all loads
- **N+1 redundancy** at component level (e.g., multiple generators, UPS modules)
- **No alternate path** if main path fails
- **Lowest cost** and simplest design

### Detection Keywords
- No special keywords needed (default topology)
- "radial", "single-feed"

### Best For
- Small to medium data centers
- Tier I/II requirements
- Budget-constrained projects
- Non-critical applications

---

## 2. Dual-Feed (A/B) Topology

### Architecture
```
Gen A → SWGR A ─┐         ┌─ TX A → LV A → UPS A ─┐
                │         │                        ├─ STS → PDU → Load
Gen B → SWGR B ─┴─[TIE]─┴─ TX B → LV B → UPS B ─┘
```

### Characteristics
- **Two independent paths** (A and B)
- **Tie breaker** allows cross-connection during maintenance
- **N+1 redundancy** within each path
- **Single-cord loads** can receive power from either A or B
- **Dual-cord loads** via Static Transfer Switch (STS)

### Detection Keywords
- "dual", "a/b", "dual-feed"
- "tie breaker"

### Best For
- Tier II/III data centers
- Balance between cost and reliability
- Systems requiring maintenance flexibility
- Mixed single-cord and dual-cord loads

### Key Difference from 2N
- **Has tie breaker** between A and B
- **Each path N+1** (not full capacity)
- **Can share resources** between paths

---

## 3. Ring Bus Topology

### Architecture
```
        RMU 1 ← Gen 1
           ↓
RMU 4 ← Ring → RMU 2 ← Gen 2
   ↓              ↓
Gen 4          Gen 3 → RMU 3

Each RMU feeds TX → LV → UPS → Load
```

### Characteristics
- **Closed-loop configuration** with 4 nodes
- **RMUs (Ring Main Units)** at each node with IN/OUT/FEEDER switches
- **No single point of failure** - power can flow both directions
- **Concurrent maintainability** - isolate any section while maintaining power
- **Common in industrial** and utility-grade installations

### Detection Keywords
- "ring", "ring bus"
- "rmu", "ring main unit"

### Best For
- Tier III data centers
- Industrial facilities
- Utility-interconnected systems
- High-reliability applications
- Sites requiring frequent maintenance

### Key Features
- **4 RMUs automatically created** when ring topology detected
- **Sectionalizing switches** for fault isolation
- **Bi-directional power flow**

---

## 4. Distributed Redundant (2N) Topology

### Architecture
```
Gen A1 → SWGR A → TX A1 → LV A1 → UPS A1 ─┐
Gen A2 ↗                                    ├─ STS → PDU → Load
                                           ↗
Gen B1 → SWGR B → TX B1 → LV B1 → UPS B1 ─┘
Gen B2 ↗

NO CONNECTION BETWEEN A AND B PATHS
```

### Characteristics
- **Two completely isolated power trains** (A and B)
- **NO tie breaker** between paths
- **Each path 100% capacity** (true 2N redundancy)
- **Any single failure** affects only one train
- **Highest uptime** and availability
- **Tier IV compliant**

### Detection Keywords
- "distributed", "2n", "distributed redundant"
- "independent power trains"
- "no tie"

### Best For
- **Tier IV data centers**
- Mission-critical facilities
- Financial services, healthcare
- Hyperscale cloud providers
- Maximum uptime requirements (99.995%)

### Key Differences from Dual-Feed
- **NO tie breaker** - complete isolation
- **100% capacity per path** (not N+1)
- **Cannot share resources** between A and B
- **Higher cost** but maximum reliability
- **Concurrent maintainability** without impacting either path

---

## Selection Guide

### Choose **Radial** if:
- Budget < $1M for electrical
- Downtime tolerance > 4 hours/year
- Single-cord equipment acceptable
- Small to medium IT load (< 500 kW)

### Choose **Dual-Feed** if:
- Budget $1M - $3M
- Downtime tolerance 1-4 hours/year
- Need maintenance flexibility
- Mix of single and dual-cord equipment
- Tier II/III requirement

### Choose **Ring Bus** if:
- Industrial or utility-style design preferred
- Frequent maintenance required
- High generator/transformer count
- Need sectionalizing capability
- Tier III requirement

### Choose **Distributed Redundant (2N)** if:
- Mission-critical application
- Downtime tolerance < 30 minutes/year
- All dual-cord equipment
- Tier IV requirement
- Budget > $3M for electrical
- Maximum concurrent maintainability needed

---

## Implementation Examples

### Generate Radial System
```python
bod_text = "13.8kV system with two generators feeding single MV switchboard"
network, metadata = build_network_from_description(bod_text)
```

### Generate Dual-Feed System
```python
bod_text = """
Dual-feed 13.8kV with MV switchboards A and B.
Two generators per side with tie breaker.
Static UPS for IT loads via STS.
"""
network, metadata = build_network_from_description(bod_text)
```

### Generate Ring Bus System
```python
bod_text = """
13.8kV ring bus with four nodes and RMUs.
One generator per node feeding transformers to LV distribution.
"""
network, metadata = build_network_from_description(bod_text)
```

### Generate 2N System
```python
bod_text = """
Distributed redundant 2N architecture.
Completely independent A and B power trains with no tie breaker.
Each path sized for 100% of load.
"""
network, metadata = build_network_from_description(bod_text)
```

---

## Validation Differences

The validator performs topology-specific checks:

### Dual-Feed Checks
- Verifies 2 MV switchboards present
- Confirms tie breaker exists
- Validates A/B redundancy classification

### Ring Bus Checks
- Requires 4 RMUs minimum
- Validates closed-loop connectivity
- Checks ring segmentation

### 2N (Distributed Redundant) Checks
- **Verifies 2 MV switchboards** with 2N classification
- **Ensures NO tie breaker** between A and B
- **Validates complete isolation** of power trains
- **Confirms 100% sizing** of each path

---

## Cost and Complexity Comparison

| Aspect | Radial | Dual-Feed | Ring Bus | 2N |
|--------|--------|-----------|----------|-----|
| **Initial Cost** | 1x | 1.5x | 1.8x | 2.2x |
| **Operational Complexity** | Low | Medium | Medium | High |
| **Maintenance Windows** | Full outage | Partial capacity | Full capacity | Full capacity |
| **Footprint** | Smallest | Medium | Medium | Largest |
| **Uptime (%)** | 99.67 | 99.74 | 99.98 | 99.995 |

---

## Standards References

- **TIA-942-A**: Data Center Tier Classifications
  - Tier I: Radial
  - Tier II: Radial with N+1
  - Tier III: Dual-feed or Ring
  - Tier IV: Distributed Redundant (2N)

- **Uptime Institute**: Tier Standard Topology
  - Tier IV requires 2N+1 at minimum
  - No single point of failure
  - Concurrent maintainability

---

## Summary

The choice of topology depends on:
1. **Uptime requirements**
2. **Budget constraints**
3. **Maintenance strategy**
4. **Load criticality**
5. **Tier certification needed**

For **maximum reliability**, use **Distributed Redundant (2N)**.  
For **cost-effective reliability**, use **Dual-Feed (A/B)**.  
For **industrial-grade resilience**, use **Ring Bus**.  
For **basic applications**, use **Radial**.

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-02
