import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import json
import pickle

# Function to load the saved model and parameters
def prediction(X_test):
    # Load best parameters and model
    with open("best_params.json", "r") as f:
        best_params = json.load(f)
    with open("best_model.pkl", "rb") as f:
        best_model = pickle.load(f)

    # Predict the outcome
    y_pred = best_model.predict(X_test)
    return "No Delay" if y_pred[0] == 0 else "Delay"

def main():
    st.title("Truck Delay Prediction")
    st.header("Please enter the details for delay prediction:")
    
    # Collect user inputs
    average_hours = st.number_input("Average Hours", value=0.0)
    distance = st.number_input("Distance (miles)", value=0.0)
    travel_time_hours = st.number_input("Travel Time (hours)", value=0.0)
    city_humidity_y = st.number_input("City Humidity Y", value=0.0)
    city_temp_y = st.number_input("City Temperature Y", value=0.0)
    city_temp_x = st.number_input("City Temperature X", value=0.0)
    average_speed_mph = st.number_input("Average Speed (mph)", value=0.0)
    city_humidity_x = st.number_input("City Humidity X", value=0.0)
    hour_estimated_arrival = st.number_input("Estimated Arrival Hour", value=0.0)
    humidity = st.number_input("Humidity", value=0.0)
    temp = st.number_input("Temperature", value=0.0)
    city_hour_y = st.number_input("City Hour Y", value=0.0)
    city_pressure_y = st.number_input("City Pressure Y", value=0.0)
    city_visibility_y = st.number_input("City Visibility Y", value=0.0)
    no_of_vehicles = st.number_input("Number of Vehicles", value=0.0)
    city_pressure_x = st.number_input("City Pressure X", value=0.0)

    # Create input DataFrame
    X_test = pd.DataFrame([[
        average_hours, distance, travel_time_hours, city_humidity_y, city_temp_y, 
        city_temp_x, average_speed_mph, city_humidity_x, hour_estimated_arrival, 
        humidity, temp, city_hour_y, city_pressure_y, city_visibility_y, 
        no_of_vehicles, city_pressure_x
    ]], columns=[
        "average_hours", "distance", "travel_time_hours", "city_humidity_y", "city_temp_y", 
        "city_temp_x", "average_speed_mph", "city_humidity_x", "hour_estimated_arrival", 
        "humidity", "temp", "city_hour_y", "city_pressure_y", "city_visibility_y", 
        "no_of_vehicles", "city_pressure_x"
    ])

    # Prediction button
    if st.button("Predict"):
        result = prediction(X_test)  # Call prediction function
        if result == "No Delay":
            st.success("Prediction: No Delay")
        else:
            st.error("Prediction: Delay")

if __name__ == '__main__':
    main()
