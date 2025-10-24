---
Created: 2025-10-16 15:30
For: Julia (Architect)
From: Benton & Erik
Date: October 16, 2025
Source: Meeting transcript - October 8, 2025
---

# Interior Design & Architectural Brief - Saga Pryor DC
## Overview

This document captures key interior design concepts and architectural requirements for the Saga Pryor DC project that emerged from Erik's vision for differentiating this facility. These go beyond the standard Schneider RD109 reference design and represent opportunities to create a more innovative, flexible, and operationally superior data center.

## 1. Elevated Operations Center (Signature Feature)

### Concept
Build a **tall enough data center with an overhead walkway** running down the middle of the data hall, connecting to an elevated operations office.
### Key Requirements
- Operations staff positioned **centrally and elevated** with visual oversight of entire data floor
- Staff can observe if someone falls, gets hurt, or needs assistance
- **NOT** in a traditional soundproof NOC with no visibility
- Access to security cameras **plus** direct visual oversight
- Needs secure zone access control (TBD: how staff get up/down)

### Design Implications
- **Potentially Higher ceiling heights** than typical data centers
- **Structural capacity** for elevated platform/walkway + staff loads
- Potentially spectacular from an investor presentation perspective
- Consider: glass-enclosed operations office with 360° views?
- Half of this structure is public access, and the other half is gated to allow for DC access.

### Erik's Quote
> "I want my people that are running the facility to be in the center, up above, where they can maybe see things going on... they can actually look down, or walk around and see if someone's working in the data center, but they fall over and get hurt or something happens, you can see it."


## 2. Security Perimeter Layers

Multiple "challenge points" creating nested security zones from exterior to interior:

1. **Perimeter fence** (outermost - site boundary)
2. **Building perimeter** (building envelope)
3. **Security/lobby area + loading dock** (reception checkpoint)
4. **Inner perimeter** → critical space corridors (staff-only access)
5. **Customer cage spaces** → prox badge + biometric access (innermost)

### Design Requirements
- Circulation design must support progressive security escalation
- Each layer requires appropriate access control infrastructure
- Consider sight lines and camera coverage at each transition
- Loading dock access separate from visitor/staff flow


## 3. Data Hall Sizing

### Target Dimensions
- Hot aisle / cold aisle containment layout (ask GPT / Erik what this means)
- Rack layout TBD based on final block sizing strategy
### Layout Strategy
- Must accommodate both air-cooled and liquid-cooled rack zones
- Overhead cable tray routing corridors required
- Consider: How does elevated walkway integrate with aisle layout?

## 4. Equipment Staging & Testing Area

### Purpose
Separate space where **customers can stage and test equipment before deployment** into the data hall.
### Requirements
- **Power connections** for equipment burn-in and testing
- Located **near loading dock** but before data hall security perimeter
- Reduces contamination from packaging materials entering clean data hall
- Approximately **2,000 SF** (recommended in feasibility memo)
### Benefits
- Prevents cardboard dust and packaging debris from entering critical spaces
- Accelerates customer onboarding (pre-staging and testing)
- Dedicated space for break-fix activities without disrupting live environment


## 6. Building Envelope - Tornado Hardening

### Oklahoma-Specific Requirements

**FM Global I-135 Rated Roof:**
- Designed for tornado **uplift pressure** resistance
- "Tornadoes don't blow roofs off, negative pressure sucks them off" - Erik
- More expensive than standard roof but necessary for insurance and regional risk

**Equipment Protection:**
- **Superstructure on roof** for chiller placement
- **Robust screen walls** → designed to withstand 2x4 lumber at high velocity
- Screen walls protect roof equipment from debris
- Consider: Can overhead walkway/operations office support be integrated with roof structure?

**Generator Equipment Yard:**
- **Concrete wall enclosure** (not standard chain-link)
- Must withstand vehicle/debris impact
- Acoustic treatment for noise compliance
- Secure enclosure for fueling/refueling operations

### Cost Implications
- Significantly more expensive than standard construction
- Erik: "There's other areas we can save money, but in that part of the country..."

## 8. Generator Equipment Yard Design

### Enclosure Requirements
- **Heavy-duty concrete walls** (not standard fencing)
- Tornado and debris impact resistance
- **Acoustic treatment** for noise ordinance compliance
- Secure perimeter for fuel storage and refueling operations

### Siting Considerations
- Indoor vs. outdoor generator placement **TBD** (client decision pending)
- If outdoor: screen walls and tornado-rated enclosures required
- Fuel storage: day tanks + bulk storage configuration TBD
- Consider: Integration with site security perimeter (berms, detention pond)


## 12. Critical Space Program

### Spaces to Include (Preliminary)

**Critical Spaces:**
- Elevated operations center + walkway
- Equipment staging/testing area (~2,000 SF)
- Loading dock + receiving
- Generator equipment yard
- Electrical/UPS rooms
- Mechanical/chiller plant areas

**Support Spaces:**
- Security/lobby checkpoint
- Meet-Me-Room (MMR) for fiber/telecom
- Staff amenities (break room, possibly showers/lockers for 24/7 ops)
- Office space (may be in separate support building - TBD)

**Note:** Feasibility memo recommends **separating non-critical office functions** into an adjacent lower-cost support building, leaving only NOC (now elevated operations center) within hardened facility.

---

## Action Items for Julia

### Immediate Next Steps

1. **Data hall layout (25,000 SF)**
   - Hot aisle / cold aisle containment strategy
   - Overhead cable tray routing corridors
   - Integration with elevated walkway concept
   - Accommodation for both air-cooled and liquid-cooled zones

2. **Equipment staging area layout (~2,000 SF)**
   - Size and locate near loading dock
   - Power rough-in requirements
   - Workflow: receiving → staging → data hall
   - Contamination control considerations

3. **Security circulation diagram**
   - Show progression through 5 security layers
   - Access control points at each transition
   - Separation of visitor/staff/customer flows
   - Loading dock access separate from visitor flow

4. **Design elevated operations center concept**
   - Sketch section showing walkway + elevated office
   - Determine ceiling height requirements
   - Structural strategy for elevated platform
   - Glass-enclosed operations office option with 360° views

5. **Generator equipment yard enclosure**
   - Concrete wall design (vehicle/debris impact resistance)
   - Acoustic treatment specifications
   - Fuel storage integration (day tanks + bulk storage)
   - Indoor vs. outdoor placement options

6. **Critical space program development**
   - Confirm all spaces listed in Section 12
   - Coordination with MEP for equipment room sizing
   - Determine if office functions should be in separate support building
   - Staff amenities sizing (break room, showers/lockers for 24/7 ops)

7. **Tornado-hardened building envelope**
   - FM I-135 rating requirements research
   - Roof superstructure for chiller equipment
   - Screen wall specifications (2x4 impact resistance)
   - Integration with elevated operations structure?




---

## Key Differentiators of This Project

What makes this data center **different** from the standard Schneider RD109:

1. ✅ **Elevated operations center** with visual oversight (unique feature)
2. ✅ **No raised floor** (cost savings + flexibility)
3. ✅ **Tornado-hardened** building envelope (FM I-135)
4. ✅ **Equipment staging area** (operational excellence)
5. ✅ **Integrated solar + BESS** microgrid (sustainability differentiator)
6. ✅ **Flexible phased deployment** (financial risk mitigation)
7. ✅ **GCP cloud onramp potential** (4 miles from Google campus)

---

## Reference Documents

- [[Feasibility Memo V3]] - Complete project scope and decisions
- [[_Project Plan]] - Timeline and milestones
- [[LOD200 Definitions - Scope Limitations]] - BIM modeling scope for this phase
- [[Terms and Definitions]] - Technical glossary
- Meeting transcript: October 8, 2025 (source of this brief)

---

## Questions or Clarifications?

Contact:
- **Benton** - Project management + coordination
- **Erik** - MEP systems + operations expertise
- **Muhammad** - Electrical engineering

---

**Tags:** #saga-project #architecture #interior-design #julia #design-brief
