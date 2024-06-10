import logging

logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title(f"{st.session_state['first_name']}'s Profile")
st.divider()

current_user_id = st.session_state["user_id"]


def get_title_to_url_dictionary(data):
    title_list = {}
    for row in data:
        logger.info(f"row = {type(row)}")
        url = row["url"]
        url_title = requests.get(f"http://api:4000/article/title/{url}")

        if url_title.status_code != 200:
            title_list[url] = url
        else:
            title_list[url_title.json()["title"]] = url

    return title_list


def display_dropdown(data, social_action):
    if response.status_code == 200:
        data = response.json()
        logger.info(f"recently_viewed data = {data}")

        title_dictionary = get_title_to_url_dictionary(data)

        title_selected = st.selectbox(social_action, title_dictionary.keys())
        st.write(title_dictionary[title_selected])

    else:
        st.write("No data yet....")


# the following three try except blocks will display the correct dropdowns and catch any exceptions
try:
    response = requests.get(f"http://api:4000/s/recently_viewed/{current_user_id}")
    logger.info(f"response code = {response.status_code}")
    logger.info(f"response = {response}")
    display_dropdown(response, "Recently Viewed")
except Exception as e:
    st.write(f"An error occurred: {e}")

try:
    response = requests.get(f"http://api:4000/s/likes/{current_user_id}")
    display_dropdown(response, "Liked")
except Exception as e:
    st.write(f"An error occurred: {e}")

try:
    response = requests.get(f"http://api:4000/s/saves/{current_user_id}")
    display_dropdown(response, "Saved")
except Exception as e:
    st.write(f"An error occurred: {e}")


st.divider()

# to fetch the trending article from the API
try:
    response = requests.get("http://api:4000/trending/trending_data")
    if response.status_code == 200:
        data = response.json()
        st.markdown("## Check out the most trendy article from this month!")
        st.write("")

        col1, col2 = st.columns(2)
        with col1:
            st.write("### Views in the Past Month")
            st.metric(label="", value=data["views_last_24_hours"])
        with col2:
            st.write("### Sentiment Score")
            st.metric(label="", value=data["sentiment"])

        st.markdown("## Read more:")
        st.write(data["content"])
    else:
        st.write("Could not find any trending articles :(")
except Exception as e:
    st.write(f"An error occurred: {e}")
