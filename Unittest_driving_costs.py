import unittest
from Driving_costs import driving_cost

class TestDrivingCost(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(driving_cost(10, 20.0, 3.1599), 1.58)
        self.assertAlmostEqual(driving_cost(50, 20.0, 3.1599), 7.90)
        self.assertAlmostEqual(driving_cost(400, 20.0, 3.1599), 63.20)
        
    def test_large_values(self):
        self.assertAlmostEqual(driving_cost(10000, 10, 1000), 1000000)
        
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            driving_cost(-5, -5, -5)
            
    def test_edge_case(self):
        self.assertAlmostEqual(driving_cost(0.001, 0.001, 0.001), 0.00)

if __name__ == "__main__":
    unittest.main()