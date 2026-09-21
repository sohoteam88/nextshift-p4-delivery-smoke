import unittest
from src.operations import add, multiply

class OperationsTests(unittest.TestCase):
    def test_add(self):
        for a, b, expected in [(2, 3, 5), (-2, 3, 1), (0, 0, 0), (1.5, 2.5, 4)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_multiply(self):
        cases = [
            (2, 3, 6),
            (-2, 3, -6),
            (2, -3, -6),
            (-2, -3, 6),
            (0, 5, 0),
            (5, 0, 0),
            (0, 0, 0),
            (1.5, 2.5, 3.75),
            (-0.5, 0.25, -0.125),
            (0.1, 0.2, 0.02),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(multiply(a, b), expected)
