import streamlit as st
import logging
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")
SideBarLinks()

st.title("Country Sentiment Prediction")

# --------------- get countries w/o csv --------------------
# you will have to change anywhere on this page that has something like df["Country"].
# Don't forget to remove the import and line that does this
# Make a request to get a list of the countries. Will be returned as JSON
country_list = requests.get('http://api:4000/utils/countries/sorted_list')

# Create an actual list with all the countries
country_names = []
for row in country_list.json():
    country_names.append(row['country_name'])

# Log the list to confirm all countries are there
# logger.info(f'country_names: {country_names}')
# ----------------------------------------------------------

# making 2 columns for the general layout
col1, col2 = st.columns(2)

# 1st column: country dropdown and text input 
with col1:
    country = st.selectbox("Country to Predict", country_names, index=None, placeholder='Where was the article written?')

# 2nd column: month slider and hour slider
with col2:
    text = st.text_area("Article Text", 'Please add your text here', placeholder='Add the body of your article here.')


if st.button('Calculate Sentiment', type='primary', use_container_width=True):
    sentiment = requests.get(f'http://api:4000/models/prediction1/{text}/{country}')
    st.write(f'The information of the article you provided indicates that it has a sentiment score of {sentiment.json()["sentiment_guess"]} with an actual sentiment score of {sentiment.json()["sentiment_actual"]}.')
