The `CSY.xlsx` file contains two sheets with market-related data necessary for running market-oriented optimizations.
It provides cost curves, bids, offers, and other market-related parameters that define how generation and consumption units interact within the market framework.

Here, you will find explanations of the required data structure, expected formats, and guidance on how to properly define market participation inputs for each actor in the system.
It's defined by a `.xlsx` file named after the case scenario, for example, `CS2_market_data.xlsx`.

This file contains the following data.

#### **Data Breakdown**:

|    Sheet    | Data Type | Explanation                                                           |
|:-----------:|:---------:|:----------------------------------------------------------------------|
|   Energy    |   float   | **Cost of production** for each period and market scenario            |
| Flexibility |   float   | **Flexibility of that same cost** for each period and market scenario |

If you want to simulate a framework with 20 scenarios, it is not necessary to manually create input data for all 20 scenarios. Instead, you may define only a small number of scenarios (e.g., 3 scenarios), 
since the package includes a scenario generation tool, as described in the [Execution File](directory.md). However, keep in mind that this tool generates new scenarios dynamically 
each time it is executed. Therefore, if you intend to perform extensive testing across a large number of scenarios while varying parameters, the generated scenarios 
may differ between executions, making direct comparisons more difficult.

For reproducibility and consistent benchmarking, we recommend manually building the Excel input file with all desired scenarios and disabling the automatic scenario generation tool.