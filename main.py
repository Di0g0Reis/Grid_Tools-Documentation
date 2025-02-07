import os
from network import Network



if __name__ == "__main__":

    case_study = os.path.join('data', 'CS1')
    network_filename = os.path.join(case_study, "case33.json")
    network_excel_file = os.path.join(case_study, "case33.xlsx")
    market_data_file = os.path.join(case_study, "CS7_market_data.xlsx")

    network = Network()
    network.load_topology(network_filename)
    network.load_case(network_excel_file)
    network.read_market_data(market_data_file)
    print()