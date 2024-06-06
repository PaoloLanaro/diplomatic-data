import streamlit as st
import logging
import pandas as pd
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Country Sentiment Prediction")
df = pd.read_csv("./assets/safetycodes.csv")

st.write("Please enter your country of interest below.")

sorted_countries = df["Country"].sort_values()
selected_country = st.selectbox("Country to Predict", sorted_countries)

if st.button("Get Prediction"):
    response = requests.get(f"http://api:4000/c/prediction/{selected_country}")
    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Prediction for {selected_country}: {prediction}")
        st.write("The above score is the sentiment analysis for your country of interest!")
        if (response.json() > 0):
            st.write("Your country has a positive sentiment score meaning people think positively about it!")
        else:
            st.write("Your country has a negative sentiment score meaning people think poorly about it :(")
    else:
        st.write("Ran into an error retrieving a prediction score -- try again")    

