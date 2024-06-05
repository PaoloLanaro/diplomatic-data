import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome PR Specialist, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View a Country Sentiment Score!',
             type = 'primary',
             use_container_width=True):
             st.session_state['authenticated']=True
             st.session_state['first_name'] = 'Katerina',
             st.session_state['last_name'] = 'Stepanov',
             st.switch_page('pages/011_Predication.py')

if st.button('View an Article!', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['first_name'] = 'Katerina'
    st.session_state['last_name'] = 'Stepanov'
    st.session_state['sentiment_score'] = '.86'
    st.session_state['source_name'] = 'CNN'
    st.switch_page('pages/09_Article_View.py')
