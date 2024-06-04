import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About World News")

st.markdown (
    """
    The purpose of the World News Web App is to analyze global perceptions of countries by examining sentiment 
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