import unittest

# Code to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Unit test class
class TestMathOperations(unittest.TestCase):
    
    # Test for add function
    def test_add(self):
        self.assertEqual(add(2, 3), 5)       # Positive numbers
        self.assertEqual(add(-2, -3), -5)   # Negative numbers
        self.assertEqual(add(2, -3), -1)    # Mixed numbers
    
    # Test for subtract function
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)     # Positive numbers
        self.assertEqual(subtract(-5, -3), -2) # Negative numbers
        self.assertEqual(subtract(5, -3), 8)   # Mixed numbers

# Run the tests
if __name__ == '__main__':
    unittest.main()
