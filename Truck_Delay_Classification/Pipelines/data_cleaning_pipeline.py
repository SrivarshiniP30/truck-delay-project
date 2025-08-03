
from sqlalchemy import create_engine
import os.path as path
import sys
import os
import warnings
warnings.filterwarnings("ignore")

parent_directory = os.path.abspath(path.join(__file__,"../../"))
sys.path.append(parent_directory)
from src.components.data_cleaning import DataCleaning


print("DataCleaning imported successfully!")


class DataCleaningPipeline:
    def __init__(self):
        self.stage_name = "Data Cleaning"
        self.engine = create_engine(
            'postgresql://postgres:saibaba@localhost:5432/truck_data_db'
        )

    def main(self):
        try:
            print(f">> Stage started: {self.stage_name} <<<<<<<")

            # Initialize the DataCleaning component
            cleaner = DataCleaning(self.engine)

            # Load and clean data
            cleaner.load_data()
            combined_df = cleaner.clean_and_merge_data()

            print(f">> Stage completed: {self.stage_name} <<")
            return combined_df
        except Exception as e:
            print(f"Error in {self.stage_name}: {e}")
            raise e

if __name__ == "__main__":
    pipeline = DataCleaningPipeline()
    pipeline.main()
