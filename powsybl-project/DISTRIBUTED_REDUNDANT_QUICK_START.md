# Distributed Redundant (2N) - Quick Start Guide

## What is Distributed Redundant (2N)?

A **Tier IV data center topology** with:
- **Two completely isolated power trains** (A and B)
- **NO tie breaker** between paths
- **Each path 100% capacity** (true redundancy)
- **Maximum uptime**: 99.995% (26 minutes downtime/year)

## Key Characteristics

✅ **Complete isolation** - A and B never connect  
✅ **True 2N** - Each path handles 100% load independently  
✅ **No single point of failure** - Any failure affects only one train  
✅ **Concurrent maintainability** - Service one path while other runs  
✅ **Tier IV compliant** - Highest reliability standard  

## How to Use

### Detection Keywords

Include **any** of these in your BOD text:
- "distributed"
- "2n" or "2N"
- "distributed redundant"
- "independent power trains"

### Example BOD Text

```python
bod_text = """
Distributed redundant 2N architecture with 13.8kV MV switchgear.
Completely independent A and B power trains with no tie breaker.
Four diesel generators (two per side).
Each side feeds two transformers to separate LV distribution.
Static lithium-ion UPS for IT loads with dual-cord PDUs.
Each power train sized for 100% of critical load.
"""

from pachyderm_bod_generator import build_network_from_description
network, metadata = build_network_from_description(bod_text)
```

## What You Get

### Components Created

**Generators:**
- Split evenly between SWGR_A and SWGR_B
- No paralleling between A and B sides

**MV Switchboards:**
- MV_SWBD_A and MV_SWBD_B
- Redundancy classification: "2N"
- NO tie breaker between them

**Transformers:**
- Alternating A/B assignment
- Each path has equal capacity

**LV Switchboards:**
- Redundancy classification: "2N"
- Completely isolated per train

**UPS & PDUs:**
- Dual-cord via STS
- A and B feed sources

## Validation Checks

The validator ensures:

✅ **2 MV switchboards** present  
✅ **NO tie breaker** exists  
✅ **2N redundancy** classification  
✅ **Complete isolation** of A and B trains  

Warning if tie breaker detected:
```
⚠️ [BUS_TIE] Tie breaker detected in distributed redundant (2N) topology
💡 Recommendation: True 2N systems have completely isolated A and B paths
```

## vs. Dual-Feed (A/B)

| Feature | Dual-Feed | Distributed 2N |
|---------|-----------|----------------|
| **Tie Breaker** | ✅ Yes | ❌ No |
| **Path Capacity** | N+1 each | 100% each |
| **Resource Sharing** | ✅ Can share | ❌ Isolated |
| **Cost** | Lower | Higher |
| **Uptime** | 99.74% | 99.995% |
| **Tier Level** | II-III | IV |

## Run the Example

```powershell
cd C:\Users\eriks\Documents\Obsidian\powsybl-project

# Run the distributed redundant example
python example_distributed_redundant.py

# Validate the output
python pachyderm_schema_validator.py
```

## Output Example

```
DISTRIBUTED REDUNDANT (2N) TOPOLOGY EXAMPLE
======================================================================

✅ Topology: DISTRIBUTED REDUNDANT

--- Power Train Architecture ---

Generators: 4
  Train A: 2 generators
    - GEN_1: RECIP DIESEL - 2000 kW / 2500 kVA
    - GEN_3: RECIP DIESEL - 2000 kW / 2500 kVA
  Train B: 2 generators
    - GEN_2: RECIP DIESEL - 2000 kW / 2500 kVA
    - GEN_4: RECIP DIESEL - 2000 kW / 2500 kVA

MV Switchboards: 2
  MV_SWBD_A: 13.8 kV, 4000A, 65 kAIC, Redundancy: 2N
  MV_SWBD_B: 13.8 kV, 4000A, 65 kAIC, Redundancy: 2N

✅ No tie breakers detected - True 2N isolation confirmed

Transformers: 4
  Train A: 2 transformers @ 300 kVA each
  Train B: 2 transformers @ 300 kVA each

KEY CHARACTERISTICS OF 2N TOPOLOGY:
======================================================================
✅ Complete isolation between A and B power trains
✅ No tie breakers or cross-connections
✅ Each path sized for 100% of load (true redundancy)
✅ Any single component failure affects only one train
✅ Concurrent maintainability - service one path while other runs
✅ Tier IV compliant - supports dual-cord equipment via STS
======================================================================
```

## When to Use

**Use Distributed Redundant (2N) for:**
- Mission-critical data centers
- Financial services infrastructure
- Healthcare/hospital data centers
- Hyperscale cloud facilities
- Government/defense installations
- 99.995% uptime requirement
- Full concurrent maintainability needed

**Don't use if:**
- Budget constrained (use Dual-Feed instead)
- Lower tier (I-III) acceptable
- Downtime tolerance > 1 hour/year
- Single-cord loads only

## References

- **TIA-942-A**: Tier IV specification
- **Uptime Institute**: Tier IV Standard (2N+1)
- **ASHRAE TC 9.9**: Data Center Power Equipment
- **IEEE 493**: Reliability prediction

---

**Quick Access:**
- Full docs: `PACHYDERM_README.md`
- Topology comparison: `TOPOLOGY_COMPARISON.md`
- Example script: `example_distributed_redundant.py`

**Version**: 1.0.0
