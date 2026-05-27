This file contains the **operational parameters** and **solver configurations** necessary to run a given optimization case. It allows you to control how the SC-OPF or MP-OPF behaves, including choices like optimization type, solver tolerances, objective formulations, and operational constraints.

In this section, you will find a complete description of each parameter, its purpose, accepted values, and how it influences the solver's execution.
It's defined by a `.json` file named after the case, for example, `case9_params.json`.


````json title="caseX_params.json"
{
	"obj_type": "COST",
	"transf_reg": true,
	"cb_reg": true,
	"reactor_reg": true,
	"es_reg": true,
	"fl_reg": true,
	"rg_curt": true,
	"l_curt": false,
	"enforce_vg": false,
	"enforce_discrete": false,
	"branch_limit_type": "APPARENT_POWER",
	"ess_model": "BILINEAR_RELAXATION",
	"slacks": {
		"grid_operation": {
			"voltage": true,
			"branch_flow": false
		},
		"flexibility": {
			"day_balance": false
		},
		"ess": {
			"day_balance": false
		},
		"node_balance": {
			"active_power": false,
			"reactive_power": false
		}
	},
	"solver": {
		"name": "ipopt",
		"verbose": false,
		"options": {
	  		"tol": 1e-5,
			"linear_solver": "ma97",
			"output_file": "optim_log.log",
			"file_print_level": 6
		}
	}
}
````


#### **Structure Breakdown**

|        Parameter        |    Data Type    | Explanation                                                                                                                                    |
|:-----------------------:|:---------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------|
|        obj_type         |     string      | Sets the objective function to: "COST" - minimize total operational cost or "CONGESTION_MANAGEMENT" - managing congestion in the power network |
|       transf_reg        |     boolean     | Enables/Disables tap-changing transformer regulation as part of the optimization                                                               |
|         cb_reg          |     boolean     | Enables/Disables tap-changing capacitor bank regulation as part of the optimization                                                            |
|       reactor_reg       |     boolean     | Enables/Disables tap-changing reactor regulation as part of the optimization                                                                   |
|         es_reg          |     boolean     | Enables/Disables energy storage regulation, i.e., storage devices won't be optimized actively                                                  |
|         fl_reg          |     boolean     | Enables/Disables flexible loads from participating in the optimization                                                                         |
|         rg_curt         |     boolean     | Allows (or not) renewable generation curtailment, giving the model flexibility to reduce excess renewables                                     |
|         l_curt          |     boolean     | Enables/Disables load curtailment (load shedding) all demand must be met                                                                       |
|       enforce_vg        |     boolean     | Enforces (or not) variable generation (e.g., solar/wind) to strictly follow forecast                                                           |
|    enforce_discrete     |     boolean     | Enforces (or not) variables to be discrete                                                                                                     |
|    branch_limit_type    |     string      | Line flow limits are enforced based on, CURRENT (A) (or CURRENT_SIMPLIFIED),  APPARENT_POWER (MVA) or MIXED                                    |
|        ess_model        |     string      | ESS model can vary from: EXACT, BILINEAR_RELAXATION or SIMPLIFIED                                                                              |
| [***slacks***](#slacks) |     boolean     | This section controls where soft constraints (i.e., constraint violations with penalties) are allowed                                          |
|         solver          | boolean/string  | Indicates the solvers settings                                                                                                                 |

!!! note 

    In the **Contingencies** parameter, the (N-1) criterion is applied, meaning each contingency is evaluated individually. As a result, a total of (C + 1) scenarios are created, where C represents the total number of contingencies (lines + generators) and, scenario 0 corresponds to the base case (a standard OPF without any contingencies).

Inside the ***slacks*** parameter resides the following:

#### **Slacks**

|        Parameter         | Data Type | Explanation                                                                                               |
|:------------------------:|:---------:|:----------------------------------------------------------------------------------------------------------|
|      grid_operation      |  boolean  | Enables/Disables Voltage limit violations and/or Branch flow limit violations                             |
|       flexibility        |  boolean  | Enables/Disables daily energy balancing for flexible resources                                            |
|           ess            |  boolean  | Enables/Disables and the relaxation of **daily energy balance** constraints in **energy storage systems** |
|       node_balance       |  boolean  | Enables/Disables softening nodal power balance constraints (helpful for feasibility testing)              |
