# test_module7.py

import unittest
import pandas as pd
import numpy as np
from pandas_operations import create_dataframe, filter_dataframe_by_age, calculate_mean_age
from numpy_operations import create_numpy_array, square_numpy_array, calculate_array_mean

class TestPandasOperations(unittest.TestCase):
    def test_create_dataframe(self):
        df = create_dataframe()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 3))

    def test_filter_dataframe_by_age(self):
        df = create_dataframe()
        filtered_df = filter_dataframe_by_age(df, 28, 35)
        self.assertEqual(filtered_df.shape, (2, 3))
        self.assertEqual(filtered_df['Name'].tolist(), ['Bob', 'Charlie'])

    def test_calculate_mean_age(self):
        df = create_dataframe()
        mean_age = calculate_mean_age(df)
        self.assertAlmostEqual(mean_age, 31.0)

class TestNumPyOperations(unittest.TestCase):
    def test_create_numpy_array(self):
        array = create_numpy_array()
        self.assertIsInstance(array, np.ndarray)
        self.assertEqual(array.tolist(), [1, 2, 3, 4, 5])

    def test_square_numpy_array(self):
        array = create_numpy_array()
        squared_array = square_numpy_array(array)
        self.assertEqual(squared_array.tolist(), [1, 4, 9, 16, 25])

    def test_calculate_array_mean(self):
        array = create_numpy_array()
        array_mean = calculate_array_mean(array)
        self.assertAlmostEqual(array_mean, 3.0)

if __name__ == "__main__":
    unittest.main()

