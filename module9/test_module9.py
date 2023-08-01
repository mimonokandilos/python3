# test_module9.py

import unittest
from module9_operations import calculate_square, calculate_cube

class TestModule9Operations(unittest.TestCase):
    def test_calculate_square(self):
        result1 = calculate_square(3)
        self.assertEqual(result1, 9)
        print(f"calculate_square(3) = {result1}")

        result2 = calculate_square(5)
        self.assertEqual(result2, 25)
        print(f"calculate_square(5) = {result2}")

        result3 = calculate_square(-4)
        self.assertEqual(result3, 16)
        print(f"calculate_square(-4) = {result3}")

    def test_calculate_cube(self):
        result1 = calculate_cube(2)
        self.assertEqual(result1, 8)
        print(f"calculate_cube(2) = {result1}")

        result2 = calculate_cube(3)
        self.assertEqual(result2, 27)
        print(f"calculate_cube(3) = {result2}")

        result3 = calculate_cube(-3)
        self.assertEqual(result3, -27)
        print(f"calculate_cube(-3) = {result3}")

if __name__ == "__main__":
    unittest.main()

