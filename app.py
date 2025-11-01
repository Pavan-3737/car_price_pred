import streamlit as st
import pandas as pd
import numpy as np
import pickle

df=pickle.load(open('df.pkl','rb'))
pipe=pickle.load(open('pipe.pkl','rb'))

car_names = [
    "Maruti Swift Dzire VDI", "Maruti Alto 800 LXI", "Maruti Alto LXi", "Maruti Alto LX",
    "Maruti Swift VDI BSIV", "Hyundai EON Era Plus", "Maruti Wagon R VXI BS IV",
    "Maruti Swift VDI", "Maruti Wagon R LXI Minor", "Maruti 800 AC",
    "Hyundai Santro Xing GLS", "Maruti Alto K10 VXI", "Maruti Ritz VDi",
    "Renault KWID RXT", "Hyundai EON Magna Plus", "Mahindra XUV500 W8 2WD",
    "Maruti Wagon R LXI", "Renault KWID 1.0 RXT Optional", "Ford Figo Diesel Titanium",
    "Hyundai Verna 1.6 SX CRDi (O)", "Maruti Alto LXi BSIII", "Tata Indica GLS BS IV",
    "Chevrolet Beat Diesel LT", "Hyundai Verna 1.6 SX", "Maruti Alto 800 VXI",
    "Mahindra XUV500 W6 2WD", "Chevrolet Spark 1.0 LS", "Maruti Swift Vdi BSIII",
    "Tata New Safari DICOR 2.2 EX 4x2", "Ford Ecosport 1.5 DV5 MT Titanium",
    "Chevrolet Beat Diesel LS", "Mahindra Bolero Power Plus SLX", "Chevrolet Beat LT",
    "Maruti Ertiga VDI", "Hyundai Grand i10 Sportz", "Maruti Swift Dzire ZDI"
]

st.title("🚗 Car Price Prediction App")
st.markdown("### Predict the selling price of a car based on its details.")

name = st.selectbox("Car Name", car_names)
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

car_age = 2025 - year
price_per_age = round(year / (car_age + 1), 6)

input_data = pd.DataFrame({
    'name': [name],
    'year': [year],
    'km_driven': [km_driven],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'owner': [owner],
    'price_per_km': [price_per_km],
    'car_age': [car_age],
    'price_per_age': [price_per_age]
})

st.subheader("🧾 Input Summary")
st.dataframe(input_data)

if st.button("🔮 Predict Price"):
    try:
        prediction =pipe.predict(input_data)
        st.success(f"💰 Estimated Selling Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Something went wrong during prediction:\n{e}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
