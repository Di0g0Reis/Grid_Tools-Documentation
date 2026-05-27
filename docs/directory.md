This `.json` file serves as a **central configuration file** that defines the overall setup for solving a case. It specifies the number of time periods to be considered in the optimization and provides the paths to all the necessary input files including topology, parameters, production and consumption data, and market data.

The `CSx.json` file acts as a master reference, allowing the solver to locate and organize all input data correctly. 
This page explains its structure, required fields, and how to correctly configure it to ensure seamless integration with the OPF and SC-OPF frameworks.
It's defined by a `.json` file named after the case scenario, for example, `CS2.json`. 

This file and all the files mentioned before are contained in a folder `CSx` and this folder is inside a folder called `data`. 


````json title="CSx.json"
{
	"NumInstants": 5,
	"PowerFlowData": {
		"BranchFlowViolationProbability": 0.05,
		"VoltageViolationProbability": 0.05,
		"DurationTimeInstant": 15
	},
	"MarketData": {
		"Filename": "CS4_market_data_IDA3_session.xlsx",
		"NumScenarios": 1,
		"GenerateSyntheticScenarios": true,
		"PlotScenarios": true
	},
	"NetworkData": {
		"NetworkFilename": "case30.json",
		"OperationalDataFilename": "case30_operational_data_IDA3_session.xlsx",
		"ParametersFilename": "case30_params.json",
		"NumScenarios": 20,
		"GenerateSyntheticScenarios": true,
		"PlotScenarios": true,
		"IsTransmission": true,
		"PlotNetworkDiagram": true,
		"PrintResults": true
	},
	"ContingencyData": [
		{"ContingencyID": 1, "Type": "generator", "ElementID": 2, "ContingencyInstant": 2},
		{"ContingencyID": 2, "Type": "generator", "ElementID": 5, "ContingencyInstant": 2},
		{"ContingencyID": 3, "Type": "line", "ElementID": 5, "ContingencyInstant": 2},
		{"ContingencyID": 4, "Type": "line", "ElementID": 8, "ContingencyInstant": 2}
	]
}
````


#### **Structure Breakdown**

|     Parameter      |       Data Type        | Explanation                                                                                                                                                                                                                                                                                |
|:------------------:|:----------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    NumInstants     |        integer         | Number of periods/instants to solve                                                                                                                                                                                                                                                        |
|   PowerFlowData    |     float/integer      | Contains the probability to allow a violation in the branchs capacity and the nodes voltage magnitude; and the duration (in minutes) of each instant mentioned above. In Portugual the TSO has 15 min to solve a contingency.                                                              |
|     MarketData     | string/integer/boolean | Contains the **Market data** file name and number of market scenarios to be considered; Tool for generation of synthetic scenarios and Plot command of said scenarios                                                                                                                      |
|    NetworkData     | string/integer/boolean | Contains the **Network topology**, **Operational data**, **Parameters configuration** file names and operational scenarios to be considered; Tool for generation of synthetic scenarios, Plot command of said scenarios and network diagram and, command to Print results to an Excel file |
|  ContingencyData   |     integer/string     | Indicates the ID of each contingency, the type of contingency and the ID of that element type that is in contingency, also contains the period/instant in which the contingency takes place                                                                                                |

!!! warning 

    For this to work, all the files must be placed within the same folder, which in turn should be located inside the project's ***data*** directory. For example, a folder named CS2 should contain the following files: ``caseX.json``, ``caseX_params.json``, ``caseX_operational_data.xlsx``, ``CS2_market_data.xlsx``, and ``CS2.json``.

In short:

``` mermaid
graph LR
   B[Network Topology] -->  A{Execution File};
  C[Number of instants to consider] -->  A;
  D[Duration of Instant] --> A;
  E[Probability to allow Violations to occur] --> A;
  F[Contingency Data] --> A;
  G[Parameters to be considered] -->  A;
  H[Network Operation Data] -->  A;
  I[Market Data] -->  A;
  A ---> |Needed in order to| J[Build Model];
  J --> |And then| K{Solve the case};
```