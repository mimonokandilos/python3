# pandas_operations.py

import pandas as pd

def create_dataframe():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [30, 28, 35],
        'Department': ['HR', 'IT', 'Finance']
    }
    return pd.DataFrame(data)

def filter_dataframe_by_age(dataframe, min_age, max_age):
    return dataframe[(dataframe['Age'] >= min_age) & (dataframe['Age'] <= max_age)]

def calculate_mean_age(dataframe):
    return dataframe['Age'].mean()

