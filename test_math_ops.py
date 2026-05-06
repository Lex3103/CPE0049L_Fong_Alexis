import unittest
from math_ops import add, multiply

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 0), 0)

# This should be outside the class
if __name__ == '__main__':
    unittest.main()