The `CSY.xlsx` file contains a **single sheet** with market-related data necessary for running market-oriented optimizations like MP-OPF. It provides cost curves, bids, offers, and other market-related parameters that define how generation and consumption units interact within the market framework.

Here, you will find explanations of the required data structure, expected formats, and guidance on how to properly define market participation inputs for each actor in the system.
It's defined by a `.xlsx` file named after the case scenario, for example, `CS2_market_data.xlsx`.

This sheet contains the following data.

#### **Data Breakdown**:

| Data  | Data Type | Explanation                                       |
|:-----:|:---------:|:--------------------------------------------------|
|  Cp   |   float   | **Cost of production** for each period            |
| Cflex |   float   | **Flexibility of that same cost** for each period |
