from solver_parameters import SolverParameters
from definitions import *


# ======================================================================================================================
#   Class NetworkParameters
# ======================================================================================================================
class NetworkParameters:

    def __init__(self):
        self.obj_type = OBJ_MIN_COST
        self.transf_reg = True
        self.es_reg = True
        self.fl_reg = True
        self.cb_reg = True
        self.rg_curt = False
        self.l_curt = False
        self.enforce_vg = False
        self.relax_equalities = False
        self.branch_limit_type = BRANCH_LIMIT_CURRENT
        self.slacks = Slacks()
        self.print_to_screen = False
        self.plot_diagram = False
        self.print_results_to_file = False
        self.solver_params = SolverParameters()


# ======================================================================================================================
#   Slack Classes
# ======================================================================================================================
class Slacks:

    def __init__(self):
        self.grid_operation = SlacksOperation()
        self.ess = SlacksEnergyStorage()

class SlacksOperation:

    def __init__(self):
        self.voltage = False
        self.branch_flow = False


class SlacksEnergyStorage:

    def __init__(self):
        self.complementarity = False
