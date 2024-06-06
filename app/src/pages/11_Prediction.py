import streamlit as st
import logging
import pandas as pd
import requests
from modules.nav import SideBarLinks

df = pd.read_csv("./assets/safetycodes.csv")

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Country Sentiment Prediction")

# making 2 columns for the general layout
col1, col2 = st.columns(2)


# 1st column: text input, country dropdown
with col1:
    country = st.selectbox("Country to Predict", df["Country"])
    text = st.text_input("Article Text")

# 2nd column: two sliders
with col2:
    month = st.slider('Month of Publishing', 0, 12)
    hour = st.slider('Hour of Publishing', 0, 24)


if st.button('Calculate Sentiment', type='primary', use_container_width=True):
    sentiment = requests.get(f'INSERT API CALL HERE') # TODO HERE
    st.write('The information of the article you provided indicates that it has a sentiment score of {sentiment}.')