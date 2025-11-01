import streamlit as st
import pandas as pd
import numpy as np
import pickle

df=pickle.load(open('df.pkl','rb'))
pipe=pickle.load(open('pipe.pkl','rb'))

st.title("🚗 Car Price Prediction App")
st.markdown("### Predict the selling price of a car based on its details.")

name = st.text_input("Car Name (Brand/Model)")
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, step=1)
km_driven = st.number_input("Kilometers Driven", min_value=0, step=500)
fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel'])
seller_type = st.selectbox("Seller Type", ['Individual', 'Dealer'])
owner = st.selectbox("Owner Type", [
    'First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'
])

price_per_km = 0
if km_driven > 0:
    price_per_km = round((year / km_driven), 6)

input_data = pd.DataFrame({
    'name': [name],
    'year': [year],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'owner': [owner],
    'price_per_km': [price_per_km]
})

st.subheader("🧾 Input Summary")
st.dataframe(input_data)

if st.button("🔮 Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"💰 Estimated Selling Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Something went wrong during prediction:\n{e}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
