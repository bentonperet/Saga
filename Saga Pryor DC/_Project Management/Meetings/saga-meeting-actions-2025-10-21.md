# Saga PGCIS Meeting - Action Items & Key Decisions
**Created:** 2025-10-21 16:30

## Meeting Overview
Client meeting with Saga team followed by PGCIS internal recap discussing data center design, power systems, and path to investor presentation.

---

## 🚨 CRITICAL ASSUMPTIONS TO UPDATE ACROSS ALL DOCUMENTS

These are fundamental changes that affect multiple documents, financial models, and narratives:

### 1. **Solar Power Contribution - MAJOR CHANGE**
- **OLD ASSUMPTION**: Solar would provide significant majority of power
- **NEW REALITY**: Solar provides only ~25% of total power at full capacity (12 MW solar → 10 MW total load)
- **IMPACT**: Changes entire "green power" narrative and marketing story
- **WHY**: Solar only generates at full capacity 5-6 hours/day; IT loads run 24/7. The gap at night and off-peak hours requires grid/generator power.
- **DOCUMENTS TO UPDATE**:
  - All marketing materials mentioning "green power"
  - Financial models
  - Basis of Design
  - Investor presentation narrative

### 2. **Grid Power is REQUIRED (Not Optional)**
- **OLD ASSUMPTION**: Micro grid with solar/BESS could potentially operate standalone
- **NEW REALITY**: Grid power is **necessary** for economic viability
- **IMPACT**: Grid interconnection timeline becomes critical path item
- **DOCUMENTS TO UPDATE**:
  - Project schedule/critical path
  - Risk register
  - Investor presentation
  - All technical documents

### 3. **Data Center Size Change**
- **OLD**: 7 MW IT load
- **NEW**: 10 MW IT load (expandable to 20 MW with density increases)
- **RATIONALE**: Better market fit, rounder numbers for customer segments (2-3 MW blocks)
- **DOCUMENTS TO UPDATE**:
  - All technical drawings
  - Financial models (revenue projections)
  - Basis of Design
  - Building square footage calculations

### 4. **UPS System Elimination**
- **OLD**: Traditional UPS systems ($8-10M cost)
- **NEW**: BESS (Battery Energy Storage System) serves as UPS replacement
- **COST SAVINGS**: $4-6M+ net savings
- **IMPACT**: Major CAPEX reduction, changes electrical design entirely
- **DOCUMENTS TO UPDATE**:
  - Equipment lists
  - Capital budget
  - Electrical single-line diagrams
  - O&M procedures

### 5. **Cooling System Change**
- **OLD**: Fan wall cooling (Schneider baseline)
- **NEW**: Rear door heat exchangers (direct-to-chip ready)
- **RATIONALE**:
  - Phased capital deployment (don't build cooling until customer signed)
  - Supports higher densities (AI workloads)
  - More flexible for different customer requirements
- **DOCUMENTS TO UPDATE**:
  - Mechanical drawings
  - Equipment lists
  - Capital deployment schedule
  - Customer SLA templates

### 6. **Backup Power System**
- **OLD**: Diesel generators
- **NEW**: Natural gas turbines (primary) + possibly diesel (emergency backup for gas outage)
- **LEAD TIME**: ~12 months for turbines
- **REQUIREMENTS**: Need gas line capacity confirmation
- **DOCUMENTS TO UPDATE**:
  - Utility requirements
  - Site plan
  - Equipment specifications
  - Fuel supply agreements

### 7. **Building Design - NOT Just a Data Hall**
- **OLD**: Schneider prefab design "as is"
- **NEW**: Significant additions required:
  - Bathrooms (none in Schneider design!)
  - Security gates and access control
  - Meet-me rooms
  - NOC (Network Operations Center) room
  - Rack and stack area
  - Hallways and circulation
  - Lockers for technicians
  - Partially secure meeting area
- **IMPACT**: Building footprint and cost will differ from baseline
- **DOCUMENTS TO UPDATE**:
  - Architectural drawings
  - Building CAPEX
  - Space program
  - Security plan

### 8. **Capital Deployment Strategy**
- **OLD**: Build entire facility upfront
- **NEW**: Phased deployment in 2-3 MW blocks
- **RATIONALE**:
  - Better IRR (deploy capital as customers sign)
  - Matches customer demand patterns (enterprises want 2-5 MW, not 10+)
  - De-risks initial investment
- **DOCUMENTS TO UPDATE**:
  - Financial model (revenue/CAPEX phasing)
  - Construction schedule
  - Customer lease templates

### 9. **Micro Grid Timeline**
- **NEW REQUIREMENT**: Solar + BESS must be operational WHEN data center comes online (not after)
- **IMPACT**: Parallel construction schedule required
- **DOCUMENTS TO UPDATE**:
  - Master project schedule
  - Solar/BESS procurement timeline
  - Critical path analysis

### 10. **Staffing Assumptions**
- **CONFIRMED**: ~12 full-time staff for 10 MW facility
- **OCCUPANCY**: Max 20 people on site at any given time
- **IMPACT**: Septic system sufficient (no need for municipal sewer connection)
- **DOCUMENTS TO UPDATE**:
  - O&M budget
  - Utility sizing (water/sewer)
  - Parking requirements

---

## 📋 ACTION ITEMS

### **AARON OLDHAM**
- [ ] **[PRIORITY]** Contact Google GCP team about interconnection at Prior, OK location
  - Get lead times for interconnection
  - Understand application process
  - Identify specific GCP contact for the region
  - Ask about who handles fiber in the area
- [ ] Take drone footage during site visit (3D mapping with AI)
- [ ] Walkthrough video 3D mapping of data center site area

### **DAVID NOCELLA**
- [ ] **[PRIORITY]** Get full breakdown from Camelot on CHILL vs HILL interconnection process
  - CHILL = interruptible power (faster approval, currently in FERC approval)
  - HILL = firm power (slower but guaranteed)
  - Understand: what % of time is power interrupted?
  - How does this mesh with 25% solar generation capacity?
  - Can we start with CHILL and upgrade to HILL later?
  - Ask about demand response programs
- [ ] **[ON-SITE THIS WEEK]** Check gas line capacity and pressure during site visit
  - Stop by utilities office while in Prior
  - Confirm gas pressure in local lines
  - Get commitment on gas availability for turbines
  - Benton to send gas requirements specifications
- [ ] **[ON-SITE THIS WEEK]** Site photography and documentation
  - Extensive photos of data center site (southern area)
  - Utility infrastructure photos (power lines, gas lines, etc)
  - Access road options (north entrance vs south entrance)
  - Check condition of gravel roads for construction traffic
- [ ] Explore wastewater options
  - Confirm septic system is viable (vs municipal sewer)
  - Check if industrial park wastewater treatment is accessible/needed
  - Document costs for either approach
- [ ] Review financial model inputs with Walker
  - Incorporate 10 MW → 20 MW analysis
  - Update CAPEX with UPS removal savings
  - Update OPEX with new occupancy numbers
  - Consider "more batteries" option (Walker's question)
- [ ] Discuss with investor about aesthetic preferences
  - Ask about green building elements (vines, exterior greening)
  - Sustainability priorities vs cost trade-offs

### **BENTON PERET**
- [ ] **[PRIORITY]** Send solar power analysis (25% calculation) to David/Walker
  - Show math on 12 MW solar → 10 MW load = 25% coverage
  - Include peak sun hours analysis for Prior, OK
  - Explain day/night load gap
- [ ] **[PRIORITY]** Send questions document for Camelot (grid power)
  - Consolidate all grid interconnection questions
  - Include technical requirements for CHILL/HILL process
- [ ] **[PRIORITY]** Send draft Basis of Design with clear notations
  - Highlight sections still being pressure-tested
  - Use asterisks or color coding for unconfirmed numbers
  - Include deviation summary from Schneider baseline
- [ ] Package financial model changes for David
  - Bullet list of adds/removes:
    - REMOVE: UPS systems (-$8-10M)
    - REMOVE: Fan walls
    - REMOVE: Raised floor
    - REMOVE: Adiabatic coolers
    - ADD: BESS system (additional cost beyond UPS replacement)
    - ADD: Micro grid controllers
    - ADD: Rear door heat exchangers (phased)
    - ADD: Natural gas turbines
    - ADD: Building amenities (bathrooms, NOC, security, etc)
  - Show net CAPEX impact
- [ ] Get gas pressure/capacity requirements from turbine vendors
  - Contact turbine suppliers (4.3 MW units mentioned)
  - Confirm 12-month lead time
  - Get gas line specifications needed
  - Share with David for site visit
- [ ] Send heating/cooling slide deck to team
  - Visual explanations of rear door heat exchangers
  - Fan wall vs RDHX comparison
  - Direct-to-chip preparation graphics
- [ ] Update building design with 10 MW scope
  - Finalize space allocations
  - Show first draft of comprehensive layout (not just data hall)
  - Include all support spaces added to Schneider baseline
- [ ] Pressure test 10 MW vs 20 MW IRR analysis with Muhammad
  - Verify density increase ROI calculations
  - Model phased deployment scenarios

### **WALKER** (via David)
- [ ] Review 12 MW battery sizing
  - Question raised: "Should we do more batteries?"
  - Analysis needed: Does more battery capacity help evening hours?
  - Benton's note: More solar needed, not more batteries (limited by panel capacity)
- [ ] Review Benton's solar analysis
- [ ] Update project schedule with micro grid parallel timeline

### **CAMELOT** (via David)
- [ ] Provide full CHILL vs HILL interconnection summary
- [ ] Clarify which process is still in FERC approval
- [ ] Explain large load interconnection fast-track options (>10 MW)
- [ ] Provide timeline estimates for each path

### **ERIK STOCKGLAUSNER / PGCIS TEAM**
- [ ] **[FUTURE]** Revisit customer engagement discussion mid-November
  - Erik asked about bringing potential customers to table early
  - David said "cart before horse" - revisit after investor meeting
  - Could involve representation agreement/fee structure
- [ ] Develop single-line diagram for 2-3 MW blocks
  - Modular "Lego block" design approach
  - N+1 redundancy within each block
  - Equipment sizing for 2-3 MW generators/switchgear

---

## ✅ DECISIONS FINALIZED

These were confirmed during the meeting and can be moved forward:

1. **Data center size: 10 MW IT load** (expandable to 20 MW via density)
2. **BESS replaces UPS** - move forward with this design
3. **Rear door heat exchangers** instead of fan walls - approved
4. **Natural gas turbines** as primary backup power - approved
5. **Closed-loop cooling** (no evaporative/adiabatic) - approved
6. **Raised floor removed** - approved
7. **Modular 2-3 MW block design** - approved
8. **Septic system** sufficient (no municipal sewer needed)
9. **~12 person staff** for facility operations
10. **Micro grid must be online** when data center opens
11. **Green building elements** (vines on exterior) - investor will like this

---

## 📅 KEY DATES

- **Tomorrow (Oct 22)**: David flies to Tulsa for site visit
- **This week**: David + Aaron on-site in Prior, OK
- **Early November**: Target for wrapping up basis of design
- **Mid-November**: Potential investor meeting
- **Mid-November**: Revisit customer engagement discussion (Erik's question)

---

## 🔗 RELATED DOCUMENTS

- Basis of Design (draft in progress)
- Feasibility Memo (sent)
- Google Cloud Connection analysis
- Schneider RD 109 baseline design
- Financial model (to be updated)
- Solar panel layout
- Site photos and drone footage

---

## 💡 KEY INSIGHTS / QUOTES

**On Solar Reality:**
> "At 7.4 megawatts IT load and like 10ish megawatts total load, that 12 megawatts of solar is like 25%. You've got 5-6 hours of good sun generating full capacity... and then you've got a long time at night where those IT loads are still running." - Benton

**On Market Positioning:**
> "The sweet spot in the market right now... is between 10 and 20 megawatts. Most customers... are like, 'If you guys can build a 10 megawatt data center, we feel like we've got a roadmap to we can take five, right?' And 10 would be nice because if we could expand to 10, who knows what the future's going to hold." - Erik

**On Automation:**
> "Customers are going to like it because anybody who knows data centers knows that when the data center goes down, it's normally when people are touching stuff. If I can automate the switching procedure on the electrical side, if I can back the UPS and BESS systems out of the building, now I've got lots of real estate to play with. I've got a reliable infrastructure. It's automated." - Erik

**On Investor Priorities:**
> "He's bullish on data centers. He's very sustainability focused. He's kind of an old hippie kind of guy. So he's all about renewables but he's also an entrepreneur. So he likes to be ahead of the curve... and just very simply a high NPV and a high IRR at the end of the day." - David

**On Capital Efficiency:**
> "This gives you incremental capital efficiency for the build. So when the customer says they want the space, you procure it, you put it in, the capital is very efficient, the IRR is better, windows shorter, and IRR still get better with age." - Erik

---

## ⚠️ RISKS & OPEN QUESTIONS

1. **Grid interconnection timeline** - Critical path unknown until Camelot provides details
2. **Gas line capacity** - Needs on-site confirmation this week
3. **GCP interconnection waitlist** - Unknown until Aaron contacts Google
4. **Turbine lead time** - 12 months estimated, but needs vendor confirmation
5. **Solar percentage marketing** - Need to reframe "green power" story with 25% reality
6. **20 MW expansion path** - Needs more analysis on when/if to expand beyond 10 MW
7. **FERC approval timing** - One of the interconnection processes still pending approval

---

#saga #datacenter #action-items #power #design-decisions #investor-prep

**Next Update:** After site visit (Oct 22-23) and Camelot response