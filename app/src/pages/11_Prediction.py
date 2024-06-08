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

# 2 columns for the two dropboxes
col1, col2 = st.columns(2)

with col1: 
    country_origin = st.selectbox("Country of Article's Origin", df["Country"])

with col2:
    country_query = st.selectbox("Country of Article's Intention", ['Russia', 'China', 'Belgium', 'United States']) # TODO make the 5 options the ones in the training set

text = st.text_area("Article Text", "Placeholder")

if st.button('Calculate Sentiment', type='primary', use_container_width=True):
    sentiment_calc, sentiment_real = requests.get(f'http://api:4000/models/prediction1/{text}/{country_origin}/{country_query}')
    st.write(f'The information of the article you provided indicates that it has a sentiment score of {sentiment_calc} based on our calculations.')
    st.write(f'The actual sentiment calculated from the article\'s text is {sentiment_real}.')