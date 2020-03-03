# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEquals(utils.fact(1), 1)
        self.assertEquals(utils.fact(0),1)
        self.assertEquals(utils.fact(4), 24)
        with self.assertRaises(ValueError):
            utils.fact(-1)
    
    def test_roots(self):
        # À compléter...
        self.assertEquals(utils.roots(-1,0,1),(-1,1))
        self.assertEquals(utils.roots(1,-4,4),(2))
        self.assertEquals(utils.roots(1,0,0),0)
    
    def test_integrate(self):
        # À compléter...
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
