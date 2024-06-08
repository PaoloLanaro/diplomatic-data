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
    month = st.slider('Month of Publishing', 1, 12)
    hour = st.slider('Hour of Publishing', 0, 23)

if st.button('Calculate Sentiment', type='primary', use_container_width=True):
    sentiment_calc, sentiment_real = requests.get(f'http://api:4000/c/sentiment_prediction/{text}/{country}/{month}/{hour}')
    st.write(f'The information of the article you provided indicates that it has a sentiment score of {sentiment_calc} based on our calculations.')
    st.write(f'The actual sentiment calculated from the article\'s text is {sentiment_real}')