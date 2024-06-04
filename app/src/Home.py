import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

st.title('World News')

st.write('\n\n')
st.write('### Hello, which user would you like to login as?')

if st.button("Anton Müller, a Foreign Policy Advisor at the EU", 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'foriegn_policy_advisor'
    st.session_state['first_name'] = 'Anton'
    st.switch_page('pages/00_Foreign_Policy_Advisor.py')

if st.button('Katerina Stepanov, a PR Specialist at Gazprom Oil', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'pr_specialist'
    st.session_state['first_name'] = 'Katerina'
    st.switch_page('pages/01_Pr_Specialist.py')

if st.button('Monika José, an unemployed traveler', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Unemployed Traveler'
    st.session_state['first_name'] = 'Monika'
    st.switch_page('pages/02_Traveler.py')