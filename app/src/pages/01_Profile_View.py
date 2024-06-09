import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"{st.session_state['first_name']}'s Profile")
st.divider()

try :
    response = requests.get(f"http://api:4000/s/recently_viewed/{st.session_state['user_id']}")
    logger.info(f'response code = {response.status_code}')
    logger.info(f'response = {response}')
    if response.status_code == 200:
        data = response.json()
        logger.info(f'recently_viewed data = {data}')
        url_list = []
        for row in data:
            logger.info(f'row = {type(row)}')
            url_list.append(row['url'])
        st.selectbox("Recently Viewed", url_list)
    else:
        st.write("No data yet....")
except Exception as e:
    st.write(f"An error occurred: {e}")

try :
    response = requests.get(f"http://api:4000/s/likes/{st.session_state['user_id']}")
    if response.status_code == 200:
        data = response.json()
        url_list = []
        for row in data:
            url_list.append(row['url'])
        st.selectbox("Liked", url_list)
    else:
        st.write("No data yet....")
except Exception as e:
    st.write(f"An error occurred: {e}")

try :
    response = requests.get(f"http://api:4000/s/saves/{st.session_state['user_id']}")
    if response.status_code == 200:
        data = response.json()
        logger.info(f'saves select data = {data}')
        url_list = []
        for row in data:
            url_list.append(row['url'])
        logger.info(f'url_list = {url_list}')
        st.selectbox("Saved", url_list)
    else:
        st.write("No data yet....")
except Exception as e:
    st.write(f"An error occurred: {e}")


st.divider()

# to fetch the trending article from the API 
try:
    response = requests.get("http://api:4000/trending/trending_data")  
    if response.status_code == 200:
        data = response.json()
        st.write('## Check out the most trendy article from this week!')
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
