import pandas as pd
import psycopg2
import requests
from io import StringIO

# PostgreSQL connection details
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "truck_data_db"
DB_USER = "postgres"
DB_PASSWORD = "saibaba"

GIT_URLS = {
    "trucks_table": "https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/trucks_table.csv",
    "truck_schedule_table": "https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/truck_schedule_table.csv",
    "city_weather" : "https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/city_weather.csv",
                     #https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/city_weather.csv
    "drivers_table":"https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/drivers_table.csv",
    "routes_table":"https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/routes_table.csv",
    "routes_weather":"https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/routes_weather.csv",
    "traffic_table":"https://raw.githubusercontent.com/sekhar4ml/Truck_Delay_Classification/072887fb3c5b779e8dc8b47c5545c1a458b850ed/Data/Training_Data/traffic_table.csv",
}

# Mapping table names to their queries
TABLE_QUERIES = {
    "trucks_table": { #TABLE1
        "create_query": """
        CREATE TABLE IF NOT EXISTS trucks_table (
            truck_id INT,
            truck_age INT,
            load_capacity_pounds FLOAT,
            mileage_mpg FLOAT,
            fuel_type VARCHAR
        );
        """,
        "insert_query": """
        INSERT INTO trucks_table (truck_id, truck_age, load_capacity_pounds, mileage_mpg, fuel_type)
        VALUES (%s, %s, %s, %s, %s);
        """
    },
    
    "truck_schedule_table": { #TABLE2
        "create_query": """
        CREATE TABLE IF NOT EXISTS truck_schedule_table (
            truck_id INT,
            route_id VARCHAR,
            departure_date TIMESTAMP,
            estimated_arrival TIMESTAMP,
            delay FLOAT
        );
        """,
        "insert_query": """
        INSERT INTO truck_schedule_table (truck_id, route_id, departure_date, estimated_arrival, delay)
        VALUES (%s, %s, %s, %s, %s);
        """
    },
    
    "city_weather": { #TABLE3
        "create_query": """
        CREATE TABLE IF NOT EXISTS city_weather (
            city_id VARCHAR,
            date TIMESTAMP,
            hour INT,
            temp INT,
            wind_speed INT,
            description VARCHAR,
            precip FLOAT,
            humidity INT,
            visibility INT,
            pressure INT,
            chanceofrain INT,
            chanceoffog INT,
            chanceofsnow INT,
            chanceofthunder INT
        );
        """,
        "insert_query": """
        INSERT INTO city_weather (city_id, date, hour, temp, wind_speed, description, precip, humidity, visibility
                        , pressure, chanceofrain, chanceoffog, chanceofsnow, chanceofthunder)
        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s);
        """
    },
    "drivers_table": { #TABLE4
        "create_query": """
        CREATE TABLE IF NOT EXISTS drivers_table (
            driver_id VARCHAR,
            name VARCHAR,
            gender VARCHAR,
            age	INT,
            experience INT, 
            driving_style VARCHAR,
            ratings	INT,
            vehicle_no INT,
            average_speed_mph FLOAT
        );
        """,
        "insert_query": """
        INSERT INTO drivers_table (driver_id, name,gender,age,experience,driving_style,
                            ratings,vehicle_no,average_speed_mph)
        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s);
        """
    },
    #route_id	origin_id	destination_id	distance	average_hours
    #R-ada2a391	C-927ceb5e	C-56e39a5e	1735.06	34.7

    "routes_table": { #TABLE5
        "create_query": """
        CREATE TABLE IF NOT EXISTS routes_table (
            route_id VARCHAR,
            origin_id VARCHAR,
            destination_id VARCHAR,
            distance FLOAT,
            average_hours FLOAT
        );
        """,
        "insert_query": """
        INSERT INTO routes_table (route_id, origin_id, destination_id, distance, average_hours)
        VALUES (%s, %s, %s, %s, %s);
        """
    },
    #route_id,Date,temp,wind_speed,description,precip,humidity,visibility,pressure,chanceofrain,chanceoffog,chanceofsnow,chanceofthunder
#R-ada2a391,2019-01-01 00:00:00,30,11,Heavy snow,0.0,90,1,1010,0,0,0,0

    "routes_weather": { #TABLE6
        "create_query": """
        CREATE TABLE IF NOT EXISTS routes_weather (
            route_id VARCHAR,
            Date TIMESTAMP
            temp INT,
            wind_speed INT,
            description VARCHAR,
            precip FLOAT,
            humidity INT,
            visibility INT,
            pressure INT,
            chanceofrain INT,
            chanceoffog INT,
            chanceofsnow INT,
            chanceofthunder INT
        );
        """,
        "insert_query": """
        INSERT INTO routes_weather (rroute_id,Date,temp,wind_speed,description,precip,humidity,visibility,pressure,
                                chanceofrain,chanceoffog,chanceofsnow,chanceofthunder)
        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s);
        """
    },
    #route_id,date,hour,no_of_vehicles,accident
    #R-ada2a391,2019-01-01,0,669.0,0

    "traffic_table": { #TABLE7
        "create_query": """
        CREATE TABLE IF NOT EXISTS traffic_table (
            route_id VARCHAR,
            date TIMESTAMP,
            hour INT,
            no_of_vehicles FLOAT,
            accident INT
        );
        """,
        "insert_query": """
        INSERT INTO traffic_table (route_id,date,hour,no_of_vehicles,accident)
        VALUES (%s, %s, %s, %s, %s);
        """
    }
}

# Function to process CSV and insert into respective tables
def process_csv_and_insert_with_queries(url, table_name):
    try:
        # Fetch CSV data from Git
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        csv_data = StringIO(response.text)

        # Load data into pandas DataFrame
        df = pd.read_csv(csv_data)
        print(f"CSV Data for {table_name} Loaded Successfully:")
        print(df.head())  # Inspect first few rows

        # Get the queries for the table
        queries = TABLE_QUERIES[table_name]
        create_query = queries["create_query"]
        insert_query = queries["insert_query"]

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Create table
        cursor.execute(create_query)

        # Insert data
        for i, row in df.iterrows():
            cursor.execute(insert_query, tuple(row)) #needs to be tuple for every row

        # Commit and close
        conn.commit()
        print(f"Data for {table_name} transferred successfully!")
        if conn:
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error for {table_name}: {e}")
    finally:
        print(f"Processing of {table_name} complete.")
        
for table_name, url in GIT_URLS.items():
    process_csv_and_insert_with_queries(url, table_name)