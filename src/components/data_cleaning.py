import pandas as pd
from sqlalchemy import create_engine, inspect

class DataCleaning:
    def __init__(self, engine):
        self.engine = engine
        self.dataframes = {}

    def load_data(self):
        # Load all tables into DataFrames
        inspector = inspect(self.engine)
        tables = inspector.get_table_names()
        for table in tables:
            self.dataframes[table] = pd.read_sql_table(table, con=self.engine)
            print(f"Loaded table: {table}")

    def clean_and_merge_data(self):
       
        df = pd.merge(self.dataframes['truck_schedule_table'], self.dataframes['trucks_table'], on='truck_id', how='left')
        df = pd.merge(df, self.dataframes['drivers_table'], left_on="truck_id", right_on="vehicle_no", how='left')
        df = pd.merge(df, self.dataframes['routes_table'], on='route_id', how='left')
  
        # Convert dates to datetime
        df['departure_date'] = pd.to_datetime(df['departure_date'], errors='coerce')
        self.dataframes['routes_weather']['Date'] = pd.to_datetime(self.dataframes['routes_weather']['Date'], errors='coerce')

        # Sort values for asof merge
        df.sort_values(by='departure_date', inplace=True)
        self.dataframes['routes_weather'].sort_values(by='Date', inplace=True)

        # Merge with routes_weather
        df = pd.merge_asof(
            df,
            self.dataframes['routes_weather'],
            by='route_id',
            left_on='departure_date',
            right_on='Date',
            direction='backward'
        )
        
        # Handle city_weather
        self.dataframes['city_weather'] = self.dataframes['city_weather'].add_prefix('city_')
        filtered_city_weather = self.dataframes['city_weather'][self.dataframes['city_weather']['city_hour'] == 700]
        filtered_city_weather = filtered_city_weather.drop_duplicates(subset=['city_city_id', 'city_date'])

        df = pd.merge(
            df,
            filtered_city_weather,
            left_on=['origin_id', 'Date'],
            right_on=['city_city_id', 'city_date'],
            how='left'
        )
        
        # Additional merging and cleaning
        self.dataframes['city_weather']['combined_datetime'] = pd.to_datetime(
            self.dataframes['city_weather']['city_date'].astype(str) + ' ' +
            self.dataframes['city_weather']['city_hour'].astype(str).str.zfill(4),
            format='%Y-%m-%d %H%M'
        )
        
        df['estimated_arrival'] = pd.to_datetime(df['estimated_arrival'], errors='coerce')
        df['estimated_arrival'] = df['estimated_arrival'].dt.round('H')
        
        df = pd.merge(
            df,
            self.dataframes['city_weather'],
            left_on=['destination_id', 'estimated_arrival'],
            right_on=['city_city_id', 'combined_datetime'],
            how='left'
        )
        self.dataframes['traffic_table']['combined_datetime'] = pd.to_datetime(
            self.dataframes['traffic_table']['date'].astype(str) + ' ' +
            self.dataframes['traffic_table']['hour'].astype(str).str.zfill(4),
            format='%Y-%m-%d %H%M'
        )

        df = pd.merge(
            df,
            self.dataframes['traffic_table'],
            left_on=['route_id', 'departure_date'],
            right_on=['route_id', 'combined_datetime'],
            how='left'
        )
        # Save combined DataFrame to CSV
        df.to_csv('combineddf.csv', index=False)
        print("Combined DataFrame saved as 'combineddf.csv'")
        return df
