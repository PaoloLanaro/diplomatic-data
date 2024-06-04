import logging
logger = logging.getLogger()
import pandas as pd

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Article Title: Miami’s Little Haiti wasn’t a target for developers. Until the seas started to rise.')
st.divider()
import streamlit as st
st.markdown(f"<p style='font-size:24px;'>Published Date: 07-12-2019" , unsafe_allow_html=True)
st.markdown(f"<p style='font-size:24px;'>Sentiment Score: {st.session_state['sentiment_score']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size:24px;'>News Source: {st.session_state['source_name']}</p>", unsafe_allow_html=True)

st.write('### Article Summary')
st.write('summary')
st.divider()

st.markdown("""
    <style>
    .stButton>button {
        width: 150px; 
        height: 50px; 
        font-size: 20px; 
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.button('Save')

with col2:
    st.button('Like')

with col3:
    st.button('Share')
