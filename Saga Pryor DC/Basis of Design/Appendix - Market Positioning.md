

# APPENDIX: MARKET POSITIONING & VALUE PROPOSITION
## Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[_BOD - Exec Summary]]  


---
## PURPOSE

This appendix provides detailed market positioning, customer profiles, and value proposition analysis for the Pryor Data Center. This content supports sales, marketing, and business development efforts but is separated from the technical Basis of Design documents to maintain their focus on engineering specifications.

---
## STRATEGIC LOCATION ADVANTAGE

### Google Cloud Proximity

The Pryor DC is located **4 miles from Google's us-central2 data center campus** in Pryor, Oklahoma. This proximity enables a **direct fiber interconnect** (Google Cloud Interconnect / Partner Interconnect) that fundamentally changes the economics and performance of AI/ML workloads.

**Physical Infrastructure:**
- Distance: 4 miles from Google campus
- Interconnect type: Google Cloud Interconnect / Partner Interconnect
- Capacity: 100 Gbps private fiber (scalable)
- Latency: <1ms round-trip

---
## TARGET CUSTOMER PROFILES

### Customer #1: AI Training Cluster (Primary Target)

**Who They Are:**
- AI cloud providers (CoreWeave, Lambda Labs, Crusoe Energy style)
- Enterprise ML teams running large-scale GPU training clusters
- Research institutions building large language models

**The Problem They Face:**

1. **Data Egress Costs:**
   - Training a large language model requires 500 TB - 5 PB of training data
   - GCP data egress pricing: **$0.08 - $0.12/GB** to internet
   - Moving 500 TB over public internet = **$40,000 - $60,000** in egress fees alone
   - Plus ongoing costs for iterative training (multiple runs with different hyperparameters)

2. **Data Transfer Speed:**
   - 500 TB over 10 Gbps internet connection = **4.6 days** of continuous transfer
   - Training jobs sit idle waiting for data
   - Engineers burn time debugging slow transfers
   - Competitive disadvantage (slower iteration cycles)

3. **GCP Compute Costs:**
   - Running H100 GPUs on Google Cloud = **~$500K per large model training job**
   - Customers need 60-70% cost reduction to be competitive

**The Pryor DC Solution:**

1. **Direct Fiber Interconnect:**
   - 100 Gbps private link to Google
   - <1ms latency
   - Bypasses public internet entirely

2. **Egress Cost Reduction:**
   - $40K-$60K → $5K-$10K per training run
   - 5-10× savings via interconnect pricing (@$0.01-$0.02/GB)
   - Savings: **$30,000 - $50,000 per training run**
   - ROI: Interconnect pays for itself in 2-3 training cycles

3. **Transfer Speed:**
   - 500 TB transfer time = **11 hours** (not 4.6 days)
   - **10× faster data movement** = 10× more training iterations per month
   - Enables rapid experimentation and model tuning

4. **Compute Cost Reduction:**
   - Customer-owned GPUs at Pryor DC colocation rates = ~$150K per training job
   - vs. $500K on GCP
   - **70% cost savings**

**Hybrid Cloud Architecture:**
```
Customer's GCP Environment (us-central2, Pryor)
├─ Production databases (Cloud SQL, BigQuery)
├─ Training datasets (500 TB in Cloud Storage)
├─ Versioned models (Cloud Storage)
├─ Application layer (GKE, Cloud Run)
└─ Real-time serving infrastructure
        ↕
  100 Gbps Direct Fiber (<1ms latency)
        ↕
Pryor DC Training Cluster (Phase 1: 30 racks, 240 GPUs)
├─ Pull training data from GCP via interconnect
├─ Train models for 48-72 hours
├─ Push completed model back to GCP
└─ Customer deploys from GCP (never leaves Google ecosystem)
```

**Why Customers Choose This Hybrid Model:**
- Data never leaves Google's security perimeter (just moves 4 miles via private fiber)
- Existing GCP applications/databases unchanged
- 60-70% lower compute cost vs. GCP's A100/H100 instances
- Same compliance posture (data in GCP, compute adjacent)
- No vendor lock-in (can move workloads back to GCP anytime)

**Customer Value Proposition:**
*"Keep your data in Google Cloud where it's safe and accessible. When you need massive GPU power, pull it over our high-speed link to our specialized AI infrastructure 4 miles away. Train at 1/3 the cost. Push the trained model back. Your customers never know it left Google's network."*

**Economics That Close the Deal:**
- Training 1 large language model on GCP: ~$500K
- Same training at Pryor DC (customer-owned GPUs, colo rates): ~$150K
- **Savings per model:** $350K (70% cost reduction)
- Interconnect cost: ~$5K/month (100 Gbps port)
- **ROI:** Interconnect pays for itself in less than 1 week of training

**Ideal Phase 1 Anchor Profile:**
- Already has GCP customers wanting cheaper GPU access
- Needs 30 racks (240 GPUs) to start, plans to scale to 100+ racks
- Values: GCP proximity + cheap power + liquid cooling ready from day 1

**The Sales Pitch:**
*"Your customers keep their data in Google Cloud in Pryor. You run training jobs only 4 miles away at 1/3 the cost. Direct fiber interconnect means 500 TB datasets transfer in hours, not days. Save $50K per training run on egress fees alone. Your customers never leave the Google ecosystem. You just give them access to cheaper, denser GPUs with liquid cooling from day 1."*

---

### Customer #2: AI Inference (Primary Target)

**Who They Are:**
- SaaS companies using Google Cloud for production workloads
- Real-time AI applications: chatbots, recommendation engines, autonomous systems
- Companies needing ultra-low latency to GCP for live user requests

**Why Proximity Matters:**
1. **Latency-Sensitive Workloads:**
   - Every millisecond counts for user experience
   - Sub-millisecond to GCP us-central2 enables real-time applications

2. **Data Locality:**
   - Keep training data in GCP
   - Run inference 4 miles away
   - Query databases in GCP in real-time

3. **Cost Arbitrage:**
   - GCP compute is expensive
   - Pryor DC colocation is 40-60% cheaper
   - Same performance, lower cost

4. **Hybrid Architecture:**
   - Database in GCP
   - Inference models at Pryor DC
   - Sub-ms latency between them
   - No egress fees for inference queries/responses

**Example Use Case:**

*E-commerce Recommendation Engine*
- Customer stores 100 TB of product catalog data in Google Cloud Storage
- Inference models run at Pryor DC (ML models for recommendations)
- User requests flow: User → GCP API → Pryor DC inference → GCP → user response
- Total latency: <5ms end-to-end

**The Value:**
- **Ultra-low latency:** Sub-millisecond to GCP us-central2
- **Cost arbitrage:** Inference compute 40-60% cheaper than GCP native instances
- **Data locality:** Keep databases/applications in GCP, run inference nearby
- **No egress fees:** Inference queries/responses via interconnect (minimal data transfer)

**Specifications:**
- 30-60 kW/rack average density
- Flexible cooling (air or D2C, customer choice)
- Tier III power reliability
- 24/7 mission-critical uptime

---

### Customer #3: Industrial Enterprise (MAIP Tenants)

**Who They Are:**
- Local high-reliability compute needs
- Oklahoma industrial base: aerospace, energy, ag-tech
- Digital twins, IoT, manufacturing control systems

**Why They Choose Pryor:**
- Local presence (Oklahoma/Arkansas industrial corridor)
- Tier III reliability
- Lower cost than Dallas/Kansas City
- Not latency-dependent on cloud providers

**Specifications:**
- 8-25 kW/rack mixed density
- Standard air cooling
- Tier III power (N+1 UPS)
- High reliability but not bleeding-edge

**Target Phase:** Phase 2+ (multi-tenant fill)

---

### Customer #4: Specialty Compute (Capacity Filler)

**Who They Are:**
- Crypto mining/staking operations
- Rendering farms
- Academic batch processing
- Any workload tolerant of interruptions

**Why They Choose Pryor:**
- Lowest possible cost-per-kilowatt
- Interruptible pricing (30-40% discount)
- High-density capability
- Cheap Oklahoma power

**Key Differentiator: Interruptible Power**

Third power distribution path:
- Fed directly from substation (bypass UPS)
- Can shed load during grid emergencies
- 30-40% lower power pricing
- Can tolerate outages

**Specifications:**
- 30-80 kW/rack high density
- Hot-aisle containment (can tolerate high temps)
- Interruptible / Non-UPS power
- Cost-optimized over reliability

**Electrical Implication:**

Requires third power distribution path:
1. **Tier III Critical (IT UPS)** - Customers #1, #2, #3
2. **House Power (Non-Critical)** - Building services
3. **Interruptible Power (Non-UPS)** - Customer #4

**Target Phase:** Phase 2+ (margin optimizer)


---

### vs. Google Cloud Native Compute

**Pryor DC Advantages:**
- **60-70% lower $/GPU-hour** (customer-owned hardware + colo rates)
- **Customer controls refresh cycle** (not locked to GCP's hardware upgrade schedule)
- **No egress fees** for intra-region data movement via interconnect
- **Cost predictability** (fixed colo rates vs. variable cloud pricing)

**Google Cloud Advantages:**
- Fully managed (no infrastructure overhead for customer)
- Instant elasticity (scale up/down on demand)
- Integrated with GCP services

**Best Fit for Pryor:**
- Predictable, sustained workloads (AI training, batch processing)
- Customers wanting to own hardware
- Cost-sensitive workloads needing cloud proximity

---

## REVENUE MODEL

### Phase 1 Anchor Tenant (AI Training)

**Pricing Model:**
- Power: $100-150/kW/month (dense D2C racks)
- 30 racks × 100 kW × $125/kW = **$375K/month**
- Annual revenue: **$4.5M** from single anchor

**Margins:**
- Power cost: ~$0.04/kWh Oklahoma = ~$30/kW/month
- Gross margin: ~75% on power
- Additional revenue: interconnect fees, hands & eyes, managed services

---

### Phase 2+ Multi-Tenant (Mixed Customer Types)

**Blended Pricing:**
- AI Training/Inference (dense): $100-150/kW/month
- Industrial Enterprise (standard): $80-120/kW/month
- Specialty Compute (interruptible): $50-80/kW/month

**Phase 2 Revenue Target (6 MW):**
- ~$600K-750K/month
- Annual revenue: **$7.2M-9M**

---

## GO-TO-MARKET STRATEGY

### Phase 1: Anchor Acquisition (Months 1-6)

**Target:** Single 3 MW AI training anchor

**Channels:**
1. Direct outreach to AI cloud providers (CoreWeave, Lambda Labs, etc.)
2. Enterprise ML teams at large tech companies
3. Google Cloud partner network
4. AI/ML conferences and events

**Key Message:**
*"Train AI models at 1/3 the cost, 4 miles from Google Cloud"*

---

### Phase 2: Diversification (Months 7-18)

**Target:** Fill remaining capacity with mixed customer types

**Channels:**
1. Colocation brokers
2. Oklahoma economic development
3. Regional industrial customers
4. Crypto/rendering farm operators

**Key Message:**
*"Midwest reliability, Google Cloud proximity, competitive pricing"*

---

## APPENDIX REFERENCES

**Related BOD Sections:**
- [[_BOD - Exec Summary|Executive Summary]] - High-level overview
- [[7BOD - Electrical (CSI Div 26) vOLD|Electrical BOD]] - Interruptible power path details
- [[Saga Pryor DC/Basis of Design/5BOD - HVAC (CSI Div 23)|Mechanical BOD]] - D2C cooling for AI workloads
- [[Saga Pryor DC/_Project Management/Design Notes/Phasing_Strategy_Discussion_Context|Phasing Strategy]] - Customer-driven buildout approach

**External References:**
- [[Saga Pryor DC/Reference Materials/GCP Interconnection - Complete Guide|GCP Interconnection Guide]] - Technical details on Google Cloud Interconnect

---

**Document Status:** Living document - update as market intelligence and customer feedback evolves
**Last Updated:** 2025-11-03
**Owner:** Business Development / Sales
