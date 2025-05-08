import unittest
from kilo_to_pounds_converter import kg_to_pounds

class TestKgToPoundsConverter(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(kg_to_pounds(0), 0)
        self.assertAlmostEqual(kg_to_pounds(1), 2.20462, places=5)
        self.assertAlmostEqual(kg_to_pounds(5), 11.0231, places=4)

    def test_large_values(self):
        self.assertAlmostEqual(kg_to_pounds(1000), 2204.62, places=2)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            kg_to_pounds(-5)

    def test_edge_case(self):
        self.assertAlmostEqual(kg_to_pounds(0.001), 0.00220462, places=8)

# Run the tests
if __name__ == '__main__':
    unittest.main()
