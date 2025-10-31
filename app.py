import streamlit as st
import pickle
import numpy as np
import pandas as pd

df=pickle.load(open('df.pkl','rb'))
pipe=pickle.load(open('pipe.pkl','rb'))

st.title("Car Price Predictor App")

year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2018)
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=30000)

fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual', 'Trustmark Dealer'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
owner = st.selectbox("Owner Type", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
top_brands = st.selectbox("Brand", ['Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Toyota', 'Honda', 'Ford', 'Renault', 'Chevrolet', 'Volkswagen', 'BMW', 'Mercedes-Benz', 'Audi', 'Skoda', 'Nissan', 'Kia'])

car_age = 2025 - year
price_per_km = 0  # placeholder, not needed for prediction but keeps column alignment
price_per_age = 0

input_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'transmission': [transmission],
    'owner': [owner],
    'top_brands': [top_brands],
    'car_age': [car_age],
    'price_per_km': [price_per_km],
    'price_per_age': [price_per_age]
})

# Predict
if st.button("Predict Price 💰"):
    prediction = pipe.predict(input_data)[0]
    st.success(f"Estimated Car Price: ₹ {prediction:,.2f}")
