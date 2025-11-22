# Critical Bugs and Fixes - Saga Pryor BOD Parser

**Date:** 2025-11-02
**Test Status:** ❌ **FAILED** - Parser unusable for production
**Priority:** 🔴 **CRITICAL** - Must fix before any real use

---

## Test Results Summary

| Specification | Expected | Actual | Status |
|--------------|----------|--------|---------|
| **Voltage** | 13.8 kV | 13.8 kV | ✅ PASS |
| **Generators** | 6 × 4MW diesel | 36 × 2MW nat gas | ❌ **FAIL (600% error)** |
| **Transformers** | 8 × 3,500 kVA | 4 × 400 kVA | ❌ **FAIL (88% undersized)** |
| **RMUs** | 6 units | 4 units | ❌ **FAIL (33% missing)** |
| **IT UPS** | 5 × 1,250 kVA | 0 units | ❌ **FAIL (100% missing)** |
| **Mech UPS** | 8 × 250 kW | 37 × 500 kW | ❌ **FAIL (365% error)** |
| **PowSyBl Model** | Valid | Broken (41 errors) | ❌ **FAIL** |

**Accuracy: 1/7 = 14%**

---

## Bug #1: Word-Counting Parser (CRITICAL)

### Current Code (BROKEN)
```python
# Line 99 in pachyderm_bod_generator.py
gen_count = len(re.findall(r'generator', text.lower())) or 4
```

### Problem
Counts every occurrence of "generator" in the document:
- "6 Diesel Generators" → counts 1
- "Generator Specifications" → counts 1
- "generator rated 4,000 kW" → counts 1
- ... (33 more occurrences)
- **Result: 36 generators instead of 6**

### Fix (REQUIRED)
```python
def extract_generator_count(text: str) -> int:
    """
    Extract generator count from BOD using specification patterns
    """
    # Pattern 1: "N × power_rating generators"
    # Matches: "6 × 4.0 MW @ 13.8 kV Diesel Generators"
    pattern1 = r'(\d+)\s*[×x]\s*[\d.]+\s*(?:MW|kW|kVA)\s*.*?[Gg]enerator'
    match1 = re.search(pattern1, text)
    if match1:
        return int(match1.group(1))

    # Pattern 2: "N generators" in specifications context
    # Look for "Generator System" or similar section header, then extract count
    gen_section = re.search(r'##\s*GENERATOR SYSTEM.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
    if gen_section:
        section_text = gen_section.group(0)
        # Find first mention of "N generators" or "N × " in generator section
        pattern = r'(\d+)\s*[×x]?\s*[Gg]enerator'
        match = re.search(pattern, section_text)
        if match:
            return int(match.group(1))

    # Default fallback
    return 4

# Usage
gen_count = extract_generator_count(text)
```

**Test:**
```python
bod_text = "6 × 4.0 MW @ 13.8 kV Diesel Generators (N+1 Redundancy)"
result = extract_generator_count(bod_text)
assert result == 6  # Should pass
```

---

## Bug #2: Generator Rating Not Parsed (CRITICAL)

### Current Code (BROKEN)
```python
# Lines 104-105 in pachyderm_bod_generator.py
rating_kw = 2000  # Hardcoded!
rating_kva = 2500 # Hardcoded!
```

### Problem
Uses default values regardless of BOD specifications

### Fix (REQUIRED)
```python
def extract_generator_rating(text: str) -> tuple[int, int]:
    """
    Extract generator kW and kVA ratings from BOD
    Returns: (kw, kva)
    """
    # Pattern: "N MW" or "N,NNN kW" @ voltage
    pattern = r'(\d+(?:,\d+)?(?:\.\d+)?)\s*(MW|kW)\s*.*?[Gg]enerator'
    match = re.search(pattern, text)

    if match:
        value_str = match.group(1).replace(',', '')
        value = float(value_str)
        unit = match.group(2)

        # Convert to kW
        if unit == 'MW':
            kw = int(value * 1000)
        else:
            kw = int(value)

        # Calculate kVA assuming 0.8 power factor (typical for generators)
        kva = int(kw / 0.8)

        return kw, kva

    # Default fallback
    return 2000, 2500

# Usage
rating_kw, rating_kva = extract_generator_rating(text)
```

**Test:**
```python
bod_text = "6 × 4.0 MW @ 13.8 kV Diesel Generators"
kw, kva = extract_generator_rating(bod_text)
assert kw == 4000
assert kva == 5000  # 4000 / 0.8
```

---

## Bug #3: Fuel Type Confusion (HIGH)

### Current Code (BROKEN)
```python
# Lines 113-116 in pachyderm_bod_generator.py
elif "natural gas" in text.lower() or "nat gas" in text.lower():
    fuel = "NAT_GAS"
```

### Problem
Finds "natural gas house generators" (for building power) and applies to all generators

### Fix (REQUIRED)
```python
def extract_generator_fuel(text: str) -> str:
    """
    Extract fuel type from generator section only
    """
    # Extract generator section
    gen_section = re.search(r'##\s*GENERATOR SYSTEM.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)

    search_text = gen_section.group(0) if gen_section else text

    # Look for fuel type near generator specifications
    fuel_pattern = r'(diesel|natural gas|nat gas|biodiesel|gas turbine)\s.*?[Gg]enerator'
    match = re.search(fuel_pattern, search_text, re.IGNORECASE)

    if match:
        fuel_type = match.group(1).lower()
        if 'diesel' in fuel_type and 'bio' not in fuel_type:
            return "DIESEL"
        elif 'natural gas' in fuel_type or 'nat gas' in fuel_type:
            return "NAT_GAS"
        elif 'biodiesel' in fuel_type:
            return "BIODIESEL"

    # Check for "Fuel: Diesel" pattern in specifications
    fuel_spec = re.search(r'\*\*Fuel\*\*:?\s*(Diesel|Natural Gas|Biodiesel)', search_text, re.IGNORECASE)
    if fuel_spec:
        fuel_value = fuel_spec.group(1).lower()
        if 'diesel' in fuel_value:
            return "DIESEL"

    return "DIESEL"  # Default to diesel
```

---

## Bug #4: Transformer Sizing Auto-Calculated (HIGH)

### Current Code (BROKEN)
```python
# Lines 186-193 in pachyderm_bod_generator.py
pdu_count = len(re.findall(r'pdu|rpp', text.lower())) or 8
total_load_kw = pdu_count * 100  # 100 kW per PDU
# ... complex formula that ignores BOD specs ...
tx_kva = math.ceil((load_per_tx / (efficiency * pf)) / 100) * 100
```

### Problem
Calculates transformer size from PDU count instead of parsing BOD specification

### Fix (REQUIRED)
```python
def extract_transformer_specs(text: str) -> tuple[int, int]:
    """
    Extract transformer count and rating from BOD
    Returns: (count, kva_per_unit)
    """
    # Pattern: "N × rating kVA" transformers
    # Matches: "8 × 3,500 kVA (13.8 kV/480V) Oil-Filled Transformers"
    pattern = r'(\d+)\s*[×x]\s*([\d,]+)\s*kVA.*?[Tt]ransformer'
    match = re.search(pattern, text)

    if match:
        count = int(match.group(1))
        kva_str = match.group(2).replace(',', '')
        kva = int(kva_str)
        return count, kva

    # Alternative pattern: Look in transformer section
    tx_section = re.search(r'##\s*TRANSFORMER.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
    if tx_section:
        section_text = tx_section.group(0)
        # Find rating in table or specs
        rating_match = re.search(r'\|\s*\*\*Rating\*\*\s*\|\s*([\d,]+)\s*kVA', section_text)
        if rating_match:
            kva = int(rating_match.group(1).replace(',', ''))
            # Count from "N × transformers" or "N transformers"
            count_match = re.search(r'(\d+)\s*[×x].*?[Tt]ransformer', section_text)
            count = int(count_match.group(1)) if count_match else 4
            return count, kva

    # Default fallback (Phase 1 assumption)
    return 4, 3500

# Usage in parse_bod_description()
xfmr_count, tx_kva = extract_transformer_specs(text)

# Replace lines 186-193 with:
for i in range(xfmr_count):
    # ... create transformers with rating = tx_kva
```

---

## Bug #5: RMU Count Hardcoded (HIGH)

### Current Code (BROKEN)
```python
# Lines 74, 170 in pachyderm_bod_generator.py
if elements["topology"] == "ring":
    for i in range(4):  # Hardcoded!
        elements["buses"].append({"id": f"RING_BUS_{i+1}", ...})
```

### Problem
Ring topology always creates exactly 4 RMUs regardless of BOD specification

### Fix (REQUIRED)
```python
def extract_rmu_count(text: str) -> int:
    """
    Extract RMU count from BOD
    """
    # Pattern: "N × RMUs" or "N RMUs"
    # Matches: "6 × RMUs (13.8 kV, 630A rated)"
    pattern = r'(\d+)\s*[×x]?\s*RMU'
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return int(match.group(1))

    # Alternative: Check RMU section
    rmu_section = re.search(r'###\s*Ring Main Units.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
    if rmu_section:
        section_text = rmu_section.group(0)
        match = re.search(r'(\d+)\s*[×x]?\s*RMU', section_text, re.IGNORECASE)
        if match:
            return int(match.group(1))

    # Default for ring topology
    return 4

# Usage in parse_bod_description()
if elements["topology"] == "ring":
    rmu_count = extract_rmu_count(text)
    for i in range(rmu_count):
        elements["buses"].append({"id": f"RING_BUS_{i+1}", "voltage": nominal_voltage})
```

---

## Bug #6: UPS Detection Broken (HIGH)

### Current Code (BROKEN)
```python
# Line 228
ups_count = len(re.findall(r'ups', text.lower())) or xfmr_count

# Lines 250-253
if "mechanical" in text.lower() or "fan" in text.lower() or "pump" in text.lower():
    function = "MECHANICAL"  # Applied to ALL UPS!
```

### Problem
- Counts word "ups" occurrences (finds 37 instead of 13)
- Classifies ALL UPS as mechanical because "mechanical" found in text
- Can't distinguish IT UPS from Mechanical UPS

### Fix (REQUIRED)
```python
def extract_ups_specs(text: str) -> dict:
    """
    Extract IT and Mechanical UPS specifications separately
    Returns: {
        'it_ups': {'count': int, 'kva_per_unit': int, 'type': str, 'battery': str},
        'mech_ups': {'count': int, 'kw_per_unit': int, 'type': str}
    }
    """
    result = {
        'it_ups': {'count': 0, 'kva_per_unit': 0, 'type': 'STATIC', 'battery': 'LI-ION'},
        'mech_ups': {'count': 0, 'kw_per_unit': 0, 'type': 'STATIC'}
    }

    # Extract IT UPS section
    it_ups_section = re.search(r'##\s*IT UPS.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
    if it_ups_section:
        section = it_ups_section.group(0)

        # Pattern: "N × rating kVA IT UPS Modules"
        # Matches: "5-6 × 1,250 kVA IT UPS Modules"
        pattern = r'(\d+)(?:-\d+)?\s*[×x]\s*([\d,]+)\s*kVA.*?UPS'
        match = re.search(pattern, section)
        if match:
            result['it_ups']['count'] = int(match.group(1))
            result['it_ups']['kva_per_unit'] = int(match.group(2).replace(',', ''))

        # Detect battery type
        if 'lithium' in section.lower() or 'li-ion' in section.lower():
            result['it_ups']['battery'] = 'LI-ION'
        elif 'vrla' in section.lower():
            result['it_ups']['battery'] = 'VRLA'

    # Extract Mechanical UPS section
    mech_ups_section = re.search(r'##\s*MECHANICAL UPS.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
    if mech_ups_section:
        section = mech_ups_section.group(0)

        # Pattern: "N × rating kW Static UPS Modules"
        # Matches: "8 × 250 kW Static UPS Modules (N+1)"
        pattern = r'(\d+)\s*[×x]\s*([\d,]+)\s*kW.*?UPS'
        match = re.search(pattern, section)
        if match:
            result['mech_ups']['count'] = int(match.group(1))
            result['mech_ups']['kw_per_unit'] = int(match.group(2).replace(',', ''))

    return result

# Usage in parse_bod_description()
ups_specs = extract_ups_specs(text)

# Create IT UPS modules
for i in range(ups_specs['it_ups']['count']):
    elements["ups"].append({
        "id": f"IT_UPS_{i+1}",
        "bus": f"LV_BUS_{(i % xfmr_count) + 1}",
        "type": ups_specs['it_ups']['type'],
        "battery": ups_specs['it_ups']['battery'],
        "function": "IT",
        "kw": int(ups_specs['it_ups']['kva_per_unit'] * 0.8),  # Assume 0.8 PF
        "kva": ups_specs['it_ups']['kva_per_unit']
    })

# Create Mechanical UPS modules
for i in range(ups_specs['mech_ups']['count']):
    elements["ups"].append({
        "id": f"MECH_UPS_{i+1}",
        "bus": f"LV_BUS_{(i % xfmr_count) + 1}",
        "type": ups_specs['mech_ups']['type'],
        "battery": "LI-ION",  # Typically lithium for static UPS
        "function": "MECHANICAL",
        "kw": ups_specs['mech_ups']['kw_per_unit'],
        "kva": int(ups_specs['mech_ups']['kw_per_unit'] / 0.9)  # Assume 0.9 PF
    })
```

---

## Bug #7: PowSyBl Substation Hierarchy Missing (HIGH)

### Current Code (BROKEN)
```python
# Lines 349-359 in build_network_from_description()
# Creates voltage levels but no substations
net.create_voltage_levels(
    id=vl_ids,
    topology_kind=['BUS_BREAKER'] * len(vl_ids),
    nominal_v=vl_voltages
)
```

### Problem
- PowSyBl requires substations before transformers can be created
- Results in "no substation" error for all transformers

### Fix (REQUIRED)
```python
def build_network_from_description(text, include_z_matrix=True):
    """Build PowSyBl network with proper hierarchy"""
    data = parse_bod_description(text, include_z_matrix)
    net = pp.network.create_empty("PACHYDERM_TierIV")

    # Group buses by voltage level
    voltage_groups = {}
    for bus in data["buses"]:
        voltage = bus["voltage"]
        if voltage not in voltage_groups:
            voltage_groups[voltage] = []
        voltage_groups[voltage].append(bus)

    # Create substations for each voltage level
    substation_map = {}
    for voltage, buses in voltage_groups.items():
        # Determine substation name based on voltage
        if voltage > 100:  # HV (345 kV, etc.)
            sub_id = "SUB_HV"
        elif voltage > 1:  # MV (13.8 kV, etc.)
            sub_id = "SUB_MV"
        else:  # LV (0.415 kV, etc.)
            sub_id = "SUB_LV"

        # Create substation if it doesn't exist
        if sub_id not in substation_map:
            net.create_substations(id=[sub_id])
            substation_map[sub_id] = []

        # Create voltage levels within substation
        for bus in buses:
            vl_id = bus["id"]
            net.create_voltage_levels(
                id=[vl_id],
                substation_id=[sub_id],
                topology_kind=['BUS_BREAKER'],
                nominal_v=[voltage]
            )
            substation_map[sub_id].append(vl_id)

            # Create bus within voltage level
            bus_id = f"{vl_id}_BUS"
            net.create_buses(
                id=[bus_id],
                voltage_level_id=[vl_id]
            )

    # Now transformers can be created (they reference voltage levels with substations)
    for t in data["transformers"]:
        try:
            net.create_2_windings_transformers(
                id=[t["id"]],
                voltage_level1_id=[t["hv_bus"]],
                bus1_id=[f"{t['hv_bus']}_BUS"],
                voltage_level2_id=[t["lv_bus"]],
                bus2_id=[f"{t['lv_bus']}_BUS"],
                r=[0.5],
                x=[5.0],
                g=[0],
                b=[0],
                rated_u1=[t["hv_voltage"]],
                rated_u2=[t["lv_voltage"]],
                rated_s=[t["rated_s"]]
            )
        except Exception as e:
            print(f"Warning: Could not create transformer {t['id']}: {e}")

    # ... rest of network creation
```

---

## Bug #8: UPS Reactive Power Not Set (MEDIUM)

### Current Code (BROKEN)
```python
# Lines 413-428 - UPS modeled as generators
net.create_generators(
    id=[u["id"]],
    # ...
    voltage_regulator_on=[False]  # But no target_q set!
)
```

### Problem
When `voltage_regulator_on=False`, must set `target_q` (reactive power) explicitly

### Fix (REQUIRED)
```python
# UPS (modeled as generators with reactive power control)
for u in data["ups"]:
    try:
        # Calculate reactive power assuming power factor = 0.9
        p_mw = u["kw"] / 1000
        pf = 0.9
        q_mvar = p_mw * math.sqrt((1 - pf**2) / pf**2)

        net.create_generators(
            id=[u["id"]],
            voltage_level_id=[u["bus"]],
            bus_id=[f"{u['bus']}_BUS"],
            max_p=[u["kw"]/1000],
            min_p=[0],
            target_p=[(u["kw"]/1000)*0.8],
            target_v=[0.415],
            target_q=[q_mvar],  # Set reactive power!
            voltage_regulator_on=[False]
        )
    except Exception as e:
        print(f"Warning: Could not create UPS {u['id']}: {e}")
```

---

## Validation Gaps (NEW ISSUE)

### Problem
Schema validator passed even though values are completely wrong:
- 36 generators instead of 6 → **No validation**
- 37 UPS instead of 13 → **No validation**
- Transformer sizing 88% wrong → **No validation**

### Fix (REQUIRED)
Add semantic validation rules:

```python
# In pachyderm_schema_validator.py, add to validate_metadata()

# Check generator count is reasonable
gen_count = len(metadata.get("generators", []))
if gen_count > 20:
    alerts.append(ValidationAlert(
        "WARNING", "GENERATORS", "count",
        f"Generator count ({gen_count}) seems unusually high",
        "Verify BOD parsing correctly extracted generator count, not word occurrences"
    ))

# Check UPS count is reasonable
ups_count = len(metadata.get("ups", []))
if ups_count > 30:
    alerts.append(ValidationAlert(
        "WARNING", "UPS", "count",
        f"UPS count ({ups_count}) seems unusually high",
        "Verify BOD parsing correctly extracted UPS count, not word occurrences"
    ))

# Check transformer sizing is reasonable for data center
for tx in metadata.get("transformers", []):
    rating = tx.get("rated_s", 0)
    if rating < 1000:  # Most data center transformers are > 1 MVA
        alerts.append(ValidationAlert(
            "WARNING", tx["id"], "rated_s",
            f"Transformer rating ({rating} kVA) seems small for data center",
            "Typical data center transformers are 1,000-5,000 kVA. Verify auto-sizing calculation."
        ))
```

---

## Implementation Priority

### Week 1 (MUST DO)
1. ✅ Fix generator count parsing (Bug #1)
2. ✅ Fix generator rating parsing (Bug #2)
3. ✅ Fix transformer specs parsing (Bug #4)
4. ✅ Fix PowSyBl substation hierarchy (Bug #7)
5. ✅ Add semantic validation (Validation Gaps)

### Week 2 (SHOULD DO)
6. ✅ Fix fuel type detection (Bug #3)
7. ✅ Fix RMU count parsing (Bug #5)
8. ✅ Fix UPS specs parsing (Bug #6)
9. ✅ Fix UPS reactive power (Bug #8)

### Week 3 (NICE TO HAVE)
10. Add comprehensive unit tests for each parser function
11. Create section-aware parser (extract specs from relevant sections only)
12. Add fuzzy matching for variations in BOD writing style

---

## Testing Checklist

After fixes, verify:

- [ ] Generator count: 6 (not 36)
- [ ] Generator rating: 4,000 kW (not 2,000 kW)
- [ ] Generator fuel: DIESEL (not NAT_GAS)
- [ ] Transformer count: 8 (not 4)
- [ ] Transformer rating: 3,500 kVA (not 400 kVA)
- [ ] RMU count: 6 (not 4)
- [ ] IT UPS: 5 units (not 0)
- [ ] Mech UPS: 8 units (not 37)
- [ ] PowSyBl transformers created: 8/8 (not 0/4)
- [ ] PowSyBl UPS created: 13/13 (not 0/37)
- [ ] Validation catches unreasonable values

---

## Conclusion

**Current Status:** Parser is **COMPLETELY BROKEN** for real-world use

**After Fixes:** Parser should achieve **>90% accuracy** on structured BOD documents

**Timeline:** 2-3 weeks to implement all fixes and tests

**Recommendation:** Create structured YAML specification format as interim solution while parser is being fixed

---

**Document Version:** 1.0
**Author:** Claude Code Review & Testing System
**Test Script:** `test_saga_pryor_bod.py`
