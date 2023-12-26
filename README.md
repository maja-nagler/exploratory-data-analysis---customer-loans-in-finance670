# Project Title: Exploratory Data Analysis - Customer Loans in Finance


# Project description: 
Project is an attempt to apply EDA to fake dataset on customer loans in finance

# Usage instructions:
    The project contains the following files:

**"db_utils.py"**: contains code to extract the data from the database, including class RDSDatabaseConnector containing the methods which extracting data from the RDS database into "loan_payments.csv" file.

**"credentials.yaml"**: stores the database credentials (part of ".gitignore" file)

**"DataTransform.py"**: file contains a class "DataTransform" allowing to convert data into the correct format (numeric, datetime etc.)

**"DataFrameInfo.py"**: file contains a class "DataFrameInfo" containing methods that generate information about the DataFrame, that includes the following functions: 

1. **"describe_columns"** -  returns data types of described columns in the DataFrame
2. **"calculate_statistics"** - extracts statistical values: median, standard deviation and mean from the columns and the DataFrame
3. **"count_distinct_values"** - counts distinct values in categorical columns
4. **"print_shape"** - returns shape of the DataFrame
5. **"count_null_values"** - generates a count/percentage count of NULL values in each column

**"Plotter.py"**: file contains "Plotter" class to visualise insights from the data

**"DataFrameTransform.py"**: file contains "DataFrameTransform" class to perform EDA transformations on the data ()
    e.g. "null_percentage" function calculates percentage of NULL values in each column
        or "drop_columns" function drops specified columns


**"milestone_3.py"**: application of the classes previously created (throughout milestone 3), data transformation

**"milestone_4.py"**: gaining deeper insight of the data (created throughout milestone 4)

