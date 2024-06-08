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

# 1st column: country dropdown and text input 
with col1:
    country = st.selectbox("Country to Predict", df["Country"])
    text = st.text_area("Article Text", "Placeholder")

# 2nd column: month slider and hour slider
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
with col2:
    month_name = st.select_slider('Month of Publishing', months)
    hour = st.slider('Hour of Publishing', 0, 23)

# convert the month_name value to the corresponding month number
month_as_num = months.index(month_name) + 1

if st.button('Calculate Sentiment', type='primary', use_container_width=True):
    sentiment = requests.get(f'http://api:4000/c/sentiment_prediction/{text}/{country}/{month_as_num}/{hour}')
    st.write('The information of the article you provided indicates that it has a sentiment score of {sentiment}.')
