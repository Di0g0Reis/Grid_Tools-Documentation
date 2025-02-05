import json
from network_parameters import NetworkParameters
from node import Node
from load import Load
from branch import Branch
from generator import Generator
from capacitor_bank import CapacitorBank
from energy_storage import EnergyStorage
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

    def construct_sheet_names(self, season, scenario):
        sheet_names = _construct_sheet_names(season, scenario)
        return sheet_names

    def load_case(self, excel_file, sheet_names):
        data = _load_case(self, excel_file, sheet_names)
        return data

    def read_market_data(self, market_data_file, sheet_names, scenario):
        _read_market_data(self, market_data_file, sheet_names, scenario)


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

def _construct_sheet_names(season, scenario):
    """
    Construct the sheet names based on the season and scenario.
    """
    prefix = {
        'Winter': 'Winter',
        'Spring': 'Spring',
        'Summer': 'Summer',
        'Fall': 'Fall'
    }
    return {
        'Pc': f'Pc, {prefix[season]}, S{scenario}',
        'Qc': f'Qc, {prefix[season]}, S{scenario}',
        'Pg': f'Pg, {prefix[season]}, S{scenario}',
        'Qg': f'Qg, {prefix[season]}, S{scenario}',
        'UpFlex': f'UpFlex, {prefix[season]}',
        'DownFlex': f'DownFlex, {prefix[season]}',
        'GenStatus': f'GenStatus, {prefix[season]}',
        'Cp': f'Cp, {prefix[season]}',
        'Flex': f'Flex, {prefix[season]}'

    }

def _load_case(network, excel_file, sheet_names):

    network.operational_data_file = excel_file

    data = {
        'consumption': {
            'pc': dict(), 'qc': dict()
        },
        'flexibility': {
            'upward': dict(),
            'downward': dict()
        },
        'generation': {
            'pg': dict(), 'qg': dict(), 'status': list()
        }
    }

    # Scenario information
    num_gen_cons_scenarios, prob_gen_cons_scenarios = _get_operational_scenario_info_from_excel_file(excel_file, 'Main')
    network.prob_operation_scenarios = prob_gen_cons_scenarios

    # Consumption and Generation data -- by scenario
    for i in range(len(network.prob_operation_scenarios)):

        # Consumption per scenario (active, reactive power)
        pc_scenario = _get_consumption_flexibility_data_from_excel_file(excel_file, sheet_names["Pc"])
        qc_scenario = _get_consumption_flexibility_data_from_excel_file(excel_file, sheet_names["Qc"])
        if not pc_scenario:
            print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No active power consumption data provided for scenario {i + 1}. Exiting...')
        if not qc_scenario:
            print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No reactive power consumption data provided for scenario {i + 1}. Exiting...')
        data['consumption']['pc'][i] = pc_scenario
        data['consumption']['qc'][i] = qc_scenario

        # Generation per scenario (active, reactive power)
        num_renewable_gens = network.get_num_renewable_gens()
        if num_renewable_gens > 0:
            pg_scenario = _get_generation_data_from_excel_file(excel_file, sheet_names["Pg"])
            qg_scenario = _get_generation_data_from_excel_file(excel_file, sheet_names["Qg"])
            if not pg_scenario:
                print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No active power generation data provided for scenario {i + 1}. Exiting...')
            if not qg_scenario:
                print(f'[ERROR] Network {network.name}, {network.year}, {network.day}. No reactive power generation data provided for scenario {i + 1}. Exiting...')
            data['generation']['pg'][i] = pg_scenario
            data['generation']['qg'][i] = qg_scenario

    # Generators status. Note: common to all scenarios
    data['generation']['status'] = _get_generator_status_from_excel_file(excel_file, sheet_names["GenStatus"])

    # Flexibility data
    flex_up_p = _get_consumption_flexibility_data_from_excel_file(excel_file, sheet_names["UpFlex"])
    if not flex_up_p:
        for load in network.loads:
            flex_up_p[load.load_id] = [0.0 for _ in range(network.num_instants)]
    data['flexibility']['upward'] = flex_up_p

    flex_down_p = _get_consumption_flexibility_data_from_excel_file(excel_file, sheet_names["DownFlex"])
    if not flex_down_p:
        for load in network.loads:
            flex_down_p[load.load_id] = [0.0 for _ in range(network.num_instants)]
    data['flexibility']['downward'] = flex_down_p

    return data

def _get_operational_scenario_info_from_excel_file(filename, sheet_name):

    num_scenarios = 0
    prob_scenarios = list()

    try:
        df = pd.read_excel(filename, sheet_name=sheet_name, header=None)
        if is_int(df.iloc[0, 1]):
            num_scenarios = int(df.iloc[0, 1])
        for i in range(num_scenarios):
            if is_number(df.iloc[0, i+2]):
                prob_scenarios.append(float(df.iloc[0, i+2]))
    except:
        print('[ERROR] Workbook {}. Sheet {} does not exist.'.format(filename, sheet_name))
        exit(1)

    if num_scenarios != len(prob_scenarios):
        print('[WARNING] Workbook {}. Data file. Number of scenarios different from the probability vector!'.format(filename))

    if round(sum(prob_scenarios), 2) != 1.00:
        print('[ERROR] Workbook {}. Probability of scenarios does not add up to 100%.'.format(filename))

    return num_scenarios, prob_scenarios

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

def _read_market_data(network, file_path, sheet_names, scenario):
    # Initialize variables to hold market data separately
    Cp, Flex, prob_market_scenarios = None, None, None

    # Read the specified sheet for the given season
    try:
        # Load the entire Cp sheet and select the specific row for the scenario
        Cp_data = pd.read_excel(file_path, sheet_name=sheet_names['Cp'])
        Cp = Cp_data.iloc[scenario - 1]  # Adjusting for zero-based index
        network.cost_energy_p.append(Cp)
        print(f"Successfully read Cp data from {sheet_names['Cp']} for scenario {scenario}")

        # Load the entire Flex sheet and select the specific row for the scenario
        Flex_data = pd.read_excel(file_path, sheet_name=sheet_names['Flex'])
        Flex = Flex_data.iloc[scenario - 1]  # Adjusting for zero-based index
        network.cost_flex.append(Flex)
        print(f"Successfully read Flex data from {sheet_names['Flex']} for scenario {scenario}")

        # Load the Probability of market (price) scenarios
        prob_data = pd.read_excel(file_path, sheet_name='Scenarios', header=None)
        prob_market_scenarios = prob_data.iloc[0, 2:].tolist()
        network.prob_market_scenarios.append(prob_market_scenarios)
        print(f"Successfully read Prob. data")

    except Exception as e:
        print(f"Error reading {sheet_names['Cp']} or , {sheet_names['Flex']}, or Prob: {e}")

    return network.cost_energy_p, network.cost_flex, network.prob_market_scenarios
