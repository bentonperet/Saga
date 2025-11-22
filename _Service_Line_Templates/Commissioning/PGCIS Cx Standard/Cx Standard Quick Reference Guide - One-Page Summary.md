# PGCIS Commissioning Standard - Quick Reference Guide

**Purpose:** One-page field reference for PGCIS 5-Level Commissioning Process
**Created:** 2025-11-20
**Status:** Active
**Tags:** #commissioning #quick-reference #pgcis #field-guide

---

## 5-LEVEL COMMISSIONING PROCESS

| Level | Name | Location | When | Key Activities | Critical Deliverables |
|-------|------|----------|------|----------------|----------------------|
| **L1** | Factory Witness Testing (FWT/FAT) | Manufacturer facility | Before delivery | Factory test review, witness testing (if required), QA/QC | Factory test reports, as-built drawings, nameplate photos |
| **L2** | Pre-Start Up Documentation | Project site | During installation | Delivery inspection, storage verification, pre-energization checks | L2 forms, delivery photos, model verification |
| **L3** | Equipment Start-Up & PFT | Project site | After installation | Manufacturer startup, setpoint documentation, point-to-point verification | L3 startup docs, setpoint matrices, L1-3 Issues Log (closed) |
| **L4** | Functional Performance Testing (FPT) | Project site | After L3 complete | Equipment/system functional testing, load bank testing, issue resolution | L4 test procedures & data, circuit breaker verification, L4 Issues Log |
| **L5** | Integrated System Testing (IST) | Project site | After all L4 pass | Facility-level integrated testing, automatic response verification | L5 test data, Final Cx Report, Completion Certificate |

---

## COMPLETION CRITERIA BY LEVEL

**L1:** Factory test reports reviewed, equipment ready to ship
**L2:** Equipment delivered undamaged, pre-energization inspections complete
**L3:** Equipment started, BAS online, all setpoints documented, L1-3 issues closed
**L4:** All equipment/systems pass functional tests, L4 issues resolved or deferred
**L5:** Integrated systems pass under all conditions, Final Report issued, Certificate signed

---

## DEFICIENCY CLASSIFICATION

| Priority | Definition | Resolution Target | Example |
|----------|-----------|-------------------|---------|
| **Critical** | Impacts overall building functionality | Immediate | Life safety system failure |
| **High** | Impacts equipment/system functionality | 2 days | Generator fails to start |
| **Medium** | Impacts isolated equipment operation | 1 week | Single pump vibration issue |
| **Low** | Does not affect critical system functionality | Prior to L5 | Minor labeling error |

---

## KEY RESPONSIBILITIES (RACI)

| Party | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|-------|---------|---------|---------|---------|---------|
| **Manufacturer** | R (conduct FAT) | C (provide startup) | R (perform startup) | C (support testing) | C (support IST) |
| **Contractor** | I (provide specs) | R (install/inspect) | C (support startup) | C (support testing) | C (support IST) |
| **CxA** | C (review reports) | A (verify compliance) | A (witness, document) | R (direct & execute) | R (direct & execute) |
| **Owner** | A (approve scope) | A (approve readiness) | A (approve startup) | A (approve results) | A (accept completion) |
| **NETA** | - | - | C (electrical testing) | R (NETA testing) | C (support IST) |

**R** = Responsible | **A** = Accountable | **C** = Consulted | **I** = Informed

---

## TEST EQUIPMENT REQUIREMENTS

- **Calibration:** All test equipment calibrated within 12 months, NIST-traceable
- **Power Quality Analyzers:** Class A per IEC 61000-4-30
- **Load Banks:** Resistive, sized for 0-110% equipment rating
- **Thermal Imaging:** Minimum 160×120 resolution, ±2°C accuracy
- **Multimeters:** True RMS, CAT III or IV rated

---

## TESTING PHILOSOPHY

- **100% Sampling Protocol:** All equipment tested unless Owner approves exception
- **Progressive Testing:** Field device → Equipment → System → Integrated facility
- **Stop on Non-Compliance:** Testing stops until deficiency corrected
- **Retest Until Pass:** Continue retesting until acceptable results achieved
- **No Active Human Intervention:** L5 tests validate automatic responses only

---

## DOCUMENTATION PLATFORMS

**Primary:** CxAlloy commissioning software (web-accessible, real-time tracking)
**Issues Logs:** Track deficiencies from identification through resolution
**Test Forms:** Approved procedures with signature blocks for all parties
**Reports:** Daily status reports during testing, Final Report within 4 weeks of L5 completion

---

## CRITICAL TIMELINES

- **Factory Test Reports:** Due before equipment ships
- **L2 Forms:** Complete within 48 hours of equipment delivery
- **L3 Startup:** Per manufacturer schedule, before L4 begins
- **L4 Testing:** Progressive equipment-by-equipment completion
- **L5 IST:** Only after all L4 tests pass
- **Completion Certificate:** Issue within 48 hours of L5 completion
- **Final Cx Report:** Issue within 4 weeks of L5 completion

---

## COMMON L4/L5 TESTS (DATA CENTER)

**Electrical Systems:**
- Generator load bank tests (0-110% load, 2-hour steady-state)
- UPS load bank tests (0-110% load, transfer time verification)
- Static Transfer Switch (STS) transfer time testing (<10ms)
- Transformer inrush and energization
- Power quality monitoring (THD, voltage regulation, power factor)
- Protective relay settings verification

**Mechanical Systems:**
- Chiller capacity verification at design conditions
- Pump flow and head verification
- Cooling tower capacity and water quality
- CRAC/CRAH unit capacity and control sequence
- Building pressurization and airflow balancing

**Integrated Systems (L5):**
- Utility failure → Generator start/transfer
- Generator failure → Load transfer to redundant path
- Chiller failure → Lead-lag sequencing
- Fire alarm integration → HVAC shutdown sequences
- BAS trending and alarming under fault conditions

---

## KEY STANDARDS & CODES

- **NETA:** Acceptance Testing Standard (electrical)
- **IEEE Standards:** C57 (transformers), 519 (harmonics), 1100 (power quality)
- **NFPA:** 70 (NEC), 70E (electrical safety), 110 (emergency power)
- **ASHRAE:** Guideline 0 (commissioning), Standards 90.1 (energy)
- **IEC:** 61000-4-30 (power quality measurement)

---

## EMERGENCY CONTACTS

| Role | Name | Phone | Email |
|------|------|-------|-------|
| CxA Lead | [NAME] | [PHONE] | [EMAIL] |
| Owner Rep | [NAME] | [PHONE] | [EMAIL] |
| GC/CM | [NAME] | [PHONE] | [EMAIL] |
| Electrical Contractor | [NAME] | [PHONE] | [EMAIL] |
| Mechanical Contractor | [NAME] | [PHONE] | [EMAIL] |
| NETA Testing | [NAME] | [PHONE] | [EMAIL] |

---

## QUICK TROUBLESHOOTING

**Issue:** Equipment won't start during L3
→ Check: L2 complete? Pre-energization inspections pass? Temporary power available?

**Issue:** Test fails during L4
→ Document deficiency, assign priority, stop testing until corrected, retest

**Issue:** Can't complete L5 on schedule
→ Document as deferred test, get Owner approval, schedule completion date

**Issue:** Manufacturer not available for startup
→ Cannot proceed to L3 without manufacturer startup rep (per specification)

**Issue:** Test equipment not calibrated
→ Cannot use for acceptance testing (12-month calibration required)

---

**Related Documents:**
[[PGCIS Commissioning Standard - Master Specification]] | [[Cx Standard Appendix A - Testing Outline Template]] | [[Cx Standard Appendix B - Load Bank and Metering Plan Template]] | [[Cx Standard Level 1-5 Documentation Summary Checklists Template]] | [[Cx Standard README]]

---

**Document Version:** 1.0
**Last Updated:** 2025-11-20
**Print:** Laminate for field use | Keep in CxA site office
