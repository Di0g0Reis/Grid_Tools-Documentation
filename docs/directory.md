This `.json` file serves as a **central configuration file** that defines the overall setup for solving a case. It specifies the number of time periods to be considered in the optimization and provides the paths to all the necessary input files including topology, parameters, production and consumption data, and market data.

The `CSY.json` file acts as a master reference, allowing the solver to locate and organize all input data correctly. This page explains its structure, required fields, and how to correctly configure it to ensure seamless integration with the SC-OPF or MP-OPF solvers.
It's defined by a `.json` file named after the case scenario, for example, `CS2.json`.


````json title="CSY.json"
{
	"NumInstants": 1,
	"Network":
		{
			"NetworkFilename": "case300.json",
			"ParamsFilename": "case300_params.json",
			"OperationalDataFilename": "case300.xlsx",
			"MarketDataFilename": "CS2_market_data.xlsx"
		}
}
````


#### **Structure Breakdown**:

|        Parameter        | Data Type | Explanation                                                    |
|:-----------------------:|:---------:|:---------------------------------------------------------------|
|       NumInstants       |  integer  | Number of periods to solve                                     |
|     NetworkFilename     |  string   | **Topology** file of the network to be studied                 |
|     ParamsFilename      |  string   | **Parameters configuration** file of the network to be studied |
| OperationalDataFilename |  string   | **Operational data** file of the network to be studied         |
|   MarketDataFilename    |  string   | **Market data** file to be considered                          |

!!! warning 

    For this to work, all the files must be placed within the same folder, which in turn should be located inside the project's ***data*** directory. For example, a folder named CS2 should contain the following files: ``caseX.json``, ``caseX_params.json``, ``caseX.xlsx``, ``CS2_market_data.xlsx``, and ``CS2.json``.

In short:

``` mermaid
graph LR
   B[Network Topology] --> |Goes to| A{Execution File};
  C[Number of instants to consider] --> |Goes to| A;
  D[Parameters to be considered] --> |Goes to| A;
  E[Network Operation data] --> |Goes to| A;
  F[Market data] --> |Goes to| A;
  A ---> |Needed in order to| G[Build Model];
  G --> |And then| H{Solve the case};
```