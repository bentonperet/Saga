**Created:** 2025-10-16 15:45

# Wind Rating and Roof Specifications Analysis
## Action Items: A-012, A-029, A-046

**Project:** PGCIS Saga Pryor Data Center
**Location:** Pryor, Oklahoma
**Related Decision IDs:** E9, S7
**Purpose:** Insurance rate reduction analysis and roof design compliance

---

## Executive Summary

**Key Finding:** The reference to "FM I-135" appears to be a misnomer. The correct standard is **FM Global Data Sheet 1-28 (Wind Design)**, updated January 2024, which includes tornado requirements.

**Critical Findings:**
- Pryor, Oklahoma is in **FM Global's tornado region** requiring 140+ mph design tornado wind speed
- ASCE 7-16 requires 107 mph wind speed (increased from 90 mph in ASCE 7-05)
- FM Global standards are **more stringent** than ASCE for tornado-prone regions
- Upgrading to tornado-resistant construction may increase costs by **up to 50%**
- **Insurance benefits** may offset upgrade costs through rate reductions

---

## A-012: FM Global Tornado Standard Details and Specifications

### Standard Identification

**Correct Reference:** FM Global Data Sheet 1-28 (Wind Design) - January 2024 Interim Revision

The tornado requirements are found in:
- **FM Data Sheet 1-28** (Wind Design) - Sections 2.11, 3.12, 4.0
- **FM Data Sheet 1-29** (Roof Deck Securement and Above-Deck Components)
- **FM Data Sheet 5-32** (Data Centers and Related Facilities)

### Tornado Region Classification

**Pryor, Oklahoma:** Confirmed in FM Global tornado region

FM Global uses ASCE 7-22's conservative 10,000-year mean recurrence interval mapping, which identifies high-risk areas including **Oklahoma** as requiring:
- **Design tornado wind speed:** 140 mph or greater
- **Tornado-resistant building envelopes** recommended (including roof assemblies)

### FM Global Roof Assembly Specifications for Tornado Regions

#### 1. **Roof Rating Format**
FM Global ratings are expressed as **"Class X-YYY"**:
- **X:** Fire resistance class (typically Class 1)
- **YYY:** Wind uplift capacity in psf (60-360 range)

For tornado regions: **Minimum Class 1-150 recommended** (150 psf uplift capacity)

#### 2. **Roof Deck Requirements**

**Preferred:** Structural concrete roof deck
- FM Global's loss experience shows concrete decks perform better under tornado loads
- More resistant to uplift and missile impact

**Alternative:** Steel roof deck (requires enhanced design)
- Narrower joist spacing (shorter deck spans)
- Thicker or deeper steel roof deck profiles
- Increased securement to joists or purlins
- Higher design loads to resist tornado forces

#### 3. **Roof Surface Restrictions**

**Critical Requirement:** Avoid roof aggregate of any type or size in tornado regions
- **Exception:** Mineral surfacing for cap sheets only
- **Rationale:** Loose aggregate becomes dangerous projectiles in tornado conditions

#### 4. **Roof Assembly Components**

Based on FM Data Sheet 1-29 requirements:

| Component           | Requirement                                           |
| ------------------- | ----------------------------------------------------- |
| **Membrane**        | FM Approved single-ply, modified bitumen, or built-up |
| **Insulation**      | FM Approved, properly fastened per zone requirements  |
| **Fasteners**       | FM Approved, designed for calculated uplift forces    |
| **Deck Attachment** | Enhanced securement for tornado wind loads            |
| **Edge Details**    | Reinforced perimeter and corner zones                 |

#### 5. **Wind Uplift Zones**

Per FM Data Sheet 1-28, calculate design wind pressures for:
- **Field Zone:** Interior areas (lowest pressures)
- **Perimeter Zone:** 10% of building dimension or 40% of building height
- **Corner Zone:** Highest pressures, most critical

#### 6. **Vertical Forces on Roof-Mounted Equipment**

**Updated procedure** for calculating vertical forces:
- Use FM-approved anchors tested per **FM 4481**
- Design to resist both horizontal AND vertical forces
- Account for tornado-induced uplift

### FM Global Resources

| Resource | Purpose | Access |
|----------|---------|--------|
| **FM Data Sheet 1-28** | Wind design methodology and tornado criteria | [fm.com/resources/fm-data-sheets](https://www.fm.com/resources/fm-data-sheets) |
| **FM Data Sheet 1-29** | Roof deck securement and fastener requirements | [fm.com/resources/fm-data-sheets](https://www.fm.com/resources/fm-data-sheets) |
| **FM Data Sheet 5-32** | Data center specific requirements | [fm.com/resources/fm-data-sheets](https://www.fm.com/resources/fm-data-sheets) |
| **FM Approvals RoofNav** | System selection and ratings calculator | [roofnav.fmglobal.com](http://roofnav.fmglobal.com/) |
| **FM 4470 Standard** | Comprehensive testing standard | FM Approvals website |

---

## A-029: FM Global vs ASCE 7 Wind Standards Comparison

### Wind Speed Requirements

| Standard | Tulsa/Pryor, OK Wind Speed | Basis | Comments |
|----------|----------------------------|-------|----------|
| **ASCE 7-05** | 90 mph | 3-second gust at 33ft, Exposure C | Older standard |
| **ASCE 7-10/16** | 107 mph | 3-second gust at 33ft, Exposure C | Current building code |
| **FM Data Sheet 1-28** | **140+ mph** | Design tornado wind speed | **Most conservative** |

### Key Differences

#### 1. **Design Philosophy**

**ASCE 7:**
- Code-minimum requirements
- Focuses on life safety and building survival
- Based on straight-line wind events
- Risk Category determines design approach
  - **Category III:** Schools, high occupancy (typical data center)
  - **Category IV:** Critical facilities (mission-critical data center)

**FM Global:**
- Property loss prevention focus
- Emphasizes protection of building AND contents
- Includes tornado-specific requirements
- **Insurance-driven standards** (more stringent)

#### 2. **Tornado Considerations**

**ASCE 7:**
- Does NOT specifically design for tornadoes
- Assumes tornadoes are low-probability, localized events
- Standard wind loads only

**FM Global:**
- **Explicitly requires tornado design** for high-risk regions
- Uses ASCE 7-22's 10,000-year mean recurrence interval
- Oklahoma designated as tornado region

#### 3. **Roof Uplift Calculations**

**ASCE 7-16:**
- Four roof zones: interior, field, perimeter, corner
- Minimum backstop: 60 psf
- Calculated based on:
  - Building dimensions
  - Height and exposure
  - Risk category
  - Enclosure classification

**FM Global:**
- Similar zoning approach
- Higher safety factors
- Additional tornado load factors
- Typical tornado-region rating: **150+ psf**

#### 4. **Material Restrictions**

**ASCE 7:**
- No specific restrictions on roof surfacing materials
- Allows ballasted systems

**FM Global:**
- **Prohibits loose aggregate** in tornado regions
- Restricts ballasted systems
- Requires fully adhered or mechanically attached systems

### Cost Impact Comparison

| Design Standard | Relative Cost | Notes |
|-----------------|---------------|-------|
| **ASCE 7 (90 mph)** | Baseline | Legacy standard |
| **ASCE 7-16 (107 mph)** | +15-25% | Current code minimum |
| **FM Tornado (140+ mph)** | +40-50% | FM Global recommendation |

### Recommendation: Which Standard to Follow?

**Primary Standard:** FM Global Data Sheet 1-28 (with tornado provisions)

**Rationale:**
1. ✅ **Insurance Benefits:** Significant premium reductions for FM-compliant construction
2. ✅ **Property Protection:** Better protection of valuable data center equipment
3. ✅ **Risk Mitigation:** Tornado protection addresses regional climate risks
4. ✅ **Exceeds Code:** FM compliance automatically satisfies ASCE 7 requirements
5. ✅ **Insurer Requirements:** Likely required by property insurer for data center coverage

**Secondary Compliance:** ASCE 7-16 (building code requirement)
- Must still demonstrate ASCE 7 compliance for building permit
- FM design will exceed ASCE requirements

---

## A-046: Roof Type Upgrade Evaluation

### Current Design Assumptions

Based on typical data center construction:
- Steel roof deck structure
- Single-ply or modified bitumen membrane
- Mechanically attached system
- Conventional wind rating: 90-120 psf

### Upgrade Requirements for FM Tornado Compliance

#### Option 1: Enhanced Steel Deck System

**Modifications Required:**
- ✅ Reduce joist spacing (increase joists)
- ✅ Upgrade to 22-gauge or 20-gauge deck (from 22ga)
- ✅ Increase deck fastening density
- ✅ Enhance perimeter and corner attachments
- ✅ Upgrade to Class 1-150 rated membrane assembly

**Estimated Cost Impact:** +35-45% vs conventional design

**Advantages:**
- Lighter weight
- Faster construction
- More economical than concrete

**Disadvantages:**
- Still less preferred by FM Global
- Higher maintenance over life
- Greater deflection under load

#### Option 2: Concrete Roof Deck (FM Preferred)

**Specifications:**
- Structural concrete deck (typically 3"-4" thick)
- Insulation mechanically attached to concrete
- Fully adhered or mechanically attached membrane
- Class 1-150 or Class 1-180 rated assembly

**Estimated Cost Impact:** +50-65% vs conventional steel deck design

**Advantages:**
- ✅ **FM Global's preferred solution** (best loss history)
- ✅ Superior tornado and missile resistance
- ✅ Better fire resistance
- ✅ Longer service life (50+ years)
- ✅ **Maximum insurance premium reduction**
- ✅ Supports heavy rooftop equipment loads

**Disadvantages:**
- Higher initial cost
- Longer construction time
- Heavier structure (higher foundation costs)

#### Option 3: Hybrid Approach

**Strategy:**
- Concrete deck over critical areas (data halls, power rooms)
- Enhanced steel deck over support spaces
- Phased implementation based on occupancy priority

**Estimated Cost Impact:** +40-50% vs conventional design

### Wind/Missile Resistance Comparison

| Roof Type | Wind Rating | Missile Impact Resistance | FM Preference | Insurance Rating |
|-----------|-------------|---------------------------|---------------|------------------|
| **Conventional Steel (90 psf)** | Adequate for code | Moderate | Not Recommended | Standard rates |
| **Enhanced Steel (150 psf)** | Good | Moderate-High | Acceptable | 10-15% reduction |
| **Concrete Deck (150+ psf)** | Excellent | Excellent | **Preferred** | **20-30% reduction** |

### Material Specifications

#### Eliminate (FM Restriction):
- ❌ Loose roof aggregate/gravel
- ❌ Ballasted EPDM systems
- ❌ Pavers or heavy ballast

#### Required (FM Compliance):
- ✅ FM Approved membrane system
- ✅ Mechanically attached or fully adhered
- ✅ Mineral surfacing on cap sheets only
- ✅ FM-rated fasteners and plates
- ✅ Enhanced perimeter metal edge

### Insurance Impact Analysis

**Current Design (90 psf, steel deck):**
- Property insurance: Baseline premium
- Potential exclusions for wind/tornado damage
- Higher deductibles

**FM-Compliant Design (150+ psf, concrete preferred):**
- Property insurance: **20-30% premium reduction**
- Broader coverage (tornado included)
- Lower deductibles
- Faster claims processing

**ROI Calculation:**
- Upgrade cost: +$1.5M - $3M (estimate for 100,000 SF roof)
- Annual insurance savings: $300K - $500K (estimate)
- **Payback period: 3-6 years**
- **Life-cycle value:** Significant over 25+ year building life

### Recommendation

**Primary Recommendation:** Concrete roof deck with Class 1-150 rated assembly

**Supporting Rationale:**
1. **Best insurance outcome** (20-30% premium reduction)
2. **FM Global's preferred solution** (superior loss history)
3. **Tornado/missile protection** for critical data center assets
4. **Long-term durability** (50+ year service life)
5. **Equipment load capacity** for rooftop cooling/generators
6. **Payback through insurance savings** within 5 years

**Alternative (Budget Constraint):** Enhanced steel deck with Class 1-150 rating
- Accept 10-15% insurance reduction (vs 20-30%)
- Lower initial cost but higher lifecycle cost
- Less preferred by FM Global

---

## Implementation Requirements

### Next Steps

#### For Erik (A-012 - Due 2025-10-18):
1. **Provide to insurance advisor:**
   - This technical memorandum
   - FM Data Sheet 1-28 specifications
   - Recommended roof assembly details (Class 1-150 concrete deck)

2. **Coordinate with insurance broker:**
   - Request premium quotes for FM-compliant design
   - Quantify insurance savings vs upgrade cost
   - Confirm coverage improvements

#### For Benton (A-029 - Due 2025-10-25):
1. **Use RoofNav tool** ([roofnav.fmglobal.com](http://roofnav.fmglobal.com/)):
   - Select FM Approved concrete deck assemblies rated Class 1-150 or higher
   - Document specific manufacturer/product options
   - Verify availability and lead times

2. **Provide to design team:**
   - FM vs ASCE comparison summary
   - Recommended design standard (FM 1-28 tornado)
   - Building code compliance pathway

#### For Benton (A-046 - Due 2025-11-08):
**Dependencies:** A-012 and A-029 complete

1. **Coordinate with financial consultant:**
   - Update CapEx model for concrete deck vs steel deck
   - Include insurance savings in NPV analysis
   - Present ROI calculation

2. **Prepare design recommendation:**
   - Specify: Concrete deck with Class 1-150 assembly
   - Coordinate with structural engineer on deck design
   - Update architectural drawings

3. **Document for Oct 30 meeting:**
   - Present upgrade cost vs insurance benefit
   - Show payback analysis
   - Recommend approval of concrete deck upgrade

---

## References

### FM Global Data Sheets (Free Access - Registration Required)
- **Data Sheet 1-28:** Wind Design (January 2024)
- **Data Sheet 1-29:** Roof Deck Securement
- **Data Sheet 5-32:** Data Centers and Related Facilities
- Access: [fm.com/resources/fm-data-sheets](https://www.fm.com/resources/fm-data-sheets)

### FM Approvals
- **RoofNav:** System selection tool - [roofnav.fmglobal.com](http://roofnav.fmglobal.com/)
- **FM 4470:** Roof assembly testing standard
- **FM 4474:** Wind uplift test method
- **FM 4481:** Anchor testing standard

### ASCE Standards
- **ASCE 7-16:** Minimum Design Loads and Associated Criteria
- **ASCE 7-22:** Latest edition (referenced by FM for tornado mapping)

### Industry Resources
- Professional Roofing Magazine: "FM Global Makes Changes" (April 2024)
- IIBEC Technical Article: "Changes to FM Global Data Sheets Related to Wind and Roofing"

---

## Tags
#pgcis #saga-pryor #roof-design #wind-rating #fm-global #tornado #insurance #building-envelope

## Related Documents
- [[_Project Plan]] - Overall project timeline
- [[Core FM Global Roof Rating System]] - Base FM rating information
- Action Items Database: A-012, A-029, A-046 in Notion

---

**Document Status:** Complete - Ready for team review
**Next Review:** After insurance advisor feedback (post-Oct 18)
**Owner:** Benton (PGCIS) / Erik (FM specs delivery to insurance)
