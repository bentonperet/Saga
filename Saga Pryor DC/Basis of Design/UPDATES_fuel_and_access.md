# Updates to Generator Fuel System and Equipment Yard Access

## Generator Fuel System Updates

### Current Specification (TO BE REPLACED):
- 10,000 gal belly tanks per generator
- 118 hours runtime per unit
- Difficult to source, expensive

### NEW Specification:

**Belly Tanks:**
- ~2,000 gallon belly tank per generator (cost-effective, easy to source)
- Connected via common fuel manifold

**Bulk Fuel Storage:**
- Separate above-ground or underground tank farm
- **24-hour minimum runtime** (not 118 hours)
- Phase 2 capacity: ~12,000 gallons (5 generators × 85 gal/hr × 24 hr + 10% reserve = ~11,250 gal)
- Fill connections located just outside equipment yard perimeter
- **Redundant fuel service contracts with SLAs** for 24-hour refueling

**Common Manifold:**
- Connects all generator belly tanks to bulk storage
- Allows fuel sharing across all units
- Simplified refueling - single fill point to bulk storage

**Rationale:**
- 24-hour runtime sufficient with redundant fuel contracts
- 2,000 gal belly tanks readily available and cost-effective
- Easier installation and maintenance
- Bulk storage more economical than oversized belly tanks

---

## Equipment Yard Access Provisions

### Emergency/Maintenance Access:
- **East-west access points** in equipment yards for:
  - Emergency vehicle access
  - Escorted maintenance equipment ingress/deliveries
  - Temporary rental equipment (load banks, generators, chillers)

### Cable Pass-Through Doors:
- **Multiple small access doors** (~dog door sized) in building envelope
- Purpose: Pass cables from secure equipment yard into building
- Supports temporary/rental equipment connections:
  - Load banks
  - Temporary generators
  - Backup chillers
  - Testing equipment

---

## Chiller Piping Provisions

### Temporary Equipment Connection Points:

**Bypass Valves:**
- Appropriate bypass piping on all chiller loops
- Allows isolation of individual chillers for maintenance
- Enables temporary chiller connection during repairs

**Quick-Connect Points:**
- Camlock or similar quick-connect fittings
- Located at strategic points on each cooling loop
- Sized for temporary chiller capacity

**Rental Equipment Support:**
- Connection points sized for standard rental chiller capacities
- Pressure/temperature ratings compatible with facility systems
- Access from equipment yard through cable pass-through doors or dedicated piping penetrations

**Documentation:**
- As-built drawings showing all connection points
- Rental equipment compatibility specifications
- Emergency procedures for temporary equipment deployment

---

## Files to Update:

1. **7BOD - Electrical (CSI Div 26).md**
   - Generator fuel capacity: Change from "10,000 gal belly tank" to "~2,000 gal belly tank + bulk storage"
   - Add bulk storage details
   - Add equipment yard access provisions

2. **_BOD - Exec Summary and TOC.md**
   - Update fuel capacity summary
   - Change from "118 hours" to "24-hour minimum runtime"

3. **5BOD - HVAC (CSI Div 23).md**
   - Add chiller bypass valve provisions
   - Add temporary equipment connection points
   - Document rental equipment support

4. **10BOD - Site and Infrastructure (CSI Divs 31-32).md**
   - Add equipment yard east-west access points
   - Add cable pass-through door locations

---

**Date:** 2025-10-30
**Status:** TO BE IMPLEMENTED
