# Equipment Pricing Database

**Created:** 2025-11-20
**Last Updated:** 2025-11-20
**Tags:** #pricing #equipment #financial-modeling #data-center
**Data Valid As Of:** 2025-11-20

---

## Database Overview

This database contains equipment pricing from multiple vendors/sellers for data center equipment. Prices include UPS systems, transformers, chillers, generators, busway systems, CRAH units, and other critical infrastructure components.

**Key Sellers:**
- CERIO (UPS, Busway, Generators)
- JCI (Chillers, Fan Walls)
- JCL ENERGY (Transformers)
- MCG (Modules, Switchgear, Generators)
- SVL (DOAS, Humidifiers, CRAH)
- TEXAS AIR SYSTEMS (Pump Skids, Thermal Storage)
- EAE (Reserve Busduct)
- HYDRAQUIP (Couplers)
- T5 (Generators)
- GIGA ENERGY (Transformers)
- STARLINE (Busway CX)

---

## Equipment Categories

### 1. UPS Systems (Uninterruptible Power Supply)

| Seller | OEM | Model | Capacity | Unit Price | Notes |
|--------|-----|-------|----------|------------|-------|
| CERIO | DELTA | DELTA-1250KVA-UPS | 1250 kVA | $352,910.96 | Large capacity UPS |
| CERIO | DELTA | DELTA-250KVA-UPS | 250 kVA | $119,010.13 | Medium capacity UPS |

### 2. Static Transfer Switches (STS)

| Seller | OEM | Model | Rating | Unit Price | Notes |
|--------|-----|-------|--------|------------|-------|
| CERIO | DELTA | DELTA-800A-STS | 800A | $92,650.00 | Standard STS |
| MCG | ABB | ABB-800A-STS | 800A | $104,331.50 | Alternative vendor |

### 3. Busway Systems

| Seller | OEM | Model | Rating | Unit Price | Notes |
|--------|-----|-------|--------|------------|-------|
| CERIO | DELTA | DELTA-400A-BUSWAY | 400A | $76,600.24 | Standard busway |
| CERIO | DELTA | DELTA-600A-BUSWAY | 600A | $76,600.24 | Standard busway |
| CERIO | DELTA | DELTA-800A-BUSWAY | 800A | $76,600.24 | Standard busway |
| CERIO | DELTA | DELTA-63A-PIU | 63A PIU | INCLUDED IN BUSWAY | Plug-in units included |
| STARLINE | STARLINE | STARLINE-L2 CX-BUSWAY | L2 CX | $12,050.00 | Commissioning support |

### 4. Reserve Busduct Systems

| Seller | OEM | Model | Rating | Unit Price | Notes |
|--------|-----|-------|--------|------------|-------|
| EAE | EAE | EAE-4000A-RESERVE BUSDUCT | 4000A | $932.00 | Per linear foot/section |
| EAE | EAE | EAE-800A-RESERVE BUSDUCT TAP BOX | 800A Tap | INCLUDED IN RBUS | Included with busduct |

### 5. Transformers

#### 13.2kV Transformers

| Seller | OEM | Model | Voltage | Cooling | Unit Price | Notes |
|--------|-----|-------|---------|---------|------------|-------|
| JCL ENERGY | JCL ENERGY | JCL ENERGY-2550KVA 13.2KV KNAN-TRANSFORMER | 13.2kV | KNAN | $109,495.00 | Natural cooling |
| JCL ENERGY | JCL ENERGY | JCL ENERGY-2550KVA 13.2KV KNAF-TRANSFORMER | 13.2kV | KNAF | $112,595.00 | Forced air cooling |

#### 18kV Transformers

| Seller | OEM | Model | Voltage | Cooling | Unit Price | Notes |
|--------|-----|-------|---------|---------|------------|-------|
| GIGA ENERGY | GIGA ENERGY | GIGA ENERGY-2550KVA 18KV KNAN-TRANSFORMER | 18kV | KNAN | $78,317.00 | Natural cooling |
| GIGA ENERGY | GIGA ENERGY | GIGA ENERGY-2550KVA 18KV KNAF-TRANSFORMER | 18kV | KNAF | $93,981.00 | Forced air cooling |

#### 34.5kV Transformers

| Seller | OEM | Model | Voltage | Cooling | Unit Price | Notes |
|--------|-----|-------|---------|---------|------------|-------|
| JCL ENERGY | JCL ENERGY | JCL ENERGY-2550KVA 34.5KV KNAN-TRANSFORMER | 34.5kV | KNAN | $20,994.28 | Natural cooling |
| JCL ENERGY | JCL ENERGY | JCL ENERGY-2550KVA 34.5KV KNAF-TRANSFORMER | 34.5kV | KNAF | $20,994.28 | Forced air cooling |
| JCL ENERGY | VTC | VTC-2550KVA 34.5KV KNAN-TRANSFORMER | 34.5kV | KNAN | $20,994.28 | VTC OEM option |
| JCL ENERGY | VTC | VTC-2550KVA 34.5KV KNAF-TRANSFORMER | 34.5kV | KNAF | $20,994.28 | VTC OEM option |

### 6. Generators

| Seller | OEM | Model | Capacity | Unit Price | Notes |
|--------|-----|-------|----------|------------|-------|
| CERIO | KOHLER | KOHLER-3MW-GENERATOR | 3.0 MW | $2,450,000.00 | Large capacity |
| MCG | KOHLER | KOHLER-2.8MW-GENERATOR | 2.8 MW | $1,470,000.00 | Slightly smaller |
| MCG | MCFI | KOHLER-3.5MW-GENERATOR | 3.5 MW | $2,460,500.00 | Largest capacity |
| T5 | CAT | CAT-1.25MW-GENERATOR | 1.25 MW | $827,682.44 | Caterpillar brand |

### 7. Switchgear & Distribution

| Seller | OEM | Model | Type | Unit Price | Notes |
|--------|-----|-------|------|------------|-------|
| MCG | ABB | ABB-38KV 330-MV SWG | 38kV MV Switchgear | $183,333.33 | 330A rating |
| MCG | ABB | ABB-38KV 210-MV SWG | 38kV MV Switchgear | $183,333.33 | 210A rating |
| MCG | POINT EIGHT POWER | PEP-1.25MW CAT-SWITCHBOARD | Switchboard | $365,949.82 | For CAT generators |
| MCG | CUMMINS | CUMMINS-70A-ATS | 70A ATS | $11,851.38 | Automatic transfer switch |

### 8. Chillers

| Seller | OEM | Model | Capacity | Unit Price | Notes |
|--------|-----|-------|----------|------------|-------|
| JCI | JCI | JCI-500T-115-CHILLER | 500 Ton | $583,361.53 | Large capacity chiller |
| JCI | JCI | JCI-HAIL LOUVERS-CHILLER | Accessory | $8,800.00 | Hail protection |

### 9. Cooling Systems - CRAH/DOAS

#### CRAH Units

| Seller | OEM | Model | Capacity | Unit Price | Notes |
|--------|-----|-------|----------|------------|-------|
| SVL | DADEX | DADEX-60KW-CRAH | 60 kW | $72,800.00 | Computer room air handler |

#### DOAS Units

| Seller | OEM | Model | Model # | Unit Price | Notes |
|--------|-----|-------|---------|------------|-------|
| SVL | AAON | AAON-RQA-005-DOAS | RQA-005 | $66,718.75 | Dedicated outdoor air |
| SVL | AAON | AAON-RQA-011-DOAS | RQA-011 | $66,718.75 | Dedicated outdoor air |

### 10. Fan Walls

| Seller | OEM | Model | Capacity | Unit Price | Notes |
|--------|-----|-------|----------|------------|-------|
| JCI | JCI | JCI-72K-FAN WALL | 72K CFM | $113,810.76 | Standard fan wall |
| JCI | JCI | JCI-FAN WALL FILTER RACK G1-REPAIR | Repair G1 | $16,875.00 | Filter rack repair |
| JCI | JCI | JCI-FAN WALL FILTER RACK G2-REPAIR | Repair G2 | $17,815.00 | Filter rack repair |
| JCI | JCI | JCI-FAN WALL IST CX-OVERTIME | CX Support | $35,630.00 | Commissioning OT |

### 11. Humidifiers

| Seller | OEM | Model | Model # | Unit Price | Notes |
|--------|-----|-------|---------|------------|-------|
| SVL | CONDAIR | CONDAIR-RS-030-HUMIDIFIER | RS-030 | $11,400.00 | Standard pricing |
| SVL | CONDAIR | CONDAIR-RS-030-HUMIDIFIER | RS-030 | $9,710.71 | Volume pricing |

### 12. Pump Systems

| Seller | OEM | Model | Type | Unit Price | Notes |
|--------|-----|-------|------|------------|-------|
| TEXAS AIR SYSTEMS | FISEN | FISEN-YVFA0459-CHILLED WATER PUMP SKID | Pump Skid | $80,458.00 | Chilled water system |

### 13. Thermal Storage Tanks

| Seller | OEM | Model | Capacity/Type | Unit Price | Notes |
|--------|-----|-------|---------------|------------|-------|
| TEXAS AIR SYSTEMS | WENDLAND | WENDLAND-15000 GAL HORIZONTAL-THERMAL STORAGE TANK | 15,000 gal Horizontal | $407,949.00 | Horizontal configuration |
| TEXAS AIR SYSTEMS | WENDLAND | WENDLAND-30000 GAL VERTICAL-THERMAL STORAGE TANK | 30,000 gal Vertical | $407,949.00 | Vertical configuration |
| TEXAS AIR SYSTEMS | WENDLAND | WENDLAND-30000 GAL HORIZONTAL-THERMAL STORAGE TANK | 30,000 gal Horizontal | $407,949.00 | Horizontal configuration |

### 14. Modular Systems

| Seller | OEM | Model | Type | Unit Price | Notes |
|--------|-----|-------|------|------------|-------|
| MCG | MCFI | MCFI-IT-MODULE | IT Module | $1,406,767.94 | Complete IT infrastructure module |
| MCG | MCFI | MCFI-MECH-MODULE | Mechanical Module | $1,406,767.94 | Complete mechanical module |

### 15. Piping Components

| Seller | OEM | Model | Type | Unit Price | Notes |
|--------|-----|-------|------|------------|-------|
| HYDRAQUIP | DANFOSS | DANFOSS-2" FD83-COUPLER | 2" Coupler | $526.30 | Quick disconnect coupling |

### 16. Commissioning Services

| Seller | OEM | Service | Type | Unit Price | Notes |
|--------|-----|---------|------|------------|-------|
| SVL | SVL | SVL-IST CX SUPPORT-CAMPUS | CX Support | $186,300.00 | Campus-wide IST/CX |
| TEXAS AIR SYSTEMS | TEXAS AIR SYSTEMS | TAS-IST CX SUPPORT-CAMPUS | CX Support | $419,530.00 | Campus-wide IST/CX |
| STARLINE | STARLINE | STARLINE-L2 CX-BUSWAY | L2 CX | $12,050.00 | Busway commissioning |

---

## Pricing Analysis Notes

### Key Observations:

1. **Transformer Pricing Anomaly:** The 34.5kV transformers ($20,994.28) appear significantly cheaper than 13.2kV ($109,495) and 18kV transformers ($78,317). This may warrant verification - could be pricing per kVA or different unit of measure.

2. **Busway Pricing:** All DELTA busway amperage ratings (400A, 600A, 800A) show identical unit pricing at $76,600.24, which may indicate package pricing or different units of measure.

3. **Modular Systems:** MCFI modules (IT and Mechanical) are identical in price at $1,406,767.94 per unit - these are complete infrastructure modules.

4. **Thermal Storage:** All WENDLAND thermal storage tanks priced identically at $407,949.00 despite different capacities (15K vs 30K gallons) - verify if this is correct.

---

## Quick Reference - Common Equipment

### Typical Data Hall Build (Per Hall)

| Component | Qty | Unit Price | Extended |
|-----------|-----|------------|----------|
| DELTA 1250kVA UPS | 42 | $352,910.96 | $14,822,260 |
| DELTA 250kVA UPS | 30 | $119,010.13 | $3,570,304 |
| DELTA 800A STS | 72 | $92,650.00 | $6,670,800 |
| JCI 500T Chiller | 30 | $583,361.53 | $17,500,846 |
| JCI 72K Fan Wall | 38 | $113,810.76 | $4,324,809 |

### Campus Infrastructure

| Component | Qty | Unit Price | Extended |
|-----------|-----|------------|----------|
| KOHLER 3MW Generator | 4 | $2,450,000.00 | $9,800,000 |
| 34.5kV KNAN Transformer | 21 | $20,994.28 | $440,880 |
| EAE 4000A Reserve Bus | 1114 | $932.00 | $1,038,248 |

---

## Data Quality & Validation

**Status:** Initial database creation - 2025-11-20

**Items Requiring Verification:**
1. 34.5kV transformer pricing (unusually low compared to lower voltages)
2. Busway identical pricing across amperage ratings
3. Thermal storage tank pricing (same price for different capacities)
4. Confirm units of measure for all equipment (each, per foot, per section, etc.)

**Next Steps:**
- Cross-reference with historical pricing data
- Verify with vendors on flagged items
- Add escalation factors for future year projections
- Integrate with project budgets

---

## Version History

| Date | Version | Changes | Updated By |
|------|---------|---------|------------|
| 2025-11-20 | 1.0 | Initial database creation from vendor quotes | Claude |

