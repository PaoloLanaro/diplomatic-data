import streamlit as st
import logging
import pandas as pd
import requests
from datetime import datetime, date, time
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

df = pd.DataFrame(pd.read_csv("./assets/safetycodes.csv"))

sorted_country_names = df["Country"].sort_values()

st.title("Hello! Please add your article information below and submit!")

# what's the difference between this and other st.text_input? we aren't using this for data... why do we have it?
st.text_area('Info about this page')

publication_date = st.date_input("When did you write this?")
publication_time = st.time_input("What time did you write this?")

# would have liked to combine into datetime at once and send in JSON post request, but datetime, dates, and time
# data types are not JSON serializable. This means we package each individually and then unpack them at the endpoint
# publication_datetime = datetime.combine(publication_date, publication_time)

content = st.text_input("Add all of the body text (the content) here", 'Include auto filled text here to do sentiment analysis on without having to actually input')
queried_country = st.selectbox("What country are you writing about?", sorted_country_names)
source_country = st.selectbox("What country are you writing from?", sorted_country_names)


if st.button("Add the article to World News Database!!"): 
    data = {
            'YYYY-MM-DD': str(publication_date), 
            'HH:MM:SS': str(publication_time), 
            'text': content,
            'article_country': queried_country,
            'query_country': source_country,
            'url': 'google.com'
    }
    response = requests.post("http://api:4000/article/article_data", json=data)
    if response.status_code == 200:
        prediction = response.json()
        st.write("The above score is the sentiment analysis for your country of interest!")
        if (response.json() > 0):
            st.write("Your country has a positive sentiment score meaning people think positively about it!")
        else:
            st.write("Your country has a negative sentiment score meaning people think poorly about it :(")
    else:
        st.write("Ran into an error retrieving a prediction score -- try again")
