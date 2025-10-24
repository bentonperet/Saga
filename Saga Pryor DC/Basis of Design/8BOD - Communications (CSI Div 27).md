**Created:** 2025-10-23 10:45

# BASIS OF DESIGN - COMMUNICATIONS
## CSI Division 27
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 2 Supporting Systems]]

---

## OVERVIEW

Telecommunications infrastructure provides high-bandwidth, diverse, and redundant connectivity for customer workloads with emphasis on low-latency GCP interconnection.

**Strategic Advantage:** Proximity to Google Pryor campus (~4 miles) enables sub-millisecond latency GCP Dedicated Interconnect.

---

## CONNECTIVITY OBJECTIVES

1. **Carrier Diversity:** Multiple telecommunications carriers (ISPs, dark fiber, cloud on-ramps)
2. **Physical Path Diversity:** Redundant fiber entry points from different directions
3. **Low Latency:** Sub-millisecond latency to Google Pryor campus for GCP interconnection
4. **Scalability:** Meet-Me-Rooms sized for 10+ carriers supporting 12 MW facility

**Connectivity Strategy:**
- **Carrier-Neutral:** Open access for all carriers (no exclusivity agreements)
- **Cross-Connect Model:** Customers order cross-connects from MMR to customer cages
- **Cloud On-Ramps:** Direct connections to GCP, AWS, Azure via carrier partners

---

## FIBER ENTRY & PATH DIVERSITY

### Fiber Entry Points
- **Primary Entry:** North side of building
- **Secondary Entry (Diversity):** South side of building
- **Physical Separation:** Entry conduits separated by >100 ft, routed through different utility vaults
- **Purpose:** Ensures redundancy if one fiber route is cut or damaged

### Conduit Infrastructure
- **Conduit Size:** 4-6" conduits from property line to MMRs
- **Quantity:** 4-6 conduits per entry point (redundancy + future capacity)
- **Material:** PVC or HDPE conduits with pull rope installed
- **Vault:** Telecommunications vault at property line for carrier hand-off

### Fiber Route Analysis (In Progress)
**Camelot Task 3 (Expected Delivery: Early November 2025):**
- Identify existing fiber routes near site
- Map carrier availability (AT&T, Cox, Level3/CenturyLink, Zayo, etc.)
- Confirm physical diversity (separate routes for redundancy)
- Estimate connectivity installation timeline and costs

**Action Required:** Review Camelot fiber analysis and negotiate Service Level Agreements (SLAs) with minimum two carriers for redundancy.

---

## MEET-ME-ROOMS (MMRs) - UPDATED OCT 2025

### Configuration
- **Quantity:** 2 Meet-Me Rooms (north and south entries for diverse fiber paths)
- **Size:** 250-300 SF each **(equal sizing confirmed)**
- **Location:** Ground floor, near respective fiber entry points
- **Purpose:**
  - Carrier cross-connects
  - GCP interconnection termination
  - Cloud on-ramp aggregation

### MMR Specifications
- **Rack Space:** 10-15 racks (42U height) for carrier equipment
- **Power:** Dedicated electrical panel, dual-feed circuits (A+B power from BESS via switchboards)
- **Cooling:** Dedicated CRAC or CRAH unit (carrier equipment generates heat)
- **Fire Suppression:** Pre-action sprinkler or clean agent (coordinate with data hall system)

### Security & Access
- **Security Level:** Highest security access required
- **Door Location:** Interior doors acceptable (not required to open to exterior)
- **Access Control:** Card reader + PIN or biometric (two-factor authentication)
- **Rack Count:** TBD based on carrier requirements for 12 MW facility (likely 10-15 carriers)

### Cross-Connect Infrastructure
- **Fiber Cross-Connect Panels:** LC or MTP fiber patch panels
- **Copper Cross-Connect:** 110-block or patch panels (for legacy circuits, if needed)
- **Cable Management:** Overhead ladder rack or wire basket tray for cross-connect cabling
- **Labeling:** All cross-connects labeled with customer ID, circuit ID, and carrier

### Carrier Onboarding Process
1. Carrier installs equipment in MMR rack
2. Carrier pulls fiber from entry vault to MMR
3. Carrier terminates fiber on cross-connect panel
4. Customer orders cross-connect from MMR to customer cage
5. Facility staff install fiber cross-connect (patch cable)

---

## MAIN DISTRIBUTION AREA (MDA) & BACKBONE

### Main Distribution Area (MDA)
- **Size:** ~300 SF (separate from MMRs, within data hall or adjacent)
- **Purpose:** Facility backbone equipment (core switches, firewalls, monitoring)
- **Rack Space:** 4-6 racks for facility network equipment

### Backbone Architecture
- **Facility Network:** Management network for BMS, DCIM, security, access control
- **Customer Network:** Physically isolated from facility network
- **Redundancy:** Dual fabric (A+B switches) for facility network
- **Bandwidth:** 10 Gbps or 40 Gbps backbone links

---

## GOOGLE CLOUD PLATFORM (GCP) INTERCONNECTION

### Proximity Advantage
Data center is ~4 miles from Google Pryor campus, enabling **low-latency direct interconnection** to GCP.

### Interconnection Options

**Option 1: Dedicated Interconnect (RECOMMENDED)**
- **Description:** Direct fiber connection from data center to Google Pryor campus
- **Bandwidth:** 10 Gbps or 100 Gbps per circuit
- **Latency:** **<1 ms** (sub-millisecond due to proximity)
- **Cost:** ~$1,700/month per 10 Gbps circuit (Google pricing)
- **Feasibility:** Requires dark fiber route confirmation (via Camelot fiber study)

**Option 2: Partner Interconnect**
- **Description:** Via carrier partners (e.g., Equinix, Megaport)
- **Bandwidth:** 50 Mbps to 50 Gbps
- **Latency:** <2 ms (depends on carrier routing)
- **Cost:** Varies by partner

### Customer Value Proposition
- **Low-latency GCP access:** Ideal for AI/ML workloads, real-time applications
- **Hybrid cloud deployments:** On-prem + GCP seamlessly integrated
- **Reduced data egress costs:** Direct connection bypasses internet

### Feasibility Actions Required
- Confirm dark fiber route availability from data center to Google Pryor campus (Camelot fiber study)
- Negotiate with Google for Dedicated Interconnect colocation at Pryor campus
- If dark fiber not feasible, leverage Partner Interconnect via carrier presence in MMR

---

## TELECOMMUNICATIONS GROUNDING

### TIA-942 Compliance
- **Telecommunications Grounding:** Per TIA-607-C
- **Telecommunications Bonding Backbone (TBB):** Connects all telecommunications spaces
- **Telecommunications Main Grounding Busbar (TMGB):** Located in MDA, bonded to building ground system
- **Equipment Grounding:** All carrier equipment and racks bonded to TBB

---

## COST IMPACTS

| System | Cost Estimate |
|---|---|
| Meet-Me Rooms (2× MMRs, 250-300 SF each) | ~$200-400K (fit-out + cooling) |
| Main Distribution Area (MDA) | ~$100-200K (fit-out + equipment) |
| Fiber conduit infrastructure (entry vaults, conduits) | ~$200-400K |
| Dark fiber to Google Pryor (if Dedicated Interconnect) | ~$50-200K (installation) |
| Carrier circuits (ongoing OPEX) | ~$1,700/mo per 10 Gbps GCP circuit |
| Cross-connect infrastructure (panels, cable management) | ~$50-100K |

---

**Tags:** #saga-project #communications #fiber #gcp-interconnection #meet-me-room #csi-division-27

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page
- [[9BOD - Electronic Safety and Security (CSI Div 28)]] - Security integration
- [[6BOD - Integrated Automation (CSI Div 25)]] - Facility network backbone
