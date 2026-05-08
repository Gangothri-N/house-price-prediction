import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("House Price Prediction")

square_feet = st.number_input("Square Feet")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
year_built = st.number_input("Year Built")

if st.button("Predict Price"):

    features = np.array([[square_feet, bedrooms, bathrooms, year_built]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")