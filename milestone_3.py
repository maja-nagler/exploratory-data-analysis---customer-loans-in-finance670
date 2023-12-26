from DataFrameInfo import DataFrameInfo
from DataTransform import DataTransform
import pandas as pd



# Loading data into dataframe as "loan_data"
loan_data = pd.read_csv('loan_payments.csv')



# Display the first few rows of the dataframe
print(loan_data.head())
print(loan_data.dtypes)



# Print information about dataframe
print(DataFrameInfo.describe_columns(loan_data))
print(DataFrameInfo.calculate_statistics(loan_data))
print(DataFrameInfo.count_distinct_values(loan_data, ['grade', 'sub_grade', 'term'])) #categorical columns
DataFrameInfo.print_shape(loan_data)
print(DataFrameInfo.count_null_values(loan_data))


# Example usage
DataTransform.convert_to_numeric(loan_data, ['loan_amount', 'collections_12_mths_ex_med'])
DataTransform.convert_to_datetime(loan_data, ['issue_date', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date'])