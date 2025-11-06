**Created:** 2025-11-06
**Updated:** MV voltage changed from 11kV to 10kV
**Tags:** #GGE-data-center #electrical-bod #10kv-distribution #mtm-topology

# ELECTRICAL SYSTEMS - 10kV MV DISTRIBUTION

### **ELECTRICAL SYSTEMS**

#### Primary Utility Service (Dual Sources - MTM Topology)
- **Source 1 - HPP:** Hydroelectric Power Plant (Local)
  - **Incoming voltage:** 400V, 3-phase, 50 Hz (low voltage)
  - **Capacity:** 3.7 MW @ 400V
  - **Step-up required:** 400V → 10 kV via 3,500 kVA step-up transformer
  - **Feeds:** MV-SWBD-A (10 kV) → XFMR-A (step-down) → BUS A (400V)
  - **Geographic path:** Feed 1
- **Source 2 - Utility Grid:** National Grid (Medium Voltage)
  - **Incoming voltage:** 10 kV, 3-phase, 50 Hz (medium voltage)
  - **Capacity:** 4.0 MW @ 10 kV
  - **No step-up needed:** Direct to MV-SWBD-B
  - **Feeds:** MV-SWBD-B (10 kV) → XFMR-B (step-down) → BUS B (400V)
  - **Geographic path:** Feed 2 (diverse from HPP)
- **Configuration:** Main-Tie-Main (MTM) topology at 400V LV level
  - Two independent utility sources at different voltages
  - Redundant MV switchboards (10 kV) for isolation and protection
  - Automatic tie breaker (52-TIE) between LV buses (normally open @ 400V)
  - Either source can carry full facility load via tie breaker
- **Reliability:** Dual diverse utility sources + 2N MTU backup = triple redundancy

#### HPP Step-Up Transformer (400V → 10 kV)
- **Purpose:** Convert HPP low-voltage output to medium voltage for distribution
- **Rating:** 3,500 kVA, 400V / 10 kV, Dyn11, oil-filled ONAN
- **Input:** HPP @ 400V (3.7 MW max)
- **Output:** 10 kV to MV-SWBD-A
- **Concurrent maintenance:** Close 52-TIE, feed facility from Grid source only
- **Note:** Unique to HPP source (Grid is already at 10 kV, no step-up needed)

#### Medium Voltage Switchboards (10 kV)
- **MV-SWBD-A:** Fed from HPP step-up transformer
  - 630A bus, VCB lineup, 10 kV
  - Feeds XFMR-A (step-down transformer)
- **MV-SWBD-B:** Fed from Utility Grid
  - 630A bus, VCB lineup, 10 kV
  - Feeds XFMR-B (step-down transformer)
- **Redundancy:** Independent switchboards, either can be maintained
- **Protection:** VCBs (Vacuum Circuit Breakers) with overcurrent, short-circuit, ground fault

#### Step-Down Transformers (10 kV → 400V)
- **Configuration:** 2N redundancy (Tier III concurrent maintainability)
- **Transformer A (XFMR-A):** 3,500 kVA, 10 kV / 400V, Dyn11, oil-filled ONAN
  - Fed from MV-SWBD-A (HPP path)
  - Feeds BUS A (SWBD-A) via ACB-M1 (6,300A frame, 5,000A trip)
  - Sized for 100% facility load (2,078 kW failure mode)
- **Transformer B (XFMR-B):** 3,500 kVA, 10 kV / 400V, Dyn11, oil-filled ONAN
  - Fed from MV-SWBD-B (Grid path)
  - Feeds BUS B (SWBD-B) via ACB-M2 (6,300A frame, 5,000A trip)
  - Sized for 100% facility load (2,078 kW failure mode)
- **Concurrent maintenance:** Either transformer can be isolated at MV switchboard; tie breaker transfers load to remaining source
- **Brands:** Schneider Electric, ABB, or Siemens (standard availability in Georgia/Turkey)

#### Backup Power - MTU Kinetic PowerPack (Rotary UPS)
- **Units:** 2 × MTU KP7 Kinetic PowerPack
- **Capacity per unit:** 2,750 kVA / 2,200 kW (Data Center Continuous Power rating)
- **Total installed:** 5,500 kVA / 4,400 kW
- **Configuration:** 2N (true fault tolerance - either unit carries 100% load)
- **Technology:** Diesel engine + kinetic flywheel energy storage
- **Ride-through:** 15-20 seconds (flywheel) while diesel engine starts
- **Output voltage:** 400V, 3-phase, 50 Hz
- **Tier compliance:** Uptime Institute Tier I-IV certified
- **Advantage:** Integrated UPS + generator in single package (no separate static UPS required)
- **Fuel:** Diesel, [TBD] liters storage, [TBD] hour runtime at full load
- **Emissions:** EU Nonroad Stage II compliant

#### Critical Power Distribution (400V - MTM)
- **Voltage:** 400V throughout (matches utility voltage after transformation)
- **Topology:** Main-Tie-Main (MTM) with automatic tie breaker
- **Configuration:** Dual path (BUS A + BUS B)

**BUS A (SWBD-A) - 2,500A Bus:**
- Primary source: HPP via XFMR-A (normal mode)
- Backup source: Grid via 52-TIE (single source failure mode)
- Backup power: MTU-1 via ACB-MTU1 (utility failure)
- Normal load: 1,039 kW (735 kW IT + 304 kW cooling)
- Failure load: 2,078 kW (full facility if Grid fails)

**BUS B (SWBD-B) - 2,500A Bus:**
- Primary source: Grid via XFMR-B (normal mode)
- Backup source: HPP via 52-TIE (single source failure mode)
- Backup power: MTU-2 via ACB-MTU2 (utility failure)
- Normal load: 1,096 kW (735 kW IT + 361 kW cooling)
- Failure load: 2,078 kW (full facility if HPP fails)

**52-TIE (Tie Breaker):**
- Rating: 6,300A frame, 5,000A trip setting
- Type: Drawout ACB with electronic trip
- Normal state: OPEN (buses operate independently)
- Automatic close: On loss of either utility source
- Purpose: Transfer full facility load to remaining utility source

**Distribution Panels:**
- **A-IT-1:** 2,500A MCCB, feeds IT loads (735 kW) from BUS A
- **B-IT-1:** 2,500A MCCB, feeds IT loads (735 kW) from BUS B
- **A-COOL-1:** 3,200A MCCB, feeds cooling loads (304 kW) from BUS A
- **B-COOL-1:** 3,200A MCCB, feeds cooling loads (361 kW) from BUS B

**Cabinet Power:** Dual PDUs per cabinet (A+B)
- PDU-A fed from A-IT-1 (BUS A)
- PDU-B fed from B-IT-1 (BUS B)
- IT equipment: Dual-corded with automatic failover

**All cooling loads on critical power:**
- CHW Pumps, CW Pumps, River Water Pumps
- In-row cooling units
- Chillers
- All backed by MTU Kinetic PowerPacks

#### Non-Critical Office Power (Separate SWBD)
- **SWBD-OFFICE:** 630A bus, 400V
- **Primary source:** On-site solar array (700 kW AC via inverters)
- **Backup source:** Utility Grid (250 kVA transformer, 10 kV / 400V)
- **Transfer:** Automatic Transfer Switch (ATS) with solar priority
- **Load:** 103 kW diversified (HVAC, lighting, IT office, security, misc)
- **No UPS or generator backup** (non-critical loads only)

#### Electrical Code Compliance
- **Standards:** IEC 60364 (Georgian electrical code based on IEC)
- **Grounding:** TN-S system (separate protective earth)
- **Arc flash:** Study and labeling per IEC 61482
- **Testing:** Factory acceptance tests (FAT) + site acceptance tests (SAT)

---

## KEY CHANGES FROM 11kV TO 10kV

**Voltage Level Update:**
- All medium voltage equipment changed from 11kV to 10kV
- HPP step-up transformer: 400V / 10kV (was 400V / 11kV)
- MV switchboards: 10kV rated (was 11kV)
- Step-down transformers: 10kV / 400V (was 11kV / 400V)
- Office transformer: 10kV / 400V (was 11kV / 400V)
- Utility Grid incoming: 10kV (was 11kV)

**Equipment Impact:**
- Transformer insulation class may change (10kV standard vs 11kV)
- VCB ratings adjusted for 10kV system
- Cable sizing may be slightly larger due to lower voltage (same power, lower voltage = higher current)

**No Change:**
- LV distribution remains 400V throughout
- All 400V equipment unchanged
- MTU Kinetic PowerPack output: 400V (unchanged)
- Control and protection philosophy: same
- MTM topology: unchanged

**Advantages of 10kV:**
- More standard voltage in some European/Asian markets
- Potentially better equipment availability
- Transformer and switchgear cost may be lower (more common voltage class)

---

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main BOD document
- [[7BOD - Electrical (CSI Div 26)]] - Detailed electrical specifications
- [[GGE_Electrical_Design_REVISED_MTM]] - MTM topology design details
