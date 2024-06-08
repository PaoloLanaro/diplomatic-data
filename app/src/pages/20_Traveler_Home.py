import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Traveler, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Configure your preferences', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.switch_page('pages/21_User_Preferences.py')

if st.button('Search for articles',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/22_Traveler_Search.py')

