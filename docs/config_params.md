This file contains the **operational parameters** and **solver configurations** necessary to run a given optimization case. It allows you to control how the SC-OPF or MP-OPF behaves, including choices like optimization type, solver tolerances, objective formulations, and operational constraints.

In this section, you will find a complete description of each parameter, its purpose, accepted values, and how it influences the solver's execution.
It's defined by a `.json` file named after the case, for example, `case9_params.json`.


````json title="caseX_params.json"
{
	"obj_type": "COST",
	"transf_reg": false,
	"es_reg": false,
	"fl_reg": false,
	"rg_curt": true,
	"l_curt": false,
	"enforce_vg": false,
	"branch_limit_type": "APPARENT_POWER",

	"contingencies": {
		"lines": {
			"status": true,
			"branch_id": [8,6,5]
		},
		"generators": {
			"status": true,
			"gen_id": [2, 1, 3, 4]
		}
	},

	"slacks": {
		"grid_operation": {
			"voltage": true,
			"branch_flow": true
		},
		"flexibility": {
			"day_balance": false
		},
		"ess": {
			"complementarity": true,
			"charging": false,
			"day_balance": false
		},
		"shared_ess": {
			"complementarity": true,
			"charging": false,
			"day_balance": false
		},
		"node_balance": false
	},
	"solver": {
		"name": "ipopt",
		"solver_tol": 1e-5,
		"verbose": true
	},
	"print_to_screen": false,
	"plot_diagram": false,
	"print_results_to_file": false
}
````


#### **Structure Breakdown**:

|        Parameter        |    Data Type    | Explanation                                                                                                                                    |
|:-----------------------:|:---------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------|
|        obj_type         |     string      | Sets the objective function to: "COST" - minimize total operational cost or "CONGESTION_MANAGEMENT" - managing congestion in the power network |
|       transf_reg        |     boolean     | Enables/Disables tap-changing transformer regulation as part of the optimization                                                               |
|         es_reg          |     boolean     | Enables/Disables energy storage regulation, i.e., storage devices won't be optimized actively                                                  |
|         fl_reg          |     boolean     | Enables/Disables flexible loads from participating in the optimization                                                                         |
|         rg_curt         |     boolean     | Allows (or not) renewable generation curtailment, giving the model flexibility to reduce excess renewables                                     |
|         l_curt          |     boolean     | Enables/Disables load curtailment (load shedding) all demand must be met                                                                       |
|       enforce_vg        |     boolean     | Enforces (or not) variable generation (e.g., solar/wind) to strictly follow forecast                                                           |
|    branch_limit_type    |     string      | Line flow limits are enforced based on, current (A),  apparent power (MVA) or Mixed                                                            |
|      contingencies      | boolean/integer | This section defines contingency events/scenarios where elements (like lines or generators) fail                                               |
| [***slacks***](#slacks) |     boolean     | This section controls where soft constraints (i.e., constraint violations with penalties) are allowed                                          |
|         solver          | boolean/string  | Indicates the solvers settings                                                                                                                 |
|     print_to_screen     |     boolean     | Enables/Disables output display in the console                                                                                                 |
|      plot_diagram       |     boolean     | Enables/Disables graphical plotting of the power system                                                                                        |
|  print_results_to_file  |     boolean     | Enables/Disables saving results to external files                                                                                              |

!!! note 

    In the **Contingencies** parameter, the (N-1) criterion is applied, meaning each contingency is evaluated individually. As a result, a total of (C + 1) scenarios are created, where C represents the total number of contingencies (lines + generators) and, scenario 0 corresponds to the base case (a standard OPF without any contingencies).

Inside the ***slacks*** parameter resides the following:

#### **Slacks**:

|   Parameter    | Data Type | Explanation                                                                                                                                                                                                                                                                        |
|:--------------:|:---------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| grid_operation |  boolean  | Enables/Disables Voltage limit violations and/or Branch flow limit violations                                                                                                                                                                                                      |
|  flexibility   |  boolean  | Enables/Disables daily energy balancing for flexible resources                                                                                                                                                                                                                     |
|      ess       |  boolean  | Enables/Disables the relaxation of **complementarity** constraints, which softens the strict "charge OR discharge" rule; the relaxation of constraints related to **charging** limits; and/or the relaxation of **daily energy balance** constraints in **energy storage systems** |
|   shared_ess   |  boolean  | Same logic as above, but for **shared energy storage systems**                                                                                                                                                                                                                     |
|  node_balance  |  boolean  | Enables/Disables softening nodal power balance constraints, helpful for feasibility testing                                                                                                                                                                                        |
