# package_tests/sum_test.py

import unittest
import sys
sys.path.append('C:/Users/pc_su/Desktop/Polytech Paris-Saclay/APP4/Qualité Logicielle/bowling_project/Bowling_score_manager_ultimate')

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2, 2), 4)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
