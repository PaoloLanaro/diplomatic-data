import streamlit as st
import logging
import pandas as pd
import requests
import datetime
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

df = pd.DataFrame(pd.read_csv("./assets/safetycodes.csv"))

sorted_country_names = df["Country"].sort_values()

st.title("Hello! Please add your article information below and submit!")

st.text_area('Info about this page')

publication_date = st.date_input("When did you write this?")
publication_time = st.date_input("What time did you write this?")
publication_datetime = datetime.combine(publication_date, publication_time)

content = st.text_input("Add all of the body text (the content) here")
queried_country = st.selectbox("What country are you writing about?", sorted_country_names)
source_country = st.selectbox("What country are you writing from?", sorted_country_names)


if st.button("Add the article to World News Database!!"): 
    response = requests.get(f"http://api:4000/ad/prediction/{selected_country}")
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