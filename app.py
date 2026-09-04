import streamlit as st
import requests

'''
# TaxiFareModel front
'''



# Date and time
date = st.date_input("Pickup date")
time = st.time_input("Pickup time")

# Pickup coordinates
pickup_longitude = st.number_input("Pickup longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup latitude", value=40.748817)

# Dropoff coordinates
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.748817)

# Passenger count
passenger_count = st.number_input(
    "Passenger count",
    min_value=1,
    max_value=8,
    value=1
)



url = "https://taxifare.lewagon.ai/predict"


if st.button("Predict fare"):

    # Build the dictionary containing the parameters
    params = {
        "pickup_datetime": f"{date} {time}",
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Call the API
    response = requests.get(url, params=params)

    # Retrieve the prediction from the JSON
    prediction = response.json()["fare"]

    # Display the prediction
    st.markdown(f"## Predicted fare: ${prediction:.2f}")
