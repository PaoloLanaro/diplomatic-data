import logging

logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title(f"Hello {st.session_state['first_name']}, Check out our ML model")
st.divider()

st.write("""This ML model is called a Random Forest Classifier. We ask that you provide the text of an article you 
         are interested in and the country your article is being written about. Using your information, our model
         will do its best to predict the article's source country (the country it is being written from).""")


country_list = requests.get('http://api:4000/utils/countries/sorted_list')

country_names = ["Russia", "China", "United States"]

col1, col2 = st.columns(2)

with col1:
    country = st.selectbox("Queried country ", country_names, index=None, placeholder='What country was the article written about?')

with col2:
    text = st.text_area("Article Text", 'Please add your text here', placeholder='Add the body of your article here.')

if st.button('Predict what country this has been written from', type='primary', use_container_width=True):
    predicted_country = requests.get(f'http://api:4000/models/prediction2/{text}/{country}')
    st.write(f'The predicted country this article is written from is the {predicted_country.json()[0]}!')
    st.write("Is this correct? If not, we may need to train this thing better....")

if st.button("Return to your personalized home", type="primary"):
    st.switch_page("pages/00_Foreign_Policy_Advisor.py")