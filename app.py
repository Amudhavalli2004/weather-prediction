import streamlit as st
import pandas as pd
import joblib

regr = joblib.load('predictor.pkl')

st.title("Weather Temperature Prediction")

st.sidebar.header("Input Features")

maxtempC = st.sidebar.slider("Max Temperature (°C)", min_value=0, max_value=40, value=28)
mintempC = st.sidebar.slider("Min Temperature (°C)", min_value=-10, max_value=30, value=16)
cloudcover = st.sidebar.slider("Cloud Cover (%)", min_value=0, max_value=100, value=2)
humidity = st.sidebar.slider("Humidity (%)", min_value=0, max_value=100, value=62)
sunHour = st.sidebar.slider("Sun Hours", min_value=0.0, max_value=24.0, value=11.6)
HeatIndexC = st.sidebar.slider("Heat Index (°C)", min_value=0, max_value=40, value=26)
precipMM = st.sidebar.slider("Precipitation (mm)", min_value=0.0, max_value=50.0, value=0.0)
pressure = st.sidebar.slider("Pressure (hPa)", min_value=900, max_value=1100, value=1013)
windspeedKmph = st.sidebar.slider("Wind Speed (Kmph)", min_value=0, max_value=50, value=14)

input_data = pd.DataFrame({
    "maxtempC": [maxtempC],
    "mintempC": [mintempC],
    "cloudcover": [cloudcover],
    "humidity": [humidity],
    "sunHour": [sunHour],
    "HeatIndexC": [HeatIndexC],
    "precipMM": [precipMM],
    "pressure": [pressure],
    "windspeedKmph": [windspeedKmph]
})

prediction = regr.predict(input_data)[0]

actual_temperature = 25.0

temperature_difference = abs(actual_temperature - prediction)

color_threshold = 5.0

if temperature_difference <= color_threshold:
    text_color = "green"  
else:
    text_color = "red" 

st.markdown(f"<h1 style='font-size: 36px; color: {text_color};'>Predicted Temperature (°C): {prediction:.2f}</h1>", unsafe_allow_html=True)