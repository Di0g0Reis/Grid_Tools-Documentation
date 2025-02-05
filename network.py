import json
from network_parameters import NetworkParameters
from node import Node
from load import Load
from branch import Branch
from generator import Generator
from capacitor_bank import CapacitorBank
from energy_storage import EnergyStorage

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

    def load_topology(self, filename):
        _load_topology(self, filename)


def _load_topology(network, filename):

    # Load JSON data
    with open(filename, 'r') as f:
        data = json.load(f)
    network.num_instants = 24 #Assumir 24?

    # Read baseMVA from JSON
    network.baseMVA = float(data.get('baseMVA', 100)) # Default to 100 if not provided

    # Read Node data
    for bus in data['nodes']:
        node = Node()
        node.bus_i = int(bus['bus_i'])
        node.type = int(bus['type'])
        node.gs = int(bus['Gs'])
        node.bs = int(bus['Bs'])
        node.base_kv = float(bus['baseKV'])
        node.v_max = float(bus['Vmax'])
        node.v_min = float(bus['Vmin'])
        network.nodes.append(node)

    # Read Load data
    for load in data['loads']:
        load_instance = Load()
        load_instance.load_id = int(load['load_id'])
        load_instance.bus = int(load['bus'])
        load_instance.status = bool(load['status'])
        load_instance.fl_reg = bool(load['fl_reg'])
        if load_instance.fl_reg:
            load_instance.flexibility.upward = [0] * network.num_instants
            load_instance.flexibility.downward = [0] * network.num_instants
        else:
            load_instance.flexibility.upward = [0] * network.num_instants
            load_instance.flexibility.downward = [0] * network.num_instants
        network.loads.append(load_instance)

    # Read Line data
    for branch in data['lines']:
        branch_instance = Branch()
        branch_instance.branch_id = int(branch['branch_id'])
        if int(branch['fbus'])!=0:
            branch_instance.fbus = int(branch['fbus'])
        if int(branch['tbus']) != 0:
            branch_instance.tbus = int(branch['tbus'])
        branch_instance.r = float(branch['r'])
        branch_instance.x = float(branch['x'])
        branch_instance.b_sh = float(branch['b'])
        branch_instance.rate = float(branch['rating'])
        branch_instance.status = bool(branch['status'])
        branch_instance.is_transformer = False
        network.branches.append(branch_instance)

    for branch in data['transformers']:
        branch_instance = Branch()
        branch_instance.branch_id = int(branch['branch_id'])
        if int(branch['fbus'])!=0:
            branch_instance.fbus = int(branch['fbus'])
        if int(branch['tbus']) != 0:
            branch_instance.tbus = int(branch['tbus'])
        branch_instance.r = float(branch['r'])
        branch_instance.x = float(branch['x'])
        branch_instance.b_sh = float(branch['b'])
        branch_instance.rate = float(branch['rating'])
        branch_instance.status = bool(branch['status'])
        branch_instance.is_transformer = True
        branch_instance.ratio = float(branch['ratio'])
        branch_instance.vmag_reg = float(branch['vmag_reg'])
        network.branches.append(branch_instance)

    # Read Generators data
    for gen in data['generators']:
        generator = Generator()
        generator.gen_id = int(gen['gen_id'])
        generator.bus = int(gen['bus'])
        generator.pmax = float(gen['Pmax'])
        generator.pmin = float(gen['Pmin'])
        generator.qmax = float(gen['Qmax'])
        generator.qmin = float(gen['Qmin'])
        generator.vg = float(gen['Vg'])
        generator.status = bool(gen['status'])
        generator.type = str(gen['type'])
        generator.pf_control = bool(gen["pf_control"]) #?Tive que adicionar pf_control=0 ao gerador que nao tinha?
        if generator.pf_control:
            generator.pf_max = float(gen["pf_max"])
            generator.pf_min = float(gen["pf_min"])
        network.generators.append(generator)

    # Read capacitor banks data
    if 'capacitor_banks' in data:
        for cap in data['capacitor_banks']:
            cap_instance = CapacitorBank()
            cap_instance.bank_id = int(cap['bank_id'])
            cap_instance.bus = int(cap['bus'])
            cap_instance.q = float(cap['q'])
            cap_instance.n_steps = int(cap['n_steps'])  # Read witch step
            cap_instance.n_init = int(cap['n_init'])  # Read initial tap position
            cap_instance.status = bool(cap['status'])
            network.capacitor_banks.append(cap_instance)

    # Read energy storage data
    if 'energy_storage' in data:
        for es in data['energy_storage']:
            es_instance = EnergyStorage()
            es_instance.es_id = int(es['es_id'])
            es_instance.bus = int(es['bus'])
            es_instance.s = float(es['s'])
            es_instance.e = float(es['e'])
            es_instance.e_init = float(es['e_init'])
            es_instance.e_min = float(es['e_min'])
            es_instance.e_max = float(es['e_max'])
            es_instance.eff_ch = float(es['eff_ch'])
            es_instance.eff_dch = float(es['eff_dch'])
            es_instance.max_pf = float(es['max_pf'])
            es_instance.min_pf = float(es['min_pf'])
            network.energy_storages.append(es_instance)

    return network