import streamlit as st
import logging
import pandas as pd
import requests
from datetime import datetime, date, time
from modules.nav import SideBarLinks
import random 

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

df = pd.DataFrame(pd.read_csv("./assets/safetycodes.csv"))

sorted_country_names = df["Country"].sort_values().tolist()

if 'sorted_country_names_1' not in st.session_state:
    shuffled_country_names_1 = sorted_country_names[:]
    random.shuffle(shuffled_country_names_1)
    st.session_state.sorted_country_names_1 = shuffled_country_names_1

if 'sorted_country_names_2' not in st.session_state:
    shuffled_country_names_2 = sorted_country_names[:]
    random.shuffle(shuffled_country_names_2)
    st.session_state.sorted_country_names_2 = shuffled_country_names_2


st.title("Hello! Please add your article information below and submit!")

publication_date = st.date_input("When did you write this?")
publication_time = st.time_input("What time did you write this?")


content = st.text_input("Add all of the body text (the content) here", 'Breaking news...')
country_written_about = st.selectbox("What country are you writing about?", st.session_state.sorted_country_names_1)
country_written_from = st.selectbox("What country are you writing from?", st.session_state.sorted_country_names_2)
url = st.text_input("What is the url of your article?")


if st.button("Add the article to World News Database!!"): 
    data = {
            'YYYY-MM-DD': str(publication_date), 
            'HH:MM:SS': str(publication_time), 
            'text': content,
            'country_written_about': country_written_about,
            'country_written_from': country_written_from, 
            'url': url
    }
    logger.info(f"Data to be sent: {data}")

    try:
        response = requests.post("http://api:4000/article/article_data", json=data)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        st.write("You have submitted your article!")
        logger.info("Article submitted successfully.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error submitting article: {e}")
        st.error(f"Ran into an error adding your article: {e}")
