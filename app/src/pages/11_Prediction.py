import streamlit as st
import requests
import pandas as pd

st.title("Country Sentiment Prediction")
df = pd.read_csv('./assets/safetycodes.csv')

sorted_countries = df['Country'].sort_values()
selected_country = st.selectbox("Country to Predict", sorted_countries)

if st.button("Get Prediction"):
    response = requests.get(f'http://localhost:4000/c/Prediction/{selected_country}')
    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Prediction for {selected_country}: {prediction['result']}")
    else:
        st.write("Ran into an error retrieving a prediction score -- try again")