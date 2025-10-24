## The PUE vs. WUE Trade-Off ⚖️

This is the central conflict in modern data center cooling design. You can't optimize for both power and water simultaneously; improving one often sacrifices the other.

- **PUE (Power Usage Effectiveness):** Total Facility Energy / IT Equipment Energy. A lower PUE is better. A PUE of 1.0 is the theoretical perfect score.
    
- **WUE (Water Usage Effectiveness):** Annual Water Usage / IT Equipment Energy. A lower WUE is better.
    

Here’s where each is sacrificed:

### Where WUE is Sacrificed (For Better PUE) 💧

You sacrifice water efficiency anytime you use **evaporation** to help with cooling. This is exactly what the **RD109 baseline's adiabatic coolers** do.

- **How it works:** When water evaporates, it absorbs a tremendous amount of heat. By spraying a mist of water into the air entering the chiller, you lower the air temperature. This means the chiller's compressors don't have to work as hard, which saves a lot of electricity and **lowers your PUE**.
    
- **The cost:** This process consumes thousands of gallons of water, leading to a high (bad) WUE. This is a major concern in drought-prone areas and for companies with sustainability goals.
    

### Where PUE is Sacrificed (For Better WUE) ⚡

You sacrifice power efficiency when you rely **only on air** to cool the refrigeration coils during hot weather. This is what your proposed deviation—**eliminating adiabatic cooling**—will do.

- **How it works:** On a hot 95°F summer day in Oklahoma, the air-cooled chillers will have to run their compressors at full blast to reject heat. This consumes a significant amount of power and **raises your PUE** during the summer months (your doc correctly estimates a PUE of 1.25 - 1.35 in this period).
    
- **The benefit:** Your cooling system will use **zero water**. This gives you an excellent sustainability story, simplifies your system, and removes reliance on the local water supply for cooling. Your annual WUE for cooling will be nearly zero.