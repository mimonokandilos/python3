# test_module8.py

import unittest
from list_operations import find_max, find_min, average

class TestListOperations(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([3, 5, 1, 8, 2]), 8)
        self.assertEqual(find_max([10, 20, 30]), 30)
        self.assertEqual(find_max([-1, -5, -3]), -1)

        # Test an empty list
        with self.assertRaises(ValueError):
            find_max([])

    def test_find_min(self):
        self.assertEqual(find_min([3, 5, 1, 8, 2]), 1)
        self.assertEqual(find_min([10, 20, 30]), 10)
        self.assertEqual(find_min([-1, -5, -3]), -5)

        # Test an empty list
        with self.assertRaises(ValueError):
            find_min([])

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average([10, 20, 30, 40, 50]), 30.0)
        self.assertEqual(average([-1, -2, -3, -4, -5]), -3.0)

        # Test an empty list
        with self.assertRaises(ValueError):
            average([])

if __name__ == "__main__":
    unittest.main()

