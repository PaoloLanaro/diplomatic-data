import logging
logger = logging.getLogger()
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"{st.session_state['first_name']}'s Profile")
st.divider()


try :
    response = requests.get("http://api:4000/s/")
    if response.status_code == 200:
        data = response.json()
        recently_viewed = data['recently_viewed']  # make sure to convert to a LIST
        st.selectbox("Recently Viewed", recently_viewed)
    else:
        st.write("Something went wrong....")
except Exception as e:
    st.write(f"An error occurred: {e}")

try :
    response = requests.get("http://api:4000/s/")
    if response.status_code == 200:
        data = response.json()
        liked = data['liked']  # make sure to convert to a LIST
        st.selectbox("Liked", liked)
    else:
        st.write("Something went wrong....")
except Exception as e:
    st.write(f"An error occurred: {e}")

try :
    response = requests.get("http://api:4000/s/")
    if response.status_code == 200:
        data = response.json()
        saved = data['saved']  # make sure to convert to a LIST
        st.selectbox("Saved", saved)
    else:
        st.write("Something went wrong....")
except Exception as e:
    st.write(f"An error occurred: {e}")



st.divider()

st.write('### Trending Articles')
st.divider()

# to fetch the trending article from the API 
try:
    response = requests.get("http://api:4000/trending/trending_data")  
    if response.status_code == 200:
        data = response.json()
        st.write('## Check out the most trendy article from this week!')
        st.markdown("---")
        st.write('### Numbers of view last 24 hours')
        st.write(data['views_last_24_hours'])
        st.write('### Sentiment')
        st.write(data['sentiment'])
        st.write('### Content:')
        st.write(data['content'])
    else:
        st.write("Could not find any trending articles :(")
except Exception as e:
    st.write(f"An error occurred: {e}")

if st.button("Return to your personalized home", type="primary"):
    st.switch_page("pages/00_Foreign_Policy_Advisor.py")
