import unittest
from square import square 

class SquareTest(unittest.TestCase):

    def test_square_positive(self):
        self.assertEqual(square(3), 9, "Square of 3 should be 9")

    def test_square_negative(self):
        self.assertEqual(square(-4), 16, "Square of -4 should be 16")

    def test_square_zero(self):
        self.assertEqual(square(0), 0, "Square of 0 should be 0")

if __name__ == '__main__':
    unittest.main()
