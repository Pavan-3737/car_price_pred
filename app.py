import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load data and model
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("🚗 Car Price Prediction App")
st.markdown("### Predict the selling price of a car based on its details.")

brands = sorted(df['brand'].unique().tolist())
brand = st.selectbox("Brand", brands)

sub_models = sorted(df[df['brand'] == brand]['sub_model'].unique().tolist())
sub_model = st.selectbox("Sub-model", sub_models)

year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, step=1)
km_driven = st.number_input("Kilometers Driven", min_value=0, step=500)
fuel = st.selectbox("Fuel Type", sorted(df['fuel'].unique().tolist()))
seller_type = st.selectbox("Seller Type", sorted(df['seller_type'].unique().tolist()))
owner = st.selectbox("Owner Type", sorted(df['owner'].unique().tolist()))

car_age = 2025 - year
price_per_km = round((year / km_driven), 6) if km_driven > 0 else 0
price_per_age = round(year / (car_age + 1), 6)

input_data = pd.DataFrame({
    'brand': [brand],
    'sub_model': [sub_model],
    'year': [year],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'owner': [owner],
    'car_age': [car_age],
    'price_per_km': [price_per_km],
    'price_per_age': [price_per_age]
    
})

st.subheader("🧾 Input Summary")
st.dataframe(input_data)

if st.button("🔮 Predict Price"):
    try:
        prediction = pipe.predict(input_data)
        st.success(f"💰 Estimated Selling Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Something went wrong during prediction:\n{e}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
