import logging
logger = logging.getLogger()

import streamlit as st
from modules.home import Welcome
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# show correct sidebar links and welcome title text
SideBarLinks()
Welcome()

# switch to predictions page
if st.button(
    "View a Country Sentiment Score!", type="primary", use_container_width=True
):
    st.switch_page("pages/11_Prediction.py")

# switch to article view page
if st.button("View an Article!", type="primary", use_container_width=True):
    st.switch_page("pages/12_Article_View.py")
