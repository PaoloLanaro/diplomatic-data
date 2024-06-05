import streamlit as st
import requests

st.title("Country Sentiment Prediction")
country = st.text_input("Enter a country name")

if st.button("Get Prediction"):
    response = requests.get(f'http://localhost:4000/c/Prediction/{country}')
    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Prediction for {country}: {prediction['result']}")
    else:
        st.write("Ran into an error retrieving a prediction score -- try again")