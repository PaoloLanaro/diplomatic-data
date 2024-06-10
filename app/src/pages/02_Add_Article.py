import streamlit as st
import logging
import requests
from modules.nav import SideBarLinks
import random

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

# --------------- get countries w/o csv --------------------
# you will have to change anywhere on this page that has something like df["Country"].
# Don't forget to remove the import and line that does this
# Make a request to get a list of the countries. Will be returned as JSON
country_list = requests.get("http://api:4000/utils/countries/sorted_list")

# Create an actual list with all the countries
country_names = []
for row in country_list.json():
    country_names.append(row["country_name"])

# Log the list to confirm all countries are there
# logger.info(f'country_names: {country_names}')
# ----------------------------------------------------------

if "sorted_country_names_1" not in st.session_state:
    shuffled_country_names_1 = country_names[:]
    random.shuffle(shuffled_country_names_1)
    st.session_state.sorted_country_names_1 = shuffled_country_names_1

if "sorted_country_names_2" not in st.session_state:
    shuffled_country_names_2 = country_names[:]
    random.shuffle(shuffled_country_names_2)
    st.session_state.sorted_country_names_2 = shuffled_country_names_2


st.title("Hello! Please add your article information below and submit!")

publication_date = st.date_input("When did you write this?")
publication_time = st.time_input("What time did you write this?")


content = st.text_input(
    "Add all of the body text (the content) here",
    "Breaking news...",
    placeholder="Add all of the body text (the content) here",
)
country_written_about = st.selectbox(
    "What country are you writing about?", st.session_state.sorted_country_names_1
)
country_written_from = st.selectbox(
    "What country are you writing from?", st.session_state.sorted_country_names_2
)
url = st.text_input("What is the url of your article?")

st.write("")

if st.button("Add the article to Diplomatic Data Database!!", use_container_width=True):
    data = {
        "YYYY-MM-DD": str(publication_date),
        "HH:MM:SS": str(publication_time),
        "text": content,
        "country_written_about": country_written_about,
        "country_written_from": country_written_from,
        "url": url,
    }
    logger.info(f"Data to be sent: {data}")

    try:
        response = requests.post("http://api:4000/article/article_data", json=data)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        st.success("You have submitted your article!")
        logger.info("Article submitted successfully.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error submitting article: {e}")
        st.error(f"Ran into an error adding your article: {e}")
