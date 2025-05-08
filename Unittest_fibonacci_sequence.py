import unittest
from For_loop_fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [0])
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(12), 144)
        self.assertEqual(fibonacci(13), 233)
        self.assertEqual(fibonacci(14), 377)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(16), 987)
        self.assertEqual(fibonacci(17), 1597)
        self.assertEqual(fibonacci(18), 2584)
        self.assertEqual(fibonacci(19), 4181)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(21), 10946)
        self.assertEqual(fibonacci(22), 17711)
        self.assertEqual(fibonacci(23), 28657)
        self.assertEqual(fibonacci(24), 46368)
        self.assertEqual(fibonacci(25), 75025)
        self.assertEqual(fibonacci(26), 121393)
        self.assertEqual(fibonacci(27), 196418)
        self.assertEqual(fibonacci(28), 317811)
        self.assertEqual(fibonacci(29), 514229)
        self.assertEqual(fibonacci(30), 832040)

if __name__ == '__main__':
    unittest.main()        