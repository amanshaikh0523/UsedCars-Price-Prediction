import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page Title
st.title("🚗 Used Car Price Prediction")
st.write("Enter the vehicle details below to predict its price.")

# Input Fields

company = st.text_input("Company")
model_name = st.text_input("Model")
variant = st.text_input("Variant")

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "Electric"]
)

colour = st.text_input("Colour")

kilometer = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=50000
)

body_style = st.text_input("Body Style")

transmission = st.selectbox(
    "Transmission Type",
    ["Manual", "Automatic"]
)

model_year = st.number_input(
    "Model Year",
    min_value=2000,
    max_value=2035,
    value=2020
)

cngkit = st.selectbox(
    "CNG Kit",
    ["Yes", "No"]
)

owner = st.number_input(
    "Number of Owners",
    min_value=1,
    max_value=10,
    value=1
)

dealer_state = st.text_input("Dealer State")

dealer_name = st.text_input("Dealer Name")

city = st.text_input("City")

warranty = st.number_input(
    "Warranty (Months)",
    min_value=0,
    value=0
)

quality_score = st.number_input(
    "Quality Score",
    min_value=0.0,
    max_value=10.0,
    value=7.0
)

car_age = st.number_input(
    "Car Age",
    min_value=0,
    value=3
)

# Prediction Button
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        'Company': [company],
        'Model': [model_name],
        'Variant': [variant],
        'FuelType': [fuel_type],
        'Colour': [colour],
        'Kilometer': [kilometer],
        'BodyStyle': [body_style],
        'TransmissionType': [transmission],
        'ModelYear': [model_year],
        'CngKit': [cngkit],
        'Owner': [owner],
        'DealerState': [dealer_state],
        'DealerName': [dealer_name],
        'City': [city],
        'Warranty': [warranty],
        'QualityScore': [quality_score],
        'CarAge': [car_age]
    })

    try:
        prediction = model.predict(input_data)

        st.success(
            f"💰 Estimated Used Car Price: ₹ {prediction[0]:,.2f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")