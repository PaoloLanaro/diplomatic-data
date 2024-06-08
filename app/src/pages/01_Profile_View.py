import logging
logger = logging.getLogger()
import pandas as pd

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"{st.session_state['first_name']}'s Profile")
st.divider()

list = ['article1', 'article2', 'article3']
st.selectbox("Recently Viewed", list)
st.selectbox("Liked Articles", list)
st.selectbox("Saved Articles", list)
st.selectbox("Shared Articles", list)

st.divider()

st.write('### Trending Articles')
st.divider()

st.write('')
st.write('')
st.write('')
st.write('')


if st.button("Return to your personalized home", type="primary"):
    st.switch_page("pages/00_Foreign_Policy_Advisor.py")
