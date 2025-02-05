from network_parameters import NetworkParameters

class Network:

    def __init__(self):
        self.name = str()
        self.data_dir = str()   #n preciso?
        self.results_dir = str()
        self.diagrams_dir = str()
        self.num_instants = 0
        self.operational_data_file = str()
        self.baseMVA = 100.0
        self.nodes = list()
        self.loads = list()
        self.branches = list()
        self.generators = list()
        self.energy_storages = list()
        self.capacitor_banks = list()   #novo
        self.transformer = list()   #novo
        self.prob_market_scenarios = list()             # Probability of market (price) scenarios
        self.prob_operation_scenarios = list()          # Probability of operation (generation and consumption) scenarios
        self.cost_energy_p = list()
        self.cost_flex = list()
        self.params = NetworkParameters()