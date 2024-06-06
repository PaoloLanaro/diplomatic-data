import logging

logger = logging.getLogger()
import pandas as pd

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Profile Information")
st.divider()

st.markdown(
    f"<p style='font-size:24px;'>First Name: {st.session_state['first_name']}</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p style='font-size:24px;'>Last Name: {st.session_state['last_name']}</p>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p style='font-size:24px;'>Job Description: {st.session_state['role']}</p>",
    unsafe_allow_html=True,
)

st.write("### User Preferences")
st.divider()

st.date_input("Preferred Timeline")

df = pd.DataFrame(pd.read_csv("./assets/safetycodes.csv"))

sorted_country_names = df["Country"].sort_values()

st.selectbox("News Subject Country", sorted_country_names)
st.selectbox("News Source Country", sorted_country_names)

st.write("")
st.button("Restore Defaults")
