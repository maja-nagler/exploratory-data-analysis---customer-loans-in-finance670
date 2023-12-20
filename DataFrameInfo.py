import pandas as pd

# Creating DataFrameInfo class

class DataFrameInfo:
    @staticmethod
    def describe_columns(dataframe):
        return dataframe.dtypes
    
    @staticmethod
    def calculate_statistics(dataframe):
        return dataframe.describe()
    
    @staticmethod
    def count_distinct_values(dataframe, columns):
        return {col: dataframe[col].nunique() for col in columns if dataframe[col].dtype == 'object'}
    
    @staticmethod
    def print_shape(dataframe):
        print(dataframe.shape)
    
    @staticmethod
    def count_null_values(dataframe):
        return dataframe.isnull().sum()
    
    # Potential for other methods
