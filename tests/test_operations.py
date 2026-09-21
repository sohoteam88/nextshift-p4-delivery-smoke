import unittest
from src.operations import add

class OperationsTests(unittest.TestCase):
    def test_add(self):
        for a, b, expected in [(2, 3, 5), (-2, 3, 1), (0, 0, 0), (1.5, 2.5, 4)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)
