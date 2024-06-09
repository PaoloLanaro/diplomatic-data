import logging

import requests

logger = logging.getLogger()
import pandas as pd
from datetime import datetime, timedelta, date
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

# get a random article from the database to display, and the next one to display. save these in a session_state
if "random_current_article" not in st.session_state:
    st.session_state["random_current_article"] = requests.get(
        "http://api:4000/article/random_article"
    ).json()
if "random_next_article" not in st.session_state:
    st.session_state["random_next_article"] = requests.get(
        "http://api:4000/article/random_article"
    ).json()

# get the article's json for displaying and accessing the data
random_article = st.session_state["random_current_article"]
random_article_title = requests.get(
    f"http://api:4000/article/title/{random_article['link']}"
)

# format the date from the table correctly
split_date = random_article["YYYY-MM-DD"].split("-")
corrected_date = split_date[1] + "-" + split_date[2] + "-" + split_date[0]

# display the article content -------------------------------------------------------------
if (
    random_article_title.status_code != 200
    or random_article_title.json()["title"] is None
):
    st.title("Read the article below!")
else:
    title_raw = random_article_title.json()["title"]
    title_split = title_raw.split(" | ")
    title_formatted = "\n### ".join(title_split)
    st.title(f"{title_formatted}")
st.divider()

st.write(f"#### Published Date: {corrected_date}")

st.write("### Article Content")
st.write(random_article["text"])

st.write(random_article["link"])
st.divider()

article_id = int(random_article["article_id"])
user_id = st.session_state["user_id"]

col1, col2, col3 = st.columns(3)
# --------------------------------------------------------------------------------------------

with col1:
    if st.button("Save Article", use_container_width=True, type="primary"):
        date_saved = str(datetime.now()).split(" ")
        data = {"article_id": article_id, "user_id": user_id, "date_saved": date_saved}
        response = requests.post("http://api:4000/s/user_saves", json=data)
        if response.status_code == 200:
            st.success("Article saved successfully!")
        else:
            st.error("Hey you, you can only save an article once!")

with col2:
    if st.button("Like Article", use_container_width=True, type="primary"):
        date_liked = str(datetime.now()).split(" ")
        data = {"article_id": article_id, "user_id": user_id, "date_liked": date_liked}
        response = requests.post("http://api:4000/s/user_likes", json=data)
        if response.status_code == 200:
            st.success("Article liked successfully!")
        else:
            st.error("Hey you, you can only like an article once!")

with col3:
    if st.button("Next Article", use_container_width=True, type="primary"):
        st.session_state["random_current_article"] = st.session_state[
            "random_next_article"
        ]
        del st.session_state["random_next_article"]
