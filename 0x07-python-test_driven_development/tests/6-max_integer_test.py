#!/usr/bin/python3
"""Defines the TestMaxInteger class.
TestMaxInteger - Unittest for the max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Performs Unittests for the ``max_integer`` function"""

    def test_integer(self):
        """Tests for integer inputs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 2, 3, float("NaN")]), 3)
        self.assertEqual(max_integer([1, 2, 3, float("inf")]), float("inf"))
        self.assertEqual(max_integer([1, 2, 3, float("-inf")]), 3)

    def test_string(self):
        """Tests for string inputs"""
        with self.assertRaises(TypeError):
            max_integer([1, "Leuel"])
        self.assertEqual(max_integer(["Leuel"]), "Leuel")


if __name__ == '__main__':
    unittest.main()
