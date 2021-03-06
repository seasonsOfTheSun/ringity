from ringity.exceptions import DisconnectedGraphError

import os
import sys
import ringity
import unittest
import networkx as nx

RINGITY_PATH = os.path.dirname(ringity.__file__)

class TestDiagramFunction(unittest.TestCase):
    def test_lipid_network(self):
        G = nx.read_edgelist(f"{RINGITY_PATH}/test_data/lipid_coexp_network.txt")
        dgm1 = ringity.core.diagram(G)
        dgm2 = ringity.classes.load_dgm(f"{RINGITY_PATH}/test_data/lipid_coexp_dgm.txt")
        for (pt1,pt2) in zip(dgm1, dgm2):
            self.assertAlmostEqual(pt1.birth,pt2.birth, places=5)
            self.assertAlmostEqual(pt1.death,pt2.death, places=5)

    def test_pathological_cases(self):
        pass

    def test_distance_matrix_flag_use_weight_compability(self):
        pass

    def test_distance_matrix_flag_vs_use_weight_with_zero_entries(self):
        pass

    def test_disconnection_error(self):
        G = nx.erdos_renyi_graph(10,0.5)
        G.add_node(11)
        self.assertRaises(DisconnectedGraphError, ringity.centralities.net_flow,G)

if __name__ == '__main__':
    unittest.main()
