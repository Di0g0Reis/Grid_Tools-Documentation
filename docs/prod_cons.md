This Excel file provides time-dependent data for both **generation** and **consumption** associated with the elements in the network.
Each sheet represents a dataset related to specific elements such as generators or loads, and includes detailed profiles for power production, consumption, and availability.

This page explains how the data should be organized, the required fields for each sheet, and best practices for preparing consistent and accurate input.
It's defined by a `.xlsx` file named after the case, for example, `case9_operational_data.xlsx`.

This file is divided into 5 main sheets.

#### **Structure Breakdown**

| Sheet name | Data Type | Explanation                                                                                          |
|:----------:|:---------:|:-----------------------------------------------------------------------------------------------------|
|     Pc     |   float   | Value of **active power consumption** of each load (lines) in each period (columns)  per scenario    |
|     Qc     |   float   | Value of **reactive power consumption** of each load (lines) in each period (columns) per scenario   |
|    Flex    |   float   | Value of **flexibility** of each load (lines) in each period (columns) per scenario                  |
|     Pg     |   float   | Value of **active power generated** of each generator (lines) in each period (columns) per scenario  |
|     Qg     |   float   | Value of **reactive power generated** of each generator (lines) in each period (columns) per scenario|

If you want to simulate a framework with 20 scenarios, it is not necessary to manually create input data for all 20 scenarios. Instead, you may define only a small number of scenarios (e.g., 3 scenarios), 
since the package includes a scenario generation tool, as described in the [Execution File](directory.md). However, keep in mind that this tool generates new scenarios dynamically 
each time it is executed. Therefore, if you intend to perform extensive testing across a large number of scenarios while varying parameters, the generated scenarios 
may differ between executions, making direct comparisons more difficult.

For reproducibility and consistent benchmarking, we recommend manually building the Excel input file with all desired scenarios and disabling the automatic scenario generation tool.