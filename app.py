import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("House Price Prediction")

# User Inputs
square_footage = st.number_input("Square Footage", min_value=0.0)
num_bedrooms = st.number_input("Number of Bedrooms", min_value=0)
num_bathrooms = st.number_input("Number of Bathrooms", min_value=0)
year_built = st.number_input("Year Built", min_value=1800)
lot_size = st.number_input("Lot Size", min_value=0.0)
garage_size = st.number_input("Garage Size", min_value=0)
neighborhood_quality = st.number_input("Neighborhood Quality", min_value=0)

# Predict Button
if st.button("Predict Price"):

    features = np.array([[square_footage,
                          num_bedrooms,
                          num_bathrooms,
                          year_built,
                          lot_size,
                          garage_size,
                          neighborhood_quality]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
