import logging

import requests

logger = logging.getLogger()
import pandas as pd

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

random_article = requests.get('http://api:4000/article/random_article').json()

split_date = random_article['YYYY-MM-DD'].split('-')

corrected_date = split_date[1] + '-' + split_date[2] + '-' + split_date[0]

st.title("Article Title: Miami’s Little Haiti wasn’t a target for developers. Until the seas started to rise.")
st.divider()

st.write(f'#### Published Date: {corrected_date}')

st.write("### Article Content")
st.write(random_article['text'])

st.write(random_article['link'])
st.divider()

article_id = "1"
user_id = "2"
date_liked = "2024-06-05T12:00:00"
date_shared = "2024-06-05T12:00:00"
date_saved = "2024-06-05T12:00:00"

API_BASE_URL = "http://api:4000"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Save Article",
                 use_container_width=True):
        data = {"article_id": article_id, "user_id": user_id, "date_saved": date_saved}
        st.write("Sending data to /s/saves:", data)
        response = requests.post(f"{API_BASE_URL}/s/saves", json=data)
        st.write("Response status code:", response.status_code)
        st.write("Response content:", response.content)
        if response.status_code == 200:
            st.success("Article saved successfully!")
        else:
            st.error(f"Failed to save article. Status code: {response.status_code}")

with col2:
    if st.button("Like Article",
                 use_container_width=True):
        data = {"article_id": article_id, "user_id": user_id, "date_liked": date_liked}
        response = requests.post(f"{API_BASE_URL}/s/likes", json=data)
        if response.status_code == 200:
            st.success("Article liked successfully!")
        else:
            st.error("Failed to like article.")

with col3:
    if st.button("Next Article",
                 use_container_width=True):
        data = {
            "article_id": article_id,
            "user_id": user_id,
            "date_shared": date_shared,
        }
        response = requests.post(f"{API_BASE_URL}/s/shares", json=data)
        if response.status_code == 200:
            st.success("Article shared successfully!")
        else:
            st.error("Failed to share article.")
