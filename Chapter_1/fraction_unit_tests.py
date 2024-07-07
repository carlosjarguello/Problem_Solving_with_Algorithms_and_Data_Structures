import unittest
from fractions import * 

class TestFraction(unittest.TestCase):

    def setUp(self):
        self.frac1 = Fraction(1, 2)
        self.frac2 = Fraction(1, 3)
        self.frac3 = Fraction(2, 4)

    def test_str(self):
        self.assertEqual(str(self.frac1), "1/2")
        self.assertEqual(str(self.frac2), "1/3")

    def test_add(self):
        result = self.frac1 + self.frac2
        self.assertEqual(result, Fraction(5, 6))
        result = self.frac1 + self.frac3
        self.assertEqual(result, Fraction(1, 1))

    def test_eq(self):
        self.assertTrue(self.frac1 == Fraction(1, 2))
        self.assertTrue(self.frac3 == Fraction(1, 2))
        self.assertFalse(self.frac1 == self.frac2)

    def test_truediv(self):
        result = self.frac1 / self.frac2
        self.assertEqual(result, Fraction(3, 2))
        result = self.frac2 / self.frac1
        self.assertEqual(result, Fraction(2, 3))

    def test_sub(self):
        result = self.frac1 - self.frac2
        self.assertEqual(result, Fraction(1, 6))
        result = self.frac2 - self.frac1
        self.assertEqual(result, Fraction(-1, 6))

    def test_lt(self):
        self.assertTrue(self.frac2 < self.frac1)
        self.assertFalse(self.frac1 < self.frac2)
        self.assertFalse(self.frac1 < self.frac3)

if __name__ == '__main__':
    unittest.main()
