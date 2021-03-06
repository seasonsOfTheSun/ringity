import os
import ringity
import unittest

RINGITY_PATH = os.path.dirname(ringity.__file__)

class TestSaveAndLoad(unittest.TestCase):
    def test_save_and_load(self):
        dgm1 = ringity.classes.random_Dgm(length=100)
        dgm1.save(f"{RINGITY_PATH}/tmp/random_dgm.txt")
        dgm2 = ringity.classes.load_dgm(f"{RINGITY_PATH}/tmp/random_dgm.txt")
        self.assertEqual(dgm1,dgm2)
        os.remove(f"{RINGITY_PATH}/tmp/random_dgm.txt")

if __name__ == '__main__':
    unittest.main()
