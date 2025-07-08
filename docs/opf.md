Power flow analysis is the most critical static operation in network calculations. This section explains how to perform various types of power flow analyses (MP-OPF and SC-OPF), highlights known issues and limitations.
=== "Available OPF's"

    * [Multi-Period Optimal Power Flow](mp_opf.md)
    * [Security-Constrained Optimal Power Flow](sc_opf.md)

The results of each OPF solution are saved as Excel files named according to the case and the OPF type. For example: ``CS2_MP-OPF_results.xlsx`` and ``CS2_SC-OPF_results.xlsx``.

These result files are stored in a "Results" folder located within the corresponding case scenario directory (e.g., within the ``CS2`` folder in this example).



#### **Results Structure Breakdown**:

The results file contains multiple sheets, starting with the ``main`` sheet, which provides a summary of the entire Excel file. Additional sheets include detailed information such as the power flow through each line and other relevant network parameters.


|    Sheet Name     | Data Type | Explanation                                                                                  |
|:-----------------:|:---------:|:---------------------------------------------------------------------------------------------|
|     Main Info     |   float   | Summary of all results. Including Objective, losses, renewable generation, etc. per scenario |
| Market Cost Info  |   float   | Info about the market per scenario and period                                                |
|      Voltage      |   float   | **Voltage** results (phase and magnitude) per scenario and period                            |
|    Consumption    |   float   | **Consumption** data (reactive and active power) per scenario and period                     |
|    Generation     |   float   | **Generation** results (reactive and active power) per scenario and period                   |
|   Branch Losses   |   float   | **Losses** in each branch per scenario and period                                            |
| Transformer Ratio |   float   | **Transformer Ratio** of each transformer                                                    |
|  Branch Loading   |   float   | Refers to how much of the **branch's capacity** is being used in a certain direction         |
|    Power Flows    |   float   | **Power Flow** results in each branch per scenario and period                                |
