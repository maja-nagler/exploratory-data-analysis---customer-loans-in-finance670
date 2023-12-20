from db_utils import RDSDatabaseConnector

def main():
    db = RDSDatabaseConnector({})  # Initialising the RDSDatabaseConnector
    loaded_data = db.load_data_from_csv('loan_payments.csv')  # Loading data from the CSV file
    
    if loaded_data is not None:
        # Displaying the first few rows of the DataFrame
        print("First 5 rows of the loaded DataFrame:")
        print(loaded_data.head())
        
        # Getting summary statistics of the DataFrame
        print("\nSummary statistics of the loaded DataFrame:")
        print(loaded_data.describe())
        
        # Getting information about the DataFrame (columns, data types)
        print("\nInformation about the loaded DataFrame:")
        print(loaded_data.info())
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()
