# SLD Generation Standards - Update Summary

**Date:** 2025-11-02
**Version:** 1.0 → 1.1
**Status:** ✅ Complete

---

## Major Updates Applied

### 1. RMU Topology Requirements - DUAL-FEED (Section 3.2)

**NEW Requirements:**

✅ **Two MV incomers at TOP** of RMU graphic
- Primary incomer (from primary MV-SWBD)
- Reserve incomer (from reserve MV-SWBD)
- Both with clearly labeled breakers (PRI / RES)
- Cable pathways shown from both sources

✅ **One outgoer at BOTTOM** of RMU graphic
- Single feeder to transformer
- Breaker labeled "TX" or "FEEDER"
- Vertical path downward

✅ **Internal bus section**
- Horizontal bus connecting both incomers
- Tee-off point (black dot) for transformer feeder

**Layout:**
```
   PRIMARY        RESERVE
   MV-SWBD        MV-SWBD
      │              │
      │ (cable)      │ (cable)
      ↓              ↓
   [CB-IN1]      [CB-IN2]
      │              │
      └──[BUS]───────┘
            │
          [Tee]
            │
         [CB-TX]
            │
            ↓ (to transformer)
```

**Spacing:**
- 80px vertical clearance above RMU for incomer paths
- 100px horizontal spacing between RMUs
- Incomer breakers: 30px from RMU top edge

---

### 2. Transformer Connection Orientation (Section 3.3)

**NEW Requirements:**

✅ **Incomer:** From TOP or LEFT of graphic (choose for symmetry)
✅ **Outgoer:** From BOTTOM or RIGHT of graphic (opposite of incomer)
✅ **Path to LV-SWBD:** Connects to TOP of LV-SWBD graphic

**Vertical Layout (Preferred):**
```
     RMU
      ↓ (incomer from top)
   [CB-HV]
      ↓
  ┌───────┐
  │  TX   │
  └───────┘
      ↓
   [CB-LV]
      ↓ (outgoer from bottom)
   LV-SWBD
```

**Symmetry Rule:**
- TOP incomer → BOTTOM outgoer (vertical symmetry) ✓
- LEFT incomer → RIGHT outgoer (horizontal symmetry) ✓
- NEVER diagonal connections ✗

---

### 3. LV Switchboard Requirements (Section 3.1)

**NEW Requirements:**

✅ **Width:** Must accommodate **5 BREAKER POSITIONS** minimum
- Width: 200px minimum (40px per position × 5)
- Height: 100px minimum

✅ **Main bus:** Horizontal bus inside at top (15px from edge)

✅ **Connections:** ALL downstream from BOTTOM of graphic
- Distribution panels
- UPS systems
- Additional switchboards
- PDUs

✅ **Incomer:** From TOP (from transformer)

**Layout:**
```
     TX
      ↓
  [CB-MAIN]
      ↓
┌─────────────────┐
│   [═══BUS═══]   │ (5 positions on bus)
│   LV-SWBD-N     │
│   480V/277V     │
└─────────────────┘
  │   │   │   │   │  (5 feeders from bottom)
  ↓   ↓   ↓   ↓   ↓
```

---

### 4. Text Clearance & Overlap Prevention (Section 2.3)

**NEW MANDATORY RULES:**

✅ Text **MUST NOT** overlap:
- Cable pathways (power lines)
- Equipment graphic boundaries
- Other text labels
- Breaker symbols

**Clearance Requirements:**
- **15px minimum** from cable paths
- **10px minimum** from equipment edges
- **15-20px offset** for breaker labels (to the side, not on top)

**Text Placement:**

| Element | Position | Clearance |
|---------|----------|-----------|
| Equipment labels | Inside box, centered | 10px from edges |
| Breaker labels | Offset 15-20px to side | Never on symbol |
| Cable labels | 15px offset from line | Above or to side |
| Rating labels | Below equipment | 15px below boundary |

**Example (CORRECT):**
```svg
<use href="#breaker-closed" x="500" y="300"/>
<text x="520" y="305">CB-1</text>  <!-- 20px offset right -->
```

**Example (WRONG):**
```svg
<use href="#breaker-closed" x="500" y="300"/>
<text x="500" y="300">CB-1</text>  ❌ <!-- On top of symbol -->
```

---

### 5. Symmetrical Spacing - MANDATORY (Section 2.2)

**NEW Requirements:**

✅ **ALL spacing MUST be symmetrical** and evenly distributed

✅ **Calculation required** (no manual adjustment):
```python
def calculate_positions(canvas_width, equipment_count, equipment_width, margin):
    usable_width = canvas_width - (2 * margin)
    total_equipment_width = equipment_count * equipment_width
    available_space = usable_width - total_equipment_width
    spacing = available_space / (equipment_count + 1)

    positions = []
    for i in range(equipment_count):
        x = margin + spacing * (i + 1) + equipment_width * i + (equipment_width / 2)
        positions.append(x)

    return positions
```

**Symmetry Rules:**
1. **Horizontal:** Left spacing = Right spacing
2. **Vertical:** Equal spacing between voltage levels
3. **Equipment:** Evenly distributed (calculated, not manual)

**Example - 8 Transformers on 4000px canvas:**
- Usable width: 3600px (4000 - 400 margin)
- Total TX width: 560px (8 × 70px)
- Available space: 3040px
- **Spacing: 337.8px** (equal between all)

---

## Implementation Checklist

When generating SLDs, now verify:

- [ ] RMUs show **2 incomers at top** (primary + reserve)
- [ ] RMUs show **1 outgoer at bottom** (to transformer)
- [ ] RMU cable paths clearly labeled (PRIMARY / RESERVE)
- [ ] Transformers: incomer from TOP, outgoer to BOTTOM
- [ ] LV-SWBDs: **200px wide** (5 breaker positions)
- [ ] LV-SWBD connections: **ALL from bottom**
- [ ] Text: **15px min** from cable paths
- [ ] Text: **10px min** from equipment edges
- [ ] Breaker labels: **offset 15-20px** to side
- [ ] Equipment spacing: **calculated** (symmetrical)
- [ ] No text overlaps lines, equipment, or symbols

---

## Files Updated

1. **SLD_GENERATION_STANDARDS.md** - Updated to v1.1
   - Section 2.2: Symmetrical spacing with calculation
   - Section 2.3: Text clearance/overlap prevention (NEW)
   - Section 3.1: LV-SWBD 5-position layout
   - Section 3.2: RMU dual-feed topology
   - Section 3.3: Transformer connection orientation

2. **Next Step:** Update SLD generator scripts to comply with v1.1

---

## Summary

The standards now define **professional, construction-ready SLD requirements** with:

✅ Dual-feed RMU topology (2 incomers, 1 outgoer)
✅ Proper transformer connection orientation (symmetry)
✅ LV switchboards with 5 breaker positions
✅ Text clearance rules (no overlaps)
✅ Symmetrical spacing (calculated, not manual)

**Status:** Ready to implement in next SLD generation script
**Compliance:** IEEE 315 / IEC 60617 + industry best practices

---

**Document Version:** SLD Standards v1.1
**Updated:** 2025-11-02
**Next Review:** After implementing v1.1 compliant generator
