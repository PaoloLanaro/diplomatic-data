# import streamlit as st
# import logging

# logger = logging.getLogger()
# import pandas as pd

# from modules.nav import SideBarLinks

# st.set_page_config(layout="wide")

# SideBarLinks()
# import requests

# st.title("Country Sentiment Prediction")
# df = pd.read_csv("./assets/safetycodes.csv")

# sorted_countries = df["Country"].sort_values()
# selected_country = st.selectbox("Country to Predict", sorted_countries)

# if st.button("Get Prediction"):
#     response = requests.get(f"http://api:4000/c/prediction/{selected_country}")
#     st.write("Response status code: ", response.status_code)
#     st.write("Response content: ", response.content)
#     if response.status_code == 200:
#         prediction = response.json()
#         st.write(f"Prediction for {selected_country}: {prediction['result']}")
#     else:
#         st.write("Ran into an error retrieving a prediction score -- try again")

import streamlit as st
import logging
import pandas as pd
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout="wide")

SideBarLinks()

st.title("Country Sentiment Prediction")
df = pd.read_csv("./assets/safetycodes.csv")

sorted_countries = df["Country"].sort_values()
selected_country = st.selectbox("Country to Predict", sorted_countries)

if st.button("Get Prediction"):
    response = requests.get(f"http://api:4000/c/prediction/{selected_country}")
    st.write("Response status code: ", response.status_code)
    st.write("Response content: ", response.content)
    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Prediction for {selected_country}: {prediction['result']}")
    else:
        st.write("Ran into an error retrieving a prediction score -- try again")

