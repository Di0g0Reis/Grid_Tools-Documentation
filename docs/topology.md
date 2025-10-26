This file defines the **network topology** of the electrical grid for a specific case. It describes how the various elements such as buses, generators, loads, lines, and transformers are connected. The data is organized in a structured `.json` format, with tables corresponding to each type of element.
Each table has columns representing the parameters and rows corresponding to individual elements.

The system network is defined by a `.json` file named after the case, for example, `case9.json`.


This is exemplified here:
````json title="caseX.json"
{
    "baseMVA": 100.0,
    "nodes": [
        {"bus_i": 1, "type": 3, "Gs": 0.0, "Bs": 0.0, "baseKV": 135.0, "Vmax": 1.05, "Vmin": 0.95},
        ...
    ],
    "generators": [
        {"gen_id":1,"bus":1,"Pmax":80,"Pmin":0,"Qmax":150,"Qmin":-20,"Vg":1,"status":1, "type": "CONV", "ramp_rate":0.05},
        ...
    ],
    "loads": [
        {"load_id": 1, "bus": 2, "status": 1, "fl_reg": 1},
        ...
    ],
    "lines": [
        {"branch_id": 1, "fbus": 1, "tbus": 2, "r": 0.02, "x": 0.06, "b": 0.03, "rating": 130.0, "status": 1},
        ...
    ],
    "transformers": [
        {"branch_id": 3, "fbus": 37, "tbus": 22, "r": 6e-05, "x": 0.00046, "b": 0.0, "rating": 2500.0, "ratio": 1.0082, "status": 1, "vmag_reg": 1},
        ...
    ],
  	"energy_storage": [
		{"es_id": 1, "bus": 1, "s": 10, "e": 20, "e_init": 10, "e_min": 1, "e_max": 19, "eff_ch": 0.9, "eff_dch": 0.9, "max_pf": 0.9, "min_pf": -0.9},
        ...
    ]
}
````

In short, you will need to provide the following parameters:
#### **Buses (Nodes)**:

|  Parameter  |  Data Type  | Explanation                                       |
|:-----------:|:-----------:|:--------------------------------------------------|
|    bus_i    |   integer   | Bus number (positive integer)                     |
|    type     |   integer   | Bus type: PQ - 1; PV - 2; REF - 3; Isolated - 4   |
|     Gs      |    float    | Shunt conductance (MW demanded at V = 1.0 p.u.)   |
|     Bs      |    float    | Shunt susceptance (MVAr injected at V = 1.0 p.u.) |
|   baseKV    |    float    | Base voltage (kV)                                 |
|    Vmax     |    float    | Maximum voltage magnitude (p.u.)                  |
|    Vmin     |    float    | Minimum voltage magnitude (p.u.)                  |


#### **Generators**:

| Parameter | Data Type | Explanation                                                |
|:---------:|:---------:|:-----------------------------------------------------------|
|  gen_id   |  integer  | Generator ID                                               |
|    bus    |  integer  | Bus number that the generator is connected                 |
|   Pmax    |   float   | Maximum real power output (MW)                             |
|   Pmin    |   float   | Minimum real power output (MW)                             |
|   Qmax    |   float   | Maximum reactive power output (MVAr)                       |
|   Qmin    |   float   | Minimum reactive power output (MVAr)                       |
|    Vg     |   float   | Voltage magnitude setpoint (p.u.)                          |
|  status   |  integer  | Status: 1 - Machine in service; 0 - Machine out of service |
|   type    |  string   | Type of generator: Conv, Wind, Solar, etc                  |
| ramp_rate |   float   | Physical Ramp rate (P/min)                                 |

!!! info 
    Based on our investigation, we obtained ramp rate values corresponding to each generator type.
    
    | Generator - Fuel Type | Ramp rate (% P/min) | 
    |:---------:|:---------:|
    |  Coal  |  1 - 4  | 
    |    Coal - **SOTA**    |  < 6  | 
    |  Hydro   |  10 - 30  |
    |  **Open Cycle** gas turbines   |  8 - 12  |
    |  **Open Cycle** gas turbines - **SOTA**  |  < 15  | 
    |  **Combined Cycle** gas turbines   |  2 - 4  |
    |  **Combined Cycle** gas turbines - **SOTA**  |  8 - 10  |
    |  Thermal (Poland)   |  2 - 6  |
    |  Thermal (Denmark)   |  4  |
    |  Thermal (Germany)   |  < 6  |
    |  Nuclear   |  100  |
    
    With **SOTA** being State of the art.


####  **Loads**:

| Parameter | Data Type | Explanation                                                    |
|:---------:|:---------:|:---------------------------------------------------------------|
|  load_id  |  integer  | Load number (positive integer)                                 |
|    bus    |  integer  | Bus number that the load is connected                          |
|  status   |  integer  | Status: 1 - Load Online; 0 - Load Offline                      |
|  fl_reg   |  integer  | Indicates if the load is flexible, 1 - If it is, 0 - Otherwise |


#### **Lines**:

| Parameter | Data Type | Explanation                                          |
|:---------:|:---------:|:-----------------------------------------------------|
| branch_id |  integer  | Line ID                                              |
|   fbus    |  integer  | From bus number                                      |
|   tbus    |  integer  | To bus number                                        |
|     r     |   float   | Resistance (p.u.)                                    |
|     x     |   float   | Reactance (p.u.)                                     |
|     b     |   float   | Total line charging susceptance (p.u.)               |
|  rating   |   float   | Rating A (MVA, long term rating)                     |
|  status   |  integer  | Status: 1 - Line in service; 0 - Line out of service |

!!! info

    The **ramp rate** which defines how much the capacity limits of branches increase under contingency conditions is set to **15% for lines** and **20% for transformers**. These values are configured in the ``branch.py`` file.

!!! note 

    **Transformers** are treated as branches in the system, with a few additional parameters. This is why their element table closely resembles the one used for **Lines**.

#### **Transformers**:

| Parameter | Data Type | Explanation                                                                                                                              |
|:---------:|:---------:|:-----------------------------------------------------------------------------------------------------------------------------------------|
| branch_id |  integer  | Line ID                                                                                                                                  |
|   fbus    |  integer  | From bus number                                                                                                                          |
|   tbus    |  integer  | To bus number                                                                                                                            |
|     r     |   float   | Resistance (p.u.)                                                                                                                        |
|     x     |   float   | Reactance (p.u.)                                                                                                                         |
|     b     |   float   | Total line charging susceptance (p.u.)                                                                                                   |
|  rating   |   float   | Rating A (MVA, long term rating)                                                                                                         |
|   ratio   |   float   | Transformer off nominal turns ratio ( = 0 for lines; taps at 'from' bus, impedance at 'to' bus, i.e. if r = x = 0, then ratio = Vf / Vt) |
|  status   |  integer  | Status: 1 - Line in service; 0 - Line out of service                                                                                     |
| vmag_reg  |  integer  | Indicates if transformer has voltage magnitude regulation (1 - If it does)                                                               |


#### **Energy Storage Systems**:

| Parameter | Data Type | Explanation                                                                                                      |
|:---------:|:---------:|:-----------------------------------------------------------------------------------------------------------------|
|   es_id   |  integer  | Energy storage identifier                                                                                        |
|    bus    |  integer  | The bus (node) number in the power network to which the storage unit is connected                                |
|     s     |   float   | Apparent power rating (MVA)                                                                                      |
|     e     |   float   | Total energy capacity of the storage device (MWh)                                                                |
|  e_init   |   float   | Initial energy stored at the beginning of the simulation (MWh)                                                   |
|   e_min   |   float   | Minimum allowable energy (MWh)                                                                                   |
|   e_max   |   float   | Maximum allowable energy, often 95% of e (MWh)                                                                   |
|  eff_ch   |   float   | Charging efficiency (0 to 1, fraction of input power converted to stored energy)                                 |
|  eff_dch  |   float   | Discharging efficiency (0 to 1, fraction of stored energy converted to output power)                             |
|  max_pf   |   float   | Maximum power factor (leading/lagging) allowed when operating — defines reactive power capability limit (0 to 1) |
|  min_pf   |   float   | Minimum power factor (0 to 1)                                                                                    |
