

For a **low-runtime backup application**, a diesel reciprocating generator fleet will almost always have a **lower Total Cost of Ownership (TCO)** than a natural gas turbine fleet.

***

### Scenario 1: 4.2 MW Load (N+1)
For a 4.2 MW load, "N" is the required capacity. A common N+1 configuration would be:

* **Diesel Fleet:** 3 x 2.5 MW gensets (Total: 7.5 MW). "N" = 2 units (5.0 MW), "1" = 1 unit.
* **Turbine Fleet:** 2 x 4.3 MW turbines (Total: 8.6 MW). "N" = 1 unit, "1" = 1 unit.

| Cost Component          | Diesel Reciprocating (3 x 2.5 MW)                                                            | Gas Turbine (2 x 4.3 MW)                                                                                        | Key Takeaway                                            |
| :---------------------- | :------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| **Generator Cost**      | **~ $900 - $1,200 / kW**                                                                     | **~ $1,400 - $1,900 / kW**                                                                                      | Turbines are 50-70% more expensive per kW.              |
| **Emissions Control**   | **Included (Tier 4 Final)**: SCR, DPF, and DEF systems. Adds ~20-30% to engine cost.         | **Lower Cost**: Inherently cleaner. May only need a simple catalytic reduction system.                          | Diesel has complex, expensive after-treatment.          |
| **Fuel Infrastructure** | **On-site Tanks**: 3 x large belly tanks or 1-2 large bulk tanks (48hr+). **~$300k - $500k** | **Gas Pipeline**: Requires a high-pressure tap, metering, and a **gas compressor station**. **~$750k - $1.5M+** | The gas infrastructure is a major, hidden capital cost. |
| **Footprint/Struct.**   | **Larger Footprint**: 3 large units. Heavier (reciprocating mass). Requires a larger pad.    | **Smaller Footprint**: Turbines are very power-dense. Lighter weight.                                           | Turbine fleet saves valuable land space.                |
| **Est. Total CapEx**    | **$7.5M - $10.0M**                                                                           | **$13.0M - $18.0M**                                                                                             | **Diesel is significantly cheaper upfront.**            |

---

### The "Hidden" Costs That Define the Choice

#### 1. Operating & Maintenance Costs (The TCO Killer)

Since your runtime is low, your main OpEx isn't fuel—it's **maintenance**.
* **Diesel Maintenance (Higher Frequency, Lower Cost):**
    * You pay for *readiness*. This includes monthly/quarterly loaded tests.
    * **Proactive Costs:** Regular oil changes, filter changes, coolant checks, and battery testing.
    * **Fuel Management:** This is a *big* one. Diesel fuel "goes bad." You **must** pay for fuel polishing, biocide additives, and regular fuel quality testing.
    * **Emissions System:** You must keep Diesel Exhaust Fluid (DEF) tanks full. This fluid has a shelf life.

* **Turbine Maintenance (Lower Frequency, Higher Cost):**
    * They require far less "tinkering" (no oil changes, no coolant).
    * **The "LTSA":** You will almost certainly be in a **Long-Term Service Agreement** with the manufacturer (e.g., Solar Turbines, Caterpillar).
    * This is a fixed annual cost (often 6 figures) that covers readiness and guarantees.
    * It amortizes the cost of a future "hot section" (blade) overhaul, which can cost **$1M - $2M** after ~40,000 run-hours. Even if you *never* hit those hours, you pay for the *right* to have that service.

For low-runtime backup, the predictable, "pay-as-you-go" diesel maintenance is often cheaper than the fixed, high-cost LTSA for the turbine.

#### 2. Permitting & Emissions (The "Go/No-Go" Cost)

This is the #1 reason a data center (like the one in your doc) chooses a turbine, even if it's more expensive.

* **Diesel:** Permitting a fleet of 5 x 2.5 MW diesel generators is an *environmental nightmare*.
    * In many air quality non-attainment zones (like parts of California, Texas, or the Northeast), **it is impossible to get a permit** for this much new diesel capacity.
    * The application process can take *years* and cost millions in environmental studies and legal fees, with no guarantee of success.
    * You are limited to a very low number of annual runtime hours (e.g., 50-100 hours) for testing and emergencies *only*.

* **Gas Turbine:** This is the "easy button" for permitting.
    * They produce significantly lower NOx and virtually zero Particulate Matter (PM).
    * Regulators *vastly* prefer them. The permitting process is faster, cheaper, and more likely to be approved.
    * You can often get permits for *much higher* runtimes, allowing you to participate in grid "demand response" or "peak shaving" programs, which can *earn you money* and help offset the turbine's high cost.

### Final Recommendation:

Your analysis is correct: for pure backup, diesel is cheaper. However, the plan in your document is likely trying to balance **cost** with **permittability**.
* **The Diesel Gensets (Secondary):** This is your cheap, reliable, "black start" capacity. It gives you the fuel independence you're worried about. You might only install *just enough* diesel to pass permitting (e.g., 2 units) for critical N+1.
* **The Gas Turbine (Primary):** This is your "green" workhorse. It's expensive, but it's the *only* way you can get a permit for the *rest* of your capacity (4.3 MW). It satisfies ESG goals and air quality boards.

The "better move" isn't all-diesel or all-turbine. The best *financial and logistical* move is often the hybrid approach your document outlines: **permit one or two turbines to please the regulators, and supplement with diesel for cost and redundancy.**

