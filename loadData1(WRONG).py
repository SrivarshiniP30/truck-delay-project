import os
import psycopg2
import pandas as pd

# PostgreSQL connection details
DB_HOST = "localhost"  # Replace with your PostgreSQL server host if different
DB_PORT = "5432"       # Default PostgreSQL port, update if using a custom port
DB_NAME = "truck_data_db"  # Database name where data will be imported
DB_USER = "postgres"   # PostgreSQL username (default is "postgres")
DB_PASSWORD = "saibaba"  # PostgreSQL password (replace with your own)

# Path to the folder containing CSV files for import
CSV_FOLDER_PATH = r"C:\AIML\VS-Lab\TruckProject\Truck_Delay_Classification\Data\Training_Data"

# Connect to PostgreSQL
try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    conn.autocommit = True  # Enable autocommit to execute database changes immediately
    cursor = conn.cursor()  # Create a cursor object to execute SQL queries
    print("Connected to PostgreSQL database")
except Exception as e:
    # Print an error message and exit if the connection fails
    print(f"Connection failed: {e}")
    exit()

# Function to import a CSV file into a PostgreSQL table
def import_csv_to_postgres(csv_file, table_name):
    try:
        # Load the CSV file into a Pandas DataFrame for data manipulation
        df = pd.read_csv(csv_file)

        # Dynamically create a SQL statement to define the table structure
        columns = ", ".join([f"{col} TEXT" for col in df.columns])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")

        # Insert each row of data from the DataFrame into the PostgreSQL table
        for _, row in df.iterrows():
            values = ", ".join([f"'{str(val).replace('\'', '\'\'')}'" for val in row])
            cursor.execute(f"INSERT INTO {table_name} VALUES ({values});")

        print(f"Imported {csv_file} into {table_name}")
    except Exception as e:
        # Print an error message if there is an issue with importing
        print(f"Error importing {csv_file}: {e}")

# Loop through all CSV files in the specified folder
for file in os.listdir(CSV_FOLDER_PATH):
    if file.endswith(".csv"):  # Process only files with a .csv extension
        csv_path = os.path.join(CSV_FOLDER_PATH, file)  # Full path of the CSV file
        table_name = os.path.splitext(file)[0]  # Use the file name (without extension) as the table name
        import_csv_to_postgres(csv_path, table_name)

# Close the database connection after all files are imported
cursor.close()
conn.close()
print("Finished importing CSV files")
