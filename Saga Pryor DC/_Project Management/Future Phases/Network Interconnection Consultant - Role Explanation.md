**Created:** 2025-10-20 15:45

# Network / Interconnection Consultant - Role Explanation
## GCP Dedicated Interconnect Implementation

**Tags:** #saga-project #gcp #interconnection #consultant-role #future-phase

**Related:** [[GCP Interconnection - Complete Guide]]

---

## Overview

This document explains the role and responsibilities of the Network/Interconnection Consultant needed for implementing GCP Dedicated Interconnect at the Saga Pryor Data Center.

**Reference:** From GCP Complete Guide, Section 10 (Vendor & Expertise Requirements), line 635

---

## The Three Core Responsibilities

### **1. Design MMR Cross-Connect Architecture**

**What it means:** Design how customers physically connect to Google Cloud in your Meet-Me-Room (MMR).

**Specifically:**
- **Rack layout**: Where does customer equipment sit? Where does Google's connection terminate?
- **Cross-connect panels**: Design the fiber patch panel system where you'll make physical connections between customer racks and the Google circuit
- **Cable management**: How fiber cables route through the MMR (overhead trays, under-floor, etc.)
- **Power & cooling**: Ensure customer edge routers have redundant power (A+B feeds from your BESS) and adequate cooling

**Analogy:** It's like designing the "wiring closet" infrastructure that allows you to plug Customer A into Google's connection using fiber patch cables.

**Deliverables:**
- MMR rack layout diagrams (CAD/BIM)
- Cross-connect panel specifications (LC or MTP connectors, how many positions)
- Cable management design (routes, labels, documentation)
- Power requirements for customer edge equipment
- Cooling load calculations for MMR

---

### **2. BGP Peering Strategy**

**What it means:** Design how customer networks will exchange routing information with Google Cloud using BGP (Border Gateway Protocol).

**Specifically:**
- **BGP configuration templates**: Standard configs customers use to peer with Google
- **ASN (Autonomous System Number) strategy**: Each customer needs an ASN (public or private) to peer with Google
- **Route advertisements**: What IP prefixes customers advertise to Google (their on-prem networks) and what Google advertises back (cloud networks)
- **Redundancy strategy**: How to configure BGP for failover if primary connection fails
- **Security**: BGP password authentication, route filtering to prevent misconfigurations

**Analogy:** BGP is how routers "talk to each other" to learn network paths. This consultant designs the "conversation rules" between customer routers and Google's routers.

**What BGP Does:**
```
Customer Router ←→ BGP Session ←→ Google Router

Customer advertises: "I have network 10.0.0.0/8"
Google advertises: "I have network 35.190.0.0/16 (GCP services)"

Result: Traffic flows correctly between customer's on-prem and Google Cloud
```

**Deliverables:**
- BGP configuration templates for common router vendors (Cisco, Juniper, Arista)
- ASN assignment strategy (public vs private ASNs)
- Route filtering policies (what to accept, what to reject)
- Failover/redundancy configuration guides
- Security best practices (MD5 authentication, prefix limits)

---

### **3. Customer Onboarding Procedures**

**What it means:** Create the step-by-step playbook your NOC team follows to activate a new customer's GCP connection.

**Specifically:**
- **Cross-connect request workflow**: Customer submits request → your team validates → schedules installation
- **Physical installation**: Step-by-step fiber patch cable installation in MMR (with photos/diagrams)
- **Testing procedures**: How to test fiber connection (optical power levels, continuity)
- **BGP configuration assistance**: How to help customers configure their edge router
- **Troubleshooting guide**: Common issues and how to resolve (e.g., "BGP session won't establish")
- **Documentation templates**: Forms, checklists, customer-facing guides

**Analogy:** This is the "instruction manual" your operations team uses to take a customer from "I want GCP connectivity" to "My traffic is flowing to Google Cloud."

**Example Workflow:**
1. **Day 1**: Customer submits cross-connect request form
2. **Day 2**: NOC validates request (rack location, circuit ID, contact info)
3. **Day 3**: NOC schedules installation window with customer
4. **Day 4**: NOC technician installs fiber patch cable in MMR, tests continuity
5. **Day 5**: Customer configures BGP on their edge router (using template)
6. **Day 6**: NOC verifies BGP session established, traffic flowing
7. **Day 7**: Customer validates application connectivity to GCP

**Deliverables:**
- Cross-connect request form template
- Installation procedure with step-by-step instructions (including photos)
- Testing checklist (fiber power levels, continuity, BGP session status)
- Customer-facing setup guide ("How to Configure Your Router for GCP Interconnect")
- Troubleshooting flowchart (if X happens, do Y)
- Training materials for NOC staff

---

## Why You Need This Consultant

This isn't something you'd figure out yourself unless your team has deep data center interconnection experience. The consultant brings:

✅ **Industry best practices** from other carrier-neutral facilities
✅ **BGP expertise** (complex routing protocol, easy to misconfigure)
✅ **Operational procedures** that minimize customer support burden
✅ **Google-specific knowledge** (how Google expects interconnections to be configured)
✅ **Scalable processes** that work for 1 customer or 100 customers

**Without this consultant:**
- Risk of customer setup failures (BGP misconfigurations, fiber issues)
- High NOC support burden (every customer needs hand-holding)
- Inconsistent documentation (each customer gets different instructions)
- Potential outages from misconfigurations

**With this consultant:**
- Smooth, repeatable customer onboarding
- Self-service setup (customers follow documented procedures)
- Low NOC support burden (only escalations, not routine setups)
- Professional documentation that builds customer confidence

---

## Engagement Details

**Cost:** $25K-$50K for deliverables (from GCP Guide line 645)

**When to Engage:** Month 2-3 (after fiber route confirmed, before first customer)

**Duration:** 4-8 weeks for deliverables + training

**Potential Vendors:**
- Network engineering firms specializing in data center interconnection
- Consultants with carrier-neutral IX (Internet Exchange) experience
- Firms with GCP Partner Interconnect experience

**Questions to Ask Potential Consultants:**
1. Have you designed MMR infrastructure for GCP Dedicated Interconnect before?
2. Can you provide examples of BGP configuration templates you've created?
3. What data center interconnection projects have you completed (references)?
4. Do you provide NOC training as part of your deliverables?
5. What is your approach to creating customer-facing documentation?

---

## Internal Training Needs

**Your NOC/Operations Team Will Need Training On:**

1. **Cross-Connect Management**
   - How to receive customer cross-connect requests
   - Physical installation procedures (fiber patch cables in MMR)
   - Testing procedures (fiber power levels, continuity)
   - Documentation and labeling standards

2. **Customer Support**
   - How to guide customers through GCP Interconnect setup
   - BGP peering troubleshooting basics (common issues)
   - Escalation procedures (when to involve Google support)

3. **Monitoring & Alerting**
   - Fiber link monitoring (optical power, BER - bit error rate)
   - Customer circuit utilization monitoring
   - Proactive alerts for degraded performance

**Training Options:**
- Google provides free online training: [Google Cloud Networking Training](https://cloud.google.com/training/networking)
- Hire network consultant for hands-on NOC training (included in consultant engagement)
- Google Cloud Interconnect partner program (if you become official Google partner, they provide training)

---

## Timeline Integration

**This consultant engagement fits into the overall GCP Interconnect timeline:**

| Phase | Timing | Consultant Role |
|-------|--------|----------------|
| Phase 0: Validation | Weeks 1-4 | Not involved yet |
| Phase 1: Design & Agreements | Weeks 5-8 | **ENGAGE CONSULTANT HERE** |
| Phase 2: Construction | Weeks 9-16 | Consultant delivers MMR design, BGP templates, procedures |
| Phase 3: Customer Onboarding | Week 17+ | Consultant trains NOC, validates first customer activation |

**Critical Path:** You need these deliverables BEFORE your first customer activates (Week 17), so engage consultant by Week 5-8.

---

## Success Metrics

**How to measure if this consultant delivered value:**

✅ **First customer activation takes <7 days** (from request to live traffic)
✅ **Zero BGP misconfigurations** requiring Google escalation
✅ **NOC can handle 90% of customer requests** without external help
✅ **Customer satisfaction score >4.5/5** on setup experience
✅ **Second customer activation is faster** than first (repeatable process)

---

## Next Steps

1. **Before engaging consultant:** Confirm fiber route to Google Pryor campus is feasible
2. **Identify consultant candidates:** Research firms with GCP Interconnect experience
3. **RFP process:** Request proposals from 2-3 qualified firms
4. **Selection criteria:** Experience > Cost (this is critical infrastructure, don't go cheap)
5. **Kick off:** Align consultant engagement with fiber installation timeline

---

## Related Documents

- [[GCP Interconnection - Complete Guide]] - Full GCP strategy and implementation roadmap
- [[Basis of Design - Part 2 Supporting Systems]] - Section 9.5 (GCP Interconnection)
- [[Feasibility Memo V3]] - Opportunity #4 (Marketing GCP Onramp)
