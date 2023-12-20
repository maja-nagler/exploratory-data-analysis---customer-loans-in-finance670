import pandas as pd

# Creating DataTransform class
class DataTransform:
    @staticmethod
    def convert_to_numeric(dataframe, columns):
        for col in columns:
            dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce')
    
    @staticmethod
    def convert_to_datetime(dataframe, columns):
        for col in columns:
            dataframe[col] = pd.to_datetime(dataframe[col], errors='coerce')
    
    # Potential for other methods