import os

class SolverParameters:

    def __init__(self):
        self.solver = 'ipopt'
        self.linear_solver = 'ma57'
        self.nlp_solver = 'ipopt'
        self.solver_path = os.environ['IPOPTDIR']
        self.solver_tol = 1e-6
        self.verbose = False
