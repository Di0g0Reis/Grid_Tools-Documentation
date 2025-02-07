import json
from node import Node
from load import Load
from branch import Branch
from generator import Generator
from capacitor_bank import CapacitorBank
from energy_storage import EnergyStorage
from network_parameters import NetworkParameters
import pandas as pd
from helper_functions import *



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

    def read_operational_data(self, excel_file):
        data = _read_operational_data(self, excel_file)
        return data

    def read_market_data(self, market_data_file):
        _read_market_data(self, market_data_file)


#=======================================================
#           Read JSON data, Topology
#=======================================================
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


#=======================================================
#           Read Excel data, Scenarios
#=======================================================
def _read_operational_data(network, filename):

    # Scenario information
    network.prob_operation_scenarios = _get_scenario_probability_from_file(filename)

    # Consumption and Generation data -- by scenario
    for i in range(len(network.prob_operation_scenarios)):

        sheet_name_pc = f'Pc, S{i + 1}'
        sheet_name_qc = f'Qc, S{i + 1}'
        sheet_name_pg = f'Pg, S{i + 1}'
        sheet_name_qg = f'Qg, S{i + 1}'

        # Consumption per scenario (active, reactive power)
        pc_scenario = _get_consumption_flexibility_data_from_excel_file(filename, sheet_name_pc)
        qc_scenario = _get_consumption_flexibility_data_from_excel_file(filename, sheet_name_qc)
        if not pc_scenario:
            print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No active power consumption data provided for scenario {i + 1}. Exiting...')
        if not qc_scenario:
            print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No reactive power consumption data provided for scenario {i + 1}. Exiting...')
        data['consumption']['pc'][i] = pc_scenario
        data['consumption']['qc'][i] = qc_scenario

        # Generation per scenario (active, reactive power)
        num_renewable_gens = network.get_num_renewable_gens()
        if num_renewable_gens > 0:
            pg_scenario = _get_generation_data_from_excel_file(excel_file, sheet_name_pg)
            qg_scenario = _get_generation_data_from_excel_file(excel_file, sheet_name_qg)
            if not pg_scenario:
                print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No active power generation data provided for scenario {i + 1}. Exiting...')
            if not qg_scenario:
                print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No reactive power generation data provided for scenario {i + 1}. Exiting...')
            data['generation']['pg'][i] = pg_scenario
            data['generation']['qg'][i] = qg_scenario

    # Generators status. Note: common to all scenarios
    data['generation']['status'] = _get_generator_status_from_excel_file(excel_file, f'GenStatus, {network.day}')

    # Flexibility data
    flex_up_p = _get_consumption_flexibility_data_from_excel_file(excel_file, f'UpFlex, {network.day}')
    if not flex_up_p:
        for load in network.loads:
            flex_up_p[load.load_id] = [0.0 for _ in range(network.num_instants)]
    data['flexibility']['upward'] = flex_up_p

    flex_down_p = _get_consumption_flexibility_data_from_excel_file(excel_file, f'DownFlex, {network.day}')
    if not flex_down_p:
        for load in network.loads:
            flex_down_p[load.load_id] = [0.0 for _ in range(network.num_instants)]
    data['flexibility']['downward'] = flex_down_p

    return data


def _get_consumption_flexibility_data_from_excel_file(filename, sheet_name):

    try:
        data = pd.read_excel(filename, sheet_name=sheet_name)
        num_rows, num_cols = data.shape
        processed_data = dict()
        for i in range(num_rows):
            node_id = data.iloc[i, 0]
            processed_data[node_id] = [0.0 for _ in range(num_cols - 1)]
        for node_id in processed_data:
            node_values = [0.0 for _ in range(num_cols - 1)]
            for i in range(0, num_rows):
                aux_node_id = data.iloc[i, 0]
                if aux_node_id == node_id:
                    for j in range(0, num_cols - 1):
                        node_values[j] += data.iloc[i, j + 1]
            processed_data[node_id] = node_values
    except:
        print(f'[WARNING] Workbook {filename}. Sheet {sheet_name} does not exist.')
        processed_data = {}

    return processed_data

def _get_generation_data_from_excel_file(filename, sheet_name):

    try:
        data = pd.read_excel(filename, sheet_name=sheet_name)
        num_rows, num_cols = data.shape
        processed_data = dict()
        for i in range(num_rows):
            gen_id = data.iloc[i, 0]
            processed_data[gen_id] = [0.0 for _ in range(num_cols - 1)]
        for gen_id in processed_data:
            processed_data_gen = [0.0 for _ in range(num_cols - 1)]
            for i in range(0, num_rows):
                aux_node_id = data.iloc[i, 0]
                if aux_node_id == gen_id:
                    for j in range(0, num_cols - 1):
                        processed_data_gen[j] += data.iloc[i, j + 1]
            processed_data[gen_id] = processed_data_gen
    except:
        print(f'[WARNING] Workbook {filename}. Sheet {sheet_name} does not exist.')
        processed_data = {}

    return processed_data

def _get_generator_status_from_excel_file(filename, sheet_name):

    try:
        data = pd.read_excel(filename, sheet_name=sheet_name)
        num_rows, num_cols = data.shape
        status_values = dict()
        for i in range(num_rows):
            gen_id = data.iloc[i, 0]
            status_values[gen_id] = list()
            for j in range(0, num_cols - 1):
                status_values[gen_id].append(bool(data.iloc[i, j + 1]))
    except:
        print(f'[WARNING] Workbook {filename}. Sheet {sheet_name} does not exist.')
        status_values = list()

    return status_values


#=======================================================
#           Read Market data
#=======================================================

def _read_market_data(network, file_path):
    network.prob_market_scenarios = _get_scenario_probability_from_file(file_path)
    network.cost_energy_p = _get_cost_data_from_market_file(file_path, 'Cp', len(network.prob_market_scenarios), network.num_instants)
    network.cost_flex = _get_cost_data_from_market_file(file_path, 'Cflex', len(network.prob_market_scenarios), network.num_instants)


def _get_scenario_probability_from_file(file_path):

    try:
        excel_data = pd.read_excel(file_path, sheet_name='Scenarios', header=None)
    except Exception as e:
        print(f"Error reading cost data from Scenarios: {e}")

    return excel_data.iloc[0,2:].tolist()



def _get_cost_data_from_market_file(file_path, sheet_name, n_scenarios, n_instants):

    try:
        excel_data = pd.read_excel(file_path, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading cost data from {sheet_name}: {e}")

    cost_data = dict()
    for s in range(n_scenarios):
        # Load the entire Cp sheet and select the specific row for the scenario
        scn_id = excel_data.iloc[s, 0]
        cost_data[scn_id] = list()
        for n in range(n_instants):
            cost_data[scn_id].append(excel_data.iloc[s, n + 1])

    return cost_data