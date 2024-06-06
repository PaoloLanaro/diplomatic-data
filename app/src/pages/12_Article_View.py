import logging

import requests

logger = logging.getLogger()
import pandas as pd

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title(
    "Article Title: Miami’s Little Haiti wasn’t a target for developers. Until the seas started to rise."
)
st.divider()

st.markdown(
    f"<p style='font-size:24px;'>Published Date: 07-12-2019", unsafe_allow_html=True
)
# st.markdown(
#     f"<p style='font-size:24px;'>Sentiment Score: {st.session_state['sentiment_score']}</p>",
#     unsafe_allow_html=True,
# )
# st.markdown(
#     f"<p style='font-size:24px;'>News Source: {st.session_state['source_name']}</p>",
#     unsafe_allow_html=True,
# )

st.write("### Article Summary")
st.write("In the article \"Miami’s Little Haiti wasn’t a target for developers. Until the seas started to rise,\" published on July 12, 2019, the authors explore the evolving landscape of Miami's Little Haiti neighborhood in the face of rising sea levels. Initially overlooked by developers, the area has become increasingly sought after due to its relatively higher elevation compared to other parts of the city. As climate change exacerbates flooding concerns, developers are now eyeing Little Haiti for its potential as a safer investment, sparking debates about gentrification and community preservation.")
st.divider()

st.markdown(
    """
    <style>
    .stButton>button {
        width: 150px; 
        height: 50px; 
        font-size: 20px; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

article_id = "1"
user_id = "2"
date_liked  = "2024-06-05T12:00:00"
date_shared = "2024-06-05T12:00:00"
date_saved  = "2024-06-05T12:00:00"

API_BASE_URL = "http://api:4000"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Save"): 
        data = {
            "article_id": article_id,
            "user_id": user_id,
            "date_saved": date_saved
        }
        st.write("Sending data to /s/saves:", data)
        response = requests.post(f"{API_BASE_URL}/s/saves", json=data)
        st.write("Response status code:", response.status_code)
        st.write("Response content:", response.content)
        if response.status_code == 200:
            st.success("Article saved successfully!")
        else:
            st.error(f"Failed to save article. Status code: {response.status_code}")
        
with col2:
    if st.button("Like"):
        data = {
            "article_id": article_id,
            "user_id": user_id,
            "date_liked": date_liked
        }
        response = requests.post(f"{API_BASE_URL}/s/likes", json=data)
        if response.status_code == 200:
            st.success("Article liked successfully!")
        else:
            st.error("Failed to like article.")

with col3:
    if st.button("Share"):
        data = {
            "article_id": article_id,
            "user_id": user_id,
            "date_shared": date_shared
        }
        response = requests.post(f"{API_BASE_URL}/s/shares", json=data)
        if response.status_code == 200:
            st.success("Article shared successfully!")
        else:
            st.error("Failed to share article.")
