# Uptime Tier Compliance Skill

## Overview

This skill validates data center designs against Uptime Institute Tier Standards and assesses certification readiness.

## How It Works With Existing Documentation

### Two Complementary Resources:

**1. This Skill (Design Validator)**
- **Location**: `.claude/skills/uptime-tier-compliance/`
- **Purpose**: Analyze BOD documents for tier compliance
- **Use during**: Design development and pre-submittal review
- **Outputs**: Gap analysis, compliance reports, recommendations

**2. Uptime Certification Submittal Requirements (Document Checklist)**
- **Location**: `../GGE BoD Template/Uptime Design Certification/Uptime Certification.md`
- **Purpose**: Official list of documents required for Uptime Institute submittal
- **Use during**: Submittal package preparation
- **Outputs**: Checklist of required deliverables

### Workflow Integration

```
Phase 1: Design Development
├─ Use this skill to validate compliance as you develop BODs
├─ Identify gaps early in design process
└─ Make corrections before designs are finalized

Phase 2: Pre-Submittal Review
├─ Use this skill for comprehensive gap analysis
├─ Generate compliance report
└─ Verify all tier requirements are met

Phase 3: Submittal Preparation
├─ Use Uptime Certification.md checklist
├─ Gather all required documents
├─ Package for Uptime Institute review
└─ Submit TCDD (Tier Certification of Design Documents)

Phase 4: Certification
├─ Uptime Institute reviews submittal
├─ Address any comments or deficiencies
└─ Receive tier certification
```

## Quick Start

**To validate a design:**
```
"Review the electrical BOD for Tier III compliance"
"Check if the mechanical system meets Tier IV requirements"
"Assess GGE design for tier certification readiness"
```

**To prepare for submittal:**
```
"Check if we have all required documents for Tier III submittal"
"Generate a submittal readiness report"
```

## Files in This Skill

- **SKILL.md**: Main skill instructions (validation logic, checklists)
- **tier-requirements.md**: Detailed tier requirement matrices
- **README.md**: This file (overview and integration guide)

## Reference Standards

- Uptime Institute Tier Standard: Topology
- ANSI/TIA-942: Telecommunications Infrastructure Standard for Data Centers
- ASHRAE TC 9.9: Data Center Guidelines

---

**Created**: 2025-11-04
**For**: GGE Data Center Project
