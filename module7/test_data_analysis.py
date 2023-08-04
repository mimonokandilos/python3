# test_data_analysis.py
import unittest
import data_science_intro as ds

class TestDataAnalysis(unittest.TestCase):

    def test_numpy_array(self):
        expected = [1, 2, 3, 4, 5]
        self.assertListEqual(list(ds.numpy_array), expected)
        print("Test query for NumPy array:")
        print("NumPy Array:", ds.numpy_array)
        print("Expected Result:", expected)
        print("Test Passed:", list(ds.numpy_array) == expected)
        print("---")

    def test_pandas_dataframe(self):
        expected_names = ['Alice', 'Bob', 'Charlie', 'David']
        expected_ages = [25, 30, 22, 28]
        self.assertListEqual(list(ds.df['Name']), expected_names)
        self.assertListEqual(list(ds.df['Age']), expected_ages)
        print("Test query for Pandas DataFrame:")
        print("Names:", list(ds.df['Name']))
        print("Ages:", list(ds.df['Age']))
        print("Expected Names:", expected_names)
        print("Expected Ages:", expected_ages)
        print("Test Passed:", list(ds.df['Name']) == expected_names and list(ds.df['Age']) == expected_ages)
        print("---")

if __name__ == "__main__":
    unittest.main()

