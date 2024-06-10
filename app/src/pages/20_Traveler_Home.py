import streamlit as st
from modules.home import Welcome
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

# show correct sidebar links and welcome title text
SideBarLinks()
Welcome()

if st.button("Configure your preferences", type="primary", use_container_width=True):
    st.session_state["authenticated"] = True
    st.switch_page("pages/21_User_Preferences.py")

if st.button("Search for articles", type="primary", use_container_width=True):
    st.switch_page("pages/22_Traveler_Search.py")
