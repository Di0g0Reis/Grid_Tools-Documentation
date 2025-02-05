import os
from network import Network



if __name__ == "__main__":

    case_study = os.path.join('data', 'CS1')
    network_filename = os.path.join(case_study, "case33.json")

    network = Network()
    network.load_topology(network_filename)
    print()