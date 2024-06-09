import logging
logger = logging.getLogger()

import streamlit as st
from modules.home import Welcome
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# show correct sidebar links and welcome title text
SideBarLinks()
Welcome()

if st.button("View Your Profile", type="primary", use_container_width=True):
    st.switch_page("pages/01_Profile_View.py")

if st.button("Add an article to our database!", type="primary", use_container_width=True):
    st.switch_page("pages/02_Add_Article.py")

if st.button("View Articles based on your preferences!", type="primary", use_container_width=True):
    st.switch_page("pages/03_Foreign_Policy_Article_View.py")

