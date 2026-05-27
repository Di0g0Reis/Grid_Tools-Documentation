Power flow analysis is one of the most important static operations in power network calculations. 
This section explains how to use the different types of **Optimal Power Flow (OPF)** analyses available in this Python package. 
As described in [Overview](index.md) section, the package provides three OPF formulations that do not consider contingencies:

## **How to use the OPF tools**
- **Probabilistic Optimal Power Flow (P-OPF)**
````python title="main.py"
from grid_management_tools import CaseStudy

    case_study = CaseStudy(working_directory, specification_filename)
    case_study.read_case_study()
    
    case_study.run_opf(opf_type=OPF_TYPE_PROBABILISTIC)
````

- **Stochastic Optimal Power Flow (S-OPF)**
````python title="main.py"
    case_study.run_opf(opf_type=OPF_TYPE_STOCHASTIC)
````

- **Chance-Constrained Optimal Power Flow (CC-OPF)**
````python title="main.py"
    case_study.run_opf(opf_type=OPF_TYPE_CHANCE_CONSTRAINED)
````

The results of each OPF simulation are saved as Excel files in the ``Results`` older of the corresponding case scenario. The output files are named according to the case and OPF type. For example, for the
``CS2`` case, the generated files are:
- ``CS2_opf_probabilistc.xlsx``
- ``CS2_opf_stochastic.xlsx``
- ``CS2_opf_chance_constrained.xlsx``.

The ``Results`` folder also contains a ``Logs`` directory with optimization log files. These logs store information such as the number of solver iterations 
and the execution time (in seconds) required to converge to a feasible solution.

To distinguish between the different OPF formulations, the log files are named as follows:
- ``optim_log_probabilistic_opf``
- ``optim_log_stochastic_opf``
- ``optim_log_cc-opf``.

All result and log files are stored within the corresponding case scenario directory (e.g., inside the``CS2`` folder in this example).



## **Results Structure Breakdown**

The results file contains multiple sheets, starting with the ``main`` sheet, which provides a summary of the entire Excel file. Additional sheets include detailed information such as the power flow through each line and other relevant network parameters.


|    Sheet Name     | Data Type | Explanation                                                                                                                                      |
|:-----------------:|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------|
|     Main Info     |   float   | Summary of all results, including:  Conventional generation and cost, Renewable generation and curtailed, Load flexibility and cost, Losses, etc |
| Market Cost Info  |   float   | Info about the market per scenario and period                                                                                                    |
|      Voltage      |   float   | **Voltage** results (phase and magnitude) per scenario and period                                                                                |
|    Consumption    |   float   | **Consumption** data (reactive and active power) per scenario and period                                                                         |
|    Generation     |   float   | **Generation** results (reactive and active power) per scenario and period                                                                       |
|   Branch Losses   |   float   | **Losses** in each branch per scenario and period                                                                                                |
|   Transformers    |   float   | Contains the Tap position and Ratio of each **Transformer** per scenario and period                                                              |
|  Branch Loading   |   float   | Refers to how much of the **branch capacity** is being used in a certain direction                                                               |
|    Power Flows    |   float   | **Power Flow** results in each branch per scenario and period                                                                                    |
|  Energy Storage   |   float   | **Energy Storage units** results (e.g, P [MW], SoC [MWh] and SoC [%]) through out every period for each scenario                                 |
| Relaxation Slacks |   float   | **Relaxation Slacks** used and their respected values                                                                                            |