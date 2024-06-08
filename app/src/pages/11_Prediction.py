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
country_list = requests.get('http://api:4000/country/sorted_list')

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
    country = st.selectbox("Country to Predict", country_names, index=None, placeholder='Select a Country')
    text = st.text_area("Article Text", 'Please add your text here', placeholder='Please add your text here')

with col2:
    country_query = st.selectbox("Country of Article's Intention", ['Russia', 'China', 'Belgium', 'United States']) # TODO make the 5 options the ones in the training set

text = st.text_area("Article Text", "Placeholder")

if st.button('Calculate Sentiment', type='primary', use_container_width=True):
    sentiment = requests.get(f'http://api:4000/models/prediction1/{text}/{country}/{month_as_num}/{hour}')
    st.write('The information of the article you provided indicates that it has a sentiment score of {sentiment}.')
