# data_science_intro.py
import numpy as np
import pandas as pd

# Create a NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])

# Create a Pandas Series
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28]}
df = pd.DataFrame(data)

# Test cases for data analysis libraries
if __name__ == "__main__":
    print("NumPy Array:", numpy_array)
    print("Pandas DataFrame:\n", df)

