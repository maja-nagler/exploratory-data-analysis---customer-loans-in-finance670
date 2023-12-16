import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = None
    
    def load_credentials(self, file_path):
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    
    def initialize_engine(self):
        db_username = self.credentials['RDS_USER']
        db_password = self.credentials['RDS_PASSWORD']
        db_host = self.credentials['RDS_HOST']
        db_port = self.credentials['RDS_PORT']
        db_name = self.credentials['RDS_DATABASE']
        
        db_string = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        self.engine = create_engine(db_string)
    
    def extract_data_to_dataframe(self):
        query = "SELECT * FROM loan_payments;"
        return pd.read_sql(query, self.engine)
    
    def save_to_csv(self, dataframe, file_name):
        dataframe.to_csv(file_name, index=False)

    def load_data_from_csv(self, file_name):
        try:
            return pd.read_csv(file_name)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return None


def main():
    # Step 3: Load credentials from credentials.yaml
    db = RDSDatabaseConnector({})
    credentials = db.load_credentials('credentials.yaml')
    
    # Step 4: Initialize RDSDatabaseConnector with credentials
    db = RDSDatabaseConnector(credentials)
    
    # Step 5: Initialize SQLAlchemy engine
    db.initialize_engine()
    
    # Step 6: Extract data from RDS database to DataFrame
    loan_data = db.extract_data_to_dataframe()
    
    # Step 7: Save data to CSV
    db.save_to_csv(loan_data, 'loan_payments.csv')

    # Task 3:
    loaded_data = db.load_data_from_csv('loan_payments.csv')
    
    if loaded_data is not None:
        print("Data loaded successfully.")
        # Perform operations with loaded_data DataFrame
    else:
        print("Failed to load data.")
    

if __name__ == "__main__":
    main()