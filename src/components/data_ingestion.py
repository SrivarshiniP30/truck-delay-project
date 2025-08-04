import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from io import StringIO

class DataIngestion:
    def __init__(self):
        # Load database credentials from environment variables
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = os.getenv("DB_PORT", "5432")
        self.db_name = os.getenv("DB_NAME", "truck_data_db")
        self.db_user = os.getenv("DB_USER", "postgres")
        self.db_password = os.getenv("DB_PASSWORD", "saibaba")
        self.engine = create_engine(f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}')

    def upload_csv_from_url(self, csv_url, table_name):
        try:
            response = requests.get(csv_url)
            response.raise_for_status()

            csv_data = StringIO(response.text)
            df = pd.read_csv(csv_data)

            df.to_sql(table_name, self.engine, if_exists='fail', index=False)
            print(f"Data from {csv_url} uploaded successfully to {table_name}.")
        except Exception as e:
            print(f"Error uploading {csv_url} to {table_name}: {e}")

    def get_csv_files_from_github(self, github_api_url):
        try:
            response = requests.get(github_api_url)
            response.raise_for_status()

            files = response.json()
            csv_files = [file['path'] for file in files if file['path'].endswith('.csv')]
            return csv_files
        except Exception as e:
            print(f"Error fetching file list from {github_api_url}: {e}")
            return []

    def upload_all_csvs_from_github(self, github_api_url):
        csv_files = self.get_csv_files_from_github(github_api_url)

        for csv_file in csv_files:
            raw_url = f"https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/main/{csv_file}"
            table_name = os.path.splitext(os.path.basename(csv_file))[0]
            self.upload_csv_from_url(raw_url, table_name)
