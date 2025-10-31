# Capacity Calculations - Transformer and Generator Sizing
## Mathematical Justification for Critical Findings

**Project:** Biliki Data Center, Tbilisi, Georgia
**Document:** GGE-CAS-DES-BOD-C02
**Date:** October 30, 2025

---

## Source Data from BOD Document

**From Page 2 - IT Load Summary:**
- Phase 1 IT Load: 2.385 MW
- Phase 2 IT Load: 3.250 MW
- **Total IT Load: 5.635 MW**

**From Page 3 - Performance Targets:**
- Target PUE: ≤ 1.5

**From Page 6 - Electrical Infrastructure:**
- Transformers: 4 total (2 per group)
  - Each group includes 1 × 3000 kVA transformer
  - Configuration: 2N (2 transformers per group, 4 total)
- Generators: 4 × 2500 kVA total (2 per group)
  - Configuration: 2N (2 generators per group)

**Load Distribution (inferred from phasing):**
- Group 1: Phase 1 = 2.385 MW IT load
- Group 2: Phase 2 = 3.250 MW IT load

---

## Calculation Methodology

### Power Factor Assumptions
- **IT Equipment Power Factor:** 0.95 (typical for modern data center IT equipment with active PFC)
- **Facility Power Factor:** 0.95 (typical with properly sized electrical infrastructure)

### Load Categories
1. **IT Load (kW):** Direct power to IT equipment
2. **Infrastructure Load:** Calculated using PUE
   - Infrastructure Load = IT Load × (PUE - 1)
   - With PUE 1.5: Infrastructure = IT × 0.5
3. **Total Facility Load:** IT Load + Infrastructure Load = IT Load × PUE

### Transformer and Generator Sizing Requirements (Tier III)

**For 2N Configuration:**
- Each transformer must independently carry the **full group load** (IT + Infrastructure)
- Each generator must independently carry the **full group load** (IT + Infrastructure)
- Minimum recommended margin: **20-25%** for:
  - Future load growth
  - Inrush current during equipment startup
  - Harmonic derating (especially with high-density IT loads)
  - Temperature derating
  - Aging/end-of-life capacity reduction

---

## GROUP 1 CALCULATIONS (Phase 1)

### IT Load
- **IT Load:** 2.385 MW = 2,385 kW

### Infrastructure Load (from PUE 1.5)
- **Infrastructure Load:** 2,385 kW × (1.5 - 1) = 2,385 kW × 0.5 = **1,192.5 kW**

### Total Group 1 Load
- **Total Load (kW):** 2,385 kW + 1,192.5 kW = **3,577.5 kW**

### Convert to Apparent Power (kVA)
- **Power Factor:** 0.95
- **Total Load (kVA):** 3,577.5 kW ÷ 0.95 = **3,765.8 kVA**

### Transformer Requirement (2N Configuration)
- **Current Spec:** 1 × 3000 kVA per side (2 total for Group 1)
- **Required Capacity per Transformer:** 3,765.8 kVA
- **With 25% Margin:** 3,765.8 kVA × 1.25 = **4,707.2 kVA**

**RESULT:**
- **Specified:** 3000 kVA
- **Required (no margin):** 3,765.8 kVA
- **Required (with 25% margin):** 4,707.2 kVA
- **Shortfall:** 3,765.8 - 3000 = **765.8 kVA (25.5% overload)**

**✗ CRITICAL ISSUE:** In 2N operation with one transformer down for maintenance, the remaining 3000 kVA transformer cannot carry the 3,765.8 kVA load. This results in **25.5% overload**, violating Tier III concurrent maintainability.

---

### Generator Requirement (2N Configuration)
- **Current Spec:** 1 × 2500 kVA per side (2 total for Group 1)
- **Required Capacity per Generator:** 3,765.8 kVA
- **With 25% Margin:** 4,707.2 kVA

**Convert to Prime Power (kW) for Generator Rating:**
- 3,765.8 kVA × 0.95 PF = **3,577.5 kW prime power**
- With 25% margin: 4,707.2 kVA × 0.95 = **4,471.8 kW**

**RESULT:**
- **Specified:** 2500 kVA = 2,375 kW (at 0.95 PF)
- **Required (no margin):** 3,577.5 kW
- **Required (with 25% margin):** 4,471.8 kW
- **Shortfall:** 3,577.5 - 2,375 = **1,202.5 kW (50.6% overload)**

**✗ CRITICAL ISSUE:** In 2N operation with one generator down for maintenance, the remaining 2500 kVA generator cannot carry the 3,577.5 kW load. This results in **50.6% overload**, violating Tier III concurrent maintainability.

---

## GROUP 2 CALCULATIONS (Phase 2)

### IT Load
- **IT Load:** 3.250 MW = 3,250 kW

### Infrastructure Load (from PUE 1.5)
- **Infrastructure Load:** 3,250 kW × (1.5 - 1) = 3,250 kW × 0.5 = **1,625 kW**

### Total Group 2 Load
- **Total Load (kW):** 3,250 kW + 1,625 kW = **4,875 kW**

### Convert to Apparent Power (kVA)
- **Power Factor:** 0.95
- **Total Load (kVA):** 4,875 kW ÷ 0.95 = **5,131.6 kVA**

### Transformer Requirement (2N Configuration)
- **Current Spec:** 1 × 3000 kVA per side (2 total for Group 2)
- **Required Capacity per Transformer:** 5,131.6 kVA
- **With 25% Margin:** 5,131.6 kVA × 1.25 = **6,414.5 kVA**

**RESULT:**
- **Specified:** 3000 kVA
- **Required (no margin):** 5,131.6 kVA
- **Required (with 25% margin):** 6,414.5 kVA
- **Shortfall:** 5,131.6 - 3000 = **2,131.6 kVA (71.1% overload)**

**✗ CRITICAL ISSUE:** In 2N operation with one transformer down for maintenance, the remaining 3000 kVA transformer cannot carry the 5,131.6 kVA load. This results in **71.1% overload**, violating Tier III concurrent maintainability and **exceeding transformer thermal limits**.

---

### Generator Requirement (2N Configuration)
- **Current Spec:** 1 × 2500 kVA per side (2 total for Group 2)
- **Required Capacity per Generator:** 5,131.6 kVA
- **With 25% Margin:** 6,414.5 kVA

**Convert to Prime Power (kW) for Generator Rating:**
- 5,131.6 kVA × 0.95 PF = **4,875 kW prime power**
- With 25% margin: 6,414.5 kVA × 0.95 = **6,093.8 kW**

**RESULT:**
- **Specified:** 2500 kVA = 2,375 kW (at 0.95 PF)
- **Required (no margin):** 4,875 kW
- **Required (with 25% margin):** 6,093.8 kW
- **Shortfall:** 4,875 - 2,375 = **2,500 kW (105.3% overload)**

**✗ CRITICAL ISSUE:** In 2N operation with one generator down for maintenance, the remaining 2500 kVA generator cannot carry the 4,875 kW load. This results in **105.3% overload** (generator would need to produce more than double its rated capacity), violating Tier III concurrent maintainability and **exceeding generator capacity by over 2×**.

---

## SUMMARY TABLE

| Parameter | Group 1 (Phase 1) | Group 2 (Phase 2) |
|-----------|-------------------|-------------------|
| **IT Load** | 2,385 kW | 3,250 kW |
| **Infrastructure Load (PUE 1.5)** | 1,192.5 kW | 1,625 kW |
| **Total Load (kW)** | 3,577.5 kW | 4,875 kW |
| **Total Load (kVA at 0.95 PF)** | 3,765.8 kVA | 5,131.6 kVA |
| | | |
| **TRANSFORMERS (2N Configuration)** | | |
| Specified Capacity | 3,000 kVA | 3,000 kVA |
| Required Capacity (no margin) | 3,765.8 kVA | 5,131.6 kVA |
| Required Capacity (25% margin) | 4,707.2 kVA | 6,414.5 kVA |
| **Shortfall (no margin)** | **-765.8 kVA** | **-2,131.6 kVA** |
| **Overload %** | **25.5%** | **71.1%** |
| | | |
| **GENERATORS (2N Configuration)** | | |
| Specified Capacity | 2,375 kW | 2,375 kW |
| Required Capacity (no margin) | 3,577.5 kW | 4,875 kW |
| Required Capacity (25% margin) | 4,471.8 kW | 6,093.8 kW |
| **Shortfall (no margin)** | **-1,202.5 kW** | **-2,500 kW** |
| **Overload %** | **50.6%** | **105.3%** |

---

## MINIMUM RECOMMENDED EQUIPMENT SIZING

### Group 1 (Phase 1 - 2.385 MW IT)

**Transformers:**
- **Minimum (no margin):** 2 × 3,766 kVA → Use 2 × **4,000 kVA**
- **Recommended (25% margin):** 2 × 4,707 kVA → Use 2 × **5,000 kVA**

**Generators:**
- **Minimum (no margin):** 2 × 3,578 kW → Use 2 × **3,750 kVA** (3,000 kW at 0.8 PF)
- **Recommended (25% margin):** 2 × 4,472 kW → Use 2 × **5,000 kVA** (4,000 kW at 0.8 PF)

### Group 2 (Phase 2 - 3.250 MW IT)

**Transformers:**
- **Minimum (no margin):** 2 × 5,132 kVA → Use 2 × **5,500 kVA**
- **Recommended (25% margin):** 2 × 6,415 kVA → Use 2 × **6,500 kVA** or **7,000 kVA**

**Generators:**
- **Minimum (no margin):** 2 × 4,875 kW → Use 2 × **5,625 kVA** (4,500 kW at 0.8 PF)
- **Recommended (25% margin):** 2 × 6,094 kW → Use 2 × **7,500 kVA** (6,000 kW at 0.8 PF)

---

## ALTERNATIVE: N+1 CONFIGURATION (More Efficient)

Instead of 2N (2 per group), consider N+1 per group for better efficiency and load sharing:

### Group 1: 3 × Smaller Units (N+1)
- **Total Load:** 3,765.8 kVA
- **Per Unit (2 units running):** 3,765.8 kVA ÷ 2 = 1,882.9 kVA per unit
- **With 25% margin:** 1,882.9 × 1.25 = 2,353.6 kVA per unit
- **Recommended:** 3 × **2,500 kVA** transformers or generators (N+1 configuration)

### Group 2: 3 × Larger Units (N+1)
- **Total Load:** 5,131.6 kVA
- **Per Unit (2 units running):** 5,131.6 kVA ÷ 2 = 2,565.8 kVA per unit
- **With 25% margin:** 2,565.8 × 1.25 = 3,207.3 kVA per unit
- **Recommended:** 3 × **3,500 kVA** transformers or generators (N+1 configuration)

**Benefits of N+1:**
- Better load sharing and efficiency at partial loads
- Smaller individual unit sizes (easier to procure, less expensive)
- More granular scalability
- Still maintains concurrent maintainability (Tier III compliant)

---

## CONCLUSION

The mathematical calculations prove that the specified equipment is **critically undersized** for Tier III operation:

1. **Group 1 Transformers:** 25.5% overload in 2N operation
2. **Group 1 Generators:** 50.6% overload in 2N operation
3. **Group 2 Transformers:** 71.1% overload in 2N operation (thermal damage risk)
4. **Group 2 Generators:** 105.3% overload in 2N operation (cannot physically deliver required power)

**This is not a design preference or best practice recommendation - it is a mathematical impossibility for the specified equipment to support the stated IT loads while maintaining Tier III concurrent maintainability.**

---

## CALCULATION ASSUMPTIONS AND VERIFICATION NEEDED

The above calculations are based on the following assumptions. **CAS GmbH should provide their calculations to verify or correct these assumptions:**

1. **Power Factor = 0.95** (typical for modern IT equipment with active PFC)
   - *If actual PF is lower (e.g., 0.9), required kVA increases further*

2. **PUE = 1.5 applied to full IT load** for infrastructure load calculation
   - *If infrastructure load is higher, required capacity increases*

3. **2N configuration** as stated in BOD (each transformer/generator carries full load independently)
   - *If configuration is different, calculations would change*

4. **No diversity factor applied** (100% of IT load assumed simultaneously)
   - *This is standard for Tier III design - diversity factors not typically used*

5. **Load groups match phasing:** Group 1 = Phase 1 (2.385 MW), Group 2 = Phase 2 (3.250 MW)
   - *If load distribution is different, please clarify*

**Request to CAS GmbH:** Please provide transformer and generator sizing calculations showing how 3000 kVA transformers and 2500 kVA generators were determined to be adequate for the stated loads in 2N configuration.

---

**Prepared by:** Design Review Team
**Date:** October 30, 2025
