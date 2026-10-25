import streamlit as st
import pandas as pd
import joblib

# Set up the app title and description
st.title("Advertising Sales Prediction App")
st.write("""
This app predicts the **Sales** volume based on advertising budgets spent on **TV**, **Radio**, and **Newspaper**.
"""
)

# Load the saved model
model = joblib.load('model.sav')

# Create input sliders for features
st.sidebar.header('Input Parameters')
tv = st.sidebar.slider('TV Advertising Budget ($)', 0.0, 300.0, 150.0)
radio = st.sidebar.slider('Radio Advertising Budget ($)', 0.0, 50.0, 25.0)
newspaper = st.sidebar.slider('Newspaper Advertising Budget ($)', 0.0, 100.0, 30.0)

# Create a DataFrame for prediction matching the original format
input_data = pd.DataFrame({
    'TV': [tv],
    'Radio': [radio],
    'Newspaper': [newspaper]
})

# Display input parameters
st.subheader('User Input parameters')
st.write(input_data)

# Predict and show results
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.subheader('Prediction Result')
    st.success(f"Predicted Sales: **{prediction[0]:.2f}** M")
