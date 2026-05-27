The **Security-Constrained Optimal Power Flow (SC-OPF)** is an advanced extension of the traditional OPF formulation that incorporates system security 
considerations into the optimization process. In addition to minimizing operational costs or losses, SC-OPF ensures that the power system remains within safe operating 
limits even under predefined contingency scenarios, such as line outages or generator failures (commonly referred to as N-1 security).

This approach is essential for maintaining system reliability and stability, especially in large-scale or critical infrastructure networks. 
By accounting for contingencies during the optimization, SC-OPF helps operators make decisions that are both economically efficient and resilient to unexpected disruptions.

In this section, you will learn how to set up and execute SC-OPF analyses and define contingency cases.
As described in [Overview](index.md) section, the package provides two SC-OPF formulations:

## **How to use the SC-OPF tools**
- **Security-Constrained Optimal Power Flow (SC-OPF)**
````python title="main.py"
from grid_management_tools import CaseStudy

    case_study = CaseStudy(working_directory, specification_filename)
    case_study.read_case_study()
    
    case_study.run_scopf(scopf_type=SCOPF_TYPE_PROBABILISTIC)
````
For the Chance-Constrained Security-Constrained Optimal Power Flow (CC-SC-OPF), two different solution frameworks are available, the first through **NonLinear Programming (NLP)** approach, and the second through **Mixed Integer Quadratic Programming (MIQP)**.  
- **Chance-Constrained Security-Constrained Optimal Power Flow (CC-SC-OPF) - NLP**
````python title="main.py"
    case_study.run_scopf(scopf_type=SCOPF_TYPE_NON_LINEAR_CHANCE_CONSTRAINED)
````

- **Chance-Constrained Security-Constrained Optimal Power Flow (CC-SC-OPF) - MIQP**
````python title="main.py"
   case_study.run_scopf(scopf_type=SCOPF_TYPE_BINARY_CHANCE_CONSTRAINED)
````

The results of each SC-OPF simulation are saved as Excel files in the ``Results`` older of the corresponding case scenario. The output files are named according to the case and SC-OPF type. 
For example, for the``CS2`` case, the generated files are:

- ``CS2_scopf_probabilistc.xlsx``
- ``CS2_scopf_non_linear_chance_constrained.xlsx``
- ``CS2_scopf_binary_chance_constrained.xlsx``.

The ``Results`` folder also contains a ``Logs`` directory with optimization log files. These logs store information such as the number of solver iterations 
and the execution time (in seconds) required to converge to a feasible solution.

To distinguish between the different SC-OPF formulations, the log files are named as follows:

- ``optim_log_sc-opf.log``
- ``optim_log_NLP_cc-sc-opf.log``
- ``optim_log_BINARY_cc-sc-opf.log``.

All result and log files are stored within the corresponding case scenario directory (e.g., inside the``CS2`` folder in this example). 
The generated Excel result files follow the same structure described in [Results Structure Breakdown](opf.md), with the additional feature that the results are also indexed by contingency scenario.

If you have not yet reviewed the [Execution File](directory.md) section, it is recommended to do so, as this component serves as the central link between all functionalities of the package.
