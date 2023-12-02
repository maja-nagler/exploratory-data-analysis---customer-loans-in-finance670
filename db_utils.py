import pandas as pd
import psycopg2  # Example: using psycopg2 for PostgreSQL, modify as per your RDS setup

class RDSDatabaseConnector:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to the database!")
        except psycopg2.Error as e:
            print(f"Error: Could not connect to the database: {e}")

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print("Disconnected from the database.")
        else:
            print("No active connection.")

    def fetch_data(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(data, columns=columns)
            cursor.close()
            return df
        except psycopg2.Error as e:
            print(f"Error fetching data: {e}")
            return None

    # Add more methods as needed for specific data extraction tasks