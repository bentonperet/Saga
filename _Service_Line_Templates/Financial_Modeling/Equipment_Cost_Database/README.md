# Equipment Cost Database - README

**Created:** 2025-11-20
**Last Updated:** 2025-11-20
**Tags:** #pricing #equipment #database #documentation
**Version:** 1.0

---

## Overview

This database contains validated equipment pricing for data center infrastructure components as of November 20, 2025. The pricing is sourced from vendor quotes and represents current market rates for major equipment categories including power distribution, cooling systems, generators, transformers, and modular infrastructure.

---

## Database Structure

### Core Files

1. **[[Equipment_Pricing_Database]]** - Main pricing database
   - Complete equipment catalog organized by category
   - Unit pricing for all equipment
   - Pricing analysis notes and observations
   - Data quality flags for items requiring verification

2. **[[Equipment_Index_By_Vendor]]** - Vendor/seller index
   - Equipment organized by vendor/seller
   - OEM brand information
   - Product line counts per vendor
   - Vendor comparison statistics

3. **[[Equipment_Index_By_Category]]** - Category index
   - Equipment grouped by functional category
   - Quick cost estimating guides
   - Price per MW calculations
   - Category summary statistics

---

## How to Use This Database

### Finding Equipment Pricing

**By Equipment Name:**
1. Open `Equipment_Pricing_Database.md`
2. Use Ctrl+F to search for equipment model number or description
3. Review unit price and any associated notes

**By Vendor:**
1. Open `Equipment_Index_By_Vendor.md`
2. Locate the vendor section
3. Review all equipment available from that vendor

**By Category (e.g., UPS, Generators, Chillers):**
1. Open `Equipment_Index_By_Category.md`
2. Navigate to the relevant category section
3. Compare options within that category

### Cost Estimating

**Quick Estimates:**
- Use the "Quick Cost Estimating" section in `Equipment_Index_By_Category.md`
- Reference the "Cost per IT MW" calculations for typical builds
- Apply category averages for preliminary budgets

**Detailed Estimates:**
- Reference specific equipment in `Equipment_Pricing_Database.md`
- Check for included items (PIUs, tap boxes, etc.) to avoid double-counting
- Review notes for pricing anomalies or verification items

---

## Data Quality & Validation

### Current Status

**Data Source:** Vendor quotes compiled 2025-11-20
**Coverage:** 46 unique product lines from 11 vendors
**Completeness:** Initial database - requires validation

### Items Flagged for Verification

The following items require vendor verification due to pricing anomalies:

1. **34.5kV Transformers** - Pricing ($20,994) significantly lower than lower voltage transformers
2. **KOHLER 3MW Generator** - Two different prices ($2.45M vs $563K)
3. **Busway Systems** - Identical pricing across different amperage ratings
4. **Thermal Storage Tanks** - Same price for different capacities (15K vs 30K gallons)
5. **Units of Measure** - Confirm "each" vs "per foot" vs "per section" for all equipment

### Recommended Validation Steps

Before using for project budgets:
- [ ] Verify flagged items with vendors
- [ ] Confirm units of measure for all equipment
- [ ] Cross-reference with historical project data
- [ ] Apply appropriate escalation factors for project timeline
- [ ] Confirm scope of supply (what's included/excluded)

---

## Equipment Categories Covered

### Power Distribution & Protection
- UPS systems (250 kVA - 1250 kVA)
- Static transfer switches (800A)
- Automatic transfer switches (70A)
- Busway systems (400A - 800A, PIUs)
- Reserve busduct (4000A)

### Transformers
- 13.2kV transformers (KNAN/KNAF cooling)
- 18kV transformers (KNAN/KNAF cooling)
- 34.5kV transformers (KNAN/KNAF cooling)

### Switchgear
- 38kV medium voltage switchgear
- Generator switchboards

### Generators
- 1.25 MW (CAT)
- 2.8 MW (KOHLER)
- 3.0 MW (KOHLER)
- 3.5 MW (KOHLER)

### Cooling Systems
- Water-cooled chillers (500 ton)
- CRAH units (60 kW)
- DOAS units
- Fan walls (72K CFM)
- Humidifiers

### Pumping & Piping
- Chilled water pump skids
- Quick disconnect couplers

### Thermal Storage
- Horizontal tanks (15K - 30K gallons)
- Vertical tanks (30K gallons)

### Modular Systems
- IT infrastructure modules
- Mechanical modules

### Services
- Commissioning support
- Repair services

---

## Vendor Directory

| Vendor | Primary Equipment | Contact Info |
|--------|-------------------|--------------|
| CERIO | UPS, STS, Busway, Generators | TBD |
| EAE | Reserve Busduct | TBD |
| GIGA ENERGY | Transformers | TBD |
| HYDRAQUIP | Piping Components | TBD |
| JCI | Chillers, Fan Walls | TBD |
| JCL ENERGY | Transformers | TBD |
| MCG | Modular Systems, Switchgear | TBD |
| STARLINE | Busway Services | TBD |
| SVL | CRAH, DOAS, Humidifiers | TBD |
| T5 | CAT Generators | TBD |
| TEXAS AIR SYSTEMS | Pumps, Thermal Storage | TBD |

**Total Vendors:** 11
**Total OEMs Represented:** 18

---

## Pricing Benchmarks

### Cost per IT Megawatt (Typical Configuration)

**Power Infrastructure:** ~$3.3M per IT MW
- Includes UPS, STS, busway systems
- Based on N+1 redundancy

**Cooling Infrastructure:** ~$2.4M per IT MW
- Includes chillers, fan walls, CRAH units
- Based on air-cooled economizer design

**Total Equipment Cost:** ~$5.7M - $6.0M per IT MW
- Does not include installation labor
- Does not include site-specific equipment (substations, etc.)

### Price per Capacity Metrics

**Generators:**
- Large generators (2.8-3.5 MW): $525K - $703K per MW
- Medium generators (1.25 MW): $662K per MW

**Chillers:**
- 500-ton units: ~$1,167 per ton

**UPS Systems:**
- Large capacity (1250 kVA): ~$282 per kVA
- Medium capacity (250 kVA): ~$476 per kVA

---

## Update & Maintenance

### Version Control

All changes to the database should be documented in the version history table at the bottom of each file.

**Update Process:**
1. Make changes to relevant file(s)
2. Update "Last Updated" date at top of file
3. Add entry to version history table
4. Document significant changes in this README

### Price Escalation

**Note:** This pricing is valid as of 2025-11-20. For future projects:
- Apply appropriate escalation factors
- Verify pricing with vendors for projects >6 months out
- Consider market conditions (supply chain, demand, etc.)

**Suggested Escalation Rates** (to be updated based on market conditions):
- General electrical equipment: 3-5% annually
- Mechanical equipment: 4-6% annually
- Specialty items (generators, modules): 2-4% annually

### Adding New Equipment

When adding new equipment to the database:

1. Add to `Equipment_Pricing_Database.md` in appropriate category
2. Add to `Equipment_Index_By_Vendor.md` under vendor section
3. Add to `Equipment_Index_By_Category.md` in relevant category
4. Update summary statistics in all files
5. Flag any anomalies or items requiring verification
6. Update version history

---

## Related Resources

### Internal Links
- [[Equipment_Pricing_Database]] - Main database
- [[Equipment_Index_By_Vendor]] - Vendor index
- [[Equipment_Index_By_Category]] - Category index

### External Resources
- Vendor contact information: (to be added)
- Historical pricing data: (to be linked)
- Project budget templates: (to be linked)

---

## Usage Notes

### Best Practices

1. **Always verify current pricing** with vendors before finalizing budgets
2. **Check included items** to avoid double-counting equipment
3. **Apply appropriate contingencies** based on project phase:
   - Conceptual design: 25-30%
   - Schematic design: 20-25%
   - Design development: 15-20%
   - Construction documents: 10-15%
4. **Consider lead times** - some equipment has 12+ month delivery
5. **Account for escalation** for projects starting >6 months out

### Common Pitfalls to Avoid

- Using 34.5kV transformer pricing without verification (appears too low)
- Assuming all busway pricing is per linear foot (may be per section)
- Not accounting for items "included in" other equipment
- Failing to add installation labor and site-specific costs
- Using thermal storage pricing without confirming capacity difference

---

## Support & Questions

For questions about this database or to report issues:

1. Check the data quality notes in `Equipment_Pricing_Database.md`
2. Review the category and vendor indexes for context
3. Verify assumptions against vendor quotes
4. Document any corrections or updates

---

## Version History

| Date | Version | Changes | Updated By |
|------|---------|---------|------------|
| 2025-11-20 | 1.0 | Initial database creation with 46 product lines from 11 vendors | Claude |

---

## Quick Start Guide

**New to this database?** Follow these steps:

1. **Browse the equipment:**
   - Open `Equipment_Pricing_Database.md`
   - Review the equipment categories
   - Note items flagged for verification

2. **Understand the vendors:**
   - Open `Equipment_Index_By_Vendor.md`
   - See which vendors supply which equipment types
   - Review vendor product line breadth

3. **Estimate costs:**
   - Open `Equipment_Index_By_Category.md`
   - Use the quick estimating guides
   - Reference cost per MW calculations

4. **Validate before use:**
   - Check the data quality section
   - Verify flagged items with vendors
   - Apply appropriate contingencies

