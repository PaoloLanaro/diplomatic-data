import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

SideBarLinks(True)

st.write("# About Diplomatic Data")

st.markdown(
    """
    The purpose of the Diplomatic Data Web App is to analyze global perceptions of countries by examining sentiment 
    in news articles. By assessing the tone and sentiment of articles related to specific nations, our 
    goal is to identify and quantify media biases, thereby offering a deeper understanding of how these 
    biases shape international perceptions. The application employs sentiment analysis and linear regression 
    to generate insights valuable to a diverse array of stakeholders.

    For individual users, comprehending global perceptions of their country can enhance their awareness and 
    expectations when traveling abroad. This understanding can facilitate more informed interactions with 
    people from other nations, allowing individuals to address stereotypes and provide a more accurate 
    representation of their homeland.

    On a governmental scale, both local and international political leaders can leverage these insights to 
    improve diplomatic efforts and manage their international image. Recognizing the biases and preconceptions 
    held by other nations is crucial for effective diplomacy and media engagement.
    """
)

response = requests.get("http://api:4000/utils/coordinates")

latitude, longitude = [], []
for city in response.json():
    latitude.append(city["latitude"])
    longitude.append(city["longitude"])

city_df = pd.DataFrame({"latitude": latitude, "longitude": longitude})

st.map(city_df, zoom=1.2)

if st.session_state["authenticated"]:
    if st.button("Logout & Home", type="primary", use_container_width=True):
        del st.session_state["role"]
        del st.session_state["authenticated"]
        st.switch_page("Home.py")
