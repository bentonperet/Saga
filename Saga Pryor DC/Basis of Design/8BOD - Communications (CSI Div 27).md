

# BASIS OF DESIGN - COMMUNICATIONS
## CSI Division 27
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]] 

---

## OVERVIEW

Telecommunications infrastructure provides carrier-neutral, diverse, and redundant connectivity supporting 12 MW IT capacity with multiple fiber paths, cloud on-ramps, and structured cabling systems.

**Design Philosophy:**
- **Carrier-neutral:** Open access to all telecommunications carriers
- **Physical diversity:** Multiple fiber entry points from different directions
- **Scalability:** Infrastructure sized for 12 MW (expandable to 24 MW master plan)
- **Cloud connectivity:** Direct connections to AWS, Azure, GCP

---

## FIBER ENTRY & PATH DIVERSITY

### Dual Fiber Entry Points

**Primary Entry (East Side):**
- Location: East wall, near electrical yard
- Conduits: 4 × 4" PVC/HDPE from property line to MPOE-1
- Vault: Telecommunications manhole at property line (carrier hand-off point)
- Purpose: Primary carrier route

**Secondary Entry (West Side - Diversity):**
- Location: West wall, opposite side of building
- Conduits: 4 × 4" PVC/HDPE from property line to MPOE-2
- Vault: Separate telecommunications manhole
- Physical separation: >150 ft from primary entry
- Purpose: Geographic diversity (different carrier routes)

**Benefits of Dual Entry:**
- Redundancy: If one fiber route is cut, secondary route maintains connectivity
- Carrier diversity: Different carriers can use different entry points
- Future capacity: 8 total conduits support expansion to 24 MW

### Conduit Infrastructure

**Specifications:**
- **Material:** Schedule 40 PVC or HDPE
- **Size:** 4" inner diameter (accommodates multiple fiber cables)
- **Pull rope:** Installed in all conduits for future cable installation
- **Markers:** Conduit route markers every 50 ft (locatable)
- **Depth:** 36-48" burial depth per NEC Article 800

**Entry Seal:**
- Fire-rated conduit sealing compound at building penetrations
- Prevents water intrusion, fire spread, and pest entry

---

## MAIN POINT OF ENTRY (MPOE) & MEET-ME-ROOMS (MMR)

### Configuration

**2 × MPOE/MMR Facilities (Geographically Diverse):**

**MPOE-1 (Primary):**
- **Location:** East side, ground floor
- **Size:** 250-300 SF <!-- @benton -->
- **Fiber entry:** From east property line conduits
- **Purpose:** Primary carrier demarcation and cross-connect

**MPOE-2 (Secondary/Diverse):**
- **Location:** West side, ground floor
- **Size:** 250-300 SF <!-- @benton -->
- **Fiber entry:** From west property line conduits
- **Purpose:** Diverse carrier route termination

**Why Two MPOEs:**
- Geographic diversity (different fiber routes from different directions)
- Redundancy (if one MPOE fails or fiber cut, secondary maintains service)
- Carrier preference (some carriers prefer specific entry points)

### MPOE/MMR Specifications

**Each MPOE/MMR Includes:**
**Power:**
- Dual-feed power (A-side + B-side from SWBD-A and SWBD-B)
- 200-400A panel per MMR
- Redundant UPS-backed circuits for carrier equipment
**Fire Suppression:**
- Preaction dry pipe or clean agent (coordinate with data hall system)
- VESDA smoke detection
**Grounding:**
- Telecommunications main grounding busbar (TMGB) per TIA-607-C
- Bonded to building grounding system
**Security:**
- Card reader + biometric (two-factor authentication)
- CCTV coverage (entry monitoring)
- Access restricted to facility staff and authorized carriers


---

## MAIN DISTRIBUTION AREA (MDA)

### Purpose

Central location for facility network equipment (not customer equipment). Houses core switches, firewalls, and BMS/DCIM infrastructure.

### MDA Specifications

**Location:** Adjacent to data halls (central position)

**Size:** 300-400 SF <!-- @benton -->
**Rack Space:**
- 4-6 × 42U four-post racks
- Equipment: Core switches, firewalls, BMS/DCIM servers, NOC workstation switches
**Power:**
- Dual-feed UPS-backed circuits (A-side + B-side)
- 100-200A panel
**Cooling:**
- Shared with data hall HVAC or dedicated mini-split


---

## FACILITY BACKBONE ARCHITECTURE

### Network Segmentation

**Physical Networks:**

**1. IT Network (Customer):**
- Customer servers, applications, internet gateway
- Isolated from facility networks (firewall, VLAN segmentation)
- No direct connection to facility BMS/DCIM
**2. Facility Network (BMS/DCIM):**
- Building management system (HVAC, lighting)
- EPMS (electrical power monitoring)
- DCIM (rack power/cooling monitoring)
- Access control, CCTV
**3. Management Network (NOC/Admin):**
- NOC workstations
- Remote access (VPN gateway)
- Administrative access to facility systems

**Firewall:** Between IT and Facility networks (strict access control rules)

### Backbone Topology

**Redundant Fiber Ring:**
- Fiber backbone connects MDA → Data Hall 1 → Data Hall 2 → MPOE-1 → MPOE-2 → MDA (ring)
- Dual fiber paths (A-side + B-side)
- Automatic failover if one fiber path cut

**Core Switches:**
- 2 × redundant core switches in MDA (A/B)
- 10 Gbps or 40 Gbps uplinks
- Layer 3 routing, VLANs for network segmentation

---

## STRUCTURED CABLING (DATA HALLS)

### Horizontal Cabling

**Configuration:**
- Overhead ladder rack or wire basket tray
- Route: MDA → Data hall zone distribution frames → Cabinets
- No raised floor (slab-on-grade with overhead cable distribution)

**Cabling Types:**
- **Fiber:** OM4 multi-mode (850 nm, 100 Gbps capable) for cabinet connections
- **Copper:** Cat6A (10 Gbps) for management/IPMI connections (if needed)

**Cabinet Connectivity:**
- 2 × fiber pairs per cabinet (A-side + B-side for redundancy)
- Terminates at cabinet top-of-rack (ToR) switches or directly to customer equipment

### Labeling & Documentation

**Cable Labels:**
- Source/destination, circuit ID, installation date
- Attached at both ends and every 10 ft along route

**As-Built Documentation:**
- CAD drawings showing all fiber routes, patch panel assignments
- Cable schedule (Excel or database) with circuit IDs, customer assignments
- Updated whenever changes are made

---

## CLOUD CONNECTIVITY

### Cloud On-Ramp Strategy

**Direct connections to major cloud providers:**

**AWS Direct Connect:**
- Via carrier partners (Equinix, Megaport, etc.)
- Bandwidth: 1 Gbps, 10 Gbps, or 100 Gbps
- Low-latency connection to nearest AWS region

**Microsoft Azure ExpressRoute:**
- Via carrier partners
- Bandwidth: 50 Mbps to 100 Gbps
- Private connection to Azure services

**Google Cloud Platform (GCP):**
- **Proximity advantage:** Pryor is near Google's Mayes County data center campus
- **Potential for low-latency interconnect:** Direct fiber route possible
- **Interconnection options:**
  - Partner Interconnect (via carrier in MMR)
  - Dedicated Interconnect (if direct fiber to Google facility negotiated)

### Implementation

**Carrier Partners:**
- Carriers present in MMR offer cloud on-ramps as a service
- Customer orders cross-connect from MMR to their cabinet
- Carrier provides cloud connectivity (AWS, Azure, GCP)

**Customer Value:**
- Low-latency hybrid cloud deployments
- Reduced data egress costs (bypass internet)
- Secure private connectivity to cloud services

---

## TELECOMMUNICATIONS GROUNDING & BONDING

### TIA-942 Compliance

**Telecommunications Main Grounding Busbar (TMGB):**
- Located in MDA
- 1/4" × 2" copper busbar, minimum 10 ft long
- Bonded to building grounding electrode system

**Telecommunications Bonding Backbone (TBB):**
- 6 AWG bare copper conductor
- Connects TMGB to grounding busbars in each MPOE/MMR, data hall zone

**Equipment Grounding:**
- All racks bonded to TBB via 6 AWG copper
- All carrier equipment chassis bonded to rack
- Fiber cable shields bonded at entry point only (avoid ground loops)

**Standards:**
- TIA-607-C (Telecommunications Bonding and Grounding)
- J-STD-607-B (Commercial Building Grounding/Bonding)


---

## COST SUMMARY

| System | Cost Estimate | Confidence | Range |
|--------|---------------|------------|-------|
| **Fiber Conduit Infrastructure (Dual Entry)** | $300,000 | ±33% | $200-400K |
| **MPOE-1 Fit-Out (Racks, Power, Cooling)** | $225,000 | ±33% | $150-300K |
| **MPOE-2 Fit-Out (Racks, Power, Cooling)** | $225,000 | ±33% | $150-300K |
| **MDA Fit-Out (Core Switches, Racks)** | $150,000 | ±33% | $100-200K |
| **Fiber Backbone (MDA to Data Halls, MPOEs)** | $150,000 | ±33% | $100-200K |
| **Structured Cabling (Overhead, Cabinets)** | $300,000 | ±33% | $200-400K |
| **Grounding & Bonding (TMGB, TBB)** | $75,000 | ±33% | $50-100K |
| **Cross-Connect Infrastructure** | $75,000 | ±33% | $50-100K |
| **Total Communications Infrastructure** | **$1,500,000** | **±33%** | **$1.0-2.0M** |

**Recurring Costs (OPEX):**
- Carrier circuits: Varies by customer (customer-paid)
- Cloud on-ramps: $500-5,000/month per connection (customer-paid)

---

## CODES AND STANDARDS

- **TIA-942-B** (Telecommunications Infrastructure Standard for Data Centers)
- **TIA-568-D** (Commercial Building Telecommunications Cabling Standard)
- **TIA-607-C** (Telecommunications Bonding and Grounding)
- **NEC 2023 Article 800** (Communications Circuits)
- **BICSI DCIM** (Data Center Infrastructure Management Best Practices)

---

**Tags:** #pryor-dc #communications #fiber #mpoe #mmr #carrier-neutral #cloud-connectivity

**Next Steps:**
1. Confirm fiber routes and carrier availability in Pryor, OK area
2. Negotiate carrier on-ramp agreements (AWS, Azure, GCP partners)
3. Design fiber backbone routing (overhead tray layout)
4. Develop cross-connect pricing and procedures for customers
5. Coordinate TMGB/TBB installation with electrical grounding system

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md and Erik_BOD reference
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** Dual MPOE/MMR for geographic diversity, cloud connectivity strategy
