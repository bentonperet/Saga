
We're going to make major changes to the Basis of design: /Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design

  My Electrical Lead wants to change the phasing. I will need you to help me plan a comprehensive phase change, which will cascade through every BOD Doc and pricing detail! Let's make a special note in github when we start this work, in case we need to go back and check before / after on this change.

  I need you to think like an engineer and a top tier management consultant skilled in data center design and documentation, to make sure we're technically correct in our work, and that our documentation is complete and CONCISE - not too many words. WE SHOULD NOT BE ADDING SIGNIFICANT WORD/LINE COUNT TO THE CURRENT SPECS, WE SHOULD BE REDUCING AND CONDENSING LINES WHERE POSSIBLE AND STILL GETTING THE MESSAGE ACROSS TO THE CLIENT.

  Also - this is a long prompt and a big plan. I'd like to capture this plan in it's own MD file, and you should update that plan step by step so that we can come back to it if we run out of context, or we get interrupted. I don't want anything to go wrong in the update process, this will help us stay on track and keep relevant context handy for executing properly. I want to take it step by step, vs. trying to do lots of different things at once.

  Please help me sequence the updates in the most reasonable order for accuracy. And, of course, ask me questions if you need more clarity.

  THE CHANGES:

  The new phasing will be more simple. We will size by 6MW IT Load each block.
  Phase 1 - 6MW IT Load
  Phase 2 - 12
  Phase 3 - 18
  Phase 4 - 24

  We will use 3.6MW Generators. N=3 per block, N+1 = 4 gens per block.
  We will have 4 electrical houses per block (so same number as gens)

  We will size electrical using a 1.6PUE b/c it get's hot in OK, and we need about 10% of extra overhead. So those gens are sized correctly. About 10.8MW for 3 gens +1 for safety.

  We are missing Medium Voltage Switch Boards in our current electrical design. Those need to be added.

  Remove all reference of rack counts and number. We don't know what that's going to be and it's certainly going to change per client. If we need that for estimating factors, we can have an estimating number noted in the documents.

  When stating the estimated average PUE of the build, we can state 1.4, on the exec summary, but we'll calculate electrical on 1.6.
  
  Let's not do pricing yet, we'll work on that in another prompt.

---


Analyze this file: [copy path]

Make sure every single section, every line, is in alignment with our new design as expressed in _BOD. If unsure, flag it.

Let's update the doc to match.

  Furthermore, let's not add more content. I'm actually looknig to reduce the amount of information in this spec by around 30%. I want to make sure we're staying true to the basis of design and not providing too much information.
  Especially information we're not certain about. 


---
## Fire Supression Pricing

Start by reading this to understand the summary of my project as a whole: /Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/_BOD - Exec Summary.md

We will work on pricing for this section of the project - read this: /Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/3BOD - Fire Suppression (CSI Div 21).md

  Please review the spec and then look at the pricing summary. Was the cost table created with broad strokes estimating methods or was it done by bottom-ups pricing from an equipment list?

  What would be the better approach to get the most accurate price at this stage of the process?



---
## Plumbing Pricing

Start by reading this to understand the summary of my project as a whole: /Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/_BOD - Exec Summary.md

We will work on pricing for this section of the project - read this: /Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/4BOD - Plumbing (CSI Div 22).md

  Please review the spec and then look at the pricing summary. Was the cost table created with broad strokes estimating methods or was it done by bottom-ups pricing from an equipment list?

  What would be the better approach to get the most accurate price at this stage of the process?


---

### Pricing

 Go through the following files:
 /Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/2BOD - Facility Construction (CSI Divs 02-14).md

/Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/3BOD - Fire Suppression (CSI Div 21).md

/Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/4BOD - Plumbing (CSI Div 22).md

/Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/5BOD - HVAC (CSI Div 23).md

/Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/6BOD - Integrated Automation (CSI Div 25).md

/Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/7BOD - Electrical (CSI Div 26) v2.md

/Users/bentonperet/Library/CloudStorage/GoogleDrive-benperet@gmail.com/My Drive/P3R3T/PGCIS/Saga Obsidian/Saga1/Saga Pryor DC/Basis of Design/8BOD - Communications (CSI Div 27).md

## Context
- We will use Phase 4 design details for all pricing. Representing the final state of the data center when estimating equipment counts and pricing.
- This is a long prompt, please save your plan and work into an md file named Financial Working File, and make sure to regularly capture your progress, your next steps and all general information you'll need to pick the effort back up if you are to get interrupted or run out of context.
- Look for ways to parallel process and save context window to get this done efficiently but VERY accurately. Accuracy and attention to detail are CRITICAL.

## Instructions
- 2BOD - Please go line by line and reconfirm the line items in the cost table (and that they match our design - is anything missing or extra?) as well as have the correct numbers / counts / square footage, and the dollar amounts on this table. Also provide a % certainty column - how certain are you about this price. 
- 3BOD - Please go line by line and reconfirm the line items in the cost table (and that they match our design  - is anything missing or extra?) as well as have the correct numbers / counts, and the dollar amounts on this table. Also provide a % certainty column - how certain are you about this price.
- 4BOD - Please go line by line and reconfirm the line items in the equipment table (and that they match our design  - is anything missing or extra?) as well as have the correct numbers / counts. Add a cost table that matches the other, and confirm the dollar amounts on this table with your research. Also provide a % certainty column - how certain are you about this price.
- 5BOD - Please go line by line and reconfirm the line items in the equipment table (and that they match our design  - is anything missing or extra?) as well as have the correct numbers / counts. Add a cost table that matches the other, and confirm the dollar amounts on this table with your research. Also provide a % certainty column - how certain are you about this price.
- 6BOD - Please go line by line and reconfirm the line items in the cost table (and that they match our design  - is anything missing or extra?) as well as have the correct numbers / counts, and the dollar amounts on this table. Also provide a % certainty column - how certain are you about this price.
- 7BOD - Please follow the details in this prompt and generate an equipment and cost chart. PAY SPECIAL ATTENTION HERE - This is a particularly important spec as electrical is one of the most costly areas of a data center. Do not include any solar or BESS costs, however as they are on the SLD they can be in the equipment list.
- 8BOD - Please go line by line and reconfirm the line items in the cost table (and that they match our design  - is anything missing or extra?) as well as have the correct numbers / counts, and the dollar amounts on this table. Also provide a % certainty column - how certain are you about this price.

## Conclusion
You will have confirmed designs, counts and decisions. Researched pricing Added all the details to the equipment tables where asked. Added all detai