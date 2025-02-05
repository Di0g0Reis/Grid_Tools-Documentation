import os
from network import Network



if __name__ == "__main__":

    case_study = os.path.join('data', 'CS1')
    network_filename = os.path.join(case_study, "case33.json")
    network_excel_file = os.path.join(case_study, "case33.xlsx")
    market_data_file = os.path.join(case_study, "CS7_market_data.xlsx")

    season = "Summer"  # Change this as needed
    scenario = 2  # Change this as needed

    network = Network()
    network.load_topology(network_filename)
    sheet_names = network.construct_sheet_names(season, scenario)
    network.load_case(network_excel_file, sheet_names)
    network.read_market_data(market_data_file, sheet_names, scenario)
    print()