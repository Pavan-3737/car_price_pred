import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load data and model
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("🚗 Car Price Prediction App")
st.markdown("### Predict the selling price of a car based on its details.")

# Combine brand + sub_model to form car names
car_names = sorted((df['brand'] + " " + df['sub_model']).unique().tolist())
name = st.selectbox("Car Name", car_names)

# Inputs
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, step=1)
km_driven = st.number_input("Kilometers Driven", min_value=0, step=500)
fuel = st.selectbox("Fuel Type", sorted(df['fuel'].unique().tolist()))
seller_type = st.selectbox("Seller Type", sorted(df['seller_type'].unique().tolist()))
owner = st.selectbox("Owner Type", sorted(df['owner'].unique().tolist()))

# Derived features
car_age = 2025 - year
price_per_km = round((year / km_driven), 6) if km_driven > 0 else 0
price_per_age = round(year / (car_age + 1), 6)

# Extract brand and sub-model
brand = name.split()[0]
sub_model = " ".join(name.split()[1:3]) if len(name.split()) > 1 else ""

# Prepare input
input_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'owner': [owner],
    'car_age': [car_age],
    'price_per_km': [price_per_km],
    'price_per_age': [price_per_age],
    'brand': [brand],
    'sub_model': [sub_model]
})

st.subheader("🧾 Input Summary")
st.dataframe(input_data)

# Predict button
if st.button("🔮 Predict Price"):
    try:
        prediction = pipe.predict(input_data)
        st.success(f"💰 Estimated Selling Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Something went wrong during prediction:\n{e}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
