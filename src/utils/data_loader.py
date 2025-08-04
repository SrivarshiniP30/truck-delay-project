import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from io import StringIO

# PostgreSQL credentials and database URL
DB_HOST = "localhost"  # Replace with your PostgreSQL server host if different
DB_PORT = "5432"       # Default PostgreSQL port, update if using a custom port
DB_NAME = "truck_data_db"  # Database name where data will be imported
DB_USER = "postgres"   # PostgreSQL username (default is "postgres")
DB_PASSWORD = "saibaba"  # PostgreSQL password (replace with your own)

# Create the SQLAlchemy engine for connecting to PostgreSQL
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Function to download CSV from a GitHub raw URL and upload it to PostgreSQL
def upload_csv_from_url_to_postgres(csv_url, table_name, engine):
    # Get the content of the CSV file from the URL
    response = requests.get(csv_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Read the CSV content into a pandas DataFrame
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        # Upload the DataFrame to PostgreSQL
        df.to_sql(table_name, engine, if_exists='fail', index=False)  # 'fail' ValueError if table already exists
        print(f"Data from {csv_url} uploaded successfully to {table_name}.")
    else:
        print(f"Failed to download {csv_url}. Status code: {response.status_code}")

# Function to get the list of files in a GitHub repository directory using GitHub API
def get_csv_files_from_github(github_api_url):
    response = requests.get(github_api_url)
    
    if response.status_code == 200:
        files = response.json()
        csv_files = [file['path'] for file in files if file['path'].endswith('.csv')]
        return csv_files
    else:
        print(f"Failed to fetch file list from {github_api_url}. Status code: {response.status_code}")
        return []
    
# Function to upload all CSVs from the GitHub directory to PostgreSQL
def upload_all_csvs_from_github(github_api_url, engine):
    # Get the list of CSV files from the GitHub API
    csv_files = get_csv_files_from_github(github_api_url)
    
    # Upload each CSV file
    for csv_file in csv_files:
        raw_url = f"https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/main/{csv_file}"
        table_name = csv_file.split('/')[-1].split('.')[0]  # Use the CSV filename (without extension) as table name
        upload_csv_from_url_to_postgres(raw_url, table_name, engine)

# GitHub API URL to list the contents of the directory (use the 'contents' endpoint)
github_api_url = 'https://api.github.com/repos/sekhar4ml/Truck_Delay_Classification/contents/Data/Training_Data'

# Upload all CSV files from the GitHub URL to PostgreSQL
upload_all_csvs_from_github(github_api_url, engine)
